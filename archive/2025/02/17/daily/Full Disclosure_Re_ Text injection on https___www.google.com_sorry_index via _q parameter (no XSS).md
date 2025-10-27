---
title: Re: Text injection on https://www.google.com/sorry/index via ?q parameter (no XSS)
url: https://seclists.org/fulldisclosure/2025/Feb/10
source: Full Disclosure
date: 2025-02-17
fetch_date: 2025-10-06T20:48:14.355989
---

# Re: Text injection on https://www.google.com/sorry/index via ?q parameter (no XSS)

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# Re: Text injection on https://www.google.com/sorry/index via ?q parameter (no XSS)

---

*From*: David Fifield <david () bamsoftware com>
*Date*: Thu, 13 Feb 2025 12:24:36 -0700

---

```
Today at about 2025-02-13 19:00 I noticed the "≠" is back, but now the
type 0x12 payload of the ?q query parameter gets formatted into the
string representation of an IP address, rather than being copied almost
verbatim into the page. If the payload length is 4 bytes, it gets
formatted as an IPv4 address; if 16 bytes, as an IPv6 address. I didn't
try a ton of experiments, but it looks like payload lengths other than 4
and 16 cause the "≠" and payload not to appear at all.

        ./sorry-payload $'\x01\x02\x03\x04'
        https://www.google.com/sorry/index?q=EgQBAgME
        (archived) https://archive.is/rTNsC
        IP address: <client IP address> ≠ 1.2.3.4

        ./sorry-payload 'AAAAAAAAAAAAAAAA'
        https://www.google.com/sorry/index?q=EhBBQUFBQUFBQUFBQUFBQUFB
        (archived) https://archive.is/wcVi1
        IP address: <client IP address> ≠ 4141:4141:4141:4141:4141:4141:4141:4141

Special IPv6 address formats, such as the ::/96 prefix for
IPv4-compatible IPv6 addresses, have their special presentation
format; e.g. 0:0:0:0:0:0:0102:0304 becomes "::1.2.3.4", not "::102:304".
https://en.wikipedia.org/wiki/IPv6_address#Representation

        printf '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04' | ./sorry-payload
        https://www.google.com/sorry/index?q=EhAAAAAAAAAAAAAAAAABAgME
        (archived) https://archive.is/mCXsX
        IP address: <client IP address> ≠ ::1.2.3.4

Whatever purpose the "≠" is supposed to serve, representing the
right-hand side as a string is probably what was originally intended,
rather than just blasting the bytes of the IP address into the HTML.

On Wed, Jan 29, 2025 at 07:15:28PM -0700, David Fifield wrote:
```

