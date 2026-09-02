---
title: Un-Racing Issues
url: https://www.tbray.org/ongoing/When/202x/2026/09/01/Un-Racing
source: ongoing by Tim Bray
date: 2026-09-01
fetch_date: 2026-09-02T06:39:33.436024
---

# Un-Racing Issues

# Un-Racing Issues

![Opens, and navigates to, search input field](/ongoing/misc/smallmag.png)

I just landed a PR that fixed a nasty data race in
[Quamina](https://github.com/timbray/quamina). Which shouldn’t have been technically challenging, but I took
side-trips into Erlang, unit test footguns, whether or not I should go on accepting LLM-generated PRs, and programming while aging.

Let’s address that last issue first.

“No” on clanker PRs ·
In late 2026 we know that:

1. Claude and its competitors can write perfectly decent code, particularly where the task at hand can be
   narrowly focused.
2. They’re also good-to-excellent at detecting vulnerabilities.
3. The underlying GenAI technology has serious negative externalities in (at least) the domains of environmental impact
   and intellectual property.
4. Using this technology might enrich and empower people about whom I feel contempt and
   fear.
5. The vast majority of people whom I care about and respect are experiencing real unhappiness about the GenAI
   big picture.

I’ve never personally put clankers seriously to work and for now I’ll continue not to. I *have* been
accepting Claude-authored PRs but, to the extent I can detect them, I’m stopping. This will have a real cost; some of
those PRs yielded big performance boosts. Also, they were built much
faster than I could have managed.

But the picture is mixed. Specifically, I have to admit that I don’t really understand the 500 or so lines of clanker
[code](https://github.com/timbray/quamina/blob/main/epsi_closure.go) and
[test](https://github.com/timbray/quamina/blob/main/epsi_closure_test.go) that compute epsilon closures for
nondeterministic finite automata. Sufficiently so that I’ve
[written an issue](https://github.com/timbray/quamina/issues/580) to think it over, understand it, and with any luck,
simplify it.

Interestingly, we got to the current epsilon-closure code in a sequence of reasonable-looking PRs that I reviewed,
asking for changes in most. But in the big picture my reviewing was
ineffective, because it ended with a large lump of code that I don’t understand or, at the end of the day, trust. I wonder how
typical that outcome is?

There’s an exception to my new policy: Vulnerability reports. I think it’d be irresponsible to ignore them and penalize
Quamina’s users because I don’t like the source. Somebody
[did a Claude scan](https://github.com/timbray/quamina/issues/437) which found 14 problems at various levels of criticality.
I’ve created issues and hope to retire them all soon.

Pruner race ·
The ugliest problem the clanker found was a data race in a piece of Quamina called
[pruner](https://github.com/timbray/quamina/blob/main/pruner.go). So I bashed out a quick unit test that ran several
thousand read operations in one goroutine and the same number of updates in another. Sure enough,
on its first run it instantly exploded in a flurry of data-race complaints.

The problem wasn’t complex and my first cut at a fix worked fine, the unit test running flawlessly. But, also
very slowly. I (reasonably, I thought) went looking for contention problems around the mutexes I’d just added.
The profiler seemed to be saying that the slowdown was in Quamina’s core matching methods, but that made no
sense at all, so I dug deeper and deeper into the Go sync primitives. And found nothing useful.

Concurrency bugs are extra irritating. Also, I’m
semi-retired and doing this for fun, so I put it down and ignored it for a few weeks.

Functional love ·
There was a bright spot in this sad story. I mistakenly thought I’d found my problem in
a statistics-gathering type with several mutexed fields. So, cackling gleefully, I turned them into
[Erlang-flavored accumulators](https://github.com/timbray/quamina/blob/main/pruner_stats.go)
updated with Go channel messages, a programming idiom that’s always given me a warm glow.

It didn’t make any performance difference but the code was smaller and prettier.

Unit tests are good except when they’re not ·
When I got over my grumpiness and went back to the problem, I started by looking at the unit test. Oops. Turns out the
read-only thread was (unsurprisingly) running twenty times as fast as the update thread and since they were doing the same
number of operations, it finished up instantly and the updater-thread kept thundering away. For reasons that need not concern
us, a stream of heavy add and delete operations without any stats-gathering read operations leads to massive, horribly complex
NFAs. Then the matching runs slow — exactly what the profiler had been trying to tell
me, only I thought I was smart enough to know better.

So I forced the reader thread to keep running until the other finished and hey-presto, the race was still fixed and
everything ran at typical Quamina speeds, which is to say very fast.

(I didn’t get rid of the Erlangified stats package though, I just liked it too much.)

I’m normally tolerant of a certain amount of sloppy informal power-coding while constructing unit
tests — more are better! — and I think I still am. But this was a
painful experience that I’d like to avoid in future. So, is there a lesson here? Maybe there are two: First, believe what the
profiler is telling you! Second, if you’re having trouble understanding unit test output, dig around a
bit and make sure it’s doing what you think it is.

Grey-haired programmer ·
Even when I’m mad at my software, I’m grateful that I still enjoy working on it. I think it supports my main post-employment
objective, which is to keep my brain working. And who knows, the software might help somebody somewhere.

And best of all, when nobody’s
paying you to work on something, you can take a few weeks off whenever you’re not in the mood.

---

**Updated: 2026/09/01**

[ongoing](https://www.tbray.org/ongoing/)

[What this is](/ongoing/WhatItIs) ·
[![Subscribe to ongoing](/ongoing/Feed.png "Subscribe to ongoing")](/ongoing/ongoing.atom)
[Truth](/ongoing/Truth) ·
[Biz](/ongoing/Biz) ·
[Tech](/ongoing/Tech)

[author](/ongoing/misc/Tim) ·
[Dad](http://www.textuality.com/BillBray/)
[colophon](/ongoing/misc/Colophon) ·
[rights](/ongoing/misc/Copyright)

[![picture of the day](/ongoing/potd.png)](/ongoing/goto-potd/)

[September](/ongoing/When/202x/2026/09/) [01](/ongoing/When/202x/2026/09/01/), [2026](/ongoing/When/202x/2026/)
 · [Technology](/ongoing/What/Technology) (90 fragments)

 · · [AI](/ongoing/What/Technology/AI) (18 more)

 · · [Quamina Diary](/ongoing/What/Technology/Quamina%20Diary) (26 more)

By [Tim Bray](/ongoing/misc/Tim).

The opinions expressed here
are my own, and no other party
necessarily agrees with them.

A full disclosure of my
professional interests is
on the [author](/ongoing/misc/Tim) page.

I’m on [Mastodon](https://cosocial.ca/%40timbray)!