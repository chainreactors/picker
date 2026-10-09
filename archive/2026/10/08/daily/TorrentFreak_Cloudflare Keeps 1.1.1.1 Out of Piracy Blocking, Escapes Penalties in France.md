---
title: Cloudflare Keeps 1.1.1.1 Out of Piracy Blocking, Escapes Penalties in France
url: https://torrentfreak.com/cloudflare-keeps-1-1-1-1-out-of-piracy-blocking-escapes-penalties-in-france/
source: TorrentFreak
date: 2026-10-08
fetch_date: 2026-10-09T08:12:22.735746
---

# Cloudflare Keeps 1.1.1.1 Out of Piracy Blocking, Escapes Penalties in France

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

# Cloudflare Keeps 1.1.1.1 Out of Piracy Blocking, Escapes Penalties in France

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Lawsuits](https://torrentfreak.com/category/lawsuits/ "Go to the Lawsuits category archives.") >

Cloudflare doesn't block pirate sports streaming sites through its 1.1.1.1 DNS resolver in France, only through its CDN. The Paris Judicial Court has now accepted that stance, rejecting Canal+'s request for penalties of €50,000 per site, per day. Interestingly, the court's conclusion relies on statistics provided by Canal+ itself.

![cloudflare 1.1.1.1 logo](https://torrentfreak.com/images/1111-logo-600x294.png)Over the past two years, French courts have ordered a growing list of intermediaries to block access to pirate sports streams.

In addition to regular ISPs, the orders now target public DNS resolvers, VPN services, search engines and CDN providers, all of which can help people bypass existing blockades.

Internet infrastructure company Cloudflare has received several of these orders. [In April](https://torrentfreak.com/eu-funded-dns-provider-must-block-pirate-sites-french-court-rules/), the Paris Judicial Court ordered the company to block 21 domains linked to pirate Formula 1 streams and 16 linked to MotoGP.

The orders covered Cloudflare’s DNS resolver as well as its CDN. However, they didn’t prescribe how the sites should be blocked, only that access from France had to be prevented “by any effective means.”

French pay-TV provider Canal+, which requested the blockades, concluded that Cloudflare’s efforts fell short. The broadcaster went back to court and, as first reported by [L’Informé](https://www.linforme.com/tech-telecom/article/piratage-sportif-cuisant-echec-de-canal-face-a-cloudflare_9405.html), it didn’t get what it wanted.

## Canal+ Requested €50,000 a Day

In May, Canal+ asked the Paris court to add daily penalties to the April orders. It requested €50,000 per day for every site that remained accessible, and the same amount for every new site that media regulator Arcom reports to Cloudflare.

*From the order (translated)*
![50k requested by canal+](https://torrentfreak.com/images/50k.png)

According to Canal+, Cloudflare had deliberately failed to comply with the site blocking orders.

“[Cloudflare] allegedly circumvented the measures by only implementing the decision through its CDN service, which meant that only three of the 21 domain names listed by the court were blocked,” Canal+ argued, according to the court’s summary (translated).

In the MotoGP case, Canal+ counted three blocked domains out of 16. In both cases, it added that two of the three blocked sites were back online a week later; one switched to a different CDN, while the other used a mirror site.

## Court Sides With Cloudflare

On September 17, a panel of three judges ruled on both penalty requests. Cloudflare had pointed to technical constraints that only allowed it to comply through its CDN. It also stressed that the court had expressly left it free to choose which of its services to use, as long as it contributed meaningfully to the fight against sports piracy.

The court first noted that the way Cloudflare implements the blocking orders is not in dispute.

“It is undisputed that Cloudflare only implements the ordered measures by blocking through its CDN service, when the site uses that service,” the court writes (translated).

*CDN only*
[![CDN only](https://torrentfreak.com/images/shot-cloudflare-cdn-only.png)](https://torrentfreak.com/images/shot-cloudflare-cdn-only.png)

Cloudflare told the court that this is incomparably more effective than DNS blocking. It added that the architecture of its public DNS resolver doesn’t allow for blocking, making such measures unreasonable.

Canal+ had argued that Cloudflare only blocked 72.6% of the domain names the court ordered it to block. The court, however, saw the figure as evidence of a genuine willingness to help stop the infringements.

The ruling doesn’t explain how this percentage relates to the three out of 21 blocked domains that Canal+ cited earlier.

The court also concluded that Cloudflare can’t be blamed for the sites that switched to another CDN or moved to a mirror.

“Cloudflare cannot be held responsible when the owners of the sites in question switch to another CDN or set up a redirect to a mirror site,” the court writes (translated).

*Not Cloudflare’s responsibility*
[![Not Cloudflare's responsibility](https://torrentfreak.com/images/shot-cloudflare-not-responsible.png)](https://torrentfreak.com/images/shot-cloudflare-not-responsible.png)

Instead, it is up to Canal+ to ask the new intermediary to block these sites and to report mirror sites to Arcom, the court notes.

Canal+ also argued that, under the EU Court of Justice’s [UPC Telekabel Wien](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62012CJ0314) ruling, intermediaries must block effectively. The Paris court disagreed. In its view of the same ruling, intermediaries only have to take reasonable measures, which Cloudflare did with its CDN blocks.

The court therefore rejected the requested penalties as neither necessary nor proportionate. In addition, Canal+’s request for €20,000 in legal costs was also denied.

## 1.1.1.1 Stays Block-Free

As a result, Cloudflare will not be penalized under these orders, even though its public DNS resolver is not blocking the sites in question. That is in line with the company’s long-standing claim that it doesn’t interfere with its DNS.

In its recent transparency reports, Cloudflare [repeatedly stated](https://torrentfreak.com/cloudflare-blocked-400-sports-piracy-domains-in-france-last-year-250303/) that it hasn’t blocked any content through 1.1.1.1, despite orders from French and Italian courts.

“To date, Cloudflare has not blocked content through the 1.1.1.1 Public DNS Resolver,” the company’s [latest report](https://cfl.re/h2-2025-transparency-report-abuse) reads.

*From Cloudflare’s transparency report*

![transparency report 1.1.1.1 not blocked](https://torrentfreak.com/images/transparency-notblocked.png)

Blocking through the CDN is another matter. According to the same report, Cloudflare geoblocked 1,238 domains in France in the second half of 2025, all under a single court order. In the first half of the year, it geoblocked 662 domains under seven orders.

Cloudflare recently explained its position to the European Commission, in a [submission](https://torrentfreak.com/images/Cloudflare_response_to_2027_EU_Watch_List_consultation.pdf) to its Counterfeit and Piracy Watch List consultation, stressing that global public DNS resolvers should not be used to block or restrict access.

Instead, it highlights its real-time pirate stream blocking program, which allows vetted rightsholders to flag pirate streams that run through its network. These streams are disrupted “within seconds,” Cloudflare says, without any DNS or IP address blocking.

“For live content, where speed is crucial, Cloudflare has built real-time mitigation mechanisms that allow vetted rightsholder partners to flag infringing streams. When those streams are running through ou...