---
title: CVE‑2025‑52187 – Stored XSS in School Management System (PHP/MySQL)
url: https://seclists.org/fulldisclosure/2025/Jul/28
source: Full Disclosure
date: 2025-07-31
fetch_date: 2025-10-06T23:56:50.073829
---

# CVE‑2025‑52187 – Stored XSS in School Management System (PHP/MySQL)

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

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

![](/shared/images/nst-icons.svg#search)

# CVE‑2025‑52187 – Stored XSS in School Management System (PHP/MySQL)

---

*From*: Sanjay Singh <sanjay70023 () gmail com>
*Date*: Tue, 22 Jul 2025 18:16:43 +0530

---

```
Hello Full Disclosure community,

I’m sharing details of a recently assigned CVE affecting a widely used
open‑source School Management System (PHP/MySQL).

--------------------------------------------
CVE ID: CVE‑2025‑52187
Vulnerability Type: Stored Cross‑Site Scripting (XSS)
Attack Vector: Remote
Discoverer: Sanjay Singh
Vendor Repository:
https://github.com/GetProjectsIdea/Create-School-Management-System-with-PHP-MySQL
Version Tested: 1.0
--------------------------------------------

Description:
The application fails to properly sanitize user-supplied input in
`my_profile_update_form1.php` before storing it in the database. When the
stored data is later rendered on pages such as `get_student_profile.php` or
`dashboard1.php`, embedded JavaScript code executes in the context of the
victim’s browser.

Impacts:
• Session hijacking
• Data exfiltration
• Phishing and fake login forms
• Keystroke logging
• Defacement
• Privilege escalation if viewed by an administrator

--------------------------------------------
Proof of Concept (PoC):
1. Log in as a student user.
2. Navigate to the profile update form (`my_profile_update_form1.php`).
3. In an input field (e.g., Name With Initials), inject:
   <script>alert('XSS-PoC')</script>
4. Submit the form.
5. View the updated profile or dashboard (`get_student_profile.php` or
`dashboard1.php`) to trigger the payload.

--------------------------------------------
Mitigation Recommendations:
• Escape and sanitize all user input before storage/output (e.g., using
htmlspecialchars()).
• Implement a strict Content Security Policy (CSP).
• Perform code reviews and security audits.

Reference:
https://github.com/GetProjectsIdea/Create-School-Management-System-with-PHP-MySQL

This vulnerability has been responsibly disclosed and assigned
CVE‑2025‑52187. Full write‑up with additional details and mitigations is
available on Medium:

https://medium.com/@sanjay70023/cve-2025-52187-stored-xss-in-school-management-system-php-mysql-79cadcd6340f

If there are any questions or further information required, feel free to
reach out.

Best regards,
Sanjay Singh
Independent Security Researcher
LinkedIn <https://www.linkedin.com/in/sanjay70023/>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

### Current thread:

* **CVE‑2025‑52187 – Stored XSS in School Management System (PHP/MySQL)** *Sanjay Singh (Jul 29)*

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