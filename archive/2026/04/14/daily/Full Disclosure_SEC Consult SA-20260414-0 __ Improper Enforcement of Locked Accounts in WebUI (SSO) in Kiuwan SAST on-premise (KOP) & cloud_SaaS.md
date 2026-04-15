---
title: SEC Consult SA-20260414-0 :: Improper Enforcement of Locked Accounts in WebUI (SSO) in Kiuwan SAST on-premise (KOP) & cloud/SaaS
url: https://seclists.org/fulldisclosure/2026/Apr/5
source: Full Disclosure
date: 2026-04-14
fetch_date: 2026-04-15T04:44:14.206601
---

# SEC Consult SA-20260414-0 :: Improper Enforcement of Locked Accounts in WebUI (SSO) in Kiuwan SAST on-premise (KOP) & cloud/SaaS

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260414-0 :: Improper Enforcement of Locked Accounts in WebUI (SSO) in Kiuwan SAST on-premise (KOP) & cloud/SaaS

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 14 Apr 2026 10:31:18 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260414-0 >
=======================================================================
              title: Improper Enforcement of Locked Accounts in WebUI (SSO)
            product: Kiuwan SAST on-premise (KOP) & cloud/SaaS
 vulnerable version: <2.8.2509.4
      fixed version: 2.8.2509.4
         CVE number: CVE-2026-24069
             impact: medium
           homepage:https://www.kiuwan.com/
              found: 2025-03-31
                 by: Bernhard Gründling (Office Vienna)
                     Fabian Würfl (Office Vienna)
                     Johannes Greil (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Thorough code inspection is essential for designing secure software products.
While your development team may not have time to comb through every line of code,
Kiuwan does. For 20 years, it has been the choice of developers to scan code
automatically and remediate defects according to security standards like OWASP,
CWE, SANS, and CERT.

Static application security testing (SAST) scans for security flaws in the source
code without running the program. It is a white-box testing method that is the
counterpart to dynamic application software testing (DAST), which tests web applications
for run-time vulnerabilities. [...]"

Source:https://www.kiuwan.com/code-security-sast/

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Improper Enforcement of Locked Accounts in WebUI (SSO) (CVE-2026-24069)
Kiuwan offers the possibility to enable single sign-on (SSO) for authentication,
e.g. through Microsoft ADFS or Azure to authenticate against an active directory.
It needs to map the AD user accounts with locally configured accounts for
authorization purposes, e.g. to configure the roles and access to applications.
SSO users have the local logon disabled and there is no password set, authentication
only works via SSO then.

It was found out that the user is still able to login at the Kiuwan WebUI via SSO,
even if the Kiuwan mapped account has been disabled in the user settings by an admin.
The login does not work in the scanner agent (KLA - Kiuwan Local Analyzer) though.
There the authorization check seems to be verifying the validity of the account first
and throws the error message "Failed to authenticate using Single sign-on".

Proof of concept:
-----------------
1) Improper Enforcement of Locked Accounts in WebUI (SSO) (CVE-2026-24069)
No specific PoC is necessary. An SSO login is possible even after disabling
the Kiuwan mapped user account in the Kiuwan user admin settings.
Steps to reproduce:
a) Disable user in Kiuwan user settings
b) Authenticate via SSO, e.g. through Microsoft ADFS
c) Login is possible in the Kiuwan WebUI

Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
* 2.8.2412.0

Vendor contact timeline:
------------------------
2025-04-02: Contacting vendor through official Kiuwan ticket system
            (https://kiuwan.zendesk.com)
            Kiuwan support responds that they will take a look into
            our submission. Support sends us a few details regarding
            SSO authentication.
2025-04-03: Informing the vendor that we know how SSO auth in Kiuwan
            works and our vulnerability exploits the improper enforcement
            of locked accounts.
2025-04-15: Vendor informs us that the issue has been escalated to R&D.
2025-07-29: Vendor has resolved the issue in the latest Kiuwan Cloud release.
2025-07-29: Asking the vendor regarding the fix for Kiuwan On-Premise.
            Vendor responds that it is currently being tested for KOP and
            they will inform us.
2025-11-03: Asking for a status update as we were not informed yet.
2025-11-10: Support team responds that KOP release is expected within the
            next couple of weeks.
2025-11-24: Issue has been resolved in the latest KOP release.
2025-11-28: Informing vendor that we cannot upgrade/verify the KOP release yet,
            scheduled for 2026.
2026-04-14: Public release of advisory.

Solution:
---------
The security issue has been fixed by the vendor on 29th July 2025 for the
Kiuwan Cloud solution.

The vendor provides a patch for the Kiuwan On-Premises version 2.8.2509.4
which can be downloaded from the vendor's installation page:
https://support.kiuwan.com/hc/en-us/articles/36356787260433-Kiuwan-On-Premises-Distributed-Installation-Guide

Workaround:
-----------
None

Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos business
Europe | Asia

About SEC Consult Vulnerability Lab
The SEC Consult Vulnerability Lab is an integrated part of SEC Consult, an
Atos business. It ensures the continued knowledge gain of SEC Consult in the
field of network and application security to stay ahead of the attacker. The
SEC Consult Vulnerability Lab supports high-quality penetration testing and
the evaluation of new offensive and defensive technologies for our customers.
Hence our customers obtain the most current information about vulnerabilities
and valid recommendation about the risk profile of new technologies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Interested to work with the experts of SEC Consult?
Send us your applicationhttps://sec-consult.com/career/

Interested in improving your cyber security with the experts of SEC Consult?
Contact our local officeshttps://sec-consult.com/contact/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mail: security-research at sec-consult dot com
Web:https://www.sec-consult.com
Blog:https://blog.sec-consult.com
X:https://x.com/sec_consult

EOF Bernhard Gründling, Johannes Greil, Fabian Würfl / @2026
```

**Attachment:
[smime.p7s](att-5/smime_p7s.bin)**
*Description:* S/MIME Cryptographic Signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![P...