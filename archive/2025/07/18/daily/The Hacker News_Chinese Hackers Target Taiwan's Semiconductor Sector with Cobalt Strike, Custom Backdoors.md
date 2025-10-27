---
title: Chinese Hackers Target Taiwan's Semiconductor Sector with Cobalt Strike, Custom Backdoors
url: https://thehackernews.com/2025/07/chinese-hackers-target-taiwans.html
source: The Hacker News
date: 2025-07-18
fetch_date: 2025-10-07T00:01:10.814457
---

# Chinese Hackers Target Taiwan's Semiconductor Sector with Cobalt Strike, Custom Backdoors

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

# [Chinese Hackers Target Taiwan's Semiconductor Sector with Cobalt Strike, Custom Backdoors](https://thehackernews.com/2025/07/chinese-hackers-target-taiwans.html)

**Jul 17, 2025**Ravie LakshmananMalware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgqn-xJYAFWxSIN8brxFHDZJ57qrJfXin_aBJd44eodbcPNVy7tq-_XacRVKyt4Fh2nbX6ZMq3g_ohkQQoa1gKU48jGRLcs5SG4tVaDB_Q7SY9OiPUuQ5r9I9-ZDFrLymyNcgM28v1mc8xuRMZ5hngzX_-UYjhkPH0_Vw-75mc4kAFdNQ-01bqugHfYvehk/s790-rw-e365/chinese-hackers.jpg)

The Taiwanese semiconductor industry has become the target of spear-phishing campaigns undertaken by three previously undocumented Chinese state-sponsored threat actors.

"Targets of these campaigns ranged from organizations involved in the manufacturing, design, and testing of semiconductors and integrated circuits, wider equipment and services supply chain entities within this sector, as well as financial investment analysts specializing in the Taiwanese semiconductor market," Proofpoint [said](https://www.proofpoint.com/us/blog/threat-insight/phish-china-aligned-espionage-actors-ramp-up-taiwan-semiconductor-targeting) in a report published Wednesday.

The activity, per the enterprise security firm, took place between March and June 2025. They have been attributed to three China-aligned clusters it tracks as UNK\_FistBump, UNK\_DropPitch, and UNK\_SparkyCarp.

UNK\_FistBump is said to have targeted semiconductor design, packaging, manufacturing, and supply chain organizations in employment-themed phishing campaigns that resulted in the delivery of Cobalt Strike or a C-based custom backdoor dubbed [Voldemort](https://thehackernews.com/2024/08/cyberattackers-exploit-google-sheets.html) that has been previously used in attacks aimed at over 70 organizations globally.

The attack chain involves the threat actor posing as a graduate student in emails sent to recruitment and human resources personnel, seeking job opportunities at the targeted company.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The messages, likely sent from compromised accounts, include a purported resume (a LNK file masquerading as a PDF) that, when opened, triggers a multi-stage sequence that either leads to the deployment of Cobalt Strike or Voldemort. Simultaneously, a decoy document is displayed to the victim to avoid raising suspicion.

The use of Voldemort has been attributed by Proofpoint to a threat actor called TA415, which overlaps with the prolific Chinese nation-state group referred to as APT41 and Brass Typhoon. That said, the Voldemort activity linked to UNK\_FistBump is assessed to be distinct from TA415 due to differences in the loader used to drop Cobalt Strike and the reliance on a hard-coded IP address for command-and-control.

UNK\_DropPitch, on the other hand, has been observed striking individuals in multiple major investment firms who focus on investment analysis, particularly within the Taiwanese semiconductor industry. The phishing emails, sent in April and May 2025, embed a link to a PDF document, which, upon opening, downloads a ZIP file containing a malicious DLL payload that's launched using DLL side-loading.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHLcNPATItVMjcCP_iWazYC_O_-8tPEeAewmF_8A-nYuNg1QJX6IoqrsGOIDIXNDxJ2XnpBiGIQtI5P_wsfBXGBeNHnENCVTOjxAXth3Mqpm-Wn6z-o5r4BJ9hVhW9_i_dyS_4s6HxtDPBw1ADTs4HeKkJX54d9xcYk_jm2zmNMVo4mn5EUX4xJKMf2ESg/s790-rw-e365/opshih.png)

The rogue DLL is a backdoor codenamed HealthKick that's capable of executing commands, capturing the results of those runs, and exfiltrating them to a C2 server. In another attack detected in late May 2025, the same DLL side-loading approach has been put to use to spawn a TCP reverse shell that establishes contact with an actor-controlled VPS server 45.141.139[.]222 over TCP port 465.

The reverse shell serves as a pathway for the attackers to conduct reconnaissance and discovery steps, and if deemed of interest, drop the Intel Endpoint Management Assistant (EMA) for remote control via the C2 domain "ema.moctw[.]info."

"This UNK\_DropPitch targeting is exemplary of intelligence collection priorities spanning less obvious areas of the semiconductor ecosystem beyond just design and manufacturing entities," Proofpoint said.

Further analysis of the threat actor infrastructure has revealed that two of the servers have been configured as SoftEther VPN servers, an open-source VPN solution [widely](https://thehackernews.com/2024/06/redjuliett-cyber-espionage-campaign.html) [used](https://thehackernews.com/2024/11/china-aligned-mirrorface-hackers-target.html) by [Chinese hacking groups](https://thehackernews.com/2025/05/chinese-hackers-exploit-sap-rce-flaw.html). An additional connection to China comes from the reuse of a TLS certificate for one of the C2 servers. This certificate has been tied in the past in connection with malware families like [MoonBounce](https://thehackernews.com/2022/01/chinese-hackers-spotted-using-new-uefi.html) and [SideWalk](https://thehackernews.com/2021/08/new-sidewalk-backdoor-targets-us-based.html) (aka ScrambleCross).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgf_diGJ6k9VJ3Q6L9337dT9371ms9qb77DqkRPq2XdYlOlXjwLYfMvX8eh1UDu0ovBoZ4VMYTNZ6nshfISkEK6T_FHEpfwSWL8aw1d64Nc2ol4yJEAc1bz5w3i-z4hLFqiOetGXGsbPsIjFf2DIe4K9B_S69mpi5rzdnCZX1Y-RxDnft0096B71oljMudP/s790-rw-e365/pshish.jpg)

That said, it's currently not known if the reuse stems from a custom malware family shared across multiple China-aligned threat actors, such as SideWalk, or due to shared infrastructure provisioning across these groups.

The third cluster, UNK\_SparkyCarp, is characterized by credential phishing attacks that single out an unnamed Taiwanese semiconductor company using a bespoke adversary-in-the-middle ([AitM](https://blog.talosintelligence.com/state-of-the-art-phishing-mfa-bypass/)) kit. The campaign ...