---
title: UNC2891 Breaches ATM Network via 4G Raspberry Pi, Tries CAKETAP Rootkit for Fraud
url: https://thehackernews.com/2025/07/unc2891-breaches-atm-network-via-4g.html
source: The Hacker News
date: 2025-08-01
fetch_date: 2025-10-07T00:49:38.477055
---

# UNC2891 Breaches ATM Network via 4G Raspberry Pi, Tries CAKETAP Rootkit for Fraud

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

# [UNC2891 Breaches ATM Network via 4G Raspberry Pi, Tries CAKETAP Rootkit for Fraud](https://thehackernews.com/2025/07/unc2891-breaches-atm-network-via-4g.html)

**Jul 31, 2025**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyKsRdqJgv59iu-VjJpzBfUpk8502lforNDu1eceFjOEA1gmr6Ryx97qAvg1u__gsuWSnTO5B2Y_E5TPuvpcjszt3mJVGj0jaZNuJv7mXTwl7gbNxoV__t1ym4CSN0jmqmNj3uJf_G3dosBIijWlMrfpEWZ9w2-tYTsiefjx_s8R6ZLUgntvMZQY676h53/s790-rw-e365/atm-hacking.jpg)

The financially motivated threat actor known as **UNC2891** has been observed targeting Automatic Teller Machine (ATM) infrastructure using a 4G-equipped Raspberry Pi as part of a covert attack.

The cyber-physical attack involved the adversary leveraging their physical access to install the Raspberry Pi device and have it connected directly to the same network switch as the ATM, effectively placing it within the target bank's network, Group-IB said. It's currently not known how this access was obtained.

"The Raspberry Pi was equipped with a 4G modem, allowing remote access over mobile data," security researcher Nam Le Phuong [said](https://www.group-ib.com/blog/unc2891-bank-heist/) in a Wednesday report.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Using the TINYSHELL backdoor, the attacker established an outbound command-and-control (C2) channel via a Dynamic DNS domain. This setup enabled continuous external access to the ATM network, completely bypassing perimeter firewalls and traditional network defenses."

UNC2891 was [first documented](https://thehackernews.com/2022/03/hackers-target-bank-networks-with-new.html) by Google-owned Mandiant in March 2022, linking the group to attacks targeting ATM switching networks to carry out unauthorized cash withdrawals at different banks using fraudulent cards.

Central to the operation was a kernel module rootkit dubbed CAKETAP that's designed to hide network connections, processes, and files, as well as intercept and spoof card and PIN verification messages from hardware security modules (HSMs) to enable financial fraud.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFCvDBX-nKCMuV3VqWt3fPDuUwspTsQ1TCA9t_TaNLXlkohVI9hWRLXnRvHrPBaIi4PVAmxR0oLC1ZfrMcLmgF173Qv30B1lwgoonb6l_7KFi1gW_DXQO7gbKozpzKKBwOVpgvktADbwfZdROId-cwUshyphenhyphenTG3harQ47ErduxTWQ1BC8l5ow8CiwezSp9Sb/s2600/tinyshell.jpg)

The hacking crew is assessed to share tactical overlaps with another threat actor called [UNC1945](https://thehackernews.com/2021/10/lightbasin-hackers-breach-at-least-13.html) (aka LightBasin), which was previously identified compromising managed service providers and striking targets within the financial and professional consulting industries.

Describing the threat actor as possessing extensive knowledge of Linux and Unix-based systems, Group-IB said its analysis uncovered backdoors named "lightdm" on the victim's network monitoring server that are designed to establish active connections to the Raspberry Pi and the internal Mail Server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The attack is significant for the abuse of [bind mounts](https://attack.mitre.org/techniques/T1564/013/) to [hide the presence](https://www.group-ib.com/blog/linux-pro-manipulation/) of the backdoor from process listings and evade detection.

The end goal of the infection, as seen in the past, is to deploy the CAKETAP rootkit on the ATM switching server and facilitate fraudulent ATM cash withdrawals. However, the Singaporean company said the campaign was disrupted before the threat actor could inflict any serious damage.

"Even after the Raspberry Pi was discovered and removed, the attacker maintained internal access through a backdoor on the mail server," Group-IB said. "The threat actor leveraged a Dynamic DNS domain for command-and-control."

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

[ATM security](https://thehackernews.com/search/label/ATM%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Financial Fraud](https://thehackernews.com/search/label/Financial%20Fraud)[Group-IB](https://thehackernews.com/search/label/Group-IB)[linux](https://thehackernews.com/search/label/linux)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Raspberry Pi](https://thehackernews.com/search/label/Raspberry%20Pi)[rootkit](https://thehackernews.com/search/label/rootkit)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to...