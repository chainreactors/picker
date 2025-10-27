---
title: Intel Data Center Manager <= 5.1 Local Privileges Escalation
url: https://seclists.org/fulldisclosure/2022/Dec/2
source: Full Disclosure
date: 2022-12-10
fetch_date: 2025-10-04T01:09:09.113950
---

# Intel Data Center Manager <= 5.1 Local Privileges Escalation

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

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# Intel Data Center Manager <= 5.1 Local Privileges Escalation

---

*From*: "Julien Ahrens (RCE Security)" <info () rcesecurity com>
*Date*: Wed, 7 Dec 2022 09:10:26 +0000

---

```
RCE Security Advisory
https://www.rcesecurity.com

1. ADVISORY INFORMATION
=======================
Product:        Intel Data Center Manager
Vendor URL:     https://www.intel.com/content/www/us/en/developer/tools/data-center-manager-console/overview.html
Type:           Incorrect Use of Privileged APIs [CWE-648]
Date found:     2022-07-16
Date published: 2022-12-07
CVSSv3 Score:   7.4 (CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H)
CVE:            -

2. CREDITS
==========
This vulnerability was discovered and researched by Julien Ahrens from
RCE Security.

3. VERSIONS AFFECTED
====================
Intel Data Center Manager 5.1 (latest) and below

4. INTRODUCTION
===============
Energy costs are the fastest rising expense for today’s data centers. Intel® Data
Center Manager (Intel® DCM) provides real-time power and thermal consumption data,
giving you the clarity you need to lower power usage, increase rack density, and
prolong operation during outages.

(from the vendor's homepage)

5. VULNERABILITY DETAILS
========================
The latest version (5.1) and all prior versions of Intel's DCM are vulnerable to a
local privileges escalation vulnerability using the application user "dcm" used to
run the web application and the rest interface. An attacker who gained RCE using
this dcm user (i.e., through Log4j) is then able to escalate their privileges to
root by abusing a weak Sudo configuration for the "dcm" user:

dcm ALL=(ALL) NOPASSWD:/usr/local/bin/SDPTool
dcm ALL=(ALL) NOPASSWD:/usr/bin/cp
dcm ALL=(ALL) NOPASSWD:/usr/bin/chmod

The Intel Server Debug and Provisioning Tool (SDP Tool) must be installed for the
Data Center Manager to be vulnerable. Successful exploits can allow an authenticated
attacker to execute commands as root. In this way, the attacker can compromise the
victim system's entire confidentiality, integrity, and availability, thereby allowing
to persist within the attached network.

6. PROOF OF CONCEPT
===================
Just one way of exploitation is by replacing the current sudoers configuration:

1.Create a new sudoers configuration file using the compromised "dcm" user in i.e. /tmp/
2.sudo chmod 440 /tmp/sudoers
3.sudo cp sudoers /etc/sudoers
4.sudo /bin/bash

7. SOLUTION
===========
None. Intel thinks that this is not a vulnerability and therefore does also not assign
a CVE for it.

8. REPORT TIMELINE
==================
2022-07-16: Discovery of the vulnerability
2022-07-16: Reported to vendor via their bug bounty program
2022-07-18: Vendor response: Sent to "appropriate reviewers"
2022-07-26: Vendor states that the vulnerability "depends on something that does not exist (eg; RCE)."
2022-07-26: Sent a clarification that a compromise of the "dcm" account is indeed necessary, but there have been RCEs
in the past (i.e. through Log4j)
2022-09-22: Vendor has troubles to reproduce the bug and asks for another PoC
2022-09-22: Sent a clarification about the PoC
2022-09-22: Vendor states that the report "does not clearly demonstrate a vulnerability in DCM" and the report will be
closed.
2022-09-23: Provided the vendor with a PoC utilizing Log4shell (CVE-2021-44228) in a former version of DCM
2022-10-10: Vendor asks whether the Log4shell bug is still reproducible in the latest version of DCM
2022-10-10: Made clear that Log4shell is not the point about the report
2022-10-11: Vendor states "We do not clearly see a a vulnerability demonstrated in DCM"
2022-10-12: [Back and forth about the provided PoCs]
2022-10-12: I'm giving up.
2022-12-07: Public disclosure

9. REFERENCES
==============
https://github.com/MrTuxracer/advisories
```

**Attachment:
[signature.asc](att-2/signature_asc.bin)**
*Description:* Message signed with OpenPGP

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

### Current thread:

* **Intel Data Center Manager <= 5.1 Local Privileges Escalation** *Julien Ahrens (RCE Security) (Dec 08)*

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