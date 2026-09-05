---
title: From a 2008 Web Server to Every Customer Record: How One Upload Took Down an Entire Hosting…
url: https://infosecwriteups.com/from-a-2008-web-server-to-every-customer-record-how-one-upload-took-down-an-entire-hosting-454fd0571375?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-09-04
fetch_date: 2026-09-05T06:29:05.058573
---

# From a 2008 Web Server to Every Customer Record: How One Upload Took Down an Entire Hosting…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-a-2008-web-server-to-every-customer-record-how-one-upload-took-down-an-entire-hosting-454fd0571375&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-------------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav--------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-a-2008-web-server-to-every-customer-record-how-one-upload-took-down-an-entire-hosting-454fd0571375&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-454fd0571375-----------------------------------------)

·

1. [The Target](/?source=post_page-----454fd0571375-----------------------------------------#4b30 "The Target")
2. [Recon: The First Red Flag Is Free](/?source=post_page-----454fd0571375-----------------------------------------#4625 "Recon: The First Red Flag Is Free")
3. [Mapping the Attack Surface](/?source=post_page-----454fd0571375-----------------------------------------#da2a "Mapping the Attack Surface")
   1. [The Break: Trust the Client, Not the Client’s Browser](/?source=post_page-----454fd0571375-----------------------------------------#b7dd "The Break: Trust the Client, Not the Client’s Browser")
   2. [Post-Exploitation: The Inventory They Didn’t Know They Had](/?source=post_page-----454fd0571375-----------------------------------------#8190 "Post-Exploitation: The Inventory They Didn’t Know They Had")
4. [What the Client Learned](/?source=post_page-----454fd0571375-----------------------------------------#2ac4 "What the Client Learned")
5. [Timeline](/?source=post_page-----454fd0571375-----------------------------------------#470a "Timeline")
6. [Toolbox](/?source=post_page-----454fd0571375-----------------------------------------#4cf0 "Toolbox")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-454fd0571375-----------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[Hacking](https://medium.com/tag/hacking?source=post_page---header_tags--454fd0571375-----------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--454fd0571375-----------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page---header_tags--454fd0571375-----------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page---header_tags--454fd0571375-----------------------------------------)

# From a 2008 Web Server to Every Customer Record: How One Upload Took Down an Entire Hosting Business

[![CypherNova1337](https://miro.medium.com/v2/resize:fill:64:64/1*4pxtZ89bwJejdrz2UBr2Lg.jpeg)](https://cyphernova1337.medium.com/?source=post_page---byline--454fd0571375-----------------------------------------)

[CypherNova1337](https://cyphernova1337.medium.com/?source=post_page---byline--454fd0571375-----------------------------------------)

6 min read

·

Aug 16, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D454fd0571375&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-a-2008-web-server-to-every-customer-record-how-one-upload-took-down-an-entire-hosting-454fd0571375&source=---header_actions--454fd0571375---------------------post_audio_button--------------------)

Share

A walkthrough of a full-scope penetration test against a small business that thought its old but secure setup was fine. All sensitive details redacted with client permission. The engagement took under two days. The compromise took twenty minutes.

Press enter or click to view image in full size

![]()

## The Target

A small computer-repair business in Western Canada. Ten years of customer trust. One website that handles repair requests, data-recovery quotes, and job applications. A couple of other domains hosted on the same box — because why pay for separate hosting when one machine can do it all?

The client authorized full-scope testing with one caveat: *“we don’t really have anything sensitive on there.”*

Spoiler: they did.

## Recon: The First Red Flag Is Free

Every engagement starts the same way — passive enumeration. Subdomain discovery, certificate transparency logs, Wayback Machine scraping, JavaScript extraction. All standard tools: `amass`, `subfinder`, `assetfinder`, `gau`, `waybackurls`.

Nothing exotic came back. Five subdomains. Mail records. A remote-support link. A Joomla site.

Then the first request hit the server, and the response headers told a story:

```
Server: Apache/2.2.8 (Win32) DAV/2 mod_ssl/2.2.8 OpenSSL/0.9.8g mod_autoindex_color PHP/5.2.5
X-Powered-By: PHP/5.2.5
```

Press enter or click to view image in full size

![]()

First request tells the story — Apache 2.2.8 / PHP 5.2.5 (2008), TLS 1.0 only, self-signed cert

For the non-nerds: **Apache 2.2.8 was released in January 2008. PHP 5.2.5 in November 2007.** The server was a teenager. TLS 1.0 only. On Windows.

But old software alone isn’t a vulnerability — a lesson this test hammered home repeatedly. So we started testing, not assuming.

## Mapping the Attack Surface

The site ran **Joomla 1.5** — end-of-life since 2012. Two third-party components stood out in the URL corpus:

1. **ArtForms** — a form builder handling repair requests, employment applications, and data-recovery quotes
2. **com\_poll** — a poll

The Joomla 1.5 core SQL injection that mass-exploited thousands of sites in 2012? Tested it properly — boolean differentials, time-based probes with `SLEEP(5)`, sqlmap. The `id` parameter was integer-cast. Dead. A good reminder: *old version is a lead, never a finding.*

Press enter or click to view image in full size

![]()

The classic 2012-era core SQLi, tested properly — boolean probes return the same article, the id is integer-cast, SLEEP(5) never fires

We also confirmed reflected XSS in the ArtForms form fields — payloads came back raw in the HTML, and the site’s WAF blocked `<script>` but happily passed `<img onerror=...>`. Real, demonstrable, medium severity. Reported it. Kept digging.

Press enter or click to view image in full size

![]()

Then we looked at the employment form more carefully. It accepted file uploads — resumes.

### The Break: Trust the Client, Not the Client’s Browser

The upload accepted resumes, and the filter checked the **MIME type sent by the browser** — not the file extension. The browser’s word on a file’s identity. On the internet. In 2026.

One `curl` request with a PHP file dressed up as `application/pdf` later, and the file was sitting in a web-accessible directory that happily executed PHP.

Press enter or click to view image in full size

![]()

Press enter or click to view image i...