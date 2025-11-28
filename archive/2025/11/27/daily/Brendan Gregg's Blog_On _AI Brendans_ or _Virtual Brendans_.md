---
title: On "AI Brendans" or "Virtual Brendans"
url: http://www.brendangregg.com/blog//2025-11-28/ai-virtual-brendans.html
source: Brendan Gregg's Blog
date: 2025-11-27
fetch_date: 2025-11-28T03:12:28.776616
---

# On "AI Brendans" or "Virtual Brendans"

Brendan's site:

[Start Here](/overview.html)
[Homepage](/index.html)
[Blog](/blog/index.html)

[Sys Perf book](/systems-performance-2nd-edition-book.html)
[BPF Perf book](/bpf-performance-tools-book.html)
[Linux Perf](/linuxperf.html)
[eBPF Tools](/ebpf.html)
[perf Examples](/perf.html)
[Perf Methods](/methodology.html)
[USE Method](/usemethod.html)
[TSA Method](/tsamethod.html)
[Off-CPU Analysis](/offcpuanalysis.html)
[Active Bench.](/activebenchmarking.html)
[WSS Estimation](/wss.html)
[Flame Graphs](/flamegraphs.html)
[Flame Scope](/flamescope.html)
[Heat Maps](/heatmaps.html)
[Frequency Trails](/frequencytrails.html)
[Colony Graphs](/colonygraphs.html)
[DTrace Tools](/dtrace.html)
[DTraceToolkit](/dtracetoolkit.html)
[DtkshDemos](/dtkshdemos.html)
[Guessing Game](/guessinggame.html)
[Specials](/specials.html)
[Books](/books.html)
[Other Sites](/sites.html)

[![](/Images/sysperf2nd_bookcover_360.jpg)](/systems-performance-2nd-edition-book.html)
*[Systems Performance 2nd Ed.](/systems-performance-2nd-edition-book.html)*

[![](/Images/bpfperftools_bookcover_360.jpg)](/bpf-performance-tools-book.html)
*[BPF Performance Tools book](/bpf-performance-tools-book.html)*

Recent posts:

* 28 Nov 2025 »
  [On "AI Brendans" or "Virtual Brendans"](/blog/2025-11-28/ai-virtual-brendans.html)
