---
title: Ask your LLM for receipts: What I learned teaching Claude C++ crash triage
url: http://addxorrol.blogspot.com/2025/12/ask-your-llm-for-receipts-what-i.html
source: ADD / XOR / ROL
date: 2025-12-12
fetch_date: 2025-12-13T03:14:27.252491
---

# Ask your LLM for receipts: What I learned teaching Claude C++ crash triage

# [ADD / XOR / ROL](http://addxorrol.blogspot.com/)

A blog about reverse engineering, mathematics, politics, economics and more ...

## Friday, December 12, 2025

### Ask your LLM for receipts: What I learned teaching Claude C++ crash triage

I recently embarked on a small toy project/experiment: How well can I equip Claude Code to automatically analyze and triage crashes in a C++ code base?

For the experimentation, I worked on a small number of crashes in the ffmpeg bug tracker. The initial results were very discouraging, Claude hallucinated all sorts of implausible root causes and tended to write typical "AI slop" -- things that follow the form of a well-written report, but that had no bearing on reality.

I iterated for a few days, but ultimately I got things to work reasonably well, at least to the point where I was happy with the result.

The result of this little diversion are a bunch of .md files (subagents and skills) that I contributed to <https://github.com/gadievron/raptor> - specifically the following parts:

[https://github.com/gadievron/raptor/blob/main/.claude/agents/crash-analysis-agent.md](goog_336902655)

[https://github.com/gadievron/raptor/blob/main/.claude/agents/coverage-analysis-generator-agent.md](goog_336902655)

[https://github.com/gadievron/raptor/blob/main/.claude/agents/function-trace-generator-agent.md](goog_336902655)

[https://github.com/gadievron/raptor/blob/main/.claude/agents/crash-analyzer-agent.md](goog_336902655)

<https://github.com/gadievron/raptor/blob/main/.claude/agents/crash-analyzer-checker-agent.md>

and the skills under <https://github.com/gadievron/raptor/tree/main/.claude/skills/crash-analysis>

The task itself is not necessarily a natural fit for an LLM: I find that LLMs tend to perform better in situations where their results can be immediately verified. This is not the case here - crash triage fundamentally includes a component of "narrative building", and it is not super clear how to validate such a narrative.

There are a few things that I took from my experience in using Claude Code for C++ development in the last year which I applied:

* Since LLMs only perceive the world through text, but their context is a scarce resource, it makes sense to provide them with effective ways of gathering extra data without wasting too much context.
* LLMs will hallucinate arbitrary things but tend to course-correct if their context includes too much data that is obviously in contradiction with their current trajectory.

In my C++ development, I learnt to provide the LLMs with copious amount of conditionally-compiled logging, and ways of running granular tests, so gathering information about what is happening without totally swamping the context window was possible.

Anyhow, what does the crash-analysis-agent end up doing?

1. It gathers a lot of stuff that provides text-level data about what is going on in the program that crashes: A function-level execution trace, gcov data, an ASAN build, and an rr recording that allows deterministic replay of a particular crashing execution.
2. It launches a subagent to then formulate a hypothesis of what is going on. This subagent is instructed to "provide receipts" for each step in the reasoning: Show the precise place where the pointer that ultimately leads to the crashing deref is allocated, show all the modifications, both in the source code **and** in the rr trace. Show all modifications to it, including the pointer values pre/post modification in the rr trace.
3. This hypothesis document is then validated by a separate subagent that is instructed to carefully vet each of the steps in the first document, and reject the file if any evidence is missing. On rejection, a rebuttal is written. This rebuttal is then passed to the previous agent again, until a report is generated that the validator accepts.
4. The final output is a report that includes specific breakpoints, pointer values, pointer modifications etc. that can be manually verified by a human by stepping through the provided rr trace.

In some sense, this is "LLM as a judge", but it appears to me that the usual problem ("generating LLM is convincing enough that the judge LLM waves everything through") is side-stepped by making the judging LLM focus on the formal correctness of the individual steps.

I didn't think much of this, but when I presented this to an audience during the last week, some of the feedback I got was that the technique of "ask the LLM for detailed receipts & have a second LLM validate the receipts" was not necessarily widely known.

So here we are. If you have a task that is perhaps not verifiable on it's final output, but involves verifiable substeps, you can greatly boost performance by providing the LLM with tools/skills to "provide receipts" for the substeps - the final output might still be wrong, but it is so with a much decreased probability.

Posted by

[halvar.flake](https://draft.blogger.com/profile/12486016980670992738 "author profile")

at
[3:17 AM](http://addxorrol.blogspot.com/2025/12/ask-your-llm-for-receipts-what-i.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://draft.blogger.com/post-edit.g?blogID=14114712&postID=1848391930076815546&from=pencil "Edit Post")

#### No comments:

[Post a Comment](https://draft.blogger.com/comment/fullpage/post/14114712/1848391930076815546)

[Older Post](http://addxorrol.blogspot.com/2025/07/understand-neural-nets-better-post-5-of.html "Older Post")
[Home](http://addxorrol.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://addxorrol.blogspot.com/feeds/1848391930076815546/comments/default)

## Blog Archive

* ▼
  [2025](http://addxorrol.blogspot.com/2025/)
  (7)
  + ▼
    [December](http://addxorrol.blogspot.com/2025/12/)
    (1)
    - [Ask your LLM for receipts: What I learned teaching...](http://addxorrol.blogspot.com/2025/12/ask-your-llm-for-receipts-what-i.html)
  + ►
    [July](http://addxorrol.blogspot.com/2025/07/)
    (2)
  + ►
    [May](http://addxorrol.blogspot.com/2025/05/)
    (1)
  + ►
    [April](http://addxorrol.blogspot.com/2025/04/)
    (2)
  + ►
    [March](http://addxorrol.blogspot.com/2025/03/)
    (1)

* ►
  [2024](http://addxorrol.blogspot.com/2024/)
  (4)
  + ►
    [December](http://addxorrol.blogspot.com/2024/12/)
    (1)
  + ►
    [July](http://addxorrol.blogspot.com/2024/07/)
    (2)
  + ►
    [January](http://addxorrol.blogspot.com/2024/01/)
    (1)

* ►
  [2023](http://addxorrol.blogspot.com/2023/)
  (1)
  + ►
    [December](http://addxorrol.blogspot.com/2023/12/)
    (1)

* ►
  [2021](http://addxorrol.blogspot.com/2021/)
  (1)
  + ►
    [February](http://addxorrol.blogspot.com/2021/02/)
    (1)

* ►
  [2020](http://addxorrol.blogspot.com/2020/)
  (4)
  + ►
    [September](http://addxorrol.blogspot.com/2020/09/)
    (1)
  + ►
    [August](http://addxorrol.blogspot.com/2020/08/)
    (1)
  + ►
    [May](http://addxorrol.blogspot.com/2020/05/)
    (1)
  + ►
    [March](http://addxorrol.blogspot.com/2020/03/)
    (1)

* ►
  [2019](http://addxorrol.blogspot.com/2019/)
  (1)
  + ►
    [August](http://addxorrol.blogspot.com/2019/08/)
    (1)

* ►
  [2018](http://addxorrol.blogspot.com/2018/)
  (3)
  + ►
    [October](http://addxorrol.blogspot.com/2018/10/)
    (1)
  + ►
    [March](http://addxorrol.blogspot.com/2018/03/)
    (1)
  + ►
    [February](http://addxorrol.blogspot.com/2018/02/)
    (1)

* ►
  [2017](http://addxorrol.blogspot.com/2017/)
  (1)
  + ►
    [August](http://addxorrol.blogspot.com/2017/08/)
    (1)

* ►
  [2016](http://addxorrol.blogspot.com/2016/)
  (3)
  + ►
    [October](http://addxorrol.blogspot.com/2016/10/)
    (1)
  + ►
    [September](http://addxorrol.blogspot.com/2016/09/)
    (1)
  + ►
    [January](http://addxorrol.blogspot.com/2016/01/)
    (1)

* ►
  [2015](http://addxorrol.blogspot.com/2015/)
  (3)
  + ►
    [December](http://addxorrol.blogspot.com/2015/12/)
    (2)
  + ►
    [May](http://addxorrol.blogspot.com/2015/05/)
    (1)

* ►
...