---
title: Unique 0-click deanonymization attack targeting Signal, Discord and hundreds of platform
url: https://gist.github.com/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117
source: Over Security - Cybersecurity news aggregator
date: 2025-01-22
fetch_date: 2025-10-06T20:11:37.152599
---

# Unique 0-click deanonymization attack targeting Signal, Discord and hundreds of platform

[Skip to content](#start-of-content)

Search Gists

Search Gists

[All gists](/discover)
[Back to GitHub](https://github.com)
[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fhackermondev%2F45a3cdfa52246f1d1201c1e8cdef6117)
[Sign up](/join?return_to=https%3A%2F%2Fgist.github.com%2Fhackermondev%2F45a3cdfa52246f1d1201c1e8cdef6117&source=header-gist)

[Sign in](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2Fhackermondev%2F45a3cdfa52246f1d1201c1e8cdef6117) [Sign up](/join?return_to=https%3A%2F%2Fgist.github.com%2Fhackermondev%2F45a3cdfa52246f1d1201c1e8cdef6117&source=header-gist)

You signed in with another tab or window. Reload to refresh your session.
You signed out in another tab or window. Reload to refresh your session.
You switched accounts on another tab or window. Reload to refresh your session.

Dismiss alert

{{ message }}

Instantly share code, notes, and snippets.

[![@hackermondev](https://avatars.githubusercontent.com/u/60828015?s=64&v=4)](/hackermondev)

# [hackermondev](/hackermondev)/**[research.md](/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117)**

Last active
October 3, 2025 23:16

Show Gist options

* [Download ZIP](/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117/archive/dd9abf5eff461694d2e8bf4bd4f5326896f09e30.zip)

* [Star

  889
  (889)](/login?return_to=https%3A%2F%2Fgist.github.com%2Fhackermondev%2F45a3cdfa52246f1d1201c1e8cdef6117)You must be signed in to star a gist
* [Fork

  63
  (63)](/login?return_to=https%3A%2F%2Fgist.github.com%2Fhackermondev%2F45a3cdfa52246f1d1201c1e8cdef6117)You must be signed in to fork a gist

* Embed

  + Embed
     Embed this gist in your website.
  + Share
     Copy sharable link for this gist.
  + Clone via HTTPS
     Clone using the web URL.
  + [Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)

  Clone this repository at &lt;script src=&quot;https://gist.github.com/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117.js&quot;&gt;&lt;/script&gt;
* Save hackermondev/45a3cdfa52246f1d1201c1e8cdef6117 to your computer and use it in GitHub Desktop.

[Code](/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117)
[Revisions
3](/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117/revisions)
[Stars
886](/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117/stargazers)
[Forks
63](/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117/forks)

Embed

* Embed
   Embed this gist in your website.
* Share
   Copy sharable link for this gist.
* Clone via HTTPS
   Clone using the web URL.
* [Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)

Clone this repository at &lt;script src=&quot;https://gist.github.com/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117.js&quot;&gt;&lt;/script&gt;

Save hackermondev/45a3cdfa52246f1d1201c1e8cdef6117 to your computer and use it in GitHub Desktop.

[Download ZIP](/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117/archive/dd9abf5eff461694d2e8bf4bd4f5326896f09e30.zip)

Unique 0-click deanonymization attack targeting Signal, Discord and hundreds of platform

[Raw](/hackermondev/45a3cdfa52246f1d1201c1e8cdef6117/raw/dd9abf5eff461694d2e8bf4bd4f5326896f09e30/research.md)

[**research.md**](#file-research-md)

hi, i'm daniel. i'm a 15-year-old high school junior. in my free time, i [hack billion dollar companies](https://hackerone.com/daniel) and build cool stuff.

3 months ago, I discovered a unique 0-click deanonymization attack that allows an attacker to grab the location of any target within a 250 mile radius. With a vulnerable app installed on a target's phone (or as a background application on their laptop), an attacker can send a malicious payload and deanonymize you within seconds--and you wouldn't even know.

I'm publishing this writeup and research as a warning, especially for journalists, activists, and hackers, about this type of undetectable attack. Hundreds of applications are vulnerable, including some of the most popular apps in the world: Signal, Discord, Twitter/X, and others. Here's how it works:

# Cloudflare

By the numbers, Cloudflare is easily the most popular CDN on the market. It beats out competitors such as Sucuri, Amazon CloudFront, Akamai, and Fastly. In 2019, a major Cloudflare outage knocked most of the internet offline for over 30 minutes.

One of Cloudflare's most used feature is Caching. Cloudflare's Cache stores copies of frequently accessed content (such as images, videos, or webpages) in its datacenters, reducing server load and improving website performance (<https://developers.cloudflare.com/cache/>).

When your device sends a request for a resource that can be cached, Cloudflare retrieves the resource from its local datacenter storage, if available. Otherwise, it fetches the resource from the origin server, caches it locally, and then returns it. By default, [some file extensions](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/) are automatically cached but site operators can also configure new cache rules.

Cloudflare has a vast global presence, with hundreds of datacenters in 330 cities across 120+ countries—an estimated 273% more datacenters than Google. In the U.S. East region, for example, the nearest datacenter to me is less than 100 miles. If you live in a developed country, there's a good chance the nearest datacenter to you is less than 200 miles from you.

A few months ago, I had a lightbulb moment: if Cloudflare stores cached data so close to users, could this be exploited for deanonymization attacks on sites we don't control?

You see, Cloudflare returns information about a request's cache status in the HTTP response.
[![image](https://private-user-images.githubusercontent.com/60828015/404693583-95e1a39a-ed25-4531-9c57-a1b43c616519.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTk3NTI5OTUsIm5iZiI6MTc1OTc1MjY5NSwicGF0aCI6Ii82MDgyODAxNS80MDQ2OTM1ODMtOTVlMWEzOWEtZWQyNS00NTMxLTljNTctYTFiNDNjNjE2NTE5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEwMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMDA2VDEyMTEzNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQ1ZWFkYjFmMTUxOTNkODFkYWQ4MWFmY2I1NzczMTcxOGRmZGFkNDZmN2ZhYjAyZTBmMzY3OTI1MWIzZmYzNmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.Jl72TahcRTDNiDc8nrKjcvBXkxIHbGKqvL-xyqIBpTs)](https://private-user-images.githubusercontent.com/60828015/404693583-95e1a39a-ed25-4531-9c57-a1b43c616519.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTk3NTI5OTUsIm5iZiI6MTc1OTc1MjY5NSwicGF0aCI6Ii82MDgyODAxNS80MDQ2OTM1ODMtOTVlMWEzOWEtZWQyNS00NTMxLTljNTctYTFiNDNjNjE2NTE5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEwMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMDA2VDEyMTEzNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQ1ZWFkYjFmMTUxOTNkODFkYWQ4MWFmY2I1NzczMTcxOGRmZGFkNDZmN2ZhYjAyZTBmMzY3OTI1MWIzZmYzNmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.Jl72TahcRTDNiDc8nrKjcvBXkxIHbGKqvL-xyqIBpTs)

`cf-cache-status` can be `HIT`/`MISS` and `cf-ray` includes the airport code for the closest airport to the datacenter that handles the request (in my case, IAD).

If we can get a user's device to load a resource on a Cloudflare-backed site, causing it to be cached in their local datacenter, we can then enumerate all Cloudflare datacenters to identify which one cached the resource. This would provide an incredibly precise estimate of the user's location.

# Cloudflare Teleport

There was a one major hurdle I had to get through before I tested this theory.

You can't simply send HTTP requests to individual Cloudflare datacenters. For "security purposes" (presumably DDoS protection), all Cloudflare IP ranges are strictly anycast. All TCP connecti...