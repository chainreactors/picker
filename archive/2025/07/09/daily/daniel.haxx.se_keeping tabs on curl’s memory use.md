---
title: keeping tabs on curl’s memory use
url: https://daniel.haxx.se/blog/2025/07/08/keeping-tabs-on-curls-memory-use/
source: daniel.haxx.se
date: 2025-07-09
fetch_date: 2025-10-06T23:49:26.529133
---

# keeping tabs on curl’s memory use

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/07/speedometer.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# keeping tabs on curl’s memory use

[July 8, 2025](https://daniel.haxx.se/blog/2025/07/08/keeping-tabs-on-curls-memory-use/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/)

One of the harder things to look out for in a software project is slow or gradual decay over a long period of time. Like if we gradually make a library 1% slower or use 2% more memory every other month.

Sometimes it is totally acceptable to make code slower and use more memory because everything we do is a balance and sometimes we want new features or improved performance that might have to use more memory etc.

We don’t want the growth or slowing down to happen without it being an explicit decision and known trade-off. If we know what the trade-off is, we can reconsider and turn down a feature because we deem the cost too high. Or we accept it because the feature is useful.

In the curl project we make an concerned effort to keep memory use and allocations to a minimum and we are proud of our work. But we also continuously try to encourage and involve more contributors and it is easy to sometimes slip and do something in the code that maybe is not the wisest idea – memory wise.

## Memory

In curl we have recently introduced a number of different checks to help us remain aware of the exact memory allocation and use situation.

An added complication for us is that curl builds and runs on numerous architectures, with lots of features on and off and with different sets of third party libraries. It means that internal struct sizes are rarely exactly the same on two different builds and code paths differ that may allocate data differently. We must make all memory limit checks with a certain amount of flexibility and margin.

### Per test-case

We have introduced a system where we can specify exact limits for a single test case: this test may not do more than N allocations and it may not have more than Z bytes allocated concurrently.

We do this in debug-builds only where we have wrapper functions for all memory functions used in curl so doing this accounting is quite easy.

The idea is to set fairly strict memory limits in a number of selected *typical* test cases. We don’t use them in all test cases because when we in the future deem we want to allow increased memory use, it could easily become inconvenient and burdensome.

There is also default limits brought with this, so that tests that really need many allocations (more than 1,000) or unusually large amount of memory (more than 1MB concurrently) have to declare that in the test case or fail because of the *suspicious* behavior.

### Primary struct sizes

A second size check was added in a new dedicated test case: it verifies that a number of important internal structs are sized within their allowed limits.

Keeping such struct sizes in check is important because we allocate a certain struct for each easy handle, each multi handle and for each concurrent connection etc. Because applications sometimes want to use a lot of those (from hundreds to several thousands), it is important that we keep them small.

This new test case makes sure that we don’t accidentally enlarge these structs and make users suffer. Maybe as a secondary effect, we can also use this test case and come back in ten years and see how much the sizes changed.

## Memory allocated by others

While we work hard on reducing and keeping curl’s own memory use in check, curl also normally uses a number of third party libraries for fundamental parts of its operations: for TLS, compression and more. The memory monitoring and checks I write about in this post are however explicitly designed and intended to *not* check or include memory allocated and used by such third parties because we cannot easily affect them. It is up to every such library’s dev team to work on their code towards their own goals that may not be the same as ours.

This is of course frustrating at the same time. Downloading `https://curl.se/` using the curl tool uses around 134 allocations done from curl and libcurl code. If curl is built with OpenSSL 3.5.0, the total amount of allocations such a command perform is over 54,000. Down from OpenSSL 3.4.1 which used over 200K!

Different TLS libraries clearly have totally different characteristics here. Rustls for example performed the same simple use case needing [just 2,176 allocations](https://hachyderm.io/%40cpu/114812537617398093) and a *much* smaller peak usage at the same time.

My friends working on wolfSSL have several different configure options to tweak and optimize the malloc patterns. The full build I tested with used more allocations than OpenSSL 3.5.0 but less than half the peak amount.

## Still worth it

I am a strong believer in each project making their best and keeping their own backyard clean and tidy.

Sure, **curl does less than 0.3% of the allocations by itself** when downloading https://curl.se using the latest OpenSSL version for TLS. This is still not a reason for *us* to be sloppy or to lower our guard rails. Instead I hope that we can lead by example.

This is what makes us proud as engineers and it makes our users trust us and appreciate what we ship.

People can use other TLS libraries. TLS library developers can improve their allocation patterns. And perhaps most importantly: in many cases the number of allocations or amount of used memory do not matter much.

## Transfer speed checks next?

We want to add similar checks and verification for transfer speeds but that is an entirely different challenge and something that is being worked on separately from these changes.

## Credits

Top image by [LoggaWiggler](https://pixabay.com/users/loggawiggler-15/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4781) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4781)

# Post navigation

[Previous Postcurl user survey 2025 analysis](https://daniel.haxx.se/blog/2025/07/03/curl-user-survey-2025-analysis/)[Next Postmore views on curl vulnerabilities](https://daniel.haxx.se/blog/2025/07/10/more-views-on-curl-vulnerabilities/)

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
* A. Ros on [car brands running curl](https://daniel.haxx.se/blog/2025/08/...