---
title: Bad things come in large packages: .pkg signature verification bypass on macOS
url: https://sector7.computest.nl/post/2023-01-xar/
source: Sector 7
date: 2023-01-14
fetch_date: 2025-10-04T03:53:59.538692
---

# Bad things come in large packages: .pkg signature verification bypass on macOS

[![](/images/logo.png)](/)

* [Research](/)
* [About](/about/)
* [Contact](/contact/)
* [Computest](https://computest.nl/)

* [Mastodon](https://infosec.exchange/%40sector7)
* [Bluesky](https://bsky.app/profile/sector7-nl.bsky.social)
* [LinkedIn](https://www.linkedin.com/company/computest)
* [GitHub](https://github.com/sector7-nl)
* [RSS](/index.xml)

January 13, 2023

# Bad things come in large packages: .pkg signature verification bypass on macOS

![](/post/2023-01-xar/header.png)

Code signing of applications is an essential element of macOS security. Besides signing applications, it is also possible to sign installer packages (.pkg files). During a short review of the xar source code, we found a vulnerability (CVE-2022-42841) that could be used to modify a signed installer package without invalidating its signature. This vulnerability could be abused to bypass Gatekeeper, SIP and under certain conditions elevate privileges to root.

# Background

Installer packages are based on xar files with a number of predefined file names. The method for signing installer packages is the same as generating signed xar files, so to start we’ll explain how that file format works.

A xar file consists of 3 parts: a fixed length header, a table of contents (TOC) and what is called the “heap”.

The header contains a number of fields, including the hashing algorithm that is used throughout the file (typically still SHA1) and the size of the TOC.

The TOC is a zlib-compressed XML document. This document lists for each file included in the archive the start address and length where the contents can be found on the heap, starting with 0 for the first byte directly after the TOC. Each file in the archive can be compressed independently by specifying an encoding, so when creating an archive file it is possible to choose the optimal way of storing each file.

For all files, a hash is included in the TOC of both the uncompressed and compressed data, using the hashing algorithm specified in the header.

For example:

```
<file id="4">
  <data>
    <length>430</length>
    <offset>2533</offset>
    <size>654</size>
    <encoding style="application/x-bzip2"/>
    <extracted-checksum style="sha1">c5c07ac6917dbbbacf1044700559dfff3c96ac26</extracted-checksum>
    <archived-checksum style="sha1">bda75d4a4f97c71985cdb5d3350fea8a62bbad0e</archived-checksum>
  </data>
  <FinderCreateTime>
    <nanoseconds>0</nanoseconds>
    <time>1970-01-01T00:00:00</time>
  </FinderCreateTime>
  <ctime>2022-10-03T17:54:54Z</ctime>
  <mtime>2022-10-03T17:54:54Z</mtime>
  <atime>2022-10-03T17:54:54Z</atime>
  <group>wheel</group>
  <gid>0</gid>
  <user>root</user>
  <uid>0</uid>
  <mode>0644</mode>
  <deviceno>16777241</deviceno>
  <inode>33</inode>
  <type>file</type>
  <name>PackageInfo</name>
</file>
```

Even xar files that are not signed have these hashes and so the integrity can be verified when extracting a file.

To verify the integrity of the entire archive, the TOC also lists the location on the heap where a value known as the “TOC hash” is stored. In practice this is usually at offset 0:

```
<checksum style="sha1">
  <offset>0</offset>
  <size>20</size>
</checksum>
```

The value stored here must be equal to the hash of the compressed TOC data and this is verified when the archive is opened. The reason this is included on the heap and not in the TOC itself is that this would create a cyclic dependency: adding this value into the TOC would change the TOC and the TOC hash again.

This hash indirectly guarantees the integrity of all files in the archive: for each file, the `extracted-checksum` in the TOC ensures the integrity of that file. The integrity of the TOC is covered by the TOC hash. This construction has the nice benefit that a single file can be extracted and validated without having to validate the entire archive. This means it is possible to extract files from xar archives without completely reading the archive, or possibly even without completely downloading it.

Signed xar files additionally contain a signature element with a certificate chain in the TOC:

```
<signature style="RSA">
  <offset>20</offset>
  <size>256</size>
  <KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#">
    <X509Data>
      <X509Certificate>MIIFdjCCBF6gAwIBAgIQMJvx21UGMjp4U[...]</X509Certificate>
      <X509Certificate>MIIEbDCCA1SgAwIBAgIQWqJHoRaQ3Cgu/[...]</X509Certificate>
      <X509Certificate>MIIEuzCCA6OgAwIBAgIBAjANBgkqhkiG9[...]</X509Certificate>
    </X509Data>
  </KeyInfo>
</signature>
```

The signature itself is also stored on the heap (for the same cyclic dependency reason). The data used for generating the signature is the TOC hash. This signature therefore ensures the authenticity of all files in the archive.

Interestingly, this design does mean that data on the heap that is not included in any of the ranges can be modified without invalidating the signature. For example, appending more data to a xar file will always keep the TOC hash and signature valid.

# The vulnerability

For signed packages, the TOC hash needs to be used for two different checks:

* The computed TOC hash needs to be equal to the TOC hash stored on the heap.
* The signature and the certificates need to correspond to the TOC hash.

This is implemented in the following locations in the xar source code.

Here, the computed TOC is compared to the value stored on the heap.

<https://github.com/apple-oss-distributions/xar/blob/f67a3a8c43fdd35021fd3d1562b62d2da32b4f4b/xar/lib/archive.c#L391-L484>

```
/* if TOC specifies a location for the checksum, make sure that
 * we read the checksum from there: this is required for an archive
 * with a signature, because the signature will be checked against
 * the checksum at the specified location <rdar://problem/7041949>
 */
const char *value;
uint64_t offset = 0;
uint64_t length = 0;
if( xar_prop_get( XAR_FILE(ret) , "checksum/offset", &value) == 0 ) {

    if (value) {
        errno = 0;
        offset = strtoull( value, (char **)NULL, 10);
        if( errno != 0 ) {
            fprintf(stderr, "checksum/offset missing or invalid!\n");
            xar_close(ret);
            return NULL;
        }
    } else {
        fprintf(stderr, "checksum/offset missing or invalid!\n");
        xar_close(ret);
        return NULL;
    }
}

[...]

XAR(ret)->heap_offset = xar_get_heap_offset(ret) + offset;
if( lseek(XAR(ret)->fd, XAR(ret)->heap_offset, SEEK_SET) == -1 ) {
    xar_close(ret);
    return NULL;
}
[...]

size_t tlen = 0;
void *toccksum = xar_hash_finish(XAR(ret)->toc_hash_ctx, &tlen);
XAR(ret)->toc_hash_ctx = NULL;

if( length != tlen ) {
    free(toccksum);
    xar_close(ret);
    return NULL;
}

// Store our toc hash upon archive open, so callers can determine if it
// has changed or been tampered with after archive open
XAR(ret)->toc_hash = malloc(tlen);
memcpy(XAR(ret)->toc_hash, toccksum, tlen);
XAR(ret)->toc_hash_size = tlen;

void *cval = calloc(1, tlen);
if( ! cval ) {
    free(toccksum);
    xar_close(ret);
    return NULL;
}

ssize_t r = xar_read_fd(XAR(ret)->fd, cval, tlen);

[...]

if( memcmp(cval, toccksum, tlen) != 0 ) {
    fprintf(stderr, "Checksums do not match!\n");
    free(toccksum);
    free(cval);
    xar_close(ret);
    return NULL;
}
```

This first retrieves the attribute checksum attribute from the XML document as a `const char *value`. Then, `strtoull` converts it to an unsigned 64-bit integer and it gets stored in the `offset` variable.

For obtaining the TOC hash for validating the signature, a similar bit of code is used:
<https://github.com/apple-oss-distributions/xar/blob/f67a3a8c43fdd35021fd3d1562b62d2da32b4f4b/xar/lib/signature.c#L244-L276>

```
uint32_t offset = 0;
xar_t x = NULL;
const char  *value;

// xar 1.6 fails this method if any of data, length, signed_data, signed_length are NULL
// within OS X we use this method to get combinations of signature, signed data, or signed_offset,
// so this method checks and sets these out values indepen...