---
title: Belgium’s Latest Pirate Site-Blocking Order Spares DNS Providers
url: https://torrentfreak.com/belgiums-latest-pirate-site-blocking-order-spares-dns-providers/
source: TorrentFreak
date: 2025-12-05
fetch_date: 2025-12-06T03:11:56.497798
---

# Belgium’s Latest Pirate Site-Blocking Order Spares DNS Providers

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

# Belgium’s Latest Pirate Site-Blocking Order Spares DNS Providers

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

The Brussels Business Court has issued a new site-blocking order, targeting popular pirate sites including 1337x and Soap2day. Surprisingly, this latest order only requires major ISPs to take action. This is a notable change, as the initial blocking order under this regime also required DNS resolvers to take action. Whether this is a formal retreat or merely a pause has yet to be seen.

![stop danger](https://torrentfreak.com/images/stop-danger.jpg)

These blockades follow a newly instated two-step process. A local court first issues a blocking order, after which a special government body determines how it will be implemented. This process aims to prevent errors and overblocking.

## Pirate DNS Blocking

While site blocking is common in Europe, these new Belgian blockades go beyond the typical ISP blockade. Similar to [France](https://torrentfreak.com/french-court-orders-cloudflare-to-dynamically-block-motogp-streaming-piracy-250405/) and [Italy](https://torrentfreak.com/court-orders-google-to-poison-public-dns-to-prevent-iptv-piracy-250321/) , the orders were also directed at third-party public DNS resolvers.

The first implementation order, issued by the Belgian Department for Combating Online Infringement [in April](https://torrentfreak.com/dazn-pirate-iptv-action-coincided-with-massive-public-dns-blockade-250407/), required both ISPs and DNS resolvers to restrict access to pirate sites. Specifically, Cloudflare, Google, and Cisco’s OpenDNS were ordered to stop resolving over 100 pirate sites or face fines of €100,000 euros per day.

This order prompted significant pushback, most notably from Cisco, which [ceased operating its OpenDNS service in Belgium](https://torrentfreak.com/opendns-quits-belgium-under-threat-of-piracy-blocks-or-fines-of-e100k-per-day-250416/) soon after the order was announced.

In July, another order by the Belgian authority ordered blockades of shadow library websites, including Libgen, Zlibrary, and Anna’s Archive. This [sweeping court order](https://torrentfreak.com/belgium-targets-internet-archives-open-library-in-sweeping-site-blocking-order/) required ISPs to take action and also involved other intermediaries, such as hosting providers, search engines, and DNS services.

The underlying court order also called for a [broad blockade](https://torrentfreak.com/how-a-court-order-to-block-internet-archives-open-library-was-put-on-hold/) of the Internet Archive’s Open Library service. While that was ultimately [prevented](https://torrentfreak.com/internet-archive-ordered-to-block-books-in-belgium-after-talks-with-publishers-fail/), the involvement of a broad range of intermediaries caused concern about the escalating scope of the blocking orders.

## New ‘Limited’ Piracy Blocking Order

On November 26, the Belgian Department for Combating Online Infringement published a new blocking implementation order. While this effectively adds dozens of new domains to the Belgian blocklist, the scope of this order is surprisingly limited.

Instead of casting a wide net, the order strictly targets Belgium’s five major Internet Service Providers: Proximus, Telenet, Orange Belgium, DIGI Communications Belgium, and Mobile Vikings.

*From the order*

![orderbel](https://torrentfreak.com/images/orderbel.png)

The list of “addressees” no longer includes the DNS resolvers, Google, Cloudflare, and Cisco, which were central targets in the April blocking order. There is no mention of hosting services, advertisers, or other intermediaries either.

The official implementation order does not mention the rightsholder(s) who requested the blocking measures, nor does it mention the targeted sites. However, the blocked domains are published in a separate spreadsheet showing that 1337x, Fmovies, Soap2Day, and Sflix branded domains are among the key targets.

*From the blocking spreadsheet*
![block](https://torrentfreak.com/images/blockbel.png)

Since these pirate targets often switch domain names to evade enforcement, rightsholders can submit a new list of mirror sites or proxies once per week, capped at 50 new domains per week. When these are approved by the Belgian Department, ISPs have five working days to update the blocklist.

## Retreat or a Pause?

The decision to exclude DNS resolvers from this latest order is likely not a coincidence. It might very well be a direct consequence of the legal pushback Cisco initiated earlier this year, when it appealed the April blocking order at the Brussels Business Court.

This appeal was not without result, as the court suspended enforcement of that blocking order against Cisco in July, after which OpenDNS became available again in Belgium.

“The OpenDNS service has been reactivated in Belgium following a decision by the Brussels court to suspend enforcement of the order requiring Cisco to implement DNS blocking measures. The suspension of the order is pending a final ruling in the legal proceedings which remain ongoing,” a Cisco representative wrote in a [community update](https://community.cisco.com/t5/security-knowledge-base/opendns-service-currently-available-to-users-in-belgium/ta-p/5283479/redirect_from_archived_page/true#M18273).

To find out more about the suspended blocking measures, we reached out to the Belgian Department for Combating Online Infringement, which did not respond to our inquiry. Without further details, we don’t know whether the suspension also applies to other DNS resolvers. Confusingly, the official transparency portal makes no mention of an appeal at all.

It is likely, however, that since the legality of the blocking orders against third-party DNS resolvers is still being litigated, rightsholders have chosen to limit their blocking requests to ISPs. This would suggest that it’s a pause, not a formal retreat.

*—*

A copy of the latest blocking implementation order, published by the *Department for Combating Infringements of Copyright and Related Rights Committed Online and the Illegal Exploitation of Online Games of Chance* on the 26th of November, 2025, is available [here (pdf)](https://torrentfreak.com/images/251124-BAP0-D-FR-010-EN.pdf).
 *The full blocking spreadsheet, last updated November 26, is available at the Belgian [government website](https://economie.fgov.be/en/themes/intellectual-property/intellectual-property-rights/copyright-and-related-rights/sanctions-and-legal-actions/online-piracy).*

* [Previous Post![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-right.svg)](https://torrentfreak.com/court-empowers-hollywood-in-race-to-block-wicked-for-good-piracy-251204/)

### Tagged In:

* [belgium](https://torrentfreak.com/tag/belgium/)
* [DNS](https://torrentfreak.com/tag/dns/)
* [site blocking](https://torrentfreak.com/tag/site-blocking/)

### You Might Also Like:

[![]...