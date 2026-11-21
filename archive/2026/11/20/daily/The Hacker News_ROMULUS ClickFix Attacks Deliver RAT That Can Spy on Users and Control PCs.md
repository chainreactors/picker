---
title: ROMULUS ClickFix Attacks Deliver RAT That Can Spy on Users and Control PCs
url: https://thehackernews.com/2026/11/romulus-clickfix-attacks-deliver-rat.html
source: The Hacker News
date: 2026-11-20
fetch_date: 2026-11-21T09:02:35.902507
---

# ROMULUS ClickFix Attacks Deliver RAT That Can Spy on Users and Control PCs

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [ROMULUS ClickFix Attacks Deliver RAT That Can Spy on Users and Control PCs](https://thehackernews.com/2026/11/romulus-clickfix-attacks-deliver-rat.html)

**Ravie Lakshmanan**Nov 20, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjugg63OPJwZuh94vDIg7MkA4YoeLKr5sjiqI6CEgjvDjUvJ-pBJOfUrUBxPUTbartqVwdldczbKSYo6lpkcVic1EDQYIDyWq12zMdMONjpDtK4NKCgkppAWvnOJpXe7prfmRG8WNpH0RrQ0bhX2nZKGpRy33y0OMZraBjEPoDorp9h3kNJSa-IQrJC7Nl5/s1700-nu-rw-lo-l85-e365/cf.jpg)

Threat actors have been observed using the **ROMULUS** ClickFix malware delivery platform to deliver a previously undocumented remote access trojan (RAT) that shares similarities with CNCMachineRMS.

"ROMULUS likely operates as a delivery service, distributing CNCMachineRMS and Legion Loader through separate chains while retaining ClickFix and signed binary sideloading techniques," Blackpoint Cyber researchers Sam Decker, Nevan Beal, and Andi Ursry [said](https://blackpointcyber.com/blog/romulus-cncmachinerms/) in a report.

ROMULUS was [first publicly documented](https://thehackernews.com/2026/10/romulus-clickfix-platform-tricks-users.html) by Forescout Research last month, describing it as a malware delivery service that employs ClickFix-style lures to distribute malware families like Legion Loader (aka Satacom downloader, CurlyGate, and RobotDropper).

Attacks involving ROMULUS have also leveraged [ChatGPT Custom GPTs](https://thehackernews.com/2026/09/attackers-abuse-chatgpt-custom-gpts-to.html) as a pathway to direct unsuspecting victims to malicious sites that employ ClickFix lures to deliver a RAT payload by means of DLL sideloading.

Interestingly, CNCMachineRMS has also been [delivered](https://thehackernews.com/2026/08/threatsday-296k-iot-botnet-100-water.html#clickfix-chain-drops-new-rat) via another malware loader called BabaDeda Loader through ClickFix attacks that employ DLL sideloading involving the legitimately signed IBM SPSS IDE executable.

The latest findings from Blackpoint Cyber indicate that ROMULUS is distributing CNCMachineRMS alongside LegionLoader through separate infection chains.

One of the payloads delivered through the ClickFix activity associated with ROMULUS is a malicious MSI installer ("IconEdit2Turb.msi") that's executed using "msiexec.exe" by means of a PowerShell command. The installer masquerades as Stardock Smart DeElevation Tool, while initiating a DLL sideloading chain to run a malicious DLL ("I++u.dll").

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

The DLL is designed to decode and run embedded shellcode responsible for launching CNCMachineRMS. It's worth noting that the RAT malware is the same final implant also distributed via the aforementioned ChatGPT Custom GPT lures.

The trojan enables remote desktop control, screen streaming, microphone and camera capture, file management, and system reconnaissance. It's also equipped to run additional payloads on demand. Communication with attacker-controlled infrastructure takes place through DNS over HTTPS (DoH).

"As attackers continue to change the applications and loaders used to distribute their payloads, the underlying malware architecture provides a more consistent way to identify related activity and understand the threats being delivered," Blackpoint Cyber said.

The findings coincide with the discovery of a number of ClickFix-style campaigns that -

* Combine ClickFix with EtherHiding on more than [70,000 compromised websites](https://www.stormshield.com/news/cti-payload-slaiclind-campaign/) to run JavaScript that interacts with a Polygon smart contract to fetch additional JavaScript that renders a fake Cloudflare CAPTCHA prompt and ultimately deliver malware ("slaiclind").
* Use [fake Zillow apartment-review pages](https://efficientip.com/blog/clickfix-netsupport-rat/) that serve a fake verification prompt to install NetSupport RAT on visitors' Windows computers.
* Employ a JavaScript-to-WordPress attack chain called [TRUST#GRAFT](https://www.securonix.com/blog/trust-graft-wordpress-admin-php-backdoor/) that employs an unknown initial access method to inject JavaScript into WordPress sites that serves a fake Cloudflare verification prompt and then fingerprints the visitor and checks if the request is from an already authenticated WordPress administrator browser before uploading a malicious PHP plugin named Web Media Optimizer that's capable of injecting remote JavaScript into public pages and copying itself into the "mu-plugins" plugins directory for persistence.
* Use a [sponsored Google search result](https://www.huntress.com/blog/amazon-clickfix-finger) for the keywords "amazon business" to a spoofed Amazon login page ("orders-amazon[.]com[.]advancedfences[.]com") with an embedded ClickFix command that uses the Window's built-in [finger](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/finger) utility to initiate a multi-stage attack chain that leads to the deployment of the NetSupport Client remote monitoring and management (RMM) tool and a version of Lumma Stealer.
* Abuse Google Ads to direct users to an [Anthropic Claude shared chat](https://thehackernews.com/2026/07/threatsday-ai-powered-hacking-370.html#fake-claude-guide-spreads-malware) that stages a [fake "Download Claude" page](https://www.gendigital.com/blog/insights/research/claude-content-sharing-malware) with ClickFix commands to trick Mac users into running a malicious command on their Terminal, resulting in the deployment of Atomic macOS Stealer (AMOS) stealer.
* Use a typosquatted domain that employs a ["House Wiring Scheme" theme](https://flare.io/learn/resources/blog/crocorat-clickfix-dns-payload-delivery) ("veriffication-redirect[.]com") to serve a fake Cloudflare verification prompt, which utilizes clipboard manipulation to trick users into running a malicious command on the Windows Run dialog, which then retrieves next-stage ...