* 22 Nov 2025 »
  [Intel is listening, don't waste your shot](/blog/2025-11-22/intel-is-listening.html)
* 17 Nov 2025 »
  [Third Stage Engineering](/blog/2025-11-17/third-stage-engineering.html)
* 04 Aug 2025 »
  [When to Hire a Computer Performance Engineering Team (2025) part 1 of 2](/blog/2025-08-04/when-to-hire-a-computer-performance-engineering-team-2025-part1.html)
* 22 May 2025 »
  [3 Years of Extremely Remote Work](/blog/2025-05-22/3-years-of-extremely-remote-work.html)
* 01 May 2025 »
  [Doom GPU Flame Graphs](/blog/2025-05-01/doom-gpu-flame-graphs.html)
* 29 Oct 2024 »
  [AI Flame Graphs](/blog/2024-10-29/ai-flame-graphs.html)
* 22 Jul 2024 »
  [No More Blue Fridays](/blog/2024-07-22/no-more-blue-fridays.html)
* 24 Mar 2024 »
  [Linux Crisis Tools](/blog/2024-03-24/linux-crisis-tools.html)
* 17 Mar 2024 »
  [The Return of the Frame Pointers](/blog/2024-03-17/the-return-of-the-frame-pointers.html)
* 10 Mar 2024 »
  [eBPF Documentary](/blog/2024-03-10/ebpf-documentary.html)
* 28 Apr 2023 »
  [eBPF Observability Tools Are Not Security Tools](/blog/2023-04-28/ebpf-security-issues.html)
* 01 Mar 2023 »
  [USENIX SREcon APAC 2022: Computing Performance: What's on the Horizon](/blog/2023-03-01/computer-performance-future-2022.html)
* 17 Feb 2023 »
  [USENIX SREcon APAC 2023: CFP](/blog/2023-02-17/srecon-apac-2023.html)
* 02 May 2022 »
  [Brendan@Intel.com](/blog/2022-05-02/brendan-at-intel.html)
* 15 Apr 2022 »
  [Netflix End of Series 1](/blog/2022-04-15/netflix-farewell-1.html)
* 09 Apr 2022 »
  [TensorFlow Library Performance](/blog/2022-04-09/tensorflow-library-performance.html)
* 19 Mar 2022 »
  [Why Don't You Use ...](/blog/2022-03-19/why-dont-you-use.html)
* 26 Sep 2021 »
  [The Speed of Time](/blog/2021-09-26/the-speed-of-time.html)
* 06 Sep 2021 »
  [ZFS Is Mysteriously Eating My CPU](/blog/2021-09-06/zfs-is-mysteriously-eating-my-cpu.html)

[Blog index](/blog/index.html)
[About](/blog/about.html)
[RSS](/blog/rss.xml)

# [Brendan Gregg's Blog](/blog/index.html)

[home](/blog/index.html)

## On "AI Brendans" or "Virtual Brendans"

28 Nov 2025

There are now multiple AI performance engineering agents that use or are trained on my work. Some are helper agents that interpret flame graphs or eBPF metrics, sometimes privately called *AI Brendan*; others have trained on my work to create a *Virtual Brendan* that claims it can tune everything just like the real thing. It sounds like my brain has been uploaded to the cloud by someone else who is now selling it (yikes!). I've been told it's even "easy" to do this thanks to all my publications available to train on: >90 talks, >250 blog posts, >600 open source tools, and >3000 book pages. Are people allowed to sell you, virtually? And am I the first individual engineer to be AI'd? (There is a 30-year-old precedent for this, which I'll get to later.)

This is an emerging subject, with lots of different people, objectives, and money involved. Note that this is a personal post about my opinions, not an official post by my employer, so I won't be discussing internal details about any particular project. I'm also not here to recommend you buy any in particular.

## Summary

* **There are two types**:
  + **AI agents**. I've sometimes heard them called an AI Brendan because it does Brendan-like things, like systems performance recommendations and interpretation of flame graphs and eBPF metrics. There are already several of these and this idea in general should be useful.
  + **Virtual Brendan** can refer to something not just built on my work, but trained on my publications to create a virtual *me*. These would only automate about 15% of what I do as a performance engineer, and will go out of date if I'm not training it to follow industry changes.
* **Pricing is hard, in-house is easier**. With a typical pricing model of $20 per instance per month, customers may just use such an agent on one instance and then copy-and-paste any tuning changes to their entire fleet. There's no practical way to keep tuning changes secret, either. These projects are easier as internal in-house tools.
* **Some claim a lot but do little**. There's no Brendan Gregg benchmark or empirical measurement of my capability, so a company could claim to be selling a virtual Brendan that is nothing more than a dashboard with a few eBPF-based line charts and a flame graph. The few times I've given suggestions to projects, my ideas have been considered too hard or a low priority. Which leads me to believe that some aren't trying to make a good product -- they're in it to make a quick buck.
* **There's already been one expensive product failure**, but I'm not concluding that the idea is bad and the industry will give up. Other projects already exist.
* **Iâm not currently involved with any of these products**.
* **We need AI to help save the planet from AI**. Performance engineering gets harder every year as systems become more complex. With the rising cost of AI datacenters, we need better performance engineering more than ever. **We need AI agents that claim a lot *and do a lot***. I wish the best of luck to those projects that agree with this mantra.

## Earlier uses of AI

Before I get into the AI/Virtual Brendans, yes, we've been using AI to help performance engineering for years. Developers have been using coding agents that can help write performant code. And as a performance engineer, I'm already using ChatGPT to save time on resarch tasks, like finding release notes and recent developments for a given technology. I once used ChatGPT to find and old patch sent to lkml, just based on a broad description, which would otherwise take hours of trial-and-error searches. I keep finding more ways that ChatGPT/AI is useful to me in my work.

## AI Agents (AI Brendans)

A common approach is to take a CPU flame graph and have AI do pattern matching to find performance issues. Some of these agents will apply fixes as well. It's like a modern take on the practice of "recent performance issue checklists," just letting AI do the pattern matching instead of the field engineer.

I've recently worked on a [Fast by Friday](https://www.brendangregg.com/Slides/KernelRecipes2023_FastByFriday/) methodology: where we engineer systems so that performance can be root-cause analyzed in 5 days or less. Having an AI agent look over flame graphs, metrics, and other data sources to match previously seen issues will save time and help make Fast by Friday possible. For some companies with few or no performance engineers, I'd expect matching previously seen issues should find roughly 10-50% performance gains.

I've heard some flame graph agents privately referred to as an "AI Brendan"...