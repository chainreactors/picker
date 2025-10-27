---
title: Documenting KeePass KDBX4 file format
url: https://palant.info/2023/03/29/documenting-keepass-kdbx4-file-format/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-30
fetch_date: 2025-10-04T11:08:58.343012
---

# Documenting KeePass KDBX4 file format

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# Documenting KeePass KDBX4 file format

2023-03-29
 [Keepass](/categories/keepass/)/[Password-Managers](/categories/password-managers/)
 19 mins
 [5 comments](/2023/03/29/documenting-keepass-kdbx4-file-format/#comments)

Iâve been playing around with KeePass databases. One aspect was rather surprising: given how many open source products use this format, it is remarkably underdocumented. At best, you can find [outdated and incomplete descriptions by random people](https://gist.github.com/lgg/e6ccc6e212d18dd2ecd8a8c116fb1e45). The KeePass developers themselves never bothered providing complete documentation. All you get is a semi-intelligible list of changes [from KDBX 3.1 to KDBX 4](https://keepass.info/help/kb/kdbx_4.html) and [from KDBX 4 to KDBX 4.1](https://keepass.info/help/kb/kdbx_4.1.html). With the starting point not being documented, these are only moderately useful.

And so itâs not surprising that the implementations I looked at arenât actually implementing the same file format. They all probably manage to handle common files in the same way, but each of them has subtle differences when handling underdocumented format features.

Iâll try to explain the format and the subtle details here. For that, I looked at the source code of [KeePass](https://github.com/dlech/KeePass2.x), [KeePassXC](https://github.com/keepassxreboot/keepassxc), [keepass-rs](https://github.com/sseemayer/keepass-rs/) Rust library and the [kxdbweb](https://github.com/keeweb/kdbxweb/) JavaScript library. Letâs hope this documentation helps whoever else needs to work with that file format, and studying source code will no longer be required.

I can only document the latest version of the format (KDBX 4.1), though Iâll try to highlight changes wherever Iâm aware of them.

#### Contents

* [The outer header](#the-outer-header)
  + [Outer header format](#outer-header-format)
  + [Supported ciphers](#supported-ciphers)
  + [The VariantMap structure](#the-variantmap-structure)
  + [Example of a KXDB4 outer header](#example-of-a-kxdb4-outer-header)
* [Header integrity data](#header-integrity-data)
* [Key derivation](#key-derivation)
  + [Key file format](#key-file-format)
  + [Creating a composite key](#creating-a-composite-key)
  + [Computing the keys](#computing-the-keys)
  + [Key changes on database saves](#key-changes-on-database-saves)
* [Data encryption and compression](#data-encryption-and-compression)
* [The inner header](#the-inner-header)
* [The XML data](#the-xml-data)
  + [Example of the data](#example-of-the-data)
  + [The non-trivial parts](#the-non-trivial-parts)
  + [Which fields are required?](#which-fields-are-required)
  + [The âprotectedâ values](#the-protected-values)

## The outer header

### Outer header format

A general note first: all numbers are stored using little-endian format. So the UInt32 number 0x12345678 is stored as bytes `78 56 34 12` on disk.

The KDBX4 format has two binary file headers: the outer and the inner header. The former is unencrypted and contains all the information necessary to decrypt the fileâs payload. The latter is stored in the encrypted part of the file.

The outer header starts with some version information:

| Field | Type | Value |
| --- | --- | --- |
| Signature1 | UInt32 | 0x9AA2D903 |
| Signature2 | UInt32 | 0xB54BFB67 |
| VersionMinor | UInt16 | Minor part of the format version, e.g. 1 for 4.1 |
| VersionMajor | UInt16 | Major part of the format version, e.g. 4 for 4.1 |

While `Signature1` value is meant to be always the same, `Signature2` has the value 0xB54BFB65 for the KeePass 1.x format.

Presumably, details of the binary format only ever change with a major format version. So a library determining whether it supports the format should be safe checking `VersionMajor` field only. KeePass itself refuses opening files with an unknown `VersionMajor` value and asks for a user confirmation when encountering an unknown `VersionMinor` value.

The version information is followed by a list of header fields. Each header field has the following format:

| Field | Type | Value |
| --- | --- | --- |
| Type | UInt8 | Field type identifier |
| Size | UInt32 | Size of field value |
| Data | byte[Size] | Field value |

*Note*: In the KDBX3 format the `Size` field had type `UInt16`.

The following field types are currently supported:

| Field type | Data type | Value |
| --- | --- | --- |
| 0 (EndOfHeader) |  | Indicates the last header field, typically contains the byte sequence `0d 0a 0d 0a` |
| 2 (CipherID) | UUID (16 bytes) | The cipher used for database encryption |
| 3 (Compression) | UInt32 | Compression algorithm: 0 = None, 1 = Gzip |
| 4 (MainSeed) | byte[32] | Random data used in key derivation |
| 7 (EncryptionIV) | byte[] | Initialization vector for encryption. Size is 16 bytes for CBC ciphers, 12 bytes for ChaCha20. |
| 11 (KdfParameters) | VariantMap | Parameters specific to the key derivation algorithm (new in KDBX4) |
| 12 (PublicCustomData) | VariantMap | Unencrypted storage for arbitrary data, meant to be used by KeePass plugins (new in KDBX4) |

The outer header ends when an `EndOfHeader` field is encountered. Technically speaking, all of the fields listed are optional. In practice however, only the `PublicCustomData` field is optional. All other fields are required for the database to be decrypted.

When reading KDBX4 files, it should be advisable to fail on unexpected fields. Implementors of KeePass and KeePassXC chose to be very forgiving however, resulting in unknown fields being dropped from the database silently. KeePass never rejects any fields, KeePassXC only fails when encountering no longer supported KDBX3 fields:

| Field type | Replacement |
| --- | --- |
| 5 (TransformSeed) | AES-KDF parameter, moved to KdfParameters |
| 6 (TransformRounds) | AES-KDF parameter, moved to KdfParameters |
| 8 (StreamKey) | Moved to [inner header](#the-inner-header) |
| 9 (StreamStartBytes) | Replaced by [header integrity data](#header-integrity-data) |
| 10 (StreamCipher) | Moved to [inner header](#the-inner-header) |

### Supported ciphers

KeePassXC knows four possible values for the `CipherID` field:

| Value | Cipher |
| --- | --- |
| 61ab05a1-9464-41c3-8d74-3a563df8dd35 | AES128-CBC |
| 31c1f2e6-bf71-4350-be58-05216afc5aff | AES256-CBC |
| ad68f29f-576f-4bb9-a36a-d47af965346c | Twofish-CBC |
| d6038a2b-8b6f-4cb5-a524-339a31dbb59a | ChaCha20 |

Out of these, AES128 is generally unsupported. It is unclear when this cipher was even used.

The default encryption cipher is AES256-CBC. KeePass introduced support for the ChaCha20 cipher along with the KDBX4 format, and the plan is probably to make it the default in the long term.

*Note*: ChaCha20 really means the unauthenticated ChaCha20 stream cipher without Poly1305. As weâll see below, KeePass has their own encryption authentication bolted on.

For some reason, KeePassXC does not merely support Twofish-CBC for legacy reasons but also allows creating new databases using this cipher. This is quite a footgun as many other tools will not be able to open such databases (KeePass and kdbxweb in particular wonât).

### The VariantMap structure

The `VariantMap` fields are a key-value storage. They start with a UInt16 value encoding the format version. Usually, it should have the value `0x100`. Implementors are told to ignore the lower 8 bits of the version number, only raising an error if the higher bits encode an unsupported version. So `0x123` should be accepted here, `0x200` should not (keepass-rs didnât get the memo).

The version number is followed by any number of entries using the following format:

| Field | Type | Value |
| --- | --- | --- |
| Type | UInt8 | Type of the value |
| KeySize | UInt32 | Size of the key name |
| Key | byte[KeySize] | Key name |
| ValueSize | UInt32 | Size of the value |
| Value | b...