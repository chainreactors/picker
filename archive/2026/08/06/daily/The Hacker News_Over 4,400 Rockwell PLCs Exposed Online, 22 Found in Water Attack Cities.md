---
title: Over 4,400 Rockwell PLCs Exposed Online, 22 Found in Water Attack Cities
url: https://thehackernews.com/2026/08/over-4400-rockwell-plcs-exposed-online.html
source: The Hacker News
date: 2026-08-06
fetch_date: 2026-08-07T04:30:25.107876
---

# Over 4,400 Rockwell PLCs Exposed Online, 22 Found in Water Attack Cities

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

![cybersecurity](data:image/svg+xml;base64...)

# [Over 4,400 Rockwell PLCs Exposed Online, 22 Found in Water Attack Cities](https://thehackernews.com/2026/08/over-4400-rockwell-plcs-exposed-online.html)

**Swati Khandelwal**Aug 06, 2026OT Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUzp-V2FqPXO6jQl0K2Qnn-2Ys6UG168FNhA0TcFv7CGHtBIgWuD66JsjhDiQhf_DkSTBo_YpVGTY3wcLe3SITSszBT0XAD01P6_nFLkXOHNNoKmp6VTsQ-zB9oKR6qYU2tCpf5RwHZ_u35lJiF41Sa3T7zuGfXujh_Ums9snpXTUAJIbcL6LfF9a5bIw/s1700-e365/power.jpg)

Forescout found 22 internet-facing Rockwell Automation programmable logic controllers (PLCs) in cities hit by recent cyberattacks on US water utilities. Nineteen used the same mobile carrier network.

Its August 3 scan counted 4,407 exposed Rockwell controllers worldwide, including 2,844 in the United States, but Forescout could not confirm any were compromised. That figure counts exposed controllers, not water utilities or confirmed victims.

Forescout said the publicly described effects could be achieved without a vulnerability exploit: attackers changed IP addresses and set passwords on controllers that were already reachable, causing operators to lose visibility and, in some cases, control of connected equipment.

Neither the government alerts nor Forescout's analysis explains how the attackers found, selected, or initially accessed their targets.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Water and wastewater utilities in at least seven states have [reported incidents since July 27](https://thehackernews.com/2026/07/coordinated-cyberattack-targets-30.html), the FBI and EPA said in a [July 30 public service announcement](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions). The Hacker News found on August 6 that Forescout's post says the announcement confirmed at least 12 states, while the FBI page says seven. No agency has attributed the campaign.

Whatever the final count, defenders can act now by [taking the controllers off the public internet](https://thehackernews.com/2024/05/rockwell-advises-disconnecting-internet.html).

Exposing EtherNet/IP on port 44818 creates an unauthenticated path that, depending on device configuration, lets an attacker identify a controller or write settings to it, [Forescout said](https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgE-VtOnubM7b90HiKoHv9ItXL-tJQkSjnmIjI8k8u3v3Mvo3kt5BEDDq-pIIdW1iKcDcVniIesGshi-7joYEkScoifbZ12LRcqUaLTAy9kbLVwEpl9PFrinQT0wmSOfToAXYKOgmAKYaIUWhYp9_uxinBk0OOOvS9quMAM14LyiFqymebzqiSJam5tflU/s1700-e365/water.jpg)

Forescout found more than 70% of the US-based exposed controllers on large mobile carrier networks. The [FBI and EPA recommend](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions) strong authentication, updates and logging for cellular modems, with remote access isolated through a private APN, VPN or similar architecture.

[A July 30 Censys snapshot](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/) found 4,148 exposed Rockwell/Allen-Bradley EtherNet/IP hosts, with Verizon Business, AT&T Mobility and T-Mobile USA accounting for 59%. The Censys and Forescout snapshots both exceed 4,100 hosts, but different platforms, queries and dates make the figures not directly comparable. Forescout's historical series hit a June 2026 low of 4,169, down 47% from 7,814 in March 2020; its August 3 snapshot was 4,407.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

MicroLogix 1400 devices made up 50% of Forescout's results and MicroLogix 1100 devices 8%. The FBI and EPA named both families. Forescout said 19 of the 22 controllers in affected cities ran firmware susceptible to [CVE-2017-16740](https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.PN1010.html) (Rockwell CVSS score: 8.6).

The flaw is a Modbus TCP buffer overflow affecting MicroLogix 1400 Series B and C running firmware 21.002 and earlier; Rockwell fixed it in revision 21.003. Exploitation requires Modbus TCP to be enabled, which Forescout could not verify on those hosts. Firmware updates address specific bugs but "do not make direct public exposure of PLCs acceptable," the researchers wrote.

Rockwell [discontinued](https://www.rockwellautomation.com/en-us/products/details.1763-L16AWA.html) the MicroLogix 1100 on April 30, 2022. [Advisory SD1790](https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1790.html) tells operators locked out by an attacker-set password how to reset a MicroLogix 1400 or 1100 to factory defaults and redownload a known-good project file. The notice carries no CVE because it is recovery guidance, not a vulnerability disclosure.

That recovery path requires a current offline copy of the controller logic. The FBI said at least one victim found modified PLC project files after spotting ladder logic discrepancies across several sites. It also warned that similar third-party network setups may let attackers repeat successful compromises across customers sharing vulnerable configurations.

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
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](...