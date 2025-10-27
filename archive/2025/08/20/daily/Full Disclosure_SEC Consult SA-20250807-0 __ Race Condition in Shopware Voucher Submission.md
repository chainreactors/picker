---
title: SEC Consult SA-20250807-0 :: Race Condition in Shopware Voucher Submission
url: https://seclists.org/fulldisclosure/2025/Aug/17
source: Full Disclosure
date: 2025-08-20
fetch_date: 2025-10-07T00:51:00.332178
---

# SEC Consult SA-20250807-0 :: Race Condition in Shopware Voucher Submission

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

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20250807-0 :: Race Condition in Shopware Voucher Submission

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 7 Aug 2025 08:34:32 +0000

---

```
Confidentiality class: Internal & Partner

SEC Consult Vulnerability Lab Security Advisory < publishing date 20250807-0 >
=======================================================================
              title: Race Condition in Shopware Voucher Submission
            product: Shopware 6
 vulnerable version: v6.6.10.4
      fixed version: No fixed version available yet
         CVE number: CVE-2025-7954
             impact: medium
           homepage: https://github.com/shopware/shopware
              found: 2025-04-14
                 by: Timo Müller (Office Munich)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Shopware 6 is an open commerce platform based on Symfony Framework and Vue
and supported by a worldwide community and more than 1.500 community extensions"

Source: https://github.com/shopware/shopware

Business recommendation:
------------------------
The vendor has not yet provided a patch for this vulnerability but has
already publicized it through a GitHub issue. Please check the "Workaround"
section of this advisory for up to date recommended mitigation measures.

Vulnerability overview/description:
-----------------------------------
1) Race Condition in Shopware Voucher Submission (CVE-2025-7954)
A race condition exists within the voucher system of the Shopware Core.
Successful exploitation of this vulnerability allows an attacker
to bypass voucher usage limits during the checkout process. This vulnerability
exists due to the fact that validation of voucher codes is not an
atomic operation. Due to this, limited vouchers can be used in
multiple simultaneous checkouts.

In the worst case an attacker can abuse this vulnerability to use
generated vouchers over their pre-set usability limit.

Proof of concept:
-----------------
1) Race Condition in Shopware Voucher Submission (CVE-2025-7954)

Successful exploitation of this issue requires access to a valid
restricted (e.g. one-time use) voucher.
Further information about the exploitation process is withheld until
an official patch by Shopware is available.

Vulnerable / tested versions:
-----------------------------
The following version has been tested, which was the latest version available
at the time of the vulnerability submission:
* v6.6.10.4

Vendor contact timeline:
------------------------
2025-05-09: Contacting vendor through the security reporting form at
https://www.shopware.com/en/contact/security-reporting/
2025-05-21: Asking for a status update, whether our form submission was received.
            Vendor confirms receipt.
2025-07-15: Asking for a another status update including a request for a rough patch timeline
2025-07-15: Vendor classifies this vulnerability as a not security-relevant bug.
They also discloses this "bug" as a Shopware GitHub issue https://github.com/shopware/shopware/issues/11245
2025-07-15: Asking the vendor for a statement, why this submission is not rated as security-relevant
2025-07-15: The vendor does not rate this issue as security-relevant because
merchants can recognize and cancel malicious orders
2025-07-25: Informing vendor that we will publish the finding, too. (Vendor already published it via Github)
2025-08-07: Publishing advisory.

Solution:
---------
No official patch is currently available for this vulnerability.
Patch availability status can be tracked via the GitHub issue at
https://github.com/shopware/shopware/issues/11245

Workaround:
-----------
Until a patch is available, vouchers with usage limits should not be used.
Such vouchers are:
* one-time vouchers
* vouchers with a restricted amount of activations

If vouchers with usage limits are used, it is suggested to review any
orders connected to these vouchers for suspicious activity.

Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/

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
Twitter: https://x.com/sec_consult

EOF Timo Müller - 2025

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](16)
[By Date](date.html#17)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#17)
[![Next](/images/right-icon-16x16.png)](18)

### Current thread:

* **SEC Consult SA-20250807-0 :: Race Condition in Shopware Voucher Submission** *SEC Consult Vulnerability Lab via Fulldisclosure (Aug 18)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanner...