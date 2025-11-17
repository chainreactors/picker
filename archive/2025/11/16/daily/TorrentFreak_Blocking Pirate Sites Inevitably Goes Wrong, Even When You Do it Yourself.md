---
title: Blocking Pirate Sites Inevitably Goes Wrong, Even When You Do it Yourself
url: https://torrentfreak.com/blocking-pirate-sites-inevitably-goes-wrong-even-when-you-do-it-yourself-251116/
source: TorrentFreak
date: 2025-11-16
fetch_date: 2025-11-17T03:12:52.698147
---

# Blocking Pirate Sites Inevitably Goes Wrong, Even When You Do it Yourself

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

# Blocking Pirate Sites Inevitably Goes Wrong, Even When You Do it Yourself

today by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

Support for site or content blocking measures usually turns on individual needs. Equally, those who object to blocking pirate sites, may be enthusiastic supporters of blocking abusive ads, trackers, and malware. Internet users should be free to block whatever they like, piracy included. But as a novel 'anti-piracy' blocklist reveals, when things inevitably go wrong, transparency puts things right.

![overblocking-s](https://torrentfreak.com/images/overblocking-s.png)
Today’s internet is arguably better than it’s ever been. Yet there are significant privacy and security concerns that, despite best efforts, only seem to be getting worse.

Calls for governments to get much more involved carry the not insignificant risk of them doing just that. Not necessarily to tackle the issues that led to the cordial invitation, of course, but when blocking and access restrictions are heavily promoted as the solution to one problem, suddenly everyone has a problem. Governments looking for solutions unsurprisingly have many times more.

## The Normalization of Blocking

A little over fifteen years ago, there wasn’t much appetite for online blocking, at least beyond abusive images and videos, for which blocking still receives overwhelming public support. Today it doesn’t really matter if the public approves or not, site blocking is permitted almost everywhere. Whether for suppressing piracy or silencing perceived overseas propaganda, or brandished as punishment for [non-compliance with local rules](https://torrentfreak.com/uk-govt-finds-ideal-pirate-bay-poster-boy-to-sell-blocking-of-non-pirate-sites-250824/), the potential seems unlimited.

Yet the majority of content blocking experienced day-to-day isn’t imposed, it’s a personal choice. Most browsers have an option to block popups, for example. Blocking intrusive advertising is increasingly popular too, since without some type of defense, any veneer of online privacy quickly heads south, taking usability with it. For many, the browser-based [uBlock Origin](https://github.com/gorhill/uBlock) remains the gold standard but thanks to ISPs’ site blocking efforts, running software like [Pi-hole](https://pi-hole.net/) takes care of the ads and with its own DNS, simultaneously unblocks the pipes.

For those averse to tinkering under the hood, personal blocking performance is almost completely reliant on the decisions made by third-party blocklist maintainers. Make the right decisions and deploy reputable blocklists, overall things can go very well indeed. That doesn’t necessarily mean *everything* always goes according to plan, but with the right approach, getting back on track is simplicity itself.

## Blocklists Always Contain Errors

The standard lists bundled with uBlock Origin and Pi-hole are generally perceived as very good. Indeed, many view uBlock as an indispensable first line of defense against the endless appearance of malicious ads. On GitHub, all kinds of DNS blocklists are available from [Hagezi’s repo](https://github.com/hagezi), all with a common and genuine mission to keep the internet as ‘clean’ and as safe as possible.

Essentially a one-man labor of love crammed into his spare time, by many accounts Hagezi’s main lists strike a fair balance between blocking unwanted trackers and not breaking websites, which for most people is the sweet spot. For those with more specific needs, there’s no shortage of choice.

![blocklists-2](https://torrentfreak.com/images/blocklists-2.png)

The threat intelligence-led [blocklist](https://github.com/hagezi/dns-blocklists#tif) has been used here without any issues, likewise the [feed for NRDs](https://github.com/hagezi/dns-blocklists#nrd) (newly registered domains) which often contains new streaming site domains, purchased as replacements in the wake of anti-piracy blocking. Others clearly have specific goals in mind, one in particular.

## The ‘Anti Piracy – Protects Against Piracy!’ Blocklist

This blocklist contains [over 11,000 entries](https://github.com/hagezi/dns-blocklists?tab=readme-ov-file#piracy), in theory blocking access to just as many pirate sites. In practice, it may block a few thousand but since domains come and go quickly, only well-funded anti-piracy groups have the necessary resources to stay anywhere near up to date, and the list naturally reflects that.

No third-party list will ever be comprehensive, and this one makes no claims to the contrary. Indeed, a [disclaimer](https://github.com/hagezi/dns-blocklists/blob/main/README.md#disclaimer) concerning all lists notes that the ultimate responsibility for using or not using a blocklist lies with the user. We completely agree, and we’ll return to that in just a moment.

The fact that many domains on the list today fell out of action a decade or more ago, presents issues. These issues are not unique to this blocklist; they also apply to any region where enthusiasm for pirate site blocking isn’t matched by corresponding unblocking when domains are repurposed.

**The key differences deserve early emphasis:** Pirate site blocking lists are imposed and either fully closed or open to limited scrutiny. Hagezi’s blocklists are free, voluntary, and transparent. While that means errors get pointed out (see below), that’s what gives open source its strength.

**Welcometothescene.com** was home to [The Scene](https://www.imdb.com/title/tt2201890/plotsummary/), a drama miniseries set around the topic of piracy. Created by Jun Group, the show was free to watch online, including on peer-to-peer networks, under a Creative Commons license. Released to a pre-YouTube audience in 2004, the last episode aired 20 years ago.

Long since repurposed, the domain appears both dead and alive in DuckDuckGo’s search results, and very much alive in the Anti-Piracy Blocklist.

![the-scene-search](https://torrentfreak.com/images/the-scene-search.png)

How the domain got onto the anti-piracy blocklist is anyone’s guess, likewise why it’s somehow still there today. Other problematic entries are more current and at times, quite puzzling too.

## A Few Examples

We’ve highlighted a few obvious blunders below, but the context means that when compared to similar blunders made elsewhere, these are much less serious. Mistakes are inevitable, yet transparency and the ability to put things right make a world of difference.

> **Open Source Projects**
>
> *[torrent.fedoraproject.org](https://torrent.fedoraproject.org/) | [torrent.ubuntu.com](https://torrent.ubuntu.com/) | [fosstorrents.com](https://fosstorrents.com/) | tracker.parrotlinux.org | tracker.parrotsec.org | [Webtorrent.io](https://webtorrent.io/) | [Instant.io](https://github.com/webtorrent/instant.io)*
>
> **Free Music / Independent Artists / Pro-Sharing Bands**
>
> *Jamendo.com | bt.etree.org*
>
> **Anti-Piracy |...