---
title: Quad9 Exits France as Expired Piracy Order Lingers at Google and ISPs
url: https://torrentfreak.com/quad9-exits-france-as-expired-piracy-order-lingers-at-google-and-isps/
source: TorrentFreak
date: 2026-11-24
fetch_date: 2026-11-25T10:48:29.136088
---

# Quad9 Exits France as Expired Piracy Order Lingers at Google and ISPs

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

# Quad9 Exits France as Expired Piracy Order Lingers at Google and ISPs

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Law and Politics](https://torrentfreak.com/category/law-politics/ "Go to the Law and Politics category archives.") >

As of this morning, DNS resolver Quad9 no longer serves users in France. The exit comes after a Paris court ordered it to block pirate tennis streams, which it refused to do. The blocking order behind that ruling expired when the WTA season ended ten days ago. Most of the blocks have since been lifted, but not all of them.

![frexit](https://torrentfreak.com/images/french-announcement-image-600x600.png)Last month, DNS resolver [Quad9](https://quad9.net/) [announced](https://torrentfreak.com/dns-resolver-quad9-will-leave-france-after-court-orders-piracy-blocking-penalty/) that it would leave France, after losing a legal battle against beIN Sports.

The Paris court imposed a penalty of €1,000 a day, which ran until November 14, when the blocking order expired at the end of the WTA tennis season. Quad9’s exit, however, went ahead as planned.

## Service Unavailable

From this morning, Paris time, French users of the Swiss foundation’s DNS resolver no longer get answers. We confirmed this through probes in France shortly after 09:00.

*Service unavailable due to French legal constraints*

![refused](https://torrentfreak.com/images/refused.png)

Quad9 told us that it answers queries from France with a refusal. The response includes extended DNS error code 18, which is labeled “Prohibited” under DNS standards, as well as a short note pointing to the legal situation in France.

Most people will never see these details, as web browsers don’t display them. For regular users, DNS lookups through Quad9 simply stop working.

The Internet doesn’t have physical borders, so Quad9 relies on a GeoIP database to decide who is in France. The foundation believes that data is good, but notes that it will be imperfect. Some users outside France will be refused, and some French users will slip through.

VPN use will also impact its blocking. A French user connected to a VPN server in Helsinki will still get answers, while a user in Kenya who connects through a French VPN server is refused. People who believe they are blocked by mistake can contact Quad9’s support team, which will then adjust its list.

The foundation has also posted a notice on its [status page](https://uptime.quad9.net/maintenance/1131466), titled “Quad9 No Longer Serving French Users as of November 24, 2026.”

*Maintenance*
[![Quad9 status page](https://torrentfreak.com/images/quad9-maintenance.png)](https://torrentfreak.com/images/quad9-maintenance.png)

While the tennis order may have expired, beIN’s case was never Quad9’s only concern. The foundation [previously said](https://quad9.net/news/blog/au-revoir-france/) that it can’t survive the penalties that may follow from roughly 20 other pending blocking cases in France.

Quad9 sees leaving France as the least bad option it had.

## No Censorship Tool

The exit means that French users who never watched a pirated match lose their resolver, while an imperfect block of the listed domains would have hit far fewer people. We asked why the foundation prefers this option nonetheless, which touches on the core values of its operation.

“Because Quad9’s mission is to protect users from harm, not to guard private companies from outcomes they do not want,” Todd says. “We do not wish to be complicit in building the tools of censorship.”

Quad9 sees DNS filtering as a distraction in any case, as it does nothing to stop the source of the pirate streams.

Quad9 calculates that the penalty could reach €24,000. There is no official demand for payment yet, the foundation told us, and court delays mean it may be some time before one arrives.

## Partly Unblocked

Earlier this month, we [took a closer look](https://torrentfreak.com/inside-a-french-piracy-blocklist-expired-domains-a-seized-site-and-hong-kong-servers/) at the blocklist behind beIN’s order, which had grown to 118 domains. After the order expired, we checked all of them again on Monday, through a French VPN server.

Most of the blocks are gone, which shows that blocks do get lifted after an order expires, at least at Google and NordVPN

Google’s DNS resolver now blocks 22 of the 118 domains, down from 91 on October 28. NordVPN’s resolver blocks 20, down from 89, while Cloudflare’s 1.1.1.1 still blocks none.

*Blocked by Google DNS in France, by batch*

| Reported to Lumen | Domains | Blocked (Oct 28) | Blocked (Nov 23) |
| --- | --- | --- | --- |
| May 13 (court order) | 6 | 6 | 6 |
| June 15 | 22 | 22 | 8 |
| September 21 | 30 | 30 | 3 |
| October 16 | 30 | 30 | 2 |
| October 26 | 30 | 3 | 3 |
| **Total** | **118** | **91** | **22** |

The six domains in the original (now expired) court order are all still blocked. Google’s error message links to a notice that was filed on behalf of beIN Sports in June, under the case number of the tennis order (RG 26/02207).

*beIN’s notice*
[![beIN's notice](https://torrentfreak.com/images/lumennotice.png)](https://torrentfreak.com/images/lumennotice.png)

None of the remaining Google blocks refer to the Arcom notices that added the later batches to the tennis order. The other 16 domains point to different notices. The two we checked were filed on behalf of Arcom under other court orders, one of them on November 13, the day before the tennis order expired.

Our two research domains clearly show the split. Google now resolves rktv.top, which was added in the June batch. ap-live.top, one of the six domains in the court order, is still refused.

“The requested domain is subject to a judicial injunction or other governmental blocking order for FR,” Google’s response reads.

*Blocked and unblocked*
[![Blocked and unblocked](https://torrentfreak.com/images/shot-google-dns-pair.png)](https://torrentfreak.com/images/shot-google-dns-pair.png)

Why Google still applies beIN’s notice to the six domains in the original order is unclear.

## ISPs Go Their Own Way

French ISPs don’t follow the same schedule. Earlier this month, Bouygues Telecom and Free redirected rktv.top to [offrelegalesports.fr](https://www.offrelegalesports.fr/), a page that links visitors to licensed sports broadcasts. SFR’s business provider Completel did the same.

When we tested the ISP resolvers on Monday, these redirects were gone.

Orange, however, blocks ap-live.top on most of the resolvers we tested, answering with 127.0.0.1 or reporting that the domain doesn’t exist. One Orange resolver also still blocks rktv.top.

The other ISP resolvers we tested are inconsistent. Most answer normally for both domains, but some still block ap-live.top, and one gave no answer at all.

For now, our research domain ap-live.top remains blocked by Google and several French ISP resolvers, a month after we registered it. Arcom did not respond when we asked whether a new owner can get a listed domain removed.

## A Comeback?

The pirate domains that made up most of the list, meanwhile, haven’t gone anywhere. The 74 domains that pointed to two Hong Kong IP addres...