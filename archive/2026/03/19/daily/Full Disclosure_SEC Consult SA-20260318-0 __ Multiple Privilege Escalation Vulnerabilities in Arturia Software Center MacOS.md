---
title: SEC Consult SA-20260318-0 :: Multiple Privilege Escalation Vulnerabilities in Arturia Software Center MacOS
url: https://seclists.org/fulldisclosure/2026/Mar/9
source: Full Disclosure
date: 2026-03-19
fetch_date: 2026-03-20T04:09:29.839507
---

# SEC Consult SA-20260318-0 :: Multiple Privilege Escalation Vulnerabilities in Arturia Software Center MacOS

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20260318-0 :: Multiple Privilege Escalation Vulnerabilities in Arturia Software Center MacOS

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 18 Mar 2026 15:39:22 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20260318-0 >
=======================================================================
              title: Multiple Privilege Escalation Vulnerabilities
            product: Arturia Software Center MacOS
 vulnerable version: 2.12.0.3157
      fixed version: -
         CVE number: CVE-2026-24062, CVE-2026-24063
             impact: high
           homepage:https://www.arturia.com/technology/asc
              found: 2026-01-02
                 by: Florian Haselsteiner (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Atos business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"We create instruments and effects that encourage musical discovery,
reward curiosity, and savor the artistic process. We’re an international
team of passionate people, on a mission to navigate uncharted sonic territory
in the name of creative empowerment.
From the raw analog power of Brute synthesizers to our faithful virtual
instrument emulations of V Collection, we provide musicians with an inspiring
sonic experience that's instantly accessible, exploratory, and thrilling."

Source:https://www.arturia.com/company

Business recommendation:
------------------------
The vendor was unresponsive and did not respond to any of our communication
attempts. Therefore, a patch is not available. In case you are using this
product, please approach the vendor and demand a fix.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Insufficient XPC Client validation (CVE-2026-24062)
It was found that the "Privileged Helper" component of the Arturia Software
Center does not perform sufficient client code signature validation when a
client connects. This leads to an attacker being able to connect to the helper
and execute privileged actions leading to local privilege escalation.

2) World writable uninstall.sh script executed by root (CVE-2026-24063)
It was found that when a plugin is installed using the Arturia Software Center,
that this plugin also installs an uninstall.sh bash script in a root owned path.
This script is written to disk with the file permissions 777, meaning it is
writable by any user. When uninstalling a plugin via the Arturia Software Center
the Privileged Helper gets instructed to execute this script.
When the bash script is manipulated by an attacker this scenario will lead
to privilege escalation.

Proof of concept:
-----------------
1) Insufficient XPC Client validation (CVE-2026-24062)
The Privileged Helper service does not check if the connecting client
is signed with a valid code signature. Any process can connect to the
privileged helper and trigger privileged actions.

The following C code can be used to connect to the privileged helper and
trigger code execution as root. By first using the FINISHM command to achieve
/Library/Arturia being a symlink to /tmp/test and then triggering an UNINSTA
of /Library/Arturia/uninstall.sh, the attacker controlled bash script in
/tmp/test/uninstall.sh will get executed by root. The following example proof
of concept sets up the /tmp/test directory as well as the
/tmp/test/uninstall.sh script containing commands to add the user lowpriv
to the sudoers file.
-----------------
[ PoC exploit code removed ]
-----------------

The code can be compiled using clang:
-----------------
clang -o exploit exploit.c
-----------------

And then be executed like:
-----------------
./exploit com.Arturia.InstallHelper
-----------------

This will trigger execution of /tmp/test/uninstall.sh as root
leading to privilege escalation.

2) World writable uninstall.sh script executed by root (CVE-2026-24063)
When a vst is installed via the ASC the following path will be generated:
-----------------
/Library/Arturia/Acid V/Acid V.vst3/Contents/Resources
-----------------
The following contents are installed:
-----------------
user@usersVilMachine Resources % ls -al
total 8
drwxrwxrwx  3 root  wheel    96 Oct  9 09:27 .
drwxrwxrwx  7 root  wheel   224 Oct  9 09:27 ..
-rwxrwxrwx  1 root  wheel  3315 Oct  9 09:26 uninstall.sh
user@usersVilMachine Resources % pwd
/Library/Arturia/Acid V/Acid V.vst3/Contents/Resources
-----------------
When uninstalling the same software via the ASC the following XPC message
is sent to the InstallHelper:
-----------------
UNINSTA /Library/Arturia/Acid V/Acid V.vst3/Contents/Resources/uninstall.sh
-----------------
This will trigger execution of the uninstall.sh file as root.
The uninstallation can either be triggerd by exploiting the missing
XPC client authentication of the Privileged Helper or by manually
triggering the uninstall via the UI.

Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
* 2.12.0.3157

All tests have been performed on MacOS 26.2 with SIP enabled!

Vendor contact timeline:
------------------------
2026-01-05: Contacting vendor throughinfo () arturia com; no response.
2026-01-27: Contacting vendor through contact form. Got error, "Support out of reach!"
2026-01-27: Contact via contact form again, seems to have a bug.
2026-01-27: Contact viainfo () arturia com andwebmaster () arturia com; no response.
2026-02-03: Tried to contact vendor via contact form after login. Got same error.
2026-02-03: Contact viasales.support () arturia com; no response.
2026-02-24: Tried to contact vendor via contact form, again same error.
2026-02-25: Contact viaprivacy-inquiries () arturia com; no response.
2026-03-18: Public release of advisory.

Solution:
---------
The vendor was unresponsive and did not respond to any of our communication
attempts. Therefore, a patch is not available. In case you are using this
product, please approach the vendor and demand a fix.

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
and valid recommendation ab...