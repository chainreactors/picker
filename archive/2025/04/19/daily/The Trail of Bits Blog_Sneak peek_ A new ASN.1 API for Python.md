---
title: Sneak peek: A new ASN.1 API for Python
url: https://blog.trailofbits.com/2025/04/18/sneak-peek-a-new-asn.1-api-for-python/
source: The Trail of Bits Blog
date: 2025-04-19
fetch_date: 2025-10-06T22:05:29.454593
---

# Sneak peek: A new ASN.1 API for Python

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Sneak peek: A new ASN.1 API for Python

[William Woodruff](https://infosec.exchange/%40yossarian)

April 18, 2025

[open-source](/categories/open-source/), [engineering-practice](/categories/engineering-practice/), [cryptography](/categories/cryptography/)

Page content

* [Some quick background on ASN.1](#some-quick-background-on-asn1)
* [Motivating an ASN.1 library for Python](#motivating-an-asn1-library-for-python)
* [But why a *new* library?](#but-why-a-new-library)
* [Stay tuned for more](#stay-tuned-for-more)

If you’ve ever worked with cryptography, PKI schemes, or low-level networking
in Python, you’ve likely encountered [ASN.1](https://en.wikipedia.org/wiki/ASN.1).
ASN.1 undergirds every TLS handshake (via [X.509](https://en.wikipedia.org/wiki/X.509) path validation),
provides the serialization layer for core internet protocols like [LDAP](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol), [SNMP](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol),
and [3GPP](https://www.3gpp.org/), and generally operates as the *lingua franca* of cryptographic
primitive and protocol representation.

ASN.1’s critical role is complemented by a colorful security history:
implementations of ASN.1’s encoding rules have historically been a
rich source of
[memory corruption and denial-of-service vulnerabilities](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=asn.1). Similarly,
ASN.1’s presence at the lowest layers of the internet’s protocols
makes performance and a lack of [parser differentials](https://langsec.org/) a critical requirement.

Python has multiple excellent ASN.1 implementations (like [pyasn1](https://pypi.org/project/pyasn1/),
[asn1](https://pypi.org/project/asn1/), and
[asn1tools](https://pypi.org/project/asn1tools/)), but these generally
fall into the latter category: being written purely in Python makes performance
a concern, and integration into a stack where other ASN.1 parsers are used
(e.g., at the X.509 layer) introduces a differential risk.

We’re changing that: with the help of funding from [Alpha-Omega](https://alpha-omega.dev/),
we’re building an ASN.1 API for [PyCA Cryptography](https://cryptography.io/) that addresses
three key shortcomings in the Python ecosystem today:

1. **Performance**: This new API will use a [pure Rust ASN.1 parser](https://github.com/alex/rust-asn1),
   giving us close-to-native parsing performance.
2. **Differential reduction**: The parser mentioned above is already used
   by [PyCA Cryptography](https://cryptography.io/) for its X.509 APIs. This will reduce the need for
   “mix and match” approaches to ASN.1 parsing, which in turn drive
   differential vulnerabilities.
3. **Modernization**: The new API will expose a declarative [`dataclasses`](https://docs.python.org/3/library/dataclasses.html)
   style interface replete with type hints, making it familiar, idiomatic,
   and compatible with type checkers.

For example, an ASN.1 definition like this:

```
Doohickies ::= SEQUENCE {
    tschotchkes       OCTET STRING,
    baubles           INTEGER,
    knickknacks       UTF8String,
    whatchamacallits  SEQUENCE OF OBJECT IDENTIFIER,
    gizmos            SET OF GeneralizedTime OPTIONAL
}
```

…will correspond to the following Python code:

```
from datetime import datetime

from cryptography.hazmat import asn1

@asn1.sequence
class Doohickies:
    tschotchkes: bytes
    baubles: int
    knickknacks: str
    whatchamacallits: list[asn1.ObjectIdentifier]
    gizmos: set[datetime] | None

doohickies = Doohickies.from_der(b"...")
print(doohickies.tschotchkes)
doohickies.to_der() # b"..."
```

This work is a logical continuation of our previous work on
[X.509 path validation](/2024/01/25/we-build-x-509-chains-so-you-dont-have-to/), as funded by the [Sovereign Tech Fund](https://www.sovereign.tech/programs/fund). It
reflects our ongoing commitment to improving the Python ecosystem, particularly
in the areas of cryptography and supply chain security.

Please get in touch if you’re interested in learning more, or funding
similar work!

## Some quick background on ASN.1

[ASN.1](https://en.wikipedia.org/wiki/ASN.1), or Abstract Syntax Notation One, is an *interface description language*
(IDL). That’s a fancy way of saying that it’s a syntax for describing
data structures in a language- and platform-agnostic manner.

Confusingly, ASN.1 is **not itself** a serialization format. Instead, it defines
*encoding rules*, which in turn define serialization and deserialization
of ASN.1 structures in different settings. In practice,
ASN.1 is synonymous[1](#fn:1) with the [Distinguished Encoding Rules](https://en.wikipedia.org/wiki/X.690#DER_encoding), or DER.

![A helpful visual explanation of ASN.1’s different encoding rules](/img/encoding-rules.png)

Figure 1: A helpful visual explanation of ASN.1's different encoding rules

We’ll treat “ASN.1” and “DER” as interchangeable for the purposes of this post.
Instead of delving too deeply into the intricacies of both
([Let’s Encrypt covers them excellently](https://letsencrypt.org/docs/a-warm-welcome-to-asn1-and-der/)), we’ll focus on the properties
of DER that have kept it relevant for decades:

* **DER is a *canonical* encoding:** There’s only one way to encode a given ASN.1
  structure in DER. In other words, the encoding of an ASN.1 structure in DER
  is deterministic and can be round-tripped while preserving bit-for-bit
  equality.
* **DER is *relatively compact*:** DER defines a binary format and, as a
  consequence of being canonical, forbids non-minimal encodings of integers,
  booleans, and times.
* **DER is a *self-describing* and *self-delimiting* encoding:** A given DER
  message can be fully and soundly parsed without prior reference to a
  schema or format description beyond the encoding rules of DER themselves.

  These properties lend themselves naturally to what web developers would
  call “progressive enhancement”: an application that consumes DER can
  decode the specific structures it cares about while skipping the ones it
  doesn’t, decoding only their length in order to jump ahead to the next one.
* **DER supports *arbitrary-precision integers*:** The `INTEGER` type in DER
  is functionally unconstrained in size, which makes it suitable for
  representing the kinds of large numbers that regularly appear in
  cryptographic settings (e.g., primes).

Put together, these properties make DER very popular in cryptographic,
networking, and telecommunications settings.

More precisely, it’s very popular in the guts of each of these settings:
ASN.1 is used to represent the X.509 certificates that secure the world’s TLS
traffic, is widely used with [PEM-encoded](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail#PEM_encoding) formats, and provides the
description and serialization for much of the internet’s lower protocol layers.

## Motivating an ASN.1 library for Python

You might reasonably ask: why does Python need this?

After all, most Python developers aren’t touching ASN.1 on a daily basis, and
those that do are mostly doing so in predefined ways (such as X.509
certificates). Why does the ecosystem need *generic* support for ASN.1?

The answer to this is that, for better or worse, there are *many* situations
in which Python developers need to do ASN.1 encoding and decoding outside
of the “standard” shapes of X.509 and other well-known formats and protocols.

This can be seen in the [Sigstore](https://sigstore.dev/) ecosystem: Sigstore is
*primarily* an ordinary [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280)–style PKI, but it also includes some custom
[X.509 extensions](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2) for its own purposes. For example, an excerpt
of a [Sigstore log entry](https://search.sigstore.dev/?logIndex=147137139) shows the following extensions:

```
O...