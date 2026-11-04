---
title: Scrutinize our assessments
url: https://daniel.haxx.se/blog/2026/11/03/scrutinize-our-assessments/
source: daniel.haxx.se
date: 2026-11-03
fetch_date: 2026-11-04T08:17:44.818984
---

# Scrutinize our assessments

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/03/curl-runs-in-these-things.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Security](https://daniel.haxx.se/blog/category/tech/security/)

# Scrutinize our assessments

[November 3, 2026](https://daniel.haxx.se/blog/2026/11/03/scrutinize-our-assessments/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/11/03/scrutinize-our-assessments/#respond)

I recently blogged about how the curl project switched to [doing all handling of vulnerabilities at severity LOW and MEDIUM in the public](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/).

Let me now describe how you can follow along this process and help out. Add your opinions, comments and assessments to help the curl project stay honest, do even better and manage the load.

## Issues

Vulnerability reports are now submitted directly in [curl’s issue tracker on GitHub](https://github.com/curl/curl/issues). Judging by the initial set received, the persons submitting them do not particularly highlight the security angle in the title but it is instead implied or specified in the issue description. I hope people react if we somehow miss it.

## Tags

We use a set of tags to manage vulnerability reports on GitHub. They are all prefixed by *vuln:*.

## vuln:ASSESS

Every submitted issue that has a claimed or suspected security angle – a possible vulnerability – first gets the `vuln:ASSESS` tag set (by one of the curl maintainers). This tag marks the issue as one that we should evaluate, assess and determine first if it is a vulnerability, and if it is, what severity.

Anyone is free to leave their comment and thinking to help us come to a conclusion.

This tag is removed again when an assessment has been done.

## vuln:NONE

This issue was assessed in regards to its vulnerability risk and we deem that it has none; or it is so low that it is considered to be less than severity LOW. This issue is treated as *just a bug*.

If someone objects provides a reasonable and convincing argument, we can reassess.

## vuln:LOW

This issue is a confirmed vulnerability at severity LOW. We work on a fix for this that we merge as soon as it works and then we close this issue.

If someone objects to the severity and provides a reasonable and convincing argument, we can reassess.

## vuln:MEDIUM

This issue is a confirmed vulnerability at severity MEDIUM. We work on a fix for this that we merge as soon as it works and then we close this issue.

If someone objects to the severity and provides a reasonable and convincing argument, we can reassess.

## Advisories

Confirmed vulnerabilities get a CVE and a dedicated security advisory that we work on separately from the issue and its fix [in the curl-www repository](https://github.com/curl/curl-www/pulls). The CVE and its advisory get published in sync with the pending curl release. They are left as open in-progress pull-requests until then, using [vuln:LOW](https://github.com/curl/curl-www/pulls?q=is%3Apr+state%3Aopen+label%3Avuln%3ALOW) or [vuln:MEDIUM](https://github.com/curl/curl-www/pulls?q=is%3Apr+state%3Aopen+label%3Avuln%3AMEDIUM) tags.

Each advisory has all the information about a single curl vulnerability. A detailed description, all the info, CWE, CVE, affected version ranges, if it is a C mistake, in which curl “area” it happens, a link to the original report, etc. The idea being that this single markdown file has all necessary information anyone might want and need about this specific vulnerability.

## Public vs published

The work on these vulnerabilities is immediately public and the second we register and assign a CVE Id (the actual numerical identifier) to a problem, you can learn about its existence.

We do however not *publish* the issue and all relevant metadata to the CVE database until the publication date, which is the same date as the curl release date when we ship the first release that contains the fix for the vulnerability.

So information is *public* in the curl repositories early on, but it is not *published* until perhaps several weeks later, and it is at that later moment that it gets picked up by other tools and ecosystems and then gets widely known.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[CVE](https://daniel.haxx.se/blog/tag/cve/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous Post“ignore the slop”](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/)

### Leave a Reply [Cancel reply](/blog/2026/11/03/scrutinize-our-assessments/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
seven6oneeight7

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [Scrutinize our assessments](https://daniel.haxx.se/blog/2026/11/03/scrutinize-our-assessments/)
  November 3, 2026
* [“ignore the slop”](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/)
  October 22, 2026
* [Do minor curl vulnerabilities in the open](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/)
  October 20, 2026
* [OSI approved the curl license](https://daniel.haxx.se/blog/2026/10/15/osi-approved-the-curl-license/)
  October 15, 2026
* [A curl audit by Aisle](https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/)
  October 14, 2026
* [A UAF turned RCE](https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/)
  October 14, 2026

# Recent Comments

* [Daniel Stenberg](https://daniel.haxx.se/) on [“ignore the slop”](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/comment-page-1/#comment-27572)
* [Marya](https://kinomig.tv/) on [“ignore the slop”](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/comment-page-1/#comment-27571)
* [Christian Buhtz](https://buhtz.codeberg.page/) on [“ignore the slop”](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/comment-page-1/#comment-27569)
* Adrian Johnston on [“ignore the slop”](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/comment-page-1/#comment-27568)
* Imran Chaudhry on [Do minor curl vulnerabilities in the open](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/comment-page-1/#comment-27567)
* Matthias Hörmann on [“ignore the slop”](https://daniel.haxx.se/blog/2026/10/22/ignore-the-slop/comment-page-1/#comment-27566)
* Patrick T on [Do minor curl vulnerabilities in the open](https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/comment-page-1/#comment-27565)
* [Soufiane](https://www.easytutoriel.com) on [OSI approved the curl license](https://daniel.haxx.se/blog/2026/10/15/osi-approved-the-curl-license/comment-page-1/#comment-27564)
* [Arthur Sathish](https://peeklaunch.com) on [A curl audit by Aisle](https://daniel.haxx.se/blog/2026/10/14/a-curl-audit-by-aisle/comment-page-1/#comment-27563)
* [Daniel Stenberg](https://daniel.haxx.se/) on [A slightly faster slimmer curl](https://daniel.haxx.se/blog/2026/10/13/a-slightly-faster-slimmer-curl/comment-page-1/#comment-27559)

## curl, open source and networking

##

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/03/final-12-1000x1000-1.jpg)

Sponsor me: [on GitHub](https://github.com/users/bagder/sponsorship)
Follow me: [@bagder](https://mastodon.social/%40bagder)
Keep up: [RSS-feed](https://daniel.haxx.se/blog/feed/)
Email: [weekly reports](http...