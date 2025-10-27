---
title: New Linux Rootkit
url: https://www.schneier.com/blog/archives/2025/04/new-linux-rootkit.html
source: Schneier on Security
date: 2025-04-25
fetch_date: 2025-10-06T22:07:13.700236
---

# New Linux Rootkit

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

## New Linux Rootkit

[Interesting](https://betanews.com/2025/04/24/hackers-bypass-linux-security-with-armo-curing-rootkit/):

> The company has released a working rootkit called “Curing” that uses io\_uring, a feature built into the Linux kernel, to stealthily perform malicious activities without being caught by many of the detection solutions currently on the market.
>
> At the heart of the issue is the heavy reliance on monitoring system calls, which has become the go-to method for many cybersecurity vendors. The problem? Attackers can completely sidestep these monitored calls by leaning on io\_uring instead. This clever method could let bad actors quietly make network connections or tamper with files without triggering the usual alarms.

[Here’s](https://github.com/armosec/curing) the code.

Note the self-serving nature of this announcement: ARMO, the company that released the research and code, has a product that it claims blocks this kind of attack.

Tags: [Linux](https://www.schneier.com/tag/linux/), [rootkits](https://www.schneier.com/tag/rootkits/)

[Posted on April 24, 2025 at 3:35 PM](https://www.schneier.com/blog/archives/2025/04/new-linux-rootkit.html) •
[8 Comments](https://www.schneier.com/blog/archives/2025/04/new-linux-rootkit.html#comments)

### Comments

Peter •
[April 24, 2025 5:21 PM](https://www.schneier.com/blog/archives/2025/04/new-linux-rootkit.html/#comment-444802)

One simple “fix” is to [disable io\_uring](https://lwn.net/Articles/937013/). In most cases the performance impact will be acceptable.

Auditing and security may have been [a bit of an afterthought](https://lwn.net/Articles/858023/).

[Julia Clement](https://juliaclement.com/) •
[April 24, 2025 7:07 PM](https://www.schneier.com/blog/archives/2025/04/new-linux-rootkit.html/#comment-444804)

This was just waiting to happen, if it hasn’t already happened earlier. In June 2023, Google reported on its [Security blog](https://security.googleblog.com/2023/06/learnings-from-kctf-vrps-42-linux.html):

> in the past year, there has been a clear trend: 60% of the submissions exploited the io\_uring component of the Linux kernel[…]. Furthermore, io\_uring vulnerabilities were used in all the submissions which bypassed our mitigations.
>
> * ChromeOS: We disabled io\_uring (while we explore new ways to sandbox it).
> * Android: Our seccomp-bpf filter ensures that io\_uring is unreachable to apps. Future Android releases will use SELinux to limit io\_uring access to a select few system processes.
> * GKE AutoPilot: We are investigating disabling io\_uring by default.
> * It is disabled on production Google servers.

I’m sure that there are a small number of use cases where io\_uring gives a major benefit, but having it enabled by default on all Linux system seems dangerous to me.

lurker •
[April 25, 2025 12:03 AM](https://www.schneier.com/blog/archives/2025/04/new-linux-rootkit.html/#comment-444805)

LWN waved a big red flag four years ago [1], so the only surprise here is that the rootkit is issued in public this much later, and apparently still works.

“there is nobody with a checklist making sure that all of the relevant boxes have been marked before a new subsystem can be merged.”

[1] <https://lwn.net/Articles/858023/>

Clive Robinson •
[April 25, 2025 6:37 AM](https://www.schneier.com/blog/archives/2025/04/new-linux-rootkit.html/#comment-444806)

@ Julia Clement, ALL,

With regards,

> “… having it enabled by default on all Linux system seems dangerous to me.”

This is true of all “off device I/O” even the humble serial port (now mostly done by USB). As well as a number of other “on device processes” to do with inter process communications.

In fact just about any function that serialises data is a potential security vulnerability via a side channel, when you dig into it.

So the question is

“What benefit” do such functions have?”

Well anyone who has “bit banged” serial data asynchronous or not out of a microprocessor can tell you “Comms is a lot of work” thus any library or pre-written function “lifts the yoke”.

However standard “Asynchronous IO”(AIO) interfaces on most operating systems that have their roots older than a decade or so have a “traditional” view as to AIO which is “slow and burdensome” and don’t really work well with modern hardware capabilities. As has been observed

“Everything through the kernel twice then block…”

Anyone who has tried writing a terminal program that looks even remotely interactive knows that,

“The POSIX Way is the WRONG way!”

And the same is true for anything that “blocks”.

Yes there are “poll” based functions using “signals” but you really won’t find many who will be happy to do it.

But fundamentally traditional AIO works on the blocking “completion model” rather than a “readiness model”.

Further it uses “circular buffers” that don’t need “signalling flags” as with a little bit of thought the signalling becomes implicit in the read or write functions via the pointer use.

But further… even with well written code most programmers that do various serialisation functions be it bit, byte, or block generally do not realise what awful vulnerabilities they open up in the process.

As a rule of thumb traditional AIO is written in a “conservative” fashion on the assumption programmers “will break the system if allowed to”… Which is all to often true.

They way around much of this for high IO code like web servers has been to move the IO from kernal space to user space as much as possible to get the fineness of control. But you can all to easily end up with deadlocks and resource hog issues, that appear to happen at the worst of times.

The theory is io\_uring gets around most of these issues and at the same time cuts down a lot of load from the system.

For those that want to get more into the reasoning,

<https://blogs.oracle.com/linux/post/an-introduction-to-the-io-uring-asynchronous-io-framework>

The reason io\_uring is seen as “less secure” is not that it is (all comms IO is by definition insecure)… But because it’s “not being watched” the same way as other kernel based IO.

That is the fault not of io\_uring or it’s designers and developers, but the fault of the “security monitor” software being “blind in one eye” thus “Doing a Nelson” of “I see no ships”.

Clive Robinson •
[April 25, 2025 7:46 AM](https://www.schneier.com/blog/archives/2025/04/new-linux-rootkit.html/#comment-444807)

@ ALL,

Due to not immediately being able to find it…

<https://m.youtube.com/watch?v=AaaH6skUEI8>

Which is why I also left Something out of my above… which is the old “you can have any two of three” comment that applies to io\_uring,

“Of speed, ease of use, and oversight, you can have any two…”

Why do I say “oversight” well it’s what allows you to do realtime “audit” like logging of resource usage. Audit in turn allows you to do realtime “control” such as for flow. But logging and con...