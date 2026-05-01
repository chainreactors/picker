---
title: Approaching zero bugs?
url: https://daniel.haxx.se/blog/2026/04/30/approaching-zero-bugs/
source: daniel.haxx.se
date: 2026-04-30
fetch_date: 2026-05-01T05:38:14.895929
---

# Approaching zero bugs?

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2017/09/bug-insect-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Approaching zero bugs?

[April 30, 2026](https://daniel.haxx.se/blog/2026/04/30/approaching-zero-bugs/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [2 Comments](https://daniel.haxx.se/blog/2026/04/30/approaching-zero-bugs/#comments)

In this era of [powerful tools to find software bugs](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/), we now see tools find a lot of problems at a high speed. This causes problems for developers, as dealing with the growing list of issues is hard. It may take a longer time to address the problems than to find them – not to mention to put them into releases and then it takes yet another extended time until users out in the wild actually get that updated version into their hands.

In order to find many bugs fast, they have to already exist in source code. These new tools don’t add or create the problems. They just find them, filter them out and bring them to the surface for exposure. A better filter in the pool filters out more rubbish.

The more bugs we fix, the fewer bugs remain in the code. Assuming the developers manage to fix problems at a decent enough pace.

For every bugfix we merge, there is a risk that the change itself introduces one more more new separate problems. We also tend to keep adding features and changing behavior as we want to improve our products, and when doing so we occasionally slip up and introduce new problems as well.

Source code analyzing tools is a concept as old as source code itself. There has always existed tools that have tried to identify coding mistakes. Now they [just recently got better](https://daniel.haxx.se/blog/2025/10/10/a-new-breed-of-analyzers/) so they can find more mistakes.

These new tools, similar to the old ones, don’t find *all* the problems. Even these new modern tools sometimes suggest fixes to the problems they find that are incomplete and in fact sometimes downright buggy.

Undoubtedly code analyzer tooling will improve further. The tools of tomorrow will find even more bugs, some of them were not found when the current generation of tools scanned the code yesterday.

Of course, we now also introduce these tools in CI and general development pipelines, which should make us land better code with fewer mistakes going forward. Ideally.

If we assume that we fix bugs faster than we introduce new ones and we assume that the AI tools can improve further, the question is then more how much more they can improve and for how long that improvement can go on. Will the tools find 10% more bugs? 100%? 1000%? Is the tool improving going to gradually continue for the next two, ten or fifty years? Can they actually find *all* bugs?

Can we reach the utopia where we have no bugs left in a given software project and when we do merge a new one, it gets detected and fixed almost instantly?

## Are we close?

If we assume that there is at least a theoretical chance to reach that point, how would we know when we reach it? Or even just if we are getting closer?

I propose that one way to measure if we are getting closer to *zero bugs* is to check the age of reported and fixed bugs. If the tools are this good, we should soon only be fixing bugs we introduced very recently.

In the curl project we don’t keep track of the age of regular bugs, but we do for vulnerabilities. The worst kind of bugs. If the tools can find almost all problems, they should soon only be finding very recently added vulnerabilities too. The age of new finds should plummet and go towards zero.

If the age of newly reported vulnerabilities are getting younger, it should make the average and median age of the total collection go down over time.

## Average age of vulnerabilities

The average and median time vulnerabilities had existed in the curl source code by the time they were found and reported to the project.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/04/Screenshot-2026-04-30-at-09-37-07-curl-Project-status-dashboard.png)

Accumulated vulnerability age when reported

## Bugfixes

When the tools have found most problems there should be less bugs left to fix. The bugfix rate should go down rapidly – independently of how you count them or how liberal we are in counting exactly what is a bugfix.

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/04/Screenshot-2026-04-30-at-09-50-17-curl-Project-status-dashboard.png)

Bugfixes

Given the data from the curl project, there does not seem to be fewer bugfixes done – yet. Maybe the bugfix speed goes up before it goes down?

## We are not close

Given the look of these graphs I don’t think we are close to *zero bugs* yet. These two curves do not seem to even start to fall yet.

Yes, these graphs are based on data from a single project, which makes it super weak to draw statistical conclusions from, but this is all I have to work with.

## So when?

I think that’s mostly an indication of what you believe the tooling can do and how good they can eventually end up becoming.

I don’t know. I will keep fixing bugs.

# Post navigation

[Previous PostInspired](https://daniel.haxx.se/blog/2026/04/30/inspired/)

## 2 thoughts on “Approaching zero bugs?”

1. ![](https://secure.gravatar.com/avatar/0d523dc4f8f760af295c493786bfb380a0e27fd6e4a5cfda2aeb3152e453703b?s=34&d=monsterid&r=g) **[Chris Swan](https://chris.swanz.net)** says:

   [April 30, 2026 at 11:30](https://daniel.haxx.se/blog/2026/04/30/approaching-zero-bugs/#comment-27436)

   There’s an excellent paper on this from ~20y ago: “Milk or Wine: Does Software Security Improve with Age?” [pdf]

   <https://www.usenix.org/legacy/event/sec06/tech/full_papers/ozment/ozment.pdf>

   They build a model for bug/vuln arrival rate and discovery rate, which then leads to an estimate for latent vulns.

   It’s the first thing I thought about as news of Mythos/Glasswing broke.

   [Reply](https://daniel.haxx.se/blog/2026/04/30/approaching-zero-bugs/?replytocom=27436#respond)
2. ![](https://secure.gravatar.com/avatar/016701fd30c1bba9c3a440cca88e4135bd7cc2b89da246491a79a518ce83ec5a?s=34&d=monsterid&r=g) **[Mohcin Bounouara](https://mohcinbounouara.com/)** says:

   [April 30, 2026 at 21:53](https://daniel.haxx.se/blog/2026/04/30/approaching-zero-bugs/#comment-27437)

   I think AI tools are tools at the end, so they will fix and not catch all the bugs..

   [Reply](https://daniel.haxx.se/blog/2026/04/30/approaching-zero-bugs/?replytocom=27437#respond)

### Leave a Reply [Cancel reply](/blog/2026/04/30/approaching-zero-bugs/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Time limit is exhausted. Please reload CAPTCHA.
three6sevenseven6

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Recent Posts

* [Approaching zero bugs?](https://daniel.haxx.se/blog/2026/04/30/approaching-zero-bugs/)
  April 30, 2026
* [Inspired](https://daniel.haxx.se/blog/2026/04/30/inspired/)
  April 30, 2026
* [curl 8.20.0](https://daniel.haxx.se/blog/2026/04/29/curl-8-20-0/)
  April 29, 2026
* [High-Quality Chaos](https://daniel.haxx.se/blog/2026/04/22/high-quality-chaos/)
  April 22, 2026
* [Don’t trust, verify](https://daniel.haxx.se/blog/2026/03/26/dont-trust-verify/)
  March 26, 2026
* [One hundred weirdo emails](https://daniel.haxx.se/blog/2026/03/25/one-hundred-weirdo-emails/)
  March 25, 2026

# Recent Comments

* [Mohcin Bounouara](http...