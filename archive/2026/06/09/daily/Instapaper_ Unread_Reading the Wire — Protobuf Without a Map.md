---
title: Reading the Wire — Protobuf Without a Map
url: https://bebinary4n6.blogspot.com/2026/06/reading-wire-protobuf-without-map.html
source: Instapaper: Unread
date: 2026-06-09
fetch_date: 2026-06-10T06:17:21.091668
---

# Reading the Wire — Protobuf Without a Map

# [Be-binary 4n6](https://bebinary4n6.blogspot.com/)

This is my blog about topics in the field of digital forensics.

## Sunday, June 7, 2026

### Reading the Wire — Protobuf Without a Map

Moin! 👋

Protobuf turns up constantly in DFIR work. Android apps, iOS apps, Chrome internals,
sync engines, health databases — wherever Google's tooling reaches, Protobuf follows.
And yet it is one of those formats where a lot of examiners open the hex, see a wall of
binary, and move on. That is understandable. Without the schema, Protobuf does not
announce what it is holding.

This post is a deep dive into what Protobuf actually is at the wire level — byte by byte —
and what you can and cannot recover from it without access to the original
`.proto` definition. Where tool output is shown, it comes from
[crush](https://github.com/kalink0/crush-forensics) — an open-source DFIR
workbench I develop in my personal time. The forensic concepts apply regardless of
which tool you use.

## What Is Protobuf?

Protocol Buffers (Protobuf) is a binary serialisation format developed by Google.
The design goal is compact, fast, schema-driven serialisation — the opposite of a
human-readable format like JSON or XML. A `.proto` file defines the message
structure: field names, types, and field numbers. The compiled schema is used by both
the writer (to encode) and the reader (to decode). Without the schema, you get the wire
format — and the wire format is deliberately sparse.

That sparseness is the core forensic problem. The wire format encodes field numbers and
wire types, but **not field names, not semantic types beyond a handful of primitives,
and not the structure of nested messages**. A value of `1` in a varint
field could be a boolean true, an enum value, an integer count, or a Unix timestamp in
seconds — the wire format cannot tell you which.

What makes Protobuf interesting for forensics is that it is self-delimiting and robust.
A decoder that does not know the schema can still walk the byte stream, identify field
boundaries, and extract raw values. That is exactly what schema-less decode tools —
including `protoc --decode_raw` and the crush BLOB Inspector — do.

## The Wire Format — From the Ground Up

A serialised Protobuf message is a sequence of fields. There is no message header, no
length prefix for the overall message, no magic bytes. The stream starts immediately
with the first field. Each field has two components: a **tag** and a
**payload**.

### The Tag Byte

The tag encodes two things in a single varint: the **field number** and the
**wire type**. It is constructed as:

```
tag = (field_number << 3) | wire_type
```

The three low-order bits carry the wire type (values 0–5). The remaining bits carry the
field number. There are six wire types in use:

| Wire Type | Value | Used For |
| --- | --- | --- |
| Varint | 0 | int32, int64, uint32, uint64, sint32, sint64, bool, enum |
| 64-bit | 1 | fixed64, sfixed64, double |
| Length-delimited | 2 | string, bytes, embedded messages, packed repeated fields |
| Start group | 3 | proto2 only — deprecated; group and contents silently skipped by crush |
| End group | 4 | proto2 only — deprecated; consumed as part of group skip |
| 32-bit | 5 | fixed32, sfixed32, float |

So a tag byte of `0x08` decodes as: `0x08 = 0b00001000` →
low 3 bits = `000` = wire type 0 (Varint), remaining bits = `00001` = field number 1.
A tag of `0x12` = `0b00010010` → wire type 2 (Length-delimited), field number 2.

Tags themselves are encoded as varints, which matters when field numbers exceed 15
(the tag no longer fits in a single byte).

### Varints — The Core Encoding

Varint is the most important encoding to understand, because it is used for both tags
and for all integer-typed field values. The encoding is variable-length little-endian
with a continuation bit:

* Each byte contributes 7 bits of value data.
* The most significant bit (MSB) is the continuation flag: `1` means
  another byte follows; `0` means this is the last byte.
* Bytes are in little-endian order — the first byte holds the least significant 7 bits.

Let us decode `0x96 0x01` step by step:

```
Byte 1: 0x96 = 1001 0110
        MSB = 1 → continuation, more bytes follow
        Value bits: 001 0110 = 0x16 = 22 (least significant 7 bits)

Byte 2: 0x01 = 0000 0001
        MSB = 0 → final byte
        Value bits: 000 0001 = 0x01 (next 7 bits)

Assembled (little-endian 7-bit groups):
  [ 000 0001 ] [ 001 0110 ]
   bits 13–7     bits 6–0

Result: 0b 0000001 0010110 = 0x96 & 0x7F | (0x01 << 7)
      = 22 | 128 = 150
```

So `0x96 0x01` is the varint encoding of **150**. A single-byte
varint (MSB = 0) encodes values 0–127 directly. Values from 128–16383 require two bytes.
The practical maximum for a 64-bit varint is 10 bytes.

### A Complete Field Walkthrough

Take this 7-byte sequence:

```
08 96 01 12 03 74 65 73
```

Breaking it down field by field:

```
Field 1:
  Tag:   0x08 = wire type 0 (Varint), field number 1
  Value: 0x96 0x01 → varint → 150

Field 2:
  Tag:   0x12 = wire type 2 (Length-delimited), field number 2
  Length: 0x03 → 3 bytes follow
  Data:  0x74 0x65 0x73 → UTF-8 → "tes"
```

Without a schema, we know: field 1 holds the integer 150, field 2 holds 3 bytes that
happen to be valid UTF-8. We do not know if field 1 is a count, a status code, an enum,
or a timestamp. We do not know if field 2 is a string, a serialised sub-message, or
arbitrary bytes. That ambiguity is inherent — and unavoidable.

### ZigZag Encoding — Signed Integers

Varint is efficient for small positive integers. Negative integers are a problem: in
two's complement, `-1` is `0xFFFFFFFF` for int32, which as a
varint requires 10 bytes. Protobuf solves this with two approaches:

**int32 / int64**: negative values are sign-extended to 64 bits and then
varint-encoded. `-1` encodes as 10 bytes. Inefficient, but rarely used for
fields that are expected to hold negative values.

**sint32 / sint64**: ZigZag encoding maps signed integers to unsigned integers
such that small-magnitude values — both positive and negative — produce small varints.
The mapping is:

```
ZigZag(n) = (n << 1) ^ (n >> 31)   // sint32
ZigZag(n) = (n << 1) ^ (n >> 63)   // sint64

 0 → 0
-1 → 1
 1 → 2
-2 → 3
 2 → 4
-3 → 5
```

To decode: if the raw varint value is `n`, the ZigZag-decoded signed value
is `(n >> 1) ^ -(n & 1)`.

The forensic implication: if a schema-less decoder shows a varint value that seems
implausibly large (e.g., a field holding `4294967295` where you expected
something small), the field may be a `sint32` that holds `-1`.
Without the schema, you cannot tell — you can only note the raw value and be aware of
the possibility.

### 64-bit and 32-bit Fixed-Width Fields

Wire type 1 (64-bit) and wire type 5 (32-bit) are fixed-width little-endian. They are
used for `double`, `float`, `fixed64`, `sfixed64`,
`fixed32`, and `sfixed32`. Because the width is fixed, no varint
encoding is involved — the bytes are read directly.

A forensically common case: Unix timestamps stored as `double` (wire type 1,
8 bytes, IEEE 754 double precision) or as `fixed64` (wire type 1, 8 bytes,
unsigned 64-bit integer). Both look identical at the wire level. A schema-less decoder
will show you the raw 8 bytes and typically interpret them as a 64-bit integer —
it cannot know whether you should read it as a double instead.

### Length-Delimited Fields

Wire type 2 covers strings, byte arrays, embedded sub-messages, and packed repeated
fields. The format is:

```
[tag: varint] [length: varint] [payload: length bytes]
```

A **packed repeated field** is a wire type 2 field where the payload itself
is a concatenated sequence of varints or fixed-width values — no tags between them.
This is how arrays of integers are efficiently encoded. In a schema-less decoder, a
packed repeated field is indistinguishable from a byte string or an embedded message
without attempting to parse the payload.

An **embedded message** is also wire type 2. Its payload is its...