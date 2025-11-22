---
title: Intel is listening, don't waste your shot
url: http://www.brendangregg.com/blog//2025-11-22/intel-is-listening.html
source: Brendan Gregg's Blog
date: 2025-11-21
fetch_date: 2025-11-22T03:07:09.831952
---

# Intel is listening, don't waste your shot

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
* 30 Aug 2021 »
  [Analyzing a High Rate of Paging](/blog/2021-08-30/high-rate-of-paging.html)

[Blog index](/blog/index.html)
[About](/blog/about.html)
[RSS](/blog/rss.xml)

# [Brendan Gregg's Blog](/blog/index.html)

[home](/blog/index.html)

## Intel is listening, don't waste your shot

22 Nov 2025

Intel's new CEO, Lip-Bu Tan, has made listening to customers a top priority, saying at Intel Vision [earlier](https://www.reuters.com/technology/intels-new-ceo-tells-customers-be-brutally-honest-with-us-2025-03-31/) this year: "Please be brutally honest with us. This is what I expect of you this week, and I believe harsh feedback is most valuable."

I'd been in regular meetings with Intel for several years before I joined, and I had been giving them technical direction on various projects, including at times some brutal feedback.
When I finally interviewed for a role at Intel I was told something unexpected: that I had already accomplished so much within Intel that I qualified to be an Intel Fellow candidate. I then had to pass several extra interviews to actually become a Fellow (and was told I may only be the third person in Intel's history to be hired as a Fellow) but what stuck with me was that I had already accomplished so much at a company I'd never worked for.

If you are in regular meetings with a hardware vendor as a customer (or potential customer) you can accomplish a lot by providing firm and tough feedback, particularly with Intel today. This is easier said than done, however.

Now that I've seen it from the other side I realize I could have accomplished more, and you can too. I regret the meetings where I wasn't really able to have my feedback land as the staff weren't really getting it, so I eventually gave up. After the meeting I'd crack jokes with my colleagues about how the product would likely fail. (Come on, at least I tried to tell them!)

Here's what I wish I had done in any hardware vendor meeting:

* **Prep before meetings**: study the agenda items and look up attendees on LinkedIn and note what they do, how many staff they say they manage, etc.
* **Be aware of intellectual property risks**: Don't accept meetings covered by some agreement that involves doing a transfer of intellectual property rights for your feedback (I wrote a post on this); ask your legal team for help.
* **Make sure feedback is documented in the meeting minutes** (e.g., a shared Google doc) and that it isn't watered down. Be firm about what you know and don't know: it's just as important to assert when you haven't formed an opinion yet on some new topic.
* **Stick to technical criticisms** that are constructive (uncompetitive, impractical, poor quality, poor performance, difficult to use, of limited use/useless) instead of trash talk (sucks, dumb, rubbish).
* **Check minutes include who was present and the date.**
* **Ask how many staff are on projects** if they say they don't have the resources to address your feedback (they may not answer if this is considered sensitive) and share industry expectations, for example: âThis should only take one engineer one month, and your LinkedIn says you have over 100 staff.â
* **Decline freeloading**: If staff ask to be taught technical topics they should already know (likely because they just started a new role), decline, as I'm the customer and not a free training resource.
* **Ask "did you Google it?" a lot**: Sometimes staff join customer meetings to elevate their own status within the company, and ask questions they could have easily answered with Google or ChatGPT.
* **Ask for staff/project bans**: If particular staff or projects are consistently wasting your time, tell the meeting host (usually the sales rep) to take them off the agenda for at least a year, and don't join (or quit) meetings if they show up. Play bad cop, often no one else will.
* **Review attendees**. From time to time, consider: Am I meeting all the right people? Review the minutes. E.g., if you're meeting Intel and have been talking about a silicon change, have any actual silicon engineers joined the call?
* **Avoid peer pressure**: You may meet with the entire product team who are adamant that they are building something great, and you alone need to tell them it's garbage (using better words). Many times in my life I've been the only person to speak up and say uncomfortable things in meetings, yet I'm not the only person present who could.
* **Ask for status updates**: Be prepared that even if everyone appears grateful and appreciative of your feedback, you may realize six months later that nothing was done with it. Ask for updates and review the prior meeting minutes to see what you asked for and when.
* **Speak to ELT/CEO**: Once a year or so, ask to speak to someone on the executive leadership team (ELT; the leaders on the website) or the CEO. Share brutal feedback, and email them a copy of the meeting minutes...