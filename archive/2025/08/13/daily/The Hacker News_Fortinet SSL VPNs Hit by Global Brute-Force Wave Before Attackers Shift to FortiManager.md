---
title: Fortinet SSL VPNs Hit by Global Brute-Force Wave Before Attackers Shift to FortiManager
url: https://thehackernews.com/2025/08/fortinet-ssl-vpns-hit-by-global-brute.html
source: The Hacker News
date: 2025-08-13
fetch_date: 2025-10-07T00:53:14.691705
---

# Fortinet SSL VPNs Hit by Global Brute-Force Wave Before Attackers Shift to FortiManager

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

# [Fortinet SSL VPNs Hit by Global Brute-Force Wave Before Attackers Shift to FortiManager](https://thehackernews.com/2025/08/fortinet-ssl-vpns-hit-by-global-brute.html)

**Aug 12, 2025**Ravie LakshmananThreat Intelligence / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrEMbHTYM3BGdWTNDNB1t2ExuWZ2wkRWViLkCW4V3tG9hDbMQ81Z0g-Sp_8WzaZi5-s3wL7V7A8vDxIh6-Qsedy8STadCsneZ3CvyZ3hGNLknHxiYpqnCZNtOPi00j27y2bxN_auhKvOS17YcBk4Dp_iT8k5qq_sbCXLBG3XDhxucgsgdVFD0zjYnxxI_e/s790-rw-e365/map.jpg)

Cybersecurity researchers are warning of a "significant spike" in brute-force traffic aimed at Fortinet SSL VPN devices.

The coordinated activity, per threat intelligence firm GreyNoise, was [observed](https://viz.greynoise.io/tags/fortinet-ssl-vpn-bruteforcer?days=90) on August 3, 2025, with over 780 unique IP addresses participating in the effort.

As many as 56 unique IP addresses have been detected over the past 24 hours. All the IP addresses have been [classified](https://viz.greynoise.io/query/tags%3A%22Fortinet%20SSL%20VPN%20Bruteforcer%22%20last_seen%3A1d) as malicious, with the IPs originating from the United States, Canada, Russia, and the Netherlands. Targets of the brute-force activity include the United States, Hong Kong, Brazil, Spain, and Japan.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Critically, the observed traffic was also targeting our FortiOS profile, suggesting deliberate and precise targeting of Fortinet's SSL VPNs," GreyNoise [said](https://www.greynoise.io/blog/vulnerability-fortinet-vpn-bruteforce-spike). "This was not opportunistic -- it was focused activity."

The company also pointed out that it identified two distinct assault waves spotted before and after August 5: One, a long-running, brute-force activity tied to a single TCP signature that remained relatively steady over time, and Two, which involved a sudden and concentrated burst of traffic with a different TCP signature.

"While the August 3 traffic has targeted the FortiOS profile, traffic fingerprinted with TCP and client signatures – a meta signature – from August 5 onward was not hitting FortiOS," the company noted. "Instead, it was consistently targeting our FortiManager."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPnAsFA2tqevfbNPjKEE5hh1BMzyDLh7k5fn7bG8wgl-tIE2YP9jwm_br6qjI_Ewr0p6JhJk_HoMEEb1ryvyk5KNuL40WQDTm46m7T3fcrEmUh1otXlYtz2-LRLJc3hDLeazTTONkYKOvDc7Uzqqrd7FKXt63PgEkwhR3C-CmO_fzk554wkl3emIyFuxm1/s790-rw-e365/ddos.png)

"This indicated a shift in attacker behavior – potentially the same infrastructure or toolset pivoting to a new Fortinet-facing service."

On top of that, a deeper examination of the historical data associated with the post-August 5 TCP fingerprint has uncovered an earlier spike in June featuring a unique client signature that resolved to a FortiGate device in a residential ISP block managed by Pilot Fiber Inc.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This has raised the possibility that the brute-force tooling was either initially tested or launched from a home network. An alternative hypothesis is the use of a residential proxy.

The development comes against the backdrop of findings that spikes in malicious activity are often followed by the disclosure of a new CVE affecting the same technology within six weeks.

"These patterns were exclusive to enterprise edge technologies like VPNs, firewalls, and remote access tools – the same kinds of systems increasingly targeted by advanced threat actors," the company [noted](https://www.greynoise.io/blog/greynoise-uncovers-early-warning-signals-emerging-vulnerabilities) in its Early Warning Signals report published late last month.

The Hacker News has reached out to Fortinet for further comment, and we will update if we hear back.

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

[Brute-force Attack](https://thehackernews.com/search/label/Brute-force%20Attack)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[Fortigate](https://thehackernews.com/search/label/Fortigate)[FortiManager](https://thehackernews.com/search/label/FortiManager)[Fortinet](https://thehackernews.com/search/label/Fortinet)[GreyNoise](https://thehackernews.com/search/label/GreyNoise)[network security](https://thehackernews.com/search/label/network%20security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense...