---
title: Aisuru Botnet Shifts from DDoS to Residential Proxies
url: https://krebsonsecurity.com/2025/10/aisuru-botnet-shifts-from-ddos-to-residential-proxies/
source: Over Security - Cybersecurity news aggregator
date: 2025-10-29
fetch_date: 2025-10-30T03:12:40.572334
---

# Aisuru Botnet Shifts from DDoS to Residential Proxies

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-action1/2.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Aisuru Botnet Shifts from DDoS to Residential Proxies

October 28, 2025

[19 Comments](https://krebsonsecurity.com/2025/10/aisuru-botnet-shifts-from-ddos-to-residential-proxies/#comments)

**Aisuru**, the botnet responsible for a series of record-smashing distributed denial-of-service (DDoS) attacks this year, recently was overhauled to support a more low-key, lucrative and sustainable business: Renting hundreds of thousands of infected Internet of Things (IoT) devices to proxy services that help cybercriminals anonymize their traffic. Experts say a glut of proxies from Aisuru and other sources is fueling large-scale data harvesting efforts tied to various artificial intelligence (AI) projects, helping content scrapers evade detection by routing their traffic through residential connections that appear to be regular Internet users.

![Image credit: vxdb](https://krebsonsecurity.com/wp-content/uploads/2025/10/aisuru-ipidea.png)

First identified in August 2024, Aisuru has spread to at least 700,000 IoT systems, such as poorly secured Internet routers and security cameras. Aisuru’s overlords have used their massive botnet to clobber targets with headline-grabbing DDoS attacks, flooding targeted hosts with blasts of junk requests from all infected systems simultaneously.

In June, Aisuru hit KrebsOnSecurity.com with a DDoS [clocking at 6.3 terabits per second](https://krebsonsecurity.com/2025/05/krebsonsecurity-hit-with-near-record-6-3-tbps-ddos/) — the biggest attack that **Google** had ever mitigated at the time. In the weeks and months that followed, Aisuru’s operators demonstrated DDoS capabilities of nearly 30 terabits of data per second — well beyond the attack mitigation capabilities of most Internet destinations.

These digital sieges have been particularly disruptive this year for U.S.-based Internet service providers (ISPs), in part because Aisuru recently succeeded in [taking over a large number of IoT devices in the United States](https://krebsonsecurity.com/2025/10/ddos-botnet-aisuru-blankets-us-isps-in-record-ddos/). And when Aisuru launches attacks, the volume of outgoing traffic from infected systems on these ISPs is often so high that it can disrupt or degrade Internet service for adjacent (non-botted) customers of the ISPs.

“Multiple broadband access network operators have experienced significant operational impact due to outbound DDoS attacks in excess of 1.5Tb/sec launched from Aisuru botnet nodes residing on end-customer premises,” wrote **Roland Dobbins**, principal engineer at **Netscout**, in a recent [executive summary on Aisuru](https://www.netscout.com/blog/asert/asert-threat-summary-aisuru-and-related-turbomirai-botnet-ddos). “Outbound/crossbound attack traffic exceeding 1Tb/sec from compromised customer premise equipment (CPE) devices has caused significant disruption to wireline and wireless broadband access networks. High-throughput attacks have caused chassis-based router line card failures.”

The incessant attacks from Aisuru have caught the attention of federal authorities in the United States and Europe (many of Aisuru’s victims are customers of ISPs and hosting providers based in Europe). Quite recently, some of the world’s largest ISPs have started informally sharing block lists identifying the rapidly shifting locations of the servers that the attackers use to control the activities of the botnet.

Experts say the Aisuru botmasters recently updated their malware so that compromised devices can more easily be rented to so-called “**residential proxy**” providers. These proxy services allow paying customers to route their Internet communications through someone else’s device, providing anonymity and the ability to appear as a regular Internet user in almost any major city worldwide.

![](https://krebsonsecurity.com/wp-content/uploads/2015/06/proxy.png)

From a website’s perspective, the IP traffic of a residential proxy network user appears to originate from the rented residential IP address, not from the proxy service customer. Proxy services can be used in a legitimate manner for several business purposes — such as price comparisons or sales intelligence. But they are massively abused for hiding cybercrime activity (think advertising fraud, credential stuffing) because they can make it difficult to trace malicious traffic to its original source.

And as we’ll see in a moment, this entire shadowy industry appears to be shifting its focus toward enabling aggressive content scraping activity that continuously feeds raw data into large language models (LLMs) built to support various AI projects.

## ‘INSANE’ GROWTH

**Riley Kilmer** is co-founder of [spur.us](https://spur.us), a service that tracks proxy networks. Kilmer said all of the top proxy services have grown exponentially over the past six months — with some adding between 10 to 200 times more proxies for rent.

“I just checked, and in the last 90 days we’ve seen 250 million unique residential proxy IPs,” Kilmer said. “That is insane. That is so high of a number, it’s unheard of. These proxies are absolutely everywhere now.”

To put Kilmer’s comments in perspective, here was Spur’s view of the Top 10 proxy networks by approximate install base, circa May 2025:

AUPROXIES\_PROXY  66,097
RAYOBYTE\_PROXY    43,894
OXYLABS\_PROXY   43,008
WEBSHARE\_PROXY   39,800
IPROYAL\_PROXY    32,723
PROXYCHEAP\_PROXY    26,368
IPIDEA\_PROXY    26,202
MYPRIVATEPROXY\_PROXY  25,287
HYPE\_PROXY    18,185
MASSIVE\_PROXY    17,152

Today, Spur says it is tracking an unprecedented spike in available proxies across all providers, including;

LUMINATI\_PROXY    11,856,421
NETNUT\_PROXY    10,982,458
ABCPROXY\_PROXY    9,294,419
OXYLABS\_PROXY     6,754,790
IPIDEA\_PROXY     3,209,313
EARNFM\_PROXY    2,659,913
NODEMAVEN\_PROXY    2,627,851
INFATICA\_PROXY    2,335,194
IPROYAL\_PROXY    2,032,027
YILU\_PROXY    1,549,155

Reached for comment about the apparent rapid growth in their proxy network, Oxylabs (#4 on Spur’s list) said while their proxy pool did grow recently, it did so at nowhere near the rate cited by Spur.

“We don’t systematically track other providers’ figures, and we’re not aware of any instances of 10× or 100× growth, especially when it comes to a few bigger companies that are legitimate businesses,” the company said in a written statement.

**Bright Data** was formerly known as **Luminati Networks**, the name that is currently at the top of Spur’s list of the biggest residential proxy networks, with more than 11 million proxies. Bright Data likewise told KrebsOnSecurity that Spur’s current estimates of its proxy network are dramatically overstated and inaccurate.

“We did not actively initiate nor do we see any 10x or 100x expansion of our network, which leads me to believe that someone might be presenting these IPs as Bright Data’s in some way,” said **Rony Shalit**, Bright Data’s chief compliance and ethics officer. “In many cases in the past, due to us being the leading data collection proxy provider, IPs were falsely tagged as being part of our network, or while being used by other proxy providers for malicious activity.”

“Our network is only sourced from verified IP providers and [a robust opt-in only residential peers](https://brightdata.com/trustcenter/bright-sdk-ethical-data-pra...