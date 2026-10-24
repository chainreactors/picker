---
title: Russia-Linked Hackers Used New Mesh Network Backdoor in Destructive Ukraine Attack
url: https://thehackernews.com/2026/10/russian-linked-hackers-used-new-mesh.html
source: The Hacker News
date: 2026-10-23
fetch_date: 2026-10-24T06:48:22.250595
---

# Russia-Linked Hackers Used New Mesh Network Backdoor in Destructive Ukraine Attack

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Russia-Linked Hackers Used New Mesh Network Backdoor in Destructive Ukraine Attack](https://thehackernews.com/2026/10/russian-linked-hackers-used-new-mesh.html)

**Ravie Lakshmanan**Oct 23, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxH9YdfH7FHfSBJt7wrnd1P2hTQG6_2rpkp3YBqp2Yd49nYy4-a0zmvk5mqKlXH4DWfRO4Q4MmzLG4_t19me5rErcvoEpGJ5Q8LYty_GXXys63QC8HlO3G2jRC9f5vJd1BDiOp4APzxV4rSbFOZY80zIUmxvJ8V6isB-eDy9e9tVWaLR53fpPO80mzn_BH/s1700-nu-rw-lo-l85-e365/uk-russia.jpg)

The Russian state-sponsored hacking group **Sandworm** teamed up with another threat actor to carry out a destructive wiping attack targeting a Ukrainian logistics company last year.

According to [ESET](https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/), the attack involved [UAC-0099](https://thehackernews.com/2026/10/uac-0099-targets-ukrainian-government.html) (aka Earth Sirrush) obtaining initial access to the target on July 16, 2025, via a spear-phishing email bearing a malware-laced attachment that led to the deployment of the MATCHWOK backdoor through a downloader called MATCHBOIL.

The activity ultimately culminated with the threat actor handing off access to Sandworm, which then conducted a data-wiping attack on September 17, 2025, more than two months after it obtained a foothold.

What makes the attack stand out is UAC-0099's use of a previously undocumented backdoor called MythicRatatoskr that communicates with a command-and-control (C2) server hosted inside the Yggdrasil mesh network. The backdoor was deployed a day after MATCHWOK was executed.

There are indications that development on the backdoor started sometime between December 2024 and February 2025. Its functionality is fairly straightforward in that it sends victim metadata to the C2 server, poll for new commands, transmit command output, take screenshots, and upload/download files.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

It can also alter the current working directory, enumerate directory contents, change the C2 server URL, execute a shell command via "cmd.exe," and spawn a reverse SOCKS5 proxy. In addition, some artifacts include a 10-minute startup delay in a likely effort to avoid immediately connecting to the Yggdrasil network and evade detection.

"To our knowledge, this is the first documented case of Yggdrasil being abused in this way by a state-aligned threat actor, and it may signal a broader trend of adversaries adopting experimental peer-to-peer networks to increase the resilience and stealth of their infrastructure," ESET researchers Anton Cherepanov and Peter Strýček said.

MythicRatatoskr is said to have been used to deploy a SOCKS5 server to route connections through the compromised network. The attack culminated with Sandworm carrying out a data-wiping attack by dropping the SDelete utility via Active Directory Group Policy. It's worth noting that the Sandworm-linked [NikoWiper](https://thehackernews.com/2023/01/new-report-reveals-nikowiper-malware.html) malware is also derived from SDelete.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnHBbozozFukXkCOkHaaC569gciokco_OadwOEydnfineh9AGa3PjJ6Gj4btxJycTHJIElOQn0nz8yiWo_ECTTOW0biPM84TL9DT4fbtQjyOJEMSz0-uZHu65jBaP2jeE-tyKO7h9xpGWHvrqcFuYXxJFYRQplzG9PRhK4U3rI1kFsgWqnoZ7FC-KtxxC8/s1700-nu-rw-lo-l85-e365/candc.png) |
| Yggdrasil map with the C&C serve |

While the attack investigated by ESET compromised a Windows system, source code references to "crond" within MythicRatatoskr suggest there possibly exists an equivalent Linux version of the malware.

The assessment that UAC-0099 is likely collaborating with Sandworm is not new. In its APT Activity Report Q2 2025–Q3 2025, ESET [said](https://thehackernews.com/2025/11/trojanized-eset-installers-drop.html) it observed UAC-0099 conducting initial access operations and subsequently transferring "validated targets" to Sandworm for further post-exploitation.

These attacks targeted government, energy, logistics, and grain sectors in Ukraine, the Slovak cybersecurity company noted at the time. ESET confirmed to The Hacker News that the MythicRatatoskr case was among those attacks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

This sort of cooperation between Russia-aligned actors is also not new. Last year, ESET said it [identified evidence](https://thehackernews.com/2025/09/russian-hackers-gamaredon-and-turla.html) that Gamaredon and Turla were working together to target and co-compromise Ukrainian entities, with one intrusion leveraging Gamaredon's PteroGraphin to deploy Turla's Kazuar backdoor.

Furthermore, a Gamaredon-linked downloader called Pterodo has been [used](https://thehackernews.com/2020/06/invisimole-hackers.html) to retrieve and execute [InvisiMole](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/), a modular spyware program put to use against targets in Ukraine and Russia.

"This kind of cooperation underscores the potential for coordinated cyber espionage campaigns among Russia-aligned groups, likely intended to amplify their operational impact," ESET said.

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
[...