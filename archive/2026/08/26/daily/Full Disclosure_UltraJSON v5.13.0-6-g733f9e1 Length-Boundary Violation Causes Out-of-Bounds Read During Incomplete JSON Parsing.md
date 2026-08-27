---
title: UltraJSON v5.13.0-6-g733f9e1 Length-Boundary Violation Causes Out-of-Bounds Read During Incomplete JSON Parsing
url: https://seclists.org/fulldisclosure/2026/Aug/106
source: Full Disclosure
date: 2026-08-26
fetch_date: 2026-08-27T12:14:25.797708
---

# UltraJSON v5.13.0-6-g733f9e1 Length-Boundary Violation Causes Out-of-Bounds Read During Incomplete JSON Parsing

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](105)
[By Date](date.html#106)
[![Next](/images/right-icon-16x16.png)](107)

[![Previous](/images/left-icon-16x16.png)](105)
[By Thread](index.html#106)
[![Next](/images/right-icon-16x16.png)](107)

![](/shared/images/nst-icons.svg#search)

# UltraJSON v5.13.0-6-g733f9e1 Length-Boundary Violation Causes Out-of-Bounds Read During Incomplete JSON Parsing

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 22 Aug 2026 08:44:03 -0400

---

```
UltraJSON contains an out-of-bounds read in its native C JSON decoder when
processing certain incomplete JSON values supplied through an explicitly
length-bounded input buffer.

The affected native entry point, JSON_DecodeObject(), accepts both a buffer
pointer and an explicit buffer length:

JSON_DecodeObject(
    JSONObjectDecoder *dec,
    const char *buffer,
    size_t cbBuffer
)

The decoder establishes cbBuffer as the logical boundary of the supplied
input. However, several parsing paths can advance the internal input cursor
to this boundary and subsequently dereference it without first verifying
that additional input remains.

A minimal one-byte input containing only:

[

is sufficient to reproduce the issue.

When an exact one-byte, non-NUL-terminated heap allocation containing 0x5b (
[) is passed to JSON_DecodeObject() with cbBuffer == 1, decode_array()
consumes the opening bracket and advances the decoder cursor to the end of
the supplied input.

decode_array() then calls SkipWhitespace(). Because SkipWhitespace()
immediately dereferences the cursor without verifying that it remains below
ds->end, it performs a one-byte read immediately beyond the supplied buffer.

AddressSanitizer confirms the resulting out-of-bounds read:

ERROR: AddressSanitizer: heap-buffer-overflow
READ of size 1

0x502000000011 is located 0 bytes after 1-byte region
[0x502000000010,0x502000000011)

SUMMARY: AddressSanitizer: heap-buffer-overflow
/src/./src/ujson/lib/ultrajsondec.c:317:13
in SkipWhitespace

Malformed or truncated JSON should result in a normal decoding error. It
should not cause the native decoder to access memory outside the explicitly
supplied input boundary.
Affected Attack Surface

The vulnerable native decoder entry point is:

src/ujson/lib/ultrajsondec.c

through:

JSON_DecodeObject(
    JSONObjectDecoder *dec,
    const char *buffer,
    size_t cbBuffer
)

JSON_DecodeObject() explicitly accepts a buffer length rather than
requiring the supplied buffer to be NUL-terminated.

The decoder initializes its input boundaries using:

ds.start = (char *) buffer;
ds.end = ds.start + cbBuffer;

ds.end therefore represents the exclusive upper boundary of the supplied
input.

Any parser operation that dereferences ds.start or another cursor derived
from it must first establish that the cursor is strictly less than ds.end.

The vulnerable parser path fails to enforce this invariant.
Vulnerable Code

The confirmed invalid access occurs in SkipWhitespace():

static FASTCALL_ATTR void FASTCALL_MSVC
SkipWhitespace(struct DecoderState *ds)
{
    char *offset = ds->start;

    for (;;)
    {
        switch (*offset)
        {
            case ' ':
            case '\t':
            case '\r':
            case '\n':
                offset++;
                break;

            default:
                ds->start = offset;
                return;
        }
    }
}

The function immediately evaluates:

*offset

without checking:

offset < ds->end

Consequently, if a caller reaches SkipWhitespace() after consuming the
final byte of the supplied input:

offset == ds->start == ds->end

the first switch (*offset) operation accesses memory outside the
length-bounded input.
Proof of Concept

The PoC deliberately avoids relying on an implicit trailing NUL byte.

It allocates exactly one byte:

buffer = malloc(1);

copies the payload into that allocation:

memcpy(buffer, "[", 1);

and invokes the decoder with the exact allocation length:

JSON_DecodeObject(&decoder, buffer, 1);

The supplied allocation therefore contains only:

Address N:
    0x5b

There is intentionally no second byte belonging to the allocation.

This is consistent with the native API contract because JSON_DecodeObject()
receives the input length explicitly through cbBuffer.
Reproduction

From the repository root:

scripts/repro_decoder_oob_asan.sh array /tmp/ujson-asan-poc.log

The harness reports:

seed=array
payload=[
payload_hex=5b

FUZZ seed=array len=1 payload="[" hex=5b

The process subsequently terminates under AddressSanitizer after detecting
the invalid memory access.
AddressSanitizer Evidence

AddressSanitizer identifies the vulnerability as a heap-buffer overflow
involving a one-byte read:
  ERROR: AddressSanitizer: heap-buffer-overflow
  READ of size 1 at 0x502000000011 thread T0
      #0 ... in SkipWhitespace /src/./src/ujson/lib/ultrajsondec.c:317:13
      #1 ... in decode_array /src/./src/ujson/lib/ultrajsondec.c:617:5
      #2 ... in decode_any /src/./src/ujson/lib/ultrajsondec.c:780:24
      #3 ... in JSON_DecodeObject /src/./src/ujson/lib/ultrajsondec.c:822:9
      #4 ... in run_seed /src/./scripts/decoder_oob_asan_harness.c:150:18
      #5 ... in main /src/./scripts/decoder_oob_asan_harness.c:171:16

  0x502000000011 is located 0 bytes after 1-byte region
  [0x502000000010,0x502000000011)

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<https://linkedin.com/in/yourhandle>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](105)
[By Date](date.html#106)
[![Next](/images/right-icon-16x16.png)](107)

[![Previous](/images/left-icon-16x16.png)](105)
[By Thread](index.html#106)
[![Next](/images/right-icon-16x16.png)](107)

### Current thread:

* **UltraJSON v5.13.0-6-g733f9e1 Length-Boundary Violation Causes Out-of-Bounds Read During Incomplete JSON Parsing** *Ron E (Aug 26)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure....