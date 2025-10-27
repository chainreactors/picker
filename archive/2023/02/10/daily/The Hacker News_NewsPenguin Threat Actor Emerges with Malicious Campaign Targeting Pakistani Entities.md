---
title: NewsPenguin Threat Actor Emerges with Malicious Campaign Targeting Pakistani Entities
url: https://thehackernews.com/2023/02/newspenguin-threat-actor-emerges-with.html
source: The Hacker News
date: 2023-02-10
fetch_date: 2025-10-04T06:17:03.570702
---

# NewsPenguin Threat Actor Emerges with Malicious Campaign Targeting Pakistani Entities

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

# [NewsPenguin Threat Actor Emerges with Malicious Campaign Targeting Pakistani Entities](https://thehackernews.com/2023/02/newspenguin-threat-actor-emerges-with.html)

**Feb 09, 2023**Ravie LakshmananCyber Attack / Cyber Threat

[![NewsPenguin Threat Actor](data:image/png;base64... "NewsPenguin Threat Actor")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiOpviJY3F2-rGA1qv57BYnJTopWJpAuELWygbXvZ5VZJGjWcceM1bpsAiTK_XcbZ66ZGRuVl-2oGH6ZjCwRCyamf9o7bQpr9j13Vt36a3rvOKAQC3fvQNTJ297fB0Jd_Mqk8af6qzvPus_cPsldJo_l_phdplvSpbQj8jcrZ1TBXduykYeU41H4-i/s790-rw-e365/marine.png)

A previously unknown threat actor dubbed **NewsPenguin** has been linked to a phishing campaign targeting Pakistani entities by leveraging the upcoming international maritime expo as a lure.

"The attacker sent out targeted phishing emails with a weaponized document attached that purports to be an exhibitor manual for PIMEC-23," the BlackBerry Research and Intelligence Team [said](https://blogs.blackberry.com/en/2023/02/newspenguin-a-previously-unknown-threat-actor-targets-pakistan-with-advanced-espionage-tool).

**PIMEC**, short for Pakistan International Maritime Expo and Conference, is an [initiative](https://twitter.com/PIMEC2023) of the Pakistan Navy and is organized by the Ministry of Maritime Affairs with an aim to "jump start development in the maritime sector." It's scheduled to be held from February 10-12, 2023.

The Canadian cybersecurity company said the attacks are designed to target marine-related entities and the event's visitors by tricking the message recipients into opening the seemingly harmless Microsoft Word document.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Once the document is launched and macros are enabled, a method called [remote template injection](https://attack.mitre.org/techniques/T1221/) is employed to fetch the next-stage payload from an actor-controlled server that's configured to return the artifact only if the request is sent from an IP address located in Pakistan.

[![NewsPenguin](data:image/png;base64... "NewsPenguin")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbpcWIcB_XA8HGT4BDb-BeyZk7lUr2kI0283uMKRcK33Nh-st5O0UfZSNKMFVa5-8CKe4_kjRDCEoEMAtn_sdWSvjdCWmXaXVM3XqCv5HoI181V8PC-6j7EDoP06FH47a04WCMxHlMUvk-x8VPqExT0PDknQvab7nmyXN11wvoaJnwAvp6GfcCw5Q5/s790-rw-e365/expo.png)

BlackBerry said it found the server to be hosting two ZIP archive files sans any password protections, one of which includes a Windows executable (updates.exe) that functions as a covert spying tool capable of bypassing sandboxes and virtual machines.

Dmitry Bestuzhev, a threat researcher at BlackBerry, told The Hacker News that the backdoor has been written from scratch in a manner that's tailored to this campaign.

"The threat actor behind it made a special effort to fly under the radar by being undetected," Bestuzhev said. "For example, between each request, there is a five minute delay. That's to lessen the risk of being uncovered."

"The implant includes self-deletion commands in case of exposure or when the op is finalized. It also contains commands for data transfer, deleting other files, and executing/running other apps in the victim's system. It looks for files in the system, gathers information about them, and uploads them to the remote server if the files are interesting. It's designed to steal sensitive files on the victim's disk."

What's more, the contents of the binary are encrypted with the [XOR encryption](https://en.wikipedia.org/wiki/XOR_cipher) algorithm, where the XOR key is "penguin." The HTTP response containing the backdoor also comes with the name parameter in the [Content-Disposition response header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition) set to "getlatestnews."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The name NewsPenguin is a reference to the uncommon XOR key and the name parameter, with BlackBerry finding no tactical overlaps that connect the malware to any currently-known threat actor or group.

An analysis of the domain hosting the payloads shows that it has been registered since June 30, 2022, indicating some level of advance planning for the campaign while simultaneously taking steps to iterate its toolset.

"As the target is an event run by the Pakistan Navy, it implies that the threat actor is actively targeting government organizations, rather than this being a financially motivated attack," BlackBerry said.

"It appears that the goal of this campaign is to find and steal the most interesting files containing information about the theme of the conference, people's networking, and technologies presented there," Bestuzhev added.

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
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[encryption](https://thehackernews.com/search/label/encryption)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Indian Hackers](https://thehackernews.com/search/label/Indian%20Hackers)[Pakistani Hackers](https://thehackernews.com/search/label/Pakistani%20Hackers)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWind...