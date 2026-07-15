---
title: LabubaRAT Masquerades as NVIDIA Software to Control Windows Hosts
url: https://thehackernews.com/2026/07/labubarat-masquerades-as-nvidia.html
source: The Hacker News
date: 2026-07-14
fetch_date: 2026-07-15T04:49:59.386902
---

# LabubaRAT Masquerades as NVIDIA Software to Control Windows Hosts

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [LabubaRAT Masquerades as NVIDIA Software to Control Windows Hosts](https://thehackernews.com/2026/07/labubarat-masquerades-as-nvidia.html)

**Ravie Lakshmanan**Jul 14, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpSmSwv3hz6LMJIQCrVej_pophE9XNTZyveEV1GctCyQMSNoac_Mx3CfmAHLgYkpDkymvscLLY71u2Kq-7z-7bDemSeKHryPVH3h7FNxw9e64D3jTeoLOzmWW305j1Rctz5kdiwFV29lFNqo33TUZMGWCaZqtyKNPYARGtrrhZ0Bsc4LMLXhnRgzKXjKYb/s1700-e365/NVIDIA-rat.jpg)

Cybersecurity researchers have flagged a previously undocumented Rust-based remote access trojan (RAT) codenamed **LabubaRAT** that masquerades as NVIDIA software to blend into target environments.

"LabubaRAT creates a reusable foothold for hands-on activity," Blackpoint Cyber researchers Sam Decker and Nevan Beal [said](https://blackpointcyber.com/blog/labubarat-a-rust-based-remote-access-tool-masquerading-as-nvidia-software/) in an analysis published today. "Once deployed, it can profile the host, identify security tools, receive operator commands, move files, capture screenshots, and proxy traffic through the affected system."

The implant also supports multiple communication methods, including HTTPS, WebView2, and DNS tunneling, allowing attackers to maintain access to compromised hosts even if one pathway is detected and closed off. There are some signs that LabubuRAT is being offered under a malware-as-a-service (MaaS) model.

The starting point of the attack chain is an executable named "nvidia-sysruntime.exe," which impersonates NVIDIA's container runtime toolkit. The sample, instead of hard-coding its command-and-control (C2) information, accepts a runtime configuration through command-line arguments.

This allows the campaign operator to define various parameters that are key to establishing communication with the remote server, including the server details ("pipicka[.]xyz") and the polling interval used by the implant. Alternatively, the attacker can also supply these individual values in the form of one single Base64-encoded argument.

"Because those values were provided at launch, the same compiled binary could be reused with different infrastructure, organizations, or campaign groupings instead of relying on a hard-coded server," the researchers noted.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The configuration is then stored in a local SQLite database, following which it undertakes discovery operations to inventory the list of web browsers and security products installed on the host, specifically checking for the presence of Google Chrome, Mozilla Firefox, Microsoft Edge, Brave, Microsoft Defender, CrowdStrike, SentinelOne, Carbon Black, Sophos, Malwarebytes, Bitdefender, ESET, Kaspersky, McAfee, Symantec, and Trend Micro.

In addition, it gathers the hostname, RAM size, CPU model, and the Windows User Account Control (UAC) state as a way to prepare the environment for the next stage, as some RAT functionality may be dictated by the security tools present on the system.

Once launched, LabubaRAT supports a wide range of functions, such as command execution, PowerShell execution, JavaScript execution, screenshot capture, file upload and download, archive handling, and SOCKS5 proxy support.

"Those capabilities gave the operator enough control to interact with the host, move files in and out of the environment, route traffic through the system, and maintain access without relying on a separate loader or narrowly scoped follow-on tool," Blackpoint Cyber said.

The malware is a reference to the "LabubaPanel" title associated with its C2 infrastructure and a Labubu-themed favicon.

"The sample combined runtime configuration, local state, host profiling, multiple communication paths, and operator tasking into a complete remote access tool," Blackpoint Cyber said. "The malware gave an operator a practical way to enroll hosts, understand the environment around each agent, execute commands, move files, capture screenshots, proxy traffic, and maintain user level autostart."

"The LabubaPanel branding provided the clearest external naming clue, but the more important finding is the framework-like structure behind it: a Rust based RAT built to be configured, enrolled, and operated across multiple deployments."

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

[Command and Control](https://thehackernews.com/search/label/Command%20and%20Control), [Cybercrime](https://thehackernews.com/search/label/Cybercrime), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [Malware](https://thehackernews.com/search/label/Malware), [Malware-as-a-Service](https://thehackernews.com/search/label/Malware-as-a-Service), [network security](https://thehackernews.com/search/label/network%20security), [Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence), [Windows Security](https://thehackernews.com/search/label/Windows%20Security)

⚡ Top Stories This Week

[![16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on...