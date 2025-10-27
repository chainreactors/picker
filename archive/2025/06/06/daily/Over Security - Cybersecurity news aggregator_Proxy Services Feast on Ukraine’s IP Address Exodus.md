---
title: Proxy Services Feast on Ukraine’s IP Address Exodus
url: https://krebsonsecurity.com/2025/06/proxy-services-feast-on-ukraines-ip-address-exodus/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-06
fetch_date: 2025-10-06T22:55:46.352749
---

# Proxy Services Feast on Ukraine’s IP Address Exodus

Advertisement

[![](/b-knowbe4/36.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

Advertisement

[![](/b-ninjio/10.png)](https://ninjio.com/lp46d-krebs/)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Proxy Services Feast on Ukraine’s IP Address Exodus

June 5, 2025

[16 Comments](https://krebsonsecurity.com/2025/06/proxy-services-feast-on-ukraines-ip-address-exodus/#comments)

![](https://krebsonsecurity.com/wp-content/uploads/2025/06/ukraine-networks.png)

Ukraine has seen nearly one-fifth of its Internet space come under Russian control or sold to Internet address brokers since February 2022, a new study finds. The analysis indicates large chunks of Ukrainian Internet address space are now in the hands of shadowy proxy and anonymity services that are nested at some of America’s largest Internet service providers (ISPs).

The findings come in [a report](https://www.kentik.com/blog/exodus-of-ipv4-from-war-torn-ukraine/) examining how the Russian invasion has affected Ukraine’s domestic supply of **Internet Protocol Version 4** (IPv4) addresses. Researchers at **Kentik**, a company that measures the performance of Internet networks, found that while a majority of ISPs in Ukraine haven’t changed their infrastructure much since the war began in 2022, others have resorted to selling swathes of their valuable IPv4 address space just to keep the lights on.

For example, Ukraine’s incumbent ISP **Ukrtelecom** is now routing just 29 percent of the IPv4 address ranges that the company controlled at the start of the war, Kentik found. Although much of that former IP space remains dormant, Ukrtelecom told Kentik’s **Doug Madory** they were forced to sell many of their address blocks “to secure financial stability and continue delivering essential services.”

“Leasing out a portion of our IPv4 resources allowed us to mitigate some of the extraordinary challenges we have been facing since the full-scale invasion began,” Ukrtelecom told Madory.

Madory found much of the IPv4 space previously allocated to Ukrtelecom is now scattered to more than 100 providers globally, particularly at three large American ISPs — **Amazon** (AS16509), **AT&T** (AS7018), and **Cogent** (AS174).

Another Ukrainian Internet provider — **LVS** (AS43310) — in 2022 was routing approximately 6,000 IPv4 addresses across the nation. Kentik learned that by November 2022, much of that address space had been parceled out to over a dozen different locations, with the bulk of it being announced at AT&T.

![](https://krebsonsecurity.com/wp-content/uploads/2025/06/kentik-lvs.png)

Ditto for the Ukrainian ISP **TVCOM**, which currently routes nearly 15,000 fewer IPv4 addresses than it did at the start of the war. Madory said most of those addresses have been scattered to 37 other networks outside of Eastern Europe, including Amazon, AT&T, and **Microsoft**.

The Ukrainian ISP **Trinity** (AS43554) went offline in early March 2022 during the bloody siege of Mariupol, but its address space eventually began showing up in more than 50 different networks worldwide. Madory found more than 1,000 of Trinity’s IPv4 addresses suddenly appeared on AT&T’s network.

Why are all these former Ukrainian IP addresses being routed by U.S.-based networks like AT&T? According to **spur.us**, a company that tracks VPN and proxy services, nearly all of the address ranges identified by Kentik now map to commercial proxy services that allow customers to anonymously route their Internet traffic through someone else’s computer.

![](https://krebsonsecurity.com/wp-content/uploads/2015/06/proxy.png)

From a website’s perspective, the traffic from a proxy network user appears to originate from the rented IP address, not from the proxy service customer. These services can be used for several business purposes, such as price comparisons, sales intelligence, [web crawlers and content-scraping bots](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7326663504701140992/?actorCompanyId=51677041). However, proxy services also are [massively abused for hiding cybercrime activity](https://intel471.com/blog/a-look-at-the-residential-proxy-market) because they can make it difficult to trace malicious traffic to its original source.

IPv4 address ranges are always in high demand, which means they are also quite valuable. There are now multiple companies that will pay ISPs to lease out their unwanted or unused IPv4 address space. Madory said these IPv4 brokers will pay between $100-$500 per month to lease a block of 256 IPv4 addresses, and very often the entities most willing to pay those rental rates are proxy and VPN providers.

A cursory review of [all Internet address blocks currently routed through AT&T](https://bgp.he.net/AS7018#_prefixes) — as seen in public records maintained by the Internet backbone provider **Hurricane Electric** — shows a preponderance of country flags other than the United States, including networks originating in Hungary, Lithuania, Moldova, Mauritius, Palestine, Seychelles, Slovenia, and Ukraine.

![](https://krebsonsecurity.com/wp-content/uploads/2025/06/att-bg-he-net.png)

AT&T’s IPv4 address space seems to be routing a great deal of proxy traffic, including a large number of IP address ranges that were until recently routed by ISPs in Ukraine.

Asked about the apparent high incidence of proxy services routing foreign address blocks through AT&T, the telecommunications giant said it recently changed its policy about originating routes for network blocks that are not owned and managed by AT&T. That new policy, spelled out in [a February 2025 update to AT&T’s terms of service](http://serviceguidenew.att.com/sg_flashPlayerPage/MIS), gives those customers until Sept. 1, 2025 to originate their own IP space from their own autonomous system number (ASN), a unique number assigned to each ISP (AT&T’s is AS7018).

“To ensure our customers receive the best quality of service, we changed our terms for dedicated internet in February 2025,” an AT&T spokesperson said in an emailed reply. “We no longer permit static routes with IP addresses that we have not provided. We have been in the process of identifying and notifying affected customers that they have 90 days to transition to Border Gateway Protocol routing using their own autonomous system number.”

Ironically, the co-mingling of Ukrainian IP address space with proxy providers has resulted in many of these addresses being used in cyberattacks against Ukraine and other enemies of Russia. Earlier this month, the European Union sanctioned **Stark Industries Solutions Inc.**, an ISP that surfaced two weeks before the Russian invasion and quickly became the source of large-scale DDoS attacks and spear-phishing attempts by Russian state-sponsored hacking groups. A deep dive into Stark’s considerable address space showed some of it was sourced from Ukrainian ISPs, and [most of it was connected to Russia-based proxy and anonymity services](https://krebsonsecurity.com/2024/05/stark-industries-solutions-an-iron-hammer-in-the-cloud/).

![](https://krebsonsecurity.com/wp-content/uploads/2025/06/iproyal.png)

According to Spur, the proxy service IPRoyal is the current beneficiary of IP address blocks from several Ukrainian ISPs profiled in Kentik’s report. Customers can chose proxies by specifying the city and country they would to proxy their traffic through. Image: Trend Micro.

Spur’s Chief Technology Officer **Riley Kilmer**said AT&T’s policy change will likely force many proxy services to migrate to other U.S. providers that have less strin...