---
title: Citrix NetScaler ADC and Gateway Devices Under Attack: CISA Urges Immediate Action
url: https://thehackernews.com/2023/07/citrix-netscaler-adc-and-gateway.html
source: The Hacker News
date: 2023-07-22
fetch_date: 2025-10-04T11:58:04.188848
---

# Citrix NetScaler ADC and Gateway Devices Under Attack: CISA Urges Immediate Action

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

# [Citrix NetScaler ADC and Gateway Devices Under Attack: CISA Urges Immediate Action](https://thehackernews.com/2023/07/citrix-netscaler-adc-and-gateway.html)

**Jul 21, 2023**Ravie LakshmananVulnerability / Cyber Threat

[![Citrix NetScaler ADC and Gateway](data:image/png;base64... "Citrix NetScaler ADC and Gateway")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikPrlcCUIsLSJZGgYPG7MsuGFFKrQdRzCCkx6CQaxLNUPhmM49VQthvGaY7J1eT1Kd2GoiY3Rj5gszQGvzZ7TxDPVD5IOxfRJrnqxJWee9kUET8eeLiMIGphtOuMZeInVCxrIMd3iltdDUf-jHoSxaL5GYSETGbEdU1U8XlV4cFMGVnS0jJ45TpLDsOXxo/s790-rw-e365/hacked.jpg)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) issued an advisory on Thursday warning that the newly disclosed critical security flaw in Citrix NetScaler Application Delivery Controller (ADC) and Gateway devices is being abused to drop web shells on vulnerable systems.

"In June 2023, threat actors exploited this vulnerability as a zero-day to drop a web shell on a critical infrastructure organization's non-production environment NetScaler ADC appliance," the agency [said](https://www.cisa.gov/news-events/alerts/2023/07/20/cisa-releases-cybersecurity-advisory-threat-actors-exploiting-citrix-cve-2023-3519).

"The web shell enabled the actors to perform discovery on the victim's active directory (AD) and collect and exfiltrate AD data. The actors attempted to move laterally to a domain controller but network segmentation controls for the appliance blocked movement."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The shortcoming in question is [CVE-2023-3519](https://thehackernews.com/2023/07/zero-day-attacks-exploited-critical.html) (CVSS score: 9.8), a code injection bug that could result in unauthenticated remote code execution. Citrix, earlier this week, released patches for the issue and warned of active in-the-wild exploitation.

Successful exploitation requires the appliance to be configured as a Gateway (VPN virtual server, ICA Proxy, CVPN, RDP Proxy) or authentication, authorization, and auditing (AAA) virtual server.

CISA did not disclose the name of the organization that was impacted by the incident. The threat actor or the country allegedly behind it is presently unknown.

In the incident analyzed by CISA, the web shell is said to have enabled the collection of NetScaler configuration files, NetScaler decryption keys, and AD information, after which the data was transmitted as a PNG image file ("medialogininit.png").

The adversary's subsequent attempts to laterally move across the network as well as run commands to identify accessible targets and verify outbound network connectivity were thwarted due to robust network segmentation practices, the agency noted, adding the actors also attempted to delete their artifacts to cover up the tracks.

[![Citrix NetScaler ADC and Gateway](data:image/png;base64... "Citrix NetScaler ADC and Gateway")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQ5F1eHkA5NaXY1Qd8WeQBgoYt5TSh8gVaK1IhaJIvBhHjWpQhw5mM4i4R5Ud9LxTSNAo-9TR_8D0wb07eTlzkflZRlWTNawuW8xpqRxF0SYauZqSnXjGeccXot8G_9F5hChrZJMS4plH1pjE4XogST44zRA7-ICZCvA5HKlDsahShbnSMdxmf3URpRTUT/s790-rw-e365/tips.jpg)

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Vulnerabilities in gateway products such as NetScaler ADC and NetScaler Gateway have become popular targets for threat actors looking to obtain privileged access to targeted networks. This makes it imperative that users move quickly to apply the latest fixes to secure against potential threats.

### Update

The Shadowserver Foundation [said](https://twitter.com/Shadowserver/status/1682355280317919233) it has found more than 15,000 Citrix Netscaler ADC and Gateway servers worldwide at risk of potential compromise, making them vulnerable to attacks exploiting the [critical remote code execution flaw](https://www.mandiant.com/resources/blog/citrix-zero-day-espionage). The largest number of unpatched appliances are located in the U.S., Germany, the U.K., and Australia.

"The vulnerability is a simple unauthenticated stack overflow," cybersecurity firm Bishop Fox [said](https://bishopfox.com/blog/citrix-adc-gateway-rce-cve-2023-3519), noting that exploitation is trivial. "This is made significantly worse by the fact that exploit mitigations do not protect the vulnerable function on some versions."

### CISA Discloses New TTPs and IoCs

On September 6, 2023, CISA shared details of additional TTPs and IoCs that it received from an unidentified victim and trusted third-parties, noting that the threat actors dropped a PHP web shell, gained root level access to the compromised system, and performed hands-on discovery against the Active Directory (AD).

“They queried the AD via ldapsearch for users, groups, and computers,” CISA [said](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-201a). “They collected the data in gzipped text files renamed 1.css and 2.css and placed the files in /netscaler/ns\_gui/vpn/ for exfiltration. After exfiltrating the files, the actors deleted them from the system as well as some access logs, error logs, and authentication logs.”

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
[**Share o...