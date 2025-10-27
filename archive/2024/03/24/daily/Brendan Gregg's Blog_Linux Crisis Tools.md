---
title: Linux Crisis Tools
url: http://www.brendangregg.com/blog//2024-03-24/linux-crisis-tools.html
source: Brendan Gregg's Blog
date: 2024-03-24
fetch_date: 2025-10-04T12:08:19.426700
---

# Linux Crisis Tools

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

## Linux Crisis Tools

24 Mar 2024

When you have an outage caused by a performance issue, you don't want to lose precious time just to install the tools needed to diagnose it. Here is a list of "crisis tools" I recommend installing on your Linux servers by default (if they aren't already), along with the (Ubuntu) package names that they come from:

| Package | Provides | Notes |
| --- | --- | --- |
| procps | ps(1), vmstat(8), uptime(1), top(1) | basic stats |
| util-linux | dmesg(1), lsblk(1), lscpu(1) | system log, device info |
| sysstat | iostat(1), mpstat(1), pidstat(1), sar(1) | device stats |
| iproute2 | ip(8), ss(8), nstat(8), tc(8) | preferred net tools |
| numactl | numastat(8) | NUMA stats |
| tcpdump | tcpdump(8) | Network sniffer |
| linux-tools-common linux-tools-$(uname -r) | perf(1), turbostat(8) | profiler and PMU stats |
| bpfcc-tools (bcc) | opensnoop(8), execsnoop(8), runqlat(8), softirqs(8), hardirqs(8), ext4slower(8), ext4dist(8), biotop(8), biosnoop(8), biolatency(8), tcptop(8), tcplife(8), trace(8), argdist(8), funccount(8), profile(8), etc. | canned eBPF tools[1] |
| bpftrace | bpftrace, basic versions of opensnoop(8), execsnoop(8), runqlat(8), biosnoop(8), etc. | eBPF scripting[1] |
| trace-cmd | trace-cmd(1) | Ftrace CLI |
| nicstat | nicstat(1) | net device stats |
| ethtool | ethtool(8) | net device info |
| tiptop | tiptop(1) | PMU/PMC top |
| cpuid | cpuid(1) | CPU details |
| msr-tools | rdmsr(8), wrmsr(8) | CPU digging |

(This is based on Table 4.1 "Linux Crisis Tools" in [SysPerf 2](/systems-performance-2nd-edition-book.html).)

Some longer notes: [1] bcc and bpftrace have many overlapping tools: the bcc ones are more capable (e.g., CLI options), and the bpftrace ones can be edited on the fly. But that's not to say that one is better or faster than the other: They emit the same BPF bytecode and are equally fast once running. Also note that bcc is evolving and migrating tools from Python to libbpf C (with CO-RE and BTF) but we haven't reworked the package yet. In the future "bpfcc-tools" should get replaced with a much smaller "libbpf-tools" package that's just tool binaries.

This list is a minimum. Some servers have accelerators and you'll want their analysis tools installed as well: e.g., on Intel GPU servers, the intel-gpu-tools package; on NVIDIA, nvidia-smi. Debugging tools, like gdb(1), can also be pre-installed for immediate use in a crisis.

Essential analysis tools like these don't change that often, so this list may only need updating every few years. If you think I missed a package that is important today, please let me know (e.g., in the comments).

The main downside of adding these packages is their on-disk size. On cloud instances, adding Mbytes to the base server image can add seconds, or fractions of a second, to instance deployment time. Fortunately the packages I've listed are mostly quite small (and bcc will get smaller) and should cost little size and time. I have seen this size concern prevent debuginfo (totaling around 1 Gbyte) from being included by default.

## Can't I just install them later when needed?

Many problems can occur when trying to install software during a production crisis. I'll step through a made-up example that combines some of the things I've learned the hard way:

* **4:00pm**: Alert! Your company's site goes down. No, some people say it's still up. Is it up? It's up but too slow to be usable.
* **4:01pm**: You look at your monitoring dashboards and a group of backend servers are abnormal. Is that high disk I/O? What's causing that?
* **4:02pm**: You SSH to one server to dig deeper, but SSH takes forever to login.
* **4:03pm**: You get a login prompt and type "iostat -xz 1" for basic disk stats to begin with. There is a long pause, and finally "Command 'iostat' not found...Try: sudo apt install sysstat". Ugh. Given how slow the system is, installing this package could take several minutes. You run the install command.
* **4:07pm**: The package install has failed as it can't resolve the repositories. Something is wrong with the /etc/apt configuration. Since the server owners are now in the SRE chatroom to help with the outage, you ask: "how do you install system packages?" They respond "We never do. We only update our app." Ugh. You find a different server and copy its working /etc/apt config over.
* **4:10pm**: You need to run "apt-get update" first with the fixed config, but it's miserably slow.
* **4:12pm**: ...should it really be taking this long??
* **4:13pm**: apt returned "failed: Connection timed out." Maybe this system is too slow with the performance iss...