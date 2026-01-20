---
title: CrashFix Chrome Extension Delivers ModeloRAT Using ClickFix-Style Browser Crash Lures
url: https://thehackernews.com/2026/01/crashfix-chrome-extension-delivers.html
source: The Hacker News
date: 2026-01-19
fetch_date: 2026-01-20T03:35:29.365477
---

# CrashFix Chrome Extension Delivers ModeloRAT Using ClickFix-Style Browser Crash Lures

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

# [CrashFix Chrome Extension Delivers ModeloRAT Using ClickFix-Style Browser Crash Lures](https://thehackernews.com/2026/01/crashfix-chrome-extension-delivers.html)

**Ravie Lakshmanan**Jan 19, 2026Malware / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHk6v6YRLFG3a9vVJQ5OLdPuN9cBdDklQzJHf91XqJUjDiKB8IT7VEmxB7VyKcSXbahTKXr-seTEvP3hdRWT2ws4xUteRY4tfouGxjDrH22aIxauonv9sb7Gw6TgCRh4GfoMCZLnp6gL79_feODNKp7LHF8nkte3e6mvt4d3UERPwMxUvHgnF1e6uB2BSf/s900-e365/edges.jpg)

Cybersecurity researchers have disclosed details of an ongoing campaign dubbed KongTuke that used a malicious Google Chrome extension masquerading as an ad blocker to deliberately crash the web browser and trick victims into running arbitrary commands using [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)-like lures to deliver a previously undocumented remote access trojan (RAT) dubbed ModeloRAT.

This new escalation of ClickFix has been codenamed [CrashFix](https://www.huntress.com/blog/malicious-browser-extention-crashfix-kongtuke) by Huntress.

[KongTuke](https://thehackernews.com/2025/10/hackers-exploit-wordpress-themes-to.html), also tracked as 404 TDS, Chaya\_002, LandUpdate808, and TAG-124, is the name given to a traffic distribution system (TDS) known for profiling victim hosts before redirecting them to a payload delivery site that infects their systems. Access to these compromised hosts is then handed off to other threat actors, including ransomware groups, for follow-on malware delivery.

Some of the cybercriminal groups that have leveraged TAG-124 infrastructure include [Rhysida ransomware](https://thehackernews.com/2025/10/microsoft-revokes-200-fraudulent.html), [Interlock ransomware](https://thehackernews.com/2025/04/ransomhub-went-dark-april-1-affiliates.html), and [TA866](https://thehackernews.com/2025/08/new-ps1bot-malware-campaign-uses.html) (aka Asylum Ambuscade), with the threat actor also associated with [SocGholish](https://thehackernews.com/2025/08/socgholish-malware-spread-via-ad-tools.html) and [D3F@ck Loader](https://thehackernews.com/2025/07/credential-theft-and-remote-access.html), according to a Recorded Future report from April 2025.

In the attack chain documented by the cybersecurity company, the victim is said to have searched for an ad blocker when they were served a malicious advertisement that redirected them to an extension hosted on the Official Chrome Web Store.

The browser extension in question, "NexShield – Advanced Web Guardian" (ID: cpcdkmjddocikjdkbbeiaafnpdbdafmi), masquerades as the "ultimate privacy shield" and claims to protect users against ads, trackers, malware, and intrusive content on web pages. It was downloaded at least 5,000 times. It's currently no longer available for download.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The extension, per Huntress, is a near-identical clone of uBlock Origin Lite version 2025.1116.1841, a legitimate ad blocker add-on available for all major web browsers. It's engineered to display a fake security warning, claiming the browser had "stopped abnormally" and prompting users to run a "scan" to remediate a potential security threat detected by Microsoft Edge.

Should the user opt to run the scan, the victim is presented with a bogus security alert that instructs them to open the Windows Run dialog and paste the displayed command already copied to the clipboard, and execute it. This, in turn, causes the browser to completely freeze, crashing it by launching a denial-of-service (DoS) attack that creates new [runtime port connections](https://developer.chrome.com/docs/extensions/reference/api/runtime) through an infinite loop that triggers one billion iterations of the same step repeatedly.

This resource exhaustion technique results in excessive memory consumption, causing the web browser to become slow, unresponsive, and eventually crash.

Once installed, the extension is also designed to transmit a unique ID to an attacker-controlled server ("[nexsnield[.]com](https://www.virustotal.com/gui/domain/nexsnield.com/detection)"), giving the operators the ability to track victims. In addition, it adopts a delayed execution mechanism that ensures the malicious behavior is only triggered 60 minutes after it's installed. After that, the payload is executed every 10 minutes.

"The pop-up only appears on browser startup after the browser becomes unresponsive," researchers Anna Pham, Tanner Filip, and Dani Lopez said. "Before the DoS executes, a timestamp is stored in local storage. When the user force-quits and restarts their browser, the startup handler checks for this timestamp, and if it exists, the CrashFix popup appears, and the timestamp is removed."

"The DoS only executes if the UUID exists (meaning the user is being tracked), the C2 server responds successfully to a fetch request, and the pop-up window has been opened at least once and subsequently closed. This last condition may be intentional to ensure user interaction with the extension before triggering the payload."

The end result is that it creates a loop of its own, activating the fake warning every time the victim force-quits and restarts the browser after it becomes unresponsive due to the DoS attack. In the event the extension is not removed, the attack is triggered again after 10 minutes.

The pop-up also incorporates various anti-analysis techniques that disable right-click context menus and prevent attempts to use keyboard shortcuts to launch developer tools. The CrashFix command employs the legitimate Windows utility, [finger.exe](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/finger), to retrieve and execute the next-stage payload from the attacker's server ("199.217.98[.]108"). KongTuke's use of the Finger command was [documented](https://thehackernews.com/2025/12/threatsday-bulletin-whatsapp-hijacks.html#fake-captcha-delivers-malware) by security researcher Brad Duncan in December 2025.

The payload received from the server is a PowerShell command that's configured to retrieve a secondary PowerShell script, which, in turn, takes a page out of SocGholish's playbook, using multiple layers of Base64 encoding and XOR operations to conceal the next-stage malware.

The decrypted blob scans running proce...