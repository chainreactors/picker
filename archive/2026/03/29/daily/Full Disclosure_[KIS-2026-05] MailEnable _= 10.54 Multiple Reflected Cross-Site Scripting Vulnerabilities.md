---
title: [KIS-2026-05] MailEnable <= 10.54 Multiple Reflected Cross-Site Scripting Vulnerabilities
url: https://seclists.org/fulldisclosure/2026/Mar/15
source: Full Disclosure
date: 2026-03-29
fetch_date: 2026-03-30T04:46:59.685760
---

# [KIS-2026-05] MailEnable <= 10.54 Multiple Reflected Cross-Site Scripting Vulnerabilities

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

# [KIS-2026-05] MailEnable <= 10.54 Multiple Reflected Cross-Site Scripting Vulnerabilities

---

*From*: Egidio Romano <n0b0d13s () gmail com>
*Date*: Mon, 23 Mar 2026 17:35:58 +0100

---

```
---------------------------------------------------------------------------
MailEnable <= 10.54 Multiple Reflected Cross-Site Scripting Vulnerabilities
---------------------------------------------------------------------------

[-] Software Link:

https://www.mailenable.com

[-] Affected Versions:

Version 10.54 and prior versions.

[-] Vulnerabilities Description:

1) Vulnerable code in ManageShares.aspx

User input passed through the "SelectedIndex" GET parameter to the
/Mondo/lang/sys/Forms/ManageShares.aspx page is not properly sanitized
before being used to generate JavaScript code, allowing an attacker to
break out of the existing function and inject arbitrary JavaScript.
This can be exploited by attackers to perform Reflected Cross-Site
Scripting (XSS) attacks.

Proof of Concept:
https://[MailEnable_WebMail]/Mondo/lang/sys/Forms/ManageShares.aspx?SelectedIndex=%27;}alert(%27XSS%27);function%20x(){return%27

An attacker can use a crafted link like the one above to trick a
victim user into issuing a request containing a malicious payload. The
application reflects unsanitized input into JavaScript code, enabling
execution of arbitrary script in the victim's browser.

2) Vulnerable code in FreeBusy.aspx

User input passed through the "Attendees" GET parameter to the
/Mondo/lang/sys/Forms/CAL/FreeBusy.aspx page is not properly sanitized
before being used to generate JavaScript code, allowing an attacker to
break out of the existing function and inject arbitrary JavaScript.
This can be exploited by attackers to perform Reflected Cross-Site
Scripting (XSS) attacks.

Proof of Concept:
https://[MailEnable_WebMail]/Mondo/lang/sys/Forms/CAL/FreeBusy.aspx?Attendees=%27);}alert(%27XSS%27);function%20x(){return%20x(%27

An attacker can use a crafted link like the one above to trick a
victim user into issuing a request containing a malicious payload. The
application reflects unsanitized input into JavaScript code, enabling
execution of arbitrary script in the victim's browser.

3) Vulnerable code in FreeBusy.aspx

User input passed through the "StartDate" GET parameter to the
/Mondo/lang/sys/Forms/CAL/FreeBusy.aspx page is not properly sanitized
before being used to generate JavaScript code, allowing an attacker to
break out of the existing function and inject arbitrary JavaScript.
This can be exploited by attackers to perform Reflected Cross-Site
Scripting (XSS) attacks.

Proof of Concept:
https://[MailEnable_WebMail]/Mondo/lang/sys/Forms/CAL/FreeBusy.aspx?StartDate=%27);}alert(%27XSS%27);function%20x(){return%20x(%27

An attacker can use a crafted link like the one above to trick a
victim user into issuing a request containing a malicious payload. The
application reflects unsanitized input into JavaScript code, enabling
execution of arbitrary script in the victim's browser.

[-] Solution:

Upgrade to version 10.55 or later.

[-] Disclosure Timeline:

[24/02/2026] - Vendor notified

[02/03/2026] - Vendor released version 10.55, including fixes for
these vulnerabilities

[02/03/2026] - CVE identifier requested

[23/03/2026] - Public disclosure

[-] CVE Reference:

The Common Vulnerabilities and Exposures project (cve.org) has not
assigned a CVE identifier for these vulnerabilities.

[-] Credits:

Vulnerabilities discovered by Egidio Romano.

[-] Other References:

https://www.mailenable.com/rss/article.asp?Source=RSSADMIN&ID=MAILENABLEVERSION1055

[-] Original Advisory:

https://karmainsecurity.com/KIS-2026-05
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **[KIS-2026-05] MailEnable <= 10.54 Multiple Reflected Cross-Site Scripting Vulnerabilities** *Egidio Romano (Mar 28)*

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