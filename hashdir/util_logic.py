import os
import fnmatch
from .util_hash import hash_file_imohash, hash_file_md5, hash_file_sha1, hash_string_md5


def is_excluded(file_path, patterns):
    if file_path[0:2] == "./":
        file_path = file_path[2:]
    for pattern in patterns:
        if fnmatch.fnmatch(file_path, pattern):
            return True
    return False


def get_files(directory, excluded):
    os.chdir(directory)
    for root, dirs, files in os.walk("."):
        for name in files:
            file_path = os.path.join(root, name)
            if not is_excluded(file_path, excluded):
                yield file_path


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


def hashdir(args):
    files = list(get_files(args.directory, args.exclude))
    hash_func = get_hash_func(args)
    file_hashes = hash_files(files, hash_func)
    hash_string = generate_hash_string(file_hashes)

    result = hash_string_md5(hash_string)
    return (hash_string, result)
