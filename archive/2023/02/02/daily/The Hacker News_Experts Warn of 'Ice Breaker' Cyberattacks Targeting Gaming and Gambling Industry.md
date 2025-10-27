---
title: Experts Warn of 'Ice Breaker' Cyberattacks Targeting Gaming and Gambling Industry
url: https://thehackernews.com/2023/02/experts-warn-of-ice-breaker.html
source: The Hacker News
date: 2023-02-02
fetch_date: 2025-10-04T05:32:04.385064
---

# Experts Warn of 'Ice Breaker' Cyberattacks Targeting Gaming and Gambling Industry

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

# [Experts Warn of 'Ice Breaker' Cyberattacks Targeting Gaming and Gambling Industry](https://thehackernews.com/2023/02/experts-warn-of-ice-breaker.html)

**Feb 01, 2023**Ravie LakshmananGaming / Cyber Attack

[![Gaming and Gambling Industry](data:image/png;base64... "Gaming and Gambling Industry")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSylnLrjflS9NoFBBVs2U5BvsPkYIqO8eut6b1r9F4aKXi2oLGcRzgB1JLqcWghdMHP72qiHPSYxNuJUAg60z9sdweIApqzo9rkUTUFsDLBBE-doukXlPwfZB960tk3pQfvHodeUw1jcK6Aks20ey5-Bodi15JPVL-hVyk-N-QaRa8XIsGTJq5zeBR/s790-rw-e365/gaming.png)

A new attack campaign has been targeting the gaming and gambling sectors since at least September 2022, just as the [ICE London 2023](https://www.icelondon.uk.com/) gaming industry trade fair event is scheduled to kick off next week.

Israeli cybersecurity company **Security Joes** is tracking the activity cluster under the name **Ice Breaker**, stating the intrusions employ clever social engineering tactics to deploy a JavaScript backdoor.

The attack sequence proceeds as follows: The threat actor poses as a customer while initiating a conversation with a support agent of a gaming company under the pretext of having account registration issues. The adversary then urges the individual on the other end to open a screenshot image hosted on Dropbox.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Security Joes [said](https://www.securityjoes.com/post/operation-ice-breaker-targets-the-gam-bl-ing-industry-right-before-it-s-biggest-gathering) that the threat actor is "well-aware of the fact that the customer service is human-operated."

Clicking the purported screenshot link sent in the chat leads to the retrieval of an LNK payload or, alternatively, a VBScript file as a backup option, the former of which is configured to download and run an MSI package containing a Node.js implant.

The JavaScript file has all the features of a typical backdoor, enabling the threat actor to enumerate running processes, steal passwords and cookies, exfiltrate arbitrary files, take screenshots, run VBScript imported from a remote server, and even open a reverse proxy on the compromised host.

[![Gaming and Gambling Industry](data:image/png;base64... "Gaming and Gambling Industry")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO5k3C38EMTi1iD69XY_nTnKpOHoeW9NSR6sxtKBxnU8KAZKtr_dv5bug4Yyg1uY8mtMBbWaiWePFgMRUkkw4IES8o4bKaojEPcxR8iIJCk0L4iRh4P2eDFXwJWfm89K3iUb8v1DeS1RGv2_S7n8-Wb3u_oougV46RmoJtecTHvSAP3GksZlPdbKSM/s790-rw-e365/hacking.png)

Should the VBS downloader be executed by the victim, the infection culminates in the deployment of [Houdini](https://malpedia.caad.fkie.fraunhofer.de/details/win.houdini), a VBS-based remote access trojan that dates back to 2013.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The threat actors' origins are currently unknown, although they have been observed using broken English during their conversations with customer service agents. Some indicators of compromise (IoCs) associated with the campaign were [previously shared](https://twitter.com/malwrhunterteam/status/1576984214351724546) by the MalwareHunterTeam in October 2022.

"This is a highly effective attack vector for the gaming and gambling industry," Felipe Duarte, senior threat researcher at Security Joes, said.

"The never-seen-before compiled JavaScript second stage malware is highly complex to dissect, showing that we are dealing with a skilled threat actor with the potential of being sponsored by an interest owner."

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

[JavaScript](https://thehackernews.com/search/label/JavaScript)[Malware](https://thehackernews.com/search/label/Malware)[Malware Hunter](https://thehackernews.com/search/label/Malware%20Hunter)[VBScript](https://thehackernews.com/search/label/VBScript)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and A...