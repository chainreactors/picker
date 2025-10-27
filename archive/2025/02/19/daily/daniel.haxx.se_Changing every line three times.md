---
title: Changing every line three times
url: https://daniel.haxx.se/blog/2025/02/18/changing-every-line-three-times/
source: daniel.haxx.se
date: 2025-02-19
fetch_date: 2025-10-06T20:36:43.273146
---

# Changing every line three times

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/07/we-need-more-curl-bugfixes-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Changing every line three times

[February 18, 2025](https://daniel.haxx.se/blog/2025/02/18/changing-every-line-three-times/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [2 Comments](https://daniel.haxx.se/blog/2025/02/18/changing-every-line-three-times/#comments)

Is there some magic making three times, or even pi, the number of times you need to write code for it to be good?

So what am I talking about? Let’s rewind and start with talking about writing code.

Let’s say you start out by writing a program that is exactly one hundred lines long, and you release your creation to the world. Every line in this program was written just once.

Then someone reports a bug so you change source code lines. Say you change ten lines. Which is the equivalent of adding ten lines and removing ten lines. The total number of lines remains 100 lines, but you have written 110. The average line has then been changed 1.1 times.

Over time, you come to change more lines and if the project survives you probably add new code too. A living software project that is maintained is bound to have had many more lines added than what is currently present in the current working source code branch.

*Exactly how many more lines were added than what is currently present?*

That is the question that I asked myself regarding curl development. If we play with the thought that curl is a decently mature project as it has been developed for over twenty-five years maybe the number of times every line has been changed would tell us something?

By counting the number of added lines and comparing how many lines of code are still present, we know how often lines are changed – on average. Sure, some lines in the file headers and similar are probably rarely changed and some others are changed all the time, but let’s smear out the data and just count average.

curl is also an interesting test subject here because it has grown *significantly* over time. It started out as 180 lines of code in 1996 (then called *httpget*) and is almost 180,000 lines of code today in early 2025. An almost linear growth in number of lines of code over time, while at the same time having a fierce rate of bugfixes and corrections done.

I narrowed this research to all the *product code* only, so it does not include test cases, documentation, examples etc. I figured that would be the most interesting bits.

## Number of lines of code

First a look at the raw number of how many lines of product code is present at different moments in time during the project’s history.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/02/Screenshot-2025-02-18-at-14-33-25-curl-Project-status-dashboard.png)

## Added LOC per LOC still present

Then, counting the number of added lines of code (LOC) and comparing with how many lines of code are still present. As you can see here, the change rate is around three for a surprisingly long time.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/02/Screenshot-2025-02-18-at-14-32-29-curl-Project-status-dashboard.png)

Already by 2004 we had modified every line on average three times. The rate of changes then goes up and down a little but remains roughly three for years until 2015 something when the change rate start to gradually increase a little to 3.5 in early 2025 – while at the same time the number of lines of code in the project kept growing.

Today, February 18 2025 actually marks the day when it was calculated to a number above 3.5 for the first time ever.

## What does it mean?

It means that every line in the product source code tree have by now been edited on average 3.5 times. It might been that we have written bad code and need to fix many bugs or that go back to refactor and improve existing lines frequently. Probably both.

Of course, some lines are edited and changed far more often than others, the 3.5 is just an average. We have some source lines left in the code that was brought before year 2000 and have not been changed since.

# Post navigation

[Previous PostOpenSSL does a QUIC API](https://daniel.haxx.se/blog/2025/02/16/openssl-does-a-quic-api/)[Next Postcurl website traffic Feb 2025](https://daniel.haxx.se/blog/2025/02/22/curl-website-traffic-feb-2025/)

## 2 thoughts on “Changing every line three times”

1. ![](https://secure.gravatar.com/avatar/6d446c3138833e2143a1e5bf2f8ccdc7e13c82b4b71af2f8ad7b4e43ddc650af?s=34&d=monsterid&r=g) **Matthias Hörmann** says:

   [February 19, 2025 at 09:38](https://daniel.haxx.se/blog/2025/02/18/changing-every-line-three-times/#comment-27134)

   I suspect that this type of measurement is highly language dependent, e.g. I would expect the average line of Haskell (a very expressive language that also has a habit of putting entire chains of expressions on a single line) to change more often than the average line of Java (a very verbose language where a lot of lines are just boilerplate or syntax fluff that have little to no potential for bugs at all because they express very little about the program logic).

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [February 19, 2025 at 09:49](https://daniel.haxx.se/blog/2025/02/18/changing-every-line-three-times/#comment-27135)

      @Matthias: probably, yes. It also depends at least partly on what kind of line (length) and source code policy you have in the project.

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
* Tjark on [car brands ru...