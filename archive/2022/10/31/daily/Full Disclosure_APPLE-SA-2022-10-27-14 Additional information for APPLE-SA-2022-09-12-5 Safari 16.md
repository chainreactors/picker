---
title: APPLE-SA-2022-10-27-14 Additional information for APPLE-SA-2022-09-12-5 Safari 16
url: https://seclists.org/fulldisclosure/2022/Oct/50
source: Full Disclosure
date: 2022-10-31
fetch_date: 2025-10-03T21:21:53.295962
---

# APPLE-SA-2022-10-27-14 Additional information for APPLE-SA-2022-09-12-5 Safari 16

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

[![Previous](/images/left-icon-16x16.png)](49)
[By Date](date.html#50)
[![Next](/images/right-icon-16x16.png)](51)

[![Previous](/images/left-icon-16x16.png)](49)
[By Thread](index.html#50)
[![Next](/images/right-icon-16x16.png)](51)

![](/shared/images/nst-icons.svg#search)

# APPLE-SA-2022-10-27-14 Additional information for APPLE-SA-2022-09-12-5 Safari 16

---

*From*: Apple Product Security via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Oct 2022 18:23:51 -0700

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

APPLE-SA-2022-10-27-14 Additional information for APPLE-SA-2022-09-12-5 Safari 16

Safari 16 addresses the following issues.
Information about the security content is also available at
https://support.apple.com/HT213442.

Safari Extensions
Available for: macOS Big Sur and macOS Monterey
Impact: A website may be able to track users through Safari web
extensions
Description: A logic issue was addressed with improved state
management.
WebKit Bugzilla: 242278
CVE-2022-32868: Michael

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: A buffer overflow issue was addressed with improved
memory handling.
WebKit Bugzilla: 241969
CVE-2022-32886: P1umer, afang5472, xmzyshypnc

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Processing maliciously crafted web content may lead to
arbitrary code execution
Description: An out-of-bounds read was addressed with improved bounds
checking.
WebKit Bugzilla: 242762
CVE-2022-32912: Jeonghoon Shin (@singi21a) at Theori working with
Trend Micro Zero Day Initiative

WebKit
Available for: macOS Big Sur and macOS Monterey
Impact: Visiting a website that frames malicious content may lead to
UI spoofing
Description: The issue was addressed with improved UI handling.
WebKit Bugzilla: 243236
CVE-2022-32891: @real_as3617 and an anonymous researcher
Entry updated October 27, 2022

WebKit Sandboxing
Available for: macOS Big Sur and macOS Monterey
Impact: A sandboxed process may be able to circumvent sandbox
restrictions
Description: An access issue was addressed with improvements to the
sandbox.
WebKit Bugzilla: 243181
CVE-2022-32892: @18楼梦想改造家 and @jq0904 of DBAppSecurity's WeBin lab
Entry added October 27, 2022

Safari 16 may be obtained from the Mac App Store.
All information is also posted on the Apple Security Updates
web site: https://support.apple.com/en-us/HT201222.

This message is signed with Apple's Product Security PGP key,
and details are available at:
https://www.apple.com/support/security/pgp/
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEBP+4DupqR5Sgt1DB4RjMIDkeNxkFAmNbKowACgkQ4RjMIDke
NxlCEg/+KnbktSos4M/gMt7rkcCymB4Ul4mMw0XW6eJVBL34H3XiOM9i8OoRGbg2
F3Ft4mxRWFlzA9SgNVuvMBVHREkOdeOJ37PDtfZp9bITGAtOww8K8Ng56VxhpPem
gs5q+veUTu95cVXDfGebwQNYtXc76+Zg/+Ju9VmhFJg0XXrjC2mzAEC8Mz2yy91b
9otf+UeDmdBUF3eLrygVAwtXE0/swZVaRMeDu2EYFuJWl/afN+ICOrHYLxtLa9dB
1uvw+RbOhwFRdKB010tcUUhf+M06Tp6pHPvtWHdS+Xy3RxA1d4rMzdon4TmsdEdr
dBpOiu0EOFLMXekVosIkkvKLXAWwH5C1Ogap7IchXnc8c+rEm6Hl1QuoH4QL0krD
P+sGYV4457e+VASkaUDEr6yxXJj+8MILm4x+7akD767qhoKvzpIfrFKY2gMnWkvK
JNUMzPXCYLkht39KWGEJk/b/HMvlwniBmXKGDVaTG/oNcMVFyRvx81qxrNlELxcw
lYSfP5tICA0CBWyVXYvUy1JRe15QrelLmCwpcAvAz1Edqu90sAAsPybvrPJHcZxD
2O+parML2rVJ6zOVBg1cOddohgnJEbT3PzDW48HRV8Ub5I8WzvIKqnS+R7VWkh66
Av8d8ElI37WY2sfIsFwXvhsIYFLZL86nel5HVEflmog2K0g/Kd0=
=lLIK
-----END PGP SIGNATURE-----

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](49)
[By Date](date.html#50)
[![Next](/images/right-icon-16x16.png)](51)

[![Previous](/images/left-icon-16x16.png)](49)
[By Thread](index.html#50)
[![Next](/images/right-icon-16x16.png)](51)

### Current thread:

* **APPLE-SA-2022-10-27-14 Additional information for APPLE-SA-2022-09-12-5 Safari 16** *Apple Product Security via Fulldisclosure (Oct 30)*

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