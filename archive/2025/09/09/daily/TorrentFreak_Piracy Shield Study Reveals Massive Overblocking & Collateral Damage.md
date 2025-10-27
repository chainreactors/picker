---
title: Piracy Shield Study Reveals Massive Overblocking & Collateral Damage
url: https://torrentfreak.com/piracy-shield-study-reveals-massive-overblocking-collateral-damage-250909/
source: TorrentFreak
date: 2025-09-09
fetch_date: 2025-10-02T19:52:44.231211
---

# Piracy Shield Study Reveals Massive Overblocking & Collateral Damage

[![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/search.svg)

* News ▼
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/x.svg)

# Piracy Shield Study Reveals Massive Overblocking & Collateral Damage

September 8, 2025 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Piracy Research](https://torrentfreak.com/category/research/ "Go to the Piracy Research category archives.") >

Faced with rampant piracy of content that generates a significant chunk of their revenue, sports leagues and their broadcasting partners are deploying increasingly aggressive anti-piracy measures. Italy's Piracy Shield was promoted as the solution, but a new peer-reviewed study casts a very different light. Researchers reveal an ineffective anti-piracy system easily circumvented by pirates, that causes collateral damage affecting hundreds of entirely innocent websites.

![piracy-shield-planet-s](https://torrentfreak.com/images/piracy-shield-planet-s.png)
From the perspective of rightsholders, blocking domains and IP addresses is necessary to counter a persistent threat from online piracy. In this context, they insist it is reasonable to force internet intermediaries to intervene, using blocking measures that also elevate the risk of unintended consequences and collateral damage.

With blocking demands moving towards a ‘real time’ requirement as standard, increasingly unsupervised blocking exposes third parties to a risk of becoming collateral damage in a war that already transcends national borders.

With no requirement to report incidents of overblocking, and third party claims routinely dismissed as unsubstantiated hearsay, the findings of a new study focused on Italy’s Piracy Shield platform provides an opportunity for reflection.

The peer-reviewed study reveals that broad-scope blocking significantly disrupts legitimate online services, renders IP address space unusable, undermines the operation of legitimate businesses, while posing a broader systemic risk encompassing national infrastructure.

## Piracy Shield: Collateral Damage and Efficacy

The credentialed authors of the [study](https://research.utwente.nl/en/publications/90th-minute-a-first-look-to-collateral-damages-and-efficacy-of-th), *90th Minute: A First Look to Collateral Damages and Efficacy of the Italian Piracy Shield* are [Raffaele Sommese](https://academia.r4ffy.info/), [Anna Sperotto](https://annasperotto.org/), [Jeroen van der Ham](https://www.jvdham.nl/), and [Antonia Affinito](https://people.utwente.nl/a.affinito) at the University of Twente, Netherlands, and [Antonio Prado](https://www.prado.it/), an independent consultant in Italy.

Motivated by the aggressive piracy countermeasures of Italy’s Piracy Shield, related collateral damage, and a lack of empirical data on the platform’s real-world impact, the study aims to provide the first data-driven investigation into the platform’s efficacy and unintended consequences.

## Obtaining Data, Understanding Blocked Resources

In an environment that the researchers describe as favoring “enforcement efficiency over full transparency” access to relevant official data was an immediate challenge. Resources blocked by Piracy Shield are not published by telecoms regulator AGCOM and an unofficial list of blocking tickets available via ISP Infotech appear only in redacted form.

![piracy shield tickets1](https://torrentfreak.com/images/piracy-shield-tickets1.png)
A Piracy Shield dataset leaked to GitHub, containing ~11,000 IP addresses and ~42,600 fully qualified domains (FQDN), provides the foundation for the study.

Of these domains, 18,849 (44.2%) were confirmed as still blocked, while 23,805 (55.8%) had been removed. Verified by the researchers as authentic after cross-referencing with Infotech data, the same dataset was independently reviewed by TorrentFreak in 2024 and is considered reliable.

Identification of the blocked resources and exploration of their characteristics, allowed the researchers to evaluate ownership, operational control, while inferrinng hosting and leasing activity; i.e IP addresses likely to belong to leased address space.

The researchers leveraged data provided by [OpenINTEL](https://openintel.nl/) to identify domains either hosted on blocked IP addresses or referring – via CNAME records – to blocked FQDNs. They also conducted their own scan of 1.8 billion FQDN extracted from Certificate Transparency logs to identify shared infrastructure and potential collateral damage.

## Distribution of Blocked IPs and FQDNs

From February 2, 2024 to June 4, 2025, a total of 3,782 blocking requests (tickets) were issued to the Piracy Shield platform. Of those, 1,817 (48%) tickets targeted at least one FQDN and one IPv4 address, 1,719 (45%) targeted only FQDNs, and 246 (7%) targeted only IP addresses. The distribution of blocked IP addresses per country and FQDN per TLD are shown in the tables below:

*EU IP Addresses Dominate*

![Piracy_Shield_study_1](https://torrentfreak.com/images/Piracy_Shield_study_1.png)

Table II shows that 37.9% of the IP addresses blocked by Piracy Shield are hosted in the Netherlands followed by Germany (9.0%) and Romania (8.2%), with a relatively modest 843 IP addresses (7.7&) located to the United States.

“Interestingly, 2.5% of the blocked IPs are located in Italy, and 76.8% of the blocked IPs are within the European Union, where copyright owners may have better leverage to identify illegal streaming perpetrators and take them down,” the researchers note.

Distribution across the top 15 hosting infrastructures for the 10,918 IP addresses, by company, /24 networks (2,134 overall), and ASN (262 overall), is shown in the table below. *(Note: As referenced in the study, a ‘/24 network’ is a Class C IPv4 network supporting 254 hosts)*

![Piracy_Shield_study_2](https://torrentfreak.com/images/Piracy_Shield_study_2.png)

“Interestingly, a single company – GZ Remittance— hosted more than 9.5% of all blocked resources, concentrated in just 15 distinct /24s. This may suggest that the company is highly favored by illegal streaming operators, who likely rotate through IPs to evade blocking. The same pattern is observable for NexonHost, which shows similar figures,” the study notes.

“OVH stands out for having the highest number of unblocked IPs – 41 in total, accounting for almost one third of all unblocked addresses. This suggests that shared resources may have been inadvertently affected, or that the infrastructure was later reused for benign purposes.”

## IP Addresses and Leased Address Space

The researchers observed that of the 10,918 blocked IP addresses, 2,618 (24%) were linked to leased address space. This is significant; leased address space can be used as an evasion tactic and could lead to collateral damage when ‘pirate’ leases expire and IP addresses are made available under a new lease.

The study found that, on average, 7.5 IP addresses per /24 were blocked in leased address blocks, compared to just 4.5 IP addresses per /24 in non-leased blocks. This suggests that some pirates prefer leased address space, leading to potential collateral damage when blocked IP addresses are reassigned under a new lease. Interestingly, 453 IP addresses were leased for the first time *after* being blocked, signaling major Italian connectivity issu...