---
title: SEC Consult SA-20260615-0 :: Multiple Critical Vulnerabilities in Wertheim SafeController Software for VAULT ROOMS (Safe Deposit Locker System)
url: https://seclists.org/fulldisclosure/2026/Jun/8
source: Full Disclosure
date: 2026-06-16
fetch_date: 2026-06-17T07:04:07.726450
---

# SEC Consult SA-20260615-0 :: Multiple Critical Vulnerabilities in Wertheim SafeController Software for VAULT ROOMS (Safe Deposit Locker System)

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

# SEC Consult SA-20260615-0 :: Multiple Critical Vulnerabilities in Wertheim SafeController Software for VAULT ROOMS (Safe Deposit Locker System)

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 15 Jun 2026 12:06:21 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260615-0 >
=======================================================================
              title: Multiple Critical Vulnerabilities
            product: Wertheim SafeController Software for VAULT ROOMS
                     (Safe Deposit Locker System)
 vulnerable version: AssemblyVersion 6.15.8328.28014
      fixed version: No information provided by vendor
         CVE number: CVE-2026-34023, CVE-2026-34024, CVE-2026-34025,
                     CVE-2026-34026, CVE-2026-34027, CVE-2026-34028,
                     CVE-2026-34029, CVE-2026-34030
             impact: critical
           homepage:https://wertheim-safes.com/safe-deposit-box-management/
              found: 2023-04-03
                 by: Christian Hager (Office Vienna)
                     Gorazd Jank (Office Vienna)
                     Philipp Espernberger (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"On September 1, 1852, Franz Wertheim and 85 employees began to build "fireproof safes".
Then as now, Wertheim has been successfully involved in production of safes and banking
facilities, nationally and internationally. To secure the market position and develop
new business areas, Wertheim has continuously adapted its product range over the years
as well as expanded its assortment of offerings. Today, the Wertheim Group of companies
also produces bank and object furnishings in our own joinery in Uttendorf, and
Commissioned Work has developed into an essential business area for the group. The
diversity of state-of-the-art technologies characterizes the flexibility and technical
know-how of this division."

Source:https://wertheim.at/en/company/ (2023)

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately. Specific version
information was not provided. Please contact the vendor in order to request the
update.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Violation of the Least-Privilege Principle
The application service is running in the context of a highly privileged user. An
attacker managing to compromise the affected service, can run commands with
these privileges.
This vulnerability is not a direct Wertheim vulnerability but rather an installation
problem. However, due to the following issues, an attacker would be able to exploit
this problem and carry out actions with the permissions of the service account.

2) Broken WebSocket Authorization (CVE-2026-34023)
Due to flaws in the authorization scheme, an authorization bypass vulnerability
allows an attacker to get access to restricted functions and resources in other
branches via the established WebSocket communication. To perform this attack an
attacker has to be in the possession of valid user credentials of a low privileged
branch user.

3) Broken access control (CVE-2026-34024)
In the tested system multiple endpoints where identified which do not perform
authorization checks. These endpoints may not be visible in the frontend but can
be accessed anyway. This enables authenticated users with minimal privileges to,
among others, perform the following actions:
* Switch the user's branch
* Upload arbitrary files
* Download arbitrary files
* View details of an arbitrary branch

4) IP Restriction Bypass (CVE-2026-34025)
The web application restricts user logins based on the specific IP address
associated to the branch's location. It was identified that the IP restriction
can be bypassed by manipulating HTTP requests during the login process.

5) Path traversal (CVE-2026-34026)
Due to insufficient application-side input validation, it is possible to
request arbitrary files, accessible by the affected application, using a path
traversal attack. This includes but is not limited to application-specific
log files containing sensitive information. An existing session is required for
this attack. However, it does not matter which role or permissions the utilized
user possesses (see vulnerability 3).

6) Upload Restriction Bypass (CVE-2026-34027)
As a result of insufficient application-side filetype validation it is possible
to upload arbitrary files. An existing session is required to exploit this
vulnerability. However, it does not matter which role or permissions the
utilized user possesses (see vulnerability 3).

7) Unauthenticated Access to Web Data (CVE-2026-34028)
An attacker has the ability to directly access HTTP endpoints which are not
protected by any authorization scheme. The attacker is able to directly
download files and execute binaries which are stored on the specific file path.

8) Hardcoded Secrets in DLL files (CVE-2026-34029)
Application components were identified storing sensitive data in an insecure
non-cryptographically protected format. An attacker with access to the application
files can reverse engineer them and read out the hardcoded secrets.

9) Insufficient input validation (CVE-2026-34030)
When a new branch is added to a company the chosen branch code is not validated
correctly and therefore malicious symbols can be injected into it. This enables
a malicious user to attack functions which actively use the branch code. The
branch code is used in multiple occasions. Possible attacks include, but are
not limited to, Cross-Site Scripting (XSS), path traversal attacks and all
types of injections (OS Command, SQL, etc.).
Special privileges ("settings_branches_manage") are needed to create a new
branch. Privileges can be elevated using the vulnerability described in
3 and 5.

10) Undisclosed Vulnerability
This vulnerability was identified during a reassessment commissioned by Wertheim.
Detailed disclosure is withheld as the finding is subject to the vendor's ownership
and disclosure authority. Affected parties are advised to contact the vendor
directly for further information.

The combination of 3), 5), 6), 7) and 9) leads to an authenticated remote code
execution. If the service is running with high privileges (see 1), an attacker
is able to fully compromise the whole server. The detailed proof-of-concept is
shown in the chapter "Attack Chain" below.

Proof of concept:
-----------------
1) Violation of the Least-Privilege Principle
To verify the vulnerability, it is sufficient to search for the name "Wertheim
Message Broker" in the list of running services. This can be done e.g., by
using the "Windows Task Manager" and switching to the tab "Services". The tab
shows the runni...