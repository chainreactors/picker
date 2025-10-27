---
title: Cross-Platform JavaScript Stealer Targets Crypto Wallets in New Lazarus Group Campaign
url: https://thehackernews.com/2025/02/cross-platform-javascript-stealer.html
source: The Hacker News
date: 2025-02-06
fetch_date: 2025-10-06T20:39:54.074747
---

# Cross-Platform JavaScript Stealer Targets Crypto Wallets in New Lazarus Group Campaign

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

# [Cross-Platform JavaScript Stealer Targets Crypto Wallets in New Lazarus Group Campaign](https://thehackernews.com/2025/02/cross-platform-javascript-stealer.html)

**Feb 05, 2025**Ravie LakshmananCryptocurrency / Data Breach

[![JavaScript Stealer Targets Crypto Wallets](data:image/png;base64... "JavaScript Stealer Targets Crypto Wallets")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhm7EasDvlqTK-eD-uHPE0emLNC3ddIxCu9PLyn5mJYOMiL5l-rJV_yfriFHBjflUBQKIONu9eeVBPO84k220rkTYgcYSSazV7JGZMXIGkIaWi6Cgo8VClKbeIlmomd9xQZ5MsbUS5IQ8jwvHL1Z8_socr31WJFqgAn7B2-cOWwI5k1BYReJKJmHESkd0Oj/s790-rw-e365/malware.png)

The North Korea-linked **Lazarus Group** has been linked to an active campaign that leverages fake LinkedIn job offers in the cryptocurrency and travel sectors to deliver malware capable of infecting Windows, macOS, and Linux operating systems.

According to cybersecurity company Bitdefender, the scam begins with a message sent on a professional social media network, enticing them with the promise of remote work, part-time flexibility, and good pay.

"Once the target expresses interest, the 'hiring process' unfolds, with the scammer requesting a CV or even a personal GitHub repository link," the Romanian firm [said](https://www.bitdefender.com/en-us/blog/labs/lazarus-group-targets-organizations-with-sophisticated-linkedin-recruiting-scam) in a report shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Although seemingly innocent, these requests can serve nefarious purposes, such as harvesting personal data or lending a veneer of legitimacy to the interaction."

Once the requested details are obtained, the attack moves to the next stage where the threat actor, under the guise of a recruiter, shares a link to a GitHub or Bitbucket repository containing a minimum viable product (MVP) version of a supposed decentralized exchange (DEX) project and instructs the victim to check it out and provide their feedback.

Present within the code is an obfuscated script that's configured to retrieve a next-stage payload from api.npoint[.]io, a cross-platform JavaScript information stealer that's capable of harvesting data from various cryptocurrency wallet extensions that may be installed on the victim's browser.

The stealer also doubles up as a loader to retrieve a Python-based backdoor responsible for monitoring clipboard content changes, maintaining persistent remote access, and dropping additional malware.

At this stage, it's worth noting that the tactics documented by Bitdefender exhibit overlaps with a known attack activity cluster dubbed [Contagious Interview](https://thehackernews.com/2024/12/north-korean-hackers-deploy-ottercookie.html) (aka DeceptiveDevelopment and DEV#POPPER), which is [designed](https://thehackernews.com/2023/11/north-korean-hackers-pose-as-job.html) to drop a JavaScript stealer called BeaverTail and a Python implant referred to as InvisibleFerret.

"The analyzed malware seems to fall within the Contagious Interview cluster," Bitdefender Labs told The Hacker News. "However, the infected JavaScript sample is different from other BeaverTail samples that were seen in the past. We have also observed other details in the infection chain that leads us to believe that the threat actors are continuously adapting and improving their tactics."

The malware deployed by means of the Python malware is a .NET binary that can download and start a TOR proxy server to communicate with a command-and-control (C2) server, exfiltrate basic system information, and deliver another payload that, in turn, can siphon sensitive data, log keystrokes, and launch a cryptocurrency miner.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimndsAfUC4znozD3U-ZYl0CE1ZTSgtubkRTaal-Qya83S2FDYX6tQeXEMkchxsxFOiTAGhHuF_rJ28FVMAxmyWEHX_dgg9q3Wts5n9BwcrOomJvOESITMrHFSp499jMLVYhvEBTcw0mA8jZSTlSK8SlVtqL1Ye-5bIZNGia52hJaxA9XGckZ_orKZN_VR6/s790-rw-e365/coins.png)

"The threat actors' infection chain is complex, containing malicious software written in multiple programming languages and using a variety of technologies, such as multi-layered Python scripts that recursively decode and execute themselves, a JavaScript stealer that first harvests browser data before pivoting to further payloads, and .NET-based stagers capable of disabling security tools, configuring a Tor proxy, and launching crypto miners," Bitdefender said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

There is evidence to suggest these efforts are quite widespread, going by reports shared on [LinkedIn](https://www.linkedin.com/posts/josh-johnston-a25a7b186_so-apparently-code-interview-scams-are-a-activity-7288359204862509057-z21C) and [Reddit](https://www.reddit.com/r/programming/comments/1i84akt/recruiter_tried_to_hack_me_full_story_on_comments/), with minor tweaks to the overall attack chain. In some cases, the candidates are asked to clone a Web3 repository and run it locally as part of an interview process, while in others they are instructed to fix intentionally introduced bugs in the code.

One of the Bitbucket repositories in question refers to a project named "[miketoken\_v2](https://bitbucket.org/sarostech/miketoken_v2)." It is no longer accessible on the code hosting platform. Bitdefender said the activity is part of the same campaign with the repository names and recruiter profiles shuffled.

The disclosure comes a day after SentinelOne [revealed](https://thehackernews.com/2025/02/north-korean-hackers-deploy-ferret.html) that the Contagious Interview campaign is being used to deliver another malware codenamed FlexibleFerret.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exc...