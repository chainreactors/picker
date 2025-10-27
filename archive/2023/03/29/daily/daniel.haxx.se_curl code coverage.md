---
title: curl code coverage
url: https://daniel.haxx.se/blog/2023/03/28/curl-code-coverage/
source: daniel.haxx.se
date: 2023-03-29
fetch_date: 2025-10-04T11:01:41.437996
---

# curl code coverage

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2017/10/bobby-car-crash-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl code coverage

[March 28, 2023](https://daniel.haxx.se/blog/2023/03/28/curl-code-coverage/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

Every once in a while someone brings up the topic of code coverage in relation to curl. What portion of the code is actually exercised when running the tests?

Honestly, **we don’t know**. We can’t figure it out. We are not trying to figure it out. We have to live with this.

## We used to get a number

A few years back we actually did a build and a test run in our CI setup that used one of those cloud services that would monitor the code coverage and warn if we would commit something that drastically reduced coverage.

This had significant drawbacks:

First, the service was unstable which made it occasionally sound the horns because we had gone down to 0% coverage and that is bad.

Secondly, it made parts of the audience actually believe that what was reported by that service for a single build and a single test run was the final and accurate code coverage number. It was far from it.

We ended up ditching that job as it did very little good but some amount of harm.

## Different build combinations – and platforms

Code coverage is typically the number of lines of code that were executed as a share out of the total amount of *possible* lines (lines that were compiled and used in the build, not lines of code that were not included in the complete source). Since curl offers literally many million build combinations, an evaluated code coverage number can only apply to that specific build combination. When using that exact setup and running a particular set of tests on a fixed platform.

Just getting the coverage rate off *one* of these builds is easy enough but is hardly representing the true number as we run tests on many build combinations doing many different tests.

## Can’t do it all in a single test run

We run many different tests and some of the tests we limit and split up into several different specific CI jobs since they are very slow and by doing a smaller portion of the jobs in separate CI jobs, we allow them to run in parallel and thus complete faster. That is super complicated from a code coverage point of view as we would have to merge coverage data between numerous independent and isolated build runs, possibly running on different services, to get a number approaching the truth.

We don’t even try to do this.

## Not the panacea

Eventually, even if we would be able to get a unified number from a hundred different builds and test runs spread over many platforms, what would it tell us?

libcurl has literally over 300 run-time options that can be used in combinations. Running through the code with a few different option combinations could theoretically reach almost complete code coverage and yet only test a fraction of the possibilities.

But yes: it would help us identify source code lines that are never executed when the tests run and it would be very useful.

## Instead

We rely on manual (and more error-prone) methods of identifying what parts of the code we need to add more tests for. This is hard, and generally the best way to find weak spots is when someone reports a bug or a regression as that usually means that there was a lack of tests for that area that allowed the problem to sneak in undetected.

Of course we also need to make sure that all new features and functions get test cases added in parallel.

This is a rather weak system but we have not managed to make a better one yet.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[source code](https://daniel.haxx.se/blog/tag/source-code/)[testing](https://daniel.haxx.se/blog/tag/testing/)

# Post navigation

[Previous Postcurl 8.0.1 because I jinxed it](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/)[Next Posta Bloomberg donation](https://daniel.haxx.se/blog/2023/03/28/a-bloomberg-donation/)

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

March 2023

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | [1](https://daniel.haxx.se/blog/2023/03/01/) | [2](https://daniel.haxx.se/blog/2023/03/02/) | [3](https://daniel.haxx.se/blog/2023/03/03/) | 4 | 5 |
| [6](https://daniel.haxx.se/blog/2023/03/06/) | 7 | 8 | 9 | [10](https://daniel.haxx.se/blog/2023/03/10/) | 11 | 12 |
| 13 | 14 | 15 | 16 | 17 | 18 | [19](https://daniel.haxx.se/blog/2023/03/19/) |
| [20](https://daniel.haxx.se/blog/2023/03/20/) | 21 | 22 | 23 | 24 | 25 | 26 |
| 27 | [28](https://daniel.haxx.se/blog/2023/03/28/) | [29](https://daniel.haxx.se/blog/2023/03/29/) | 30 | 31 |  | |

[« Feb](https://daniel.haxx.se/blog/2023/02/)

[Apr »](https://daniel.haxx.se/blog/2023/04/)

[Privacy](https://daniel.haxx.se/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/)