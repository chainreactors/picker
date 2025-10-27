---
title: The 2022 curl security audit
url: https://daniel.haxx.se/blog/2022/12/21/the-2022-curl-security-audit/
source: daniel.haxx.se
date: 2022-12-22
fetch_date: 2025-10-04T02:13:37.635639
---

# The 2022 curl security audit

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/03/binoculars-1209011_1280-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Security](https://daniel.haxx.se/blog/category/tech/security/)

# The 2022 curl security audit

[December 21, 2022](https://daniel.haxx.se/blog/2022/12/21/the-2022-curl-security-audit/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

*tldr: several hundred hours of dedicated scrutinizing of curl by a team of security experts resulted in two CVEs and a set of less serious remarks.* The link to the reports is at the bottom of this article.

Thanks to an [OpenSSF](https://openssf.org/) grant, [OSTIF](https://ostif.org/) helped us set up a curl security audit, which the excellent [Trail of Bits](https://www.trailofbits.com/) was selected to perform in September 2022. We are most grateful to OpenSSF for doing this for us, and I hope all users who use and rely on curl recognize this extraordinary gift. [OSTIF](https://ostif.org/the-ostif-audit-of-curl-with-trail-of-bits-is-complete/) and [Trail of Bits](https://blog.trailofbits.com/2022/12/22/curl-security-audit-threat-model/) both posted articles about this audit separately.

We previously had an [audit performed on curl back in 2016](https://daniel.haxx.se/blog/2016/11/23/curl-security-audit/) by [Cure53](https://cure53.de/) (sponsored by Mozilla) but I like to think that we (curl) have traveled quite far and matured a lot since those days. The fixes from the discoveries reported in that old previous audit were all merged and shipped in the 7.51.0 release, in November 2016. Now over six years ago.

## Changes since previous audit

We have done a lot in the project that have improved our general security situation over the last six years. I believe we are in a *much* better place than the last time around. But we have also grown and developed a lot more features since then.

curl is now at**150,000** lines of C code. This count is for “product code” only and excludes blank lines but includes **19%** comments.

**71** additional vulnerabilities have been reported and fixed since then. (**42** of those even existed in the version that was audited in 2016 but were obviously not detected)

We have **30,000** additional lines of code today (+27%), and we have done over **8,000** commits since.

We have **50%** more test cases (now 1550).

We have done **47** releases featuring more than **4,200** documented bugfixes and 150 changes/new features.

We have **25** times the number of CI jobs: up from 5 in 2016 to **127** today.

The OSS-Fuzz project started fuzzing curl in 2017, and it has been fuzzing curl non-stop since.

We [introduced our “dynbuf” system](https://daniel.haxx.se/blog/2020/09/23/a-google-grant-for-libcurl-work/) internally in 2020 for managing growing buffers to maybe avoid common C mistakes around those.

## Audit

The Trail of Bits team was assigned this as a three-part project:

1. Create a Threat Model document
2. Testing Analysis and Improvements
3. Secure code Review

The project was setup to use a total of 380 man hours and most of the time two Trail of Bits engineers worked in parallel on the different tasks. The Trail of Bits team themselves eventually also voluntarily extended the program with about a week. They had no problems finding people who wanted to join in and look into curl. We can safely say that they spent a significant amount of time and effort scrutinizing curl.

The curl security team members had frequent status meetings and assisted with details and could help answer questions. We would also get updates and reports on how they progressed.

## Two security vulnerabilities were confirmed

The first vulnerability they found ended up known as the [CVE-2022-42915: HTTP proxy double-free](https://curl.se/docs/CVE-2022-42915.html) issue.

The second vulnerability was found after Trail of Bits had actually ended their work and their report, while they were still running a fuzzer that triggered a separate flaw. This second vulnerability is not covered in the report but was disclosed earlier today in sync with the curl 7.87.0 release announcement: [CVE-2022-43552: HTTP Proxy deny use-after-free](https://curl.se/docs/CVE-2022-43552.html).

## Minor frictions detected

Discoveries and remarks highlighted through their work that were not consider security sensitive we could handle on the fly. Some examples include:

* Using `--ssl` now outputs a warning saying it is unsafe and instead recommending `--ssl-reqd` to be used.
* The `Alt-svc:` header parser did not deal with illegal port numbers correctly
* The URL parser accepted “illegal” characters in the host name part.
* Harmless memory leaks

You should of course read the full reports to learn about all the twenty something issues with all details, including feedback from the curl security team.

## Actions

The curl team acted on all reported issues that we think we could act on. We disagree with the Trail of Bits team on a few issues and there are some that are “good ideas” that we should probably work on getting addressed going forward but that can’t be fixed immediately – but also don’t leave any immediate problem or danger in the code.

## Conclusions

Security is not something that can be checked off as *done* once and for all nor can it ever be considered *complete*. It is a process that needs to blend in and affect everything we do when we develop software. Now and forever going forward.

This team of security professionals spent more time and effort in this security auditing and poking on curl with fuzzers than probably anyone else has ever done before. Personally, I am thrilled that they only managed to uncovered two actual security problems. I think this shows that a lot of curl code has been written the right way. The CVEs they found were not even that terrible.

## Lessons

Twenty something issues were detected, and while the report includes advice from the auditors on how we should improve things going forward, they are of the kind we all already know we should do and paths we should follow. I could not really find any real lessons as in obvious things or patterns we should stop or new paradigms och styles to adapt.

I think we learned or more correctly we got these things reconfirmed:

* we seem to be doing things mostly correct
* we can and should do more and better fuzzing
* adding more tests to increase coverage is good

## Security is hard

To show how hard security can be, we received no less than *three* additional security reports to the project during the actual life-time when this audit was being done. Those additional security reports of course came from other people and identified security problems this team of experts did not find.

## My comments on the reports

The term *Unresolved* is used for a few issues in the report and I have a minor qualm with the use of that particular word in this context for all cases. While it is correct that we in several cases did not act on the advice in the report, we saw some cases where we distinctly disagree with the recommendations and some issues that mentioned things we might work on and address in the future. They are all just marked as *unresolved* in the reports, but they are not all unresolved to us in the curl project.

In particular I am not overly pleased with how the issue called TOB-CURLTM-6 is labeled *severity high* and *status unresolved* as I believe this wrongly gives the impression that curl has issues with high severity left unresolved in the code.

If you want to read the specific responses...