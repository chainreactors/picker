---
title: CosmicBeetle Deploys Custom ScRansom Ransomware, Partnering with RansomHub
url: https://thehackernews.com/2024/09/cosmicbeetle-deploys-custom-scransom.html
source: The Hacker News
date: 2024-09-11
fetch_date: 2025-10-06T18:30:09.333286
---

# CosmicBeetle Deploys Custom ScRansom Ransomware, Partnering with RansomHub

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

# [CosmicBeetle Deploys Custom ScRansom Ransomware, Partnering with RansomHub](https://thehackernews.com/2024/09/cosmicbeetle-deploys-custom-scransom.html)

**Sep 10, 2024**Ravie LakshmananMalware / Threat Intelligence

[![ScRansom Ransomware](data:image/png;base64... "ScRansom Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZ8L1EwjviCeO8ZoqVEg3-n4bQEFjKLve-Y-EUiCXj2Xr6b_8brhdtDGcdGwNzoS2DnFEmWcWxJjjaXsmE2NcTIvcxfJD4Jra7tv1SpLZgq0FboIaQYnDs82MJ70DMHkhNmTTDCbO8Cbky-4CEjfBMDr_wxp6wlu_Aap9BLsF26VrKS8Hy9mqB4WPaNfM1/s790-rw-e365/ransomware.png)

The threat actor known as CosmicBeetle has debuted a new custom ransomware strain called ScRansom in attacks targeting small- and medium-sized businesses (SMBs) in Europe, Asia, Africa, and South America, while also likely working as an affiliate for [RansomHub](https://thehackernews.com/2024/09/ransomhub-ransomware-group-targets-210.html).

"CosmicBeetle replaced its previously deployed ransomware, Scarab, with ScRansom, which is continually improved," ESET researcher Jakub Souček [said](https://www.welivesecurity.com/en/eset-research/cosmicbeetle-steps-up-probation-period-ransomhub/) in a new analysis published today. "While not being top notch, the threat actor is able to compromise interesting targets."

Targets of ScRansom attacks span manufacturing, pharmaceuticals, legal, education, healthcare, technology, hospitality, leisure, financial services, and regional government sectors.

CosmicBeetle is best known for a malicious toolset called [Spacecolon](https://thehackernews.com/2023/08/spacecolon-toolset-fuels-global-surge.html) that was previously identified as used for delivering the Scarab ransomware across victim organizations globally.

Also known as NONAME, the adversary has a track record of experimenting with the [leaked LockBit builder](https://thehackernews.com/2023/08/lockbit-30-ransomware-builder-leak.html) in an attempt to pass off as the infamous ransomware gang in its ransom notes and leak site as far back as November 2023.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's currently not clear who is behind the attack or where they are from, although an earlier hypothesis implied that they could be of Turkish origin due to the presence of a custom encryption scheme used in another tool named ScHackTool. ESET, however, suspects the attribution to no longer hold water.

"ScHackTool's encryption scheme is used in the legitimate [Disk Monitor Gadget](https://vovsoft.com/software/disk-monitor-gadget/)," Souček pointed out. "It is likely that this algorithm was adapted [from a [Stack Overflow thread](https://stackoverflow.com/questions/6798188/delphi-simple-string-encryption)] by VOVSOFT [the Turkish software firm behind the tool] and, years later, CosmicBeetle stumbled upon it and used it for ScHackTool."

Attack chains have been observed taking advantage of brute-force attacks and known security flaws ([CVE-2017-0144](https://nvd.nist.gov/vuln/detail/cve-2017-0144), [CVE-2020-1472](https://nvd.nist.gov/vuln/detail/cve-2020-1472), [CVE-2021-42278](https://nvd.nist.gov/vuln/detail/cve-2021-42278), [CVE-2021-42287](https://nvd.nist.gov/vuln/detail/CVE-2021-42287), [CVE-2022-42475](https://nvd.nist.gov/vuln/detail/CVE-2022-42475), and [CVE-2023-27532](https://nvd.nist.gov/vuln/detail/cve-2023-27532)) to infiltrate target environments.

The intrusions further involve the use of various tools like [Reaper](https://github.com/MrEmpy/Reaper), [Darkside](https://github.com/ph4nt0mbyt3/Darkside), and [RealBlindingEDR](https://github.com/myzxcg/RealBlindingEDR) to terminate security-related processes to sidestep detection prior to deploying the Delphi-based ScRansom ransomware, which comes with support for partial encryption to speed up the process and an "ERASE" mode to render the files unrecoverable by overwriting them with a constant value.

[![ScRansom Ransomware](data:image/png;base64... "ScRansom Ransomware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4-apqijChu5jBe-2Atvv7Q9yoQhZjLhxp8KA5IXe9neHgz64RdHYK-1r501tfZ5qnspEGnWrmf6Tl4PPoQyF2LVS0FLhxfwOGbUSBXOpmpeGX5Gl3AOTDGfRoXW1F6GhhTY4YkPrkX_mNCrGIBrDL3kuj3FTz_CGVQpI3Zwg4plOPPsay9r9gVfe6zH7v/s790-rw-e365/figure-6.png)

The connection to RansomHub stems from the fact that the Slovak cybersecurity company spotted the deployment of ScRansom and RansomHub payloads on the same machine within a week's time.

"Probably due to the obstacles that writing custom ransomware from scratch brings, CosmicBeetle attempted to leech off LockBit's reputation, possibly to mask the issues in the underlying ransomware and in turn to increase the chance that victims will pay," Souček said.

## Cicada3301 Unleashes Updated Version

The disclosure comes as threat actors linked to the [Cicada3301 ransomware](https://thehackernews.com/2024/09/new-rust-based-ransomware-cicada3301.html) (aka Repellent Scorpius) have been observed using an updated version of the encryptor since July 2024.

"Threat authors added a new command-line argument, --no-note," Palo Alto Networks Unit 42 [said](https://unit42.paloaltonetworks.com/repellent-scorpius-cicada3301-ransomware) in a report shared with The Hacker News. "When this argument is invoked, the encryptor will not write the ransom note to the system."

Another important modification is the absence of hard-coded usernames or passwords in the binary, although it still retains the capability to execute PsExec using these credentials if they exist, a technique highlighted recently by Morphisec.

In an interesting twist, the cybersecurity vendor said it observed signs that the group has data obtained from older compromise incidents that predate the group's operation under the Cicada3301 brand.

This has raised the possibility that the threat actor may have operated under a different ransomware brand, or purchased the data from other ransomware groups. That having said, Unit 42 noted it identified some overlaps with [another attack](...