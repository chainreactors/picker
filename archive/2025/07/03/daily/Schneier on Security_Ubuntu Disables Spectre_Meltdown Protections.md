---
title: Ubuntu Disables Spectre/Meltdown Protections
url: https://www.schneier.com/blog/archives/2025/07/ubuntu-disables-spectre-meltdown-protections.html
source: Schneier on Security
date: 2025-07-03
fetch_date: 2025-10-06T23:56:39.347671
---

# Ubuntu Disables Spectre/Meltdown Protections

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

## Ubuntu Disables Spectre/Meltdown Protections

A whole class of speculative execution attacks against CPUs [were published](https://www.schneier.com/blog/archives/2018/01/spectre_and_mel_1.html) in 2018. They seemed pretty catastrophic at the time. But the fixes were as well. Speculative execution was a way to speed up CPUs, and removing those enhancements resulted in significant performance drops.

Now, people are rethinking the trade-off. Ubuntu [has disabled](https://bugs.launchpad.net/ubuntu/%2Bsource/intel-compute-runtime/%2Bbug/2110131) some protections, resulting in 20% performance boost.

> After discussion between Intel and Canonical’s security teams, we are in agreement that Spectre no longer needs to be mitigated for the GPU at the Compute Runtime level. At this point, Spectre has been mitigated in the kernel, and a clear warning from the Compute Runtime build serves as a notification for those running modified kernels without those patches. For these reasons, we feel that Spectre mitigations in Compute Runtime no longer offer enough security impact to justify the current performance tradeoff.

I agree with this trade-off. These attacks are hard to get working, and it’s not easy to exfiltrate useful data. There are way easier ways to attack systems.

News [article](https://arstechnica.com/security/2025/06/ubuntu-disables-intel-gpu-security-mitigations-promises-20-performance-boost/).

Tags: [cyberattack](https://www.schneier.com/tag/cyberattack/), [malware](https://www.schneier.com/tag/malware/), [operating systems](https://www.schneier.com/tag/operating-systems/)

[Posted on July 2, 2025 at 7:02 AM](https://www.schneier.com/blog/archives/2025/07/ubuntu-disables-spectre-meltdown-protections.html) •
[22 Comments](https://www.schneier.com/blog/archives/2025/07/ubuntu-disables-spectre-meltdown-protections.html#comments)

### Comments

PG •
[July 2, 2025 7:09 AM](https://www.schneier.com/blog/archives/2025/07/ubuntu-disables-spectre-meltdown-protections.html/#comment-446275)

How much do you think that these mitigations affected Intel’s economic problems and how much their disabling is due to them?

Clive Robinson •
[July 2, 2025 7:47 AM](https://www.schneier.com/blog/archives/2025/07/ubuntu-disables-spectre-meltdown-protections.html/#comment-446277)

@ ALL,

With regards,

> “These attacks are hard to get working, and it’s not easy to exfiltrate useful data. There are way easier ways to attack systems.”

Is hanging on an unproven assumption that is probably not true.

That is the assumption is that all these types of attack are now known about and characterised, thus a value judgment can be made.

This was Intel’s “default position” from the begining.

However I warned that the problem would be

“The Xmas Gift that kept giving”

And to expect further similar failings for a half decade or more.

And so it turned out to be… the case is many more such errors have been found and I’ve no reason to believe we’ve stopped finding them.

So that leaves two questions about future “black swans”,

1, Will they be hard to get working?

The answer to both of those is a “probabilistic unknown”. That is the assumption is that,

“The low hang fruit has already been plucked…”

It’s a dangerous assumption to make in certain circumstances.

Which gives rise to a third question,

3, Is there a working mitigation that is easy to implement?

To which the answer is,

“Yes by segregation”

The problem that arises is,

4, Are there system configurations where “mitigation by segregation” is not an option?

The answer unfortunately is “yes”.

But the the question is,

5, Why?

And the answer is a pigs ear type MBA Mantra of,

“Any and all communications is good”.

Which is patently untrue and mostly an infantile excuse to,

“Leave all the doors and windows open for criminals to wander through.”

The real issue is “not leaving money on the table” arguments. That we don’t know what is going to be big next…

Well the simple answer to that is,

“Security vulnerabilities that will cost.”

The only question as with “ransomware” is really,

“Who gets hit first before and after the issues is patched?”

The fact is there are other mitigations other than hard segregation… But even those that are relatively inexpensive mostly don’t get implemented for fiscal reasons.

So saying,,

“I agree with this trade-off”

Is kind of accepting that,

“Incompetent management is king”…

But is it? Because in the US that is in effect the legal position due to “maximise shareholder value” determinations in court effectively pushing the “Short term value” viewpoint…

Other places and entities have different view-points and the cost of mitigating a 10-30% loss in performance is very small compared to dealing with a ransomware or similar attack and clean up especially if NatSec is involved.

Anonymous •
[July 2, 2025 9:16 AM](https://www.schneier.com/blog/archives/2025/07/ubuntu-disables-spectre-meltdown-protections.html/#comment-446278)

“…there is the possibility that this would open up an unknown avenue for attack…without any known exploits…could open up some other bug that was covered up by the mitigations…we have some confidence…we could have unknown behavioral differences…”

That’s a lot of unknowns.
They call this security?

[Mexaly](http://xkcd.com/722) •
[July 2, 2025 9:38 AM](https://www.schneier.com/blog/archives/2025/07/ubuntu-disables-spectre-meltdown-protections.html/#comment-446279)

I think someone said,
“Attacks that are hard only become easier,”
or words to that effect.

Mr. Peed Off •
[July 2, 2025 9:59 AM](https://www.schneier.com/blog/archives/2025/07/ubuntu-disables-spectre-meltdown-protections.html/#comment-446280)

The spectre/meltdown protections have long been cursed by gamers and other computer performance enthusiasts. Most users are unlikely to be targeted by such an attack. Certainly those who are likely to be targeted should take all precautions.

Clive Robinson •
[July 2, 2025 11:00 AM](https://www.schneier.com/blog/archives/2025/07/ubuntu-disables-spectre-meltdown-protections.html/#comment-446284)

@ Mr Peed Off, ALL,

With regards,

> “The spectre/meltdown protections have long been cursed by gamers and other computer performance enthusiasts”

Have you read the bottom of the ARS Article by Dan Goodin where in the penultimate paragraph he says,

> *“One thing Ubuntu users should know is that the change will only provide performance boosts when GPUs are handling workloads running the OpenCL framework or the OneAPI Level Zero interface. **That likely means that people using games and similar apps will see no benefit**.”*

Grima Squeakersen •
[July 2, 2025 3:47 PM](https://www.schneier.com/blog/archives/2025/07/ubuntu-disables-spectre-meltdown-protections.html/#comment-446286)

Are cyber-currency mining systems vulnerable to the Spectre/Meltdown (or similar) attacks, and to performance hits from the mitigation...