import argparse

from typing import Optional
from typing import Sequence

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

    # return find_large_added_files(
    #     args.filenames,
    #     args.maxkb,
    #     enforce_all=args.enforce_all,
    # )

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
