---
title: USENIX SREcon APAC 2022: Computing Performance: What's on the Horizon
url: http://www.brendangregg.com/blog/2023-03-01/computer-performance-future-2022.html
source: Brendan Gregg's Blog
date: 2023-03-02
fetch_date: 2025-10-04T08:25:54.629476
---

# USENIX SREcon APAC 2022: Computing Performance: What's on the Horizon

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

## USENIX SREcon APAC 2022: Computing Performance: What's on the Horizon

01 Mar 2023

At USENIX SREcon22 APAC I gave the opening keynote on the future of computer performance, rounding up the latest developments and making predictions of where I see things heading. This talk originated from my updates to [Systems Performance 2nd Edition](/systems-performance-2nd-edition-book.html), and this was the first time I've given this talk in person!

The video is now on [YouTube](https://www.youtube.com/watch?v=zGSQdN2X_k0):

The slides are [online](/Slides/SREcon2022_ComputingPerformance/) and as a [PDF](/Slides/SREcon2022_ComputingPerformance.pdf):

![]()

first prev next last / permalink/zoom

In Q&A I was asked about CXL (compute express link) which was fortunate as I had planned to cover it and then forgot, so the question let me talk about it (although Q&A is missing from the video). CXL in a way allows a custom memory controller to be added to a system, to increase memory capacity, bandwidth, and overall performance. My personal opinion is that I don't see a widespread need for more capacity given horizontal scaling and servers that can already exceed 1 Tbyte of DRAM; bandwidth is also helpful, but I'd be concerned about the increased latency for adding a hop to more memory. So it's interesting, but I don't think they have the killer use case for it yet.

## Realizing and exceeding a lifelong dream

I began my tech career as a junior Unix sysadmin in Newcastle, NSW, Australia, in 1999, with no connection to the exciting world of tech in Silicon Valley, New York, or even nearby Sydney. As I was determined to become great at my new occupation regardless of my location, I read every sysadmin book, article, and magazine I could find on the shelf. This included SysAdmin magazine, which contained articles from various experts including Amy Rich, and a couple of advertisements: One was to submit your own articles to the magazine for publication (by writing to the editor, Rikki Endsley) and another was to attend USENIX conferences in the US and learn directly from the experts! I made both of these my goals, even though I'd never been published before and I'd never been to the US. Or even on a plane.

I didn't end up getting published in SysAdmin directly, but my performance work did make it as a feature article (thanks Matty). As for attending USENIX conferences: I finally started attending and speaking at them in 2010 when a community manager encouraged me to (thanks Deirdre Straughan), and since then I've met many friends and connections, including Amy who is now USENIX President, and Rikki with whom I co-chaired the USENIX LISA18 conference. USENIX has been a great help to my career and my employers, and I hope it is just as helpful for you. It's an important vendor-neutral space to share the latest in technology.

And now, helping bring USENIX conferences to Australia by giving the first keynote: I could not have scripted or expected it. It was a great privilege.

## SREcon 2023 CFP

Tech moves fast, however, and I have little time to reflect on 2022 when there's 2023 to plan! I'm now program co-chair for SREcon 2023 APAC, and our 2023 conference is June 14-16 in Singapore. The [call for participation](/blog/2023-02-17/srecon-apac-2023.html) ends on March 2nd 23:59 SGT! **That's about 24 hours from now!**

## References

I've reproduced the references from my SREcon22 keynote below, so you can click on links:

* [Gregg 08] Brendan Gregg, âZFS L2ARC,â <http://www.brendangregg.com/blog/2008-07-22/zfs-l2arc.html>, Jul 2008
* [Gregg 10] Brendan Gregg, âVisualizations for Performance Analysis (and More),â <https://www.usenix.org/conference/lisa10/visualizations-performance-analysis-and-more>, 2010
* [Greenberg 11] Marc Greenberg, âDDR4: Double the speed, double the latency? Make sure your system can handle next-generation DRAM,â <https://www.chipestimate.com/DDR4-Double-the-speed-double-the-latencyMake-sure-your-system-can-handle-next-generation-DRAM/Cadence/Technical-Article/2011/11/22>, Nov 2011
* [Hruska 12] Joel Hruska, âThe future of CPU scaling: Exploring options on the cutting edge,â <https://www.extremetech.com/computing/184946-14nm-7nm-5nm-how-low-can-cmos-go-it-depends-if-you-ask-the-engineers-or-the-economists>, Feb 2012
* [Gregg 13] Brendan Gregg, âBlazing Performance with Flame Graphs,â <https://www.usenix.org/conference/lisa13/technical-sessions/plenary/gregg>, 2013
* [Shimpi 13] Anand Lal Shimpi, âSeagate to Ship 5TB HDD in 2014 using Shingled Magnetic Recording,â <https://www.anandtech.com/show/7290/seagate-to-sh...