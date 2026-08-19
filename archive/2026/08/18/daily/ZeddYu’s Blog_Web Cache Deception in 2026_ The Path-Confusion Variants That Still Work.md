---
title: Web Cache Deception in 2026: The Path-Confusion Variants That Still Work
url: https://blog.zeddyu.info/2026/08/18/Web-Cache-Deception-Path-Confusion-2026/
source: ZeddYu’s Blog
date: 2026-08-18
fetch_date: 2026-08-19T02:56:16.188335
---

# Web Cache Deception in 2026: The Path-Confusion Variants That Still Work

* [Skip to primary navigation](#site-nav)
* [Skip to content](#main)
* [Skip to footer](#footer)

[ZeddYu's Blog](/)

Toggle menu

### [ZeddYu](https://blog.zeddyu.info/)

Security Researcher. HTTP Smuggling, Web Security, CTF.

Follow

# [Web Cache Deception in 2026: The Path-Confusion Variants That Still Work](https://blog.zeddyu.info/2026/08/18/Web-Cache-Deception-Path-Confusion-2026/)

4 minute read

#### On this page

* [The original trick, restated as a parser differential](#the-original-trick-restated-as-a-parser-differential)
* [Why it survived nine years](#why-it-survived-nine-years)
* [The 2026 variants worth testing](#the-2026-variants-worth-testing)
* [Detection and the actual fix](#detection-and-the-actual-fix)

Most of the parser-differential work on this blog has been about two servers on one connection disagreeing over where a request ends. [Request smuggling](/2026/05/16/Revisiting-HTTP-Smuggling-2026/) is the canonical case. But the same underlying bug, two parties parsing one string differently, shows up anywhere two systems interpret a URL and only one of them makes a security decision from it. The clearest non-smuggling example is [web cache deception](https://portswigger.net/web-security/web-cache-deception), and despite being nine years old it is still live on real infrastructure in 2026, for reasons that are structural rather than incidental.

## The original trick, restated as a parser differential

Omer Gilâs 2017 âWeb Cache Deceptionâ attack is usually explained as a caching bug. It is more precisely a disagreement between two parsers. The victim is sent a URL like:

```
https://site.example/account/settings/nonexistent.css
```

The origin routes this to the `account/settings` handler and ignores the trailing `/nonexistent.css`, so it returns the victimâs authenticated account page. The cache in front of the origin makes a different decision: it sees a path ending in `.css`, concludes the response is a static asset, and stores it. The attacker then requests the same URL and is served the victimâs cached account page.

Nothing here is a caching bug in isolation, and nothing is a routing bug in isolation. The vulnerability is the delta between the originâs parser (which treats the path as `account/settings` plus ignored trailing junk) and the cacheâs parser (which treats the same path as âa thing ending in `.css`â). That is the identical shape as a CL/TE desync, moved from the connection layer to the caching layer.

## Why it survived nine years

The 2020 USENIX study âCached and Confusedâ measured this class in the wild and found it widespread; the surprising part in 2026 is how little changed. The reason is that the two decisions genuinely live in two different systems with two different design goals, and neither one is obviously wrong on its own:

* The **cache** wants to be cheap and fast, so it decides cacheability with a heuristic on the path: static-looking extensions, or a static path prefix. It usually does not consult the originâs routing logic, because that would defeat the point of caching.
* The **origin** framework wants to be forgiving, so it routes on the meaningful part of the path and tolerates trailing segments, path parameters, and encoded characters that the developer never thinks about as security-relevant.

Fixing it requires the two systems to agree on how the path is parsed, and they are built by different vendors, deployed by different teams, and tuned for different things. That is exactly why request smuggling persisted too. Agreement across a trust boundary is the hard part; each side in isolation looks fine.

## The 2026 variants worth testing

The plain `.css` suffix is patched on the obvious targets now, usually by the cache being taught not to cache authenticated responses regardless of extension. What still works are the variants that exploit a finer-grained parsing disagreement, where the cache and origin split the path at a different point:

1. **Delimiter discrepancies.** The origin treats `;`, or a path parameter, or an encoded `%3F` as ending the meaningful path; the cache does not, or vice versa. `GET /account/settings;x.css` can route to `account/settings` at the origin while the cache keys and caches the whole string as static.
2. **Encoded-slash disagreement.** `%2F` is where a lot of these live. If the cache decodes `%2F` before pattern-matching and the origin does not, or the reverse, the two see different path structures for the same bytes.
3. **Newline and null truncation in the cache key.** A cache that truncates its key at `%0A` or `%00` while the origin serves the full path lets an attacker cache a sensitive response under a key the victimâs own requests will also hit.

Every one of these is a controlled experiment: send the same crafted path through the stack, capture what the origin returns and whether the cache stored it, and vary one delimiter at a time. The methodology is the one from the smuggling work, just with âdid the cache store an authenticated responseâ as the oracle instead of âdid the next request get poisoned.â

## Detection and the actual fix

The robust fix is the same principle that eventually tamed smuggling: stop inferring, start agreeing. Concretely, the cache should cache a response only when the origin explicitly authorises it through `Cache-Control`, rather than guessing from the URLâs extension. An origin that returns `Cache-Control: no-store` on every authenticated response closes the whole class regardless of how the path is parsed, because the cache no longer has a decision to get wrong. Where extension-based caching is unavoidable, the cache and origin must share one normalisation library so that `%2F`, path parameters, and trailing segments resolve identically on both sides before either makes a decision.

On the defensive-monitoring side, the signal is a cache storing a response that carries a `Set-Cookie` or an authenticated body, keyed under a static-looking path. That combination should never happen and is cheap to alert on.

Web cache deception is not a clever edge case that will be designed away. It is the caching layerâs version of the same disagreement that request smuggling exploits at the connection layer, and it will keep working for exactly as long as caches and origins are allowed to parse the same URL differently.

**Tags:**

[cache-poisoning](/tags/#cache-poisoning),
[cdn](/tags/#cdn),
[parsing-differentials](/tags/#parsing-differentials),
[web-cache-deception](/tags/#web-cache-deception),
[web-security](/tags/#web-security)

**Categories:**

[research](/categories/#research)

**Updated:** August 18, 2026

[Previous](/2026/07/06/HTTP2-Downgrade-ALB-Style-Reverse-Proxies/ "HTTP/2 Downgrade Attacks Against ALB-Style Reverse Proxies: Where the Desync Actually Lives")
Next

* [Feed](/feed.xml)

© 2026 [ZeddYu's Blog](https://blog.zeddyu.info). Powered by [Jekyll](https://jekyllrb.com) & [Minimal Mistakes](https://mademistakes.com/work/jekyll-themes/minimal-mistakes/).