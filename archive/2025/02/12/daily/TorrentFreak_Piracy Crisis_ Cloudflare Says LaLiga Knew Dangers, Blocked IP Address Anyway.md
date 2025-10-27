---
title: Piracy Crisis: Cloudflare Says LaLiga Knew Dangers, Blocked IP Address Anyway
url: https://torrentfreak.com/spain-piracy-crisis-cloudflare-says-laliga-knew-danger-blocked-ip-address-anyway-250211/
source: TorrentFreak
date: 2025-02-12
fetch_date: 2025-10-06T20:57:16.440598
---

# Piracy Crisis: Cloudflare Says LaLiga Knew Dangers, Blocked IP Address Anyway

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

# Piracy Crisis: Cloudflare Says LaLiga Knew Dangers, Blocked IP Address Anyway (Update)

February 11, 2025 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

Unexplained chaos at ISPs Movistar and DIGI has prevented some customers from accessing many sites using Cloudflare for over a week. Simultaneously, football league LaLiga stated they are working to shut down pirate streaming platforms, warning Cloudflare and others that they consider them responsible for profiting from piracy. Since statements now link these two events, Spain has a crisis on its hands.

![football block](https://torrentfreak.com/images/football-block.png)

In time, those who protested the loudest were the ones dismissed as deluded. Their warnings, that handing internet blocking powers to rightsholders would eventually end in disaster, were subsequently dismissed by governments and national courts all around Europe. Politicians often dismissed these concerns, citing safeguards and suggesting such problems were impossible.

If the events of the past week are connected, as the evidence suggests, Spain faces a significant problem. While some may call for intervention to de-escalate the situation, this could be a missed opportunity to address the underlying issues.

## A Week of Disruption at ISPs

To prevent piracy, Spain’s top football league LaLiga has permission from the courts to compel ISPs, including Movistar and DIGI, to block access to pirate sites. For roughly a week, customers of Movistar and DIGI have been complaining that seemingly random sites were refusing to load for no obvious reason. Tests conducted on mobile phones, however, showed no problems.

Some pointed out that Cloudflare might be the root of the problem, since the platform had been identified as the common denominator in all instances of sites refusing to load. That claim also faced challenges. Cloudflare was working just fine for some sites, but not for others. A growing consensus suggested that the problems only affected a specific Cloudflare IP address or addresses.

The situation was worsened by the ISPs’ apparent lack of information; they provided no useful responses about the cause of the problems or when they might be resolved. These telecommunications companies depend on their ability to provide communication services. The suggestion that they were unaware of the cause is highly unlikely.

Unconfirmed reports indicate that some complaining customers were given additional mobile data to access the blocked sites. As compensation for a technical issue, that might work. In reality, the ISPs likely knew more than they were giving away.

## Cloudflare Customers Also Affected

In parallel, Cloudflare customers were reporting similar issues; more specifically, Cloudflare customers who are also customers of Movistar, or Cloudflare customers who run websites that customers of Movistar could no longer visit.

![cloudflare-spain](https://torrentfreak.com/images/cloudflare-spain.png)

With no (initial) official response or announcement from Cloudflare, sysadmin @jaumepons posted a [link](https://x.com/jaumepons/status/1888711866937172052) on X showing how a tracert (or traceroute) launched from over 200 locations in Spain, from different operators, revealing significant issues with two specific ISPs.

“I leave you here a tracert to a Cloudflare IP launched from 230 different points in the country, from different operators. Then you go to “Results”, sort by operator “ASN” and you will see what those from @movistar are doing, and also @digimobil\_es,” @jaumepons wrote.

![Tracert](https://torrentfreak.com/images/PcanmfsHNB.png)

Those interested are invited to [check for themselves](https://atlas.ripe.net/measurements/86812634/results) but the stream of red crosses in the ‘SUCCESS’ column shows that [AS3352](https://bgpview.io/asn/3352), registered to Movistar parent company Telefonica, had major connectivity problems. The fact that these issues did not affect all Cloudflare IP addresses complicated the situation but also strengthened suspicions of IP address blocking.

## LaLiga ‘Deactivates’ DuckVision

When enforcement action shuts down pirate sites in the physical world, press releases tend to reference towns, cities, the number of officers involved, potentially the arrests of those who operate them, plus any evidence seized in the operation. When less typical words are used to describe a site’s demise, it’s worth considering whether ambiguity serves any purpose.

In an announcement published on the LaLiga website late Sunday, the country’s top football league led with the headline below.

*Image credit: [LaLiga](https://www.laliga.com/noticias/laliga-desactiva-antes-del-derbi-de-madrid-la-plataforma-de-pirateria-de-vivo-duckvision)*

![laliga-duckvision](https://torrentfreak.com/images/laliga-duckvision.png)

“LALIGA remains committed to fighting against audiovisual fraud and the consumption of illegal content through various initiatives and legal actions,” the announcement began.

“Now, thanks to the coordination of a specialized team, LALIGA has managed to deactivate DuckVision with immediate effect. This is a pirate platform that offered illegal access to live sports content, including the Spanish competition, to more than 200,000 people in Spain alone.”

## Deactivate

The decision to use the word ‘deactivate’ rather than ‘shut down’ gains relevance when, seemingly out of nowhere, Cloudflare finds itself mentioned in the same breath.

“DuckVision consisted of a web application that invited people to download an Android app that had more than 200,000 active users in Spain during the month of January 2025, according to data.ai, and was covered by the service of the American technology company Cloudflare, which intentionally protects criminal organizations in order to make a profit.”

In the absence of ISPs making a clear statement, and previous comments that Cloudflare’s protection can’t be beaten, we can assume that DuckVision was dealt with differently. It wasn’t shut down, clearly, but it was ‘deactivated’ which sounds like a euphemism for blocking measures.

A less ambiguous statement wouldn’t have been difficult to put together. However, a reasonable person might get the impression that, since Cloudflare is considered part of the problem, and DuckVision’s IP addresses were successfully protected by Cloudflare, the only way to “deactivate” DuckVision was to block Cloudflare IP addresses.

While offering a potential explanation for the woes at Movistar, this theory still lacks confirmation that the two events are connected in any way. Or at least that was the case; not any more.

## Telefonica, Movistar, and Cloudflare Break Silence

After declining [Xataka’s](https://www.xataka.com/servicios/movistar-o2-estan-provocando-muchos-problemas-quejas-sus-clientes-te-contamos-que-sabemos-como-solucionarlo) request to explain connectivity problems at Movistar, Telefonica...