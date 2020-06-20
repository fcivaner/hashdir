# hashdir

A command line tool to calculate hash of directory trees using various hash algorithms.

## installation

To install run the following command in your terminal:

```pip3 install hashdir```

## usage

```text
usage: hashdir [-h] [-a {md5,sha1,imohash}] [--log-level {error,info,debug}]
               [directory]

hashdir

positional arguments:
  directory

optional arguments:
  -h, --help            show this help message and exit
  -a {md5,sha1,imohash}, --algorithm {md5,sha1,imohash}
                        warning: imohash is a constant-time hashing library,
                        and while being fast for large files, it produces
                        approximate results.
  --log-level {error,info,debug}
```

## algorithm

Hashdir performs the following steps;

- Walk the directory tree and find all file paths.
- Sort file paths to get a consistent hash for every system.
- Compute the hash value for each file separately using the algorithm selected by the -a option (Or md5 as default).
- Create a "hash string" using the results. Hash string is a string value which consists of a file path and its hash separated by a space character on each line. Print the hash string.
- Compute the md5 hash value of the hash string and return as the result.

## contributing

Contributions are welcome! Please use black for formatting code before sending a PR.
