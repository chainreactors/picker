---
title: A twenty-five years old curl bug
url: https://daniel.haxx.se/blog/2024/12/12/a-twenty-five-years-old-curl-bug/
source: daniel.haxx.se
date: 2024-12-13
fetch_date: 2025-10-06T19:37:14.643496
---

# A twenty-five years old curl bug

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/09/old-machine.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Security](https://daniel.haxx.se/blog/category/tech/security/)

# A twenty-five years old curl bug

[December 12, 2024](https://daniel.haxx.se/blog/2024/12/12/a-twenty-five-years-old-curl-bug/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [2 Comments](https://daniel.haxx.se/blog/2024/12/12/a-twenty-five-years-old-curl-bug/#comments)

I have talked about old curl bugs before, but now we have a new curl record.

When we announced the security flaw [CVE-2024-11053](https://curl.se/docs/CVE-2024-11053.html) on December 11, 2024 together with the release of [curl 8.11.1](https://daniel.haxx.se/blog/2024/12/11/curl-8-11-1/) we fixed a security bug that was introduced in a curl release **9039** days ago. That is close to twenty-five years.

The previous record holder was [CVE-2022-35252](https://curl.se/docs/CVE-2022-35252.html) at 8729 days.

Now at [161 reported CVEs](https://curl.se/docs/security.html), the *median* time a security problem has existed in curl until fixed is **2583** days, a little over seven years.

## Age

We know the age of every single curl security problem because every time we have a confirmed one, I spend a significant time and effort digging through the source code history to figure out in which exact commit the problem was introduced.

(This is also how we know that almost every CVE we have ever announced was introduced by *my* mistakes.)

## What’s Wrong?

I don’t think anyone is doing anything wrong here. I think it illustrates the difficulty and challenges involved. There are a lot of people looking at curl code all the time. We run tests and analyzers on the code, all the time. In fact, in November 2024 alone, we had CI jobs running on GitHub alone at 9.17 CPU days per day. Meaning that on average more than nine machines were running curl tests and builds to help us verify that it works as intended.

Apart from that, we of course have all the human individual testers, security researchers and the Google OSS-Fuzz project that is fuzzing curl non-stop and has been doing so for the last 6-7 years.

*Security is hard.* I mean really really hard.

I have no immediate ideas how to find the next such bug other than the plain old: add more test cases for scenarios and setups not previously tested. That is hard, difficult and quite frankly quite boring work that nobody in particular wants to do nor fund someone else to do.

## Enough eyeballs

I think we all agree by now that not all bugs are shallow. Or perhaps we can’t ever truly get enough eyeballs. Or maybe the saying works, just that it needs an addendum

*Given enough eyeballs **and time**, all bugs are shallow*

## Learn from each mistake

It is often said, and it is true, that you learn from mistakes. The question is only what exactly to learn from each and every reported security vulnerability. Each new one always feels like a unique stupid mistake that was a one-off that *surely* will not happen again because that situation is now gone and we have no other like that.

## Not a C mistake

Let me also touch this subject while talking security problems. This bug, the oldest so far in curl history, was a plain logic error and would not have been avoided had we used another language than C.

Otherwise, about 40% of all security problems in curl can be blamed on us using C instead of a memory-safe language. 50% of the high/critical severity ones.

Almost all of those C mistakes were done before there even existed a viable alternative language – if that even exists now.

## Graphs

I decided to not sprinkle graph images in the post this time. You can find data and graphs for all my claims in here in the [curl dashboard](https://curl.se/dashboard.html).

## Sad update

After intensive bisecting, it turns out this bug was incorrectly believed to have been introduced in a certain commit, while in fact it was introduced *much* later. As of January 7th 2025, we have updated the metadata for this CVE and now it is no longer the oldest bug fixed in curl…

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous Postcurl 8.11.1](https://daniel.haxx.se/blog/2024/12/11/curl-8-11-1/)[Next Postdropping hyper](https://daniel.haxx.se/blog/2024/12/21/dropping-hyper/)

## 2 thoughts on “A twenty-five years old curl bug”

1. ![](https://secure.gravatar.com/avatar/ae611143af8098268b5da57d7ea71845c0823f51b69287e0067993e193b95897?s=34&d=monsterid&r=g) **Kay-Uwe** says:

   [December 14, 2024 at 07:49](https://daniel.haxx.se/blog/2024/12/12/a-twenty-five-years-old-curl-bug/#comment-27089)

   Hi,

   When you say “Almost all of those C mistakes were done before there even existed a viable alternative language – if that even exists now.” What about Ada/SPARK? Ada is around since 1980 and it avoids a lot of stupid C mistakes by design.
   SPARK might by a solution for a lot of logical errors and it also avoid a lot of testing by proving the program is error “free” (follow the defined purpose) once.

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [December 14, 2024 at 10:49](https://daniel.haxx.se/blog/2024/12/12/a-twenty-five-years-old-curl-bug/#comment-27090)

      @Kay-Uwe: because that is not a viable language for writing system libraries. Which you already know and is one reason why no widely used system libraries are written in anything else than C even today.

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
* H. Stefan on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-c...