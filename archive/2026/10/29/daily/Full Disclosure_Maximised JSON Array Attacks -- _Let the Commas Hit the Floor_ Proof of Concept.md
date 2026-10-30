---
title: Maximised JSON Array Attacks -- "Let the Commas Hit the Floor" Proof of Concept
url: https://seclists.org/fulldisclosure/2026/Oct/50
source: Full Disclosure
date: 2026-10-29
fetch_date: 2026-10-30T07:56:41.237032
---

# Maximised JSON Array Attacks -- "Let the Commas Hit the Floor" Proof of Concept

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](49)
[By Date](date.html#50)
[![Next](/images/right-icon-16x16.png)](51)

[![Previous](/images/left-icon-16x16.png)](49)
[By Thread](index.html#50)
[![Next](/images/right-icon-16x16.png)](52)

![](/shared/images/nst-icons.svg#search)

# Maximised JSON Array Attacks -- "Let the Commas Hit the Floor" Proof of Concept

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 28 Oct 2026 05:30:20 +0000

---

```
On 29 August 2026, we released "Commas of D00m" -- an old proof of concept that demonstrates unconstrained resource
consumption in many JSON parsers.  As recently discussed (in "Continued Apache Struts2 JSON Plugin Insecure
Deserialisation"), the Apache Struts2 JSON Plugin's S2-072 and prior code changes fail to sufficiently protect against
this style of attack.  In that write-up, we examined the code and the underlying, incomplete fixes, as well as marched
through a series of basic mathematical analyses that illustrated the point - showing how a single <2MB JSON string can
consume more than 10 times that in RAM and how, when run with rather modest concurrency, such a request can consume
more than a GB of RAM.

As discussed in that write-up, for the sake of simplicity, an array-of-arrays of only 2 levels deep was chosen for the
discussion, with several payload options discussed (and the desired end goal -- consumption of excessive CPU for a
little less memory, shorter payloads, or more extreme memory consumption).  The following is the more "memory-hungry",
more complex approach that better maximises the 2MB character length limit that the Apache Struts2 JSON Plugin applies
(realistically, using an array-of-arrays of just 2 levels deep, the string can be under 1MB and consume over 40MB of
RAM on a single query -- some queries can even get over 80GB per-request, but we'll save that as an exercise for the
reader).

The Approach
A JSON nested JSON array with the following dimensions:

  *   Level 0 (root): an array with exactly 2 children
  *   Level 1: each of the children from the above array contains an array with exactly 8,256 children (a total of
16,512 elements, at the moment)
  *   Levels 2-63: each of those 16,512 elements is a chain of 62 nested single-child arrays (`[[[[...]]]]`), with each
level holding exactly one element
  *   Leaf: each chain terminates in an empty String `""`
Total: 16,512 chains, each exactly 62 singleton-array levels deep, fed by a 2 * 8256 fan-out at the top

Analysis
A single array can hold at most 10,000 direct children (`maxElements`), so an array-of-arrays with no other content
will use 1,290,001 characters (of the 2,097,152 maximum) and consume roughly 48.6MB, leaving 807,151 characters unused
simply because the depth and breadth limiters.  This means that, without having any "content" other than arrays, we can
consume almost 50MB on a single request, which is pretty good considering we are only using ~1.3 million of the ~2
million character budget.  A massive array-of-arrays with no actual data, though, is fairly noisy and, frankly, 50MB is
small peanuts compared to what we can get with just a little bit of data.

Before we go further, we need to discuss something that was mentioned in the last write-up but that needs a little more
explanation.  Java's default ArrayList capacity (which is the maximum number of elements that it can house and
shouldn't be conflated with "size") is 10.  Most developers don't change this value and neither does the Apache Struts2
JSON Plugin.  The cost of this, however, is not incurred, to its fullest, until the first `add(Object)` call is made --
once that happens, the backing array is allocated, costing 56 bytes (double that if not using the compressed oops, as
discussed in the previous write-up).  After the first `add(Object)` call is made, the total cost of the ArrayList is 80
bytes (for simplicity's sake, we're going to stick with the compressed oops and lowest possible values throughout the
rest of this work -- this value can be more depending on the environment) regardless of if the array has 1 or 10
elements in it (we'll ignore the automatic resizing in making that statement, just for the sake of argument).  This
means that for the cost of simply two characters -- `[` and `]`, which is just two bytes in our input, we cost the
server 80 bytes (which is 40 bytes/input character -- a massive win for the attacker).  The next best that we can do is
an empty String, which has a 20 bytes/input character pay-off, which is significantly worse.  Adding elements to the
array costs us at least one character -- `,` -- but we only see the ArrayList grow at key intervals, so it actually has
a slightly worse bytes/input character pay-off overall.

Looking at the problem, we have ample room sideways -- 10,000 units left and right per element -- but are constrained
along the y-axis by the 64-depth limit.  As width doesn't immediately equal a significant number of bytes consumed
since the cost is stepped, it's best to go n-1 deep and then fill out the leaves, which means that we get maximum usage
-- 82,785,552 bytes of RAM consumed on a single request (assume 64-bit HotSpot JVM running with compressed oops and
8-byte alignment -- a standard configuration set) -- in the manner described in the above "The Approach" section.

In other words, by fanning out into empty Strings and using 40 concurrent requests, we can consume ~3.31GB of RAM on
the host and maximise the 2MB input limit that Apache has put in place.

The Maths

  *   ArrayList: ~24B + backing Object array of capacity n
     *   Backing array: 16B + 4nB (rounded to 8 bytes by the JVM)
     *   On first `add(Object)` call, the backing array goes to 56B
     *   If hit rapidly and concurrently, garbage collection will not run (we'll take the worst case scenario, here,
for simplicity), so growing an array to 10,000 elements (14,053 capacity) costs 168,944 bytes in backing arrays
  *   One singleton-chain level: 80B / 2 input characters = 40 bytes/input character
  *   One chain (62 levels + leaf): (62B * 80B) + 40B = 5,000B for (62 * 2) + 2 characters -- 126 characters (39.68
bytes/input character)\
  *   16,512 chains: 82,560,000B
     *   two 8,256-wide level-2 arrays: 2 * 112,736 = 225,472B
     *   2-wide root: 80B
Add it all up and you get 82,785,552B on a single request.  Multiply that by 40 (40 concurrent requests) and you have
~3.31GB residing in memory at any given time.  Stepped attacks, especially if paired with high-compute requests (again,
boxing and unboxing requests are a great option), can dramatically increase that while allowing the attacker to
decrease the number of requests/second.  Note that we leave such a trivial tweak to the PoC to the reader.

The Script
The following is a modernised version of Commas of D00m known as "Let the Commas Hit the Floor".

```python
#!/usr/bin/python3
# ---
# name: Nested-array depth overflow tester
# category: Testing and scanning
# tags: dos, payload, nested-array, recursion-depth, stack-overflow, json, flood, load, http
# description: Floods a host with concurrent deeply nested JSON arrays (2 root children x 8,256 nested children,
#   each a 62-level chain of single-element arrays terminating in an empty string) to probe JSON parser
#   recursion/stack-depth limits.
# placeholders:
#   - token: "@@HOSTS@@"
#     field: hosts
#     kind: list
#     format: python
#     label: Hosts
#   - token: "@@CONTENT_TYPE@@"
#     field...