---
title: Scammers Mimic Cloudflare’s ‘Error 451’ Site Blocking Notice to Infect Pirates
url: https://torrentfreak.com/scammers-mimic-cloudflares-error-451-site-blocking-notice-to-infect-pirates-251211/
source: TorrentFreak
date: 2025-12-11
fetch_date: 2025-12-12T03:23:16.235779
---

# Scammers Mimic Cloudflare’s ‘Error 451’ Site Blocking Notice to Infect Pirates

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

# Scammers Mimic Cloudflare’s ‘Error 451’ Site Blocking Notice to Infect Pirates

today by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Piracy](https://torrentfreak.com/category/piracy/ "Go to the Piracy category archives.") >

Earlier today we saw fairly compelling evidence that blocking pirate sites can lead to internet users being infected with malware. Apparently inspired by Cloudflare's use of HTTP Error 451, which greets pirates when attempting to visit sites blocked in the UK, unknown actors mimicked Cloudflare's site blocking page and then attempted to trigger malicious scripts.

![error-451](https://torrentfreak.com/images/error-451lrs.png)
Anti-piracy groups provide regular reminders that pirate sites expose users to malware and related security risks. In some cases, no action is required for users to come to harm, all they have to do is visit a malicious site.

While not the most common route of infection, under the right circumstances that can indeed happen. Yet something we saw for ourselves this week may go even further than that.

When blocking measures are deployed against dozens of sites, there’s a period of uncertainty in which many pirates are traditionally less cautious about visiting alternative sites. For those who benefit from internet users clicking first and thinking later, there’s arguably no better time to target pirates. In the context of recent developments, targeting pirates before they even set foot on a pirate site, using a distraction they may already be familiar with, is something we haven’t seen before.

So why now?

## Fewer Options For UK Pirates

Around early September, Cloudflare suddenly began [blocking pirate sites in the UK](https://torrentfreak.com/cloudflare-starts-blocking-pirate-sites-for-uk-users-thats-a-pretty-big-deal-250715/). Cloudflare’s unique position in the market is certainly not lost on the major movie and TV studios, and it’s a matter of record that they view voluntary cooperation as the best way forward.

What prevented Cloudflare from digging a trench in opposition to site-blocking hasn’t been revealed. However, since adversarial cases at the High Court tend to get quite noisy, and Cloudflare appears to have been added to existing, long-running blocking injunctions rather more quietly, something else may have happened.

If the instructions are the same as those issued to ISPs, Cloudflare’s blocking targets include dozens of branded pirate streaming sites, in some cases clustered under common control or ownership, plus the countless domains they have already deployed and are yet to deploy, to circumvent UK site blocking measures.

## Exploiting The Fallout from Blocking Measures

During mid-November, an existing blocking injunction was updated with the addition of approximately 150 fully qualified domain names (FQDNs), which precisely identify resources using their hostnames, domain names, and top-level domains. The ‘pirate brands’ involved are as high profile as they come: Sflix, GoMovies, 123movies, Solarmovies, Fmovies, Soap2Day, Hurawatch, and Bflix, plus more recent upcoming brands such as Boomflix and Moonflix.

Early this month, a notice from the MPA referencing High Court injunction application [IL-2021-000027](https://lumendatabase.org/notices/75453605?access_token=F1EZdpSwSWmRgDcy1yzS0w) was posted by Cloudflare to the Lumen Database. Originally granted in 2021, a note on Lumen suggests that the High Court issued an order on December 8, 2025, presumably to formalize Cloudflare’s role in blocking associated domains.

While we were carrying out tests and making inquiries to determine Cloudflare’s response, a familiar notice appeared in connection with a domain that felt familiar. In the company of Sflix, MyFlixer, Bflix and Flixbaba, Flixerplus stood out no more than Cucuflix or Flixmomo.

For UK pirates tired of ISP blocking, now with added Cloudflare and the joy of intermittent VPN blocking on top, it may even represent hope. Unfortunately, the notice below suggests otherwise.

*Error 451 – Unavailable for Legal Reasons?*

![error451](https://torrentfreak.com/images/errorrr451.png)

Aside from some unusual additional characters, the Error HTTP 451 notice is similar to previous blocking notices published by Cloudflare for the same reasons. A cautious hover over the link to the order on the Lumen Database revealed nothing untoward either.

Yet, near the bottom, why would Cloudflare “Thank you for your !” ?

## Not a Cloudflare Notice, But a Serious Distraction

While the Flixerplus domain has a relatively small online footprint, it’s not new. This means it doesn’t trigger precautionary security features that deny access to DNS for newly registered domains. The WHOIS records raise no alarms either.

The 451 notice being served over HTTP, instead of HTTPS, is a big red flag, however. The same goes for the questionable domains the site attempts to access in the background, and what appears to be an iframe loading a script (or scripts) from an external source. As far as we can tell, regular anti-virus vendors have yet to detect this.

URLScan [reveals](https://urlscan.io/result/019b0978-62b5-7259-ab34-a947a919a30e/) some of the broader picture. URLQuery [reveals](https://urlquery.net/report/8ef11320-d938-4722-815f-bfaa2a1ccd44) that the same attack also [exists elsewhere](https://urlquery.net/report/e081c164-edcf-4b6a-ac00-088243bed9c1), in connection with similarly branded sites.

*![](https://torrentfreak.com/images/threats-1.png)*

DNS providers have already taken action against an underlying network, but whether that will have enough impact is currently unknown.

At the time of writing, Cloudflare has not responded to our request for comment. As for Flixerplus, it may stick around for a while. Unlike the domains Cloudflare will likely be required to block, Flixerplus doesn’t appear to be listed for blocking in the UK, or indeed anywhere else.

* [Previous Post![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-right.svg)](https://torrentfreak.com/rampant-u-s-piracy-is-a-multibillion-dollar-concern-for-japanese-manga-publishers/)

### Tagged In:

* [Cloudflare](https://torrentfreak.com/tag/cloudflare/)
* [site blocking](https://torrentfreak.com/tag/site-blocking/)

### You Might Also Like:

[![](https://torrentfreak.com/images/computerkeyboardfeat-500x210.png)

Anti-Piracy

### Belgium’s Latest Pirate Site-Blocking Order Spares DNS Providers

* December 5, 2025, 09:36 by Ernesto Van der Sar](https://torrentfreak.com/belgiums-latest-pirate-site-blocking-order-spares-dns-providers/)

[![](https://torrentfreak.com/images/aus-feat-500x210.jpg)

Anti-Piracy

### Court Empowers Hollywood in Race to Block “Wicked: For Good” Piracy

* December 4, 2025, 14:31 by Andy Maxwell](https://torrentfreak.com/court-empowers-hollywood-in-race-to-block-wicked-for-good-piracy-251204/)

[![](https://torrentfreak.com/images/server-block1-500x210.png)

Anti-Piracy

### DDoS Guard: LaLiga’s Piracy Blocks Test Whether Anyone Will Protect the Internet

* December 3, 2025, 09:25 by Andy Maxwell](https://torrentfreak.com/ddos-guard-laligas-piracy-blocks-test-whether-an...