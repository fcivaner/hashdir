import hashlib
import imohash


def hash_file_imohash(filepath):
    return imohash.hashfile(filepath, hexdigest=True)


def hash_file_md5(filepath):
    hash_obj = hashlib.md5()
    return hash_file_hashlib(filepath, hash_obj)


def hash_file_sha1(filepath):
    hash_obj = hashlib.sha1()
    return hash_file_hashlib(filepath, hash_obj)


def hash_file_hashlib(filepath, hash_obj):
    READ_CHUNK_SIZE = 4096
    with open(filepath, "rb") as f:
        while 1:
            buf = f.read(READ_CHUNK_SIZE)
            if not buf:
                break
            hash_obj.update(hashlib.md5(buf).hexdigest().encode())
    return hash_obj.hexdigest()


def hash_string_md5(input_str):
    h = hashlib.md5()
    h.update(input_str.encode())
    return h.hexdigest()
