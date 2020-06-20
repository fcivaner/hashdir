import argparse
import logging
import os


def get_parser():
    parser = argparse.ArgumentParser(description="hashdir")

    parser.add_argument("directory", nargs="?", default=".")

    parser.add_argument(
        "-a",
        "--algorithm",
        choices=["md5", "sha1", "imohash"],
        default="md5",
        help="warning: imohash is a constant-time hashing library, "
        "and while being fast for large files, it produces approximate results.",
    )

    parser.add_argument(
        "--log-level", choices=["error", "info", "debug"], default="info"
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
