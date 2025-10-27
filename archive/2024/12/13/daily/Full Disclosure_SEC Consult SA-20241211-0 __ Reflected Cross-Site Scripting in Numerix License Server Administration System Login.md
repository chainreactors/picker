---
title: SEC Consult SA-20241211-0 :: Reflected Cross-Site Scripting in Numerix License Server Administration System Login
url: https://seclists.org/fulldisclosure/2024/Dec/4
source: Full Disclosure
date: 2024-12-13
fetch_date: 2025-10-06T19:41:11.249782
---

# SEC Consult SA-20241211-0 :: Reflected Cross-Site Scripting in Numerix License Server Administration System Login

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

# SEC Consult SA-20241211-0 :: Reflected Cross-Site Scripting in Numerix License Server Administration System Login

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 11 Dec 2024 11:39:55 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20241211-0 >
=======================================================================
              title: Reflected Cross-Site Scripting
            product: Numerix License Server Administration System Login
 vulnerable version: 1.1_596
      fixed version: -
         CVE number: CVE-2024-50585
             impact: medium
           homepage: https://connect.numerix.com/nlslogin.jsp
              found: 2024-04-05
                 by: Daniel Hirschberger (Office Bochum)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Founded in 1996, Numerix has over 19 offices, 700 clients and 90 partners
across more than 26 countries. Numerix is recognized across the industry for
its many breakthroughs in quantitative research and is proud of its
reputation for being able to price and risk manage any derivative instrument
â€“ vanillas to the most sophisticated exotic products."

Source: https://www.numerix.com/about-numerix

Business recommendation:
------------------------
The vendor was unresponsive during multiple attempts to contact them via
various channels, hence there is no solution available. In case you are
using this software, be sure to restrict access and monitor logs.
Try to reach out to your contact person for this vendor and request a patch.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) Reflected Cross-Site Scripting (CVE-2024-50585)
Users who click on a malicious link or visit a website under the control of an
attacker can be infected with arbitrary JavaScript which is running in the
context of the "Numerix License Server Administration System Login".
(FQDN: https://connect.numerix.com)

Proof of concept:
-----------------
1) Reflected Cross-Site Scripting (CVE-2024-50585)
This vulnerability can be triggered by sending the following POST request:
[ redacted ]

The server responds with the injected JavaScript code which is then
executed in the browser of the victim.

<xss.png>

Vulnerable / tested versions:
-----------------------------
This vulnerability was identified on 5th April 2024. The following version seems to be
affected:
* 1.1_596, powered by Orion v2.5.10-083015, Agilis Software

Vendor contact timeline:
------------------------
2024-04-08: Contacting vendor through support () numerix com; no response
2024-04-24: Contacting vendor through support () numerix com; no response
2024-05-06: Contacting vendor through sales () numerix com; no response
2024-05-28: Found out that the page might be part of a solution which
            is developed by agilis-sw.com; contacted them via
            info () agilis-sw com; no response
2024-07-18: Contacted again via info () agilis-sw com; no response
2024-10-22: Contacting support () numerix com, sales () numerix com and
            license () numerix com again, asking for a security contact.
            Contacting CEO of Agilis Software via LinkedIn connection
            request.
            No response from all channels.
2024-10-28: Asking CERT/CC for coordination support
2024-11-18: CERT/CC will not handle this case, recommending to go through
            with public disclosure
2024-12-11: Public disclosure of advisory.

Solution:
---------
The vendor was unresponsive during multiple attempts to contact them via
various channels, hence there is no solution available. In case you are
using this software, be sure to restrict access and monitor logs.
Try to reach out to your contact person for this vendor and request a patch.

Workaround:
-----------
None

Advisory URL:
-------------
https://r.sec-consult.com/numerix

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia

About SEC Consult Vulnerability Lab
The SEC Consult Vulnerability Lab is an integrated part of SEC Consult, an
Eviden business. It ensures the continued knowledge gain of SEC Consult in the
field of network and application security to stay ahead of the attacker. The
SEC Consult Vulnerability Lab supports high-quality penetration testing and
the evaluation of new offensive and defensive technologies for our customers.
Hence our customers obtain the most current information about vulnerabilities
and valid recommendation about the risk profile of new technologies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Interested to work with the experts of SEC Consult?
Send us your application https://sec-consult.com/career/

Interested in improving your cyber security with the experts of SEC Consult?
Contact our local offices https://sec-consult.com/contact/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mail: security-research at sec-consult dot com
Web: https://www.sec-consult.com
Blog: https://blog.sec-consult.com
Twitter: https://twitter.com/sec_consult

EOF Daniel Hirschberger / @2024
```

[![](att-4/xss.png)](att-4/xss.png)

**Attachment:
[smime.p7s](att-4/smime_p7s.bin)**
*Description:* S/MIME Cryptographic Signature

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

* **SEC Consult SA-20241211-0 :: Reflected Cross-Site Scripting in Numerix License Server Administration System Login** *SEC Consult Vulnerability Lab via Fulldisclosure (Dec 12)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [Breac...