---
title: Why Tokens Per Second Matters Less Than You Think
url: http://b1twis3.ca/why-tokens-per-second-matters-less-than-you-think/
source: B1twis3 | HM
date: 2026-10-11
fetch_date: 2026-10-12T08:13:35.602991
---

# Why Tokens Per Second Matters Less Than You Think

Search for:

[# B1twis3 | HM](http://b1twis3.ca "B1twis3 | HM")

Security Researcher

* [Home](http://b1twis3.ca/)
* [Lab](http://b1twis3.ca)
* [Twitter Feed](http://twitter.com/fasthm00)
* [My Repo](http://github.com/Leoid)

MenuHomeLabTwitter FeedMy Repo

[Home](http://b1twis3.ca) / [Uncategorized](http://b1twis3.ca/category/uncategorized/) / Why Tokens Per Second Matters Less Than You Think

# Why Tokens Per Second Matters Less Than You Think

Why Tokens Per Second Matters Less Than You Think
[October 11, 2026](http://b1twis3.ca/why-tokens-per-second-matters-less-than-you-think/ "Why Tokens Per Second Matters Less Than You Think")
[admin](http://b1twis3.ca/author/admin/ "View all posts by admin")

[Uncategorized](http://b1twis3.ca/category/uncategorized/)

![](http://b1twis3.ca/wp-content/uploads/2026/10/Screenshot-2026-10-11-at-9.53.55-AM.png)

*Why a wrong fast answer costs more than a right slow one*, *and why the ecosystem isn’t ready for it anyway*

Oct 10, 2026 · @b1twis3 | HM

## Do we need faster models?

Every couple of days the community posts a screenshot of a local model running at 40, 50, 60 or even 300 tps. The replies go like “how and what kind of hardware is needed” Less replies go by “What did the extra speed actually buy us?”.

For most engineering based work, inference, running models locally, the honest answer is perhaps little. But past 20 to 40 tps, the bottleneck now leaves the model. It moves to the user reading the decoded text or output, to the workflow/tool that reads the output or built around it, and above all to the work of checking whether the answer is right, not just false positive.

In this article, I make an argument. A wrong fast answer costs you more than a right slow one, because verification, triage, allocating resource for that, dominate the real cost of using a model. However, there might be fields where speed genuinely matters because their ecosystem is.

The token per second numbers shared are usually single stream decode, meaning how fast one request emits tokens after the first one appears. It is one of three speeds that matter, and often the least important of the three.

*Prefill speed* is how fast the model reads your prompt before it starts answering. It matters when you paste in long files, codebases, or chat history.

*Single stream decod**e*** is how fast one answer comes out once it starts. It matters when one person is watching one reply.

*Aggregate throughput* is the total output across many requests running at once. It matters for batch jobs, multi agent setups, and shared servers.

The three can move independently. A four node cluster (Dgx Sparks for instance) serving a 744B MoE might show 29 tok/s single stream, 70 tok/s aggregate across 8 streams, and 550 tok/s prefill. Swap the quantization or the engine and any one of those can jump while the other two stay flat or fall.

Decode or prose speed dominates the conversation because it is easy to observe and measure, it fits in one number, and looks cool. It hides the two things that usually matters and decide whether the session was productive in your field, such as, how long you have waited before anything appeared, and whether what appeared was correct.

This mean, human are the slowest reader or consumer in the loop. Because the average adult reads English nonfiction silently at about 238 words per minute, according to a review of 190 studies ([Brysbaert, 2019](https://reader.ku.edu/sites/reader/files/2024-01/How%20many%20words%20do%20we%20read%20per%20minute%20%281%29.pdf)). At roughly 0.75 words per token, that is about 5.3 tok/s. Fiction runs slightly faster, around 5.8 tok/s.

The same paper notes that reading above 1,000 words per minute with real comprehension is not possible, because the eye can only take in so much per fixation. That ceiling works out to about 22 tok/s. So, this means a model with 25 tok/s prose is already faster than a reader who does not exist (yet).

**Test it yourself.** You ask for a 600 word explanation, about 800 tokens.

| Decode speed | Generation time | Reading time at 238 wpm | When you finish reading |
| --- | --- | --- | --- |
| 25 tok/s | **32 s** | 151 s | 151 s |
| 100 tok/s | **8 s** | 151 s | 151 s |

Both models write faster than you read, so you finish at the same time either way; the fast one just finishes writing sooner. With code, the effect is even stronger, because people read code much more slowly than prose.

Now consider this claim, which I tested and observed a lot, at work, or during my personal projects. The time a model spends generating is usually the cheapest part of using it. the expensive parts and real cost come after. This includes, reading the answer, triaging it, and paying for it when it turns out to be wrong, not practical, theoretical only or simply wrong.

### Example: Reviewing a suspicious function

When you ask an LLM model whether a parser, decoder, deserializer has a memory related vulnerability. The answer might cost ~1K tokens. Below is a mimic or illustrative when you compare a smaller fast (100 tok/s) with a larger slow one (20 tok/s).

|  | Fast setup | Slow setup |
| --- | --- | --- |
| Decode speed | 100 tok/s | 20 tok/s |
| Generation time | 10 s | 50 s |
| Chance the answer is right | 60% | 85% (More parameters) |
| Your time to verify | 5 min | 5 min |
| Cost when wrong (notice, dig in, redo) | 15 min | 15 min |
| **Expected time per task** | **11.2 min** | **8.1 min** |
| **Per 100 tasks** | **18.6 h** | **13.5 h** |

The fast setup saves 40 seconds of generation per task and loses almost 4 minutes to rework. Over 100 tasks it costs about five extra hours, despite decoding five times faster.

And this is the friendly case, where every wrong answer gets caught. An uncaught one is worse, a false positive escalated to a vendor, a missed bug that ships, or a confident claim in a report that someone else builds on. Those costs have no upper bound.

On local hardware, speed is usually bought with something else. The common levers are a smaller model, fewer bits per weight (4 bit down to 2 bit), a smaller context, or a lower reasoning setting such as low or off efforts. Each one can raise decode speed, and each one can raise the chance of a wrong answer.

That trade is often invisible. Benchmarks report tok/s precisely and quality loosely, so a 40% speed gain looks like a clear win while a few points of accuracy loss looks like noise.

### What happens when generation is cheap and triaging is not (Bug Bounty Example)

The curl project ended its HackerOne bug bounty at the end of January 2026 after being overwhelmed by low quality, AI generated vulnerability reports ([BleepingComputer](https://bleepingcomputer.com/news/security/curl-ending-bug-bounty-program-after-flood-of-ai-slop-reports/)). Daniel Stenberg has said that until early 2025 only about one in six security reports to curl were real ([The New Stack](https://thenewstack.io/curls-daniel-stenberg-ai-is-ddosing-open-source-and-fixing-its-bugs/)). Each fake report took seconds to generate and hours of a small team’s time to disprove.

That is the formula at scale. Faster generation would only have made it worse, more bug bounty reports per hour, the same handful of maintainers, the same hours per report.

In METR’s 2025 randomized trial, 16 experienced open source developers took 19% longer on real issues when AI tools were allowed. They had predicted a 24% speedup and still believed they had been sped up by 20% afterwards ([METR, 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)). METR now treats those numbers as out of date and thinks later tools likely do speed developers up ([METR, Feb 2026](https://metr.org/blog/2026-02-24-uplift-update/)). The lesson is the perception gap, fluent, fast output feels productive even when review and cleanup eat the gain.

Hence, the more expert the user, the higher the verification cost and the lower the tolerance for errors. A security ...