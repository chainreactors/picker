---
title: MACOBOX is back from San Francisco
url: https://mandomat.github.io/2026-04-15-macobox-new-features/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-15
fetch_date: 2026-04-16T04:54:07.485523
---

# MACOBOX is back from San Francisco

[Home](https://mandomat.github.io/)

* [About Me](/aboutme)
* Search

[![Navigation bar avatar](/assets/img/avatar-icon.png)](https://mandomat.github.io/)

✕

# MACOBOX is back from San Francisco

## AI agents, on-premise inference, IoT scanning and PDF reports: a roundup of the latest features

Posted on April 15, 2026

At the end of March we spent a week in Silicon Valley. We had the chance to sit down with some remarkable people: researchers, builders, founders. Every conversation left us with more questions than we arrived with, in the best possible way. It was one of those rare times when ideas came faster than we could write them down. We came back full of ideas.

![MACOBOX in San Francisco](/assets/img/2026-04-15/SF.jpg)

That energy fed directly into the sprint that followed. MACOBOX comes back from San Francisco with a whole series of new features, the most dense release we’ve shipped so far. The AI side got a major change, a brand new IoT scanning engine landed, and the reporting workflow finally closes the loop from recon to deliverable. Let’s walk through everything in detail.

---

## The AI Agent now covers every interface

The agent originally started as an experiment; a conversational interface built on top of the hardware hacking tools. It could help you with UART. Then SPI. Then eMMC and Logic Analyzer.

With this release, the agent reaches **full interface coverage**: UART, SPI, I2C, JTAG, Logic Analyzer, eMMC; everything you can plug into MACOBOX is now something the agent can reason about and act on. In practice, this means you can describe what you want to do in plain language and let the agent figure out the right sequence of operations: start OpenOCD, send a telnet command, dump the flash, run a hexdump without having to remember the exact steps yourself.

![AI agent covering all interfaces](../assets/img/2026-04-15/agent_interfaces.png)
*The agent handling a JTAG session end-to-end*

This matters especially in the middle of a session when context-switching is expensive. Instead of navigating between pages or recalling the right command syntax, you just ask.

---

## Chat history: your sessions survive a reboot

One persistent frustration with had with our agent was that every session started from scratch. You had a productive exchange with the agent during a JTAG dump last night and today it knows nothing about it.

**Chat history** solves this. Every conversation is now saved as a JSON session on disk, with a searchable index. A sidebar in the agent UI lists all past sessions, ordered by most recent activity. You can pick up where you left off, review what the agent suggested, or revisit a successful workflow and replicate it on a different target.

![Chat history sidebar](../assets/img/2026-04-15/chat_history.gif)
*Browsing and resuming past sessions from the sidebar*

Sessions are stored locally on the device: no cloud, no sync required.

---

## Ollama: run the AI stack entirely on-premise

Until now, MACOBOX’s AI features like photo analysis, text reasoning, the agent… all depended on frontier models. That’s a fine default, but it’s a hard blocker in air-gapped environments, or when you simply don’t want your target’s firmware leaving your lab.

With **Ollama support**, the entire AI stack can now run on your own hardware. You point MACOBOX at an Ollama server (it can be local oßr anywhere on your network), and from that point on all inference happens without touching the cloud.

The configuration lives in **Settings → AI Provider**, where you can:

* Switch between `MACOBOX AI` and `ollama` as the active provider
* Set the Ollama server URL
* Choose separate models for each role: text analysis, vision (PCB/photo analysis), project assistant, and the agent itself
* Test the connection directly from the UI before committing to a target session

![Ollama provider settings](../assets/img/2026-04-15/ollama_settings.png)
*Configuring an on-premise Ollama provider in Settings*

This is a meaningful shift for professional use cases. A capable model like `qwen2.5:14b` running on a workstation in the same room gives you analysis that is fast, private, and reproducible.

---

## Project AI Assistant: an expert that knows your target

The **Project AI Assistant** lives inside each project and is context-aware from the start. When you open a chat, the assistant already has access to everything you’ve collected: dumps, extracted strings, hexdumps, scan results, interface checklists, notes, and any previous cloud analysis runs.

You can ask questions like:

* *“Based on what I’ve dumped, does this look like a vendor-modified Linux?”*
* *“What debug interfaces have I tested so far and what’s still open?”*
* *“Summarize the findings for a report.”*

The assistant never invents data it hasn’t seen, it works strictly from the project context you’ve built up.

![Project AI assistant](../assets/img/2026-04-15/project_ai_chat.png)
*Chatting with the project assistant about a target device*

Project chat sessions are also persisted, so you can have a long-running conversation that spans multiple lab sessions.

---

## PDF reports with brand styles

MACOBOX has had scan reports for a while, but the new **PDF report generator** is different. It takes the full project like findings, dumps, checklists, interface notes, cloud analysis summaries and compiles them into a professional-grade security assessment document.

The workflow is simple: go to your project, hit *Generate Report*, select the sections you want to include, and pick a style. Out comes a structured PDF with a cover page, table of contents, findings summary, and all the supporting artifacts.

On the styling side, two paths are available:

* **Mindstorm preset**: the default, using the Mindstorm brand palette.
* **Custom**: upload your own logo and define primary/accent colors. The report engine picks up the palette automatically and applies it to headers, tables, and cover page.

![PDF report wizard](../assets/img/2026-04-15/project_report.png)
*The offline PDF wizard with brand style selection*

The report is generated entirely offline no cloud dependency, no upload of your findings anywhere.

---

## New JTAG UI

The JTAG page got a full redesign. The previous version was functional but navigating it mid-session (especially on the touchscreen) was clunky.

The new layout is cleaner and better organised around the actual workflow: connect, configure, control, collect. Config files are easier to browse, the OpenOCD output is more readable, and the dump progress is visible inline rather than buried in logs.

One specific addition worth highlighting: **chip configuration search**. OpenOCD ships with hundreds of target config files for different chips and boards. Finding the right one used to mean leaving MACOBOX and digging through documentation. You can now search the scripts library directly from the JTAG page, preview the config file content, and load it into your session without ever leaving the UI.

![New JTAG UI](../assets/img/2026-04-15/jtag_ui.gif)
*Searching for a chip config file in the new JTAG interface*

---

## IoT Network Scanner

This is the biggest new surface area in this release. The **IoT Network Scanner** is a dedicated tool for discovering and profiling devices on the same network as MACOBOX.

When you kick off a scan, the engine (advanced or standard) runs host discovery and port scanning across your subnet. For each device it finds, it presents:

* Open ports and running services
* MAC address and OUI vendor lookup
* A **hardware profile panel** that surfaces likely SoC candidates, debug interface information (UART, JTAG, SPI), extraction method suggestions, and links to FCC ID records, OpenWRT wiki pages, and community documentation… all without leaving the tool

![IoT scanner hardware profile](../assets/img/2026-04-15/iot_scanner_profile.gif)
*The hardware profile panel for a discovered device*

Devices can be saved directly to a MACOBOX project. Once saved...