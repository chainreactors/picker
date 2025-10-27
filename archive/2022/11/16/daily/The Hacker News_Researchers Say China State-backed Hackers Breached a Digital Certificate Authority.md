---
title: Researchers Say China State-backed Hackers Breached a Digital Certificate Authority
url: https://thehackernews.com/2022/11/researchers-say-china-state-backed.html
source: The Hacker News
date: 2022-11-16
fetch_date: 2025-10-03T22:56:05.559014
---

# Researchers Say China State-backed Hackers Breached a Digital Certificate Authority

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

# [Researchers Say China State-backed Hackers Breached a Digital Certificate Authority](https://thehackernews.com/2022/11/researchers-say-china-state-backed.html)

**Nov 15, 2022**Ravie Lakshmanan

[![Digital Certificate Authority](data:image/png;base64... "Digital Certificate Authority")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilqUno8MchRSb5k6XaOn7SrN1IT3QrKBEn5MuvUwxXd37eWaxmxG9N9wOso133k9oURQbTPW2mPkGoTh4PHX1finIJDmJh7SjTZIXBcqVinFJeioZylQBMA3VNe_oA128FOf5KSbKQbaj7D12lkt1UGIAZQzeKWcWiVH_w_b7cD31q4gxqJWzL66XJ/s790-rw-e365/cert.jpg)

A suspected Chinese state-sponsored actor breached a digital certificate authority as well as government and defense agencies located in different countries in Asia as part of an ongoing campaign since at least March 2022.

Symantec, by Broadcom Software, linked the attacks to an adversarial group it tracks under the name **Billbug**, citing the use of tools previously attributed to this actor. The activity appears to be driven by espionage and data-theft, although no data is said to have been stolen to date.

[Billbug](https://malpedia.caad.fkie.fraunhofer.de/actor/lotus_panda), also called Bronze Elgin, Lotus Blossom, Lotus Panda, [Spring Dragon](https://securelist.com/spring-dragon-updated-activity/79067/), and [Thrip](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/thrip-hits-satellite-telecoms-defense-targets), is an advanced persistent threat (APT) group that is believed to operate on behalf of Chinese interests. Primary targets include government and military organizations in South East Asia.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Attacks mounted by the adversary in 2019 involved the use of backdoors like [Hannotog and Sagerunex](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/thrip-apt-south-east-asia), with the intrusions observed in Hong Kong, Macau, Indonesia, Malaysia, the Philippines, and Vietnam.

Both the implants are designed to grant persistent remote access to the victim network, even as the threat actor is known to deploy an information-stealer known as Catchamas in select cases to exfiltrate sensitive information.

"The targeting of a certificate authority is notable, as if the attackers were able to successfully compromise it to access certificates they could potentially use them to sign malware with a valid certificate, and help it avoid detection on victim machines," Symantec researchers [said](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/espionage-asia-governments-cert-authority) in a report shared with The Hacker News.

"It could also potentially use compromised certificates to intercept HTTPS traffic."

The cybersecurity company, however, noted that there is no evidence to indicate that Billbug was successful in compromising the digital certificates. The concerned authority, it said, was notified of the activity.

An analysis of the latest wave of attacks indicates that initial access is likely obtained through the exploitation of internet-facing applications, following which a combination of bespoke and living-off-the-land tools are employed to meet its operational goals.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This comprises utilities such as WinRAR, Ping, Traceroute, NBTscan, Certutil, in addition to a backdoor capable of downloading arbitrary files, gathering system information, and uploading encrypted data.

Also detected in the attacks were an open source multi-hop proxy tool called [Stowaway](https://github.com/ph4ntonn/Stowaway/blob/master/README_EN.md) and the Sagerunex malware, which is dropped on the machine via Hannotog. The backdoor, for its part, is equipped to run arbitrary commands, drop additional payloads, and siphon files of interest.

"The ability of this actor to compromise multiple victims at once indicates that this threat group remains a skilled and well-resourced operator that is capable of carrying out sustained and wide-ranging campaigns," the researchers concluded.

"Billbug also appears to be undeterred by the possibility of having this activity attributed to it, with it reusing tools that have been linked to the group in the past."

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

[Chinese Hackers](https://thehackernews.com/search/label/Chinese%20Hackers)[hacking news](https://thehackernews.com/search/label/hacking%20news)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Gl...