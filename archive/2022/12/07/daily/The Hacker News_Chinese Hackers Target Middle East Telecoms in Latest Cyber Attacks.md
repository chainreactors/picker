---
title: Chinese Hackers Target Middle East Telecoms in Latest Cyber Attacks
url: https://thehackernews.com/2022/12/chinese-hackers-target-middle-east.html
source: The Hacker News
date: 2022-12-07
fetch_date: 2025-10-04T00:49:47.052762
---

# Chinese Hackers Target Middle East Telecoms in Latest Cyber Attacks

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

# [Chinese Hackers Target Middle East Telecoms in Latest Cyber Attacks](https://thehackernews.com/2022/12/chinese-hackers-target-middle-east.html)

**Dec 06, 2022**Ravie LakshmananAdvanced Persistent Threat

[![Latest Cyber Attacks](data:image/png;base64... "Latest Cyber Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-qU9NKl3nAe5a5zI3DJ8Rxu1D1YqgePCv15VyLhI67WwsJKok5GF10g3-Dyn0eFD-U-nmBeVoyNvoB4O-s3fHHQUrhAspA4HocUne9buCCUzlYkY0NpqUgllZAd6zUpUnGAh2hFGO-GjA-vLzs0L8_5Ly-4ZpWwnG5rKQy4WM-jQgP2Z0tIjedC1X/s790-rw-e365/telecom.jpg)

A malicious campaign targeting the Middle East is likely linked to **BackdoorDiplomacy**, an advanced persistent threat (APT) group with ties to China.

The espionage activity, directed against a telecom company in the region, is said to have commenced on August 19, 2021 through the successful exploitation of [ProxyShell flaws](https://thehackernews.com/2021/08/hackers-actively-searching-for.html) in the Microsoft Exchange Server.

Initial compromise leveraged binaries vulnerable to side-loading techniques, followed by using a mix of legitimate and bespoke tools to conduct reconnaissance, harvest data, move laterally across the environment, and evade detection.

"File attributes of the malicious tools showed that the first tools deployed by the threat actors were the NPS proxy tool and IRAFAU backdoor," Bitdefender researchers Victor Vrabie and Adrian Schipor said in a [report](https://www.bitdefender.com/blog/labs/backdoor-diplomacy-wields-new-tools-in-fresh-middle-east-campaign) shared with The Hacker News.

"Starting in February 2022, the threat actors used another tool – [the] Quarian backdoor, along with many other scanners and proxy/tunneling tools."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

BackdoorDiplomacy was [first documented](https://thehackernews.com/2021/06/new-cyber-espionage-group-targeting.html) by ESET in June 2021, with the intrusions primarily aimed at diplomatic entities and telecommunication companies in Africa and the Middle East to deploy Quarian (aka Turian or Whitebird).

[![Latest Cyber Attacks](data:image/png;base64... "Latest Cyber Attacks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-rT1WrTqTUr6-tNAaa2bMsRz74Zng2B1zWX_GnHE2cc5x0ks-27yru1J0n7AkoXHG-xzXM_JtP7wCCVyQFygUCcbR8IjiGTSuKU6WwPYyYYO2gszje9tIUzla8X5JEQl4bfHo3JGAf1Te9dZhPZ9Dg45qe0gqlppG4lWKoJ6Is7Pp4OFtDjZgYyea/s790-rw-e365/hackers.png)

The espionage motives of the attack is evidenced by the use of keylogger and PowerShell scripts designed to gather email content. IRAFAU, which is the first malware component delivered after obtaining a foothold, is used to perform information discovery and lateral movement.

This is facilitated by downloading and uploading files from and to a command-and-control (C2) server, launching a remote shell, and executing arbitrary files.

The second backdoor used in the operation is an updated version of Quarian, which comes with a broader set of capabilities to control the compromised host.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Also put to use is a tool dubbed Impersoni-fake-ator that's embedded into legitimate utilities like [DebugView](https://learn.microsoft.com/en-us/sysinternals/downloads/debugview) and Putty and is engineered to capture system metadata and execute a decrypted payload received from the C2 server.

The intrusion is further characterized by the use of open source software such as [ToRat](https://github.com/lu4p/ToRat), a Golang remote administration tool, and [AsyncRAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.asyncrat), the latter of which is likely dropped via Quarian.

Bitdefender's attribution of the attack to BackdoorDiplomacy comes from overlaps in the C2 infrastructure identified as used by the group in prior campaigns.

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

[APT Hackers](https://thehackernews.com/search/label/APT%20Hackers)[Chinese Hackers](https://thehackernews.com/search/label/Chinese%20Hackers)[cyber attacks](https://thehackernews.com/search/label/cyber%20attacks)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Creden...