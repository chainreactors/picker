---
title: Aurora Ransomware Operators Use Cursor AI in Attacks Against 10 Targets
url: https://thehackernews.com/2026/08/aurora-ransomware-operators-use-cursor.html
source: The Hacker News
date: 2026-08-31
fetch_date: 2026-09-01T07:01:28.739489
---

# Aurora Ransomware Operators Use Cursor AI in Attacks Against 10 Targets

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

# [Aurora Ransomware Operators Use Cursor AI in Attacks Against 10 Targets](https://thehackernews.com/2026/08/aurora-ransomware-operators-use-cursor.html)

**Ravie Lakshmanan**Aug 31, 2026Artificial Intelligence / Ransomware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHyB4qaQy8srcEIgc1oMi08PMKtoVFIsmW3ho_7f7rISFML8Kmz8jYzDE1FCN9Nfo4LvvgVFV_FEijgLbCrZcJ5zy7xlvAYTKuyGrcE0IU6yqEd-awlmOyRQ3FXcSeA5yM71NLDa5nxpj9taGnNiVXvCb_5tun5j3dfb6z8j7cmwQ2O0PE2V3y0oKWv6sB/s1700-nu-rw-lo-l85-e365/cursor.jpg)

Threat actors associated with Aurora (aka Aur0ra) ransomware have been observed using SpaceX's artificial intelligence (AI)-powered coding assistant Cursor to break into target networks, according to findings from [CloudSEK](https://www.cloudsek.com/blog/aurora-ransomware-affiliate-ai-attack-planning-crypto-payments) and [Gambit Security](https://gambit.security/blog-posts/aurora-ransomware-targets-esxi-abuses-cursor-agent-for-exploitation).

The two independent analyses are based on exposed infrastructure associated with the Russian-speaking cybercrime group, leading to the discovery of its toolkit, shell history, and encryptor. CloudSEK said the exposed open directory leaked "months of activity" that was active against more than 20 organizations across nine countries between April and July 2026. Four of those victims have since been listed on its data leak site.

"The operator used Cursor, an agentic coding assistant, to plan attacks in Russian, while excluding CIS [Commonwealth of Independent States] ranges and CIS-country domains, without exception," CloudSEK noted.

Details about Aurora first emerged in late May 2026, with CYFIRMA [highlighting](https://www.cyfirma.com/news/weekly-intelligence-report-22-may-2026/) attacks primarily targeting Windows systems and its continued technical development through incremental updates and feature expansion. Data from Ransomware.Live lists [33 victims](https://ransomware.live/group/aurora) located in the U.S., Germany, the Netherlands, Canada, and the U.K.

In one case [detailed](https://activesoc.blackhillsinfosec.com/blog/introducing-the-aur0ra-ransomware-group/) by Black Hills Information Security earlier this month, initial access was achieved via aggressive email bombing followed by [making phone calls to employees](https://thehackernews.com/2026/08/twinloot-abuses-sharepoint-and-teams-to.html) by posing as IT help desk personnel to assist them in dealing with the issue, only to establish remote access using an open-source utility called [Xray-core](https://github.com/xtls/xray-core).

The attack chain subsequently involves lateral movement via SMB, LDAP, WinRM, RDP, and RPC, obtaining access to high-privilege administrator accounts, and abusing them to evade detection by clearing logs and disabling Microsoft Defender before harvesting and exfiltrating sensitive data and deploying the encryptor.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

CloudSEK said it identified both Windows and Linux versions of Aurora written in Zig, adding the operator's recovered chat history shows heavy use of Cursor for planning various phases of the attack. This includes a full Active Directory Certificate Services (AD CS) exploitation plan written in Russian.

"Both encryptor binaries, the Windows sap.exe and the Linux/ESXi encrypt.out, are static builds from a single Zig codebase, compiled for different targets rather than written twice," the company noted. "The Windows binary even carries the Linux build's usage examples inside it, a leftover from sharing one source tree across both platforms."

The Windows variant is also equipped to inhibit system recovery through the deletion of volume shadow copies and disabling System Restore directly via the Registry. The Linux and ESXi variant, on the other hand, attempts to forcefully kill every single virtual machine on the host prior to starting encryption.

Furthermore, a key recovered from the Aurora encryptor is said to have granted access to a ransom negotiation between the threat actor and an unspecified victim, and a cluster of four cryptocurrency wallets that show varying splits between affiliates and the main operators. Affiliates have been found to get a cut anywhere between 54% and 79%, while the rest goes to the administrators.

This indicates that the affiliate cut of the ransom amount is decided per victim and depends on the ransom amount demanded and the victim's revenue figures. The illicit funds and then laundered and cashed out.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgreORI5cSHtS_A-kocRNn-uP7k4OiISym1UJoaNq24jFBe7kkJp6SOn_7saONX3H0_O730QBEbAHLnfvyNDt5Q6wcXxtjYG-svaGbbe6pkLCGC-iDhkmOTyTHGKWpeZxsqpR4aV-69JgjlbLQ_DXwZRgLOp-C0ST0iwOB2mS8UButaxmNnEIcW8-LTk__C/s1700-nu-rw-lo-l85-e365/aurora.png)

Gambit Security, which released its own insights into the activity, said it observed the Aurora operator using Cursor Agent, running Anthropic's Claude Sonnet, to help with hands-on exploitation against 10 targets between April 8 and May 21, 2026.

"In these cases the agent was given credentials or an existing route into the victim organization," Eyal Sela, director of threat intelligence at Gambit Security, said. "Then it was tasked with various exploitation activities."

"The agent was tasked with standard exploitation tasks. In some cases, the attacker only asked the agent to achieve an objective, such as 'tell me what rights the user has,' while in others, they told the agent which exploitation tool to use or instructed it to follow a previously generated attack plan. In some cases, the Agent gave a list of potential next steps - and all the attacker did was reply with a number corresponding to one of them."

Some of the tasks offloaded to the agent are listed below -

* Installing a VPN client or proxychains, then configuring it and connecting to a victim with supplie...