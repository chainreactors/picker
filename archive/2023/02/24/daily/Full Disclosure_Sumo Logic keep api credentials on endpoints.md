---
title: Sumo Logic keep api credentials on endpoints
url: https://seclists.org/fulldisclosure/2023/Feb/11
source: Full Disclosure
date: 2023-02-24
fetch_date: 2025-10-04T07:59:48.598645
---

# Sumo Logic keep api credentials on endpoints

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

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

![](/shared/images/nst-icons.svg#search)

# Sumo Logic keep api credentials on endpoints

---

*From*: dammitjosie--- via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sat, 18 Feb 2023 02:42:46 +0100 (CET)

---

```
security bug:

go sumologic.com (big company, many customer)

make free account

log in account, make access key - help.sumologic.com/docs/manage/security/access-keys/
<http://help.sumologic.com/docs/manage/security/access-keys/>

download collector for windows -
help.sumologic.com/docs/send-data/installed-collectors/collector-installation-reference/download-collector-from-static-url/

<http://help.sumologic.com/docs/send-data/installed-collectors/collector-installation-reference/download-collector-from-static-url/>

install collector by `cmd` using access key - help.sumologic.com/docs/send-data/installed-collectors/windows/
<http://help.sumologic.com/docs/send-data/installed-collectors/windows/>
ex: SumoCollector.exe -console -q "-Vsumo.accessid=<accessId>" "-Vsumo.accesskey=<accessKey>"

look c:\users\(you)\appdata\local\temp\i4j_nlog_1.log

accessid and accesskey in log file !! give access to whole api !!:
help.sumologic.com/docs/api/ <http://help.sumologic.com/docs/api/>
api.sumologic.com/docs/ <http://api.sumologic.com/docs/>

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

### Current thread:

* **Sumo Logic keep api credentials on endpoints** *dammitjosie--- via Fulldisclosure (Feb 22)*

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