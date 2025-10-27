---
title: Rock-solid curl
url: https://daniel.haxx.se/blog/2024/11/07/rock-solid-curl/
source: daniel.haxx.se
date: 2024-11-08
fetch_date: 2025-10-06T19:19:30.507170
---

# Rock-solid curl

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/curl-on-rock.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [wolfSSL](https://daniel.haxx.se/blog/category/work/wolfssl/)

# Rock-solid curl

[November 7, 2024](https://daniel.haxx.se/blog/2024/11/07/rock-solid-curl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [2 Comments](https://daniel.haxx.se/blog/2024/11/07/rock-solid-curl/#comments)

I am thrilled to announce:

**[Rock-Solid curl](https://rock-solid.curl.dev/): long term supported curl releases**

## Basics

We make long term support releases of curl that we call **Rock-solid curl**.

We support each release branch for *at least* five years.

We only merge security fixes and important stability bugfixes into these branches for updates. No new features. No surprises.

We offer **Rock-solid curl** downloads to existing support customers. It means that there is no free and open access to these releases. To get access, become a customer!

**Rock-solid curl** is released under [the same license as normal curl](https://curl.se/docs/copyright.html) (or optionally a commercial license). No funny business.

**Rock-solid curl** is meant to greatly reduce the risk of regressions and yet be a safe and secure solution with full support. For the companies who want this extra level of attention. An even smoother ride.

We plan to make new **Rock-solid curl** release branches roughly every 18-24 months.

## The first Rock-solid curl release

**Rock-solid curl** 8.9.2 is the first long-term support curl version. As the version number implies, it is based on the curl 8.9.1 release that we shipped back in July, with two security fixes and a small number of stability patches applied.

Once you have a contract with us, you can get it.

## Who is doing this?

I, Daniel Stenberg, will be the primary support person for Rock-solid curl and I will do the releases, and most of the patching and the back-porting of what is deemed necessary.

Customers sign contracts with [wolfSSL](https://wolfssl.com/) for this. wolfSSL pays my salary. I have worked for and with wolfSSL with this business setup since 2019.

## What about “the normal” curl?

Nothing changes with or happens to the curl project and the regular curl releases because of this. No one is going anywhere. The curl license remains the same. The curl releases and the release cadence remain intact.

Support customers help fund the project by allowing us to pay developers.

## How do I become a customer?

Head over to [rock-solid.curl.dev](https://rock-solid.curl.dev/) and contact us via the provided links.

Downloads and all **Rock-solid curl** information is hosted on the dedicated [rock-solid.curl.dev](https://rock-solid.curl.dev/) site, separate from the open source project on [curl.se](https://curl.se/).

## On curl

Born in the late 1990s, curl is a *client-side Internet transfer engine*. Installed in over twenty billion instances it serves virtually everything that is internet connected: phones, tablets, cars, television sets, printers, medical devices, game consoles, helicopters on other planets, etc and it is an embedded component in a significant share of our most used and beloved apps, tools, games and services.

curl is the fruit and outcome from hard work by thousands of volunteers and is completely free and Open Source. The curl project is independent. It is not part of any umbrella organization or foundation and it is not owned nor controlled by any company.

curl is secure, fast and feature-rich. It is a defacto standard and key infrastructure.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Rock-solid](https://daniel.haxx.se/blog/tag/rock-solid/)[support](https://daniel.haxx.se/blog/tag/support/)[WolfSSL](https://daniel.haxx.se/blog/tag/wolfssl/)

# Post navigation

[Previous Postcurl 8.11.0](https://daniel.haxx.se/blog/2024/11/06/curl-8-11-0/)[Next PostThe 2024 HTTP Workshop](https://daniel.haxx.se/blog/2024/11/13/the-2024-http-workshop/)

## 2 thoughts on “Rock-solid curl”

1. ![](https://secure.gravatar.com/avatar/6d446c3138833e2143a1e5bf2f8ccdc7e13c82b4b71af2f8ad7b4e43ddc650af?s=34&d=monsterid&r=g) **Matthias Hörmann** says:

   [November 8, 2024 at 09:37](https://daniel.haxx.se/blog/2024/11/07/rock-solid-curl/#comment-27078)

   What will be the version policy on that LTS branch for future versions? Will they be labelled 8.9.3, 8.9.4,… or something like 8.9.2.1, 8.9.2.2,…?

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [November 8, 2024 at 10:27](https://daniel.haxx.se/blog/2024/11/07/rock-solid-curl/#comment-27079)

      @Matthias: I want to keep it simple and easy to understand. The Rock-solid curl branches will always be done on branches the upstream curl master has already left, so 8.9.2 has the same features 8.9.1 had, just more patches. Then we can continue to release versions in the 8.9.x series with an increasing value for X. As they are then just extending the 8.9.x branch with more releases.

Comments are closed.

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
* Tjark on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27313)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](https://lists.haxx.se/listinfo/daniel)

November...