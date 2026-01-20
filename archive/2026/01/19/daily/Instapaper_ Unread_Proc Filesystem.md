---
title: Proc Filesystem
url: https://andreafortuna.org/2026/01/19/proc-filesystem.html
source: Instapaper: Unread
date: 2026-01-19
fetch_date: 2026-01-20T03:35:20.880239
---

# Proc Filesystem

[Andrea Fortuna](/)
[ ]

[About](/about/)[Rss](/feed.xml)

# Peeking into /proc: turning live Linux data into evidence

Jan 19, 2026

After a long stretch of management talk and incident playbooks, it feels good to get my hands dirty again.

![Cover: /proc live artifacts for DFIR](/assets/2026/proc-filesystem-cover.jpg)

This round is about Linux internals, and more precisely the `/proc` virtual filesystem, because a well-run forensic workflow can turn that volatile, live process data into structured evidence you can actually review.

## /proc as a live kernel interface

If you want the authoritative semantics of each file, keep the [kernel documentation](https://docs.kernel.org/filesystems/proc.html) open while you read this.

![/proc as a live kernel interface](/assets/2026/proc-kernel-interface.svg)

The first thing to remember is that `/proc` is not a regular folder, it is a pseudo-filesystem where the kernel exposes its state through a filesystem-like interface. When a tool reads `/proc/meminfo` or `/proc/cpuinfo`, it asks the kernel to generate current state on the spot, which is why it can feel “weird” the first time you treat it like a normal directory. If you want a friendly, hands-on explanation, [Fernandovillalba’s walkthrough](https://fernandovillalba.substack.com/p/a-journey-into-the-linux-proc-filesystem) is a great companion.

This design is practical: user space gets a consistent way to query kernel and process data without a custom API for every little thing. It is also why `/proc` shines during incident response, because it is tied to what is running right now.

A few global paths under `/proc` routinely show up in forensic triage:

* `/proc/meminfo`, the detailed memory stats (free, cached, buffers, swap, and a lot more).
* `/proc/modules`, the live list of loaded modules, handy when you want to spot unexpected drivers or rootkit tricks; the [Velociraptor artifact notes](https://docs.velociraptor.app/artifact_references/pages/linux.proc.modules/) cover it if you use Velociraptor in your fleet.
* `/proc/net/*`, a cluster of files that describe sockets, protocol tables, and active connections.

Even before diving into individual processes, these files sketch the baseline: is the system under pressure, which subsystems are active, and does anything look “off” compared to the usual profile.

If you are building a broader Linux IR checklist, the [Magnet Forensics overview](https://www.magnetforensics.com/blog/linux-forensics-artifacts-every-investigator-should-know/) is a good reference point, and it pairs nicely with `/proc` because it reminds you what to grab when you have time.

## Process directories, the core of /proc

The real treasure is under `/proc/<PID>/`, one directory per running process. Here `/proc` stops being a generic status board and turns into a way to reconstruct concrete behavior: which binary is running, with which arguments, in which environment, and with which resources open.

![Inside /proc/](/assets/2026/proc-pid-anatomy.svg)

A practical, process-centric triage usually revolves around a handful of entries.

**Executable identity and provenance**

`/proc/<PID>/exe` is a symlink to the executable mapped as the process image, and it is usually the quickest answer to “what is really running here”. Names can mislead, both by accident (wrappers, launchers) and by design (masquerading).

`/proc/<PID>/cmdline` shows the arguments (null-separated), and it is great for reconstructing how something was launched and which flags may change its behavior. In the wild it is often how you spot odd patterns, like interpreters with inline payloads or binaries running from directories that should never host executables, the kind of detail highlighted in Fernandovillalba’s writeup.

**Environment variables as configuration and leakage**

`/proc/<PID>/environ` reads like a configuration snapshot. It often carries hints about deployment context (service manager, container, CI) and, sometimes, secrets that should not be there, because plenty of apps still take credentials from environment variables, a risk the kernel docs quietly remind us of.

From a defensive angle, env vars help for two reasons. They explain behavior that otherwise looks weird (proxy configs, debug flags, library path overrides), and they expose abuse, because variables like `LD_PRELOAD` or custom library paths can hijack execution flow.

**Open file descriptors and “what this process touches”**

`/proc/<PID>/fd/` is a directory of symlinks, one per open file descriptor, resolving to everything the process has open, from files to pipes to sockets. If you need to know which process is writing to a file or why a log keeps getting truncated, `fd/` is usually the fastest clue, as shown in Fernandovillalba’s examples.

The key is that file descriptors are live handles to resources. Spotting a suspicious binary is one thing; seeing it also holds an outbound socket and a credential file makes it a story you can act on, which is why the kernel reference treats `fd/` as first-class evidence.

## Memory insights without a full memory dump

It is tempting to think memory forensics always means a full RAM dump, but `/proc` already offers a lot of memory metadata you can use right away. Host-level views like `/proc/meminfo` give you the pressure snapshot (swapping, thrashing, sustained load).

At the process level, files like `/proc/<PID>/maps` and `/proc/<PID>/smaps` describe mappings, permissions, and per-region stats. Those details help flag oddities such as unexpected executable mappings or writable-and-executable regions.

There is a pragmatic angle too. When a server is unstable or starved for memory, correlating host pressure with specific processes and their mappings shrinks the “what is happening” phase.

## Turning /proc into structured evidence with an artifact parser

Reading `/proc` by hand is fine when the box has ten PIDs and one question. With hundreds of processes, containers, and short-lived jobs, manual browsing gets messy.

A dedicated artifact parser helps here: it ingests collected `/proc` data, normalizes it, and turns it into a dataset you can sift. One option is Linux Artifact Parser (LAP), which you can find on [SourceForge](https://sourceforge.net/projects/linux-artifact-parser/) if you want to evaluate it.

LAP is GUI-focused and includes a module for the `/proc` virtual filesystem. The module does not invent new facts; it correlates what `/proc` already exposes and does it at scale across all captured processes.

![Workflow: collect /proc and analyze with LAP](/assets/2026/lap-proc-workflow.svg)

Where it really helps, at least in my experience, is the boring part of incident work: reducing the time you spend navigating and the number of times you have to repeat the same checks.

For example, instead of jumping between `/proc/<PID>/cmdline`, `/proc/<PID>/fd/`, `/proc/<PID>/environ`, and `/proc/net/*` for a dozen different processes, you can start from a process table and work your way down. That changes the flow of the analysis.

Typical things I look for when I have a `/proc` dataset loaded into a tool like LAP:

* Processes with odd provenance (unexpected path, deleted executable, strange parent/child relationships).
* Command lines that explain behavior (inline scripts, suspicious flags, LOLBAS-style abuse on Linux).
* Environment variables that should not exist in production (proxy overrides, `LD_PRELOAD`, credentials in cleartext).
* Open file descriptors that connect the dots (an outbound socket plus access to sensitive files, or a process that keeps a log file open while it is being truncated).

One practical tip: if you plan to use LAP (or any other parser), treat collection as a first-class step. In a real incident, `/proc` changes while you are looking at it. A process can exit, a socket can close, a helper can run and disappear. If you capture too late, you end up doing analysis on a world that no longer exists.

In practical terms, a ...