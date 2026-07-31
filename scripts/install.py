#!/usr/bin/env python3
"""Install the project-context-bootstrap skill without third-party dependencies."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
from pathlib import Path


SKILL_NAME = "project-context-bootstrap"
REQUIRED_PATHS = (
    Path("SKILL.md"),
    Path("LICENSE.txt"),
    Path("agents/openai.yaml"),
    Path("references/kernel-principles.md"),
    Path("references/bootstrap-contract.md"),
)


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def source_skill() -> Path:
    return repository_root() / "skills" / SKILL_NAME


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install the Agent Context Kernel bootstrap skill."
    )
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument(
        "--project",
        nargs="?",
        const=".",
        metavar="PATH",
        help="install under PATH/.agents/skills; defaults to the current directory",
    )
    scope.add_argument(
        "--user",
        action="store_true",
        help="install under $HOME/.agents/skills (the default)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace an existing installation after staging the new copy",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show the resolved source and destination without writing files",
    )
    return parser.parse_args(argv)


def resolve_destination(args: argparse.Namespace) -> Path:
    if args.project is not None:
        root = Path(args.project).expanduser().resolve()
        return root / ".agents" / "skills" / SKILL_NAME
    return Path.home() / ".agents" / "skills" / SKILL_NAME


def validate_source(source: Path) -> None:
    missing = [path.as_posix() for path in REQUIRED_PATHS if not (source / path).is_file()]
    if missing:
        joined = ", ".join(missing)
        raise RuntimeError(f"source skill is incomplete: {joined}")


def install(source: Path, destination: Path, *, force: bool, dry_run: bool) -> None:
    validate_source(source)
    print(f"source:      {source}")
    print(f"destination: {destination}")

    if dry_run:
        print("dry run: no files changed")
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and not force:
        raise FileExistsError(
            f"installation already exists at {destination}; rerun with --force to replace it"
        )

    staging_root = Path(
        tempfile.mkdtemp(prefix=f".{SKILL_NAME}-", dir=destination.parent)
    )
    staged_skill = staging_root / SKILL_NAME
    backup: Path | None = None

    try:
        shutil.copytree(source, staged_skill)
        validate_source(staged_skill)

        if destination.exists():
            backup = destination.with_name(
                f".{destination.name}.backup-{os.getpid()}"
            )
            if backup.exists():
                shutil.rmtree(backup)
            destination.rename(backup)

        staged_skill.rename(destination)

        if backup is not None:
            shutil.rmtree(backup)
    except Exception:
        if destination.exists() and backup is not None and backup.exists():
            shutil.rmtree(destination)
        if backup is not None and backup.exists():
            backup.rename(destination)
        raise
    finally:
        if staging_root.exists():
            shutil.rmtree(staging_root)

    print(f"installed {SKILL_NAME}")
    print("restart the coding agent so it discovers the installed skill")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        install(
            source_skill(),
            resolve_destination(args),
            force=args.force,
            dry_run=args.dry_run,
        )
    except (FileExistsError, RuntimeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
