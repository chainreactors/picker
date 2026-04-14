---
title: Paris Court Issued Simultaneous Site Blocking Orders Against ISPs, DNS Resolvers and VPNs
url: https://torrentfreak.com/paris-court-issued-simultaneous-site-blocking-orders-against-isps-dns-resolvers-and-vpns/
source: TorrentFreak
date: 2026-04-13
fetch_date: 2026-04-14T04:46:00.618221
---

# Paris Court Issued Simultaneous Site Blocking Orders Against ISPs, DNS Resolvers and VPNs

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

# Paris Court Issued Simultaneous Site Blocking Orders Against ISPs, DNS Resolvers and VPNs

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Lawsuits](https://torrentfreak.com/category/lawsuits/ "Go to the Lawsuits category archives.") >

In a series of simultaneous rulings, the Paris Judicial Court ordered ISPs, VPN providers, and DNS resolvers to block access to 35 sports piracy sites. The orders were requested by Spanish football league LaLiga, which lacked standing as a foreign entity under French law. LaLiga licensee beIN Sports France had to intervene in the cases and secure the blocks in its own name.

![justice](https://torrentfreak.com/images/justice-statue.jpg)

The initial order required [Cloudflare, Google, and Cisco](https://torrentfreak.com/court-expands-google-and-cloudflare-dns-blocking-to-combat-piracy-241125/) to actively block access to pirate sites through their own DNS resolvers, confirming that third-party intermediaries can be required to take responsibility. Not much later, [VPN providers were added](https://torrentfreak.com/french-court-orders-vpns-to-block-more-pirate-sites-rejects-eu-court-referral/) to the blocking roster.

Initially, these orders were to address circumvention techniques for domains that were already blocked through ISPs. The DNS resolver and VPN provider blockades limited these loopholes. Several blocking orders have followed since, but a series of orders that came out at the Paris Judicial Court take a different approach.

On March 18, Judge Jean-Christophe Gayet issued seven simultaneous rulings, targeting a broad range of online intermediaries that enable access to pirate sports streams in France. The cases were filed by the Spanish professional football league LaLiga, which requested blocking measures against 35 domain names of sports streaming sites.

The pirate sites listed include librefutboltv.su, which has over 27 million monthly visits, as well as smaller ones such as tflix.live, daddylive.dad, yallashooot.video, ballcontrol.click, and kora-live.im.

The targeted intermediaries span every layer of the technical stack: this includes major French ISPs, alternative DNS resolvers such as Google, Cloudflare, and Quad9, as well as several of the world’s largest VPN providers.

## Court: LaLiga Lacks Standing

Interestingly, however, LaLiga was not victorious in court. In each of the seven cases, the court declared the league’s claims inadmissible.

The court explained that, under [Article L. 333-10](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044247629/) of the French Sports Code, the right to bring blocking injunctions applies to rightsholders, broadcasting companies, and professional sports leagues. However, the court interprets that last category narrowly.

To qualify for protection, sports leagues must be created by a state-delegated federation under French law, specifically under Articles L. 131-14 and L. 132-1 of the Sports Code. As a Spanish association with no delegation from the French state, LaLiga does not meet that definition.

LaLiga argued that the law should also cover foreign leagues that commercialize their audiovisual rights, and that reading it otherwise would discriminate against non-French rights holders. However, the court rejected these arguments.

The restriction has nothing to do with LaLiga’s nationality, the court noted; the league simply needs a subdelegation from the French state to qualify for protection via site-blocking orders. Additionally, the court concluded that LaLiga is not directly harmed by piracy in France, as it assigned its exclusive French broadcast rights to beIN Sports France.

This same reasoning applied to all seven cases and initially appears to be a major setback for the football league. However, help was just around the corner.

## beIN Sports Steps In

[beIN Sports France](https://www.beinsports.com/fr-fr), which holds exclusive broadcast rights to LaLiga in France as part of a deal with the Spanish league, intervened voluntarily in all seven cases.

As the company that acquired exclusive French broadcasting rights for LaLiga, it qualifies under the second category in Article L. 333-10. Unlike LaLiga, beIN could also point to documented harm, including evidence that 35 disputed domain names were streaming LaLiga matches, with beIN Sports branding visible in the pirate feeds.

The court ultimately concluded that there was grave and repeated infringement of beIN Sports France’s exclusive rights in all seven cases and granted the blocking orders in its name.

## Blocking The Full Stack

What further stands out is the fact that these orders all came out on the same day, targeting nineteen French ISPs, three DNS resolvers, a CDN provider, and four VPN services. This broad approach ensures that the most popular circumvention options are immediately cut off.

The orders run until June 21, 2026, and are also dynamic in nature. This means that new domain names can be added in the future, once they are approved for blocking by France’s audiovisual regulator, ARCOM.

The **ISP order** will have the most direct impact. It includes France’s largest providers, such as Orange, SFR, Free, and Bouygues Telecom, as well as various smaller ones.

If subscribers try to circumvent these blocking measures by switching to alternative DNS resolvers, orders against **Google**, **Cloudflare**, and **Quad9** will prevent this.

VPN providers are not necessarily an option either, as the court granted blocking orders against **ProtonVPN**, as well as **CyberGhost** and **ExpressVPN**. LaLiga also [referenced orders against](https://www.laliga.com/noticias/laliga-y-bein-sports-france-obtienen-siete-resoluciones-judiciales-de-alto-valor-en-francia-contra-la-pirateria) NordVPN and Surfshark jointly, but TorrentFreak was unable to locate these.

The Cloudflare order is the most technically comprehensive of the batch. It covers not only Cloudflare’s public DNS resolver but also its CDN, reverse proxy service, and WARP service under a single ruling. The court requires Cloudflare to block the domains across its infrastructure, by whatever technical means it chooses.

Some of the defendants raised counterarguments in court. For example, several VPN providers argued that Article L. 333-10 conflicts with the EU E-Commerce Directive, while others sought a referral to the Court of Justice. However, none of these arguments convinced the court.

## Site Blocking Evolution

The seven court orders represent the most comprehensive single-day blocking action under France’s sports piracy framework, as far as we know. Whereas initial orders targeted single intermediary categories, these come in one full sweep.

LaLiga president Javier Tebas is pleased with the outcome and thanks beIN for their cooperation.

“These rulings represent a significant step forward because they extend protection to the entire technical ecosystem that piracy currently relies on. The fight against audiovisual fraud must grow through collaboration, as is the case here with beIN Sports France, which has been key to developing a solid and effective defense in the French market,” T...