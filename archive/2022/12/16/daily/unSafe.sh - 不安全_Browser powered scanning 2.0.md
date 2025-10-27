---
title: Browser powered scanning 2.0
url: https://buaq.net/go-140174.html
source: unSafe.sh - 不安全
date: 2022-12-16
fetch_date: 2025-10-04T01:38:54.264696
---

# Browser powered scanning 2.0

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/72a8d0c173340b72ba45c418624eabd2.jpg)

Browser powered scanning 2.0

Tom Shelton-Lefley |15 December 2
*2022-12-15 22:30:0
Author: [portswigger.net(查看原文)](/jump-140174.htm)
阅读量:28
收藏*

---

Tom Shelton-Lefley |
15 December 2022 at 14:30 UTC

![That's no moon](https://portswigger.net/cms/images/7c/e0/7b0f-article-browser-powered-scanning-2-full.png)

It's been two years since we [unleashed browser powered scanning on the world](https://portswigger.net/blog/browser-powered-scanning-in-burp-suite), and we decided what better way to celebrate than to start again from scratch!

## It started out as a task, how did it end up like this?

As the [Burp Scanner](https://portswigger.net/burp/vulnerability-scanner) development team has been reminded several times over the last few months, completely re-writing the entirety of our embedded browser integration layer wasn't what we set out to achieve at the start of the quarter. So how did it happen?

The catalyst for this mammoth undertaking was something that's been an elephant in the room with users for a while now: the ability to handle browser actions that open new tabs or windows (specifically in [recorded logins](https://portswigger.net/burp/vulnerability-scanner/authenticated-scanning)). [Recorded logins](https://portswigger.net/blog/recorded-logins-in-burp-scanner) was a feature developed with external SSO providers in mind, many of which open a new tab at the start of their sign-in sequence, so this feature has been on everyone's list for some time.

You probably don't think this sounds too difficult, and neither did we - the ticket was assigned an "XS" t-shirt size when created and left as a quick win to be picked up by someone with a day or two free. We miscalculated.

Burp Scanner uses [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) to drive its embedded Chromium browser. When getting everything set up for this, there are two ways of initiating a connection:

1. Attach to a specific target, sending and receiving events over a connection isolated to only that tab or window.
2. Connect to the whole browser, multiplexing target events over a single connection.

Back when we started browser powered scanning, past us¹ decided that it would be adequate to use method 1. Whilst limiting in the long run, at the time it made everything a lot easier and suited our use-case. [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it), [KISS](https://en.wikipedia.org/wiki/KISS_principle), [et al.](https://en.wikipedia.org/wiki/Overengineering) said it was the way to go.

The problem with talking to a single target is that if something happens to create a new one, it's not part of the conversation (and if something happens to close the existing one, we're really stuffed!). Fundamentally, we couldn't track and control tabs or windows created beyond the one we were initially connected to. Herein lay the problem: To achieve our innocuous "sounds like a Friday afternoon job" ticket would require changing the absolute core of our embedded browser integration.

## A forced metaphor

So how does needing to change our Chromium connection lead us to rewriting the entire integration module?

Imagine you have a neat and tidy desk at home. Your computer and all of its peripherals are in their proper place and all of the cables are bundled and routed properly². Everything is kept untangled from everything else. If you need to replace your keyboard, or a monitor, or even the computer itself you can do so without disturbing any of the other components. Bliss.

Now imagine you need to replace the desk. Less bliss. Suddenly the fact that all of your immaculately arranged cables are zip-tied down the table legs is less than ideal …

We needed to replace our desk: Even though all of our browser powered code was nicely compartmentalized and encapsulated, changing the principle it was all built on made it easier to rip it all out and start again.

## Blowing the whole thing up is a good excuse to rebuild without a fatally flawed exhaust port

Whilst being a daunting prospect, starting again from scratch actually presented us with an opportunity to improve code and functionality at a scale not normally possible.

When we first started working on browser powered scanning in 2019 we had no idea what we were doing - it hadn't been done before. There was a lot of trial and error involved, a lot of hurdles that popped up out of nowhere, and a lot of coffee. We were very pleased with what we achieved, and have continued to improve upon it since. However (as is to be expected) we were also left with plenty of "what would you do differently next time"-s.

When we started browser powered scanning again, we *did* know what we were doing³ - it *had* been done before. *Do you know an "Obi-Wan" Chromenobi? Well of course I do, he's me.* We knew where all of the bumps in the road would be ahead of time, and were able to prepare with them in mind rather than having to react to them as we tripped.

Suddenly we had the opportunity to do all of the things we wanted to do differently, and to great effect. A few examples of things that have massively benefitted from being rewritten with lessons learned are:

* Complex navigation. Finding a better middle ground between speed for simple page refreshes and tolerance for multi-stage DOM mutations and redirects.
* Browser pooling and process management. Improving resource usage and plugging some leaks (on both the Burp Suite and Chromium sides of the fence).
* Live crawling view. Providing a method for streaming the display of the integrated browser to a frame in Burp Suite.
* Multi-target support. The actual goal we were supposed to be working on from the start.

Of course, starting from scratch has its downsides. Over the years we've stumbled across lots of little specific edge-cases or "gotchas" in Chromium's behavior and had to add or amend code paths to account for them.

Some of these "quirks" caught us out again the second time around (there were plenty of "ohhh, hang on, I know why it's doing that" moments). For example: Chromium uses epoch seconds across parts of its API instead of milliseconds … amazing. Thankfully, whilst we were brave enough to throw away most of our existing production code, we weren't foolish enough to throw away the tests!

Tests are the other asset we had this time around; not just unit tests, but also a suite of real-world web applications that either did or didn't work well with the first implementation. We were able to use these, with the help of our awesome tech support team, to ensure we improved performance on the latter without regressing the former.

## Wheel 2.0

Why do we even have a Chromium integration layer, and why are the Burp Scanner team working on it? That doesn't sound very scanner-y, can't we just use an existing library and get back to implementing [James Kettle's dark science](https://portswigger.net/research)? Why reinvent the wheel?

At PortSwigger, reinventing the wheel is pretty much our favorite thing to do. Partly because, by building our own wheel, it ensures we properly understand how that wheel works. Mainly because, more often than not, we need to do weird and specific things with our wheel that "wheel normies" probably haven't considered and accounted for.

Bizarre-analogy-that-I-wanted-to-scrap-but-the-team-said-to-keep aside, what I mean by this is that Burp Scanner is built to to break specs and standards. Unfortunately (fortunately?) existing libraries - be they for networking, serialization, or in this case driving a browser...