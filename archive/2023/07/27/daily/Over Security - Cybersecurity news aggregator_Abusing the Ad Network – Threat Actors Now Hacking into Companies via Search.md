---
title: Abusing the Ad Network – Threat Actors Now Hacking into Companies via Search
url: https://www.bitdefender.com/blog/labs/abusing-the-ad-network-threat-actors-now-hacking-into-companies-via-search/
source: Over Security - Cybersecurity news aggregator
date: 2023-07-27
fetch_date: 2025-10-04T11:55:46.475024
---

# Abusing the Ad Network – Threat Actors Now Hacking into Companies via Search

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Whitepapers](/en-us/blog/labs/tag/whitepapers "Whitepapers")[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

min read

# Abusing the Ad Network – Threat Actors Now Hacking into Companies via Search

[![Victor VRABIE](https://blogapp.bitdefender.com/labs/content/images/size/w100/2021/05/vvrabie-150x150.png "Victor VRABIE")](/en-us/blog/labs/author/vvrabie "Victor VRABIE")[![Alexandru MAXIMCIUC](https://blogapp.bitdefender.com/labs/content/images/size/w100/2020/11/amaximciuc.png "Alexandru MAXIMCIUC")](/en-us/blog/labs/author/amaximciuc "Alexandru MAXIMCIUC")

[Victor VRABIE](/en-us/blog/labs/author/vvrabie "Victor VRABIE")[Alexandru MAXIMCIUC](/en-us/blog/labs/author/amaximciuc "Alexandru MAXIMCIUC")

July 26, 2023

*Promo*

Protect all your devices, without slowing them down.
 [Free 30-day trial](../../Downloads/)

  ![Abusing the Ad Network – Threat Actors Now Hacking into Companies via Search](https://blogapp.bitdefender.com/labs/content/images/size/w600/2023/07/email-g4a0b69e04_1920.png "Abusing the Ad Network – Threat Actors Now Hacking into Companies via Search")

For the past few years, hackers have increasingly targeted customers and businesses with tainted software boosted via ads. The recipe is simple – cyber-criminal groups set up fake websites for high-interest software and promote them on top of the results page through advertisements.

It takes just one search and one click for a user to fall victim to the trick. Testament to that is the series of attacks against prominent crypto-currency figures earlier in 2023 as well as a recent spate of incidents Bitdefender investigated in the second part of the year.

This report is based on an investigation into threat actors’ use of a malicious ISO archive to offer business users more than they bargained for. Besides the software it advertised, the malicious ISO file contained a ZIP archive holding a Python executable and its dependencies. One DLL loaded by the python.exe process was set to execute malicious code in the form of a Meterpreter stager, giving the attackers access to the victim’s computer.

Starting with that subset of indicators, Bitdefender researchers were able to identify more artifacts related to the same campaign that seems to have started at least as far back as May 2023. The malicious ISO archives were distributed using malicious ads that impersonated download pages for applications such as AnyDesk, WinSCP, Cisco AnyConnect, Slack, TreeSize and potentially more.
The same campaign seems to have caught the attention of multiple security researchers, and we would like to join their efforts by sharing our own findings.

This malvertising campaign leads to the propagation of the infection after initial exposure. For as long as they dwell in the victim’s network, the attackers’ primary goal is to obtain credentials, set up persistence on important systems and exfiltrate data, with extortion as the end goal. We also noticed attempts to deploy BlackCat ransomware.

**Findings at a glance:**

* A threat actor with previous roots in cybercrime has shifted its initial access techniques to search engine advertisements to hijack searches for business applications such as AnyDesk, WinSCP, Cisco AnyConnect, Slack, TreeSize and potentially more;
* Our research shows that the actor(s) has successfully used this type of attack since late May 2023.
* Based on our threat insights, attackers seem to exclusively focus on North America. Until now, we have identified six target
  organizations in the US and one in Canada.

## Indicators of Compromise

An up-to-date, complete list of indicators of compromise is available to  [Bitdefender Advanced Threat Intelligence](https://www.bitdefender.com/oem/advanced-threat-intelligence.html) users. Currently known indicators of compromise can be found in the whitepaper below.

[Download the research paper](https://blogapp.bitdefender.com/labs/content/files/2023/07/Bitdefender-PR-WhitePaper-RatNitro-dex14210-en_EN.pdf)

tags

[Whitepapers](/en-us/blog/labs/tag/whitepapers "Whitepapers")[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

---

### Author

---

[![Victor VRABIE](https://blogapp.bitdefender.com/labs/content/images/size/w300/2021/05/vvrabie-150x150.png "Victor VRABIE")](/en-us/blog/labs/author/vvrabie "Victor VRABIE")

[## Victor VRABIE](/en-us/blog/labs/author/vvrabie "Victor VRABIE")

Victor VRABIE is a security researcher at Bitdefender Iasi, Romania. Focusing on malware research, advanced persistent threats and cybercrime investigations, he's also a graduate of Computer Sciences.

[View all posts](/en-us/blog/labs/author/vvrabie)

[![Alexandru MAXIMCIUC](https://blogapp.bitdefender.com/labs/content/images/size/w300/2020/11/amaximciuc.png "Alexandru MAXIMCIUC")](/en-us/blog/labs/author/amaximciuc "Alexandru MAXIMCIUC")

[## Alexandru MAXIMCIUC](/en-us/blog/labs/author/amaximciuc "Alexandru MAXIMCIUC")

I'm a veteran security researcher with more than a decade of experience. His research is mostly focused on exploits, advanced persistent threats, cybercrime investigations, and packing technologies.

[View all posts](/en-us/blog/labs/author/amaximciuc)

---

## Right now Top posts

[![Active Subscription Scam Campaigns Flooding the Internet](https://blogapp.bitdefender.com/labs/content/images/size/w300/2025/04/advanced_persistent_threats.jpg "Active Subscription Scam Campaigns Flooding the Internet")](/en-us/blog/labs/active-subscription-scam-campaigns-flooding-the-internet "Active Subscription Scam Campaigns Flooding the Internet")

[Scam Research](/en-us/blog/labs/tag/scam-research "Scam Research")

[### Active Subscription Scam Campaigns Flooding the Internet](/en-us/blog/labs/active-subscription-scam-campaigns-flooding-the-internet "Active Subscription Scam Campaigns Flooding the Internet")

April 30, 2025

min read

[![Infected Minecraft Mods Lead to Multi-Stage, Multi-Platform Infostealer Malware](https://blogapp.bitdefender.com/labs/content/images/size/w300/2023/06/minecraft-1106252_1920.jpg "Infected Minecraft Mods Lead to Multi-Stage, Multi-Platform Infostealer Malware")](/en-us/blog/labs/infected-minecraft-mods-lead-to-multi-stage-multi-platform-infostealer-malware "Infected Minecraft Mods Lead to Multi-Stage, Multi-Platform Infostealer Malware")

[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

[### Infected Minecraft Mods Lead to Multi-Stage, Multi-Platform Infostealer Malware](/en-us/blog/labs/infected-minecraft-mods-lead-to-multi-stage-multi-platform-infostealer-malware "Infected Minecraft Mods Lead to Multi-Stage, Multi-Platform Infostealer Malware")

June 08, 2023

min read

[![Vulnerabilities identified in Amazon Fire TV Stick, Insignia FireOS TV Series](https://blogapp.bitdefender.com/labs/content/images/size/w300/2023/05/old-tv-gab6450206_1920.png "Vulnerabilities identified in
Amazon Fire TV Stick, Insignia
FireOS TV Series")](/en-us/blog/labs/vulnerabilities-identified-amazon-fire-tv-stick-insignia-fire-os-tv-series "Vulnerabilities identified in
Amazon Fire TV Stick, Insignia
FireOS TV Series")

[IoT Research](/en-us/blog/labs/tag/iot-research "IoT Research")[Whitepapers](/en-us/blog/labs/tag/whitepapers "Whitepapers")

[### Vulnerabilities identified in Amazon Fire TV Stick, Insignia FireOS TV Series](/en-us/blog/labs/vulnerabilities-identified-amazon-fire-tv-stick-insignia-fire-os-tv-series "Vulnerabilities identified in
Amazon Fire TV Stick, Insignia
FireOS TV Series")

May 02, 2023

min read

[![EyeSpy - Iranian Spyware Deliv...