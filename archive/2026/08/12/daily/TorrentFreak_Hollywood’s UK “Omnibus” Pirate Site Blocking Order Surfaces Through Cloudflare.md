---
title: Hollywood’s UK “Omnibus” Pirate Site Blocking Order Surfaces Through Cloudflare
url: https://torrentfreak.com/hollywoods-uk-omnibus-pirate-site-blocking-order-surfaces-through-cloudflare/
source: TorrentFreak
date: 2026-08-12
fetch_date: 2026-08-13T04:05:27.700581
---

# Hollywood’s UK “Omnibus” Pirate Site Blocking Order Surfaces Through Cloudflare

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

# Hollywood’s UK “Omnibus” Pirate Site Blocking Order Surfaces Through Cloudflare

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

In May, the UK High Court granted several Hollywood studios a broad "omnibus" site blocking order, allowing them to block rotating networks of pirate sites, without the need to link them to known pirate brands. This breakthrough order was recently cited in a Canadian court order, but remained unavailable to the public, until now.

![pirate flags](https://torrentfreak.com/images/pirate-flags-1.jpg)When the Motion Picture Association (MPA) described its new UK blocking order to WIPO in May, it was presented as a key step in the fight against online piracy.

The [“omnibus” order](https://torrentfreak.com/hollywood-secures-broad-omnibus-pirate-site-blocking-order-in-uk-high-court/) would make it easier and quicker to block new domain names and pirate site brands that pop up in response to blocking efforts.

According to the MPA, it allows Hollywood studios to seek blocking of any “structurally infringing audiovisual piracy services that meet defined criteria, without having to bring a fresh court application for each new domain or site name available in the future.”

## Cited but Inaccessible

As we reported at the time, the order itself was nowhere to be found. The judgment was not on BAILII or in the National Archives, and none of the targeted ISPs had mentioned it. The MPA’s summary was the only public account.

The significance of the order was clear though. The MPA prominently featured it at WIPO and the UK ruling was also referenced and used as an example in a Canadian site blocking order that was handed down last month.

Canada’s Federal Court [noted](https://torrentfreak.com/canadas-expanded-scope-blocking-order-targets-existing-and-future-pirate-sites/) that the purpose of the order is to “address increased fragmentation in the Internet piracy landscape” that is the result of people switching from blocked to non-blocked sites and domains.

This “expanded scope” order, as Canada’s Federal Court called it, allows Hollywood studios and broadcasters to add unrelated sites to the blocklist, without having to go back to court. However, the UK order that it was based on remained unpublished, until recently.

This week, we spotted a new transparency filing from Cloudflare, which was added to the [Lumen database](https://lumendatabase.org/). This filing references the UK omnibus order and also attaches a copy of it.

## Omnibus Order Details Surface

That attachment is, as far as we know, the first public copy of the omnibus order. It is headed a “Public Version,” a copy with a confidential schedule removed, which confirms the broad powers the MPA described as well as other details.

The order, handed down by Mr Justice Mellor on 7 May 2026, was requested by Columbia, Disney, Netflix, Paramount, Universal and Warner Bros. The respondents are the UK’s six largest ISPs: BT, EE, Plusnet, Sky, TalkTalk and Virgin Media.

*The order (public version)*

![hc order](https://torrentfreak.com/images/hcorder.png)

Like previous UK blocking orders, the ISPs are required to block access to a series of websites. In this case, the first part of schedule 1 specifically lists 345movie.nl and 456movie.nl, cineby.app, movies2watch.watch and streamm4u.com.co. These are the ‘seeds,’ followed by an open-ended category in part 2 of the same schedule.

*The ‘seed’ domains and brands*

![schedule 1](https://torrentfreak.com/images/schedule1-1.png)

Since 2022, UK court orders also support subsequent blockades of similarly branded websites. The latest order expands this power to a much broader list of pirate sites, regardless of the brand used, as long as these are similar in functionality.

“[E]ach Part 2 Target Website has essentially the same mode of operation as one or more of the Part 1 Target Websites in so far as it enables users to stream film/audiovisual content by indexing and aggregating links to unauthorised copies of such content,” the order reads.

There is a clear set of boxes newly added sites have to tick, so future expansions are not unlimited. In this case, all pirate movie streaming sites that are available in the UK and unresponsive to complaints, should be fair game.

*The ‘add site’ requirements*

![addedreq](https://torrentfreak.com/images/onlyreq22.png)

The order does not come with a transparency clause that requires the list of blocked domains to be made public, which makes it impossible for the public and journalists to review the blocking efforts.

## Voluntary Expansion

Importantly, adding new sites to the blocklist does not involve a judge. When the studios flag a new Part 2 site, they notify the ISPs that the conditions are met, and it is added. There is no court hearing or independent review.

The order states that the ISPs are “wholly reliant on the Applicants accurately identifying” the URLs to block, and that they “have no obligation to verify whether the Applicants’ or their agents’ determination is correct.” The studios are in charge of expanding the blockades.

These expansions are not limited to the ISPs either. As mentioned earlier, Cloudflare published the order without being a party. This is because the American company voluntarily blocks targeted sites if these use its CDN services. These blocks are limited to the UK, as [we documented before](https://torrentfreak.com/cloudflare-starts-blocking-pirate-sites-for-uk-users-thats-a-pretty-big-deal-250715/).

*Error HTTP 451*

![error 451](https://torrentfreak.com/images/error451.png)

As shown above, Cloudflare shows an Error HTTP 451 to UK visitors that try to access movies2watch.watch, explaining that the site is unavailable for legal reasons.

## Guardrails and Limitations

The order is not without safeguards. In addition to the earlier mentioned expansion requirements, site operators or other people caught up in these blocking efforts have the right to object.

Importantly, rightsholders are also strictly prohibited from asking ISPs to block an IP address if the underlying server also hosts legitimate, non-infringing websites. This should prevent overblocking incidents.

Finally, there is also a relatively short time limit on the order, which expires after six months.

“This Order shall cease to have effect at 23:59pm on the date 6 months from the date of this Order, unless the Court orders otherwise,” it reads.

This doesn’t mean that the blocking order will cease to exist after that. In practice, it means that the Hollywood studios will return to court to request an extension. While there is no formal blocklist review, if there are any concerns they can be brought up then as well.

As far as we know, the judgment linked to the order has yet to be added to BAILII or the National Archives. Ironically, we only know of it because of the transparency efforts of Cloudflare, which isn’t even a formal pa...