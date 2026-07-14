---
title: U.S. Seizes More Pirate Sports Streaming Domains, But Iranian Fallbacks Remain
url: https://torrentfreak.com/u-s-seizes-more-pirate-sports-streaming-domains-but-iranian-fallbacks-remain/
source: TorrentFreak
date: 2026-07-13
fetch_date: 2026-07-14T04:48:23.694468
---

# U.S. Seizes More Pirate Sports Streaming Domains, But Iranian Fallbacks Remain

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

# U.S. Seizes More Pirate Sports Streaming Domains, But Iranian Fallbacks Remain

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Piracy](https://torrentfreak.com/category/piracy/ "Go to the Piracy category archives.") >

The U.S. continues to crack down on sports streaming sites, seizing well over a hundred additional domain names this weekend. While these enforcement actions sorted effect, several of the targeted domains now use fallback domains on Iran's .ir country-code TLD, which might be harder to reach for American law enforcement.

![ballnetblock](https://torrentfreak.com/images/ballnetblock-600x445.jpg)With the FIFA World Cup nearing its conclusion this week, the crackdown on sports streaming sites continued this weekend.

As part of the “[Operation Offsides](https://torrentfreak.com/feds-seize-domain-names-of-nearly-400-pirate-sports-streaming-sites/)” enforcement action, led by U.S. authorities, more than 100 domain names were seized over the past days.

These new seizures came more than two weeks after the U.S. Department of Justice officially announced the action. While no new announcement was released, the recent seizures in part target fallback domains that pirate sites switched to following the initial crackdown.

For example, when the buffstreams.plus domain name was seized, ibuffstreams.app took its place, pointing to the same server infrastructure. This backup domain did not go unnoticed and was subsequently seized, pointing to the now-familiar banner.

The seizure banner
[![seizure banner](https://torrentfreak.com/images/seized-banner.png)](https://torrentfreak.com/images/seized-banner.png)

These secondary domain seizures also targeted many other domains and brands, including sportsurge.ws, footybite.app, totalsportekz.app, and istreameast.app. A longer list with more examples is available below.

## Iranian Fallback

As long as the people running these sites are not caught, they will often launch new domain names. This is not new, but a recent series of domains caught our eye, as it is using seemingly more resilient fallback: Iran’s .ir country-code top-level domain.

OSINT data gathered by TorrentFreak found that buffstreams.ir, sportsurge.ir, and footybite.ir are all active and operational. These domains resolve to the same Ukrainian [IP-address](https://iplocation.io/ip/45.12.1.108), which was previously used by the now seized buffstreams.plus, ibuffstreams.app, and sportsurge.ws domains.

The Iranian domains are paired with Iranian [nameservers](https://www.whatsmydns.net/#NS/sportsurge.ir), [ns1.pars.cloud and ns2.pars.cloud](https://torrentfreak.com/images/pars.png), which are also new as the earlier domains relied on Cloudflare nameservers. This suggests that the operators are intentionally moving away from American infrastructure.

## Three Years in the Making

Iranian WHOIS data doesn’t reveal when the domains were registered, but SSL certificate logs tell us these .ir domains are not recent emergency registrations.

Both buffstreams.ir and sportsurge.ir received their first SSL certificates on September 22, 2023, within six minutes of each other. Their certificate chains have been renewed without interruption every 90 days since.

In other words, the .ir domains were set up nearly three years before Operation Offsides was announced. All this time they were presumably kept in reserve as a fallback and following the recent seizure actions they were brought to the fore.

The same certificate information also shows that, [a few days ago](https://crt.sh/?q=buffstreams.ir&output=json), these .ir domains moved away from the Google SSL certificates they have been using for years. Instead, they switched to certificates from Let’s Encrypt.

## More Iranian Links

The three domains on pars.cloud are not the only pirate streaming brands using .ir. Our investigation identified at least 20 additional streaming-related .ir domains spread across several operator clusters.

This includes Totalsportek, nflbite, and nflstreams branded sites with .ir domains, which are all share the same Cloudflare nameserver pair, indicating that they are run from the same account. There is also a separate .ir-linked mlb66 and nhl66 operation, which has been in use for a while.

These .ir domains are not necessarily a response to the recent U.S. domain seizures, as they’ve been around for much longer, but they show that more operators have discovered the .ir ccTLD.

In fact, we have also seen a cluster of Iranian sports streaming domains that are registered, but are not serving any content. These include nbabite.ir, nbastreams.ir, nhlbite.ir, mmastreams.ir, nflstream.ir, stream2watch.ir, and streameastt.ir. These may be waiting to be deployed at a later moment.

## Political Tensions

Iran’s .ir country-code TLD is managed by IRNIC, which is part of the Institute for Research in Fundamental Sciences, an academic institution based in Tehran. This makes it essentially unreachable for U.S. law enforcement.

Because of American sanctions, U.S. domain registrars are not allowed to resell .ir domain names. At the same time, given the current state of U.S.-Iran relations it is unlikely that IRNIC will voluntarily cooperate with U.S. authorities to target these domain names.

For pirate sites operators, .ir domains are also appealing due to a revision of IRNIC’s WHOIS policy in 2023. As a result, public queries no longer return registration dates, registrant names, or other contact information. For outsiders, these domains are essentially anonymous.

Notably, Iran’s copyright laws do not cover works from outside Iran, as the country is not a signatory to the Berne Convention, the WIPO Copyright Treaty, or a member of the WTO. This further complicates enforcement actions.

Of course, there are plenty of downsides to using .ir domain names. The international sanctions will make it challenging to monetize these domains, while Iranian domains are more complicated to register, and may also seem less trustworthy to the broader public.

Also, if an Iranian domain name gets millions of monthly visits, including a large American audience, the U.S. authorities may try to target these operations from alternative angles.

*—*

Below is a list pirate sports streaming domains that were seized this past weekend. This is addition to the domain names that were [seized earlier](https://torrentfreak.com/feds-seize-domain-names-of-nearly-400-pirate-sports-streaming-sites/).

– 247sports1.live
– 4kstream.online
– 808score.net
– acrli.org
– alamalkoora.info
– alphastreams1.online
– arkooora.live
– articletech.info
– asyallakora.live
– bally-sports.click
– bintv.net
– bracupgi.org
– buffstreams.app
– coollkoora.live
– cupshots.live
– daddylive.org
– daysports.online
– deporte-libre.live
– deporte-libre.online
– dingdongsport.org
– dosenow.net
– dotsport.online
– embedhd.org
– exorbitantprivilege.net
– extremesportstv.online
– falconstreams.org
– firstrowsports.org
– foorja.live
– footfytv.live
– footstreams.link
– footy100.net
– footybite.app
– footybitez.app
– fotoklikk.live
– funteam.info
– futbollibre.gratis
– goal-koora.live
– goal2.live
– goto-matc...