> ```
> I tested a few more times, and it appears the text injection has
> disappeared.
>
> These are timestamps when I tested, with offsets relative to the initial
> discovery.
>
> +0h   2025-01-28 03:00        initial discovery
> +5h   2025-01-28 08:19        ?q=EgtoZWxsbyB3b3JsZA works
>                               (https://archive.is/DD9xB)
> +14h  2025-01-28 17:31        ?q=EgtoZWxsbyB3b3JsZA works
>                               (no archive)
> +45h  2025-01-30 00:18        ?q=EgtoZWxsbyB3b3JsZA doesn't work
>                               (https://archive.is/0PJRW)
>
> On Tue, Jan 28, 2025 at 02:26:16AM -0700, David Fifield wrote:
> ```
>
> > ```
> > The page https://www.google.com/sorry/index is familiar to Tor and VPN
> > users. It is the one that says "Our systems have detected unusual
> > traffic from your computer network. Please try your request again
> > later." You will frequently be redirected to this page when using Tor
> > Browser, when you do a search on a Google site such as www.youtube.com
> > or scholar.google.com. The text of the page reports the client IP
> > address, a timestamp of the request, and the URL that was requested.
> >
> > At 2025-01-28 03:00 or earlier, the "sorry" page changed its behavior
> > from what I have seen before. After the client IP address, the page now
> > displays " ≠ ", followed by a few apparently nonsense bytes (not even
> > necessarily properly UTF-8–encoded). The extra bytes turn out to come
> > from a data structure that is encoded in the ?q URL query parameter. By
> > changing the ?q parameter, you can make the string of bytes have any
> > length and contents you like. The byte string will be included in the
> > HTML body, after the client IP address and " ≠ ". However, any bytes
> > that have meaning in HTML will be HTML-escaped, so while you can make
> > text appear on the page, no XSS is possible, as far as I can tell.
> >
> > This is a simple demonstration:
> >
> >     https://www.google.com/sorry/index?q=EgtoZWxsbyB3b3JsZA
> >     (archived) https://archive.is/DD9xB
> >
> > This displays:
> >
> >     IP address: <client IP address> ≠ hello world
> >
> > Let's decode the ?q payload to see what's going on.
> >
> >     $ python3 -c 'import base64; print(repr(base64.urlsafe_b64decode("EgtoZWxsbyB3b3JsZA==")))'
> >     b'\x12\x0bhello world'
> >
> > After base64 decoding, the first byte is 0x12, which is some kind of
> > data type indicator. The second byte, 0x0b, is the length of the value
> > to follow. Then the value is what ends up being copied into the page.
> >
> > The length field is actually a Protobuf varint. Lengths greater than 127
> > need to be encoded as more than 1 byte:
> > https://protobuf.dev/programming-guides/encoding/#varints
> > The following is a Python program to encode arbitrary byte strings
> > appropriately for the ?q parameter:
> >
> > #!/usr/bin/env python3
> > import base64
> > import sys
> > if len(sys.argv) > 1:
> >     payload, = sys.argv[1:]
> >     payload = payload.encode()
> > else:
> >     payload = sys.stdin.buffer.read()
> > def encode_varint(n):
> >     e = [n & 0x7f]
> >     n >>= 7
> >     while n > 0:
> >         e[len(e) - 1] |= 0x80
> >         e.append(n & 0x7f)
> >         n >>= 7
> >     return bytes(e)
> > print(base64.urlsafe_b64encode(b"\x12" + encode_varint(len(payload)) + payload).rstrip(b"=").decode())
> >
> > Use it as follows, for example:
> >
> >     $ curl "https://www.google.com/sorry/index?q=$(printf 'hello world' | ./sorry-payload)"
> >
> > You can see what HTML escaping the server applies by sending a string
> > that consists of every byte value:
> >
> >     $ curl "https://www.google.com/sorry/index?q=$(for c in $(seq 0 255); do printf '\x'$(printf %02x $c); done |
> > ./sorry-payload)" -o resp
> >
> > 00000000: 0001 0203 0405 0607 0820 2020 2020 0e0f  .........     ..
> > 00000010: 1011 1213 1415 1617 1819 1a1b 1c1d 1e1f  ................
> > 00000020: 2021 2671 756f 743b 2324 2526 616d 703b   !&quot;#$%&amp;
> > 00000030: 2623 3339 3b28 292a 2b2c 2d2e 2f30 3132  &#39;()*+,-./012
> > 00000040: 3334 3536 3738 393a 3b26 6c74 3b3d 2667  3456789:;&lt;=&g
> > 00000050: 743b 3f40 4142 4344 4546 4748 494a 4b4c  t;?@ABCDEFGHIJKL
> > 00000060: 4d4e 4f50 5152 5354 5556 5758 595a 5b5c  MNOPQRSTUVWXYZ[\
> > 00000070: 5d5e 5f60 6162 6364 6566 6768 696a 6b6c  ]^_`abcdefghijkl
> > 00000080: 6d6e 6f70 7172 7374 7576 7778 797a 7b7c  mnopqrstuvwxyz{|
> > 00000090: 7d7e 7f80 8182 8384 8586 8788 898a 8b8c  }~..............
> > 000000a0: 8d8e 8f90 9192 9394 9596 9798 999a 9b9c  ................
> > 000000b0: 9d9e 9fa0 a1a2 a3a4 a5a6 a7a8 a9aa abac  ................
> > 000000c0: adae afb0 b1b2 b3b4 b5b6 b7b8 b9ba bbbc  ................
> > 000000d0: bdbe bfc0 c1c2 c3c4 c5c6 c7c8 c9ca cbcc  ................
> > 000000e0: cdce cfd0 d1d2 d3d4 d5d6 d7d8 d9da dbdc  ................
> > 000000f0: ddde dfe0 e1e2 e3e4 e5e6 e7e8 e9ea ebec  ................
> > 00000100: edee eff0 f1f2 f3f4 f5f6 f7f8 f9fa fbfc  ................
> > 00000110: fdfe ff                                  ...
> >
> > The following replacements are applied:
> >
> >     0x09    HT      becomes 0x20
> >     0x0a    LF      becomes 0x20
> >     0x0b    VT      becomes 0x20
> >     0x0c    FF      becomes 0x20
> >     0x0d    CR      becomes 0x20
> >     0x22    "       becomes...