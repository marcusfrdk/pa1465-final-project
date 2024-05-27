""" Main module for the main program. """

import sys
from argparse import ArgumentParser, Namespace
from versions import main as test_versions


def get_args() -> Namespace:
  """ Returns the parsed arguments. """
  parser = ArgumentParser()
  parser.add_argument(
      "-v",
      "--versions",
      help="test different versions of Python",
      action="store_true"
  )
  parser.add_argument(
      "-os",
      "--operating-systems",
      help="test different operating systems", action="store_true"
  )
  return parser.parse_args()


def main() -> int:
  """ Entrypoint for the main module of the main program. """
  args = get_args()

  if args.versions:
    test_versions()

  return 0


if __name__ == "__main__":
  sys.exit(main())
