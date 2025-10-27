---
title: New Gorilla Botnet Launches Over 300,000 DDoS Attacks Across 100 Countries
url: https://thehackernews.com/2024/10/new-gorilla-botnet-launches-over-300000.html
source: The Hacker News
date: 2024-10-08
fetch_date: 2025-10-06T18:54:24.709922
---

# New Gorilla Botnet Launches Over 300,000 DDoS Attacks Across 100 Countries

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

# [New Gorilla Botnet Launches Over 300,000 DDoS Attacks Across 100 Countries](https://thehackernews.com/2024/10/new-gorilla-botnet-launches-over-300000.html)

**Oct 07, 2024**Ravie LakshmananIoT Security / Botnet

[![Gorilla Botnet](data:image/png;base64... "Gorilla Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3_LXe3apUde3JYajQXc8w82tHJjS4Blw81Sa8XaTSiwtCHvbHKFnXDqIgFJnIgxY9I22Q6gJpV6KJq5qI-TtcwgkAs4jG3DN2JLBlpSXgE5YeximF1FHrc_Zwv3_biwyLM7n2_USOwctGxQJpLGtaSeNJPfHzGnbUY0egTtKnBkEMHjCPTZbk8LDrO1u3/s790-rw-e365/botnet.png)

Cybersecurity researchers have discovered a new botnet malware family called Gorilla (aka GorillaBot) that draws its inspiration from the leaked [Mirai](https://thehackernews.com/2023/06/active-mirai-botnet-variant-exploiting.html) botnet source code.

Cybersecurity firm NSFOCUS, which identified the activity last month, [said](https://nsfocusglobal.com/over-300000-gorillabot-the-new-king-of-ddos-attacks/) the botnet "issued over 300,000 attack commands, with a shocking attack density" between September 4 and September 27, 2024. No less than 20,000 commands designed to mount distributed denial-of-service (DDoS) attacks have been issued from the botnet every day on average.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The botnet is said to have targeted more than 100 countries, attacking universities, government websites, telecoms, banks, gaming, and gambling sectors. China, the U.S., Canada, and Germany have emerged as the most attacked countries.

The Beijing-headquartered company said Gorilla primarily uses [UDP flood](https://www.cloudflare.com/learning/ddos/udp-flood-ddos-attack/), ACK BYPASS flood, [Valve Source Engine (VSE) flood](https://www.fortinet.com/blog/threat-research/botnets-continue-exploiting-cve-2023-1389-for-wide-scale-spread), [SYN flood](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/), and [ACK flood](https://www.cloudflare.com/learning/ddos/what-is-an-ack-flood/) to conduct the DDoS attacks, adding the [connectionless nature of the UDP protocol](https://thehackernews.com/2024/03/new-loop-dos-attack-impacts-hundreds-of.html) allows for arbitrary source IP spoofing to generate a large amount of traffic.

Besides supporting multiple CPU architectures such as ARM, MIPS, x86\_64, and x86, the botnet comes with capabilities to connect with one of the five predefined command-and-control (C2) servers to await DDoS commands.

In an interesting twist, the malware also embeds functions to exploit a security flaw in Apache Hadoop YARN RPC to achieve remote code execution. It's worth noting that the shortcoming has been abused in the wild as far back as 2021, according to [Alibaba Cloud](https://www.alibabacloud.com/blog/zero-day-attack-analysis-and-dissemination-method-disclosure-for-hadoop-yarn-rpc_598248) and [Trend Micro](https://www.trendmicro.com/en_us/research/21/g/threat-actors-exploit-misconfigured-apache-hadoop-yarn.html).

Persistence on the host is achieved by creating a service file named custom.service in the "/etc/systemd/system/" directory and configuring it to run automatically every time at system startup.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The service, for its part, is responsible for downloading and executing a shell script ("lol.sh") from a remote server ("pen.gorillafirewall[.]su"). Similar commands are also added to "/etc/inittab," "/etc/profile," and "/boot/bootcmd" files to download and run the shell script upon system startup or user login.

"It introduced various DDoS attack methods and used encryption algorithms commonly employed by the [Keksec group](https://thehackernews.com/2022/04/new-enemybot-ddos-botnet-borrows.html) to hide key information, while employing multiple techniques to maintain long-term control over IoT devices and cloud hosts, demonstrating a high level of counter-detection awareness as an emerging botnet family," NSFOCUS said.

### Update

A security researcher who goes by the online alias Fox\_threatintel, in a [post](https://x.com/banthisguy9349/status/1843333881828913539) [shared](https://x.com/banthisguy9349/status/1787434705849069843) on X, said the botnet malware is not entirely new and that it has been active for over a year.

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

[Apache Hadoop](https://thehackernews.com/search/label/Apache%20Hadoop)[botnet](https://thehackernews.com/search/label/botnet)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ddos attack](https://thehackernews.com/search/label/ddos%20attack)[Internet of Things](https://thehackernews.com/search/label/Internet%20of%20Things)[Malware](https://thehackernews.com/search/label/Malware)[mirai botnet](https://thehackernews.com/search/label/mirai%20botnet)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Inci...