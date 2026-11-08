---
title: Inside a French Piracy Blocklist: Expired Domains, a Seized Site, and Hong Kong Servers
url: https://torrentfreak.com/inside-a-french-piracy-blocklist-expired-domains-a-seized-site-and-hong-kong-servers/
source: TorrentFreak
date: 2026-11-07
fetch_date: 2026-11-08T08:14:53.460714
---

# Inside a French Piracy Blocklist: Expired Domains, a Seized Site, and Hong Kong Servers

[![](https://torrentfreak.com/wp-content/themes/torrentfreak/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/torrentfreak/build/assets/img/search.svg)

* News
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/torrentfreak/build/assets/img/x.svg)

# Inside a French Piracy Blocklist: Expired Domains, a Seized Site, and Hong Kong Servers

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Opinion Articles](https://torrentfreak.com/category/opinion/ "Go to the Opinion Articles category archives.") >

In May, a Paris court ordered DNS resolvers to block six domains that streamed pirated tennis matches. After a series of quiet, unannounced expansions, the list has since grown to 118. This includes two domain names that now belong to TorrentFreak. Notably, no domain names have been taken off the list, not even one that was seized by the U.S. Government months ago.

![a stale and old croissant](https://torrentfreak.com/images/croissant-600x368.png)On October 22, DNS resolver [Quad9](https://quad9.net/) [announced](https://torrentfreak.com/dns-resolver-quad9-will-leave-france-after-court-orders-piracy-blocking-penalty/) that it will stop serving users in France, after a Paris court ordered it to block pirate tennis streams or pay a daily penalty.

The underlying order, which [beIN Sports](https://www.beinsports.com/fr-fr) obtained in May, initially listed six domains. That number has since grown considerably, with the latest additions coming in late October.

To take a closer look at the evolution of this blocklist, we compiled it from the notices that Google files with the [Lumen database](https://lumendatabase.org/) when it receives a blocking order. Today, [118 domains](#blocked) are listed under this order.

## From 6 to 118 Domains

The pirate site blocklist, which is one of many in France, expanded in batches. The first update, reported by Google on June 15, added 22 domains. Three more updates followed on September 21, October 16 and October 26, each adding exactly 30.

*The blocklist [snapshot](#snapshot), batch by batch*

| Reported to Lumen | Domains added | Running total | Blocked by Google DNS in France (Oct 28) | Blocked by Cloudflare DNS in France (Oct 28) |
| --- | --- | --- | --- | --- |
| May 13 (court order) | 6 | 6 | 6 | 0 |
| June 15 | 22 | 28 | 22 | 0 |
| September 21 | 30 | 58 | 30 | 0 |
| October 16 | 30 | 88 | 30 | 0 |
| October 26 | 30 | 118 | 3 | 0 |

Nothing appears to have been taken off the list. The notices only add domains, and the ones that no longer work were still blocked when we checked. The blocking measures remain in effect until November 14, when the WTA tennis season ends.

Transparency is limited and it’s hard for the public to see what is blocked and on what grounds. [Arcom](https://www.arcom.fr/) doesn’t publish blocking updates. Google’s Lumen notices are the only public record we found, and they take some digging. The later notices don’t mention the case number, so a [search for the order](https://lumendatabase.org/notices/search?term=%2226%2F02207%22&sort_by=) only turns up the first few, and the full domain lists are only shown to people who request access from Lumen.

This example shows the value of the [Lumen Database](https://lumendatabase.org/) when governments or courts don’t provide transparency.

Quad9 didn’t block any of the domains before the court ruled on the penalty on October 21, according to the ruling, which records the foundation’s statement to that effect and beIN’s objections to it.

## Expired Domains, Seized Site

ISPs, online intermediaries, lawmakers and rightsholders all have different views on the effectiveness and proportionality of site blocking. However, logically speaking, all should agree that there is no need to block a domain that no longer links to anything infringing. That’s not necessarily what happens.

We checked all 118 domains on October 28, from the Netherlands and through a French server. Most still resolve to an IP address. However, the exceptions are more interesting.

Four domain names no longer resolve at all. Two of these, predb.click and line.golden-iptv.in, aren’t registered anymore; the latter was one of the six domains in the original court order. Meanwhile, 4kib.xyz has been suspended by its registrar, and fermin37.com stopped working after we first checked it on October 23.

Another domain, fr4.sportplus.live, now loads [a page titled](http://fr4.sportplus.live/) “THIS DOMAIN HAS BEEN SEIZED”. Its main domain was among the pirate sports domains that U.S. authorities [seized in July](https://torrentfreak.com/u-s-seizes-more-pirate-sports-streaming-domains-but-iranian-fallbacks-remain/).

*Seized globally, blocked in France*

![seizure banner](https://torrentfreak.com/images/seized-small.png)

The mgntv-nexon.xyz domain, meanwhile, points to an IP address that belongs to domain marketplace [Sedo](https://sedo.com/).

In France, none of this makes a difference. Google’s DNS resolver blocks 91 of the 118 domains and NordVPN’s DNS blocks 89, dead names and all. The domains that aren’t blocked yet mostly come from the latest batch; only three of those 30 were blocked on October 28, two days after Google reported them. The exception is Cloudflare, whose 1.1.1.1 resolver blocks nothing. Cloudflare applies French blocking orders through its CDN instead, which a Paris court [accepted as a reasonable effort](https://torrentfreak.com/cloudflare-keeps-1-1-1-1-out-of-piracy-blocking-escapes-penalties-in-france/) in September.

We know all this because we looked at the DNS responses directly. Users that try to access these sites through a browser have no idea what is going on. They simply see an error message noting that the site can’t be reached. That also applies to rktv.top, which TorrentFreak owns today.

*Browser error*
![browser error, dns not resolved](https://torrentfreak.com/images/dns-error.png)

## Under New Ownership

On October 23, two names on the list were free to register for anyone, as they had expired. These are [rktv.top](http://rktv.top/), which was added to the blocklist in June, and [ap-live.top](http://ap-live.top), one of the six domains in the court order itself.

We registered both domains and put up a short page on each, stating that TorrentFreak owns the domain for research and that it doesn’t offer, link to, or promote any streaming service. That’s all.

*TorrentFreak’s Research domain*

![torrentfreak registered http://rktv.top/](https://torrentfreak.com/images/tf-registered.png)

From the Netherlands, this page loads as expected. In France, however, Google refuses to resolve rktv.top. “The requested domain is subject to a judicial injunction or other governmental blocking order for FR,” its DNS response reads. The response carries extended error code 16, which the DNS standard labels “Censored”.

*Blocked in France*
[![Blocked in France](https://torrentfreak.com/images/shot-google-dns-rktv.png)](https://torrentfreak.com/images/shot-google-dns-rktv.png)

Some French ISP resolvers go a step further and redirect the DNS response. When we queried rktv.top through Bouygues Telecom and Free, the answer wasn’t a refusal but [a different IP address](https://globalping.io?measurement=2Hlt3pzLtO40tZKhN00021SFc), 54.246.190.12, which serves [offrelegalesports.fr](https://www.offrelegalesports.fr/), a page that links visitors to licensed sports broadcasts. Completel, a bus...