---
title: Dysphoria IoT Botnet Adds Blockchain C2 and Victim Relays After JackSkid Disruption
url: https://thehackernews.com/2026/07/dysphoria-iot-botnet-adds-blockchain-c2.html
source: The Hacker News
date: 2026-07-27
fetch_date: 2026-07-28T05:00:16.148622
---

# Dysphoria IoT Botnet Adds Blockchain C2 and Victim Relays After JackSkid Disruption

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Dysphoria IoT Botnet Adds Blockchain C2 and Victim Relays After JackSkid Disruption](https://thehackernews.com/2026/07/dysphoria-iot-botnet-adds-blockchain-c2.html)

**Swati Khandelwal**Jul 27, 2026Botnet / IoT Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIg3DnKkxpBnQZhAB8v4Wb9FDnDuh3ifKpBMF3kFhNr7_lYOk3S4CgvBoOxFD65FlCjRpoaoBNyH8zo8NtOhjTtTWriXHawlL9mndT3fd_7zlhUBU4mhjU4AvvYNzgV-PGsd52Ng0wnaDRAJMkRQtW4kUuMKlcrP0B71xxywX6cTICeHmMAjswmKhQJKo/s1700-e365/blockchain-botnet.jpg)

**Dysphoria**, an Internet of Things (IoT) botnet line tracked by CNCERT and XLab, has adopted blockchain-based name services and infected-device relays after a March law-enforcement operation against JackSkid infrastructure. The researchers say the design makes the botnet harder to disrupt.

CNCERT, China's national computer emergency response team, and XLab, the threat-intelligence lab of Chinese firm Qi'anxin, put its population above 200,000 bots. Their telemetry logged 4,401 confirmed active devices inside China between July 14 and 20 and a single-day peak of 239,000 bots abroad.

None of the counts has been independently reproduced. The researchers published no counting or de-duplication methodology, so the numbers should not be read as a precise device census.

Defenders should patch exposed IoT gear, replace devices that can no longer be updated, eliminate default and weak credentials, and disable remote management and UPnP where they are not needed.

The lineage runs through [JackSkid](https://thehackernews.com/2026/03/doj-disrupts-3-million-device-iot.html), one of four IoT botnets targeted in coordinated U.S., German, and Canadian law-enforcement actions on March 19. Court documents attributed more than 90,000 DDoS commands to JackSkid alone.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Within days, Nokia Deepfield and Comcast's threat lab [documented](https://github.com/deepfield/public-research/blob/main/jackskid/report.md) the operator falling back to an Ethereum Name Service (ENS) domain, m3rnbvs5d[.]eth, for command-and-control (C2). XLab's Dysphoria timeline opens with a JackSkid sample captured on March 25, six days after the disruption, that resolves C2 through the same domain.

[XLab found](https://blog.xlab.qianxin.com/dysphoria/) that the burrberry[.]eth record encodes distribution-node IPv4 addresses, while 24carnforth2merseyside[.]sol supplies other infrastructure records. The DDoS sample asks a distribution node over HTTP for a current server list, and the listed endpoints are infected machines relaying traffic to the real controllers. The design keeps those controllers one step removed from the addresses exposed to bots.

The XLab analysis, published July 25, tracks a fast run of builds: custom RC4 string encryption and ENS resolution at the end of April, followed by Solana Name Service (SNS) resolution in early May. A relay-only variant appeared on June 25, with UPnP-based port mapping added days later to traverse NAT gateways.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeERa-d9ZUe23QQJdFmb03DzeX-stZSBm4bO7gmoF7oZnIcuzLSaM6ITRoEgDmbpoT_dlQi1h3GUm_x-pfDDcUmKmT2qUXmai3iDWGrP46xY9xLeVUnUjRtdRssT6qeyrYxIXMM5ZnRGRA9vkbiEMiKWgIWSF77sJYv-SlEH3UmwyUBluqMzgV7M6HBxk/s1700-e365/botnet.jpg)

The relay-only build drops the DDoS modules and instead uses UPnP to map ports on the local gateway and Linux epoll to shuttle traffic between an outside connection and a remote C2 service. XLab documented the [related Kimwolf botnet](https://thehackernews.com/2025/12/kimwolf-botnet-hijacks-18-million.html) using ENS-based C2 late last year. Dysphoria couples the same resolution model with a relay mesh built from its own victims.

The shift complicates a conventional server seizure, but it does not remove infrastructure from the chain: the botnet still depends on blockchain records, reachable distribution nodes, and compromised relays.

Japan's NICT independently [documented](https://blog.nicter.jp/2026/05/jackskid_2026_may/) the same JackSkid-to-ENS/SNS shift in May, and, like Nokia and Comcast, found code and strings shared with several other botnet families. That overlap points to shared tooling rather than proof of a single operator, and none of the researchers name one.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrEy9jEFSadp95ztaH87-97Z_U9V94nUsE-BsrdwSR8ETPJDyCjy63vNxc-O26z6VhA3nDOrU24lJqNdy24bfNxGPxGxXNRvM_XCwnZ7ukY5wDnXKsvDZN42aCT1JFYXZZGoZFEtSQgbba742oPTEgEbtoa0GBYWWkkkU43P1wPq-LByZPJfbzwZsb1RiI/s728-e100/sygnia-d-1.png)](https://thn.news/sygnia-webinar)

XLab and CNCERT say Dysphoria spreads through Telnet and SSH weak-password guessing and a set of known IoT remote-code-execution flaws in routers, gateways, and cameras. One example present in both published lists is [CVE-2025-9528](https://nvd.nist.gov/vuln/detail/CVE-2025-9528), a Linksys E1700 command-injection flaw disclosed in August 2025 with a public exploit.

The vendor did not respond to the original report. NVD's CVSS vector rates the flaw as requiring high privileges, and neither publication explains how it fits the botnet's propagation chain.

A comparison by The Hacker News found that XLab's post and a mirrored [CNCERT notice](https://www.secrss.com/articles/92461) publish different vulnerability lists despite presenting the same joint research. Both agree that weak Telnet and SSH credentials remain the most consistent way in.

XLab says Dysphoria attacks internet-service and gaming targets almost daily, but it names no victims or measured peaks. The storefront advertises attacks of up to about 4 Tbps for tens to hundreds of dollars, but that is an operator claim, not a measured attack.

Cloudflare [measured a 31.4 Tbps attack](https://blog.cloudflare.com/ddos-threat-report-2025-q4/) from the related [AISURU/Kimwolf botnet](https://thehackernews.com/2026/02/aisu...