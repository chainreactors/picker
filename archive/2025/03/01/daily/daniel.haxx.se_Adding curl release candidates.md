---
title: Adding curl release candidates
url: https://daniel.haxx.se/blog/2025/02/28/adding-curl-release-candidates/
source: daniel.haxx.se
date: 2025-03-01
fetch_date: 2025-10-06T21:58:20.830204
---

# Adding curl release candidates

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2018/06/we-need-more-curl-releases-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Development](https://daniel.haxx.se/blog/category/development/)

# Adding curl release candidates

[February 28, 2025](https://daniel.haxx.se/blog/2025/02/28/adding-curl-release-candidates/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

Heading towards [curl](https://curl.se/) release number 266 we have decided to spice up our *release cycle* with *release candidates* in an attempt to help us catch regressions better earlier.

It has become painfully obvious to us in the curl development team that over the past few years we have done several dot-zero releases in which we shipped quite terrible regressions. Several times those regressions have been so bad or annoying that we felt obligated to do quick follow-up releases a week later to reduce friction and pain among users.

Every such patch release have caused pain in our souls and have worked as proof that we to some degree failed in our mission.

We have thousands of tests. We run several hundred CI jobs for every change that verify them. We simply have too many knobs, features, build configs, users and combinations of them all to be able to catch all possible mistakes ourselves.

## Release candidates

Decades ago we sometimes did release candidates, but we stopped. We have instead shipped *[daily snapshots](https://curl.se/snapshots/)*, which is basically what a release would look like, packaged every day and made available. In theory this should remove the need and use of release candidates as people can always just get the latest snapshots, try those out and report problems back to us.

We are also acutely aware of the fact that [only releases get tested](https://un.curl.dev/code/releases.html) properly.

Are release candidates really going to make a difference? I don’t know. I figure it is worth a shot. Maybe it is a matter of messaging and gathering the troops around these specific snapshots and by calling out the need for the testing to get done, maybe it will happen at least to some extent?

Let’s attempt this for a while and then come back in a few years and evaluate if it has seemed to help or otherwise improve the regression rate or not.

## Release cycle

We have a standard release cycle in the curl project that is exactly eight weeks. When things run smoothly, we ship a new release on a Wednesday every 56 days.

The release cycle is divided into three periods, or phases, that control what kind of commits us maintainers are permitted to merge. Rules to help us ship solid software.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/02/rc.jpg)

The curl release cycle, illustrated

Immediately after a release, we have a ten day *cool down* period during which we absorb reactions and reports from the release. We only merge bugfixes and we are prepared to do a patch release if we need to.

Ten days after the release, we open the *feature window* in which we allow new features and *changes* to the project. The larger things. Innovations, features etc. Typically these are the most risky things that may cause regressions. This is a three-week period and those changes that do not get merged within this window get another chance again next cycle.

The longest phase is the *feature freeze* that kicks in twenty-five days before the pending release. During this period we only merge bugfixes and is intended to calm things down again, smooth all the frictions and rough corners we can find to make the pending release as good as possible.

## Adding three release candidates

The first release candidate (rc1) is planned to ship on the same day we enter *feature freeze*. From that day on, there will be no more new features before the release so all the new stuff can be checked out and tested. It does not really make any sense to do a release candidate before that date.

We will highlight this release candidate and ask that everyone who can (and want) tests this one out and report every possible issue they find with it. This should be the first good opportunity to catch any possible regressions caused by the new features.

Nine days later we ship rc2. This will be done no matter what bugreports we had on rc1 or what possible bugs are still pending etc. This candidate will have additional bugfixes merged.

The final and third release candidate (rc3) is then released exactly one week before the pending release. A final chance to find nits and perfect the pending release.

I hope I don’t have to say this, but **you should not use the release candidates in production**, and they may contain more bugs than what a regular curl release normally does.

## Technically

The release candidates will be created exactly like a real release, except that there will not be any tags set in the git repository and they will not be archived. The release candidates are automatically removed after a few weeks.

They will be named **`curl-X.Y.Z-rcN`**, where x.y.z is the version of the pending release and N is the release candidate number. Running “curl -V” on this build will show “x.y.x-rcN” as the version. The libcurl includes will say it is version x.y.z, so that applications can test out preprocessor conditionals etc exactly as they will work in the *real* x.y.z release.

## You can help!

You can most certainly help us here by getting one of the release candidates when they ship and try it out in your use cases, your applications, your pipelines or whatever. And let us know how it runs.

I will do something on the website to help highlight the release candidates once there is one to show, to help willing contributors find them.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Development](https://daniel.haxx.se/blog/tag/development/)

# Post navigation

[Previous PostThe curl roadmap webinar 2025](https://daniel.haxx.se/blog/2025/02/25/the-curl-roadmap-webinar-2025/)[Next PostMy cookie spec problem](https://daniel.haxx.se/blog/2025/03/01/my-cookie-spec-problem/)

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
* [Daniel Stenberg](https://daniel.haxx.se/) on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/co...