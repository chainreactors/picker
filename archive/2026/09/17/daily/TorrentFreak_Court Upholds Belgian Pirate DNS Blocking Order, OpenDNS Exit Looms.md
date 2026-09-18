---
title: Court Upholds Belgian Pirate DNS Blocking Order, OpenDNS Exit Looms
url: https://torrentfreak.com/court-upholds-belgian-pirate-dns-blocking-order-opendns-exit-looms/
source: TorrentFreak
date: 2026-09-17
fetch_date: 2026-09-18T06:53:41.008875
---

# Court Upholds Belgian Pirate DNS Blocking Order, OpenDNS Exit Looms

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

# Court Upholds Belgian Pirate DNS Blocking Order, OpenDNS Exit Looms

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

Google, Cloudflare, and Cisco lost a key challenge against a Belgian DNS blocking order. The revised injunction, obtained by sports rightsholder DAZN, requires alternative resolvers to block pirate sports streaming domains on match days. Cisco says it will suspend OpenDNS in Belgium rather than comply, and intends to appeal.

![opendns](https://torrentfreak.com/images/cisco-opendns.png)
Belgium was relatively late to the site blocking party, but since a dedicated anti-piracy department opened its doors, the country has caught up quickly.

The [first blocking order](https://torrentfreak.com/dazn-pirate-iptv-action-coincided-with-massive-public-dns-blockade-250407/) under this new regime, obtained by sports rightsholder DAZN in April 2025, started quite aggressively. In addition to major ISPs, it required Cloudflare, Google and Cisco to stop resolving pirate streaming domains through their public DNS services, under threat of €100,000 in fines per day.

Cisco’s response was also aggressive, as the company [pulled its OpenDNS service](https://torrentfreak.com/opendns-quits-belgium-under-threat-of-piracy-blocks-or-fines-of-e100k-per-day-250416/) out of Belgium entirely. Google and Cloudflare, meanwhile, complied [in their own ways](https://torrentfreak.com/dns-piracy-blocking-orders-google-cloudflare-and-opendns-respond-differently-250511/), but all three companies challenged the order.

In July 2025, the court [suspended](https://torrentfreak.com/belgiums-latest-pirate-site-blocking-order-spares-dns-providers/) the DNS blocking requirement against Cisco pending a final ruling, after which [OpenDNS](https://www.opendns.com/) returned to Belgium. This also put additional DNS blocking orders on hold. However, that may very well change in the near future.

## Court Upholds DNS Blocking

That final ruling has now arrived, and it’s not what the DNS providers were hoping for. On August 20, the President of the French-speaking Business Court of Brussels rejected the core of their challenge. The DNS blocking requirement stands.

The order itself hasn’t been published, but a new implementation decision from Belgium’s anti-piracy department summarizes the outcome and explains how the blockade will work in practice.

According to the decision, the court ruled that it’s technically possible for alternative DNS resolvers to block domains, and that the companies failed to show that the costs would be disproportionate. Worries that some users near the border could be caught by geolocation overblocking errors did not change that decision.

“Imposing a blocking measure on the main alternative DNS resolution service providers helps strengthen the effectiveness of the blocking injunction imposed on ISPs, which is regarded as a relevant measure,” the decision reads.

“The combination of these measures is intended to discourage users seeking access to unlawful content, as their experience as consumers of football matches, which they are very attached to watching live, will be disrupted,” it adds.

*From the implementation order*

![order](https://torrentfreak.com/images/ciscoordr.png)

The court order also included some small wins for the DNS providers. For example, it scrapped the requirement to redirect users to a warning page, noting that this measure can’t be imposed on DNS resolvers.

The penalties for non-compliance were also softened. The €100,000 per day fine remains, but it only counts on days that DAZN matches are broadcast live. There’s a €20 million maximum per company, and fines don’t apply to under-blocking caused by “an exceptional geolocation error.”

## Evolving Blocklist with a 90-minute Clock

The department’s decision also explains how the blocking will work in practice. The order covers matches from Belgian football competitions, including the Jupiler Pro League. As the season continues, DAZN can submit one blocklist update per week, with a maximum of 100 new domains.

There’s no fixed schedule. Instead, DAZN tells the department which matchday it wants the blocklist updated for, at least seven working days in advance. The DNS resolvers then get five working days to implement the changes.

The actual blockades should go live 90 minutes before a match starts, to catch pirates off guard.

“It is also with this effectiveness of the blocking measure in mind that it was decided that it should operate intermittently, and that it should only be implemented one and a half hours before the start of matches,” the implementation order reads.

“In this way, users find it more difficult to anticipate the blocking and plan around it in advance.”

*“Difficult to anticipate”*

![difficult](https://torrentfreak.com/images/intermittent.png)

The evolving nature of the blocklist is apparent from the publicly shared data, which shows that the domains blocked under this order have grown from 58 to 258 after it was first issued.

## OpenDNS Exit Looms

As reported last year, Google and Cloudflare complied with the original order. The latest order doesn’t change anything for them. However, for Cisco it’s a different story.

During the hearing, Cisco informed the department that it will pull OpenDNS out of Belgium again.

The company stated that the public DNS system “does not allow for the implementation of selective, geolocated and dynamic blocking as required by the order,” and that enabling it “would compromise the performance, stability and security of that service.”

Pulling out of Belgium is the only concrete measure Cisco is “technically able” to implement, the company added. The Belgian anti-piracy department accepts this drastic measure as compliance with the order.

The DNS resolvers have three months to implement the blocking measures. For now, OpenDNS remains available in Belgium and Cisco indicated it intends to appeal the ruling. TorrentFreak was told that a formal statement was still being finalized at the time of publication.

Unless the appeal changes anything, OpenDNS users in Belgium can expect the service to go dark for a second time later this year.

—

**Update:** Cisco did not go into most of our questions and released a short statement instead.

“OpenDNS currently remains available in Belgium,” a spokesperson said.

*—*

A copy of the Belgian anti-piracy department’s implementation decision of September 7 is available [here (pdf)](https://torrentfreak.com/images/260907-BAPO-D-FR-025-EN.pdf).

* [Previous Post![](https://torrentfreak.com/wp-content/themes/torrentfreak/build/assets/img/arrow-right.svg)](https://torrentfreak.com/denuvo-sues-game-cracker-voices38-for-bypassing-its-anti-tamper-drm/)

### Tagged In:

* [Cisco](https://torrentfreak.com/tag/cisco/)
* [Cloudflare](https://torrentfreak.com/tag/cloudflare/)
* [DNS](https://torrentfreak.com/tag/dns/)
* [google](https://to...