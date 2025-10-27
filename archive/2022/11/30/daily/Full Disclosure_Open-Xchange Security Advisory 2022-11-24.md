---
title: Open-Xchange Security Advisory 2022-11-24
url: https://seclists.org/fulldisclosure/2022/Nov/18
source: Full Disclosure
date: 2022-11-30
fetch_date: 2025-10-04T00:08:18.275903
---

# Open-Xchange Security Advisory 2022-11-24

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](20)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](20)

![](/shared/images/nst-icons.svg#search)

# Open-Xchange Security Advisory 2022-11-24

---

*From*: Martin Heiland via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 24 Nov 2022 11:31:13 +0100 (CET)

---

```
Dear subscribers,

we're sharing our latest advisory with you and like to thank everyone who contributed in finding and solving those
vulnerabilities. Feel free to join our bug bounty programs for OX AppSuite, Dovecot and PowerDNS at HackerOne and soon
at YesWeHack.

Yours sincerely,
  Martin Heiland, Open-Xchange GmbH

Product: OX App Suite
Vendor: OX Software GmbH

Internal reference: OXUIB-1654
Vulnerability type: Cross-Site Scripting (CWE-80)
Vulnerable version: 7.10.6 and earlier
Vulnerable component: frontend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Fixed version: 7.10.5-rev37, 7.10.6-rev16
Vendor notification: 2022-05-23
Solution date: 2022-08-10
Public disclosure: 2022-11-24
CVE reference: CVE-2022-31469
CVSS: 4.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N)

Vulnerability Details:
The detection mechanism for "deep links" in E-Mail (e.g. pointing to OX Drive) allows to inject references to arbitrary
fake applications. This can be used to request unexpected content, potentially including script code, when those links
are used.

Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering
unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would
require the victim to follow a hyperlink.

PoC:
<a class="deep-link-app"
href="https://test/#!!&app=%2e./%2e./%2e./%2e./%2e./%2e./appsuite/apps/themes/default/logo.png?cut=&id=123";>

Solution:
We improved deep-link validation to avoid malicious use.

---

Internal reference: OXUIB-1678
Vulnerability type: Cross-Site Scripting (CWE-80)
Vulnerable version: 7.10.6 and earlier
Vulnerable component: frontend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Fixed version: 7.10.5-rev37, 7.10.6-rev16, 8.3
Vendor notification: 2022-05-30
Solution date: 2022-08-10
Public disclosure: 2022-11-24
CVE reference: CVE-2022-37307
CVSS: 5.4 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N)

Vulnerability Details:
Certain content like E-Mail signatures are stored using the "snippets" mechanism. This mechanism contains a weakness
that allows to inject seemingly benign HTML content, like XHTML CDATA constructs, that will be sanitized to malicious
code. Once such code is in place it can be used for persistent access to the users account.

Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering
unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would
require access to the same OX App Suite instance or temporary access to the users account.

PoC:
<![CDATA[
<bo<script></script>dy>AA<img src onerror="alert('XSS')">BB</body>
]]>

Solution:
We improved the sanitizing algorithm to deal with disguised code.

---

Internal reference: OXUIB-1731
Vulnerability type: Cross-Site Scripting (CWE-80)
Vulnerable version: 7.10.6 and earlier
Vulnerable component: frontend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Fixed version: 7.10.5-rev37, 7.10.6-rev16, 8.3
Vendor notification: 2022-06-22
Solution date: 2022-08-10
Public disclosure: 2022-11-24
CVE reference: CVE-2022-37308
CVSS: 5.4 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N)

Vulnerability Details:
Plain-text mail that contains HTML code can be used to inject script code when printing E-Mail.

Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering
unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would need
to make the victim print a malicious E-Mail.

PoC:
...
Content-Type: text/plain
<img src onerror="alert('XSS')">

Solution:
We removed plain-text specific code and use existing sanitization mechanisms for HTML content.

---

Internal reference: OXUIB-1732
Vulnerability type: Cross-Site Scripting (CWE-80)
Vulnerable version: 7.10.6 and earlier
Vulnerable component: frontend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Fixed version: 7.10.5-rev37, 7.10.6-rev16, 8.4
Vendor notification: 2022-06-22
Solution date: 2022-08-10
Public disclosure: 2022-11-24
CVE reference: CVE-2022-37309
CVSS: 5.4 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N)

Vulnerability Details:
Contacts that do not contain a name but only a e-mail address can be used to inject script code to the "contact picker"
component, commonly used to select contacts as recipients or participants.

Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering
unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would
require access to the same OX App Suite instance or make the victim import malicious contact data.

Solution:
We now apply proper HTML escaping to all relevant data sets.

---

Affected product: OX App Suite
Internal reference: OXUIB-1785
Vulnerability type: Cross-Site Scripting (CWE-80)
Vulnerable version: 7.10.6 and earlier
Vulnerable component: frontend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Fixed version: 7.10.5-rev37, 7.10.6-rev16, 8.4
Vendor notification: 2022-07-20
Solution date: 2022-08-10
Public disclosure: 2022-11-24
CVE reference: CVE-2022-37310
CVSS: 4.3 (CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N)

Vulnerability Details:
The metrics and help modules use parts of the URL to determine capabilities. This mechanism suffers from a weakness
that allows attackers to use special characters that register malicious capabilities, which will be executed as script
code after login.

Risk:
Malicious script code can be executed within the victims context. This can lead to session hijacking or triggering
unwanted actions via the web interface (e.g. redirecting to a third-party site). To exploit this an attacker would
require the victim to follow a hyperlink to its App Suite instance and login. While the "metrics" module is optional,
the "help" module is available on all instances.

PoC:
https://appsuite.example.com/appsuite/#!!&app=io.ox/files&cap=t,(()%3d>{$$%3d%2bf;$f%3d%2b!f;$t%3d$f%2b!f;f$%3d$t|!f;t$%3df$%2b!f;$$f%3dt$|!f;$$t%3d$$f%2b!f;$f$%3d$$t|!f;$t$%3d(""%2b{})[$$f]%2b(""%2b{})[$f]%2b(""%2b[][f])[$f]%2b"f"[f$]%2b"t"[$$]%2b"t"[$f]%2b"t"[$t]%2b(""%2b{})[$$f]%2b"t"[$$]%2b(""%2b{})[$f]%2b"t"[$f];$$$%3d[][$t$][$t$];$$$("$$$('"%2b'\\'%2b$f%2bt$%2b$f%2b'\\'%2b$f%2b$$f%2bt$%2b'\\'%2b$f%2bt$%2b$$f%2b'\\'%2b$f%2b$$t%2b$t%2b'\\'%2b$f%2b$$t%2bt$%2b'('%2b'"'%2b'\\'%2b$f%2bf$%2b$$%2b'\\'%2b$f%2b$t%2bf$%2b'\\'%2b$f%2b$t%2bf$%2b'"'%2b')'%2b"')();")()})()

Solution:
We sanitized any non-parsable characters from the capabilities input.

---

Internal reference: MWB-1712
Vulnerability type: Server-Side Request Forgery (CWE-918)
Vulnerable version: 7.10.6 and earlier
Vulnerable component: backend
Report confidence: Confirmed
Solution status: Fixed by Vendor
Fixed version: 7.10.5-rev47, 7.10.6-rev22, 8.4
Vendor notification: 2022-07-14
So...