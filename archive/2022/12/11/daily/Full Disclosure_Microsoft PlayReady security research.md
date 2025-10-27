---
title: Microsoft PlayReady security research
url: https://seclists.org/fulldisclosure/2022/Dec/10
source: Full Disclosure
date: 2022-12-11
fetch_date: 2025-10-04T01:13:00.656976
---

# Microsoft PlayReady security research

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# Microsoft PlayReady security research

---

*From*: Security Explorations <contact () security-explorations com>
*Date*: Sat, 10 Dec 2022 12:23:11 +0100

---

```
Hello,

Microsoft PlayReady is one of the key technologies used by PayTV
industry and OTT platforms for Digital Rights Management and content
security in general. According to Microsoft, PlayReady Server SDK has
several hundred service provider licensees.

Security Explorations conducted security analysis of Microsoft Play
Ready content protection technology in the environment of CANAL+ SAT
TV provider. As a result, complete access to movie assets and content
keys available in CANAL+ VOD library could be gained with the use of a
fake client device identity.

Below, a summary of discovered issues is given:
1) weak security of CANAL+ STB (unpatched 3 years old vulnerabilities)
made it possible to acquire STB PlayReady private group ECC key (its
plaintext value),
2) PlayReady license server did not check whether the client device
identity used in a certificate chain corresponded to the valid
subscriber (fake MAC and SERIAL values could be used for license
requests),
3) PlayReady license server did not verify whether client device had
access to target content (any VOD content / collection could be
accessed, this includes paid content that was available though 48h
rentals only or collections of movies from channels to which the
subscriber didn’t have access to),
4) PlayReady license server was not synced with Content Delivery
Network (CDN), as such access to content could be made outside of the
granted license period (outside of the rental period, etc.),
5) there has been no key rotation observed (same, static content keys
were returned by the PlayReady license server for given content),
6) PlayReady protected content was not watermarked (same content was
returned for requests corresponding to different client identities),
7) PlayReady license server could be crawled in an automatic fashion
for content keys,
8) there has been no detection and blacklisting observed as a response
to invalid / malicious license requests  (some triggered license
server exceptions),
9) PlayReady certificate chain in use by target STB device didn’t have
any time / expiration attribute.

PlayReady security model relies on the security of the link between
client device and a license server. As such, a compromised client
device can implicate compromise of the security of content.

This security model should take into account such a compromise. As
such, reversing PlayReady operation should be more challenging too.
Acquiring PlainReady client secrets such as group keys should not be
straightforward either.

Unfortunately, this was not the case for CANAL+ STB devices as:
1) multiple symbol names were left in a PlayReady binary (Linux ELF file),
2) the binary didn't contain any reverse engineering countermeasures
such as code obfuscation, etc.
3) PlayReady functionality was implemented at the application layer.
This implicated no need to break security of the kernel or HW chip
(PlayReady compromise from user level application). This made runtime
hooking and tracing PlayRedy operation easy.

It was interesting to find out that instead of the usual code and
symbols obfuscation, Microsoft likely decided to build DRM strength on
the strength of ECC crypto and associated math in general (my
impression). They tweaked standard NIST P-256 ECC curve parameters and
conducted whole computations in an affine space (it is called a "MOD"
space in binary).

The ECC curve parameters were embedded in a binary in a non-standard
way (affine transformation to MOD space). All calculations were
conducted with respect to that transformation too (and with certain
optimizations such as Montgomery ladder). Yet, this hasn't been an
obstacle as long as fundamentals of ECC cryptography were acquired.

The crucial weak point was the P256 symbol and subroutine verifying
whether a given point is on curve. This subroutine indirectly leaked
curve parameters (and type).

The ECC formula for NIST P-256 curve is the following:

Y^2 = X^3 + A*x + B

This formula can be used to check whether a given point (X,Y) lies on ECC curve.

For points transformed to the MOD space

Y = y*F
X = x*F

This yields the following:

(y*F)^2 = (x*F)^3 + A*x + B

y^2 * F^2 = x ^3 * F^3 + A*x + B // multiplying by the F^-1 (inverse)

y^2 * F^2 * F^-1 = x ^3 * F^3 * F^-1 + A*x*F^-1 + B*F^-1

y^2 * F^2 * F^-1 = x ^3 * F^3 * F^-1 + (A*F^-1)*x + B*F^-1

which yields the curve parameters used for points transformed to MOD space:

real_a=(A*F^-1)
real_b=B*F^-1

While the private group key and group certificates were embedded in
PlayReady binary in an encrypted form (possible to decrypt with the
use of device root key), their plaintext content could be retrieved in
runtime with the help of user level API too (access to encrypted file
system through symbols exposed by a shared library).

In Jul 2022, I contacted Microsoft and offered to share the results of
my research with the company. To me it looked like a bug at license
server end, but Microsoft closed the case on the basis "this is not a
server-side compromise".

As a result of Microsoft evaluation and multiple communication
problems during report handling process (mails not reaching MS,
automated MSRC system not showing MS responses in the message chat,
advice to contact "breach" team while this should be MS job to forward
any relevant information to proper team such as PlayReady), I decided
not to get into further discussion with Microsoft and did not explain
in particular that server side compromise did not matter for the given
case as Microsoft Play Ready license server was verified to provide
license (and content keys) to any content (not authorized, not rented,
not paid, etc.), it was not synced with CDN and had no watermarking in
place.

I tried to reach out to CANAL+ instead, but without much success.
CANAL+ company was clearly not interested to talk to me over this (no
responses to e-mails and/or requests to establish an official
communication channel for the reporting, discussion and
vulnerabilities disclosure purposes).

Although Microsoft evaluated the issue as no bug in PlayReady, the
overall attack exposes both a significant PlayReady limitation and a
fault at CANAL+ end (no server side auth checks, no watermarking in
place, no license server syncing with CDN, etc.). The demonstrated
technique might potentially constitute a significant risk for content
providers as compromise of a single device or presence of the
unpatched device is sufficient for a large scale, distributed piracy
of a high premium content coming from CANAL+, HBO, FOX, WARNER, etc.
(18K+ assets in CANAL+ VOD library).

Microsoft is aware of that and points out that Microsoft Azure Media
Services (AMS) are free of the above limitations. What I am not sure
is whether Microsoft PlayReady licensees are.

According to Microsoft, PlayReady Server SDK has several hundred
service provider licensees. They should implement security features
missing in PlayReady such as authentication, authorization,
watermarking, etc. on their own in order to avoid the situation
encountered in CANAL+ environment.

As such, ther...