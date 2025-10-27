---
title: Microsoft Warbird and PMP security research - technical doc
url: https://seclists.org/fulldisclosure/2024/Dec/1
source: Full Disclosure
date: 2024-12-04
fetch_date: 2025-10-06T19:41:51.258068
---

# Microsoft Warbird and PMP security research - technical doc

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

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# Microsoft Warbird and PMP security research - technical doc

---

*From*: Security Explorations <contact () security-explorations com>
*Date*: Tue, 3 Dec 2024 10:09:52 +0100

---

```
Hello All,

We have released a technical document pertaining to our Warbird / PMP security
research. It is available for download from this location:

https://security-explorations.com/materials/wbpmp_doc.md.txt

The document provides a more in-depth technical explanation, illustration and
verification of discovered attacks affecting PlayReady on Windows 10 / 11 x64
and pertaining to the following in particular:
- Warbird deficiencies
- content key sniffer operation
- magic XOR keys discovery
- white-box crypto attack
- complete client identity compromise attacks

Microsoft aimed to implement state of the art code protection to mitigate
security threats related to client side based security through crypto, code
integrity, auth checks, white-box crypto, code obfuscation and kernel level
support. Yet, a successful and complete (from an identity and content key
security point of view) PlayReady compromise could be achieved. This was
primarly due to some wrong assumption made with respect to code obfuscation,
crypto and OS kernel integration.

We proved these assumptions wrong by showing that:
1) obfuscated code doesn't need to be analysed in a thorough fashion (or that
   it doesn't need to be analysed at all),
2) some crypto properties (or weaknesses such as bijections) can be revealed
   through specially crafted inputs, which immediately lead to secret keys
   extraction,
3) kernel level support (`PEAuth` driver, protected process functionality)
   didn't matter at all (no need for any privilege elevation).

While Microsoft was well aware of the research impact (PlayReady for Windows
being broken to pieces) along the amount of work it required, the company has
not expressed / signaled any interest to discuss access to this research on
a fair and commercial basis (regulating conditions of IP / know how use,
mutual agreement on a price, etc.) for the last 8 months. Submitting our
work through MSRC was out of question due to the following:
- the research took us nearly 9 months of work (on top of the 6 months of
  R&D done in 2022, which has been "consumed" and in some way ignored by the
  company), one more extra month needs to be added to this too (attacks #2-#4
  and crypto proofs investigated due to platforms' avoidance to confirm the
  initial XOR key attack,
- the new research embeds some potentially valuable IP / know-how, which we
  wanted to protect too, we have reasons to believe that some parties from a
  PayTV industry use our ideas in their commercial products / services - we
  inquired Nagra / Kudelski (PayTV / CAS security provider), Telefonica (the
  owner of Movistar) and Cyfrowy Polsat (the owner of Polsat) about it, but
  none of the companies responded (none clearly denied the use of our know
  how / IP for commercial purposes as of writing of this message)
- Microsoft Bounty Terms and Conditions, which implicate commercial use with
  unknown payment terms, all non-negotiable and under Microsoft control)
- Microsoft game plays in 2022 regarding PlayReady "deficiencie" (evaluation)
  and their addressing.

Anyway, we decided to give Microsoft (a company consisting of 100,000+
software engineers, with access to all the know-how, internal docs and source
codes) approx. the same amount of time to fix / address the issues as it took
us (a 1 man shop relying on binaries and public info only) to analyze and
reverse engineer the technology, discover the issues, develop illustrating
POCs and dedicated toolsets. Thus, Dec 2024 disclosure date.

We provided Microsoft with access to the complete research package comprising
of a technical document, all toolsets with sources and test data (285MB ZIP
file) on Nov 18, 2024 and free of any charge (two weeks prior to the planned
disclosure). We indicated to Microsoft that sharing of the material was not
done as part of MSRC vulnerability reporting process (thus no obligation for
any confirmation / follow ups / rewards / confidentiality / implicit license
granting, etc.), Microsoft was however informed that the research could be
acquired by the company upon evaluation (commercial companies do not pay bills
/ run business by waving a glossy "thank you from Microsoft" coupon at the
cashier stand / checkout).

Although Microsoft got all the details for free, the company is only partly
the winner here as its engineers likely failed to locate / address the root
cause of the issues over the recent 8 months (no fixes / mitigations observed
as of Nov 19, 2024). That's quite a shame in our opinion. The other source for
the shame lies in the nature of the issues and attacks described in the doc
(vide 10 years of innovation and more than $1B invested).

While we initially indicated to Microsoft that sharing of the research would
implicate the need to clear company's "privileged position" (access to the
toolset / know-how) and release POCs / source codes, we decided to postpone
such a publication as of now.

We believe the disclosure provides both important contribution along a valuable
perspective on the state of the art / security provided by PlayReady content
security technology (vide the nature of the issues uncovered / verification of
vendor's claims).

Thank you.

Best Regards,
Adam Gowdiak

----------------------------------
Security Explorations -
AG Security Research Lab
https://security-explorations.com
----------------------------------
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

### Current thread:

* **Microsoft Warbird and PMP security research - technical doc** *Security Explorations (Dec 03)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)...