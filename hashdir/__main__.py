#!/usr/bin/env python3
import os
import sys
import traceback
import logging
from . import util_logging, cli
from .util_hash import hash_file_imohash, hash_file_md5, hash_file_sha1, hash_string_md5


def get_files(directory):
    os.chdir(directory)
    for root, dirs, files in os.walk("."):
        for name in files:
            filepath = os.path.join(root, name)
            yield filepath


def hash_files(files, hash_func):
    files = sorted(files)
    for f in files:
        file_hash = hash_func(f)
        yield (f, file_hash)


def get_hash_func(args):
    if args.algorithm == "md5":
        return hash_file_md5
    elif args.algorithm == "sha1":
        return hash_file_sha1
    elif args.algorithm == "imohash":
        return hash_file_imohash


def generate_hash_string(file_hashes):
    hash_string = ""
    for fh in file_hashes:
        hash_string += "{} {}\n".format(fh[0], fh[1])
    return hash_string


def run(args):
    logger = util_logging.adjust_logger()

    args = cli.parse_args(args)
    if not args:
        return

    logger.setLevel(util_logging.get_log_level(args.log_level))

    files = list(get_files(args.directory))
    hash_func = get_hash_func(args)
    file_hashes = hash_files(files, hash_func)
    hash_string = generate_hash_string(file_hashes)

    print(hash_string)
    result = hash_string_md5(hash_string)
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
        logging.debug(traceback.extract_stack()[0])
        exit_code = EXIT_CODE_ERROR
    sys.stdout.flush()
    exit(exit_code)


if __name__ == "__main__":
    main()
