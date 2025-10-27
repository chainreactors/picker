---
title: Deepseek writes textbook insecure code in 2025-01-28
url: https://seclists.org/fulldisclosure/2025/Jan/22
source: Full Disclosure
date: 2025-01-31
fetch_date: 2025-10-06T20:15:04.722852
---

# Deepseek writes textbook insecure code in 2025-01-28

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

# Deepseek writes textbook insecure code in 2025-01-28

---

*From*: Georgi Guninski <gguninski () gmail com>
*Date*: Tue, 28 Jan 2025 16:23:28 +0200

---

```
Asking Deepseek on Jan 28 09:33:11 AM UTC 2025:

Write a python CGI which takes as an argument string NAME and outputs
"Hello"+NAME

The Deepseek AI [3] returned:

====
name = form.getvalue('NAME', 'World')  # Default to 'World' if NAME is
not provided
# Output the HTML response
print(f"<html><body><h1>Hello, {name}!</h1></body></html>")

*For security reasons, always sanitize and validate input when working
with CGI scripts to avoid vulnerabilities like code injection.
====

This is a textbook example of XSS (Cross Site Scripting).

In 2023 Chatgpt suffered from the same testcase [1]

I have experience with AI and believe that one of the AI problems is
that it is trained on insecure data, first result on google returns
the insecure responses. GIGO == Garbage In Garbage Out.

This might be a joke:

Humans built a super AI and the first question was: "Is there god?".
The answer was: "Since now there is". (In Bulgarian: Хората направили
супер изкуствен интелект и първият въпрос бил: "Има ли бог".
Отговорът: "Вече има")

When the robots take over the real world, hacking the robots will be powerful :)

From [2]

The technological singularity—or simply the singularity—is a
hypothetical future point in time at which technological growth
becomes uncontrollable and irreversible, resulting in unforeseeable
consequences for human civilization.

[1]: https://www.linkedin.com/pulse/ai-chatgpt-writes-insecure-code-georgi-guninski
[2]: https://en.wikipedia.org/wiki/Technological_singularity
[3]: https://www.deepseek.com/
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

* **Deepseek writes textbook insecure code in 2025-01-28** *Georgi Guninski (Jan 29)*

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