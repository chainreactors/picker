---
title: AIs Discovering Vulnerabilities
url: https://www.schneier.com/blog/archives/2024/11/ais-discovering-vulnerabilities.html
source: Schneier on Security
date: 2024-11-06
fetch_date: 2025-10-06T19:20:21.922581
---

# AIs Discovering Vulnerabilities

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

## AIs Discovering Vulnerabilities

I’ve been [writing about](https://www.schneier.com/essays/archives/2018/03/artificial_intellige.html) the possibility of AIs automatically discovering code vulnerabilities since at least 2018. This is an ongoing area of research: AIs doing source code scanning, AIs finding zero-days in the wild, and everything in between. The AIs aren’t very good at it yet, but they’re getting better.

Here’s some [anecdotal data](https://zeropath.com/blog/0day-discoveries) from this summer:

> Since July 2024, ZeroPath is taking a novel approach combining deep program analysis with adversarial AI agents for validation. Our methodology has uncovered numerous critical vulnerabilities in production systems, including several that traditional Static Application Security Testing (SAST) tools were ill-equipped to find. This post provides a technical deep-dive into our research methodology and a living summary of the bugs found in popular open-source tools.

Expect lots of developments in this area over the next few years.

This is what I [said](https://ieeexplore.ieee.org/document/10718663) in a recent interview:

> Let’s stick with software. Imagine that we have an AI that finds software vulnerabilities. Yes, the attackers can use those AIs to break into systems. But the defenders can use the same AIs to find software vulnerabilities and then patch them. This capability, once it exists, will probably be built into the standard suite of software development tools. We can imagine a future where all the easily findable vulnerabilities (not all the vulnerabilities; there are lots of theoretical results about that) are removed in software before shipping.
>
> When that day comes, all legacy code would be vulnerable. But all new code would be secure. And, eventually, those software vulnerabilities will be a thing of the past. In my head, some future programmer shakes their head and says, “Remember the early decades of this century when software was full of vulnerabilities? That’s before the AIs found them all. Wow, that was a crazy time.” We’re not there yet. We’re not even remotely there yet. But it’s a reasonable extrapolation.

EDITED TO ADD: And Google’s LLM [just discovered](https://www.scworld.com/news/googles-big-sleep-llm-agent-discovers-exploitable-bug-in-sqlite) an exploitable zero-day.

Tags: [AI](https://www.schneier.com/tag/ai/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/), [zero-day](https://www.schneier.com/tag/zero-day/)

[Posted on November 5, 2024 at 7:08 AM](https://www.schneier.com/blog/archives/2024/11/ais-discovering-vulnerabilities.html) •
[15 Comments](https://www.schneier.com/blog/archives/2024/11/ais-discovering-vulnerabilities.html#comments)

### Comments

Glen •
[November 5, 2024 7:13 AM](https://www.schneier.com/blog/archives/2024/11/ais-discovering-vulnerabilities.html/#comment-441500)

I’m looking forward to this being a stage in my Jenkins pipeline!

Clive Robinson •
[November 5, 2024 9:20 AM](https://www.schneier.com/blog/archives/2024/11/ais-discovering-vulnerabilities.html/#comment-441503)

With regards,

> “AIs doing source code scanning, AIs finding zero-days in the wild, and everything in between. The AIs aren’t very good at it yet, but they’re getting better.”

An obvious observation applies,

“The blind leading the blind.”

Lets be honest humans are not very good at it either… So the usual way of learning to do it is by,

“Fumbling around in the dark till you develop a hinky/spidey sense.”

Eventually you get a feel for “patterns” and these warn you of problem areas and where to look more closely.

Thus it’s learning not just to hear the signal in the noise but what is just noise and what are the various types signal within it.

We’ve done this before back at the end of the last century with “extracting secrets” from “Power Signitures” on smart cards and what are now seen as obsolete 8bit microcontrollers and similar.

For some reason once discovered few people went further with it, even though much earlier back from the mid 1960’s one software diagnostic tool was an AM radio tuned to a harmonic of the computer clock frequency. Where the “envelope modulation” produced a sound that was indicative of what the code was doing.

In the “academic community” this kind of got relegated to student projects written in assembler to play “tunes” and similar.

Some year ago when talking about “Castles -v- Prisons” I went into quite some detail about doing this by having a hypervisor looking for aberrant signals or changes in expected signals from executing programs in small single task computing units I called Prisons.

Such changes in signal signatures indicated that the code functioning of a tasklet in a prison was not as expected, thus something was wrong such as error, or on otherwise debugged code untested/allowed input or malware thus an exception needed to be raised and investigated.

In theory this is very easy to do you just simplify the code into individual tasks with clear function thus a clear “signal against time” could be established and then develop an appropriate monitoring mask.

Thus we get back to the idea of “Digital Signal Processing”(DSP) and “Adaptive filtering” around a base mask.

As we actually know how to do this, I would expect us to be able to get an LLM system to do it. Provided we keep the tasks sufficiently defined and simplified.

This has been one of the promises of very small RISC cores in superscalar arrangements using highly parallel processing. Only the way we’ve gone done the superscalar path on the hardware side of things has made it a very rough road.

This is because humans are very bad at doing parallel programming and appear stuck in an ever increasingly awkward form of sequential programming.

Thus I predict that what will probably need to happen is that some form of yet to be AI will need to take human written “high level code” that will be in effect “sequential” and produce via the compiler optimised parallel code that will give clear signatures.

Yes I can see the arguments, but remember we have been walking down a similar path with RISC designs that in the 1990’s led to Intel’s idea of “EPIC” on the Itanium processors that turned into a bit of a disaster. Especially with AMD coming up with a clean way thus their x64 system that Intel ended up having to licence. Some say because of Microsoft digging their heals in and refusing to go down into Intel’s way.

Thus a second warning is that for AI to do this in a cost efficient way, it needs the “software tool chain” developers to be very much on board with it…

And that will probably be the major stumbling block with patents used to put in road blocks to protect what are monopoly positions.

Alex M •
[November 5, 2024 9:30 AM](https://www.schneier.com/blog/archives/2024/11/ais-discovering-vulnerabilities.html/#comment-441504)

It’s a strange ...