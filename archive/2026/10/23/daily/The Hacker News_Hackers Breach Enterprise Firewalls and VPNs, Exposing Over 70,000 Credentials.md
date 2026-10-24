---
title: Hackers Breach Enterprise Firewalls and VPNs, Exposing Over 70,000 Credentials
url: https://thehackernews.com/2026/10/hackers-breach-enterprise-firewalls-and.html
source: The Hacker News
date: 2026-10-23
fetch_date: 2026-10-24T06:48:21.795530
---

# Hackers Breach Enterprise Firewalls and VPNs, Exposing Over 70,000 Credentials

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Hackers Breach Enterprise Firewalls and VPNs, Exposing Over 70,000 Credentials](https://thehackernews.com/2026/10/hackers-breach-enterprise-firewalls-and.html)

**Ravie Lakshmanan**Oct 23, 2026Vulnerability / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSk-Q06Dd5YyYmXWMt9b860DzGRKbTae_QwvoZDKNICaEznAj2AUurJmv6vPnpcH7qqDjauFZWWx7GX1RN93BLaU9Rqgiqe9j1iQRg2Vqcz3HpSqgesA6oS-GrMTyx4CTzwOD7C_z205k57ZpT70Gv4RXi-65X-nyI04wpA3raJ5nh46pN5ox42cyLnHjv/s1700-nu-rw-lo-l85-e365/1000117358.jpg)

Cybersecurity researchers have disclosed details of a large-scale campaign that has targeted exposed network edge devices such as Fortinet FortiGate and Palo Alto Networks GlobalProtect firewalls.

"Artifacts from this investigation also indicate that operators in this campaign have obtained access to numerous organizations worldwide, and have attempted to further compromise some victims, resulting in persistent remote access and data exfiltration," according to a [joint investigation](https://www.group-ib.com/blog/stray-cat-network-edge/) published by Group-IB and NyxLab.

The widespread exploitation activity has been attributed to a threat actor known as k0t, who also goes by the aliases CryptoFeel, Member19, and QazWsxShop. The cybercriminal actor was first seen in the wild on October 22, 2025.

The threat actor is assessed to share connections with ransomware groups such as Qilin and The Gentlemen, likely operating as an initial access broker or an affiliate. Analysis of the threat actor's dark web activity reveals a keen interest in purchasing vulnerability exploit code and tools or premium accounts for metadata search engines like [FOFA and ZoomEye](https://www.vectra.ai/blog/how-attackers-use-shodan-fofa).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

The campaign's victims are global and belong to a broad range of sectors, given the indiscriminate targeting of exposed network devices. A significant chunk of compromises are said to have taken place between February and June 2026, which also overlaps with another credential harvesting campaign codenamed [FortiBleed](https://thehackernews.com/2026/10/fbi-warns-fortibleed-remains-active.html).

Nearly 38% of victims are concentrated in the Asia Pacific region, followed by 31.9% in Latin America, 15.8% in Europe, and 12.7% in the Middle East and North Africa.

The attack chain plays out as follows -

* Conduct reconnaissance through public scanning tools like FOFA and ZoomEye to enumerate internet-facing VPN and firewall appliances, filter candidates by product, and put together target lists of potentially vulnerable edge devices.
* Attempt to exploit these devices via known vulnerabilities like [CVE-2025-64446](https://thehackernews.com/2025/11/fortinet-fortiweb-flaw-actively.html) (a path traversal flaw in FortiWeb) and [CVE-2026-0257](https://thehackernews.com/2026/10/qilin-and-inc-ransomware-groups-exploit.html) (an authentication bypass flaw in Palo Alto Networks PAN-OS and Prisma Access) through bespoke Python scripts named "fortnew.py" and "exploit\_2026\_0257.py," or perform brute-force attacks using common username and password combinations, to obtain initial access.
* Establish a foothold on the targets via an OpenConnect VPN connection.
* Conduct post-exploitation actions and additional credential theft like enumeration of Active Directory, SMB, and installed antivirus solution.
* Establish persistence on the host via legitimate remote access tools like MeshCentral Agent, Atera, Teramind, and AnyDes, as well as an open-source, adversary-emulation framework known as [AdaptixC2](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html).
* Exfiltrate harvested data using Rclone into Wasabi S3 buckets and MEGA cloud drives.

The attacks are also characterized by the use of legitimate administrator and pentesting utilities like NetExec, SoftPerfect, Impacket, noPac, Kerbrute, PetitPotam, and Mimikatz to burrow deeper into victims' corporate environments.

"k0t appears to select potential targets by enumerating exposed network appliances at scale rather than researching individual organizations," Group-IB and NyxLab researchers said. "His stated geographic priorities begin with the United States and Canada, followed by European countries and selected APAC markets."

"The product and location of an exposed device therefore appear to matter more than the industry of the organization operating it, consistent with the broad range of victims observed in this campaign."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

k0t's links to Qilin and The Gentlemen stem from the fact that many victims of the campaign were also later listed by the ransomware groups on their data leak sites. However, the exact nature of the connection between the threat and these gangs is unclear.

What's more, Group-IB and NyxLab said they found a "negligible overlap" in compromised data between this activity and FortBleed. More than 70,000 exposed credentials associated with network devices and LDAP dumps have been identified in connection with the campaign.

"This aligns with reports that many operators are likely to be involved in the FortiBleed activity cluster, suggesting that this may be a separate dataset, operator subset, or related access operation within the broader FortiBleed-related activity," the researchers said. "Organizations are advised to act on ensuring that any vulnerabilities mentioned in this report are appropriately remedied."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_shar...