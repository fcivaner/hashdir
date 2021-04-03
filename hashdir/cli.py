import argparse
import logging
import os

from hashdir import __version__, description, name


def get_parser():
    parser = argparse.ArgumentParser(prog=name, description=description)

    parser.add_argument("directory", nargs="?", default=".")

    parser.add_argument(
        "-a",
        "--algorithm",
        choices=["md5", "sha1", "imohash"],
        default="md5",
        help="the hashing algorithm for files. warning: imohash is a constant-time hashing library, "
        "and while being fast for large files, it produces approximate results.",
    )

    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="exclude a pattern, like .git/* or *.log",
    )

    parser.add_argument(
        "--log-level",
        choices=["error", "info", "debug"],
        default="info",
        help="set the logging level.",
    )

    parser.add_argument(
        "-v", "--version", action="version", version="{} {}".format(name, __version__)
    )

    return parser


def parse_args(args):
    argument_parser = get_parser()
    args = argument_parser.parse_args(args)
    valid = validate_args(args)
    if valid:
        return args
    else:
        return None


def validate_args(args):
    if not os.path.isdir(args.directory):
        logging.error("%s is not a directory.", args.directory)
        return False
    return True
