# py standard lib usecase

The lossless compression algorithm uses the time it takes to compress or decompress data in exchange for the space required to store the data to make up for the lack of storage capacity. Python provides interfaces for some of the most popular compression libraries, so that different compression libraries can be used alternately to read and write files.

Zlib and gzip provide the GNU zip library, and bz2 allows access to the updated bzip2 format. These formats all deal with the data stream regardless of the input format, and provide an interface to transparently read and write compressed files. You can use these modules to compress individual files or data sources.

The standard library also includes some modules to manage the archive format, merge multiple files into one file, and manage it as a unit. tarfile reads and writes UNIX tape archive format, which is a standard, but it is still widely used because of its flexibility. zipfile processes archives according to the zip format. This format is popularized by the PC program PKZIP. It was originally used under MS-DOS and Windows. However, due to the simplicity of its API and the portability of this format, it is now also used on other platforms. .

## zlib

