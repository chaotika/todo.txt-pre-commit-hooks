import argparse

from typing import Optional
from typing import Sequence

import pytodotxt
import datetime

def add_task_creation_dates(todotxt_filename):
    print(todotxt_filename)

    todotxt = pytodotxt.TodoTxt(todotxt_filename)
    todotxt.parse()

    today = datetime.date.today()

    for task in todotxt.tasks:
        if not task.creation_date:
            task.creation_date = today

    todotxt.save()

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
        if add_task_creation_dates(filename):
            changed = True

    if changed:
        return 1
    else:
        return 0

if __name__ == '__main__':
    raise SystemExit(main())
