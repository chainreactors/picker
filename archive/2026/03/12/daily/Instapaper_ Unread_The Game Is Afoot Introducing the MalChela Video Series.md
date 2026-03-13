---
title: The Game Is Afoot Introducing the MalChela Video Series
url: https://bakerstreetforensics.com/2026/03/11/the-game-is-afoot-introducing-the-malchela-video-series/
source: Instapaper: Unread
date: 2026-03-12
fetch_date: 2026-03-13T04:07:58.929835
---

# The Game Is Afoot Introducing the MalChela Video Series

[Skip to content](#content)

[Baker Street Forensics](https://bakerstreetforensics.com/)

Where Irregulars are part of the Game

Menu

* [Blog](https://bakerstreetforensics.com/blog/)
* [Links, Resources & Swag](https://bakerstreetforensics.com/resources/)

[![](https://bakerstreetforensics.com/wp-content/uploads/2022/05/output-onlinepngtools-4.png)](https://bakerstreetforensics.com/)

# The Game Is Afoot: Introducing the MalChela Video Series

[DFIR](https://bakerstreetforensics.com/category/dfir/), [Malware](https://bakerstreetforensics.com/category/malware/), [Memory Analysis](https://bakerstreetforensics.com/category/memory-analysis/), [MITRE ATT&CK](https://bakerstreetforensics.com/category/mitre-attck/), [REMnux](https://bakerstreetforensics.com/category/remnux/), [Rust](https://bakerstreetforensics.com/category/rust/), [SIgma](https://bakerstreetforensics.com/category/sigma/), [Triage](https://bakerstreetforensics.com/category/triage/), [yara](https://bakerstreetforensics.com/category/yara/)

There’s a moment every analyst knows — the one where an unknown file lands on your desk and the clock starts ticking. You need answers, and you need them fast. MalChela was built for exactly that moment.

Today I’m excited to announce the **MalChela Video Series** on YouTube — a growing collection of tutorial episodes walking through real malware analysis workflows using [MalChela](https://github.com/dwmetz/MalChela), the open-source Rust-based toolkit I’ve been building for the DFIR community. Whether you’re new to the tool or already running it in your lab, there’s something here for you.

Four episodes are available right now in the playlist.

---

## What’s in the Playlist

### Ep0 | Installation & First Run

Every case starts somewhere. Episode 0 is your onboarding — installing MalChela, walking through its dependencies, and getting oriented with both the CLI and GUI modes. If you’ve been curious about the tool but weren’t sure where to start, this is the episode to bookmark.

---

### Ep1 | First Contact: Hash, Inspect, Identify

You’ve just been handed a suspicious file. What do you do first?

This episode covers the first three tools in a malware triage workflow — the exact sequence I reach for every time I encounter an unknown file:

* **hashit** — generate MD5, SHA1, and SHA256 hashes to protect chain of custody and enable deduplication
* **fileanalyzer** — static inspection: entropy analysis, PE header fields, compile timestamps, and import tables
* **malhash** — simultaneous lookup against VirusTotal and MalwareBazaar to identify known malware families

By the end of this episode, you’ll take an unknown file from zero to confirmed malware family identification in under five minutes — no sandboxing required.

---

### Ep2 | From Strings to Signatures

Continuing from Episode 1, we go deeper into the confirmed RedLine info-stealer sample using **mStrings** — MalChela’s string extraction engine. Unlike the traditional `strings` utility, mStrings runs every extracted string through a detection ruleset and MITRE ATT&CK mapping layer simultaneously, turning raw output into actionable intelligence.

We walk through 62 detections, including PDB path artifacts, hard-coded dropper filenames, WMI queries, credential harvesting patterns, anti-debug checks, and a code injection setup. We then feed the extracted IOCs into **Strings2YARA** to auto-generate a structured YARA rule — and confirm it fires against the sample using File Analyzer.

By the end, you’ll be reading a malware file not as a pile of strings, but as a window into the attacker’s tradecraft.

---

### Ep3 | REMnux Mode & Custom Tools

MalChela doesn’t work in isolation. Episode 3 covers how to extend the toolkit through the `tools.yaml` config file and how enabling REMnux mode surfaces an entire distro’s worth of malware analysis utilities directly within MalChela’s interface.

We also explore three built-in integrations: **Volatility 3** with a dynamic plugin builder, **T-Shark** with a searchable reference, and **YARA-X** — a faster, Rust-native rewrite of YARA.

---

## What’s Coming

The series is ongoing. Future episodes will push further into advanced workflows — think directory-scale triage, corpus management, and the AI-assisted analysis capabilities introduced in MalChela’s MCP integration. Stay subscribed and you won’t miss them.

---

## Get Involved

If MalChela is useful in your work, the best thing you can do is help spread the word:

* 📺 **[Subscribe to the YouTube channel](https://www.youtube.com/%40BakerStreetForensics?sub_confirmation=1)** — Subscribe to the channel and save the playlist so you don’t miss new episodes as they land.
* 📖 **Follow Baker Street Forensics** — Writeups, major releases, and workflow deep dives live here.
* 💬 **Share and comment** — If an episode clicks for you, pass it along to a colleague or drop a comment on the video. That feedback genuinely shapes what comes next.

The game is afoot. Let’s get to work.

---

*MalChela is open-source and freely available. Find the project on [GitHub](https://github.com/bakerstreetforensics/MalChela).*

### Share this:

* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://bakerstreetforensics.com/2026/03/11/the-game-is-afoot-introducing-the-malchela-video-series/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://bakerstreetforensics.com/2026/03/11/the-game-is-afoot-introducing-the-malchela-video-series/?share=reddit)
* [Share on Bluesky (Opens in new window)
  Bluesky](https://bakerstreetforensics.com/2026/03/11/the-game-is-afoot-introducing-the-malchela-video-series/?share=bluesky)
* [Share on Mastodon (Opens in new window)
  Mastodon](https://bakerstreetforensics.com/2026/03/11/the-game-is-afoot-introducing-the-malchela-video-series/?share=mastodon)

Like Loading...

### *Related*

[March 11, 2026](https://bakerstreetforensics.com/2026/03/11/the-game-is-afoot-introducing-the-malchela-video-series/) [Doug Metz](https://bakerstreetforensics.com/author/dwmetz/)[DFIR](https://bakerstreetforensics.com/tag/dfir/), [Forensics](https://bakerstreetforensics.com/tag/forensics/), [Github](https://bakerstreetforensics.com/tag/github/), [MalChela](https://bakerstreetforensics.com/tag/malchela/), [Malware](https://bakerstreetforensics.com/tag/malware/), [Memory](https://bakerstreetforensics.com/tag/memory/), [yara](https://bakerstreetforensics.com/tag/yara/), [YouTube](https://bakerstreetforensics.com/tag/youtube/)

## Leave a comment [Cancel reply](/2026/03/11/the-game-is-afoot-introducing-the-malchela-video-series/#respond)

Δ

## Post navigation

[Previous Previous post: MalChela Meets AI: Three Paths to Smarter Malware Analysis](https://bakerstreetforensics.com/2026/03/03/malchela-meets-ai-three-paths-to-smarter-malware-analysis/)

Search for:

* [GitHub](https://github.com/dwmetz)
* [Mastodon](https://infosec.exchange/%40dwmetz)
* [Link](https://linktr.ee/dwmetz)
* [Twitter](https://twitter.com/dwmetz)
* [LinkedIn](https://www.linkedin.com/in/dwmetz/)

## Recent Posts

* [The Game Is Afoot: Introducing the MalChela Video Series](https://bakerstreetforensics.com/2026/03/11/the-game-is-afoot-introducing-the-malchela-video-series/)
  March 11, 2026
* [MalChela Meets AI: Three Paths to Smarter Malware Analysis](https://bakerstreetforensics.com/2026/03/03/malchela-meets-ai-three-paths-to-smarter-malware-analysis/)
  March 3, 2026
* [Streamline Malware Hash Search with FOSSOR](https://bakerstreetforensics.com/2026/02/10/streamline-malware-hash-search-with-fossor/)
  February 10, 2026
* [Enhancing Malware Analysis with REMnux and AI](https://bakerstreetforensics.com/2026/02/09/enhancing-malware-analysis-with-remnux-and-ai/)
  February 9, 2026
* [2025 Year in Review: Open Source DFIR Tools and Malware Analysis Projects](https://bakerstreetforensics.com/2025/12/05/2025-year-in-review-open-source-dfir-tools-and-malware-analysis-projects/)
  December 5, 2025

[Website Powered by WordPress.com]...