---
title: Doom GPU Flame Graphs
url: http://www.brendangregg.com/blog//2025-05-01/doom-gpu-flame-graphs.html
source: Brendan Gregg's Blog
date: 2025-05-01
fetch_date: 2025-10-06T22:25:32.560488
---

# Doom GPU Flame Graphs

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
* 30 Aug 2021 »
  [Analyzing a High Rate of Paging](/blog/2021-08-30/high-rate-of-paging.html)
* 27 Aug 2021 »
  [Slack's Secret STDERR Messages](/blog/2021-08-27/slack-crashes-secret-stderr.html)
* 05 Jul 2021 »
  [USENIX LISA2021 Computing Performance: On the Horizon](/blog/2021-07-05/computing-performance-on-the-horizon.html)

[Blog index](/blog/index.html)
[About](/blog/about.html)
[RSS](/blog/rss.xml)

# [Brendan Gregg's Blog](/blog/index.html)

[home](/blog/index.html)

## Doom GPU Flame Graphs

01 May 2025

[AI Flame Graphs](/blog/2024-10-29/ai-flame-graphs.html) are now [open source](https://github.com/intel/iaprof) and include Intel Battlemage GPU support, which means it can also generate full-stack GPU flame graphs for providing new insights into gaming performance, especially when coupled with [FlameScope](/flamescope.html) (an older open source project of mine). Here's an example of GZDoom, and I'll start with flame scopes for both CPU and GPU utilization, with details annotated:

[![](/blog/images/2025/flamescopes1.png)](/blog/images/2025/flamescopes1.png)

(Here are the raw [CPU](/blog/images/2025/cpu_flamescope.png) and [GPU](/blog/images/2025/gpu_flamescope.png) versions.) FlameScope shows a subsecond-offset heatmap of profile samples, where each column is one second (in this example, made up of 50 x 20ms blocks) and the color depth represents the number of samples, revealing variance and perturbation that you can select to generate a flame graph just for that time range. Update: the row size can be ajusted (it is limited by the sample rate captured in the profile), e.g., you could generate 60 rows to match 60fps games.

Putting these CPU and GPU flame scopes side by side has enabled your eyes to do pattern matching to solve what would otherwise be a time-consuming task of performance correlation. The gaps in the GPU flame scope on the right – where the GPU was not doing much work – match the heavier periods of CPU work on the left.

## CPU Analysis

FlameScope lets us click on the interesting periods. By selecting one of the CPU shader compilation stripes we get the flame graph just for that range:

[![](/blog/images/2025/cpuflamegraph_shader1.png)](/blog/images/2025/cpuflamegraph_shader1.png)

This is brilliant, and we can see exactly why the CPUs were busy for about 180 ms (the vertical length of the red stripe): it's doing compilation of GPU shaders and some NIR preprocessing (optimizations to the [NIR intermediate representation](https://docs.mesa3d.org/nir/index.html) that Mesa uses internally). If you are new to flame graphs, you look for the widest towers and optimize them first. Here is the [interactive SVG](/blog/images/2025/cpu_flamegraph.svg).

CPU flame graphs and CPU flame scope aren't new (from [2011](/flamegraphs.html) and [2018](/flamescope.html), both open source). What is new is full-stack **GPU** flame graphs and **GPU** flame scope.

## GPU Analysis

![](/blog/images/2025/gpuflamescope_highlight.png)

Interesting details can also be selected in the GPU FlameScope for generating GPU flame graphs.
This example selects the "room 3" range, which is a room in the Doom map that contains hundreds of enemies.
The green frames are the actual instructions running on the GPU, aqua shows the source for these functions, and red (C) and yellow (C++) show the CPU code paths that initiated the GPU programs. The gray "-" frames just help highlight the boundary between CPU and GPU code. (This is similar to what I described in the [AI flame graphs](/blog/2024-10-29/ai-flame-graphs.html) post, which included extra frames for kernel code.) The x-axis is proportional to cost, so you look for the widest things and find ways to reduce them.

[![](/blog/images/2025/gpuflamegraph_title.png)](/blog/images/2025/gpuflamegraph_title.png)

![](/blog/images/2025/gpu_flamegraph.svg)

I've included the [interactive SVG](/blog/images/2025/gpu_flamegraph.svg) version of this flame graph so you can mouse-over elements and click to zoom. ([PNG](/blog/images/2025/gpu_flamegraph.png) version.)

The GPU flame graph is split between stalls coming from rendering walls (41.4%), postprocessing effects (35.7%), stenciling (17.2%), and sprites (4.95%). The CPU stacks are further differentiated by the individual shaders that are causing stalls, along with the reasons for those stalls.

## GZDoom

We picked [GZDoom](https://zdoom.org/index) to try since it's an open source version of a well known game that runs on Linux (our profiler does not support Windows yet). Intel Battlemage makes light work of GZDoom, however, and since the GPU profile is stall-based we weren't getting many samples. We could have switched to a more modern and GPU-demanding game, but didn't have any great open source ideas, so I figured we'd just make GZDoom more demanding. We built GPU demanding maps for GZDoom (I can't believe I have found a work-related reason to be using [Slade](https://slade.mancubus.net/index.php?page=about)), and also set some Battlemage tunables to limit resources, magnifying the utilization of remaining resources.

[![](/blog/i...