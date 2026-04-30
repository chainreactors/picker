---
title: Claude Mythos Has Found 271 Zero-Days in Firefox
url: https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html
source: Schneier on Security
date: 2026-04-29
fetch_date: 2026-04-30T05:30:25.378608
---

# Claude Mythos Has Found 271 Zero-Days in Firefox

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Claude Mythos Has Found 271 Zero-Days in Firefox

That’s [a lot](https://blog.mozilla.org/en/firefox/ai-security-zero-day-vulnerabilities/). No, it’s an extraordinary number:

> Since February, the Firefox team has been working around the clock using frontier AI models to find and fix latent security vulnerabilities in the browser. We wrote previously about our collaboration with Anthropic to scan Firefox with Opus 4.6, which led to fixes for 22 security-sensitive bugs in Firefox 148.
>
> As part of our continued collaboration with Anthropic, we had the opportunity to apply an early version of Claude Mythos Preview to Firefox. This week’s release of Firefox 150 includes fixes for 271 vulnerabilities identified during this initial evaluation.
>
> As these capabilities reach the hands of more defenders, many other teams are now experiencing the same vertigo we did when the findings first came into focus. For a hardened target, just one such bug would have been red-alert in 2025, and so many at once makes you stop to wonder whether it’s even possible to keep up.
>
> Our experience is a hopeful one for teams who shake off the vertigo and get to work. You may need to reprioritize everything else to bring relentless and single-minded focus to the task, but there is light at the end of the tunnel. We are extremely proud of how our team rose to meet this challenge, and others will too. Our work isn’t finished, but we’ve turned the corner and can glimpse a future much better than just keeping up. **Defenders finally have a chance to win, decisively.**

They’re right. Assuming the defenders can patch, and push those patches out to users quickly, this technology favors the defenders.

News [article](https://arstechnica.com/ai/2026/04/mozilla-anthropics-mythos-found-271-zero-day-vulnerabilities-in-firefox-150/).

Tags: [AI](https://www.schneier.com/tag/ai/), [Firefox](https://www.schneier.com/tag/firefox/), [zero-day](https://www.schneier.com/tag/zero-day/)

[Posted on April 29, 2026 at 6:12 AM](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html) •
[24 Comments](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html#comments)

### Comments

Ismar •
[April 29, 2026 6:44 AM](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html/#comment-454071)

Hmmm, how many of those vulnerabilities are actually exploitable by those outside the few nation-level attackers who can already do this with using Mythos?

Anonymous •
[April 29, 2026 6:52 AM](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html/#comment-454072)

271 zero days! It’s not enough to “just” fix the code anymore. The coders responsible for introducing the zero days need to be fired and blacklisted on suspicion of sabotage.

Har de har har •
[April 29, 2026 7:29 AM](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html/#comment-454075)

271, that’s three quarters of a zero-year!

hello again •
[April 29, 2026 7:34 AM](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html/#comment-454076)

This post made me realize that I had not bothered to update Firefox for Android. The date on the patch was April 15th. This is what the patch notes said.

> Behind-the-scenes updates to keep your browsing steady, smooth, and responsive.

Thanks for the information!

Clive Robinson •
[April 29, 2026 7:55 AM](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html/#comment-454077)

@ Bruce, ALL,

Maybe we should look a little closer at the article when it says,

> *“This week’s release of Firefox 150 includes fixes for 271 vulnerabilities identified during this initial evaluation.”*

Before making claims… Because that’s effectively “diplomatic double speak” being deployed…

That last part of,

“identified during this initial evaluation”

Tells us that those “271 vulnerabilities” are in effect a “low water mark”, from “the first run” of the tool against the code base…

Or to put it another way,

“An initial discovery of 271 vulnerabilities with probably more to come from later runs of the tooi…

[Miguel Farah](https://www.farah.cl/) •
[April 29, 2026 8:36 AM](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html/#comment-454078)

That a security-focused audit (AI or not) found this many bugs speaks of poor quality source code and an extremely shallow (or non-existing?) code review process. This is impressive… but not for the same reasons.

I wonder whether a “regular” code audit would have found a similar amount of problems, and I also wonder what was the “raw” number of observations made, before discarding out the false positives down to the 271 confirmed ones.

Ed25519 •
[April 29, 2026 9:16 AM](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html/#comment-454081)

A buddy of mine shared this article with me. A pretty good critique of these findings. Turns out its a bit more marketing fluff than we typically like to see.

I’m sure AI bug finding has a bright future, but the 271 0-days is a bit overblown.

<https://www.flyingpenguin.com/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/>

Security Sam •
[April 29, 2026 9:17 AM](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html/#comment-454082)

271 = BGA = Big Gay Anus!

Hooray!

ALFDAD - Live & Pissed •
[April 29, 2026 9:20 AM](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html/#comment-454084)

I JUST WANT TO BE THE BEST LOVER I CAN BE TO YOU, ALF.

WILLIE! YOU THINK I’M A F/\GGOT?

Oh, ALF, I thought you LIKED F/\ggots.

You know I love you, ALF.

I’ll go down on ya, ALF.

the love the love the love illusion •
[April 29, 2026 9:40 AM](https://www.schneier.com/blog/archives/2026/04/claude-mythos-has-found-271-zero-days-in-firefox.html/#comment-454086)

It’s clear, use the [Dillo](https://dillo-browser.org/) browser.

Dillo is a fast and small graphical web browser with the following features:

* Multi-platform, running on Linux, BSD, MacOS, Windows (via Cygwin) and even Atari.
* Written in C and C++ with few dependencies.
* Implements its own real-time rendering engine.
* Low memory usage and fast rendering, even with large pages.
* Uses the fast and bloat-free FLTK GUI library.
* Support for HTTP, HTTPS, FTP and local files.
* Extensible with plugins written in any language (see the list of plugins).
* Is free software licensed with the GPLv3.
* Helps authors to comply with web standards by using the bug meter Bugmeter icon.

James •
[April 29, 2026 9:54 AM](https://www.schnei...