---
title: Supported curl versions and end of life
url: https://daniel.haxx.se/blog/2025/05/14/supported-curl-versions-and-end-of-life/
source: daniel.haxx.se
date: 2025-05-15
fetch_date: 2025-10-06T22:26:53.904011
---

# Supported curl versions and end of life

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/02/many-tickers.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Supported curl versions and end of life

[May 14, 2025](https://daniel.haxx.se/blog/2025/05/14/supported-curl-versions-and-end-of-life/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

The other week we shipped the 266th curl release. This counter is perhaps a little inflated since it also includes the versions we did before we renamed it to curl, but still, there are *hundreds* of them. We keep cranking them out at least once every eight weeks; more often than so when we need to do patch releases. There is no planned end or expected change to this system for the foreseeable future. We can assume around ten new curl releases per year for a long time to come.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/05/Screenshot-2025-05-14-at-08-55-08-curl-Project-status-dashboard.png)

curl releases over time since late 1996 to April 2025

## Release versions

We have the simplest possible release branching model: there is only one long term development branch. We create releases from *master* when the time comes. This means that we only have one version that is the latest and that *we never fix or patch old releases*. No other long-living release branches.

You can still find older curl versions in the wild getting patched, but those are not done by the curl project. Just about every Linux distribution, for example, maintains several old curl versions to which they back-port security fixes etc.

As we work crazy hard at not breaking users and to maintain behaviors, users *should* always be able to upgrade to the latest version without risking to break their use cases. Even when that upgrade jump is enormous. (We offer [commercial alternatives](https://daniel.haxx.se/blog/2024/11/07/rock-solid-curl/) for those who want even stronger guarantees, but they are provided slightly separate from the Open Source project.)

## Supported versions

The curl support we provide for no money in the Open Source curl project is of course always a best-effort with no promises. We offer [paid support](https://curl.se/support.html) for those that need promises, guaranteed response times or just want more and dedicated attention.

We support users with their curl issues, independent of their version – if we can. It is however likely that we ask the reporters using old versions to first try their cases using a modern curl version to see if the problem is not already fixed, so that we do not have to waste time researching something that might not need any work.

If the user’s reported problem cannot be reproduced with the latest curl version, then we are done. Otherwise, again, the paid support option exists.

So, while this is not quite a *supported versions* concept, we focus our free-support efforts on recent releases – bugs that are reported on old versions that cannot be reproduced with a modern version are considered outdated.

## Not really End of life

Because of this concept, we don’t really have *end of life* dates for our products. They are all just in varying degrees of aging. We still happily answer questions about versions shipped twenty years ago if we can, but we do not particularly care about bugs in them if they don’t seem to exist anymore.

We urge and push users into using the most recent curl versions at any time so that they get the best features, the most solid functionality and the least amount of security problems.

Or that they pay for support to go beyond this.

In reality, of course, users are regularly stuck with old curl versions. Often because they use an (outdated) Linux distribution which does not upgrade its curl package.

## They all “work”

We regularly have users ask questions about curl versions we shipped ten, twelve or even fifteen years ago so we know old releases are used widely. All those old versions still mostly work and as long as they do what the users want and ask curl to do, then things are fine. At least if they use versions from distributions that back-port security fixes.

In reality of course, the users who still use the most ancient curl versions also do this on abandoned or end-of-lived distros, which means that they run insecure versions of curl – and probably basically every other tool and library they use are also insecure by then. In the best of worlds the users have perfect control and awareness of those details.

## Feature window

Since we do all releases from the single master branch we have the feature window/freeze concept. We only allow merging features/changes during a few weeks in the release cycle, and all the other time we only merge bugfixes and non-feature changes. This, to make sure that the branch is as stable as possible by the time the release is to be shipped.

[bug report](https://daniel.haxx.se/blog/tag/bug-report/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[support](https://daniel.haxx.se/blog/tag/support/)

# Post navigation

[Previous Post1k-0036 means sad eyeballs on my LG](https://daniel.haxx.se/blog/2025/05/13/1k-0036-means-sad-eyeballs-on-my-lg/)[Next PostDetecting malicious Unicode](https://daniel.haxx.se/blog/2025/05/16/detecting-malicious-unicode/)

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
Keep up: [RSS-feed](...