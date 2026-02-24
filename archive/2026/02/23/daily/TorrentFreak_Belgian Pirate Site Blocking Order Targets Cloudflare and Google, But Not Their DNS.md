---
title: Belgian Pirate Site Blocking Order Targets Cloudflare and Google, But Not Their DNS
url: https://torrentfreak.com/belgian-pirate-site-blocking-order-targets-cloudflare-and-google-but-not-their-dns/
source: TorrentFreak
date: 2026-02-23
fetch_date: 2026-02-24T04:12:18.453755
---

# Belgian Pirate Site Blocking Order Targets Cloudflare and Google, But Not Their DNS

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

# Belgian Pirate Site Blocking Order Targets Cloudflare and Google, But Not Their DNS

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

Belgium's site-blocking machine keeps turning. A new order, obtained by local broadcasters RTL Belgium and RTBF, compels ISPs, Cloudflare, and Google to restrict access to five illegal IPTV services. Importantly, the latter two are not required to block content through their DNS resolvers, which is likely the result of an ongoing legal challenge.
Notably, DNS providers are spared this time around, likely reflecting the ongoing legal fallout from earlier Belgian orders that drove Cisco's OpenDNS to temporarily abandon the country.

![cloudgoogle](https://torrentfreak.com/images/cloudgoogle.png)
Belgium has become one of Europe’s most active testing grounds when it comes to pirate site-blocking enforcement.

The country’s [two-step system](https://torrentfreak.com/how-a-court-order-to-block-internet-archives-open-library-was-put-on-hold/), where a court issues an injunction and a government department ([BAPO](https://economie.fgov.be/en/themes/intellectual-property/intellectual-property-rights/copyright-and-related-rights/sanctions-and-legal-actions/online-piracy)) then determines how it is implemented, has resulted in a series of diverse site-blocking orders since the framework launched in 2025.

## An Eclectic Site Blocking Push

The first order, obtained by sports broadcaster DAZN in April 2025, started quite aggressively. It required ISPs and third-party DNS resolvers, [including Cloudflare, Google, and Cisco’s OpenDNS](https://torrentfreak.com/dazn-pirate-iptv-action-coincided-with-massive-public-dns-blockade-250407/), to stop resolving over 100 pirate domains. If not, they would risk a fine of €100,000 per day.

Cisco refused to comply with the order and instead [pulled OpenDNS out of Belgium](https://torrentfreak.com/opendns-quits-belgium-under-threat-of-piracy-blocks-or-fines-of-e100k-per-day-250416/) entirely. Cloudflare and Google remained in Belgium and cooperated, though each did so in its own way.

A second blocking order followed in July last year, requiring various intermediaries, including ISPs, hosting companies, and payment services, [to block shadow libraries](https://torrentfreak.com/belgium-targets-internet-archives-open-library-in-sweeping-site-blocking-order/). Initially, Internet Archive’s Open Library was also targeted, but [this decision](https://torrentfreak.com/how-a-court-order-to-block-internet-archives-open-library-was-put-on-hold/) was eventually reversed after the U.S. non-profit [agreed to geo-block](https://torrentfreak.com/internet-archive-ordered-to-block-books-in-belgium-after-talks-with-publishers-fail/) certain content on its service.

Meanwhile, Cisco reportedly appealed the initial site-blocking order and returned to Belgium. While this appeal remains ongoing, the Belgian site-blocking machine didn’t stop.

Last November, an order obtained by [Disney, Netflix, Sony, Apple, and others](https://torrentfreak.com/hollywood-netflix-and-apple-are-behind-latest-pirate-brand-blockades-in-belgium/), targeted popular movie piracy sites, including 1337x and Soap2day. Notably, this order only applied to Belgium’s five major ISPs. [DNS resolvers were nowhere on the list](https://torrentfreak.com/belgiums-latest-pirate-site-blocking-order-spares-dns-providers/), likely due to Cisco’s appeal.

## First IPTV Blocking Order

A new order, issued by the Court of Brussels, targets five illegal IPTV services: LEMEILLEURIPTV, BESTIPTVABO, ATLASPRO12, OTT PREMIUM, and MIJNIPTV. The order was obtained by Belgian broadcasters RTL Belgium and RTBF, whose broadcasts were distributed by these services without permission.

*IPTV targets*

![iptv block](https://torrentfreak.com/images/iptvblock.png)

The implementation decision, published by Belgium’s Department for Combating Infringements of Copyright and Related Rights Committed Online (BAPO), described the IPTV services as “structurally dedicated to the mass infringement of audiovisual content”.

**Note:** While the BAPO implementation order does not explicitly name the rightsholders, it lists specific content from **RTL Belgium** and **RTBF**. Both broadcasters [confirmed](https://www.mm.be/news-nl-89458-iptv-rtbf-en-rtl-voeren-druk-op-illegale-diensten-op) obtaining an IPTV blocking order against Belgian ISPs at the Brussels court earlier this month.

According to information shared by the rightsholders, the services used cryptocurrency, which they see as a sign of illegality. In addition, the IPTV services showed users how to circumvent blocking measures.

All in all, the implementation order requires Belgium’s five major ISPs, Proximus, Telenet, Orange Belgium, Mobile Vikings, and DIGI Communications, to block domain names associated with these IPTV services. This also applies to mirror sites and redirect domains that can be added to the blocklist in future updates.

## Cloudflare and Google Are Back, But Not for DNS

The ISPs will have to use DNS-based blocking measures, as is standard procedure in most countries. However, DNS blocking measures are not requested from Cloudflare and Google, which are also covered by the injunction.

The order names the American tech companies as intermediaries and requires them to help stop the IPTV services through other routes.

Specifically, if Cloudflare acts as a CDN or hosting provider, it must take measures to prevent Belgian users from accessing the named IPTV services. Crucially, Cloudflare’s DNS resolver and WARP service are not covered.

Google is not required to block the domains on its DNS resolver either. Instead, Google must de-index the relevant domains from its search results, deactivate associated Google Ads, and block access through Google Sites and Google Cloud services where applicable.

This omission of any third-party DNS restrictions is almost certainly not accidental. Cisco’s appeal of the April 2025 order resulted in a Brussels court suspending enforcement of the DNS blocking requirement, allowing OpenDNS to resume operations in Belgium pending a final ruling.

With that legal challenge still unresolved, rightsholders appear to have opted for a more defensible scope, targeting Cloudflare and Google in their roles as infrastructure providers rather than as DNS operators.

## Exploring the Blocking Limits

The latest blocking order shows how Belgium’s blocking regime continues to calibrate itself in real time. Each new order is seemingly shaped by the legal and practical fallout from the last.

**April 2025:** Initial DAZN order aggressively targets ISPs and third-party DNS resolvers. Cisco pulls OpenDNS from Belgium.

**July 2025:** Second order requires various intermediaries to block shadow libraries.

**Summer 2025:** Cisco appeals; court suspends DNS blocking requirement, allowing OpenDNS to return.

**Nov 2025:** Broad order agai...