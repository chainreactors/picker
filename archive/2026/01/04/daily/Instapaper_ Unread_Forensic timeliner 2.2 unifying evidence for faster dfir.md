---
title: Forensic timeliner 2.2 unifying evidence for faster dfir
url: https://andreafortuna.org/2026/01/04/forensic-timeliner-2-2-unifying-evidence-for-faster-dfir.html
source: Instapaper: Unread
date: 2026-01-04
fetch_date: 2026-01-05T03:52:15.298341
---

# Forensic timeliner 2.2 unifying evidence for faster dfir

[Andrea Fortuna](/)
[ ]

[About](/about/)[Rss](/feed.xml)

# Forensic timeliner 2.2: unifying evidence for faster dfir

Jan 4, 2026

![Forensic Timeliner 2.2 cover](/assets/forensic-timeliner-2-2-cover-2026.jpg)

## Why unified timelines matter now

In incident response, speed is rarely blocked by a lack of data. The bottleneck is the opposite, too many artifacts arriving in incompatible formats, each capturing a narrow slice of behavior. A workstation might produce file system traces, execution evidence, and Windows event logs that are individually useful, but analytically fragmented. That fragmentation turns *temporal coherence* into a manual, error-prone exercise, especially when multiple tools output separate CSVs that do not share field names, time zones, or even consistent semantics.

This is the core problem space **Forensic Timeliner** targets: ingesting heterogeneous forensic exports and producing a single, navigable chronology that an analyst can filter and review without spending hours on spreadsheet plumbing. The project’s scope is unusually pragmatic, it meets practitioners where the data already is, in the CSV outputs of widely used tooling, and it documents supported formats in the upstream [Forensic Timeliner repository](https://github.com/acquiredsecurity/forensic-timeliner) in a way that encourages repeatable workflows rather than one-off scripts.

![Unified timeline pipeline](/assets/forensic-timeliner-unification-pipeline.svg)

The journalistic significance of this approach is not the novelty of timelines, the discipline has relied on chronology for decades, but the operational shift it enables. When a team can move from “collect outputs” to “see the whole story” quickly, triage improves, handoffs become cleaner, and the investigation is less likely to get stuck in the seams between tools.

## What changes in version 2.2

Version 2.2 continues the tool’s high-performance direction while focusing on usability, a strategic choice in a field where sophisticated capabilities often fail to land because the interface is too brittle under pressure. The release is maintained in C# on **.NET**, a platform choice that aligns with many enterprise environments, and it benefits from the ecosystem’s maturity around packaging and cross-platform execution. In practical terms, it means analysts can keep tooling closer to standard pipelines, while still gaining a specialized engine for timeline unification.

The most visible refinement is in the interactive mode. New prompts allow investigators to preview how filters will be applied to sensitive artifact families such as MFT-derived data and Windows event logs. This matters because filtering is where analysts can unintentionally discard context. A guided preview makes *defensible scoping* easier, and it also makes peer review more realistic, since a colleague can understand what was included and excluded without reverse-engineering a command line.

Under the hood, **.NET 9** provides a modern runtime foundation, and its engineering choices are documented in the official [Microsoft .NET documentation](https://learn.microsoft.com/dotnet/) that many SOC engineering teams already use for adjacent tooling. In 2.2, the interactive previews are rendered via **Spectre.Console**, which is a small detail with outsized impact, clear tables reduce the cognitive load of verifying filters, tags, and configuration assumptions when time is scarce.

## From csv sprawl to investigative signal

The value of an aggregated timeline is not just being able to sort by timestamp. It is about adding structure that supports investigative questions, “what changed right before persistence was established?”, “which account activity preceded lateral movement?”, “what execution traces correlate with a suspicious network login?”. Tools integrated into the workflow reflect those questions. For instance, event-log hunting outputs from **Chainsaw** can align with the tactics and techniques used in **MITRE ATT&CK**, and the framework’s canonical matrix is available directly at [**MITRE ATT&CK**](https://attack.mitre.org/) while the analysis remains grounded in local evidence.

Forensic Timeliner’s model keeps the original provenance in view while also normalizing fields so that different sources can be queried consistently. That duality is essential. A normalized row makes correlation possible, but the link back to “where this came from” is what keeps the timeline admissible and the conclusions accountable.

A notable element in 2.2 is the emphasis on *keyword tagging*. Tagging is not a replacement for detection logic, yet it is a powerful way to accelerate pivoting across noisy timelines, especially when teams standardize tag groups in a shared `keywords.yaml`. The new interactive option to enable tagging and generate a session file for **Timeline Explorer** pushes the workflow one step closer to an analyst’s daily reality, opening a curated view, already labeled, instead of dumping a raw export into a generic spreadsheet.

![Tagging and filtering workflow](/assets/forensic-timeliner-tagging-and-filters.svg)

## Operational adoption, limits, and next steps

Tools that unify data tend to fail when they promise too much automation and hide too many assumptions. The strength of Forensic Timeliner is that it stays explicit about configuration. Discovery rules and filters are controlled via YAML, which makes the process auditable, and it acknowledges that some sources demand conventions, for example, customized outputs from **Hayabusa** require consistent naming so the right parser can be applied.

Interoperability is another quiet feature that matters. The timeline can be exported as CSV compliant with **RFC 4180**, enabling analysts to move between tools without losing basic structure, and the specification itself is maintained at the [RFC Editor](https://www.rfc-editor.org/rfc/rfc4180), which is a useful reference when teams must guarantee that downstream ingestion, whether in **Excel** or a SIEM enrichment pipeline, behaves predictably. The option to include raw source rows (even as an experimental capability) is also an important safeguard, it helps preserve context when investigators need to justify why a normalized field looks a certain way.

There are still limits that teams should treat as part of the tradecraft. Timestamp normalization can reduce confusion, but it cannot fix missing clocks, inconsistent time zones, or artifacts with ambiguous semantics. Deduplication can reduce clutter, but it can also erase “repetition as evidence” if applied uncritically. Treating the workflow as *reproducible analysis*, with reviewed configurations and documented assumptions, is what turns a unified timeline from a convenience into a reliable investigative substrate.

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)

## Andrea Fortuna

* Andrea Fortuna
* andrea@andreafortuna.org

* [andreafortuna](https://github.com/andreafortuna)
* [andreafortunaig](https://instagram.com/andreafortunaig)
* [andrea-fortuna](https://www.linkedin.com/in/andrea-fortuna)
* [andrea](https://social.privacytools.click/%40andrea)
* [andreafortunatw](https://www.twitter.com/andreafortunatw)

Cybersecurity expert, software developer, experienced digital forensic analyst, musician