---
title: [local] GeoVision ASManager Windows Application 6.1.2.0 - Credentials Disclosure
url: https://www.exploit-db.com/exploits/52423
source: Exploit-DB.com RSS Feed
date: 2025-08-27
fetch_date: 2025-10-07T00:47:57.357567
---

# [local] GeoVision ASManager Windows Application 6.1.2.0 - Credentials Disclosure

[![Exploit Database](/images/spider-white.png)](/)
[Exploit Database](/)

* [Exploits](/)
* [GHDB](/google-hacking-database)
* [Papers](/papers)
* [Shellcodes](/shellcodes)

---

* [Search EDB](/search)
* [SearchSploit Manual](/searchsploit)
* [Submissions](/submit)

---

* [Online Training](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)

[![Exploit Database](/images/edb-logo.png)](/)

* [Stats](/exploit-database-statistics)
* [About Us](/)

  [About Exploit-DB](/about-exploit-db)
  [Exploit-DB History](/history)
  [FAQ](/faq)
* Search

# GeoVision ASManager Windows Application 6.1.2.0 - Credentials Disclosure

#### EDB-ID:

###### 52423

#### CVE:

###### [2025-26263](https://nvd.nist.gov/vuln/detail/CVE-2025-26263)

---

**EDB Verified:**

#### Author:

###### [Giorgi Dograshvili](/?author=11884)

#### Type:

###### [local](/?type=local)

---

#### Platform:

###### [Windows](/?platform=windows)

#### Date:

###### 2025-08-26

---

**Vulnerable App:**

```
# Exploit Title: GeoVision ASManager Windows Application 6.1.2.0 - Credentials Disclosure
# Date: 19-MAR-2025
# Exploit Author: Giorgi Dograshvili [DRAGOWN]
# Vendor Homepage: https://www.geovision.com.tw/
# Software Link: https://www.geovision.com.tw/download/product/
# Version: 6.1.2.0 or less
# Tested on: Windows 10 | Kali Linux
# CVE : CVE-2025-26263
# PoC: https://github.com/DRAGOWN/CVE-2025-26263

GeoVision ASManager Windows desktop application with the version 6.1.2.0 or less, is vulnerable to credentials disclosure due to improper memory handling in the ASManagerService.exe process.

Requirements
To perform successful attack an attacker requires:
- System level access to the GV-ASManager windows desktop application with the version 6.1.2.0 or less;
- A high privilege account to dump the memory.

Impact
The vulnerability can be leveraged to perform the following unauthorized actions:
- An attacker with high privilege system user, who isn't authorized to access GeoVision ASManager, is able to:
-- Dump ASManager accounts credentials;
-- Authenticate in ASManager.
- After the authenticating in ASManager, an attacker will be able to:
-- Access the resources such as monitoring cameras, access cards, parking cars, employees and visitors, etc.
-- Make changes in data and service network configurations such as employees, access card security information, IP addresses and configurations, etc.
-- Disrupt and disconnect services such as monitoring cameras, access controls.
-- Clone and duplicate access control data for further attack scenarios.

PoC
The steps for a successful exploitation are described in the following GitHub article with screenshots:
- https://github.com/DRAGOWN/CVE-2025-26263

After a successful attack, you will get administrative access to:
- ASManager - Access & Security Management software in OS
- ASWeb - Access & Security Management
- TAWeb - Time and Attendance Management
- VMWeb - Visitor Management
```

**Tags:**

**Advisory/Source:**
[Link](https://github.com/DRAGOWN/CVE-2025-26263)

| **Databases** | **Links** | **Sites** | **Solutions** |
| --- | --- | --- | --- |
| [Exploits](/) | [Search Exploit-DB](/search) | [OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) | [Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Google Hacking](/google-hacking-database) | [Submit Entry](/submit) | [Kali Linux](https://www.kali.org/) | [Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Papers](/papers) | [SearchSploit Manual](/serchsploit) | [VulnHub](https://www.vulnhub.com/) | [OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www) |
| [Shellcodes](/shellcodes) | [Exploit Statistics](/statistics) |  | [Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www) |
|  |  |  | [Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) |

Databases

[Exploits](/)
[Google Hacking](/google-hacking-database)
[Papers](/papers)
[Shellcodes](/shellcodes)

Links

[Search Exploit-DB](/search)
[Submit Entry](/submit)
[SearchSploit Manual](/searchsploit)
[Exploit Statistics](/statistics)

Sites

[OffSec](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Kali Linux](https://www.kali.org/)
[VulnHub](https://www.vulnhub.com/)

Solutions

[Courses and Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Learn Subscriptions](https://www.offsec.com/learn/?utm_source=edb&utm_medium=web&utm_campaign=www)
[OffSec Cyber Range](https://www.offsec.com/cyber-range/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Proving Grounds](https://www.offsec.com/labs/?utm_source=edb&utm_medium=web&utm_campaign=www)
[Penetration Testing Services](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www)

* [Exploit Database by OffSec](/)
* [Terms](/terms)
* [Privacy](/privacy)
* [About Us](/about-exploit-db)
* [FAQ](/faq)
* [Cookies](/cookies)

©
[OffSec Services Limited](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) 2025. All rights reserved.

##### About The Exploit Database

×

[![OffSec](/images/offsec-logo.png)](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)
The Exploit Database is maintained by [OffSec](https://www.offsec.com/community-projects/?utm_source=edb&utm_medium=web&utm_campaign=www), an information security training company
that provides various [Information Security Certifications](https://www.offsec.com/courses-and-certifications/?utm_source=edb&utm_medium=web&utm_campaign=www) as well as high end [penetration testing](https://www.offsec.com/penetration-testing/?utm_source=edb&utm_medium=web&utm_campaign=www) services. The Exploit Database is a
non-profit project that is provided as a public service by OffSec.

The Exploit Database is a [CVE
compliant](http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html) archive of public exploits and corresponding vulnerable software,
developed for use by penetration testers and vulnerability researchers. Our aim is to serve
the most comprehensive collection of exploits gathered through direct submissions, mailing
lists, as well as other public sources, and present them in a freely-available and
easy-to-navigate database. The Exploit Database is a repository for exploits and
proof-of-concepts rather than advisories, making it a valuable resource for those who need
actionable data right away.

The [Google Hacking Database (GHDB)](/google-hacking-database)
is a categorized index of Internet search engine queries designed to uncover interesting,
and usually sensitive, information made publicly available on the Internet. In most cases,
this information was never meant to be made public but due to any number of factors this
information was linked in a web document that was crawled by a search engine that
subsequently followed that link and indexed the sensitive information.

The process known as “Google Hacking” was popularized in 2000 by Johnny
Long, a professional hacker, who began cataloging these queries in a database known as the
Google Hacking Database. His initial efforts were amplified by countless hours of community
member effort, documented in the book Google Hacking For Penetration Testers and popularised
by a barrage of media attention and Johnny’s talks on the subject such as this early talk
recorded at [DEFCON 13](https://www.defcon.org/html/links/dc-archives/dc-13-archive.html). Johnny coined the term “Googledork” to refer
to “a foolish or inept person as revealed by Google“. This was meant to draw attention to
the fact that this was not a “Google problem” but rather the result of an often
unintentional misconfiguration on the part of a user or a prog...