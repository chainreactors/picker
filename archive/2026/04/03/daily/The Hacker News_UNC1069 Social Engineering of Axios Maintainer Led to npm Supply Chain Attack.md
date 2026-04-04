---
title: UNC1069 Social Engineering of Axios Maintainer Led to npm Supply Chain Attack
url: https://thehackernews.com/2026/04/unc1069-social-engineering-of-axios.html
source: The Hacker News
date: 2026-04-03
fetch_date: 2026-04-04T04:17:50.272106
---

# UNC1069 Social Engineering of Axios Maintainer Led to npm Supply Chain Attack

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [UNC1069 Social Engineering of Axios Maintainer Led to npm Supply Chain Attack](https://thehackernews.com/2026/04/unc1069-social-engineering-of-axios.html)

**Ravie Lakshmanan**Apr 03, 2026Threat Intelligence / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzgZRu55MSbdanW8-1PyCciQIyWUcB9Dv4WhQQEELGJqahN5q7MyrDJKQ77e-9-fNetZJZiaJKERrgMWTGcQ-4TKhzhWE6veQp5w3wxhUnjq3NPMifbpdn1VLYpx5nngu4GsgPknNfAV8CNTGq_L_PBri4s3xz4hp8yt7OPin9Q-Kq_xcBNqzbgHx5SkrU/s1700-e365/supplychain.jpg)

The maintainer of the Axios npm package has confirmed that the supply chain compromise was the result of a highly-targeted social engineering campaign orchestrated by North Korean threat actors tracked as [UNC1069](https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html).

Maintainer **Jason Saayman** said the attackers tailored their social engineering efforts "specifically to me" by first approaching him under the guise of the founder of a legitimate, well-known company.

"They had cloned the company's founders' likeness as well as the company itself," Saayman [said](https://github.com/axios/axios/issues/10636) in a post-mortem of the incident. "They then invited me to a real Slack workspace. This workspace was branded to the company's CI and named in a plausible manner. The Slack [workspace] was thought out very well; they had channels where they were sharing LinkedIn posts."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

Subsequently, the threat actors are said to have scheduled a meeting with him on Microsoft Teams. Upon joining the fake call, he was presented with a fake error message that stated "something on my system was out of date." As soon as the update was triggered, the attack led to the deployment of a remote access trojan.

The access afforded by the trojan enabled the attackers to steal the npm account credentials necessary to publish two trojanized versions of the Axios npm package (1.14.1 and 0.30.4) containing an implant named WAVESHAPER.V2.

"Everything was extremely well coordinated, looked legit, and was done in a professional manner," Saayman added.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwmmgzjQKLb1gdwwdQxrSdHqmmOTIia1r5pqRLA2oadyg8bfg4SA25jqXYtTOvAj-Mk12bnCQBmiRs2B-Q4h0hL6F0KWCSRvgEp_8xUAZzYd9rt8tyMsbE9JwAPAQWBbCQ07PxUgSS6DGR3CbNOZwYZckVn56bMlxpfYN8Ub4aRqTRwcmgFZ8BBstRM_y0/s1700-e365/image.jpg) |
| Source: Kaspersky |

The attack chain described by the project maintainer shares [considerable overlaps](https://thehackernews.com/2026/02/north-korea-linked-unc1069-uses-ai.html) with tradecraft associated with UNC1069 and BlueNoroff. Details of the campaign were extensively documented by [Huntress](https://thehackernews.com/2025/06/bluenoroff-deepfake-zoom-scam-hits.html) and [Kaspersky](https://thehackernews.com/2025/10/researchers-expose-ghostcall-and.html) last year, with the latter tracking it under the moniker GhostCall.

In these attacks, users are displayed an error message seconds after joining the call, stating that their system is not functioning properly and instructing them to download a malicious Zoom or Teams SDK through a [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)-like pop-up message. Depending on the operating system of the victim, this action leads to the execution of an AppleScript (for macOS) or a PowerShell (for Windows) script.

One of the malicious payloads deployed as part of the attack chain is a Nim-based macOS backdoor (or a Go variant written for Windows) called CosmicDoor that delivers a comprehensive stealer suite dubbed SilentSiphon to capture credentials from web browsers and password managers, and secrets associated with GitHub, GitLab, Bitbucket, npm, Yarn, Python pip, RubyGems, Rust argo, and .NET NuGet.

"Historically, [...] these specific guys have gone after crypto founders, VCs, public people," security researcher Taylor Monahan said. "They [social engineer](https://fortune.com/2026/04/02/north-korea-dprk-zoom-phishing-social-engineering-attack-telegram/) them and take over their accounts and target the next round of people. This evolution to targeting [OSS maintainers] is a bit concerning in my opinion."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

As preventive steps, Saayman has outlined several changes, including resetting all devices and credentials, setting up immutable releases, adopting OIDC flow for publishing, and updating GitHub Actions to adopt best practices.

The findings demonstrate how open-source project maintainers are increasingly becoming the target of sophisticated attacks, effectively allowing threat actors to target downstream users at scale by publishing poisoned versions of highly popular packages.

With Axios attracting nearly 100 million weekly downloads and being used heavily across the JavaScript ecosystem, the blast radius of such a supply chain attack can be massive as it propagates swiftly through direct and transitive dependencies.

"A package as widely used as Axios being compromised shows how difficult it is to reason about exposure in a modern JavaScript environment," Socket's Ahmad Nassri [said](https://socket.dev/blog/hidden-blast-radius-of-the-axios-compromise#Why-the-Blast-Radius-Is-Larger-Than-It-Looks). "It is a property of how dependency resolution in the ecosystem works today."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_sh...