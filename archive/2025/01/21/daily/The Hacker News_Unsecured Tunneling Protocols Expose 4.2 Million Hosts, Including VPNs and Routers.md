---
title: Unsecured Tunneling Protocols Expose 4.2 Million Hosts, Including VPNs and Routers
url: https://thehackernews.com/2025/01/unsecured-tunneling-protocols-expose-42.html
source: The Hacker News
date: 2025-01-21
fetch_date: 2025-10-06T20:13:05.824512
---

# Unsecured Tunneling Protocols Expose 4.2 Million Hosts, Including VPNs and Routers

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

# [Unsecured Tunneling Protocols Expose 4.2 Million Hosts, Including VPNs and Routers](https://thehackernews.com/2025/01/unsecured-tunneling-protocols-expose-42.html)

**Jan 20, 2025**Ravie LakshmananNetwork Security / Vulnerability

[![Tunneling Protocols](data:image/png;base64... "Tunneling Protocols")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbemTVqg0rpnGDJzNcmjV5hGZDDBzpEyjSQW4N8BMQIJrZjfZMwAcQ_TrIH6o3DrEzgbbTkc0vKpU-hrCTIGqago-idWziUoooxIUtjQXJNmLKfqjhw9ItbDfDQ6udECe3SoiADwveEZYF1AuBHINmuF2Cx-yddCIxDBnKkaM51AXJT1DQmQ8kij326nRU/s790-rw-e365/tunnel.png)

New research has uncovered security vulnerabilities in multiple [tunneling protocols](https://en.wikipedia.org/wiki/Tunneling_protocol) that could allow attackers to perform a wide range of attacks.

"Internet hosts that accept tunneling packets without verifying the sender's identity can be hijacked to perform anonymous attacks and provide access to their networks," Top10VPN [said](https://www.top10vpn.com/research/tunneling-protocol-vulnerability/) in a study, as part of a collaboration with KU Leuven professor and researcher Mathy Vanhoef.

As many as 4.2 million hosts have been found susceptible to the attacks, including VPN servers, ISP home routers, core internet routers, mobile network gateways, and content delivery network (CDN) nodes. China, France, Japan, the U.S., and Brazil top the list of the most affected countries.

Successful exploitation of the shortcomings could permit an adversary to abuse a susceptible system as one-way proxies, as well as conduct denial-of-service (DoS) attacks.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"An adversary can abuse these security vulnerabilities to create one-way proxies and spoof source IPv4/6 addresses," the CERT Coordination Center (CERT/CC) [said](https://kb.cert.org/vuls/id/199397) in an advisory. "Vulnerable systems may also allow access to an organization's private network or be abused to perform DDoS attacks."

The vulnerabilities are rooted in the fact that the tunneling protocols such as IP6IP6, GRE6, 4in6, and 6in4, which are mainly used to facilitate data transfers between two disconnected networks, do not authenticate and encrypt traffic without adequate security protocols like Internet Protocol Security ([IPsec](https://en.wikipedia.org/wiki/IPsec)).

The absence of additional security guardrails opens the door to a scenario where an attacker can inject malicious traffic into a tunnel, a variation of a flaw that was [previously flagged](https://www.tenable.com/blog/cve-2020-10136-ip-in-ip-packet-processing-vulnerability-could-lead-to-ddos-network-access) in 2020 ([CVE-2020-10136](https://nvd.nist.gov/vuln/detail/CVE-2020-10136)).

The newly discovered flaws have been assigned the following CVE identifiers for the protocols in question -

* CVE-2024-7595 (GRE and GRE6)
* CVE-2024-7596 (Generic UDP Encapsulation)
* CVE-2025-23018 (IPv4-in-IPv6 and IPv6-in-IPv6)
* CVE-2025-23019 (IPv6-in-IPv4)

"An attacker simply needs to send a packet encapsulated using one of the affected protocols with two IP headers," Top10VPN's Simon Migliano explained.

"The outer header contains the attacker's source IP with the vulnerable host's IP as the destination. The inner header's source IP is that of the vulnerable host IP rather than the attacker. The destination IP is that of the target of the anonymous attack."

Thus when the vulnerable host receives the malicious packet, it automatically strips the outer IP address header and forwards the inner packet to its destination. Given that the source IP address on the inner packet is that of the vulnerable but trusted host, it's able to get past network filters.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

As defenses, it's recommended to use IPSec or WireGuard to provide authentication and encryption, and only accept tunneling packets from trusted sources. At the network level, it's also advised to implement traffic filtering on routers and middleboxes, carry out Deep packet inspection (DPI), and block all unencrypted tunneling packets.

"The impact on victims of these DoS attacks can include network congestion, service disruption as resources are consumed by the traffic overload, and crashing of overloaded network devices," Migliano said. "It also opens up opportunities for further exploitation, such as man-in-the-middle attacks and data interception."

### Update

The study has found that vulnerable hosts can enable a wide range of novel DoS attacks, including Routing Loop DoS, administrative DoS attacks that weaponize abuse reports, Ping-Pong Amplification, Tunneled-Temporal Lensing (TuTL), and Economic Denial of Sustainability (EDoS).

"Tunnelled-Temporal Lensing (TuTL) and the Ping-Pong attack [have] an amplification factor of at least 16 and 75, respectively," the study said, adding the EDoS attack refers to a scenario where "the outgoing bandwidth of a host is consumed to incur unexpected financial costs or lead to service disruptions."

More information about the vulnerabilities has been [detailed](https://papers.mathyvanhoef.com/usenix2025-tunnels.pdf) in the study "Haunted by Legacy: Discovering and Exploiting Vulnerable Tunnelling Hosts," published by Angelos Beitis and Mathy Vanhoef.

*(The story was updated after publication on July 20, 2025, to include the research paper.)*

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
[**Sha...