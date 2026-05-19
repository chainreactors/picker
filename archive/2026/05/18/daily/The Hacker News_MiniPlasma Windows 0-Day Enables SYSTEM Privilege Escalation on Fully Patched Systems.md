---
title: MiniPlasma Windows 0-Day Enables SYSTEM Privilege Escalation on Fully Patched Systems
url: https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html
source: The Hacker News
date: 2026-05-18
fetch_date: 2026-05-19T06:05:21.488728
---

# MiniPlasma Windows 0-Day Enables SYSTEM Privilege Escalation on Fully Patched Systems

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [MiniPlasma Windows 0-Day Enables SYSTEM Privilege Escalation on Fully Patched Systems](https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html)

**Ravie Lakshmanan**May 18, 2026Zero Day / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvmx8dRRiQKx4cT0aT1-zTuzdjfThwxmlbzb2ikeeqIXUXGdcJhRrq4BykcdBB572URpoAHQhSTSyahR3M7TyvOsLSCekQGCUFM8sTcdsxkrpRFrT41wF8EqKA5LjzYHpzUtro2136Iy55cKQ_wixFUSsFDnilkUNCvrDvJbHBKK3k_IelHt9lOmbW01_u/s1700-e365/windows-exploits.jpg)

Chaotic Eclipse, the security researcher behind the recently disclosed Windows flaws, [YellowKey and GreenPlasma](https://thehackernews.com/2026/05/windows-zero-days-expose-bitlocker.html), has released a proof-of-concept (PoC) for a Windows privilege escalation zero-day flaw that grants attackers SYSTEM privileges on fully patched Windows systems.

Codenamed **[MiniPlasma](https://github.com/Nightmare-Eclipse/MiniPlasma)**, the vulnerability impacts "cldflt.sys," which refers to the Windows Cloud Files Mini Filter Driver, and resides in a routine named "HsmOsBlockPlaceholderAccess." It was [originally reported](https://project-zero.issues.chromium.org/issues/42451192) to Microsoft by Google Project Zero researcher James Forshaw in September 2020.

Although it was assumed that the shortcoming was fixed by Microsoft in December 2020 as part of [CVE-2020-17103](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103), Chaotic Eclipse said further investigation has uncovered that the "exact same issue [...] is actually still present, unpatched."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

"I'm unsure if Microsoft just never patched the issue or the patch was silently rolled back at some point for unknown reasons. The original PoC by Google worked without any changes," the researcher added. "To highlight this issue, I weaponized the original PoC to spawn a SYSTEM shell. It seems to work reliably in my machines butsuccess rate may vary since it's a race condition."

The researcher further pointed out that all Windows versions are likely affected by this vulnerability.

In a post shared on Mastodon, security researcher Will Dormann said MiniPlasma works "reliably" to open a "cmd.exe" prompt with SYSTEM privileges on Windows 11 systems running the latest May 2026 updates. "I'll note that it does not seem to work on the latest Insider Preview Canary Windows 11," Dormann [pointed out](https://infosec.exchange/%40wdormann/116584206761334151).

In December 2025, Microsoft also addressed another privilege escalation flaw in the same component ([CVE-2025-62221](https://thehackernews.com/2025/12/microsoft-issues-security-fixes-for-56.html), CVSS score: 7.8), which it identified as exploited by unknown threat actors.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Google Project Zero](https://thehackernews.com/search/label/Google%20Project%20Zero), [Microsoft](https://thehackernews.com/search/label/Microsoft), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Windows](https://thehackernews.com/search/label/Windows), [Windows 11](https://thehackernews.com/search/label/Windows%2011), [Zero-Day](https://thehackernews.com/search/label/Zero-Day)

⚡ Top Stories This Week

[![Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](data:image/svg+xml;base64... "Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak")

Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](https://thehackernews.com/2026/05/ollama-out-of-bounds-read-vulnerability.html)

[![Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](data:image/svg+xml;base64... "Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence")

Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html)

[![On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafted Email](data:image/svg+xml;base64... "On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafted Email")

On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafted Email](https://thehackernews.com/2026/05/on-prem-microsoft-exchange-server-cve.html)

[![Cisco Catalyst SD-WAN Controller Auth Bypass Actively Exploited to Gain Admin Access](data:image/svg+xml;base64... "Cisco Catalyst SD-WAN Controller Auth Bypass Actively Exploited to Gain Admin Access")

Cisco Catalyst SD-WAN Controller Auth Bypass Actively Exploited to Gain Admin Access](https://thehackernews.com/2026/05/cisco-catalyst-sd-wan-controller-auth.html)

[![ThreatsDay Bulletin: PAN-OS RCE, Mythos cURL Bug, AI Tokenizer Attacks, and 10+ Stories](data:image/svg+xml;base64... "ThreatsDay Bulletin: PAN-OS RCE, Mythos cURL Bug, AI Tokenizer Attacks, and 10+ Stories")

ThreatsDay Bulletin: PAN-OS RCE, Mythos cURL Bug, AI Tokenizer Attacks, and 10+ Stories](ht...