---
title: [webapps] RiteCMS 3.0.0 - Reflected Cross Site Scripting (XSS)
url: https://www.exploit-db.com/exploits/52413
source: Exploit-DB.com RSS Feed
date: 2025-08-19
fetch_date: 2025-10-07T00:16:19.881320
---

# [webapps] RiteCMS 3.0.0 - Reflected Cross Site Scripting (XSS)

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

# RiteCMS 3.0.0 - Reflected Cross Site Scripting (XSS)

#### EDB-ID:

###### 52413

#### CVE:

###### [2024-28623](https://nvd.nist.gov/vuln/detail/CVE-2024-28623)

---

**EDB Verified:**

#### Author:

###### [Gurjot Singh](/?author=12306)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-08-18

---

**Vulnerable App:**

```
# Exploit Title: RiteCMS 3.0.0 – Reflected Cross-Site Scripting (XSS)
# Google Dork: N/A
# Date: 2024-08-12
# Exploit Author: GURJOT SINGH
# Vendor Homepage: https://ritecms.com/
# Software Link: https://github.com/handylulu/RiteCMS/releases/download/V3.0.0/ritecms.v3.0.0.zip
# Version: <= 3.0.0
# Tested on: Ubuntu 22.04 LTS, PHP 8.1, Apache 2.4
# CVE: CVE-2024-28623

## Description:
A reflected Cross-Site Scripting (XSS) vulnerability exists in RiteCMS v3.0.0 within the `main_menu/edit_section` parameter.
An attacker can inject arbitrary JavaScript code that will execute in the context of the victim's browser session.

## Impact:
- Theft of credentials or session tokens
- Phishing or malicious redirection
- Full control over the victim’s active browser session

## Proof of Concept (PoC):

Payload:
'"><svg/onload=confirm(/xsss/)>

Steps:
1. Log in or navigate to the vulnerable `main_menu/edit_section` functionality.
2. Inject the above payload into the vulnerable parameter.
3. Observe the execution of the injected JavaScript.

Video PoC:
https://github.com/GURJOTEXPERT/ritecms/blob/main/POC.mp4

Full write-up & repository:
https://github.com/GURJOTEXPERT/ritecms

## Mitigation:
- Implement strict input validation and output encoding.
- Enforce a Content Security Policy (CSP) to limit script execution.
- Update RiteCMS to a patched version when available.
```

**Tags:**

**Advisory/Source:**
Link

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
unintentional misconfiguration on the part of a user or a program installed by the user.
Over time, the term “dork” became shorthand for a search query that located sensitive
information and “dorks” were included with may web application vulnerability releases to
show examples of vulnerable web sites.

After nearly a decade of hard work by the community, Johnny turned the GHDB
over to [OffSec](https://www.offsec.com/community-projects/?utm_source=edb&utm_medium=web&utm_campaign=www) in November 2010, and it is now maintained as
an extension of the [Exploit Database](/). Today, the GHDB includes searches for
other online search engines such as [Bing](https://www.bing.com/),
and other online repos...