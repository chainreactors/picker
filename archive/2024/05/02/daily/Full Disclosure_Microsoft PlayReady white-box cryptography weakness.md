---
title: Microsoft PlayReady white-box cryptography weakness
url: https://seclists.org/fulldisclosure/2024/May/0
source: Full Disclosure
date: 2024-05-02
fetch_date: 2025-10-06T17:17:53.629378
---

# Microsoft PlayReady white-box cryptography weakness

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

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![](/shared/images/nst-icons.svg#search)

# Microsoft PlayReady white-box cryptography weakness

---

*From*: Security Explorations <contact () security-explorations com>
*Date*: Wed, 1 May 2024 14:00:52 +0200

---

```
Hello All,

There is yet another attack possible against Protected Media Path
process beyond the one involving two global XOR keys [1]. The new
attack may also result in the extraction of a plaintext content key
value.

The attack has its origin in a white-box crypto [2] implementation.
More specifically, one can devise plaintext content key from white-box
crypto data structures of which goal is to make such a reconstruction
difficult / not possible. This alone breaks one of the main security
objective of white-box cryptography which is to protect the secret key
(unbreakability) [3].

Contrary to the initial (XOR key) attack, the white-box crypto attack
is not limited to the given narrow time window (white-box data
structures need to be present for the time of a movie decryption /
playback). Fixing it might require a completely new approach /
implementation (current one is obviously flawed).

In that context, white-box crypto attack seems to be more severe than
the XOR key one.

Additionally, a cryptographic check proving that extracted key values
correspond to real keys has been conducted for Canal+ Online, Netflix,
HBO Max, Amazon Prime Video and Sky Showtime.

The check relies on a digital cryptographic signature verification.
Such a signature is appended at the end of each license issued by
PlayReady license server.

The crypto check works as following:
- plaintext value of a digital signature key encrypted through ECC is
extracted from a Protected Media Path process
- the extracted signature key is used to calculate the AES-CMAC value
of a binary licence XMR blob
- the calculated signature value is checked against the signature
appended at the end of the issued license
- correct AES-CMAC value implicates correct signature key (and correct
content key)

The above mechanism is also used by Microsoft to verify the
correctness of decrypted content keys received from a license server.
It relies on the fact that signature key is part of the same encrypted
license blob as content key. Thus, successful extraction of a
signature key implicates successful extraction of a content key.

In the context of no confirmation / denial [4] from the platforms
indicated above as being affected, the crypto check should constitute
sufficient proof to support that claim alone.

Thank you.

Best Regards,
Adam Gowdiak

----------------------------------
Security Explorations -
AG Security Research Lab
https://security-explorations.com
----------------------------------

References:
[1] Microsoft Warbird and PMP security research
    https://security-explorations.com/microsoft-warbird-pmp.html
[2] White-box cryptography, Wikipedia
    https://en.wikipedia.org/wiki/White-box_cryptography
[3] White-Box Security Notions for Symmetric Encryption Schemes
    https://eprint.iacr.org/2013/523.pdf
[4] Microsoft DRM Hack Could Allow Movie Downloads From Popular
Streaming Services
    https://www.securityweek.com/microsoft-drm-hacking-could-allow-movie-downloads-from-popular-streaming-services/
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

### Current thread:

* **Microsoft PlayReady white-box cryptography weakness** *Security Explorations (May 01)*

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

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")