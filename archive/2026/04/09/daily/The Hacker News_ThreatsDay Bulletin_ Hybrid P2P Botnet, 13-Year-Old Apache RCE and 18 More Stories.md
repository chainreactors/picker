---
title: ThreatsDay Bulletin: Hybrid P2P Botnet, 13-Year-Old Apache RCE and 18 More Stories
url: https://thehackernews.com/2026/04/threatsday-bulletin-hybrid-p2p-botnet.html
source: The Hacker News
date: 2026-04-09
fetch_date: 2026-04-10T04:47:46.637120
---

# ThreatsDay Bulletin: Hybrid P2P Botnet, 13-Year-Old Apache RCE and 18 More Stories

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [ThreatsDay Bulletin: Hybrid P2P Botnet, 13-Year-Old Apache RCE and 18 More Stories](https://thehackernews.com/2026/04/threatsday-bulletin-hybrid-p2p-botnet.html)

**Ravie Lakshmanan**Apr 09, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6d4nK1zoWjzSmbdUmGPSycMwGmzcYM2XRrFH_ueobgO_8j7hwRdv8Ct856gg_k29HqAOw1-HGCtPpxyGDcuQIKY53ATLKb8bQCsJR5b_Jf8VqX1igItYBIe4iQazqSRe5fmFrFXS1fCcKdz6enbI6zYngIztjJ_UI262_ynNGJrd1EB_OUV1ZKYVl04-h/s1700-e365/threatsdays-main.jpg)

Thursday. Another week, another batch of things that probably should've been caught sooner but weren't.

This one's got some range — old vulnerabilities getting new life, a few "why was that even possible" moments, attackers leaning on platforms and tools you'd normally trust without thinking twice. Quiet escalations more than loud zero-days, but the kind that matter more in practice anyway.

Mix of malware, infrastructure exposure, AI-adjacent weirdness, and some supply chain stuff that's... not great. Let's get into it.

1. Resilient hybrid botnet surge

   [Phorpiex Botnet Detailed](https://www.bitsight.com/blog/ransomware-twizt-inside-phorpiex-botnet)

   A new variant of the botnet known as [Phorpiex](https://thehackernews.com/2021/12/new-phorpiex-botnet-variant-steals-half.html) (aka Trik) has been observed, using a hybrid communication model that combines traditional C2 HTTP polling with a peer-to-peer (P2P) protocol over both TCP and UDP to ensure operational continuity in the face of server takedowns. The malware acts as a conduit for encrypted payloads, making it challenging for external parties to inject or modify commands. The primary goal of Phorpiex's Twizt variant is to drop a clipper that re-routes cryptocurrency transactions, as well as distribute high-volume sextortion email spam and facilitate [ransomware deployment](https://thehackernews.com/2025/02/ransomhub-becomes-2024s-top-ransomware.html) (e.g., LockBit Black, Global). It also exhibits worm-like behavior by propagating through removable and remote drives, and drop modules responsible for exfiltrating mnemonic phrases and scanning for Local File Inclusion (LFI) vulnerabilities. "Phorpiex has consistently demonstrated its capability to evolve, shifting from a pure spam operation to a sophisticated platform," Bitsight [said](https://www.bitsight.com/blog/ransomware-twizt-inside-phorpiex-botnet). "The Phorpiex botnet remains a highly adaptive and resilient threat." There are about 125,000 infections daily on average, with the most affected countries being Iran, Uzbekistan, China, Kazakhstan, and Pakistan.
2. Chained flaws enable stealth RCE

   [13-Year-Old Flaw in Apache ActiveMQ Classic](https://horizon3.ai/attack-research/disclosures/cve-2026-34197-activemq-rce-jolokia/)

   A remote code execution (RCE) vulnerability that lurked in Apache ActiveMQ Classic for 13 years could be chained with an older flaw (CVE-2024-32114) to bypass authentication. Tracked as CVE-2026-34197 (CVSS score: 8.8), the newly identified bug allows attackers to invoke management operations through the Jolokia API and trick the message broker into retrieving a remote configuration file and executing operating system commands. According to Horizon3.ai, the security defect is a bypass for CVE-2022-41678, a bug that allows authenticated attackers to trigger arbitrary code execution and write web shells to disk. "The vulnerability requires credentials, but default credentials (admin:admin) are common in many environments," Horizon3.ai researcher Naveen Sunkavally [said](https://horizon3.ai/attack-research/disclosures/cve-2026-34197-activemq-rce-jolokia/). "On some versions (6.0.0 - 6.1.1), no credentials are required at all due to another vulnerability, CVE-2024-32114, which inadvertently exposes the Jolokia API without authentication. In those versions, CVE-2026-34197 is effectively an unauthenticated RCE." The newly discovered security defect was [addressed](https://activemq.apache.org/security-advisories.data/CVE-2026-34197-announcement.txt) in ActiveMQ Classic versions 5.19.4 and 6.2.3.
3. Cyber fraud losses hit record highs

   [Cybercrime Costs Victims $17.7B in 2025](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf)

   Cyber-enabled fraud cost victims over $17.7 billion during 2025, as financial losses to internet-enabled fraud continue to grow. The total loss exceeds $20.87 billion, up 26% from 2024. "Cyber-enabled fraud is responsible for almost 85% of all losses reported to IC3 [Internet Crime Complaint Center] in 2025," the U.S. Federal Bureau of Investigation (FBI) [said](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf). "Cryptocurrency investment fraud was the highest source of financial losses to Americans in 2025, with $7.2 billion reported in losses." In all investment scams led the pack with $8.6 billion in reported losses, followed by business email compromise ($3 billion) and tech support scams ($2.1 billion). Sixty-three new ransomware variants were identified last year, leading to more than $32 million in losses. Akira, Qilin, INC./Lynx/Sinobi, BianLian, Play, Ransomhub, Lockbit, Dragonforce, Safepay, and Medusa emerged as the top ten variants to hit critical manufacturing, healthcare, public health, and government entities.
4. AI-driven DDoS tactics escalate

   [8M DDoS Attacks in H2 2025](https://www.netscout.com/blog/how-botnet-driven-ddos-attacks-evolved-2h-2025)

   According to data from NETSCOUT, more than 8 million DDoS attacks were recorded across 203 countries and territories between July and December 2025. "The attack count remained stable compared to the first half of the year, but the nature and sophistication of attacks changed dramatically," the company [said](https://www.netscout.com/blog/how-botnet-driven-ddos-attacks-evolved-2h-2025). "The TurboMirai class of IoT botnets, including AISURU and Eleven11 (RapperBot), emerged as a major force. DDoS-for-hire platforms are now integrating dark-web LLMs and conversational AI, lowering the technical barrier for launching complex, multi-vector attacks. Even unskilled threat actors can now orchestrate sophisticated campaigns using natural-language prompts, increasing risk for all industries."
5. Insider breach exposes private phot...