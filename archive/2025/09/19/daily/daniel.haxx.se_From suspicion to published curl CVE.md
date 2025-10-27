---
title: From suspicion to published curl CVE
url: https://daniel.haxx.se/blog/2025/09/18/from-suspicion-to-published-curl-cve/
source: daniel.haxx.se
date: 2025-09-19
fetch_date: 2025-10-02T20:22:09.015393
---

# From suspicion to published curl CVE

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/09/CVE.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# From suspicion to published curl CVE

[September 18, 2025](https://daniel.haxx.se/blog/2025/09/18/from-suspicion-to-published-curl-cve/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2025/09/18/from-suspicion-to-published-curl-cve/#respond)

![](https://daniel.haxx.se/blog/wp-content/uploads/2016/04/good_curl_logo-1200x459.png)

Every curl security report starts out with someone submitting an issue to us on <https://hackerone.com/curl>. The reporter tells us what they suspect and what they think the problem is. This report is kept private, visible only to the curl security team and the reporter while we work on it.

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/01/hackerone_logo_gray-1200x271.png)

In recent months we have gotten 3-4 security reports per week. The program has run for over six years now, with almost 600 reports accumulated.

On average, someone in the team makes a first response to that report already within the first hour.

## Assess

The curl security team right now consists of seven long time and experienced curl maintainers. We immediately start to analyze and assess the received issue and its claims. Most reports are not identifying actual security problems and are instead quickly dismissed and closed. Some of them identify plain bugs that are not security issues and then we move the discussion over to the public bug tracker instead.

This part can take anything from hours up to multiple days and usually involves several curl security team members.

If we think the issue might have merit, we ask follow-up questions, test reproducible code and discuss with the reporter.

## Valid

A small fraction of the incoming reports is actually considered valid security vulnerabilities. We work together with the reporter to reach a good understanding of what exactly is required for the bug to trigger and what the flaw can lead to. Together we set a *severity* for the problem (low, medium, high, critical) and we work out a first patch – which also helps to make sure we understand the issue. Unless the problem is deemed serious we tend to sync the publication of the new vulnerability with the pending next release. Our normal release cycle is eight weeks so we are never farther than 56 days away from the next release.

## Fix

For security issues we deem to be severity low or medium we create a pull request for the problem in the public repository – but we don’t mention the security angle of the problem in the public communication of it. This way, we also make sure that the fix gets added test exposure and time to get polished before the pending next release. Over the last five or so years, only two in about eighty confirmed security vulnerabilities have been rated a higher severity than medium. Fixes for vulnerabilities we consider to be severity high or critical are instead merged into the git repository when there is approximately 48 hours left to the pending release – to limit the exposure time before it is announced properly. We need to merge it into the public before the release because our entire test infrastructure and verification system is based on public source code.

## Advisory

Next, we write up a detailed security advisory that explains the problem and exactly what the mistake is and how it can lead to something bad – including all the relevant details we can think of. This includes version ranges for affected curl versions and the exact git commits that introduced the problem as well as which commit that fixed the issue – plus credits to the reporter and to the patch author etc. We have the ambition to provide the best security advisories you can find in the industry. (We also provide them in JSON format etc on the site for the rare few users who care about that.) We of course want the original reporter involved as well so that we make sure that we get all the angles of the problem covered accurately.

## CVE

As we are a CNA (CVE Numbering Authority), we reserve and manage CVE Ids for our own issues ourselves.

## Pre-notify

About a week before the pending release when we also will publish the CVE, we inform the [distros@openwall mailing list](https://oss-security.openwall.org/wiki/mailing-lists/distros) about the issue, including the fix, and when it is going to be released. It gives Open Source operating systems a little time to prepare their releases and adjust for the CVE we will publish.

## Publish

On the release day we publish the CVE details and we ship the release. We then also close the HackerOne report and disclose it to the world. We disclose all HackerOne reports once closed for maximum transparency and openness. We also inform all the [curl mailing lists](https://curl.se/mail/) and the [oss-security mailing list](https://www.openwall.com/lists/oss-security/) about the new CVE. Sometimes we of course publish more than one CVE for the same release.

## Bounty

Once the HackerOne report is closed and disclosed to the world, the vulnerability reporter can claim a bug bounty from [the Internet Bug Bounty](https://www.hackerone.com/company/internet-bug-bounty) which pays the researcher a certain amount of money based on the severity level of the curl vulnerability.

(The original text I used for this blog post was previously provided to the [interview I made for Help Net Security](https://www.helpnetsecurity.com/2025/09/18/daniel-stenberg-running-curl-project/). Tweaked and slightly extended here.)

## The team

The heroes in the curl security team who usually work on all this in silence and without much ado, are currently (in no particular order):

* Max Dymond
* Dan Fandrich
* Daniel Gustafsson
* James Fuller
* Viktor Szakats
* Stefan Eissing
* Daniel Stenberg

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous PostDeveloper of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/)[Next PostBye bye Kerberos FTP](https://daniel.haxx.se/blog/2025/09/19/bye-bye-kerberos-ftp/)

### Leave a Reply [Cancel reply](/blog/2025/09/18/from-suspicion-to-published-curl-cve/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
sixfivefourfourone

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

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
* Fredrik on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1...