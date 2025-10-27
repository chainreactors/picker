---
title: Security Product Efficacy
url: https://textslashplain.com/2025/08/20/security-product-efficacy/
source: text/plain
date: 2025-08-21
fetch_date: 2025-10-07T00:48:16.015751
---

# Security Product Efficacy

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Security Product Efficacy

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-08-202025-08-21](https://textslashplain.com/2025/08/20/security-product-efficacy/)Posted in[security](https://textslashplain.com/category/security/)Tags:[Defender](https://textslashplain.com/tag/defender/), [security](https://textslashplain.com/tag/security/)

I’ve written about security products [previously](https://textslashplain.com/2024/11/18/security-software-an-overview/#:~:text=Framing%3A%20Protection%20Levers%C2%A0), laying out the framing that security products combine sensors and throttles with threat intelligence to provide protection against threats.

[![](https://textslashplain.com/wp-content/uploads/2025/08/image-1.png?w=596)](https://textslashplain.com/wp-content/uploads/2025/08/image-1.png)

As a product engineer, I spend most of my time thinking about how to improve sensors and throttles to enhance protection, but those components only provide value if the threat intelligence can effectively recognize data from the sensors and tell the throttles to block dangerous actions.

A common goal for the threat intelligence team is to measure the quality of their intel because understanding the current quality is critical to improving it.

[![](https://textslashplain.com/wp-content/uploads/2025/08/image-2.png?w=458)](https://textslashplain.com/wp-content/uploads/2025/08/image-2.png)

*Efficacy* is the measure of the **false negatives** (how many threats were missed) and **false positives** (how many innocuous files or behaviors were incorrectly blocked). Any security product can *trivially* have a 0% false negative rate (by blocking everything) or a 0% false positive rate (by blocking nothing). The challenge of the threat intelligence is in minimizing both false negatives and false positives.

Unfortunately, if you think about it for a moment the big problem in measuring efficacy leaps to mind: **It’s kinda impossible**.

Why?

Think about it: It’s like having a kid take a math test, and then asking that kid to immediately go back and grade his own test without first giving him an answer key or teaching him more math. When he wrote down his answers, he did his best to provide the answer he thought was correct. If you immediately ask him again, nothing has changed — he doesn’t have any more information than he had before, so he still thinks all of his answers are correct.

And the true situation is actually *much more difficult* than that analogy — arithmetic problems don’t try to hide their answers ([cloaking](https://textslashplain.com/tag/cloaking/)), and their answers stay constant over time, whereas many kinds of threat are only “active” for brief slices of time (e.g. a compromised domain serving a phishing attack [until it’s cleaned up](https://textslashplain.com/2023/10/13/beware-urls-are-pointers-to-mutable-entities/)).

There’s no such thing as an answer key for threat recognition, so what are we to do? Well, there are some obvious approaches for grading TI for false negatives:

1. **Wisdom of the Crowd** – Evaluate the entity through all available TI products (e.g. on [VirusTotal](https://www.virustotal.com/gui/file/7b878674d73009594b7eaec3e3f07dc98b4a1f13e9fde20a57bc8c974b76710f/detection)) and use that to benchmark against the community consensus.
2. **Look back later** – Oftentimes threats are not detected immediately, but become are discovered later after broader exposure in the ecosystem. If we keep copies of the evaluated artifacts and evaluate them days or weeks later, we may get a better understanding of false negatives.
3. **Sampling** – Laboriously evaluating a small sample of specimens by an expert human grader who, for example, detonates the file, disassembles the code and audits every line to come up with an accurate verdict.
4. **Corpus Analysis** – Feed a collection of known-bad files into the engine and see how many it detects.

Each of these strategies is inherently imperfect:

* the “Wisdom of the Crowd” only works for threats known to your competitors
* “look back later” only works when the threat was ever recognized by anyone and remains active
* sampling is extremely expensive, and fails when a threat is inactive (e.g. a command-and-control channel no longer exists)
* Corpus analysis only evaluates “known bad” files and often contains files that have been rendered harmless by the passage of time (e.g. attempting to exploit vulnerabilities in software that was patched decades ago).

Even after you pick a strategy, or combination of strategies for grading, you’re still not done. Are you counting false positives/negatives by **unique artifacts** (e.g. the number of files that are incorrectly blocked or allowed), or by **individual encounters** (the number of times an incorrect outcome occurs)?

Incorrectly blocking a thousand unique files once each isn’t usually as impactful to the ecosystem as blocking a single file incorrectly a million times.

This matters because of the **[base rate](https://en.wikipedia.org/wiki/Base_rate)**: the vast majority of files (and behaviors) are non-malicious, while malicious files and behaviors are rare. The base rate means that a FN rate of 1% would be reasonably good for security software, while a FP rate of 1% would be disastrously undeployable.

Finally, it’s important to recognize that **false positives and false negatives differ in terms of impact**. For example:

* A false negative might allow an attacker to take over a device, losing it forever.
* A false positive might prevent a user from accomplishing an crucial task, making their device useless to them.

Customers acquire security software with the expectation that it will prevent bad things from happening; blocking a legitimate file or action is “a bad thing.” If the TI false positive rate is significant, users will lose trust in the protection and disable security features or override blocks. *It’s very hard to keep selling fire extinguishers when they periodically burst into flame and burn down the building where they’re deployed.*

-Eric

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2025/08/20/security-product-efficacy/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2025/08/20/security-product-efficacy/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-08-202025-08-21](https://textslashplain.com/2025/08/20/security-product-efficacy/)Posted in[security](https://textslashplain.com/category/security/)Tags:[Defender](https://textslashplain.com/tag/defender/), [security](https://textslashplain.com/tag/security/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Family Safety Content Filtering](https://textslashplain.com/2025/06/12/family-safety-content-filtering/)

[Next Post Next post:
2025 Summer Vacation](https://textslashplain.com/2025/08/25/2025-summer-vacation/)

### Leave a comment [Cancel reply](/2025/08/20/security-product-efficacy/#respond)

Δ

## Search Text/Plain

Search for:

## Pages

* [About](https://textslashplain.com/about/)
* [Browse All Posts](https://textslashplain.com/browse-all-posts/)
* [Categories](https://textslashplain.com/categories/)
* [Cruises](https://textslashplain.com/cruises/)
* [IEInternals Archive](https://textslashplain.com/ieinternals-archive/)
* [Races](https://textslashplain.com/races/)

## RSS

[![RSS Feed](https://textslashplain.com/i/rss/orange-small.png)](https://tex...