---
title: xpra server information disclosure
url: https://seclists.org/fulldisclosure/2025/Sep/68
source: Full Disclosure
date: 2025-09-26
fetch_date: 2025-10-02T20:45:21.634562
---

# xpra server information disclosure

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

[![Previous](/images/left-icon-16x16.png)](67)
[By Date](date.html#68)
[![Next](/images/right-icon-16x16.png)](69)

[![Previous](/images/left-icon-16x16.png)](67)
[By Thread](index.html#68)
[![Next](/images/right-icon-16x16.png)](69)

![](/shared/images/nst-icons.svg#search)

# xpra server information disclosure

---

*From*: Antoine Martin via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 24 Sep 2025 17:05:13 +0700

---

```
1) About Xpra
Xpra is known as "screen for X11".
https://xpra.org/
```

"Xpra forwards and synchronizes many extra desktop features, which
allows remote applications to integrate transparently into the client's
desktop environment: audio input and output, printers, clipboard, system
trays, notifications, webcams, etc."

```
2) Vulnerability
```

Using the server's "control" subsystem, a client can enable sensitive
debug logging, ie: "network", "crypto", "keyboard" or "auth" categories.

```
Newer versions even include a GUI for doing so more easily:
https://github.com/Xpra-org/xpra/issues/4666
```

Then using the "file-transfer" module, the server's log file can be
retrieved.
Alternatively, the "clipboard" subsystem could also be used to transfer
this log data to the client if it can somehow be copied to the clipboard
(ie using xclip).
Even the most basic window forwarding could be used to transfer the data
in pixel form, either eyeballing it or OCRing it on the client side.

```

```

Although the user would usually first need to authenticate to access the
session, there are many use-cases where the log data may still expose
sensitive information:

```
* system configuration, paths, etc
```

\* multi-client setups could leak other user's credentials, or record all
keyboard events (effectively a keylogger)
\* proxied sessions could leak the proxy server's connection details and
credentials

```
* server encryption keys
etc

3) Affected versions
All versions prior to 6.3.3 stable and 5.1.2 LTS.
EPEL, Fedora, Debian, Ubuntu are all shipping vulnerable versions.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](67)
[By Date](date.html#68)
[![Next](/images/right-icon-16x16.png)](69)

[![Previous](/images/left-icon-16x16.png)](67)
[By Thread](index.html#68)
[![Next](/images/right-icon-16x16.png)](69)

### Current thread:

* **xpra server information disclosure** *Antoine Martin via Fulldisclosure (Sep 25)*

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