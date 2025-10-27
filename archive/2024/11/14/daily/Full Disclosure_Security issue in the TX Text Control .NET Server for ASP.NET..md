---
title: Security issue in the TX Text Control .NET Server for ASP.NET.
url: https://seclists.org/fulldisclosure/2024/Nov/4
source: Full Disclosure
date: 2024-11-14
fetch_date: 2025-10-06T19:20:22.449798
---

# Security issue in the TX Text Control .NET Server for ASP.NET.

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# Security issue in the TX Text Control .NET Server for ASP.NET.

---

*From*: Filip Palian <s3810 () pjwstk edu pl>
*Date*: Tue, 12 Nov 2024 11:51:22 +1100

---

```
Hej,

Let's keep it short ...

=====

Intro

=====

A "sudo make me a sandwich" security issue has been identified in the TX
Text

Control .NET Server for ASP.NET[1].

According to the vendor[2], "the most powerful, MS Word compatible document

editor that runs in all browsers".

Likely all versions are affected however, it was not confirmed.

=====

Issue

=====

It was possible to change the configured system path for reading and writing

files in the underlying operating system with privileges of the user
running a

web application. This could be achieved by calling the setfiledirectory()

function exposed via JavaScript API[3].

===

PoC

===

-- cut --

TXTextControl.setFileDirectory(0, "c:\\")

-- cut --

See also the attached image file for details.

===========

Remediation

===========

Contact the vendor[4] directly for remediation guidance.

========

Timeline

========

14.10.2024: Security contact requested from sales.department () textcontrol com
.

31.10.2024: CVE requested from MITRE.

......2024: Nobody cares.

12.11.2024: The advisory has been released.

==========

References

==========

[1]
https://www.textcontrol.com/products/asp-dotnet/tx-text-control-dotnet-server/overview/

[2] https://www.textcontrol.com

[3]
https://docs.textcontrol.com/textcontrol/asp-dotnet/ref.javascript.txtextcontrol.setfiledirectory.method.htm

[4] https://www.textcontrol.com/contact/email/general/

Cheers,

Filip Palian
```

[![](att-4/poc.png)](att-4/poc.png)

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

### Current thread:

* **Security issue in the TX Text Control .NET Server for ASP.NET.** *Filip Palian (Nov 12)*

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