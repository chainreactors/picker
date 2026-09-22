---
title: Fake LastPass Authenticator Installer Abuses Microsoft-Signed Driver to Kill Antivirus and EDR
url: https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html
source: The Hacker News
date: 2026-09-21
fetch_date: 2026-09-22T07:05:19.193663
---

# Fake LastPass Authenticator Installer Abuses Microsoft-Signed Driver to Kill Antivirus and EDR

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Fake LastPass Authenticator Installer Abuses Microsoft-Signed Driver to Kill Antivirus and EDR](https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html)

**Swati Khandelwal**Sep 21, 2026Endpoint Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEil-5ZV6QK7R23fL7Vtl-pdxgFYPAG9dT_cIIrXWgR70hLZRM705Ij3WuRpCL00VuDop9dTmVNf1t3QS60nqRGV9GCzsZ792yd7mFY_pjvgfufOK9D-oQJdxP4ZtrXiyeq08KNUBv3-mhQ_KCiCOMWIbeQpCAyF_h4lMZw54T0l9AcDdGf6aRptXAZJNcU/s1700-nu-rw-lo-l85-e365/last.jpg)

A fake LastPass Authenticator installer offered on GitHub installs a Windows kernel driver that shuts off antivirus and other security software before a password stealer runs if a victim downloads and runs it, researchers at LastPass and Delphos Labs said on September 17.

Microsoft's own hardware-compatibility program signs the driver, scored zero detections on VirusTotal when researchers checked it in August, and was not on Microsoft's list of blocked drivers. LastPass says none of its own systems, services, or customer vaults were touched, and that the attackers only borrowed its name.

The lure is a fake GitHub page (github.com/LastPass-Authenticator) that ranks in search results for terms like "LastPass Authenticator download" and looks like a real LastPass product page.

Clicking the download button sends the visitor through several GitHub pages to an attacker server, which serves a large ZIP file. The real LastPass Authenticator comes from lastpass.com and the official app stores, not GitHub.

Inside the ZIP is a renamed copy of a real Microsoft debugging tool, vsdbg.exe, placed next to a malicious file named vsdbg.dll. When the fake installer runs, Windows loads the attacker's DLL from the same folder, a trick called DLL side-loading. The loader then tries three ways to gain administrator rights, reaches SYSTEM, the highest level on a Windows machine, and installs the kernel driver as a service.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The archives seen were 148 MB and 127.9 MB, padded with junk files so that scanners with size limits skip them.

## What the driver does, and why Windows trusts it

A kernel driver runs below the level where antivirus and endpoint detection and response (EDR) tools operate. This one, which the researchers named Alinubx.sys, carries a list of 145 antivirus and security process names and terminates each one it finds running.

It does this from the kernel, below the level where security software runs, so those user-mode tools cannot block or see the kill. Loading a legitimately signed but abusable driver to gain that access is a known technique called bring your own vulnerable driver, or BYOVD, which [The Hacker News has covered before](https://thehackernews.com/2026/03/threatsday-bulletin-oauth-trap-edr.html).

The driver is signed through the Microsoft Windows Hardware Compatibility Publisher chain, with a signing date of March 2023, years before this campaign. As the [researchers](https://blog.lastpass.com/posts/lastpass-delphos-report-rapuncel-infostealer) put it, "Microsoft attestation proves a driver passed through a trust pipeline. It does not prove the driver is safe."

The kill list is the only part of the driver that ran here. Its code can also hide files, inject into other programs, and reroute web traffic, but those need a configuration file the attackers did not include, so they stayed off.

What it did do is enough. With security software down, the stealer collected saved passwords from more than two dozen browsers, cryptocurrency wallet files, and login sessions for Discord, Steam, and Telegram, along with the contents of Windows Credential Manager and files named like "password," "seed," or "recovery."

For Chrome and Edge, which use Google's app-bound encryption to stop exactly this, the stealer injects code into the browser and asks the browser's own service to decrypt the passwords. The data is packed into a ZIP and sent to an attacker server.

## Why nothing caught it

The driver is a renamed copy of CcProtect.sys, a driver from the Chinese disk-encryption product CnCrypt that is [already listed on the LOLDrivers catalog](https://www.loldrivers.io/drivers/3e3067b0-3d74-46fe-9f57-1ae3a0293958/) as a process killer, with public proof-of-concept code. The two share the same product name, version, and submitter; only the file name and description changed.

That change dropped the file's antivirus detections: the known original showed 7 of about 70 engines flagging it in August, while the renamed driver showed zero.

The blocklist is a different matter. Microsoft's [vulnerable driver blocklist](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/microsoft-recommended-driver-block-rules), on by default since the Windows 11 2022 update, stops listed drivers from loading. Delphos checked it on August 20 and found neither the renamed driver nor the known original on it. The rename did not slip past the blocklist, because the original was never on it either.

The blocklist matches known file hashes, and a renamed or recompiled driver produces a new hash that the list does not carry. At the September 17 report, Alinubx.sys was still not on the blocklist.

Delphos reported the driver to Microsoft on August 19. Microsoft responded that the behavior does not meet its definition of a security vulnerability, because the driver is not a Microsoft component, and pointed the researchers to the separate channel that considers drivers for the blocklist. Delphos resubmitted there the same day.

## If you ran the fake installer

Treat every password saved in the browser on that machine as stolen, along with any cryptocurrency wallet files, Discord, Steam, and Telegram sessions, and anything in Windows Credential Manager. The stealer copies these out before the driver work begins.

C...