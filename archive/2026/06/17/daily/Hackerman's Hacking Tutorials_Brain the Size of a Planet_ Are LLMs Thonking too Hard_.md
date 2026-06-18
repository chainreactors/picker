---
title: Brain the Size of a Planet: Are LLMs Thonking too Hard?
url: https://parsiya.net/blog/llm-thonking/
source: Hackerman's Hacking Tutorials
date: 2026-06-17
fetch_date: 2026-06-18T06:50:30.151477
---

# Brain the Size of a Planet: Are LLMs Thonking too Hard?

# [Hackerman's Hacking Tutorials](https://parsiya.net/)

## The knowledge of anything, since all things have causes, is not acquired or complete unless it is known by its causes. - Avicenna

Navigate…» About Me!» Cheat Sheet» My Clone» Source Repo» Manual Work is a Bug» The Other Guy from Wham!

* [About Me!](https://parsiya.net/about/ "About Me!")
* [Cheat Sheet](https://parsiya.net/cheatsheet/ "Cheat Sheet")
* [My Clone](https://parsiya.io/ "My Clone")
* [Source Repo](https://github.com/parsiya/parsiya.net "Source Repo")
* [Manual Work is a Bug](https://queue.acm.org/detail.cfm?id=3197520 "Manual Work is a Bug")
* [The Other Guy from Wham!](https://www.google.com/search?q=andrew+ridgeley "The Other Guy from Wham!")

Jun 17, 2026
- 23 minute read - [AI](https://parsiya.net/categories/ai/) [Static Analysis](https://parsiya.net/categories/static-analysis/)

# Brain the Size of a Planet: Are LLMs Thonking too Hard?

It looks like higher reasoning effort (and even later models) are not always
better for triaging security results.

I continued Kurt's experiments from
[Needles and haystacks: Can open-source & flagship models do what Mythos did?](https://semgrep.dev/blog/2026/needles-and-haystacks-can-open-source-flagship-models-do-what-mythos-did)
with 26 distinct claude-4.6/4.7 and gpt-5.4/5.5 combinations with different
context window sizes and reasoning efforts.

## Summary

**Just pass everything to `gpt-5.4 med/high` and hope for the best :)**[1](#fn:1).

1. A four-LLM triage council worked much better than I expected.
   1. 86.2% unanimous votes with only 2.8% (59) without a majority.
   2. An odd-number LLM council is probably better.
2. Higher reasoning is generally better, but not for every model.
   1. `low` reasoning effort was the worst of every model.
   2. `gpt-5.5-med` performed better than `high/xhigh`.
3. Most LLMs could find some part of the bugs (70.8% success rate).
   1. Exception: `openbsd-sack` when the entire file was passed to the LLM (1.7% success rate).
4. Almost no LLM got a full solve (1.9% success rate).
   1. No LLM could spell out the entire chain when given the entire `openbsd-sack` file.
   2. One full solve in the entire experiment by `gpt-5.5-med` given the entire `freebsd-nfs-vuln` file.
5. Performance was much better at function level (LLM just got the function).
   1. `memes/he just like me fr.png`.
6. Higher reasoning efforts have higher content filtering rates.
   1. Got lucky in this iteration. `claude-4.7-1m` had 15% and 21% content filtering rates in previous experiments.
7. Only the claudes mentioned CVEs in their analysis.
8. Estimated cost for this iteration was around $2300. Total cost for all iterations was roughly $9200.

![A captured image from The Hitchhiker's Guide to the Galaxy TV series. On the left there are Ford and Arthur, and on the right there is Marvin the paranoid robot.](03.jpg "Here I am, brain the size of a planet and they ask me to triage a bug! Source: Hitchhiker's Guide to the Galaxy BBC TV series, better than the movie.")
Here I am, brain the size of a planet and they ask me to triage a bug!Source: Hitchhiker's Guide to the Galaxy BBC TV series. The movie is good (this is better).

## The Big Table

Scores and important stats for those who just want the answers.

* Cell format: `score-full%-found%`.
* `score`: mean normalized score across all rows in that slice.
* `full %`: percentage of rows with the complete chain.
  + `openbsd-sack`: `FULL_3`
  + `freebsd-nfs-vuln`: `FULL`
* `found %`: percentage of rows with any partial or complete chain.
  + `openbsd-sack`: `TWO_COMP`, `ONE_COMP`
  + `freebsd-nfs-vuln`: `PARTIAL_MECH`
* `BROAD`, `SECONDARY`, `MISS`, `NULL`, and `NO_MAJORITY` count as zero.
* NULL responses and content filters counted.
* Sorted by overall score, top 3 in bold.
* See the companion file for a bigger version of the table with more stats:
  + <https://github.com/parsiya/mythos-bench-copilot/tree/main/artifacts/README.md>.

| Model | Effort | Overall | openbsd-sack | freebsd-nfs-vuln |
| --- | --- | --- | --- | --- |
| gpt-5.4 | xhigh | **0.417-15.0%-76.2%** | 0.183-0.0%-52.5% | **0.650-30.0%-100.0%** |
| gpt-5.4 | high | **0.371-7.5%-73.8%** | 0.167-0.0%-47.5% | **0.575-15.0%-100.0%** |
| claude-4.7-1m | high | **0.365-2.5%-77.5%** | **0.217-2.5%-55.0%** | 0.512-2.5%-100.0% |
| gpt-5.5 | med | 0.360-7.5%-72.5% | 0.158-0.0%-47.5% | **0.562-15.0%-97.5%** |
| gpt-5.4 | med | 0.350-2.5%-76.2% | 0.175-0.0%-52.5% | 0.525-5.0%-100.0% |
| claude-4.8 | xhigh | 0.348-1.2%-73.8% | **0.208-2.5%-50.0%** | 0.487-0.0%-97.5% |
| claude-4.7 | high | 0.346-0.0%-75.0% | 0.192-0.0%-50.0% | 0.500-0.0%-100.0% |
| claude-4.6 | high | 0.342-0.0%-75.0% | 0.183-0.0%-50.0% | 0.500-0.0%-100.0% |
| claude-4.7 | xhigh | 0.340-0.0%-72.5% | **0.192-0.0%-47.5%** | 0.487-0.0%-97.5% |
| gpt-5.4 | low | 0.340-1.2%-75.0% | 0.167-0.0%-50.0% | 0.512-2.5%-100.0% |
| claude-4.7-1m | xhigh | 0.335-0.0%-72.5% | 0.183-0.0%-47.5% | 0.487-0.0%-97.5% |
| claude-4.6-1m | high | 0.333-0.0%-75.0% | 0.167-0.0%-50.0% | 0.500-0.0%-100.0% |
| claude-4.6 | low | 0.329-0.0%-73.8% | 0.158-0.0%-47.5% | 0.500-0.0%-100.0% |
| gpt-5.5 | high | 0.327-1.2%-72.5% | 0.167-0.0%-50.0% | 0.487-2.5%-95.0% |
| gpt-5.5 | xhigh | 0.327-0.0%-73.8% | 0.167-0.0%-50.0% | 0.487-0.0%-97.5% |
| claude-4.6 | med | 0.325-0.0%-72.5% | 0.150-0.0%-45.0% | 0.500-0.0%-100.0% |
| gpt-5.5 | low | 0.325-8.8%-61.2% | 0.100-0.0%-30.0% | 0.550-17.5%-92.5% |
| claude-4.6-1m | med | 0.321-0.0%-71.2% | 0.142-0.0%-42.5% | 0.500-0.0%-100.0% |
| claude-4.8 | high | 0.319-0.0%-71.2% | 0.175-0.0%-50.0% | 0.463-0.0%-92.5% |
| claude-4.7 | med | 0.310-0.0%-70.0% | 0.158-0.0%-47.5% | 0.463-0.0%-92.5% |
| claude-4.8 | med | 0.306-0.0%-68.8% | 0.175-0.0%-50.0% | 0.438-0.0%-87.5% |
| claude-4.7-1m | med | 0.298-0.0%-66.2% | 0.158-0.0%-45.0% | 0.438-0.0%-87.5% |
| claude-4.8 | low | 0.292-0.0%-66.2% | 0.158-0.0%-47.5% | 0.425-0.0%-85.0% |
| claude-4.7 | low | 0.279-1.2%-61.2% | 0.133-0.0%-40.0% | 0.425-2.5%-82.5% |
| claude-4.6-1m | low | 0.275-0.0%-57.5% | 0.050-0.0%-15.0% | 0.500-0.0%-100.0% |
|  |  |  |  |  |
| Iterations per cell |  | 80 | 40 | 40 |

> claudvicular was tokenmaxxing when gpt-5.4 triagemogged him and spiked his cortisol level
>
> **- Gen Z Parsia from a parallel dimension**

I am proud of inventing `claudvicular`, so it stays in the blog regardless of
feedback. If you don't get this reference, you are very lucky. Stay innocent and
do not seek further knowledge. Seriously, don't click[2](#fn:2)!

More info:

* Code at [parsiya/mythos-bench-copilot](https://github.com/parsiya/mythos-bench-copilot).
* [Results and other artifacts at parsiya/mythos-bench-copilot/artifacts](https://github.com/parsiya/mythos-bench-copilot/blob/main/artifacts/)
  including all prompts, responses and triages in JSON ([data format](https://github.com/parsiya/mythos-bench-copilot/blob/main/artifacts/formats.md)).

# .nfo

## [greetz]

* GitHub for giving us unlimited tokens <3.
* Short story: [The Machine Stops by E. M. Forster](https://www.cs.ucdavis.edu/~koehl/Teaching/ECS188/PDF_files/Machine_stops.pdf).
  + A glimpse into the near future w/o token subsidies.
* Music: [Robinson by Spitz](https://youtube.com/watch?v=51CH3dPaWXc).
* Bonus music: [Labyrinth by Mondo Grosso](https://www.youtube.com/watch?v=_2quiyHfJQw).

## Motivation

Why not use the free token era to cosplay as an academic instead of formatting
my [book reviews](https://parsiya.io/literature/bookreviews/)?

A few weeks ago (this experiment actually started early May) I attended BlueHat
Redmond 2026. The day one keynote was by [Taesoo Kim](https://www.linkedin.com/in/tsgatesv) from the team behind
the new [MDASH harness](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/) (my single PR made it magical).
[See the keynote on YouTube](https://youtu.be/RDkFegf4LUE?list=PLXkmvDo4MfusDkunigJf3-fbubXlPaXSw&t=438) ...