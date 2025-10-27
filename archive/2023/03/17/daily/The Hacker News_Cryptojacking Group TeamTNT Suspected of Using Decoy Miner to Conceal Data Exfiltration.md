---
title: Cryptojacking Group TeamTNT Suspected of Using Decoy Miner to Conceal Data Exfiltration
url: https://thehackernews.com/2023/03/cryptojacking-group-teamtnt-suspected.html
source: The Hacker News
date: 2023-03-17
fetch_date: 2025-10-04T09:54:07.318674
---

# Cryptojacking Group TeamTNT Suspected of Using Decoy Miner to Conceal Data Exfiltration

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Cryptojacking Group TeamTNT Suspected of Using Decoy Miner to Conceal Data Exfiltration](https://thehackernews.com/2023/03/cryptojacking-group-teamtnt-suspected.html)

**Mar 16, 2023**Ravie LakshmananCryptojacking / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2Qb6QnUx-0NvP_-MNsNMIf2-NxyyGi9vTft5Rtw5I-KSOPbzDStPyOe1KMx92M5O3gmXOAqZ7M7Sojqfh2-JW5opd6-BRnKYZFqj8cvFIrwZrmL6qVQ3hZx6H7Zqtipyg-qLk-nEeUqghLw_MMRHA4aM10dabX-Ia_KZIKXB6O4OUIobzH_wy47Ox/s790-rw-e365/hacking.png)

The cryptojacking group known as **TeamTNT** is suspected to be behind a previously undiscovered strain of malware used to mine Monero cryptocurrency on compromised systems.

That's according to Cado Security, which [found](https://www.virustotal.com/gui/file/595497c407795e0dbb562a4616fd877ce1eb2e86424672bac8003662e1fa07eb/) the [sample](https://www.virustotal.com/gui/file/61fdad6d9b149e8d4fc54a848a25219eb9f1364a58073c27eadde8f8298a9573/) after Sysdig detailed a sophisticated attack known as [SCARLETEEL](https://thehackernews.com/2023/03/hackers-exploit-containerized.html) aimed at containerized environments to ultimately steal proprietary data and software.

Specifically, the early phase of the attack chain involved the use of a cryptocurrency miner, which the cloud security firm suspected was deployed as a decoy to conceal the detection of data exfiltration.

The artifact – uploaded to VirusTotal late last month – "bear[s] several syntactic and semantic similarities to prior TeamTNT payloads, and includes a wallet ID that has previously been attributed to them," a new analysis from Cado Security has [revealed](https://www.cadosecurity.com/previously-undiscovered-teamtnt-payload-recently-surfaced/).

[TeamTNT](https://thehackernews.com/2022/04/watch-out-cryptocurrency-miners.html), active since at least 2019, has been documented to repeatedly strike cloud and container environments to deploy cryptocurrency miners. It's also known to unleash a crypto mining worm capable of [stealing AWS credentials](https://thehackernews.com/2020/09/cloud-monitoring.html).

While the threat actor willingly shut down their operations in November 2021, cloud security firm Aqua [disclosed](https://thehackernews.com/2022/09/hackers-targeting-weblogic-servers-and.html) in September 2022 a fresh set of attacks mounted by the group targeting misconfigured Docker and Redis instances.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

That said, there are also indications that rival crews such as [WatchDog](https://www.trendmicro.com/en_us/research/22/j/teamtnt-returns-or-does-it.html) might be mimicking TeamTNT's tactics, techniques, and procedures (TTPs) to foil attribution efforts.

Another activity cluster of note is [Kiss-a-dog](https://thehackernews.com/2022/10/new-cryptojacking-campaign-targeting.html), which also relies on tools and command-and-control (C2) infrastructure previously associated with TeamTNT to mine cryptocurrency.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrio3gsQ3VaA1dm0i86Imm_gxdKQFoDxAOcDghNGZBJFd3vminT1LotY7lkyqjnBMrkRAOAfmkUScg8-zOwGxjpQX8gam6Yed-JzG6C8fPfZbUFRYexISBftSJJBSI2iWlH08HPQ2JESK--_iKCNXF-pQ0k599gAG00M7K0prgEdi9TPWwDM4FiplV/s790-rw-e365/a.png)

There is no concrete evidence to tie the new malware to the SCARLETEEL attack. But Cado Security pointed out that the sample surfaced around the same time the latter was reported, raising the possibility that this could be the "decoy" miner that was installed.

The shell script, for its part, takes preparatory steps to reconfigure [resource hard limits](https://www.ibm.com/docs/en/aix/7.3?topic=u-ulimit-command), prevent command history logging, accept all ingress or egress traffic, enumerate hardware resources, and even clean up prior compromises before commencing the activity.

Like other TeamTNT-linked attacks, the malicious payload also leverages a technique referred to as [dynamic linker hijacking](https://attack.mitre.org/techniques/T1574/006/) to cloak the miner process via a shared object [executable](https://github.com/gianlucaborello/libprocesshider) called [libprocesshider](https://www.virustotal.com/gui/file/c8d05df48e059da25ff3786470f52a4c4918851db742a02887fa592c5b38d101/) that uses the [LD\_PRELOAD](https://www.cadosecurity.com/linux-attack-techniques-dynamic-linker-hijacking-with-ld-preload/) environment variable.

Persistence is achieved by three different means, one of which modifies the [.profile file](https://www.ibm.com/docs/en/aix/7.3?topic=formats-profile-file-format), to ensure that the miner continues to run across system reboots.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings come as another crypto miner group dubbed the [8220 Gang](https://thehackernews.com/2023/03/new-scrubcrypt-crypter-used-in.html) has been observed using a crypter called ScrubCrypt to carry out illicit cryptojacking operations.

What's more, unknown threat actors [have been found](https://thehackernews.com/2023/03/new-cryptojacking-operation-targeting.html) targeting vulnerable Kubernetes container orchestrator infrastructure with exposed APIs to mine the Dero cryptocurrency, marking a shift from Monero.

Cybersecurity company Morphisec, last month, also shed light on an evasive malware campaign that leverages the [ProxyShell vulnerabilities](https://thehackernews.com/2021/11/hackers-exploiting-proxylogon-and.html) in Microsoft Exchange servers to drop a crypto miner strain codenamed [ProxyShellMiner](https://blog.morphisec.com/proxyshellminer-campaign).

"[Mining cryptocurrency](https://thehackernews.com/2023/03/new-cryptojacking-campaign-leverages.html) on an organization's network can lead to system performance degradation, increased power consumption, equipment overheating, and can stop services," the researchers said. "It allows threat actors access for even more nefarious ends."

## **Update*...