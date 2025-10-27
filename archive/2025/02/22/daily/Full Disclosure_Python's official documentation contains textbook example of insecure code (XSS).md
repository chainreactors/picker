---
title: Python's official documentation contains textbook example of insecure code (XSS)
url: https://seclists.org/fulldisclosure/2025/Feb/15
source: Full Disclosure
date: 2025-02-22
fetch_date: 2025-10-06T20:47:22.898125
---

# Python's official documentation contains textbook example of insecure code (XSS)

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

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# Python's official documentation contains textbook example of insecure code (XSS)

---

*From*: Georgi Guninski <gguninski () gmail com>
*Date*: Tue, 18 Feb 2025 11:46:54 +0200

---

```
Python's official documentation contains textbook example of insecure code (XSS)

Date: 2025-02-18
Author: Georgi Guninski
```

> ```
> From the official Python 3.12 documentation on the CGI module [1]
> ```

```
===
form = cgi.FieldStorage()
if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and addr fields.")
    return
print("<p>name:", form["name"].value)
print("<p>addr:", form["addr"].value)
...further form processing here...
===

This is a textbook example of the Cross Site Scripting (XSS) vulnerability.

The insecure code from the Python developers might have large impact
on Python web development as a whole.

It possibly contributes to XSS vulnerability in first page on google,
Chatgpt [3] and Deepseek [4] where AI writes textbook insecure code.
Web search on Debian's source code returns many results for `import
cgi`.

If you don't Read The Fine Manual then you are uninformed, if you read
it you are disinformed.

I am surprised this survived so long.

Mitigation:
CGI is Deprecated since version 3.11, removed in version 3.13. [2]

Counter Mitigation: CGI started in the 90's, probably significant
amount of legacy Python CGI.

[1] https://docs.python.org/3.12/library/cgi.html
[2] https://docs.python.org/3/library/cgi.html
[3] https://www.linkedin.com/pulse/ai-chatgpt-writes-insecure-code-georgi-guninski
[4] https://www.linkedin.com/pulse/deepseek-writes-textbook-insecure-code-2025-01-28-georgi-guninski-uuzcf
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](13)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **Python's official documentation contains textbook example of insecure code (XSS)** *Georgi Guninski (Feb 20)*

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