---
title: Curvance: Invariants unleashed
url: https://blog.trailofbits.com/2024/04/30/curvance-invariants-unleashed/
source: Trail of Bits Blog
date: 2024-05-01
fetch_date: 2025-10-06T17:17:34.640626
---

# Curvance: Invariants unleashed

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Curvance: Invariants unleashed

Nat Chin

April 30, 2024

[audits](/categories/audits/), [blockchain](/categories/blockchain/), [fuzzing](/categories/fuzzing/), [invariant-development](/categories/invariant-development/)

Welcome to our deep dive into the world of invariant development with Curvance.

We’ve been building invariants as part of regular code review assessments for more than 6 years now, but our work with Curvance marks our very first official [invariant development](https://blog.trailofbits.com/2023/10/05/introducing-invariant-development-as-a-service/) project, in which developing and testing invariants is all we did.

Over the nine-week engagement, we wrote and tested 216 invariants, which helped us uncover 13 critical findings. We also found opportunities to significantly enhance our tools, including advanced trace printing and corpus preservation. This project was a journey of navigating learning curves and accomplishing technological feats, and this post will highlight our collaborative efforts and the essential role of teamwork in helping us meet the challenge. And yes, we’ll also touch on the brain-cell-testing moments we experienced throughout this project!

![](/img/wpdump/da935a97f0ffbed440d411ea546a7bef.png)

A collective “losing it” moment, capturing the challenges of this project

## Creating a quality fuzzing suite

**The success of a fuzzing suite is grounded in the quality of its invariants.** Throughout this project, we focused on fine-tuning each invariant for accuracy and relevance. Fuzzing, in essence, is like having smart monkeys on keyboards testing invariants, whose effectiveness relies heavily on their precision. Our journey with Curvance over nine weeks involved turning in-depth discussions on codebase properties into precise English explanations and then coding them into executable tests, as shown in the screenshots below.

![](/img/wpdump/904ea3fb0f09fd905d476687fae79c09.png)

Examples of what our daily discussions looked like to clarify invariants

From the get-go, Chris from Curvance was often available to help clarify the code’s expected behavior and explain Curvance’s design choices. His insights always clarified complex functions and behavior, and he always helped with hands-on debugging and checking our invariants. This engagement was as productive as it was thanks to Chris’s consistent feedback and working alongside us the entire time. Thank you, Curvance!

### The tools (and support teams) behind our success

Along with Curvance’s involvement, support from our internal teams behind Echidna, Medusa, and CloudExec helped our project succeed. Their swift responses to issues, especially during extensive rebases and complex debugging, were crucial. The Curvance engagement pushed these tools to their limits, and the solutions we had to come up with for the challenges we faced led to significant enhancements in these tools.

[CloudExec](https://github.com/crytic/cloudexec) proved invaluable for deploying long fuzzing jobs onto DigitalOcean. We integrated it with Echidna and Medusa for prolonged runs, enabling Curvance to easily set up its own future fuzzing runs. We pinpointed areas of improvement for CloudExec, such as its preservation of output data, which you can see on its [GitHub issue tracker](https://github.com/crytic/cloudexec/issues). We’ve already addressed many of these issues.

[Echidna](https://github.com/crytic/echidna), our property-based fuzzer for Ethereum contracts, was pivotal in falsifying assertions. We first used Echidna in exploration mode to broadly cover the Curvance codebase, and then we moved into assertion mode, using anywhere from 10 million to 100 billion iterations. This intense use of Echidna throughout our nine-week engagement helped us uncover vital areas of improvement for the tool, making it easier for it to debug and retain the state of explored code areas.

[Medusa](https://github.com/crytic/medusa), our `geth`-based experimental fuzzer, complemented Echidna in its coverage efforts for falsifying invariants on Curvance. Before we could use Medusa for this engagement, we needed to fix a known out-of-memory bug. The fix for this bug—along with fixes implemented in CloudExec to help it better preserve output data—critically improved the tool and helped maximize our coverage of the Curvance code. Immediately after it started running, it found a medium-severity bug in the code that Echidna had missed. (Echidna eventually found this bug after we changed the block time delay, likely due to the fuzzer’s non-determinism.)

![](/img/wpdump/3aaacd8f957c732451b159dfb98b5862.png)

Our first Medusa run of 48+ hours resulted in a medium-severity bug.

## The long and winding road

While we had the best support from the teams behind our tools and from our client that we could have asked for, we still faced considerable challenges throughout this project—from the need to keep pace with Curvance’s continued development, to the challenges of debugging assertion failures. But by meeting these challenges, we learned important lessons about the nature of invariant development, and we were able to implement crucial upgrades to our tools to improve our process overall.

### Racing to keep up with Curvance’s code changes

Changes to the Curvance codebase—like function removals, additions of function parameters, adjustments to arguments and error messages, and renaming of source contracts—often challenged our fuzzing suite by invalidating existing invariants or causing a series of assertion failures. Ultimately, these changes rendered our existing corpus items obsolete and unusable, and we had to rebase our fuzzing suite and revise both existing and new invariants constantly to ensure their continued relevance to the evolving system. This iterative process paralleled the client’s code development, presenting a mix of true positives (actual bugs in the client’s code) and false positives (failures due to incorrect or outdated invariants). Such outcomes emphasized that fuzzing isn’t a static, one-time setup; it demands ongoing maintenance and updates, akin to development of any active codebase.

Understanding the rationale behind each invariant change post-rebase is crucial. Hasty adjustments without fully grasping their implications could inadvertently mask bugs, undermining the effectiveness of the fuzzing suite. Keeping the suite alive and relevant is as vital as the development of the codebase itself. It’s not just about letting the fuzzer run; it’s about maintaining its alignment with the system it tests. Remember, the true power of a fuzzing suite lies in the accuracy of its invariants.

#### Critical tool upgrades and lessons learned

We had to make a significant rebase after the `Lendtroller` contract’s name was changed to `MarketManager` in commit `a96dc9a`. This change drastically impacted our work, as Echidna had just finished 43 days of running in the cloud using CloudExec. This nonstop execution had allowed Echidna to develop a detailed corpus capable of autonomously tackling complex liquidations. Unfortunately, the change rendered this corpus obsolete, and each corpus item caused Echidna worker threads to crash upon transaction replay. With our setup of 15 workers, it took only 14 more transactions that could not be replayed for all the Echidna workers to crash, halting Echidna entirely:

![](/img/wpdump/712f7c757b5ab5f55cefeef8724c1aae.png)

An Echidna crash resulting from not being able to replay corpus item

Our rebase due to Curvance’s code change led to a significant problem: our fuzzers could no longer access `MarketManager` functions needed to explore complex state, like posting collateral and borrowing debt. This issue prompted us to make crucial updates to Echidna, specifically to enhance [its ability to validate](https://github.com/crytic/ec...