---
title: decomplexification continued
url: https://daniel.haxx.se/blog/2026/02/24/decomplexification-continued/
source: daniel.haxx.se
date: 2026-02-24
fetch_date: 2026-02-25T04:13:45.776665
---

# decomplexification continued

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/), [Development](https://daniel.haxx.se/blog/category/development/)

# decomplexification continued

[February 24, 2026](https://daniel.haxx.se/blog/2026/02/24/decomplexification-continued/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/02/24/decomplexification-continued/#respond)

Last spring I wrote [a blog post](https://daniel.haxx.se/blog/2025/05/29/decomplexification/) about our ongoing work in the background to gradually simplify the curl source code over time.

This is a follow-up: a status update of what we have done since then and what comes next.

In May 2025 I had just managed to get the worst function in curl down to complexity 100, and the average score of all curl production source code (179,000 lines of code) was at 20.8. We had 15 functions still scoring over 70.

Almost ten months later we have reduced the most complex function in curl from 100 to 59. Meaning that we have simplified a vast number of functions. Done by splitting them up into smaller pieces and by refactoring logic. Reviewed by humans, verified by lots of test cases, checked by analyzers and fuzzers,

The current 171,000 lines of code now has an average complexity of 15.9.

## Complexity

The complexity score in this case is just the cold and raw metric reported by the pmccabe tool. I decided to use that as the absolute truth, even if of course a human could at times debate and argue about its claims. It makes it easier to just obey to the tool, and it is quite frankly doing a decent job at this so it’s not a problem.

## How to simplify

In almost all cases the main problem with complex functions is that they do a lot of things in a single function – too many – where the functionality performed could or should rather be split into several smaller sub functions. In almost every case it is also immediately obvious that when splitting a function into two, three or more sub functions with smaller and more specific scopes, the code gets easier to understand and each smaller function is subsequently easier to debug and improve.

## Development

I don’t know how far we can take the simplification and what the ideal average complexity score of a the curl code base might be. At some point it becomes counter-effective and making functions even smaller then just makes it harder to follow code flows and absorbing the proper context into your head.

## Graphs

To illustrate our simplification journey, I decided to render graphs with a date axle starting at 2022-01-01 and ending today. Slightly over four years, representing a little under 10,000 git commits.

First, a look a the complexity of the *worst* scored function in curl production code over the last four years. Comparing with P90 and P99.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/02/complexity.png)

The most complex function in curl over time

Identifying the worst function might not say too much about the code in general, so another check is to see how *the average complexity* has changed. This is calculated like this:

* All functions get a complexity score by pmccabe
* Each function has a number of lines

For all functions, add its function-score x function-length to a total complexity score, and in the end, divide that total complexity score on total number of lines used for all functions. Also do the same for a median score.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/02/line-complex.png)

Average and median complexity per source code line in curl, over time.

When 2022 started, the average was about 46 and as can be seen, it has been dwindling ever since, with a few steep drops when we have merged dedicated improvement work.

One way to complete the average and median lines to offer us a better picture of the state, is to investigate the complexity distribution through-out the source code.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/02/complex-dist.png)

How big portion of the curl source code is how complex

This reveals that the most complex *quarter* of the code in 2022 has since been simplified. Back then 25% of the code scored above 60, and now all of the code is below 60.

It also shows that during 2025 we managed to clean up all the dark functions, meaning the end of 100+ complexity functions. Never to return, as the plan is at least.

## Does it matter?

We don’t really know. We believe less complex code is generally good for security and code readability, but it is probably still too early for us to be able to actually *measure* any particular positive outcome of this work (apart from fancy graphs). Also, there are many more ways to judge code than by this complexity score alone. Like having sensible APIs both internal and external and making sure that they are properly and correctly documented etc. The fact that they all interact together and they all keep changing, makes it really hard to isolate a single factor like complexity and say that changing this alone is what makes an impact.

Additionally: maybe just the refactor itself and the attention to the functions when doing so either fix problems or introduce new problems, that is then not actually because of the change of complexity but just the mere result of eyes giving attention on that code and changing it right then.

Maybe we just need to allow several more years to pass before any change from this can be measured?

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Development](https://daniel.haxx.se/blog/tag/development/)

# Post navigation

[Previous PostOpen Source security in spite of AI](https://daniel.haxx.se/blog/2026/02/03/open-source-security-in-spite-of-ai/)

### Leave a Reply [Cancel reply](/blog/2026/02/24/decomplexification-continued/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
three71one4

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [decomplexification continued](https://daniel.haxx.se/blog/2026/02/24/decomplexification-continued/)
  February 24, 2026
* [Open Source security in spite of AI](https://daniel.haxx.se/blog/2026/02/03/open-source-security-in-spite-of-ai/)
  February 3, 2026
* [A third medal](https://daniel.haxx.se/blog/2026/02/02/a-third-medal/)
  February 2, 2026
* [GregKH awarded the Prize for Excellence in Open Source 2026](https://daniel.haxx.se/blog/2026/01/30/gregkh-awarded-the-prize-for-excellence-in-open-source-2026/)
  January 30, 2026
* [curl distro meeting 2026](https://daniel.haxx.se/blog/2026/01/28/curl-distro-meeting-2026/)
  January 28, 2026
* [Improving curl -J](https://daniel.haxx.se/blog/2026/01/27/improving-curl-j/)
  January 27, 2026

# Recent Comments

* Jesse on [A third medal](https://daniel.haxx.se/blog/2026/02/02/a-third-medal/comment-page-1/#comment-27403)
* [Lawrence Li](https://lawrenceli.me) on [GregKH awarded the Prize for Excellence in Open Source 2026](https://daniel.haxx.se/blog/2026/01/30/gregkh-awarded-the-prize-for-excellence-in-open-source-2026/comment-page-1/#comment-27401)
* [Daniel Stenberg](https://daniel.haxx.se/) on [curl distro meeting 2026](https://daniel.haxx.se/blog/2026/01/28/curl-distro-meeting-2026/comment-page-1/#comment-27398)
* [Anatolij Vasilev](https://r0.fyi/) on [curl distro meeting 2026](https://daniel.haxx.se/blog/2026/01/28/curl-distro-meeting-2026/comment-page-1/#comment-27397)
* ...