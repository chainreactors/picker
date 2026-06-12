---
title: Hacking a Fortune 500 Finance Company via Envoy Proxy Misconfiguration
url: https://infosecwriteups.com/part-1-of-abusing-envoy-kubernetes-staging-servers-verb-tampering-to-achieve-xss-idors-and-8f4620c035b2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-11
fetch_date: 2026-06-12T06:26:10.959750
---

# Hacking a Fortune 500 Finance Company via Envoy Proxy Misconfiguration

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpart-1-of-abusing-envoy-kubernetes-staging-servers-verb-tampering-to-achieve-xss-idors-and-8f4620c035b2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpart-1-of-abusing-envoy-kubernetes-staging-servers-verb-tampering-to-achieve-xss-idors-and-8f4620c035b2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8f4620c035b2---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8f4620c035b2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Hacking a Fortune 500 Finance Company via Envoy Proxy Misconfiguration

[![Alimuhammadsecured](https://miro.medium.com/v2/resize:fill:64:64/1*_yamfbX8YVQ6LTBbBQSl3A.png)](https://medium.com/%40alimuhammadsecured?source=post_page---byline--8f4620c035b2---------------------------------------)

[Alimuhammadsecured](https://medium.com/%40alimuhammadsecured?source=post_page---byline--8f4620c035b2---------------------------------------)

8 min read

·

Oct 26, 2025

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D8f4620c035b2&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpart-1-of-abusing-envoy-kubernetes-staging-servers-verb-tampering-to-achieve-xss-idors-and-8f4620c035b2&source=---header_actions--8f4620c035b2---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

Compromised Account Details

When hunting on a site I tend to just poke around, gauge the functionality and see logically what can be broken before I fuzz.

The target (`www.REDACTED.com`) was a large finance holding company. Almost all their domains were heavily locked down and required employee SSO credentials to use.

However, one of their sister websites I discovered by Google Dorking allowed verified authors worldwide publish articles on how to use the company’s financial software sold. However, publishing an article required strict manual approval by the site admins.

> This is a common step missed by bug bounty hunters, make sure to read the scope and see if they allow third party websites to be tested. I typically refer to these as “sister sites”, after finding this domain I shifted my focus on attacking this third party as it was in scope and no longer the main domain.

I couldn’t find any vulnerabilities on the third party’s main website (`www.Sister-REDACTED.com`)

### Recon

If you don’t have a recon methodology it may benefit you to read some bug bounty articles on Medium more frequently. What helped me was following users who wrote unique or practical blogs that weren’t generic or similar to ones I’d seen many times.

> Critical Side Note in automated Fuzzing:
>
> Always include a `User-Agent` header when fuzzing at the very least. I nearly missed a `P1` vulnerability in another target by not doing this.
>
> While using HTTPX to verify which subdomains were live, a few subdomains consistently returned as being unreachable. However, when I stumbled upon one of the supposedly unreachable subdomains when google dorking they were reachable, I almost missed a whole subdomain.
>
> Turns out there was a reverse proxy in front of the domain silently dropping any request packets without a proper User-Agent header. Furthermore, the Windows server behind the proxy had ICMP replies disabled making it truly appear as an unreachable domain.
>
> Even after adding proper headers, I still got inconsistent results with HTTPX. To this day, I haven’t found a reliable solution. Rate limiting was not the issue either, it loaded fine in the browser (even after 1000+ refreshes), but for some reason would fail in HTTPX.

1. Fuzz subdomain VHOSTS via`FFUF`
2. `PureDNS` for direct DNS enumeration.
3. I also went through passive collection of subdomains by using tools such as `subfinder` and google dorking (`site:Sister-REDACTED.com` ).
4. Looked for related sister sites via:

* `FOFA`
* `SHODAN` (Via Favicon hash search)
* Fuzzing `TLD` via PureDNS (ex: REDACTED`.FUZZ` )

5. Scanning ports via `Masscan` & `RustScan`

* I stopped over-relying on one tool and lowered the maximum packet rate as it typically leads to inconsistent results.

6. Scrape endpoints from `GAU` , `WayBackURLS` , `Dorking`

* When dorking I use the [URL Extractor](https://chromewebstore.google.com/detail/ggiihlkbikggfknjgbocmogobagckdpc?utm_source=item-share-cb) extension to parse all the URLs from google searches as I dork.

7. Exposed secrets by searching target-specific keywords on `Github` , `PostMan` , etc.

### Subdomain Analysis

After cleaning up and collecting the list I realized there weren’t many subdomains this company offered. However there were two that stuck out to me the most:

* `staging.Sister-REDACTED.com`
* `testing-ignore.Sister-REDACTED.com`

The `testing-ignore` subdomain was inaccessible and had no digital footprint as to what its purpose was or how the website looked (was not archived in the Wayback Machine).

I shifted my focus to the staging server, I realized account takeover (ATO) may be possible if I registered an account using an email address that existed in production but not in staging. This would only work if both servers were using the same JWT signing keys. This is a common technique explained more in-depth here: <https://sandh0t.medium.com/the-bad-twin-a-peculiar-case-of-jwt-exploitation-scenario-1efa03e891c0>.

### Black Box Reverse Engineering

Unfortunately, when registering a new account there’s an email verification sent-I could not bypass this. But then I caught myself falling into autopilot. I was just following the same checklist everyone runs through.

Why was I even trying to register with someone else’s email on staging in the first place?

Well, I told myself my goal was to obtain a JWT from staging and replay it against production. But I was getting ahead of myself, I didn’t even examine the decoded JWT, what if there wasn’t even an email field at all?

## Get Alimuhammadsecured’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

I decoded a JWT from an authenticated login on staging and it looked like this:

Press enter or click to view image in full size

![]()

I used the token.dev website when decoding the JWT

> Side Note: If you’re a penetration tester make sure to NEVER put a JWT into a public website, regardless of what their claims are.
>
> ...