---
title: PaperCut Attacker Uses Hundreds of AI Agents to Compromise 440+ Instances
url: https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html
source: The Hacker News
date: 2026-09-10
fetch_date: 2026-09-11T06:53:20.049640
---

# PaperCut Attacker Uses Hundreds of AI Agents to Compromise 440+ Instances

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

# [PaperCut Attacker Uses Hundreds of AI Agents to Compromise 440+ Instances](https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html)

**Ravie Lakshmanan**Sep 10, 2026Cyber Attack / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkLW3i6mB4uE2g7Ze6CDAess3UTTeol7YmRP-N3uTkLJHPglZc0BHvTlESyulvcTp05ObPwuGY5XHqV9q599pqLmK-ypamAPNUdHa9y-34Q4IEE3EBId9UrN9L0J3zK1TTf1Atovhkz51Gk_2gul7DmjvLmJd7BbwgqMhmVODTiQUuqu_IdFFGJt0WAiC_/s1700-nu-rw-lo-l85-e365/paper.jpg)

A suspected Russian-speaking cyber actor has been attributed to the use of artificial intelligence (AI) to devise exploits targeting a recently disclosed pair of [security flaws in PaperCut NG/MF](https://thehackernews.com/2026/09/attackers-exploit-papercut-flaws-to.html) and break into hundreds of instances.

According to independent reports from [Blackpoint Cyber](https://blackpointcyber.com/blog/death-by-a-thousand-papercuts-ai-driven-exploitation-at-scale/) and [GreyNoise](https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf), the activity originates from "[45.142.193[.]132](https://www.virustotal.com/gui/ip-address/45.142.193.132/)," an IP address that has been linked to unauthorized port scanning and brute-force attack attempts in recent weeks. It's worth noting the same IP address was also [flagged](https://thehackernews.com/2026/09/attackers-exploit-papercut-flaws-to.html) by Arctic Wolf in connection with the exploitation activity last week.

"At this time, we cannot confirm the exact end goal of this campaign," Nevan Beal, principal MDR analyst at Blackpoint, told The Hacker News. "The threat actor's methodology is consistent with initial-access activity, but we do not yet have sufficient evidence to confirm whether they are operating as an initial access broker."

At its core, the opportunistic attacks exploit CVE-2026-81578 and CVE-2026-82078, a combination of an authentication bypass and remote code execution chain, to mainly target the education sector in the U.S., the U.K., France, Spain, Canada, Belgium, Portugal, Australia, Germany, and Switzerland.

"Observed post-exploitation activity included delivery of Windows registry hive collection tools, Metasploit/Meterpreter-related Java payloads, and commands used to identify hosts, users, processes, and sensitive configuration data," Arctic Wolf noted.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

GreyNoise said it has been tracking the malicious use of the IP address since early July 2026 for probing internet-facing systems from several vendors, including Palo Alto, Ubiquiti, Citrix, SonicWall, and Proxmox VE.

"As part of the adversary's exploit development and testing, they built and attacked a lab environment that included the vulnerable PaperCut software and an Active Directory server," the threat intelligence firm said. "In parallel workflows, the adversary built target lists using an internet scanning service Netlas.io using an identified API key."

Upon gaining remote code execution and credential harvesting within its self-hosted lab environment, the threat actor has been observed unleashing hundreds of AI Agents powered by OpenAI Codex, a DeepSeek model, and publicly available offensive security tools (e.g., Mimikatz, SharpHound, Certipy, Rubeus, and Impacket) to compromise no less than 440 instances of PaperCut MF/NG hosted by 395 identified victim organizations in 48 countries.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilPXRZNH8jWQM0MAYBAWgRfm-H72AtvbKjS_Fb6GbMKRIFuIYpc6ctddSJT-zqabBxiCOe9o4GKLjeyKD3q_VSxHxspHsnUNaKcL_ijZkU6RNYjUN-gwkd979gvzusIXhh5EhjYALdPoAuYwMDx1oTNnBT_iZR_kLDXwUccgwpwJ2___oc5VIhiG04hJTA/s1700-nu-rw-lo-l85-e365/paper-1.png)

"There are other real victims that could not be attributed to a named organization," GreyNoise added. "The adversary did explicitly attempt to avoid targeting entities in 28 identified countries; however, our observed victimology shows the attempted restraint failed in some instances." Some of the countries added to the exclusion list include Russia, China, Hong Kong, Thailand, Iran, Venezuela, Indonesia, Pakistan, and Bangladesh.

The findings come at a time of considerable concern over how AI models are enabling bad actors to integrate agentic capabilities into various stages of an attack lifecycle, and help them accelerate and conduct attacks at scale.

According to GreyNoise, the attacker swiftly progressed from an empty workspace to first achieving remote code execution against a real victim in just under four hours, and compromised at least 11 organizations in 26 seconds once the campaign began in earnest. In one attack targeting a high school in the U.S., the duration between initial access and full domain administrator access was a mere seven minutes.

In all, the adversary is said to have gained domain administrator access against only 12 victim organizations. The attacker's end goals remain unclear at this stage.

"It is unclear if this actor is solely focused on access development to be handed off to other affiliated actors or if they will directly leverage their accesses to achieve follow-on objectives such as data theft or ransomware deployment," GreyNoise said.

### More Details Emerge

Blackpoint, which shared additional details of the same activity, said it traced it back to an exposed operator infrastructure that depicts the AI-assisted workflow from vulnerability research and exploit development to execution through target filtering, failure analysis, code changes, and repeated retry waves.

"The earliest recovered activity began on August 31, with the project focused on vulnerability research and comparing patched and unpatched PaperCut builds," Beal and security researcher Sam Decker wrote. "Within hours, that research had been turned into a multi-threaded validation tool that was reviewed, tested, and...