# hashdir

A command line tool to calculate hash of directory trees using various hash algorithms.

## Installing

To install, run the following command in your terminal:

```pip3 install hashdir```

## Installing on Android

You may want to install hashdir through Termux or similar on android to check hashes of directories on your android system.

On some systems, you may have to reinstall python to get development libraries, and install libcrypt before installing hashdir for the installation to work:

```bash
apt install python
apt install libcrypt
```

Otherwise, installation on android is the same as others.

```pip3 install hashdir```

## Usage

```text
usage: hashdir [-h] [-a {md5,sha1,imohash}] [--log-level {error,info,debug}]
               [-v]
               [directory]

A command line tool to calculate hashes of directory trees using various hash
algorithms.

positional arguments:
  directory

optional arguments:
  -h, --help            show this help message and exit
  -a {md5,sha1,imohash}, --algorithm {md5,sha1,imohash}
                        warning: imohash is a constant-time hashing library,
                        and while being fast for large files, it produces
                        approximate results.
  --log-level {error,info,debug}
  -v, --version         show program's version number and exit
```

## Algorithm

Hashdir performs the following steps;

- Walk the directory tree and find all file paths.
- Sort file paths to get a consistent hash for every system.
- Compute the hash value for each file separately using the algorithm selected by the -a option (Or md5 as default).
- Create a "hash string" using the results. Hash string is a string value which consists of a file path and its hash separated by a space character on each line. Print the hash string.
- Compute the md5 hash value of the hash string, and print it as the result.

## Contributing

Contributions are welcome! Please use black for formatting code before sending a PR.
