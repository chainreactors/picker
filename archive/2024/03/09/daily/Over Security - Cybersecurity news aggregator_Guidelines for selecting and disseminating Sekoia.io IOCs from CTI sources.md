---
title: Guidelines for selecting and disseminating Sekoia.io IOCs from CTI sources
url: https://blog.sekoia.io/guidelines-for-selecting-and-disseminating-sekoia-io-iocs-from-cti-sources/
source: Over Security - Cybersecurity news aggregator
date: 2024-03-09
fetch_date: 2025-10-04T12:12:20.203287
---

# Guidelines for selecting and disseminating Sekoia.io IOCs from CTI sources

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Product News](https://blog.sekoia.io/category/product-news/ "Product News")
[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Guidelines for selecting and disseminating Sekoia.io IOCs from CTI sources

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Julien de Pins](#molongui-disabled-link)
March 7 2024

0

11 minutes reading

In the ever-evolving landscape of cybersecurity, the battle against threats demands a multi-faceted approach. Organizations, now more than ever, need to leverage comprehensive Threat Intelligence to stay ahead of adversaries. At the forefront of this defense is Sekoia.io, a leading cybersecurity vendor offering a cutting-edge CTI platform (Cyber Threat Intelligence).

Sekoia.io relies on one of the most experienced teams of CTI researchers in Europe and has built capabilities to produce comprehensive intelligence covering the global cyber threat, from a strategic to a technical perspective.

This work is conducted by our Threat Detection & Research team (TDR) composed of CTI researchers and analysts working full-time on CTI production. TDR includes former members of governmental agencies, military and major private organizations.

TDR team is committed to producing exclusive intelligence. To do so, TDR has curated a dynamic ecosystem that combines its proprietary intelligence with curated and contextualized third-party OSINT (Open-Source Intelligence) sources, ensuring a holistic and informed information management strategy.

When it comes to the quality of our intelligence, there is no doubt, the numbers speak for themselves: In 2023,Sekoia.io revoked only 223 IoCs over a total of around 3 millions, which corresponds to a revocation rate of 0,01%.

This article will help you understand the process of manipulating your CTI, especially the diverse data sources present within the Sekoia SOC platform.

For starters, let’s investigate the main data sources leveraged by the platform and find out how they relate to your dissemination use cases.

## **Volume and typology of IOCs from our TOP-10 CTI sources**

Overall, **Sekoia’s intelligence is derived from more than 400 sources and encompasses more than 8 million indicators of compromise**. Many of these sources reflect exclusive Sekoia.io capabilities; some are third-party sources.

Regarding third-party sources, Sekoia.io analysts conduct extensive qualification and contextualization of intelligence. The gathering of data is aligned with the strategic objectives of our intelligence. Pieces of data coming from a third-party source are carefully integrated to fit the existing intelligence database.

The following table displays the number and types of IoCs produced in 2023, coming from our top sources:

|  |  |  |
| --- | --- | --- |
| **Source** | **# of IOCs in 2023** | **IOCs breakdown** |
| Sekoia.io exclusive sources | 763 775 | 47% file hashes21% URLs17% domains13% IPs |
| tria[.]ge | 403 831 | 90% file hashes4% IPs3% URLs3% domains |
| PhishTank | 102 787 | 100% URLs |
| ThreatFox | 93 184 | 47% URLs36% IPs15% domains1% file hashes |
| MalwareBazaar | 80 206 | 100% file hashes |
| URLhaus | 26 966 | 100% URLs |
| phishunt[.]io | 8 806 | 100% URLs |
| Total 2023 (for these 10 sources) | 1 479 555 | 55% file hashes24% URLs11% domains10% IPs |

Categories of IOCs coming from our TOP-10 sources in 2023 (jan.-dec.)

The following tables present, by category of IoC, the sources that have provided the most of these IoCs types, in 2023. They can help you understand which sources generate specific IoCs and guide you in selecting sources for your dissemination use cases.

|  |  |
| --- | --- |
| **Source** | **# of IP addresses in 2023** |
| Sekoia.io exclusive sources | 101 705 |
| ThreatFox | 33 992 |
| tria[.]ge | 16 035 |

|  |  |
| --- | --- |
| **Source** | **# of domains in 2023** |
| Sekoia.io exclusive sources | 132 656 |
| ThreatFox | 13 724 |
| tria[.]ge | 12 924 |

|  |  |
| --- | --- |
| **Source** | **# of URLs in 2023** |
| Sekoia.io exclusive sources | 164 647 |
| PhishTank | 102 787 |
| ThreatFox | 44 209 |
| URLhaus | 26 966 |
| tria[.]ge | 13 284 |
| phishunt[.]io | 8 806 |

|  |  |
| --- | --- |
| **Source** | **# of file hashes in 2023** |
| Sekoia.io exclusive sources | 363 957 |
| tria[.]ge | 361 449 |
| MalwareBazaar | 80 206 |
| Sekoia[.]io | 16 044 |
| ThreatFox | 1 240 |

Repartition of the categories of IOCs coming from our TOP-10 sources in 2023 (jan.-dec.)

## **Disseminating Sekoia intelligence**

Sekoia.io strives to offer CTI that fully supports the operational objectives of security teams. The intelligence is designed to enhance detection and hunting capabilities. Therefore, Sekoia.io relies on time-tested [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html) standards for CTI modeling. These standards are developed by the OASIS foundation (Sekoia.io is a [member of the OASIS foundation](https://www.oasis-open.org/members/)).

STIX is the language analysts use to exchange their data transparently and enable its use in vendor-agnostic security systems. At Sekoia, we believe STIX is the best way to offer interoperable intelligence consolidated in a single database.

Disseminating data to your security solutions is key to leveraging the benefits of Sekoia.io CTI. We offer different methods you can use. Please check [our public documentation](https://docs.sekoia.io/cti/features/integrations/) for more information on CTI dissemination and available APIs.

### **How to choose the method to disseminate CTI**

There are three main methods you can use to operate the dissemination. Please note that the methods are only briefly described, and you can [contact your Sekoia.io representative](https://www.sekoia.io/en/contact/) for more information.

* **Method 1...