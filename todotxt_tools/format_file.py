import argparse

from typing import Optional
from typing import Sequence

from .add_task_uuids import add_task_uuids
from .add_task_creation_dates import add_task_creation_dates
from .add_task_completion_dates import add_task_completion_dates

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        '--enforce-all', action='store_true',
        help='Enforce all files are checked, not just staged files.',
    )
    args = parser.parse_args(argv)

    changed = False
    for filename in args.filenames:
        if add_task_uuids(filename):
            changed = True
        if add_task_creation_dates(filename):
            changed = True
        if add_task_completion_dates(filename):
            changed = True

    if changed:
        return 1
    else:
        return 0

if __name__ == '__main__':
    raise SystemExit(main())
