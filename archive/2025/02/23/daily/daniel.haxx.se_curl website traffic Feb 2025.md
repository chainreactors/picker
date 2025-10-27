---
title: curl website traffic Feb 2025
url: https://daniel.haxx.se/blog/2025/02/22/curl-website-traffic-feb-2025/
source: daniel.haxx.se
date: 2025-02-23
fetch_date: 2025-10-06T20:36:56.716480
---

# curl website traffic Feb 2025

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/02/Screenshot-2025-02-22-at-23-06-27-Fastly-Observability-Fastly-Observability.png)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl website traffic Feb 2025

[February 22, 2025](https://daniel.haxx.se/blog/2025/02/22/curl-website-traffic-feb-2025/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

Data without logs sure leaves us open for speculations.

I took a quick look at what the [curl.se](https://curl.se/) website traffic situation looks like right now. Just as a curiosity.

Disclaimer: *we don’t log website visitors at all*, we don’t run any web analytics on the site so we basically don’t know a lot of who does what on the site. This is done both for privacy reasons, but also for practical reasons. Managing logs for this setup is work I rather avoid to do and to pay for.

What do we have, is a website that is hosted (fronted) by Fastly on their CDN network, and as part of that setup we have an admin interface that offers accumulated traffic data. We get some numbers, but without details and specifics.

## Bandwidth

Over the last month, the site served **62.95 TB**. This makes it average over **2TB/day**. On the most active day in the period it sent away **3.41 TB**.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/02/Screenshot-2025-02-22-at-23-06-27-Fastly-Observability-Fastly-Observability.png)

This is the live bandwidth meter displayed while I was writing this blog post.

## Requests

At **12.43** billion requests, it makes an average request transfer size **5568** bytes.

## Downloads

Since we don’t have logs, we can’t count curl download perfectly. But we do have stats for request frequency for objects of different sizes from the site, and in the category 1MB-10MB we basically only have curl tarballs.

**1.12** million such objects were downloaded over the last month. **37,000** downloads per day, or about one curl tarball downloaded every other second around the clock.

Of course most curl users never download it from curl.se. The source archives are also offered from github.com and users typically download curl from their distro or get it installed with their operating system etc.

## But…?

The average curl tarball size from the last 22 releases is **4,182,317** bytes. 3.99 MB.

1.12 million x 3.99 MB is *only* **4,362 gigabytes**. Not even ten percent of the total traffic.

Even if we count the average size of only the zip archives from recent releases, **6,603,978** bytes, it only makes **6,888** gigabytes in total. Far away from the almost 63 terabytes total amount.

This, combined with low average transfer size per request, seems to indicate that other things are transferred off the site at fairly extreme volumes.

## Origin offload

**99.77%** of all requests were served by the CDN without reaching the origin site. I suppose this is one of the benefits of us having mostly a static site without cookies and dynamic choices. It allows us to get a really high degree of cache hits and content served directly from the CDN servers, leaving our origin server only a light load.

## Regions

Fastly is a CDN with access points distributed over the globe, and the curl website is anycasted, so the theory is that users access servers near them. In the same region. If we assume this works, we can see from where most traffic to the curl website comes from.

The top-3:

1. North America – 48% of the bandwidth
2. Europe – 24%
3. Asia – 22%

## TLS

Now I’m not the expert on how exactly the TLS protocol negotiation works with Fastly, so I’m guessing a little here.

It is striking that **99%** of the traffic uses TLS 1.2. It seems to imply that a vast amount of it is not browser-based, as all popular browsers these days mostly negotiate TLS 1.3.

## HTTP

Seemingly agreeing with my TLS analysis, the HTTP version distribution also seem to point to a vast amount of traffic not being humans in front of browsers. They prefer HTTP/3 these days, and if that causes problems they use HTTP/2.

**98.8%** of the curl.se traffic uses HTTP/1, **1.1%** use HTTP/2 and only the remaining tiny fraction of less than **0.1%** uses HTTP/3.

## Downloads by curl?

I have no idea how large share of the downloads that are actually done using curl. A fair share is my guess. The TLS + HTTP data imply a huge amount of bot traffic, but modern curl versions would at least select HTTP/2 unless the users guiding it specifically opted not to.

## What is all the traffic then?

In the past, we have seen rather [extreme traffic volumes](https://daniel.haxx.se/blog/2020/04/09/a-qqgamehall-storm/) from China downloading the [CA cert store](https://curl.se/docs/caextract.html) we provide, but these days the traffic load seems to be fairly evenly distributed over the world. And over time.

According to the stats, objects in the 100KB-1MB range were downloaded 207.31 million times. That is bigger than our images on the site and smaller than the curl downloads. Exactly the range for the CA cert PEM. The most recent one is at 247KB. Fits the reasoning.

A 247 KB file downloaded 207 million times equal 46 TB. Maybe that’s the explanation?

## Sponsored

The curl website hosting is graciously sponsored by [Fastly](https:///fastly.com/).

![](https://daniel.haxx.se/blog/wp-content/uploads/2017/04/fastly-logo-1200x630.png)

# Post navigation

[Previous PostChanging every line three times](https://daniel.haxx.se/blog/2025/02/18/changing-every-line-three-times/)[Next PostA second curl distro meeting 2025](https://daniel.haxx.se/blog/2025/02/24/a-second-curl-distro-meeting-2025/)

# Recent Posts

* [How I maintain release notes for curl](https://daniel.haxx.se/blog/2025/10/01/how-i-maintain-release-notes-for-curl/)
  October 1, 2025
* [CRA compliant curl](https://daniel.haxx.se/blog/2025/09/22/cra-compliant-curl/)
  September 22, 2025
* [Bye bye Kerberos FTP](https://daniel.haxx.se/blog/2025/09/19/bye-bye-kerberos-ftp/)
  September 19, 2025
* [From suspicion to published curl CVE](https://daniel.haxx.se/blog/2025/09/18/from-suspicion-to-published-curl-cve/)
  September 18, 2025
* [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/)
  September 13, 2025
* [curl 8.16.0](https://daniel.haxx.se/blog/2025/09/10/curl-8-16-0/)
  September 10, 2025

# Recent Comments

* F.Nagy on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27323)
* Fredrik on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27322)
* [Fazal Majid](https://majid.info/) on [preparing for the worst](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/comment-page-1/#comment-27321)
* Nikhil on [About](https://daniel.haxx.se/blog/about/comment-page-1/#comment-27320)
* A. Ros on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27318)
* [Daniel Stenberg](https://daniel.haxx.se/) on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27317)
* Yoann Ricordel on [HTTP is not simple](https://daniel.haxx.se/blog/2025/08/08/http-is-not-simple/comment-page-1/#comment-27316)
* Ond?ej Surý on [Hello Sprout](https://daniel.haxx.se/blog/2025/07/28/hello-sprout/comment-page-1/#comment-27315)
* H. Stefan on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27314)
* Tjark on [car brands running curl](https://daniel.haxx....