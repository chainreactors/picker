---
title: Who Is aocr.org and Why Is It Reading My Blog?
url: https://blog.zsec.uk/aocr-org-referrer-bot/
source: ZephrSec - Adventures In Information Security
date: 2026-11-07
fetch_date: 2026-11-08T08:14:53.337606
---

# Who Is aocr.org and Why Is It Reading My Blog?

[Skip to content](#main)

[![ZephrSec - Adventures In Information Security](/content/images/size/w400/2025/05/YoutubeHeader-Recovered-1.png)](https://blog.zsec.uk)

* [About Andy Gill/ZephrFish](https://blog.zsec.uk/about/)
* [My Red Team Course](https://lms.zsec.red/courses/malwareless-adversarial-emulation)
* [ZephrSec](https://zephrsec.com)
* [My Books](https://leanpub.com/b/LearningTheRopes)
* [Photo Blog](https://photos.zsec.uk/)

[Buy me a coffee](https://blog.zsec.uk/support/)

Toggle colour scheme
[Buy me a coffee](https://blog.zsec.uk/support/)
[Subscribe](#/portal/signup)
Menu

[blueteam](/tag/blueteam/)

# Who Is aocr.org and Why Is It Reading My Blog?

A radiology college started 'sending' me traffic. In reality, it wasn't. Unpicking a headless crawler with a fake referrer, rotating proxies and a ByteDance-shaped fingerprint, and blocking it with a single Cloudflare rule.

[Andy Gill](/author/andy/)
/
7 November 2026
/
8 min read
/

 views

![](/content/images/size/w30/2026/11/IMG_0555-1.jpg)
![Who Is aocr.org and Why Is It Reading My Blog?](/content/images/size/w1200/2026/11/IMG_0555-1.jpg)

On this page

On this page

A bit of a post out of the norm but a little investigation into some interesting behaviour I saw in my logs.

While tidying up `404` entries on this blog, I kept seeing one referrer in my nginx logs: `https://www.aocr.org/`. It was linked to old URLs that no longer exist, it hit dozens of posts, and it showed up in my analytics. A new site linking to my work would be nice, however upon further investigation the problem is that aocr.org is the **American Osteopathic College of Radiology**, and I'm fairly sure they aren't reading about Kerberoasting or NUC lab builds.

This post covers how I worked out what it was, what it costs a small site, and the one Cloudflare rule that deals with it. Ege Demir has already published an excellent deep dive on the same bot ([tin.computer: the aocr.org referrer bot](https://tin.computer/blog/aocr-org-referrer-bot?ref=blog.zsec.uk)), and I'll draw on it. Below are my own numbers from an independent vantage point, which line up closely with theirs.

## TL;DR

* **What:** a headless Chrome crawler that sends a fake `Referer: https://www.aocr.org/` on every request. Nobody clicked a link.
* **How it hides:** it uses a new proxy IP for almost every page (368 IPs for 1,524 requests), so per-IP rate limits, fail2ban and IP blocks never fire.
* **Why it matters:** it runs your JavaScript, so it shows up in analytics as real readers or at least hides as one. On my worst day it made up about **20% of all page views**.
* **Who:** the tin.computer research found its TLS/HTTP/2 fingerprint matches ByteDance's Bytespider. Who actually operates it is **not proven** but the fingerprints do match which is interesting.
* **Fix:** one Cloudflare WAF custom rule on the referrer, set to Managed Challenge to block basically bot traffic.

## How it turned up

I was auditing 404s across the blog by cross-referencing 92 days of nginx logs against the sitemap, my analytics data and every internal link. Most 404s on any public site are scanner noise (`/wp/`, `/cms/`, `/two-factor-challenge/` and friends), so I only kept 404s that looked like real page slugs or had a real external referrer.

Two hits stood out: `/steelcon2023-workshop/` and `/csv-dangers-mitigations/4/`, both "referred" by `aocr.org`. They're old URLs and not linked anywhere recently but they're also *not related to each other at all*. The first is a page I've since moved, and the second looks like pagination from a previous version of the site. I thought it was pretty odd for a live link, and typical of a crawler working from a stale URL list (an archive, an old crawl, a dataset).

So I pulled every request with that referrer:

```
zcat -f /var/log/nginx/access.log* \
  | awk -F'"' '$4 ~ /aocr\.org/' > aocr.log
wc -l aocr.log
awk '{print $1}' aocr.log | sort -u | wc -l
awk -F'"' '{print $6}' aocr.log | sort | uniq -c
awk -F'"' '{print $4}' aocr.log | sort | uniq -c
```

## What the logs show

|  |  |
| --- | --- |
| Requests with the aocr.org referrer | **1,524** |
| First / last seen | 28 Sep 2026 → 7 Nov 2026 (my logs start 27 Sep, so it may be older) |
| By month | Sep 35 · Oct 273 · **Nov 1,216** (almost all on 5–7 Nov) |
| Distinct client IPs | **368** (all IPv4) |
| Distinct user agents | **1** |
| Distinct referrers | **1**: exactly `https://www.aocr.org/`, never a specific page |
| Posts crawled | **72** distinct posts, 210 page loads |

### One browser but seemingly hundreds of addresses

Every request used the same user agent:

```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
```

That's several major versions behind what my real visitors run. Meanwhile, the IPs barely ever repeated, of the 184 addresses that loaded an actual page, **161 loaded exactly one page and never came back**, 20 loaded two and 3 loaded three. That's the signature of a rotating proxy pool: every request leaves through a fresh exit, so no per-IP threshold ever trips.

The exits are a mix of hosting and what look like residential IPs or regular ISP consumer connections. Among the busiest:

* **EGIHosting** (US), a host often resold as proxy capacity
* **Television Internacional, S.A. de C.V.** (Mexico), cable broadband
* **Coop. Entrerriana de Comunicaciones** (Argentina), a regional co-op ISP
* **Link3 Technologies** (Bangladesh), an ISP
* a RIPE-registered netblock (Netherlands)

A random sample of 25 exits came out as US 10, NL 7, FR 2, AU 2, and one each for TW, RO and IN. EGIHosting also appears in the tin.computer ASN breakdown, alongside Datacamp/CDN77, Web2Objects, M247 and others. A genuine link on a US medical association's site would bring a US-heavy crowd on ordinary connections, not this.

### It's a real browser, and it runs JavaScript

This was the most useful clue from everything, it is what pointed me at thinking it might have been playwright or headless chrome, of those 1,524 requests, only 210 were page loads. The rest were the side effects of a full browser rendering the page and running its scripts:

| Request type | Count |
| --- | --- |
| Ghost Portal/Content API calls (settings, tiers, newsletters) | 537 |
| Ghost Members API calls | 360 |
| Images and assets | 238 |
| Page loads | 210 |
| Analytics page-view beacons | 179 |

A plain scraper that only downloads HTML never touches `/members/api/` or fires an analytics beacon, however this one does, so it's driving a real (headless) Chrome. The `tin.computer` write-up referenced further up goes further, with session recordings that show a ~28-second wait and scroll per page, an 800×600 screen, `Asia/Shanghai` as the time zone, and browser timing fields named after ByteDance's internal resource loader.

### What it costs a small site

Load isn't the issue as I've got caching and things setup, so a few thousand requests over a few days is nothing. **Analytics is the annoying part** because the bot fires real page-view beacons, it gets counted as readers:

| Day | Bot beacons | All beacons | Share |
| --- | --- | --- | --- |
| 5 Nov | 81 | 415 | **~20%** |
| 6 Nov | 51 | 379 | ~13% |
| 7 Nov | 14 | 832 | ~2% |

On a site where "popular posts" and per-post view counters are driven by those numbers, a fifth of a day's views being fake skews the ranking. They also count against analytics API quotas.

The same user agent also appears about 2,800 more times in my logs with **no** referrer. I can't prove those are the same crawler, but the user-agent match, the timing and the lack of client hints make it likely. If so, the referrer is only the part that's easy to see.

## Who is behind it?

My data alone only gets as far as "an automated browser behind rotating proxies with a fixed fake referrer". The attribution comes from Ege Demir's research, which found:

* **199 of 199** aocr.org-style requests matched Bytespider's network fingerpri...