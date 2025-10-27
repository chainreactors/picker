---
title: APPLE-SA-2022-11-09-2 macOS Ventura 13.0.1
url: https://seclists.org/fulldisclosure/2022/Nov/8
source: Full Disclosure
date: 2022-11-16
fetch_date: 2025-10-03T22:55:19.837869
---

# APPLE-SA-2022-11-09-2 macOS Ventura 13.0.1

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-11-09-2 macOS Ventura 13.0.1

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 09 Nov 2022 15:19:57 -0800

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-11-09-2 macOS Ventura 13.0.1

macOS Ventura 13.0.1 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213504.

libxml2
Available for: macOS Ventura
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: An integer overflow was addressed through improved input
validation.
CVE-2022-40303: Maddie Stone of Google Project Zero

libxml2
Available for: macOS Ventura
Impact: A remote user may be able to cause unexpected app termination
or arbitrary code execution
Description: This issue was addressed with improved checks.
CVE-2022-40304: Ned Williamson and Nathan Wachholz of Google Project
Zero

All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmNsFNQACgkQ4RjMIDke
NxkkbBAAsAYMux+v/27NK6+FvyxrTRLkR0yyzp8SorMSfPwZInNGkkEmQxjSzI0+
D3rK9usf/pouEV9LMnR+Uf37pEdlpSDD7uXZ81m1vhN6RPkz2qD5WdM46RaWTbAS
/xe3ZEu8+Jpr5SQSWuI+QIBr/vn9Txu/N6l/WQVxnWS+RSWO6tZLLOXMEyVk9vPx
XJGyQywt3XYoVksvzwAgm/2yslQ+0OWphWjLp73bjQGrrIiClphxmtyvA0SN8Nds
Ah0+X8SRjCErSN4736U1htKtClSHDowdaD2wevGGUrdRSLJQLTPPkqUPF3P/4/8i
xW42Zgf9qucN9O89P7ONvHOIe8swtD9vf1AjFXvsDqQvMZQVFDBNXbG138V4LLws
f5UdpUmY/0lSnVpAZQlo+xuMJSb3SMWYIB2ozhzDLHgBKTxERFB7uyrEYQgXs9XB
1qg+BbW5uooEoMKbutw36/II/JTFRM34QxWiOJHw4cCypmuaGkSJ/8jsTJDlRvG/
T9BchgHjBvqHFtCVNLGikkVYzEVQnQLXQAZoZMCYV0benebEIFLIaObaciQqA3F2
N7/rvpXd5l6G3sEGwqMPT5aYj6Vm/0LBnxuTlN1xN1wgOQoS+LWL8bW+8/HjtJLa
eyWMh8yD0o02Hf6dNIl9RTuoAKwZvmJbeqi/1uEaoL8sAP9gK1s=
=CjcG
-----END PGP SIGNATURE-----
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

### Current thread:

* **APPLE-SA-2022-11-09-2 macOS Ventura 13.0.1** *Apple Product Security via Fulldisclosure (Nov 15)*

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