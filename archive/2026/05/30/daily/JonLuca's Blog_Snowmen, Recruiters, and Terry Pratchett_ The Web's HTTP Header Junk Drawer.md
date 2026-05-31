---
title: Snowmen, Recruiters, and Terry Pratchett: The Web's HTTP Header Junk Drawer
url: https://jonlu.ca/posts/http-headers-top-1000
source: JonLuca's Blog
date: 2026-05-30
fetch_date: 2026-05-31T06:10:39.664235
---

# Snowmen, Recruiters, and Terry Pratchett: The Web's HTTP Header Junk Drawer

[Skip to content](#main-content)

JonLuca's Blog

[Posts](/ "Posts")[About](/about "About")[Contact](/contact "Contact")[Interesting Snippets](/interesting-snippets "Interesting Snippets")

May 30, 2026

# Snowmen, Recruiters, and Terry Pratchett: The Web's HTTP Header Junk Drawer

I crawled the top 1,000 sites and read their response headers. Browser fossils, CDN breadcrumbs, leaked codenames, a snowman, and a tribute to Terry Pratchett.

HTML is what a site shows you. JavaScript is what it does. Headers are what it canât help telling you.

They leak the habits of the machinery underneath: CDNs, frameworks, caches, security controls, dead browser workarounds, migration scars, and bits of infrastructure that were meant to be temporary and never left. I thought it would be interesting to see what unique or non-standard headers the most popular sites on the internet were serving, so I crawled the top 1,000 domains by traffic and saved their response headers.

For each domain I hit the root page, then one same-origin internal page when I could find one safely. I used a browser-like HTTP client and retried likely challenge pages once with Playwright. If a response still looked like a WAF, a bot wall, or an access-denied page, I logged it and dropped it from the stats so they wouldnât skew the header counts.

## [#](#the-dataset) The dataset

Of the 1,000 domains I attempted, 417 returned clean pages I could analyze; the rest were WAFs, bot walls, or challenge pages I dropped. Those clean sites sent 677 distinct header names, and 619 of them arenât in the IANA HTTP Field Name Registry.

All ânot in IANAâ means is that the name isnât registered. The web runs on standards, but it also runs on convention, vendor prefixes, CDN metadata, and whatever someone shipped five years ago that still works. Learn only the standardized headers and youâll have the formal grammar of the web while missing the dialect anyone actually speaks.

## [#](#browser-fossils) Browser fossils

The crawl turned up a whole fossil bed:

| header | sites | note |
| --- | --- | --- |
| `x-xss-protection` | 178 | Chromeâs old XSS auditor switch |
| `pragma` | 84 | deprecated, but still used for cache control |
| `p3p` | 24 | compact privacy policies for old Internet Explorer cookie behavior |
| `x-ua-compatible` | 13 | Internet Explorer document-mode hint |
| `expect-ct` | 6 | certificate transparency enforcement, now deprecated |
| `feature-policy` | 6 | predecessor to `Permissions-Policy` |
| `content-md5` | 2 | obsoleted integrity header |

`P3P` is my favorite. Itâs a privacy-policy header from the early 2000s, remembered mostly because setting *any* plausible-looking value could talk old IE into accepting third-party cookies. One value in the crawl is exactly the kind of thing you hope to dig up:

```
CP="This is not a P3P policy! See g.co/p3phelp for more info."
```

The header is obsolete. The scar tissue stays.

## [#](#security-headers-are-uneven) Security headers are uneven

Among the 417 eligible sites, adoption of common browser security headers ranged widely:

| header | sites | share |
| --- | --- | --- |
| `strict-transport-security` | 270 | 64.7% |
| `x-frame-options` | 214 | 51.3% |
| `content-security-policy` | 194 | 46.5% |
| `referrer-policy` | 105 | 25.2% |
| `permissions-policy` | 63 | 15.1% |
| `cross-origin-opener-policy` | 45 | 10.8% |
| `cross-origin-resource-policy` | 28 | 6.7% |
| `cross-origin-embedder-policy` | 2 | 0.5% |
| `clear-site-data` | 0 | 0.0% |

Plenty of sites have good reasons to skip some of these, so read the table as a map rather than a scorecard. `COEP` breaks the moment you embed a third-party resource. `Clear-Site-Data` is a sharp tool.

The spread still tells a story. HSTS is now normal. CSP is common but not yet universal. The newer cross-origin isolation headers remain rare. Browser security is a stack of migrations, and most migrations never finish.

## [#](#infrastructure-leaks-through) Infrastructure leaks through

Some headers act as status lights on the machines behind the page.

| header | sites | what it reveals |
| --- | --- | --- |
| `server` | 303 | server or gateway family |
| `x-cache` | 147 | cache state |
| `via` | 146 | proxy/CDN path |
| `x-served-by` | 53 | edge node or cache layer |
| `x-powered-by` | 47 | framework or runtime |
| `x-request-id` | 31 | request tracing |
| `x-generator` | 7 | CMS or static-site generator |

Some `Server` values are dull: `nginx`, `cloudflare`, `gws`, `AkamaiGHost`. Others say more. The crawl found `Express`, `Next.js`, `ASP.NET`, and Drupal generator strings scattered around.

On its own, most of this is harmless operational metadata. But an outsider can use it to cluster sites by stack, host, CDN, framework, and sometimes deployment shape. The public web ships a lot of public implementation detail.

## [#](#the-largest-headers-were-genuinely-large) The largest headers were genuinely large

The biggest header block I saw belonged to `state.gov`, around 15.6 KB. The runners-up were big enough to notice:

| domain | page | approximate header bytes |
| --- | --- | --- |
| `state.gov` | root | 15,622 |
| `state.gov` | internal | 15,620 |
| `eset.com` | internal | 12,819 |
| `mixpanel.com` | internal | 12,554 |
| `cursor.sh` | root | 11,702 |

These are approximate, since the crawler redacts sensitive-looking values before analysis. The point holds: headers can grow into a real chunk of the response. The bulk usually comes from reporting endpoints, CSP directives, cookies, or CDN metadata. The body gets blamed for web bloat, but the prelude packs on weight too.

## [#](#some-headers-are-just-for-fun) Some headers are just for fun

A few headers in the crawl werenât metadata at all. Someone wrote them by hand.

| header | value | site |
| --- | --- | --- |
| `x-clacks-overhead` | `GNU Terry Pratchett` | mozilla.org, debian.org |
| `x-hacker` | a recruiting pitch (full text below) | wordpress.com |
| `x-recruiting` | a recruiting pitch (full text below) | otto.de |
| `x-launch-status` | `Go Flight!` | nasa.gov |
| `x-olaf` | `â` | wordpress.org |
| `x-ballmer` | `bff-section` | welt.de |
| `x-frankenstein-eligible` | `true` | bloomberg.com |
| `x-minion` | `Varnish` | washington.edu |
| `x-asdf` | `l-70` | ivi.ru |

The best one is `x-clacks-overhead`. Mozilla, Firefox, Ubuntu, and Debian all send `GNU Terry Pratchett`, a tribute to the author that started as a fan project and never stopped. It does nothing. Thatâs the point.

Automattic uses headers to recruit. WordPress.com sends `x-hacker: Want root? Visit join.a8c.com/hacker and mention this header.`, and TechCrunch carries a VIP variant pointing at `join.a8c.com/viphacker`. The German retailer Otto runs the same play with `x-recruiting`: âSeems you like http headers. To write ours, apply at [www.otto.de/jobs/](http://www.otto.de/jobs/) and mention this header.â

NASA sends `x-launch-status: Go Flight!`. WordPress.org sends `x-olaf: â`, a snowman.

Others are internal names that escaped. Welt.de has an `x-ballmer`. Bloomberg has `x-frankenstein-eligible`. The University of Washington calls its Varnish cache `x-minion`. Fox News and WPS ship `x-debug-*` headers straight to production, and Xerox leaks its whole feature-flag list through a stack of `rollout-*` headers that quietly admit it runs Remix on Contentful.

Headers are where the web keeps its inside jokes.

## [#](#a-protocol-plus-sediment) A protocol, plus sediment

The clean mental model of HTTP is a request, a response, and a small set of standard fields. The real web is messier, and better for it.

It carries standardized headers and de facto CDN headers, knobs for browsers that barely exist, cache gossip, security policies stuck halfway through adoption, infrastructure quietly naming itself, and the occasional snowman.

Thatâs why headers are worth reading. Theyâre the receipt, and the receipt says the web is still alive, still migrating, and sti...