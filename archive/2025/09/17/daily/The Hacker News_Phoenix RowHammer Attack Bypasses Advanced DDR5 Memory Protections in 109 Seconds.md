---
title: Phoenix RowHammer Attack Bypasses Advanced DDR5 Memory Protections in 109 Seconds
url: https://thehackernews.com/2025/09/phoenix-rowhammer-attack-bypasses.html
source: The Hacker News
date: 2025-09-17
fetch_date: 2025-10-02T20:16:22.689741
---

# Phoenix RowHammer Attack Bypasses Advanced DDR5 Memory Protections in 109 Seconds

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

# [Phoenix RowHammer Attack Bypasses Advanced DDR5 Memory Protections in 109 Seconds](https://thehackernews.com/2025/09/phoenix-rowhammer-attack-bypasses.html)

**Sep 16, 2025**Ravie LakshmananHardware Security / Vulnerability

[![RowHammer Attack](data:image/png;base64... "RowHammer Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj07sYz1RKtxVQyVb_1oqROIVoV7rA96LewuBJ3LK4yFBHgPIqbTb89hfRr8Xh-j4FdXJdmhvhuaPMlGVniuV8jrYpgSucnr9V_gbZvlfqfCwZU6lYaNVQAxb3LIn487GAtQZuvEOQ9acvvicnfuda7WyV1XTtX2gr604OjJAYxEpn3-a8W7UQb5F1Si3K-/s790-rw-e365/dram.jpg)

A team of academics from [ETH Zürich](https://comsec.ethz.ch/research/dram/phoenix/) and [Google](https://security.googleblog.com/2025/09/supporting-rowhammer-research-to.html) has discovered a new variant of a [RowHammer attack](https://thehackernews.com/2025/07/gpuhammer-new-rowhammer-attack-variant.html) targeting Double Data Rate 5 (DDR5) memory chips from South Korean semiconductor vendor SK Hynix.

The RowHammer attack variant, codenamed **[Phoenix](https://github.com/comsec-group/phoenix)** ([CVE-2025-6202](https://www.cve.org/CVERecord?id=CVE-2025-6202), CVSS score: 7.1), is capable of bypassing sophisticated protection mechanisms put in place to resist the attack.

"We have proven that reliably triggering RowHammer bit flips on DDR5 devices from SK Hynix is possible on a larger scale," the Computer Security Group (COMSEC) at ETH Zürich said. "We also proved that on-die ECC does not stop RowHammer, and RowHammer end-to-end attacks are still possible with DDR5."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[RowHammer](https://thehackernews.com/2024/03/new-zenhammer-attack-bypasses-rowhammer.html) refers to a hardware vulnerability where repeated access of a row of memory in a DRAM chip can trigger bit flips in adjacent rows, resulting in data corruption. This can be subsequently weaponized by bad actors to gain unauthorized access to data, escalate privileges, or even cause a denial-of-service.

Although first demonstrated in 2014, future DRAM chips are more likely to be susceptible to [RowHammer attacks](https://arxiv.org/abs/2501.14328) as DRAM manufacturers depend on density scaling to increase DRAM capacity.

In a study published by ETH Zürich researchers in 2020, it was [found](https://ieeexplore.ieee.org/document/9138944/) that "newer DRAM chips are more vulnerable to RowHammer: as device feature size reduces, the number of activations needed to induce a RowHammer bit flip also reduces."

Further research into the subject has [demonstrated](https://dl.acm.org/doi/10.1145/3566097.3568350) that the vulnerability has several dimensions to it and that it's sensitive to several variables, including environmental conditions (temperature and voltage), process variation, stored data patterns, memory access patterns, and memory control policies.

Some of the primary mitigations for RowHammer attacks include Error Correction Code (ECC) and Target Row Refresh (TRR). However, these countermeasures have been proven to be ineffective against more sophisticated attacks like [TRRespass](https://thehackernews.com/2020/03/rowhammer-vulnerability-ddr4-dram.html), [SMASH](https://thehackernews.com/2021/04/new-javascript-exploit-can-now-carry.html), [Half-Double](https://thehackernews.com/2021/05/google-researchers-discover-new-variant.html), and [Blacksmith](https://thehackernews.com/2021/11/new-blacksmith-exploit-bypasses-current.html).

The latest findings from ETH Zürich and Google show that it's possible to bypass advanced TRR defenses on DDR5 memory, opening the door for what the researchers call the "first-ever RowHammer privilege escalation exploit on a standard, production-grade desktop system equipped with DDR5 memory."

In other words, the end result is a privilege escalation exploit that obtains root on a DDR5 system with default settings in as little as 109 seconds. Specifically, the attack takes advantage of the fact that mitigation does not sample certain refresh intervals to flip bits on all 15 DDR5 memory chips in the test pool that were produced between 2021 and 2024.

Potential exploitation scenarios involving these bit flips allow for targeting RSA-2048 keys of a co-located virtual machine to break SSH authentication, as well as using the sudo binary to escalate local privileges to the root user.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"As DRAM devices in the wild cannot be updated, they will remain vulnerable for many years," the researchers said. "We recommend increasing the refresh rate to 3x, which stopped Phoenix from triggering bit flips on our test systems."

The disclosure comes weeks after research teams from George Mason University and Georgia Institute of Technology detailed two different RowHammer attacks called [OneFlip](https://oneflipbackdoor.github.io) and [ECC.fail](https://ecc.fail), respectively.

While OneFlip revolves around triggering a single bit flip to alter Deep Neural Network ([DNN](https://en.wikipedia.org/wiki/Deep_learning)) model weights and activate unintended behavior, ECC.fail is described as the first end-to-end RowHammer attack that's effective against DDR4 server machines with ECC memory.

"Unlike their PC counterparts, servers have extra protections against memory data corruptions (e.g., RowHammer or cosmic ray bit flips), in the form of error correcting codes," the researchers said. "These can detect bit flips in memory, and even potentially correct them. ECC.fail bypasses these protections by carefully inducing RowHammer bit flips at certain memory locations."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
...