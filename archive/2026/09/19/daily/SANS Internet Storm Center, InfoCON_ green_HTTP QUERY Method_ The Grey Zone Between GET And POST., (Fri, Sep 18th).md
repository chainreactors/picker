---
title: HTTP QUERY Method: The Grey Zone Between GET And POST., (Fri, Sep 18th)
url: https://isc.sans.edu/diary/rss/33352
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-19
fetch_date: 2026-09-20T07:16:54.141057
---

# HTTP QUERY Method: The Grey Zone Between GET And POST., (Fri, Sep 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33348)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [HTTP QUERY Method: The Grey Zone Between GET And POST.](/forums/diary/HTTP%2BQUERY%2BMethod%2BThe%2BGrey%2BZone%2BBetween%2BGET%2BAnd%2BPOST/33352/)

**Published**: 2026-09-18. **Last Updated**: 2026-09-19 04:51:46 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/HTTP%2BQUERY%2BMethod%2BThe%2BGrey%2BZone%2BBetween%2BGET%2BAnd%2BPOST/33352/#comments)

In June 2026 the IETF published RFC 10008[[1](https://www.rfc-editor.org/info/rfc10008/)], defining a new HTTP method: "QUERY". The HTTP protocol faced already by changes (HTTP/2, HTTP/3) but it’s the first new standard HTTP verb since "PATCH" in 2010!

This new method sits between “GET” and “POST” and can be resumed like this: “QUERY is a GET with a body**”.** It's safe and idempotent: the request is processed without state change and can be automatically repeated or restarted without concern for partial state changes. The query itself lives in the request body instead of the URL, and it's explicitly cacheable. Servers advertise the body formats they'll accept via a new “Accept-Query” response header.

If you defend web infrastructure, the interesting part isn't the RFC. The risk is that every control you own that pattern-matches on HTTP methods was written before "QUERY" existed.WAF rules, API-gateway allowlists, CSRF middleware, cache keying, load-balancer method handling is written in terms of a known verb set: GET, POST, PUT, DELETE, PATCH.  Drop a sixth verb that behaves like a hybrid of the first two into that world and each control now has to make a *deliberate* decision about it. Most of them currently make an accidental one.

And the behaviour in the wild is genuinely inconsistent. Researchers found that nginx's limit\_except pattern and Django's View class reject QUERY outright, while curl, FastAPI's explicit routes, Caddy and Traefik pass it through untouched. On caching, one researcher built a QUERY-only API and found nginx forwards it happily and caches it never[[2](https://dev.to/alexgeorgiev17/nginxs-limitexcept-block-silently-rejects-the-new-http-query-method-1gcg)].

Think about this HTTP request:

```

curl -X QUERY https://target.com/api/search \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "q=' OR 1=1--" -v
```

If your WAF signatures (SQLi, XSS, command injection) are bound to "POST" bodies but never taught that "QUERY" also carries a body, you get a clean inspection bypass. The test is trivial: send the same malicious payload over "POST" and over "QUERY" and diff the outcome. If the "QUERY" version sails through where the "POST" version gets blocked, that's a live gap, not a theoretical one.

Because "QUERY" is cacheable and safe by spec, caches that don't key on the full request body can be poisoned into serving one user's malicious payload to the next, and CSRF middleware hardcoded to the classic state-changing verbs will wave through any "QUERY" endpoint that carries an unintended side effect.

The new method is not popular yet, here is an overview of what I found:

| Layer | Component | Status |
| --- | --- | --- |
| Clients | curl | Works today via "-x query" |
|  | Node.js / fetch (server-side), Python (httpx/requests), Go net/http, Rust reqwest | Already let you send arbitrary method strings, so QUERY works between your own services right now |
|  | Browser fetch() / XHR | Can send it, but QUERY is not CORS-safelisted → always triggers an OPTIONS preflight; browser HTTP cache should not be assumed to cache QUERY responses yet |
|  | .NET 10 | First-class support out of the box |
|  | HTTP.jl (Julia) | Merged June 2026 — client + server, retries, redirect handling, Accept-Query |
| Servers / proxies | nginx | Proxies it, never caches it. Four identical QUERY requests hit the backend four times; four POSTs hit it once. Also, the limit-except pattern silently rejects QUERY. |
|  | Caddy, Traefik | Pass it through untouched |
|  | Apache | Needs config adjustment to recognize the method and handle OPTIONS/CORS |
| Frameworks | Fast API | Explicit routes pass it through |
|  | Django | The `View` class rejects it outright |
|  | Spring (Java) | Maintainers deliberately scoping it down to "teach the framework QUERY exists" and waiting on adoption feedback before expanding |
| CDN | Cloudflare, Akamai | Co-authored the RFC, so edge/CDN support is expected to lead framework support, but reliable at-scale QUERY caching isn't there yet |

What can you actually do?

Update your rules/regexes to support the new verb:

```

http.method in ("GET","POST", "QUERY")
```

I searched across my HTTP-related logs and found no occurrence of QUERY request but it’s for sure a question of time.

And from a malware point of view? Is there a risk? Most of what a modern SOC actually relies on to catch C2 is behavioral, and behavioral detection doesn't care about the verb:

* Beaconing analysis (RITA/AC-Hunter-style connection-count and interval work), jitter/timing, volume, and flow shape are all method-agnostic. A "QUERY" beacon beacons exactly like a "POST" beacon.
* JA3/JA4 and TLS fingerprinting sit below the HTTP method entirely.
* For HTTPS C2 — which is nearly everything now — the method is inside  the TLS tunnel. A network sensor without interception never sees "GET" vs "POST" vs "QUERY" in the first place, so "QUERY" changes nothing unless you're decrypting.

[1] <https://www.rfc-editor.org/info/rfc10008/>
[2] <https://dev.to/alexgeorgiev17/nginxs-limitexcept-block-silently-rejects-the-new-http-query-method-1gcg>

Xavier Mertens (@xme)
Senior ISC Handler | SANS Principal Instructor | Freelance Consultant
[Xameco](https://xameco.be) | [PGP Key](https://xameco.be/pgpkey.txt)

Keywords: [Body](/tag.html?tag=Body) [GET](/tag.html?tag=GET) [HTTP](/tag.html?tag=HTTP) [Method](/tag.html?tag=Method) [POST](/tag.html?tag=POST) [QUERY](/tag.html?tag=QUERY) [RFC](/tag.html?tag=RFC)

[0 comment(s)](/diary/HTTP%2BQUERY%2BMethod%2BThe%2BGrey%2BZone%2BBetween%2BGET%2BAnd%2BPOST/33352/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33348)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/lice...