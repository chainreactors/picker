---
title: Five Malicious Chrome Extensions Impersonate Workday and NetSuite to Hijack Accounts
url: https://thehackernews.com/2026/01/five-malicious-chrome-extensions.html
source: The Hacker News
date: 2026-01-16
fetch_date: 2026-01-17T03:28:20.216254
---

# Five Malicious Chrome Extensions Impersonate Workday and NetSuite to Hijack Accounts

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

# [Five Malicious Chrome Extensions Impersonate Workday and NetSuite to Hijack Accounts](https://thehackernews.com/2026/01/five-malicious-chrome-extensions.html)

**Jan 16, 2026**Ravie LakshmananBrowser Security / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7kvgFz8ELXceV5_LsBgcodkjSM6meRhVnuxiijpgc1_2XcMb9Gh660H5HEknLGskzkx9L81bbOM651BUVAzu2u6bf36gf5r2x3ndhltKVFZAforGzT-dQhny2-zEk3cih03DU1pfyRFiJLlNXuv_Ml-glQC1dGl95L1KpYHBXnMOfXZwfd4bWGaUH3uel/s790-rw-e365/chrome.jpg)

Cybersecurity researchers have discovered five new malicious Google Chrome web browser extensions that masquerade as human resources (HR) and enterprise resource planning (ERP) platforms like Workday, NetSuite, and SuccessFactors to take control of victim accounts.

"The extensions work in concert to steal authentication tokens, block incident response capabilities, and enable complete account takeover through session hijacking," Socket security researcher Kush Pandya [said](https://socket.dev/blog/5-malicious-chrome-extensions-enable-session-hijacking) in a Thursday report.

The names of the extensions are listed below -

* DataByCloud Access (ID: oldhjammhkghhahhhdcifmmlefibciph, Published by: databycloud1104) - 251 Installs
* Tool Access 11 (ID: ijapakghdgckgblfgjobhcfglebbkebf, Published by: databycloud1104) - 101 Installs
* DataByCloud 1 (ID: mbjjeombjeklkbndcjgmfcdhfbjngcam, Published by: databycloud1104) - 1,000 Installs
* DataByCloud 2 (ID: makdmacamkifdldldlelollkkjnoiedg, Published by: databycloud1104) - 1,000 Installs
* Software Access (ID: bmodapcihjhklpogdpblefpepjolaoij, Published by: Software Access) - 27 Installs

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

All of them, with the exception of Software Access, have been removed from the Chrome Web Store as of writing. That said, they are still available on third-party software download sites such as Softonic. The add-ons are advertised as productivity tools that offer access to premium tools for different platforms, including Workday, NetSuite, and other platforms.. Two of the extensions, DataByCloud 1 and DataByCloud 2, were first published on August 18, 2021.

The campaign, despite using two different publishers, is assessed to be a coordinated operation based on identical functionality and infrastructure patterns. It specifically involves exfiltrating cookies to a remote server under the attackers' control, manipulating the Document Object Model (DOM) tree to block security administration pages, and facilitating session hijacking via cookie injection.

Once installed, DataByCloud Access requests permissions for cookies, management, scripting, storage, and declarativeNetRequest across Workday, NetSuite, and SuccessFactors domains. It also collects authentication cookies for a specified domain and transmits them to the "api.databycloud[.]com" domain every 60 seconds.

"Tool Access 11 (v1.4) prevents access to 44 administrative pages within Workday by erasing page content and redirecting to malformed URLs," Pandya explained. "This extension blocks authentication management, security proxy configuration, IP range management, and session control interfaces."

This is achieved by DOM manipulation, with the extension maintaining a list of page titles that's constantly monitored. Data By Cloud 2 expands the blocking feature to 56 pages, adding crucial functions like password changes, account deactivation, 2FA device management, and security audit log access. It's designed to target both production environments and Workday's sandbox testing environment at "workdaysuv[.]com."

In contrast, Data By Cloud 1 replicates the cookie-stealing functionality from DataByCloud Access, while simultaneously incorporating features to prevent code inspection using web browser developer tools using the open-source [DisableDevtool library](https://github.com/theajack/disable-devtool). Both extensions encrypt their command-and-control (C2) traffic.

The most sophisticated extension of the lot is Software Access, which combines cookie theft with the ability to receive stolen cookies from "api.software-access[.]com" and inject them into the browser to facilitate direct session hijacking. Furthermore, it comes fitted with password input field protection to prevent users from inspecting credential inputs.

"The function parses cookies from the server payload, removes existing cookies for the target domain, then iterates through the provided cookie array and injects each one using chrome.cookies.set()," Socket said. "This installs the victim's authentication state directly into the threat actor's browser session."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

A notable aspect that ties together all five extensions is that they feature an identical list comprising 23 security-related Chrome extensions, such as EditThisCookie, Cookie-Editor, ModHeader, Redux DevTools, and SessionBox, that are designed to monitor and flag their presence to the threat actor.

This is likely an attempt to assess whether the web browser has any tool that can possibly interfere with their cookie harvesting objectives or reveal the extension's behavior, Socket said. What's more, the presence of a similar extension ID list across all five extensions raises two possibilities: either it's the work of the same threat actor who has published them under different publishers or a common toolkit.

Chrome users who have installed any of the aforementioned add-ons are advised to remove them from their browsers, perform password resets, and review for any signs of unauthorized access from unfamiliar IP addresses or devices.

"The combination of continuous credential theft, administrative interface blocking, and session hijacking creates a scenario where security teams can detect unauthorized access but cannot remediate through normal channels," Socket said.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_shar...