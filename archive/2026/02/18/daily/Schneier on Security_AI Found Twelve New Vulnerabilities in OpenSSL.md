---
title: AI Found Twelve New Vulnerabilities in OpenSSL
url: https://www.schneier.com/blog/archives/2026/02/ai-found-twelve-new-vulnerabilities-in-openssl.html
source: Schneier on Security
date: 2026-02-18
fetch_date: 2026-02-19T04:22:02.306861
---

# AI Found Twelve New Vulnerabilities in OpenSSL

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

## AI Found Twelve New Vulnerabilities in OpenSSL

The title of the post is”[What AI Security Research Looks Like When It Works](https://aisle.com/blog/what-ai-security-research-looks-like-when-it-works),” and I agree:

> In the latest [OpenSSL security release>](https://openssl-library.org/news/vulnerabilities/) on January 27, 2026, twelve new zero-day vulnerabilities (meaning unknown to the maintainers at time of disclosure) were announced. Our AI system is responsible for the original discovery of all twelve, each found and responsibly disclosed to the OpenSSL team during the fall and winter of 2025. Of those, 10 were assigned CVE-2025 identifiers and 2 received CVE-2026 identifiers. Adding the 10 to the three we already found in the [Fall 2025 release](https://aisle.com/blog/aisle-discovers-three-of-the-four-openssl-vulnerabilities-of-2025), AISLE is credited for surfacing 13 of 14 OpenSSL CVEs assigned in 2025, and 15 total across both releases. This is a historically unusual concentration for any single research team, let alone an AI-driven one.
>
> These weren’t trivial findings either. They included [CVE-2025-15467](https://aisle.com/blog/openssl-stack-overflow-cve-2025-15467-deep-dive), a stack buffer overflow in CMS message parsing that’s potentially remotely exploitable without valid key material, and exploits for which have been quickly developed online. OpenSSL rated it HIGH severity; [NIST](https://nvd.nist.gov/vuln/detail/CVE-2025-15467)‘s CVSS v3 score is 9.8 out of 10 (CRITICAL, an extremely rare severity rating for such projects). Three of the bugs had been present since 1998-2000, for over a quarter century having been missed by intense machine and human effort alike. One predated OpenSSL itself, inherited from Eric Young’s original SSLeay implementation in the 1990s. All of this in a codebase that has been fuzzed for millions of CPU-hours and audited extensively for over two decades by teams including Google’s.
>
> In five of the twelve cases, our AI system directly proposed the patches that were accepted into the official release.

AI vulnerability finding is changing cybersecurity, faster than expected. This capability will be used by both offense and defense.

[More](https://www.lesswrong.com/posts/7aJwgbMEiKq5egQbd/ai-found-12-of-12-openssl-zero-days-while-curl-cancelled-its).

Tags: [AI](https://www.schneier.com/tag/ai/), [patching](https://www.schneier.com/tag/patching/), [SSL](https://www.schneier.com/tag/ssl/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/), [zero-day](https://www.schneier.com/tag/zero-day/)

[Posted on February 18, 2026 at 7:03 AM](https://www.schneier.com/blog/archives/2026/02/ai-found-twelve-new-vulnerabilities-in-openssl.html) •
[10 Comments](https://www.schneier.com/blog/archives/2026/02/ai-found-twelve-new-vulnerabilities-in-openssl.html#comments)

### Comments

TimH •
[February 18, 2026 7:47 AM](https://www.schneier.com/blog/archives/2026/02/ai-found-twelve-new-vulnerabilities-in-openssl.html/#comment-452214)

Looks to me like the AI system is checking exhaustively for known needles (flaws) in the haystack, whereas fuzzing is searching the haystack for needles, which is far less efficient.

Clive Robinson •
[February 18, 2026 8:52 AM](https://www.schneier.com/blog/archives/2026/02/ai-found-twelve-new-vulnerabilities-in-openssl.html/#comment-452216)

@ TimH,

With regards,

> “Looks to me like the AI system is checking exhaustively for known needles (flaws) in the haystack”

Think a little further “known” has an implication that,

1, As known, should not have gone in the haystack.

Which means that you are looking for “unknown” and as there are oh so many of those… So,

> “fuzzing is searching the haystack for needles, which is far less efficient”

Is in fact on average “the most efficient” way of finding new thus unknown flaws or vulnerabilities.

Clive Robinson •
[February 18, 2026 10:08 AM](https://www.schneier.com/blog/archives/2026/02/ai-found-twelve-new-vulnerabilities-in-openssl.html/#comment-452217)

@ ALL,

I’ve explained some of the issues to do with finding vulnerabilities as either an attacker or defender, and the maths favours attackers not defenders.

Because attackers can spend their resources on “focused narrow in depth” searches, whilst defenders have to spend their often lesser resorces on “unfocused wide in broad” searches.

There are many ways you can optomize searches from the mechanical search for “all instances” to the random “all areas” of fuzzing. In effect each being one end of the curve.

Thus modified techniques will out perform both.

A branch of thermodynamics called statistical mechanics is something that can tell us about what is an improved or more optimal search method.

Thus the aim is to take “Known Instances of attack and form them into classes of attacks by abstracting out basic vulnerability features.

This changes a purely “random search” from basic fuzzing to something more directed. So the “drunkards walk” becomes in effective “directed” to enlarge the class in a spiral outward about a known class.

Think of it as a drunkard on a slope, ease of walking makes a general walk too much work so the drunkard tends to head down hill.

This is what some call a “directed drunkards walk” as such Brownian motion under the influence of the force of gravity creates a density profile that in effect causers fast moving particles to rise whilst the slow moving fall towards the point of highest gravitational attraction.

However this is a general trend based on statistical properties, not one that is specific to any one type of attack.

Moving the trend to accommodate other type of instances is thus generally more efficient than pure random “fuzzing”.

But pure random fuzzing will find new instances that are in a class of just one member (it’s self). So creates new classes rather than new instances which some would view as more beneficial.

Dave •
[February 18, 2026 11:34 AM](https://www.schneier.com/blog/archives/2026/02/ai-found-twelve-new-vulnerabilities-in-openssl.html/#comment-452218)

<https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf>

Bruce is undoubtedly correct but all it does is compound the trust issue highlighted in the classic paper linked above.

Everything we have learned though the years is defenders are always playing catch up. So then the only winning move is not to play.

Clive Robinson •
[February 18, 2026 12:34 PM](https://www.schneier.com/blog/archives/2026/02/ai-found-twelve-new-vulnerabilities-in-openssl.html/#comment-452219)

@ Dave, Bruce, ALL,

Today the Register has an article on the use of AI for Computer Security that some readers would consider an exercise in doing a “face palm” by LLM users,

> **Your AI-generated password isn’t random, it just looks that way**
>
> Seemingly complex strings are actually highly predictable, cracka...