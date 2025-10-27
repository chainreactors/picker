---
title: Cloudflare Starts Blocking Pirate Sites For UK Users – That’s a Pretty Big Deal
url: https://torrentfreak.com/cloudflare-starts-blocking-pirate-sites-for-uk-users-thats-a-pretty-big-deal-250715/
source: TorrentFreak
date: 2025-07-16
fetch_date: 2025-10-07T00:06:12.212035
---

# Cloudflare Starts Blocking Pirate Sites For UK Users – That’s a Pretty Big Deal

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

# Cloudflare Starts Blocking Pirate Sites For UK Users – That’s a Pretty Big Deal

July 15, 2025 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

Cloudflare has become the first internet intermediary beyond local residential ISPs, to block access to pirate sites in the UK. Users attempting to access certain pirate sites are greeted with 'Error 451 - Unavailable for Legal Reasons'. In theory, ISP blocking should prevent UK users from even seeing this notice, but a combination of Cloudflare's blocking mechanism and choices made by some VPN users results in a piracy dead end.

![cloud-dark](https://torrentfreak.com/images/cloud-dark.png)
Internet service providers BT, Virgin Media, Sky, TalkTalk, EE, and Plusnet account for the majority of the UK’s residential internet market and as a result, blocking injunctions previously obtained at the High Court often list these companies as respondents.

These so-called “no fault’ injunctions stopped being adversarial a long time ago; ISPs indicate in advance they won’t contest a blocking order against various pirate sites, and typically that’s good enough for the Court to issue an order with which they subsequently comply.

For more than 15 years, this has led to blocking being carried out as close to users as possible, with ISPs’ individual blocking measures doing the heavy lifting. A new wave of blocking targeting around 200 pirate site domains came into force yesterday but with the unexpected involvement of a significant new player.

## Cloudflare Blocks Pirate Sites “For Legal Reasons”

If piracy is rampant, in the UK pirate site blocking must qualify as rampant too. In the latest wave of blocking that seems to have come into force yesterday, close to 200 pirate domains requested by the Motion Picture Association were added to one of the longest pirate site blocking lists in the world.

The big change is the unexpected involvement of Cloudflare, which for some users attempting to access the domains added yesterday, displays the following notice:

![Cloudflare 451 2025-07-15](https://torrentfreak.com/images/Cloudflare-451-2025-07-15.png)

As stated in the notice, Error 451 is returned when a domain is blocked for legal reasons, in this case reasons specific to the UK.

> *In response to a legal order, Cloudflare has taken steps to limit access to this website through Cloudflare’s pass-through security and CDN services within the United Kingdom.*

## Background: Cloudflare’s Blocking Policy

Before we take a look at the ‘legal order’ that prompted Cloudflare to take this action, Cloudflare’s blocking policy for copyright claims concerning its CDN and security services provides useful background information.

> *Because Cloudflare cannot remove content it does not host, other service providers are better positioned to address these issues. Among other things, any blocking by Cloudflare is of limited effectiveness, as a website will be accessible if it stops using Cloudflare’s network. Cloudflare therefore regularly pushes back against attempts to seek blocking orders.*

Cloudflare notes that it may take steps to comply with valid orders if, among other things, “principles relating to proportionality, due process, and transparency” are upheld.

Whether Cloudflare pushed back here isn’t clear, but the information made available falls well short of that promised in the Error 451 notice.

## Semi-Transparent and Still Lacking

With no central repository of blocking orders and no legal requirement to share details of injunctions with the public, transparency in the UK is mostly left to chance. Some orders make their way online, but there is no guarantee.

For those interested in finding out more about the order affecting Cloudflare, the company provides a link which promises to reveal “the party that requested it, and the authority that issued it.” The link directs to the [Lumen Database](https://lumendatabase.org/notices/39665907?access_token=1mNN2Z9qK094SVO-9teUPQ), which publishes information effectively donated by companies such as Google and Cloudflare, for the purpose of improving transparency.

In this case there’s no indication of who requested the blocking order, or the authority that issued it. However, from experience we know that the request was made by the studios of the Motion Picture Association and for the same reason the High Court in London was the issuing authority.

To the general public, the information is just a short list of domains. If it wasn’t for the efforts of Lumen, Google and Cloudflare, the situation would be significantly less clear than that.

![Lumen-MPA-2025-07-15](https://torrentfreak.com/images/Lumen-MPA-2025-07-15.png)

Look more closely and further issues become apparent. According to the sender of the original notice (a law firm representing the studios), an explanation of the court order can be found in “paragraph 1, paragraph 2, and Schedule 1 of the Order” but where that can be found isn’t made any more clear than the name of the issuing court.

Then there’s the date of the notice – February 22, 2024, well over a year ago – for blocking that we believe started just yesterday.

## Dynamic Blocking=Limited Transparency

The list of 14 domains probably relates to a High Court blocking injunction obtained by the MPA pre-February 2024, but exactly when is more difficult to say.

The issue lies with dynamic injunctions; while a list of domains will appear in the original order (which may or may not be made available), when the MPA concludes that other domains that appear subsequently are linked to the same order, those can be blocked too, but the details are only rarely made public.

From information obtained independently, one candidate is an original order obtained in December 2022 which requested blocking of domains with well known pirate brands including 123movies, fmovies, soap2day, hurawatch, sflix, and onionplay. This leads directly to another unusual issue.

The notice linked from Cloudflare doesn’t directly concern Cloudflare. The studios sent the notice to Google after Google [agreed](https://torrentfreak.com/google-removes-pirate-bay-domains-from-search-results-citing-dutch-court-order-211130/) to *[voluntarily remove](https://torrentfreak.com/googles-permanent-deindexing-of-pirate-sites-spreads-across-europe-221216/)* those domains from its search indexes, if it was provided with a copy of relevant court orders. Notices like these were supplied and the domains were deindexed, and the practice has continued ever since.

That raises questions about the nature of Cloudflare’s involvement here and why it links to the order sent to Google; notices sent to Cloudflare are usually submitted to Lumen by Cloudflare itself. That doesn’t appear to be the case here.

## Partially Effective at Blocking VPNs

When blocking measures are required, Cloudflare digs in when requests concern its public DNS resolver (1.1.1.1). To achieve a similar ...