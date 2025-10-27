---
title: North Korea-linked Supply Chain Attack Targets Developers with 35 Malicious npm Packages
url: https://thehackernews.com/2025/06/north-korea-linked-supply-chain-attack.html
source: The Hacker News
date: 2025-06-26
fetch_date: 2025-10-06T22:56:01.987476
---

# North Korea-linked Supply Chain Attack Targets Developers with 35 Malicious npm Packages

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

# [North Korea-linked Supply Chain Attack Targets Developers with 35 Malicious npm Packages](https://thehackernews.com/2025/06/north-korea-linked-supply-chain-attack.html)

**Jun 25, 2025**Ravie LakshmananMalware / Open Source

[![NPM Supply Chain Attack](data:image/png;base64... "NPM Supply Chain Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgad7RITmYNALavN0pIhYVtIXUMEcvoQClnk3Zi2gP7Ot9JPI9SPMcOVaWI5M3UDkU1DEgsfi6GUFbjr-cSfMD5Z8jPlXlERCa9TidmOQxwo48NYsOU1iBfQAV111FNzWoTfM1rg0Cem7C6h7dt0I8zQFTsEhYqPxxJ7oYtuqEUwJFJJdUMVK6NwmD7CdAH/s790-rw-e365/npm-malware.jpg)

Cybersecurity researchers have uncovered a fresh batch of malicious npm packages linked to the ongoing [Contagious Interview](https://thehackernews.com/2024/10/n-korean-hackers-use-fake-interviews-to.html) operation originating from North Korea.

According to [Socket](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages), the ongoing supply chain attack involves 35 malicious packages that were uploaded from 24 npm accounts. These packages have been collectively downloaded over 4,000 times. The complete list of the JavaScript libraries is below -

* react-plaid-sdk
* sumsub-node-websdk
* vite-plugin-next-refresh
* vite-plugin-purify
* nextjs-insight
* vite-plugin-svgn
* node-loggers
* react-logs
* reactbootstraps
* framer-motion-ext
* serverlog-dispatch
* mongo-errorlog
* next-log-patcher
* vite-plugin-tools
* pixel-percent
* test-topdev-logger-v1
* test-topdev-logger-v3
* server-log-engine
* logbin-nodejs
* vite-loader-svg
* struct-logger
* flexible-loggers
* beautiful-plugins
* chalk-config
* jsonpacks
* jsonspecific
* jsonsecs
* util-buffers
* blur-plugins
* proc-watch
* node-orm-mongoose
* prior-config
* use-videos
* lucide-node, and
* router-parse

Of these, six continue to remain available for download from npm: react-plaid-sdk, sumsub-node-websdk, vite-plugin-next-refresh, vite-loader-svg, node-orm-mongoose, and router-parse.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Each of the identified npm packages contains a hex-encoded loader dubbed HexEval, which is designed to collect host information post installation and selectively deliver a follow-on payload that's responsible for delivering a known JavaScript stealer called [BeaverTail](https://thehackernews.com/2025/04/north-korean-hackers-deploy-beavertail.html).

BeaverTail, in turn, is configured to download and execute a Python backdoor called InvisibleFerret, enabling the threat actors to collect sensitive data and establish remote control of infected hosts.

"This nesting-doll structure helps the campaign evade basic static scanners and manual reviews," Socket researcher Kirill Boychenko said. "One npm alias also shipped a cross-platform keylogger package that captures every keystroke, showing the threat actors' readiness to tailor payloads for deeper surveillance when the target warrants it."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHciBMuO9tXU5LLpzHf7n5wOGnfAmAflKrPbSGwiawSSOn1c1FJRGlnbQ6PhmYUwkXu33xQOTDU4tDsCqeYnxc9PDTQDgkPjkSHui0akMMf7k16UzuOXVUZv4WNxZCUD69JasW6IeZtDd6JqR8vQquOtCx2fASwv_z_lDxBxgIKiHLHjVk9UTgZhiJjth1/s790-rw-e365/ad.png)

Contagious Interview, first [publicly documented](https://thehackernews.com/2025/06/us-seizes-774m-in-crypto-tied-to-north.html) by Palo Alto Networks Unit 42 in late 2023, is an [ongoing campaign](https://thehackernews.com/2025/04/lazarus-group-targets-job-seekers-with.html) undertaken by North Korean state-sponsored threat actors to obtain unauthorized access to developer systems with the goal of conducting cryptocurrency and data theft.

The cluster is also broadly tracked under the monikers CL-STA-0240, DeceptiveDevelopment, DEV#POPPER, Famous Chollima, Gwisin Gang, Tenacious Pungsan, UNC5342, and Void Dokkaebi.

Recent iterations of the campaign have also been observed taking advantage of the ClickFix social engineering tactic to deliver malware such as GolangGhost and PylangGhost. This sub-cluster of activity has been designated the name [ClickFake Interview](https://thehackernews.com/2025/06/bluenoroff-deepfake-zoom-scam-hits.html).

The latest findings from Socket point to a multi-pronged approach where Pyongyang threat actors are embracing various methods to trick prospective targets into installing malware under the pretext of an interview or a Zoom meeting.

The npm offshoot of Contagious Interview typically involves the attackers [posing](https://www.reddit.com/r/CryptoScams/comments/1k37az4/exposing_north_korean_scamming_tactics_and_some/) as [recruiters](https://www.reddit.com/r/programming/comments/1i84akt/recruiter_tried_to_hack_me_full_story_on_comments/) on LinkedIn, sending job seekers and developers coding assignments by sharing a link to a malicious project hosted on GitHub or Bitbucket that embeds the npm packages within them.

"They target software engineers who are actively job-hunting, exploiting the trust that job-seekers typically place in recruiters," Boychenko said. "Fake personas initiate contact, often with scripted outreach messages and convincing job descriptions."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The victims are then coaxed into cloning and running these projects outside containerized environments during the purported interview process.

"This malicious campaign highlights an evolving tradecraft in North Korean supply chain attacks, one that blends malware staging, OSINT-driven targeting, and social engineering to compromise developers through trusted ecosystems," Socket said.

"By embedding malware loaders like HexEval in open source packages and delivering them through fake job assignments, threat actors sidestep perimeter defenses and gain execution on the systems of targeted developers. The campaign's multi-stage structure, minimal on-registry footprint, and attempt to evade containerized environments ...