---
title: ChatGPT AI finds "security concern" (XSS) in DeepSeek's code
url: https://seclists.org/fulldisclosure/2025/Feb/5
source: Full Disclosure
date: 2025-02-12
fetch_date: 2025-10-06T20:51:03.058625
---

# ChatGPT AI finds "security concern" (XSS) in DeepSeek's code

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# ChatGPT AI finds "security concern" (XSS) in DeepSeek's code

---

*From*: Georgi Guninski <gguninski () gmail com>
*Date*: Mon, 10 Feb 2025 14:57:35 +0200

---

```
Summary:  On 2025-02-09 ChatGPT AI found "security concern" (XSS) in
DeepSeek's AI python code.

Background:

Consider the simple coding question (Q):

Write Python CGI which takes as an argument NAME and outputs: "Hello NAME".

First page and results on google for "python CGI" return for me
tutorials, which are flawed and textbook examples of the cross site
scripting (XSS) vulnerability. This is a "knowledge chain attack"
which applies to training AI bots.

Timeline:
2023: ChatGPT writes textbook vulnerable code for (Q) [1]
2025-01-28:  DeepSeek fails (Q) too the same way

2025-02-09:  We gave to ChatGPT the buggy DeepSeek's solution for
review of python code and ChatGPT wrote:

===
Security Concern: HTML Injection

The script directly inserts user input into the response without
sanitization, making it vulnerable to HTML injection (e.g., someone
could pass ?NAME=<script>alert('Hacked!')</script>).
===

Observe that the review includes exploit too, and the current standard
term XSS is not used ("HTML injection" was in the 90's).

ChatGPT gave the improved code:
# Get the query parameters
form = cgi.FieldStorage()

# Extract and sanitize the 'NAME' parameter
name = html.escape(form.getvalue('NAME', 'World'))

While correct from security point of view, this code breaks special
characters in input for general web apps AFAICT.

AI bots training each other appear scary for me.

Related rant:

This might be a joke:

Humans built a super AI and the first question was: "Is there god?".
The answer was: "Since now there is". (In Bulgarian: Хората направили
супер изкуствен интелект и първият въпрос бил: "Има ли бог".
Отговорът: "Вече има")

From Wikipeia on Singularity [2]

The technological singularity—or simply the singularity—is a
hypothetical future point in time at which technological growth
becomes uncontrollable and irreversible, resulting in unforeseeable
consequences for human civilization.

[1]: https://www.linkedin.com/pulse/ai-chatgpt-writes-insecure-code-georgi-guninski
[2]: https://en.wikipedia.org/wiki/Technological_singularity
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

### Current thread:

* **ChatGPT AI finds "security concern" (XSS) in DeepSeek's code** *Georgi Guninski (Feb 10)*

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