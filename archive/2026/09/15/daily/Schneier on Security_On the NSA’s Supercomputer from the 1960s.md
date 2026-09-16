---
title: On the NSA’s Supercomputer from the 1960s
url: https://www.schneier.com/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html
source: Schneier on Security
date: 2026-09-15
fetch_date: 2026-09-16T07:06:39.628529
---

# On the NSA’s Supercomputer from the 1960s

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

## On the NSA’s Supercomputer from the 1960s

Really interesting [story](https://spectrum.ieee.org/cold-war-codebreaker-nsa-ibm) about Harvest, a specialized code breaking computer built in the 1960s by IBM for the NSA.

Tags: [history of computing](https://www.schneier.com/tag/history-of-computing/), [history of cryptography](https://www.schneier.com/tag/history-of-cryptography/), [IBM](https://www.schneier.com/tag/ibm/), [intelligence](https://www.schneier.com/tag/intelligence/), [NSA](https://www.schneier.com/tag/nsa/)

[Posted on September 15, 2026 at 6:16 AM](https://www.schneier.com/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html) •
[7 Comments](https://www.schneier.com/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html#comments)

### Comments

Clive Robinson •
[September 15, 2026 10:59 AM](https://www.schneier.com/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html/#comment-457976)

@ Bruce, ALL,

The IEEE article says,

> *“The Cray-1 was built from faster, more tightly integrated circuits that could outperform Harvest’s aging transistors at nearly any task, including text processing.”*

Whilst true to a certain extent, not just misses a point, but gets it wrong with,

> *“Harvest didn’t found a dynasty. But, in its time, it steadfastly pointed toward the future—in several directions at once.”*

Little known was that many of the “Oh so Secret” ideas in Harvest actually ended up as secret “optional extras” in Cray hardware for years to come.

And some of the Harvest and Cray additions made it into Intel Chips and still are with us today.

One thing that did not make it through the ages in general computing was “Content Addressable Memory”(CAM) that was in some ways very useful for crypto and some types of high speed “lookup Table” work.

Invented by Dr Dudley Allen Buck who worked at one time for the NSA, CAM can still be found in very high end Network Devices.

Perry Fellwock •
[September 15, 2026 11:01 AM](https://www.schneier.com/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html/#comment-457977)

When artificial general intelligence has been achieved, we will likely not know it. The government and defense contractors, also known as Big Tech, will keep it secret.

fred.bloggs •
[September 15, 2026 12:12 PM](https://www.schneier.com/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html/#comment-457982)

A note re: Content Addressable Memory:

General-purpose caching (level 1, level 2 etc.) uses CAM.

Caching also appears, in multiple ways, in the architecture of the Internet.

Memoization (using hashes to summarise content, e.g. HashLife) is another step.

Note also that Deep Blue computer chess player also used custom silicon (my poor memory seems to recall that the most profitable application of hardware was in move generation). Hashes were used to find identical positions that occurred after different sequences of moves (e.g. transpose some moves).

[ASICs, including RISC CPUs, may be another area.]

* fred.bloggs

Simon W •
[September 15, 2026 12:14 PM](https://www.schneier.com/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html/#comment-457983)

CAM was used as the cache index in early ARM processors, giving a very high associativity. It was dropped for a more conventional (lower associativity) design in the ARM7 family.

cls •
[September 15, 2026 6:34 PM](https://www.schneier.com/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html/#comment-457997)

@Clive

> CAM can still be found in very high end Network Devices.

That’s wrong. CAM is ubiquitous in layer 2 Ethernet switches. It’s how they work! No matter what the cost

If you’re thinking of longest bit string matching, for example IP routing FIB, that can be implemented by ternary CAM for wire speed routing.

cls •
[September 15, 2026 6:34 PM](https://www.schneier.com/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html/#comment-457998)

@Clive

> CAM can still be found in very high end Network Devices.

That’s wrong. CAM is ubiquitous in layer 2 Ethernet switches. It’s how they work! No matter what the cost

If you’re thinking of longest bit string matching, for example IP routing FIB, that can be implemented by ternary CAM for wire speed routing.

Clive Robinson •
[September 15, 2026 8:04 PM](https://www.schneier.com/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html/#comment-458007)

@ cls,

With regards,

> “That’s wrong. CAM is ubiquitous in layer 2 Ethernet switches.”

Two things,

Firstly what you say does not make my statement any the less true if you pause and think for a moment.

Secondly I did not want to get down into the weeds of switches and routers, type 1 or “Binary CAM”, type 2 or “Ternary CAM”(TCAM) and the “Lulea trie” algorithm that uses a tree structure in RAM to avoid using either type of CAM hardware, thus ordinary PC hardware and similar can be utilised.

What is called Binary CAM is what tends to be used in switches, TCAM is often needed in routers.

For various reasons what was favoured for cryptanalysis work was TCAM (I’ve been told the reasons are still regarded as classified in the US but not in many other places).

You can see traces of this in what Seymour Cray designed into his computers.

One of the “not for ordinary use instructions” on the Cray was a type of “find parity” instruction that would provide the count of set bits in a word of defined size. Something that used to involve a “shift, test, increment” loop that grew with word bit length on ordinary CPUs. It’s descendant is actually quite useful in Data Comms and is used in Error Correction and similar codes.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/09/on-the-nsas-supercomputer-from-the-1960s.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F09%2Fon-the-nsas-supercomputer-from-the-1960s.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required):

Comments:
![](https://www.schneier.com/wp-content/themes/schneier/assets/images/loader.gif)

**Allowed HTML**
<a href="URL"> • <em> <cite> <i> • <strong> <b> • <sub> <sup> • <ul> <ol> <li> • <blockquote> <pre>
**Markdown Extra** syntax via <https://michelf.ca/projects/php-markdown/extra/>

[ ]  Notify me of new posts by email.

Δ

[← Upcoming Speaking Engagements](https://www.schneier.com/blog/archives/2026/09/upcoming-speaking-engageme...