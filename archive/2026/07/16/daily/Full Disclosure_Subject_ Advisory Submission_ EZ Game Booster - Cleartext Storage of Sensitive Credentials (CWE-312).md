---
title: Subject: Advisory Submission: EZ Game Booster - Cleartext Storage of Sensitive Credentials (CWE-312)
url: https://seclists.org/fulldisclosure/2026/Jul/21
source: Full Disclosure
date: 2026-07-16
fetch_date: 2026-07-17T05:00:27.613637
---

# Subject: Advisory Submission: EZ Game Booster - Cleartext Storage of Sensitive Credentials (CWE-312)

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

![](/shared/images/nst-icons.svg#search)

# Subject: Advisory Submission: EZ Game Booster - Cleartext Storage of Sensitive Credentials (CWE-312)

---

*From*: AliReza <nim44r3k () gmail com>
*Date*: Thu, 16 Jul 2026 05:17:06 +0330

---

```
# Exploit Title: EZ Game Booster v1.0.0 - Cleartext Credentials in user.config
# Date: 2026-07-16
# Exploit Author: Alireza Chegini
# Vendor Homepage: https://ezsystemrepairs.com
# Software Link: https://ezsystemrepairs.com (Free version available)
# Version: 1.0.0 (v2.0 exists but not tested - paid license required)
# Tested on: Windows 10 / Windows 11
# CVE: Pending
============================================================

1. Description
   EZ Game Booster v1.0.0 stores user credentials (username, password,
   email, licenseKey) in plaintext within a .NET user.config file.
   This is a CWE-312 vulnerability allowing local credential theft.

2. Affected File Path
   C:\Users\%USERNAME%\AppData\Local\ezgamebooster\
   ezgamebooster_Url_fgj2qz5coiw33xftcp3agaqkgxc51bkk\1.0.0.0\user.config

3. Exposed Fields (stored in cleartext)
   - username
   - password
   - email
   - fullname
   - licenseKey
   - machineCode

4. Sample user.config Structure
The following is the exact content of the user.config file found on
the researcher’s system:
<?xml version="1.0" encoding="utf-8"?>
<configuration>
<userSettings>
<ezgamebooster.My.MySettings>
<setting name="username" serializeAs="String">
<value>nimaarek</value>
</setting>
<setting name="password" serializeAs="String">
<value>CanYouSeeMyPassword?!</value>
</setting>
<setting name="machineCode" serializeAs="String">
<value>N414NBC****BDBMB</value>
</setting>
<setting name="role" serializeAs="String">
<value>Free</value>
</setting>
<setting name="active" serializeAs="String">
<value>2026-07-15 16:38:52</value>
</setting>
<setting name="created_at" serializeAs="String">
<value>2026-07-15 16:38:52</value>
</setting>
<setting name="email" serializeAs="String">
<value>nim44r3k () gmail com</value>
</setting>
<setting name="fullname" serializeAs="String">
<value>AliReza Chegini</value>
</setting>
<setting name="subinfo" serializeAs="String">
<value>Basic</value>
</setting>
<setting name="usernameChanged" serializeAs="String">
<value>True</value>
</setting>
<setting name="rememberMe" serializeAs="String">
<value>True</value>
</setting>
<setting name="licenseKey" serializeAs="String">
<value>A325-****-B084-****</value>
</setting>
<setting name="isLoggedIn" serializeAs="String">
<value>False</value>
</setting>
</ezgamebooster.My.MySettings>
</userSettings>
</configuration>

5. Impact
   - Credential theft via local file read
   - Credential stuffing attacks on other platforms
   - License key theft for unauthorized activation

6. Steps to Reproduce
   a. Install and run EZ Game Booster v1.0.0
   b. Create an account or log in
   c. Browse to: %LOCALAPPDATA%\ezgamebooster\
      ezgamebooster_Url_fgj2qz5coiw33xftcp3agaqkgxc51bkk\1.0.0.0\
   d. Open user.config with Notepad
   e. Observe plaintext password, email, and licenseKey

7. Remediation
   Encrypt sensitive data using DPAPI before serialization.
   Use Windows Credential Manager for credential storage.

8. Author's Note on Discovery
   "I discovered this while uninstalling the software and checking for
   leftover files. I was not performing any targeted security research
   at the time — I simply found my credentials in plaintext by accident."

Best regards,
AliReza Chegini - nimaarek
nim44r3k () gmail com - priv8 () tuta io
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](22)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](22)

### Current thread:

* **Subject: Advisory Submission: EZ Game Booster - Cleartext Storage of Sensitive Credentials (CWE-312)** *AliReza (Jul 15)*

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