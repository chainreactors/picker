---
title: Vercel Slams LaLiga Piracy Blocks as “Unaccountable Internet Censorship”
url: https://torrentfreak.com/vercel-slams-laliga-piracy-blocks-as-unaccountable-internet-censorship-250422/
source: TorrentFreak
date: 2025-04-23
fetch_date: 2025-10-06T22:09:27.165812
---

# Vercel Slams LaLiga Piracy Blocks as “Unaccountable Internet Censorship”

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

# Vercel Slams LaLiga Piracy Blocks as “Unaccountable Internet Censorship”

April 22, 2025 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

Cloud-based web application platform Vercel is among the latest companies to find their servers blocked in Spain due to LaLiga's ongoing IPTV anti-piracy campaign. In a statement, Vercel's CEO and the company's principal engineer slam "indiscriminate" blocking as an "unaccountable form of internet censorship" that has prevented legitimate customers from conducting their daily business.

![laliga-vercel1](https://torrentfreak.com/images/laliga-vercel1.png)
Since early February, Spain has faced unprecedented yet avoidable nationwide disruption to previously functioning, entirely legitimate online services.

A court order obtained by top-tier football league LaLiga in partnership with telecommunications giant Telefonica, authorized ISP-level blocking across all major ISPs to prevent public access to pirate IPTV services and websites.

In the first instance, controversy centered on Cloudflare, where shared IP addresses were blocked by local ISPs when pirates were detected using them, [regardless](https://torrentfreak.com/spain-piracy-crisis-cloudflare-says-laliga-knew-danger-blocked-ip-address-anyway-250211/) of the legitimate Cloudflare customers using them too.

When legal action by Cloudflare failed, in part due to a [judge’s insistence](https://torrentfreak.com/judge-confirms-laligas-right-to-block-cloudflare-in-pursuit-of-iptv-pirates-250328/) that no evidence of damage to third parties had been proven before the court, joint applicants LaLiga and Telefonica continued with their blocking campaign. It began affecting innocent third parties early February and hasn’t stopped since.

## Vercel Latest Target

US-based Vercel describes itself as a “complete platform for the web.” Through the provision of cloud infrastructure and developer tools, users can deploy code from their computers and have it up and running in just seconds. Vercel is not a ‘rogue’ hosting provider that ignores copyright complaints, it takes its responsibilities [very seriously](https://vercel.com/guides/how-does-vercel-handle-copyright-infringement-claims).

Yet it became evident last week that blocking instructions executed by Telefonica-owned telecoms company Movistar were once again blocking innocent users, this time customers of Vercel.

*Movistar [informed](https://x.com/skgsergio/status/1912106265599262793) of yet more adverse blocking*

![block-laliga-tinybird](https://torrentfreak.com/images/block-lalia-tinybird.png)

As the thread on X continued, Vercel CEO Guillermo Rauch was asked whether Vercel had “received any requests to remove illegal content before the blocking occurs?”

Vercel Principal Engineer Matheus Fernandes [answered](https://x.com/matheusfrndes/status/1912114969899860243) quickly.

No takedown requests, just blocks

![block-laliga-vercel](https://torrentfreak.com/images/block-laliga-vercel.png)

Additional users were soon airing their grievances; ChatGPT [blocked](https://x.com/JuanEcheverrria/status/1912194827497746584) regularly on Sundays, a whole day “ruined” due to [unwarranted blocking](https://x.com/onticdani/status/1912197061379760132) of AI code editor Cursor, blocking at Cloudflare, GitHub, BunnyCDN, the list goes on.

![shame](https://torrentfreak.com/images/shame.png)

## Vercel Slams “Unaccountable Internet Censorship”

In a joint statement last week, Vercel CEO Guillermo Rauch and Principal Engineer Matheus Fernandes cited the LaLiga/Telefonica court order and reported that ISPs are “blocking entire IP ranges, not specific domains or content.”

Among them, the IP addresses 66.33.60.129 and 76.76.21.142, “used by businesses like Spanish startup Tinybird, Hello Magazine, and others operating on Vercel, despite no affiliations with piracy in any form.”

> *This isn’t a narrowly scoped takedown. LaLiga is a private organization triggering IP-wide blocks that impact critical infrastructure, developers, and businesses—without review, due process, or transparency. These blocks are primarily enforced during LaLiga matchdays, typically on weekends and select weekdays, when live broadcasts occur.*
>
> *ISP-level blocking of individual sites is common. Typically, this is done by inspecting the Server Name Indication (SNI) header during the TLS handshake. SNI contains the hostname in plaintext before encryption, allowing ISPs to block specific domains while leaving other traffic on the same IP untouched, even while the actual traffic is encrypted.*
>
> *But that’s not what’s happening here. Spanish ISPs are blocking entire IPs, ignoring SNI and making no effort to distinguish between hosts. Any website or service behind a blocked IP is taken offline, regardless of its legitimacy.*
>
> *What started as an anti-piracy measure has become an unaccountable form of internet censorship. There’s no distinction between targeted enforcement and mass collateral damage. IPs are being blocklisted wholesale.*

Like all platforms working with user-uploaded content, Vercel receives external complaints concerning potential copyright infringement. Vercel’s latest transparency report reveals that during the latest reporting period it received 1,015 DMCA notices and [restricted content](https://vercel.com/legal/transparency) in response to 1,001 of them. For additional perspective, Vercel has six million users and has a dedicated dispute resolution program, should that be necessary in respect of any complaint.

## Vercel Now in Contact With LaLiga

The details concerning this latest blocking disaster and the many others since February, are unavailable to the public. This lack of transparency is consistent with most if not all dynamic blocking programs around the world. With close to zero transparency, there is no accountability when blocking takes a turn for the worse, and no obvious process through which innocent parties can be fairly heard. While these negatives are a real concern, it appears that tech-savvy Spaniards are embracing the challenge.

In our previous report we highlighted several coding projects that aim to counter the blocking issues in various ways. The [hayahora.futbol](https://hayahora.futbol/) project is especially impressive; it gathers evidence of blocking events, including dates, which ISPs implemented blocking, how long the blocks remained in place, and which legitimate services were wrongfully blocked.

*Vercel blocked IP addresses, who was responsible, and for how long*

![laliga-vercel-hayahora](https://torrentfreak.com/images/laliga-vercel-hayahora.png)

While clearly unhappy with how the company has been treated, Vercel says it’s now [working with LaLiga](https://vercel.com/blog/update-on-spain-and-laliga-blocks-of-the-internet).

“We remain committed to providing fast, secure infrastructure for modern web applications. Likewise, we expect enforcement efforts to do t...