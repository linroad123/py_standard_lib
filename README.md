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

## gzip
The function of gzip is to read and write gzip files. It provides a file-like interface for GNU zip files, and it uses zlib to compress and decompress data.

## tarfile
The role of tarfile is to read and write tar archive files. This module provides read and write access to UNIX tar archive files (including compressed files). In addition to the POSIX standard, multiple GNU tar extensions are also supported. It can also handle some UNIX special file types (such as hard/soft links) and device nodes.

In the process of writing the packaging code, when adding files using tar.add(), the path of the file itself will also be added, and adding arcname can add the files to the tar package according to their own naming rules.

## zipfile
The function of the zipfile module is to read and write ZIP archive files. This module can be used to manage ZIP archive files, this format is popularized by the PC program PKZIP.

There are two very important classes in the zipfile, namely ZipFile and ZipInfo. In most cases, we only need to use these two classes. ZipFile is the main class, used to create and read zip files, and ZipInfo is to store the information of each file in the zip file.

## hashlib
The role of the hashlib module is to generate password hashes and message digests. Its appearance eliminates the use of separate md5 and sha modules, and makes them have a consistent API. To use a specific hash algorithm, you can create a hash object with an appropriate function. With a hash object, no matter which specific algorithm is used, the object will use the same API.

Since hashlib is "supported" by OpenSSL, all algorithms provided by the OpenSSL library are available, including: SHA1, SHA224, SHA256, SHA384, SHA512, MD5, etc.

## hmac
The function of the Hmac module is to implement key hashing to complete message authentication, which can be used to verify the integrity of information. This information may be passed between applications or stored in a location that may pose a security threat. The basic idea is to generate a cryptographic hash of the actual data and provide a shared secret key. The resulting hash is then used to check the transmitted or stored message to determine a trust level, instead of transmitting the secret key.

The new() function has 3 parameters. The first parameter is the secret key, which will be shared between the communicating parties so that both ends can use the same value. The second value is an initial message. If the content of the message to be authenticated is very small, such as a timestamp or an HTTP POST, the entire body of the message is passed to new() instead of using the update() method. The last parameter is to use the second-class summary module. The default is hashlib.md5. This example replaces the algorithm with hashlib.sha1.