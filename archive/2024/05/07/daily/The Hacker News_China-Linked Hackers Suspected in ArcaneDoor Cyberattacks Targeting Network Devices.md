---
title: China-Linked Hackers Suspected in ArcaneDoor Cyberattacks Targeting Network Devices
url: https://thehackernews.com/2024/05/china-linked-hackers-suspected-in.html
source: The Hacker News
date: 2024-05-07
fetch_date: 2025-10-06T17:19:53.680379
---

# China-Linked Hackers Suspected in ArcaneDoor Cyberattacks Targeting Network Devices

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

# [China-Linked Hackers Suspected in ArcaneDoor Cyberattacks Targeting Network Devices](https://thehackernews.com/2024/05/china-linked-hackers-suspected-in.html)

**May 06, 2024**Ravie LakshmananNetwork Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggY88ZniZn8np0C1A7hbQ0uyCFhBWfiAYxjxtGfo0UI8kM2tPvE7Sd5apIWlxJgixBKwB4wqWaqtcVCFEX_MLMST-kZoLk7NYAcanq-YBpJXiwWDfVb_SWYksNnak0WeJrQGSE6b5dL-KAP4DaNQP6OzUCERJ9N2vA5KUXY_PPu5H5nviQOsqF3PlmDN-s/s790-rw-e365/chinese.jpg)

The recently uncovered cyber espionage campaign targeting perimeter network devices from several vendors, including Cisco, may have been the work of China-linked actors, according to [new findings](https://censys.com/analysis-of-arcanedoor-threat-infrastructure-suggests-potential-ties-to-chinese-based-actor/) from attack surface management firm Censys.

Dubbed [ArcaneDoor](https://thehackernews.com/2024/04/state-sponsored-hackers-exploit-two.html), the activity is said to have commenced around July 2023, with the first confirmed attack against an unnamed victim detected in early January 2024.

The targeted attacks, orchestrated by a previously undocumented and suspected sophisticated state-sponsored actor tracked as [UAT4356](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/) (aka Storm-1849), entailed the deployment of two custom malware dubbed Line Runner and Line Dancer.

The initial access pathway used to facilitate the intrusions has yet to be discovered, although the adversary has been observed leveraging two now-patched flaws in Cisco Adaptive Security Appliances ([CVE-2024-20353](https://nvd.nist.gov/vuln/detail/CVE-2024-20353) and [CVE-2024-20359](https://nvd.nist.gov/vuln/detail/CVE-2024-20359)) to persist Line Runner.

Telemetry data gathered as part of the investigation has revealed the threat actor's interest in Microsoft Exchange servers and network devices from other vendors, Talos said last month.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Censys, which further examined the actor-controlled IP addresses, said the attacks point to the potential involvement of a threat actor based in China.

This is based on the fact that four of the five online hosts presenting the [SSL certificate](https://www.digicert.com/what-is-an-ssl-certificate) identified as connected to the attackers' infrastructure are associated with Tencent and ChinaNet autonomous systems ([AS](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)).

In addition, among the [threat actor-managed IP addresses](https://search.censys.io/search/report?resource=hosts&q=ip%3A%7B192.36.57.181%2C+185.167.60.85%2C+185.227.111.17%2C+176.31.18.153%2C++172.105.90.154%2C+185.244.210.120%2C+45.86.163.224%2C+172.105.94.93%2C+213.156.138.77%2C+++89.44.198.189%2C+45.77.52.253%2C+103.114.200.230%2C+212.193.2.48%2C+51.15.145.37%2C+89.44.198.196%2C+131.196.252.148%2C+213.156.138.78%2C+121.227.168.69%2C+213.156.138.68%2C++194.4.49.6%2C+185.244.210.65%2C+216.238.75.155%7D&virtual_hosts=EXCLUDE&field=services.tls.certificates.leaf_data.issuer.common_name&num_buckets=50) is a Paris-based host ([212.193.2[.]48](https://search.censys.io/hosts/212.193.2.48)) with the subject and issuer set as "Gozargah," which is likely a reference to a GitHub account that hosts an anti-censorship tool named [Marzban](https://github.com/Gozargah/Marzban).

The software, in turn, is "powered" by another open-source project dubbed Xray that has a [website](https://xtls.github.io/) written in Chinese.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4QmBttjXtaHIUy-NSF68xJm9il-P2d8RPuVmTfY6D08kNPE8_aDYsU9kRx0-uxHyjqcZ0kBmNw6qBnNpw8OGRAOgohSFhjNlvpszdKWY_KZSt4kLH6P5dpvgr7SgJmMlo7KZTZtWWK7snBqReVAR2_wAY3PQDVODlI02EULSzZ0ea6AHs8vpmn9NC2Rg2/s790-rw-e365/ip.jpg)

This implies that "some of these hosts were running services associated with anti-censorship software likely intended to circumvent [The Great Firewall](https://thehackernews.com/2024/04/china-linked-muddling-meerkat-hijacks.html)," and that "a significant number of these hosts are based in prominent Chinese networks," suggesting that ArcaneDoor could be the work of a Chinese actor, Censys theorized.

Nation-state actors affiliated with China have [increasingly targeted edge appliances](https://thehackernews.com/2024/04/zero-day-alert-critical-palo-alto.html) in recent years, leveraging zero-day flaws in Barracuda Networks, Fortinet, Ivanti, and VMware to infiltrate targets of interest and deploy malware for persistent covert access.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as French cybersecurity firm Sekoia said it successfully sinkholed a command-and-control (C2) server linked to the PlugX trojan in September 2023 by spending $7 to acquire the IP address tied to a [variant of the malware](https://thehackernews.com/2023/01/researchers-discover-new-plugx-malware.html) with capabilities to propagate in a worm-like fashion via [compromised flash drives](https://thehackernews.com/2023/03/new-naplistener-malware-used-by-ref2924.html).

A closer monitoring of the sinkholed IP address (45.142.166[.]112) has revealed the worm's presence in more than 170 countries spanning 2.49 million unique IP addresses over a six-month period. A majority of the infections have been detected in Nigeria, India, China, Iran, Indonesia, the U.K., Iraq, the U.S., Pakistan, and Ethiopia.

"Many nations, excluding India, are participants in China's [Belt and Road Initiative](https://thehackernews.com/2023/11/chinese-hackers-launch-covert-espionage.html) and have, for most of them, coastlines where Chinese infrastructure investments are significant," Sekoia [said](https://blog.sekoia.io/unplugging-plugx-sinkholing-the-plugx-usb-worm-botnet/). "Numerous affected countries are located in re...