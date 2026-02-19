---
title: Critical Flaws Found in Four VS Code Extensions with Over 125 Million Installs
url: https://thehackernews.com/2026/02/critical-flaws-found-in-four-vs-code.html
source: The Hacker News
date: 2026-02-18
fetch_date: 2026-02-19T04:22:08.086869
---

# Critical Flaws Found in Four VS Code Extensions with Over 125 Million Installs

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Critical Flaws Found in Four VS Code Extensions with Over 125 Million Installs](https://thehackernews.com/2026/02/critical-flaws-found-in-four-vs-code.html)

**Ravie Lakshmanan**Feb 18, 2026Vulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWiS4R3zdQ6nAaXW6ITobd-w2duq9sy9VGi6Jn8fBYafy_ZIL0Yvr_vssObakMIWi_2m5RT-ZP6m_G5J6sS9ivV1fj6Qj98iDtdGtdUm2o-uh1sLAxOgQmVeFpBeqBxoohezNZwJFxnJRkO1aMB2H19iYLJQ9BtJFjLkC_JbIpOqfrEobgwBU-jJkFHNVI/s1700-e365/vscode-malware.jpg)

Cybersecurity researchers have disclosed multiple security vulnerabilities in four popular Microsoft Visual Studio Code (VS Code) extensions that, if successfully exploited, could allow threat actors to steal local files and execute code remotely.

The extensions, which have been collectively installed more than 125 million times, are Live Server, Code Runner, Markdown Preview Enhanced, and Microsoft Live Preview.

"Our research demonstrates that a hacker needs only one malicious extension, or a single vulnerability within one extension, to perform lateral movement and compromise entire organizations," OX Security researchers Moshe Siman Tov Bustan and Nir Zadok [said](https://www.ox.security/blog/four-vulnerabilities-expose-a-massive-security-blind-spot-in-ide-extensions/) in a report shared with The Hacker News.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

Details of the vulnerabilities are as follows -

* **[CVE-2025-65717](https://www.ox.security/blog/cve-2025-65717-live-server-vscode-vulnerability/)** (CVSS score: 9.1) - A vulnerability in Live Server that allows attackers to exfiltrate local files, tricking a developer into visiting a malicious website when the extension is running, causing JavaScript embedded in the page to crawl and extract files from the local development HTTP server that runs at localhost:5500, and transmit them to a domain under their control. (Remains unpatched)
* **[CVE-2025-65716](https://www.ox.security/blog/cve-2025-65716-markdown-preview-enhanced-vscode-vulnerability/)** (CVSS score: 8.8) - A vulnerability in Markdown Preview Enhanced that allows attackers to execute arbitrary JavaScript code by uploading a crafted markdown (.md) file, allowing local port enumeration and exfiltration to a domain under their control. (Remains unpatched)
* **[CVE-2025-65715](https://www.ox.security/blog/cve-2025-65715-code-runner-vscode-rce/)** (CVSS score: 7.8) - A vulnerability in Code Runner that allows attackers to execute arbitrary code by convincing a user to alter the "settings.json" file through phishing or social engineering. (Remains unpatched)
* A [vulnerability in Microsoft Live Preview](https://www.ox.security/blog/xssinlivepreview/) allows attackers to access sensitive files on a developer's machine by tricking a victim into visiting a malicious website when the extension is running, which then enables specially crafted JavaScript requests targeting the localhost to enumerate and exfiltrate sensitive files. (No CVE, Fixed silently by Microsoft in [version 0.4.16](https://github.com/microsoft/vscode-livepreview/blob/main/CHANGELOG.md) released in September 2025)

To secure the development environment, it's essential to avoid applying untrusted configurations, disable or uninstall non-essential extensions, harden the local network behind a firewall to restrict inbound and outbound connections, periodically update extensions, and turn off localhost-based services when not in use.

"Poorly written extensions, overly permissive extensions, or malicious ones can execute code, modify files, and allow attackers to take over a machine and exfiltrate information," OX Security said. "Keeping vulnerable extensions installed on a machine is an immediate threat to an organization's security posture: it may take only one click, or a downloaded repository, to compromise everything."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data security](https://thehackernews.com/search/label/data%20security), [Malware](https://thehackernews.com/search/label/Malware), [Microsoft](https://thehackernews.com/search/label/Microsoft), [software security](https://thehackernews.com/search/label/software%20security), [Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security), [Threat Research](https://thehackernews.com/search/label/Threat%20Research), [Visual Studio Code](https://thehackernews.com/search/label/Visual%20Studio%20Code), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond](data:image/svg+xml;base64... "OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond")

OT Security, In Practice: 4 Cross‑Industry Trends from Global Assessments and How CISOs Should Respond](https://thehackernews.com/expert-insights/2026/01/ot-security-in-practice-4-crossindustry.html)

[![Reynolds Ransomware Embeds BYOVD Driver ...