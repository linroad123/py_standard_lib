# py standard lib usecase

The lossless compression algorithm uses the time it takes to compress or decompress data in exchange for the space required to store the data to make up for the lack of storage capacity. Python provides interfaces for some of the most popular compression libraries, so that different compression libraries can be used alternately to read and write files.

Zlib and gzip provide the GNU zip library, and bz2 allows access to the updated bzip2 format. These formats all deal with the data stream regardless of the input format, and provide an interface to transparently read and write compressed files. You can use these modules to compress individual files or data sources.

The standard library also includes some modules to manage the archive format, merge multiple files into one file, and manage it as a unit. tarfile reads and writes UNIX tape archive format, which is a standard, but it is still widely used because of its flexibility. zipfile processes archives according to the zip format. This format is popularized by the PC program PKZIP. It was originally used under MS-DOS and Windows. However, due to the simplicity of its API and the portability of this format, it is now also used on other platforms. 

zlib: Provide support for "zlib" compression. (This compression method is "deflate".).

gzip: used to read and write compressed files in gzip format.

zipfile: can be used to read and write ZIP format.

hashlib: Generate password hashes and message digests.

hmac: implements password hashing to complete message authentication.

## zlib

This in-memory compression method has some disadvantages. The main reason is that the system needs enough memory to be able to reside both uncompressed and compressed versions in memory, so it is not practical for real-world use cases. Another method is to use Compress and Decompress objects to process data incrementally, so that the entire data set does not need to be placed in memory.

Read small data blocks from a plain text file and pass them to compress(). The compressor maintains an internal buffer of compressed data. Since the compression algorithm relies on checksum and minimum block size, the compressor may not be ready to return data every time it receives more input. If it does not prepare a complete compressed block, it will return an empty string.

In addition to the compression and decompression functions, zlib also includes two functions to calculate the checksum of the data, namely adler32() and crc32(). The checksums calculated by these two functions cannot be considered as cryptographically secure, they are only used for data integrity verification.

These two functions take the same parameters, including a data string and an optional value, which is used as a starting point for the checksum. The function returns a 32-bit signed integer value, which can be passed back to subsequent calls as a new starting point parameter to generate a dynamically changing checksum.