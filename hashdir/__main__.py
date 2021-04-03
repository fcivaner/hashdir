#!/usr/bin/env python3
import sys
import traceback
import logging
from . import util_logging, cli
from .util_logic import hashdir


def run(args):
    logger = util_logging.adjust_logger()

    args = cli.parse_args(args)
    if not args:
        return

    logger.setLevel(util_logging.get_log_level(args.log_level))

    (hash_string, result) = hashdir(args)

    print(hash_string)
    print(result)


def main():
    EXIT_CODE_ERROR = 127
    args = sys.argv[1:]
    exit_code = 0
    try:
        run(args)
    except KeyboardInterrupt:
        logging.error("Terminated on user input.")
        exit_code = EXIT_CODE_ERROR
    except Exception as e:
        logging.error(
            "An unknown error have occurred: %s"
            ". Use '--log-level debug' to see details.",
            e,
        )
        logging.debug(traceback.format_exc())
        exit_code = EXIT_CODE_ERROR
    sys.stdout.flush()
    exit(exit_code)


if __name__ == "__main__":
    main()
