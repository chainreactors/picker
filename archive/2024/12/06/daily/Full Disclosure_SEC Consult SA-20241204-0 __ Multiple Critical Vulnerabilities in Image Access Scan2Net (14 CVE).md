---
title: SEC Consult SA-20241204-0 :: Multiple Critical Vulnerabilities in Image Access Scan2Net (14 CVE)
url: https://seclists.org/fulldisclosure/2024/Dec/2
source: Full Disclosure
date: 2024-12-06
fetch_date: 2025-10-06T19:41:58.709994
---

# SEC Consult SA-20241204-0 :: Multiple Critical Vulnerabilities in Image Access Scan2Net (14 CVE)

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

# SEC Consult SA-20241204-0 :: Multiple Critical Vulnerabilities in Image Access Scan2Net (14 CVE)

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Dec 2024 09:52:38 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20241204-0 >
=======================================================================
              title: Multiple Critical Vulnerabilities
            product: Image Access Scan2Net
 vulnerable version: Firmware <=7.40, <=7.42, <7.42B
                     (depending on the vulnerability)
      fixed version: mostly fixed in v7.42B
         CVE number: CVE-2024-28138, CVE-2024-28139, CVE-2024-28140
                     CVE-2024-28141, CVE-2024-28142, CVE-2024-28143
                     CVE-2024-28144, CVE-2024-28145, CVE-2024-28146
                     CVE-2024-47946, CVE-2024-47947, CVE-2024-36498
                     CVE-2024-36494, CVE-2024-50584
             impact: critical
    vendor homepage: https://www.imageaccess.de/?page=SoftwareScan2Net&lang=en
       advisory URL: https://r.sec-consult.com/imageaccess
              found: 2023-06-22
                 by: Daniel Hirschberger (Office Bochum)
                     Tobias Niemann (Office Bochum)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"Scan2Net® - The Ultimate Scanning Technology
- Better than just another client software package
- Integrates into existing networks without additional drivers or PCs
- Unrivaled performance, highest security, low connectivity cost

The Scan2Net® platform is the technological foundation of all WideTEK® and
Bookeye® scanners from Image Access. It replaces the proprietary scanner drivers
and software that traditional scanners require with the fastest common,
nonproprietary connection available: TCP/IP over Ethernet. With network
interface speeds much higher than USB or SCSI, Scan2Net devices are able to
reach unrivaled performance at very low connectivity cost. The Linux based
operating system is dedicated to scanner specific imaging and mechanical control
tasks, further maximizing scanning speeds and performance."

Source: https://www.imageaccess.de/?page=SoftwareScan2Net&lang=en

Business recommendation:
------------------------
The vendor provides a firmware update to version 7.42B which should be installed
immediately. SEC Consult could only partially verify the correction of all
identified vulnerabilities. Some vulnerabilities have not been fixed by the
vendor as the risk was accepted.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) OS Command Injection (CVE-2024-28138)
An unauthenticated attacker with network access to the scanner can execute any
system command via the "msg_events.php" script as the www-data user.

2) Privilege Escalation (CVE-2024-28139)
The www-data user can elevate his privileges because sudo is configured to allow
the execution of the mount command as root without a password. Therefore, the
privileges can be escalated to the root user.

3) Violation of Least Privilege Principle (CVE-2024-28140)
The scanner boots into a kiosk mode by default and opens the Scan2Net interface
in a browser window. This browser is run with the permissions of the root user.
There are also several other applications running as root user, some of them are
self-developed ones but those could not be exploited at first glance.

4) Cross-Site Request-Forgery (CSRF) (CVE-2024-28141)
The web application is not protected against cross-site request forgery attacks.
Therefore, an attacker can trick users into performing actions on the
application when they visit an attacker-controlled website or click on a
malicious link.

5) Stored Cross-Site-Scripting (XSS) (CVE-2024-28142, CVE-2024-47947)
Due to missing input sanitization, an attacker can perform cross-site-scripting
attacks and run arbitrary Javascript in the browser of other users.

6) Insecure Password Change Function (CVE-2024-28143)
The password change function does not require the current password, which makes
the application vulnerable to account takeover, especially if combined with the
CSRF vulnerability.

7) Broken Access Control (CVE-2024-28144)
Due to missing access control on the reboot and shutdown functions, an attacker
can perform a denial-of-service attack against the application.
Furthermore, an attacker who can spoof the IP address and the User-Agent of a
logged-in user can takeover the session because of flaws in the self-developed
session management.

8) Unauthenticated SQL Injection (CVE-2024-28145)
An unauthenticated attacker can perform an SQL injection by accessing the
dbconnector.php file and supplying malicious GET parameters.

9) Hard-coded Credentials (CVE-2024-28146)
The application uses several hard-coded credentials for protecting the firmware
update file and the installed database server.

Update 2024-04-02:
------------------
ImageAccess GmbH provided us with an internet-facing test device and we spent
some short time verifying the vulnerabilities in their latest firmware (7.40)
which should fix the security issues according to the vendor.

Unfortunately, most of them are still present and new ones have been discovered.

In short:

1) OS Command Injection (CVE-2024-28138, CVE-2024-47946)
Fixed, but a new RCE vulnerability has been discovered which requires a session
as Poweruser, updated PoC below.
The second RCE issue is tracked as CVE-2024-47946.

2) Privilege Escalation (CVE-2024-28139)
Still an issue.

3) Violation of Least Privilege Principle (CVE-2024-28140)
Still an issue.

4) Cross-Site Request-Forgery (CSRF) (CVE-2024-28141)
Fixed. The introduced "session_id" cookie is protected with the "SameSite=Strict"
cookie flag. This prevents CSRF attacks.

5) Stored Cross-Site-Scripting (XSS) (CVE-2024-28142, CVE-2024-47947, CVE-2024-36498)
Original issues are fixed (CVE-2024-28142, CVE-2024-47947), but we discovered a
new one, updated PoC below. The new XSS is tracked as CVE-2024-36498.

6) Insecure Password Change Function (CVE-2024-28143)
Fixed. The password change function now requires the current password.

7) Broken Access Control (CVE-2024-28144)
Still an issue.
If two users access the web interface from the same IP they are logged in as the
other user. Updated PoC below.

8) Unauthenticated SQL Injection (CVE-2024-28145, CVE-2024-50584)
Original issue fixed, but a new blind SQLi as Poweruser has been found, updated
PoC below. The new SQLi is tracked as CVE-2024-50584.

9) Hard-coded Credentials (CVE-2024-28146)
Still an issue, credentials can be found in different files.

Update 2024-10-14:
------------------
ImageAccess GmbH provided us with an internet-facing test device and we spent
some short time verifying the vulnerabilities in their latest firmware (7...