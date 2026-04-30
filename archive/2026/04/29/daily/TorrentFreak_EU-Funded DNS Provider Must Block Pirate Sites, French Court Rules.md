---
title: EU-Funded DNS Provider Must Block Pirate Sites, French Court Rules
url: https://torrentfreak.com/eu-funded-dns-provider-must-block-pirate-sites-french-court-rules/
source: TorrentFreak
date: 2026-04-29
fetch_date: 2026-04-30T05:30:32.467086
---

# EU-Funded DNS Provider Must Block Pirate Sites, French Court Rules

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

# EU-Funded DNS Provider Must Block Pirate Sites, French Court Rules

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Piracy](https://torrentfreak.com/category/piracy/ "Go to the Piracy category archives.") >

DNS4EU, an EU-funded initiative that aims to offer a secure and privacy-focused DNS resolver for Europeans, is the latest intermediary to get caught up in the French anti-piracy crackdown. In a series of orders in favor of Canal+, the Paris court ordered search engines, ISPs, DNS providers, VPNs, and other intermediaries to block pirate streaming sites.

![dns4eu](https://torrentfreak.com/images/dns4eu-600x387.png)

First, it required [Cloudflare, Google, and Cisco](https://torrentfreak.com/court-expands-google-and-cloudflare-dns-blocking-to-combat-piracy-241125/) to actively block access to pirate sites through their own DNS resolvers, confirming that third-party intermediaries can be required to take responsibility. Not much later, [VPN providers](https://torrentfreak.com/french-court-orders-vpns-to-block-more-pirate-sites-rejects-eu-court-referral/) were added to the blocking roster, as well as search engines.

These intermediaries were targeted because they could help pirates to bypass other blocking measures. If these alternative routes are cut off as well, the overall effectiveness of the anti-piracy injunction would improve.

This broader blocking push was further strengthened in March when the Paris court issued a [series of blocking measures](https://torrentfreak.com/paris-court-issued-simultaneous-site-blocking-orders-against-isps-dns-resolvers-and-vpns/) all at once. By ordering ISPs, DNS resolvers, and VPN providers to block pirate sites all at once, it should be even more effective.

These bundled orders appear to be the new standard. On April 17, the Paris court issued a series of 18 orders, with half protecting pirate Formula 1 streams and the other half targeting MotoGP infringers.

The series of 18 separate court orders, which we conveniently list in a [table below](#table), were all handed down on the same day. They include a wide variety of intermediaries, including a notable new name: [DNS4EU](https://joindns4.eu/).

## DNS4EU Must Block Pirate Sites

DNS4EU is a public DNS resolver service co-funded by the European Commission and operated by a consortium led by Czech cybersecurity company [Whalebone](https://www.whalebone.io/). The service, which [officially launched](https://joindns4.eu/learn/dns4eu-public-service-launched) last June, is presented as a sovereign European alternative to non-EU resolvers such as Google Public DNS and Cloudflare.

“The goal of DNS4EU is to ensure the digital sovereignty of the EU by providing a private, safe, and independent European DNS resolver,” the project’s website states.

On April 17, the Paris court issued two rulings against DNS4EU/Whalebone, requiring the DNS resolver to block 16 pirate streaming domains linked to pirated MotoGP streams and 21 domains linked to Formula 1 streams.

“Order Whalebone to implement, within the framework of its domain name resolution system called ‘Dns4eu,’ all blocking measures to prevent access from French territory, including all overseas territories of France, by any effective means to the identified internet sites and IPTV services accessible from [these domain names],” the translated order reads.

These orders were requested by French broadcaster Canal+, which holds the rights to these broadcasts, and the orders remain valid until the end of the season.

The list of targeted domains includes pirate IPTV and streaming sites such as antenawest.store, daddylive3.com, rereyano.ru, iptvsupra.com, king365tv.me, sportzonline.live, and smartbox-tv.com, with many of the same domains appearing in both orders.

*Targeted domains*
[![targeted domains](https://torrentfreak.com/images/bloque.png)](https://torrentfreak.com/images/bloque.png)

## Default Judgment

The rulings against Whalebone are default judgments. The company did not appear at the February 19 hearing and filed no defense. As a result, the Paris court ruled in Canal+’s favor without any opposing arguments.

DNS4EU is not the only DNS provider to forfeit a defense in the French proceedings. [Quad9](https://quad9.net/), a Swiss-based non-profit foundation that operates a privacy-focused public DNS resolver, also defaulted in a parallel ruling handed down the same day.

Other intermediaries did put up a fight. Google, NordVPN, Surfshark, ProtonVPN, and Cloudflare (referred to in the published ruling under the pseudonym) all contested the blocking requests, without result.

Other intermediaries did put up a fight. Google, NordVPN, Surfshark, ProtonVPN, and Cloudflare all contested the blocking requests, without result. Cloudflare appears in the published rulings under pseudonyms, possibly due to French anonymization rules.

The Paris court rejected claims that VPNs and DNS resolvers fall outside the scope of Article L. 333-10 of the French Sports Code, which permits dynamic site blocking against “any person likely to contribute” to remedying infringement.

The court also rejected the defendants’ technical arguments about cost, encryption, and general monitoring obligations, citing the lack of “quantified and verifiable” evidence.

Google and Cloudflare previously objected to similar rulings, but their opposition was also [rejected on appeal](https://torrentfreak.com/google-cloudflare-cisco-lose-pirate-site-dns-blocking-appeal-in-france/). The companies’ request to refer the case to the EU’s highest court has also been rejected.

DNS4EU has not explained why it chose not to defend itself. The organization did not respond to a request for comment, and parent company Whalebone did not return our request for clarification either.

## Global Blocking Fallout

While we do not know for sure what DNS4EU’s official position is, TorrentFreak’s tests of the DNS4EU public resolvers from outside France showed that, as of this writing, several targeted domains show SSL errors.

This includes Rightflourish.net, which shows the following error message, also to users outside of France

*SSL error on rightflourish.net*

![ssl error](https://torrentfreak.com/images/sslerror.png)

Visitors who proceed to ignore the SSL warning and continue to the blocked domain will eventually see a [blocking notification](https://warning.joindns4.eu/passthrough?data=eyJNZXRob2QiOiJHRVQiLCJTY2hlbWUiOiJodHRwcyIsIkhvc3QiOiJtYXJjb2JveC5pbiIsIlBvcnQiOiI0NDMiLCJQb3N0RGF0YSI6IiIsIlBhdGgiOiIvIiwiUXVlcnkiOiJ7fSIsIlNpbmtob2xlSUQiOjYwMDAwMTMsIk51bWJlck9mUmVkaXJlY3RzIjowfQ), confirming that DNS4EU is complying with the French court order. The blocking message was added this week.

*Confirmation*

![4eu blocked](https://torrentfreak.com/images/4eublock.png)

The block also appears to extend beyond France, applying to users in other EU member states. Technically, that could be considered overblocking. However, without a response from the EU-funded project, it remains unclear whether this cross-border application is intentional or an oversight.

We will update this article accordingly when DNS4EU responds.

*—*

An over...