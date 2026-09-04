---
title: Cheatsheet: Threat Attribution in Threat Intelligence - root@fareed:~#
url: https://fareedfauzi.github.io/cheatsheets/threat-attribution/
source: Over Security
date: 2026-09-03
fetch_date: 2026-09-04T06:43:50.021638
---

# Cheatsheet: Threat Attribution in Threat Intelligence - root@fareed:~#

xml version="1.0" standalone="no"?

[root@fareed:~#](/ "Personal blog for research, education and note purpose.
")

* [Cheatsheets](/cheatsheets.html)
* [Archive](/archive.html)
* [About](/about.html)

# Cheatsheet: Threat Attribution in Threat Intelligence

* [Threat-Intelligence](/archive.html?tag=Threat-Intelligence)

* Aug 16, 2025

Hey yow. What’s up? It’s been a year since I wrote anything in my blog. I came up with this idea for a blog topic when my ex-junior asked me, “*Yed, how can we attribute a malware to a threat actor?*” Then I remembered the first time I had to do it and asked the same question to myself at my current job.

Today, malware reversing and threat intelligence becane my day-to-day tasks. When I first joined my current employer, I was a pure malware analyst with basically zero knowledge of TI. But still, I had to do threat attribution whenever I worked on malware or threat research.

As a first-timer in this whole threat intelligence scene, I honestly found attribution really tough. It felt overwhelming at the start. But after a year, reading a bunch of books, and constantly asking my senior teammates for guidance, I’ve managed to put together a few points on how we can attribute a piece of malware or a campaign to certain threat groups.

That said, I’m still a noob even today. So this guide isn’t 100% correct. It’s just based on what I’ve read, what I’ve seen at work, and what I’ve learned from others. So, let’s go through a few aspects that can be used for threat attribution in threat intelligence. But, before that, let’s talk about several importants code of conducts in threat attribution.

# Code of conducts

1. **Stick to evidence, not guesses**. Assumptions can guide your analysis, but they should never be the foundation of your attribution.
2. **Attribution takes time**. It’s rarely quick, sometimes it takes years of tracking and connecting the dots.
3. **One clue isn’t enough**. An IP, a string, or a single sample won’t cut it. Always cross-check with multiple data points using your internal data or maybe ask other researchers.
4. Track the **bigger picture**. Document attack timelines, overlaps between campaigns, and differences in malware versions.
5. **Actors change**. Groups evolve their tools and sometimes shift their targeting, so keep an eye on how they grow over time.
6. **Expect deception**. Advanced actors may deliberately leave behind false trails to mislead investigators.
7. Attribution to a specific actor = hard.
8. Attribution to a government/nation = way harder. Why?
   * Use front companies, proxies, or criminal affiliates
   * Naming a country can trigger diplomatic, legal, or military consequences.
   * Public reports are often toned down. That’s why you’ll often see phrasing like “likely linked to Chinese state interests” instead of direct blame.
9. **Know when to stop**. Usually, attribution ends at the actor-level (e.g., APT29), and you should always state your confidence level.
   * Use confidence ratings clearly:
     + Low = weak evidence, too many gaps.
     + Moderate = some solid evidence with supporting context.
     + High = strong, consistent, and well-corroborated evidence.
10. **Be transparent**. Always explain what’s based on evidence, what’s assumption, and how you reached your conclusion.
11. **Don’t overstate**. Use careful wording like “likely,” “possibly,” or “with moderate confidence” instead of making it sound absolute.

# What usually you need to conduct threat attribution?

1. A LOT of telemetry and dataset. Attribution isn’t possible without a big pool of telemetry and evidence.
   * Endpoint
   * Network
   * Logs
   * Samples
2. A collection of previous samples and campaign data helps you spot code overlaps and recurring TTPs.
3. Knowledge and experience about the samples, group, campaign. The more you’ve worked with certain malware families, groups, or campaigns, the easier it is to recognize patterns and connect dots. Yeah, it’s a long term game my friend.
4. Threat intelligence feeds and reports
   * Threat intel reports (public and private)
   * Free/Commercial feeds
   * Sharing groups and communities
   * Blog-posts

# Threat Attribution Checklist

Below is a checklist you can use as a reference for threat attribution. For each item, you’ll need to decide whether it supports attribution with weak, moderate, or high confidence depending on the quality and amount of evidence you have.

![](https://github.com/user-attachments/assets/67a76258-f63d-4ce5-bf3b-2b2901054542)

## [1] Malware, Toolset, and Code Analysis

### Sample Similarities

* VirusTotal (VT) hunting and lookup: Use VT to check relations, comments, and prior submissions. This often reveals reuse across campaigns.
* Build or use Machine Learning algorithm to find sample similarities.

For example, using lookup or YARA hunting in VT can helps you find more samples.

![](https://github.com/user-attachments/assets/4c840c56-dc15-46e0-9085-3f0bfde7bc3a)

### Code Features & Style

* Binary diffing (Diaphora): Compare samples to see code overlaps or reused functions.
* Function naming: Custom names or weird naming conventions may persist across builds.
* Function structure & logic reuse: Attackers often recycle code logic, even across different malware families.
* Compilation timestamps: Look for consistent build times (e.g., always compiled during certain working hours).
* Internal versioning/build clues: Strings like `ver 1.0.3` or compiler artifacts may tie samples together.
* Project structure remnants: Artifacts from IDEs (e.g., Visual Studio paths).
* Code paths & import tables: Repeated API usage or unusual imports can suggest the same developer.

With Diaphora, you can compare code to identify updates, spot similar variants, or even attribute samples to specific threat actors.

![](https://github.com/user-attachments/assets/8e1b5f8a-408f-4d2c-a2b4-59441e551f61)

For example, early WannaCry (February 2017) shares nearly identical code with Lazarus malware from 2015, known as Contopee.

![](https://github.com/user-attachments/assets/e1a29248-c22f-4f22-bf50-c68316829beb)

### Detection Names

* Threat Intelligence Platforms: Check how the sample has been labeled across platforms.
* VirusTotal relations & behavior: Explore relation graphs, lookup results, and sandbox behavior.

Detection names in VirusTotal (VT) can provide useful context about the malware you are analyzing.

![](https://github.com/user-attachments/assets/e03e4f6a-6ebd-4f1c-8791-e2de47610a7b)

Additionally, the VT Community can also help in identifying the specific variant of a sample.

![](https://github.com/user-attachments/assets/41a49e08-a26e-485f-bedc-90ab4efca0f5)

### PDB Paths

* Leaked developer usernames or paths: PDB files sometimes reveal usernames, directories, or internal project names.

### Build Artifacts

* Builder leaks: If a malware builder leaks, compare generated samples.
* Stager styles: Early-stage loaders (stagers) often have unique patterns.
* Custom or reused packers: Threat groups sometimes rely on their own packers.
* Section naming patterns: Strange or repeated section names (`.abcd`, `.xyz`) can link samples.
* Overlay data: Additional data stored after the PE file can be unique to a group.

### String & Resource Analysis

* FLOSS: Use FLOSS to extract hidden/obfuscated strings.
* Embedded configuration: Config files (JSON, XML, encrypted blobs) may reveal hardcoded C2s or campaign IDs.
* Hardcoded C2s, usernames, commands: Reuse of infrastructure or operator nicknames.
* Resource metadata & entropy: Check icons, images, or version info fields.
* Interesting strings: Custom error messages, debug logs, or memes.
* Unusual resources: Embedded DLLs, HTML files, or executables with unique traits.

Examples of similar strings can be found in many variants of the Talos Trojan, also known as QReverse.

![](https://github.com/user-attachments/assets/425b3207-0564-4a47-90b7-ee0c5a18ae04)

### Anti-analysis Techniques

* ...