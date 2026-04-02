---
title: Google, Cloudflare, Cisco Lose Pirate Site DNS Blocking Appeal in France
url: https://torrentfreak.com/google-cloudflare-cisco-lose-pirate-site-dns-blocking-appeal-in-france/
source: TorrentFreak
date: 2026-04-01
fetch_date: 2026-04-02T04:31:37.172150
---

# Google, Cloudflare, Cisco Lose Pirate Site DNS Blocking Appeal in France

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

# Google, Cloudflare, Cisco Lose Pirate Site DNS Blocking Appeal in France

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

The Paris Court of Appeal has confirmed that third-party DNS providers can be legally compelled to block access to domain names to stop piracy. The DNS providers countered that such measures are technically burdensome and easily bypassed. However, the court ruled that the intermediaries must act nonetheless and pick up the bill themselves. This is a clear win for Canal+, which pioneered the blocking expansion.

![france](https://torrentfreak.com/images/france-1.jpg)
Traditional site-blocking measures that require local ISPs to block subscriber access to pirate sites have been commonplace in France for years.

By blocking pirate domains through ISP DNS resolvers, subscriber access is effectively cut off. However, the measures were only partially effective, as many users simply switched to third-party DNS resolvers to get around them.

In 2024, an order from the Paris Judicial Court, requested by football and rugby rightsholder Canal+, aimed to patch that loophole. The order required Cloudflare, Google, and Cisco to actively block access to pirate sites [through their own DNS resolvers](https://torrentfreak.com/google-cloudflare-cisco-will-poison-dns-to-stop-piracy-block-circumvention-240613/), confirming that [third-party intermediaries](https://torrentfreak.com/court-expands-google-and-cloudflare-dns-blocking-to-combat-piracy-241125/) can be required to take responsibility.

## Article L. 333-10

The DNS blocking order is grounded in [Article L. 333-10](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044247629/) of the French Sport Code, which enables rightsholders to request blocking measures against named pirate sites if they can demonstrate “serious and repeated infringement” of their exploitation rights.

To prevent pirate sites from being accessed on French soil, rightsholders may request that “all proportionate measures” are implemented by any online entity in a position to help.

The scope of Article L. 333-10 was always meant to be broad. There was little doubt that it included regular consumer ISPs. However, applying it to DNS resolvers was a different matter, and all three companies fought back.

Cisco was the most extreme in its response. The American company decided to stop offering its OpenDNS service in France, pending appeal. Google and Cloudflare kept their DNS resolvers online in the country but joined Cisco at the Paris Court of Appeal.

## Five Appeals, Five Rejections

Last week, the Paris Court of Appeal ruled on five separate appeals, where Cisco, Cloudflare, and Google appealed blocking orders that the French pay-TV provider Canal+ obtained. The court rejected all appeals and concluded that DNS blocking measures are both technically feasible and proportionate.

The news was first reported by the French news outlet [L’Informé](https://www.linforme.com/tech-telecom/article/piratage-sportif-victoire-majeure-de-canal-contre-google-cisco-et-cloudflare_3840.html), which also published [the orders](#orders).

This is the first time a French appeals court has validated the DNS blocking approach under Article L. 333-10, giving the strategy a considerably stronger legal basis. Specifically, the appeals court repeatedly stressed that DNS resolvers can be required to block pirate sites.

## Defense Arguments Fail

The DNS providers raised various arguments in their defense. According to the court’s summary, Cloudflare and Cisco argued that their services have “only a neutral and passive function” and “neither transmit nor participate in infringement.” They compared their role to an address book: they translate domain names into IP addresses, and their involvement ends the moment they return that result to a user’s browser.

This argument failed to convince the court, which found that the “neutral and passive” nature of the DNS resolvers is simply irrelevant to Article L. 333-10. The law isn’t about liability at all. What matters is whether a service can help to block access to pirate sites, which DNS resolvers clearly can.

“The DNS resolution service allows its users, via the translation of a domain name into an IP address, to access websites on which sports competitions are broadcast in violation of rights-holders’ rights, and in particular to circumvent the blocking of those sites by ISPs,” the court wrote.

Google also argued that blocking pirate sites via third-party DNS services is not an effective deterrent, since it can be circumvented by using a VPN or switching to yet another DNS resolver.

The appeals court wasn’t moved by this argument either. French law doesn’t require blocking measures to be perfect, as long as they stop a subset of the visitors to pirate sites, it’s good enough.

“Any filtering measure can be circumvented, and this possibility does not render the measures in question ineffective,” the Paris Court of Appeal wrote.

## Intermediaries Pick Up the Bill

Cisco, which [shut down](https://torrentfreak.com/opendns-suspends-service-in-france-due-to-canal-piracy-blocking-order-240629/) its OpenDNS service in France instead of complying with the original order, argued on appeal that implementing geo-targeted DNS blocking would require 64 person-weeks of engineering work.

However, the court was not swayed by this cost argument, noting in its decision that the estimate was “not supported by any objective evidence.” The court also pointed out that Cisco already offers a DNS filtering service to enterprise customers, which undermined the argument that there’s a significant technical challenge.

Cloudflare, meanwhile, offered no figures at all to quantify the cost, the court noted, adding that they also offer filtering options already.

At the end of the day, Cisco, Cloudflare, and Google will have to implement the blocking measures for hundreds of pirate site domains while covering the implementation costs themselves.

## More IP Blocking Battles Ahead

Canal+ is pleased with the five appeals court rulings. The pay-TV service Canal+ said in a statement that the rulings are “more than a victory,” forming part of “a global approach that will be reinforced by the progressive deployment of complementary measures, including IP blocking.”

In France, the next anti-piracy frontier is automated IP-address blocking, which is expected to go live later this year, ahead of the FIFA football World Cup. According to L’Informé, the Roland Garros tennis tournament will [serve as a trial](https://torrentfreak.com/france-escalates-war-on-sports-piracy-with-real-time-ip-blocking/) opportunity.

In addition to DNS providers, Canal+ and other rightsholders have also obtained blocking orders against VPN providers. These are still under appeal.

*—*

The five orders of the Paris Court of Appeal (RG 24/09372), dated March 27, 2026, are available [here (p...