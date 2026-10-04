---
title: The boring state of stalled timelines…
url: https://www.hexacorn.com/blog/2026/10/03/the-boring-state-of-stalled-timelines/
source: Hexacorn
date: 2026-10-03
fetch_date: 2026-10-04T07:37:54.003753
---

# The boring state of stalled timelines…

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2026/10/02/etwcheckcoverage-api/)

# The boring state of stalled timelines…

Posted on [2026-10-03](https://www.hexacorn.com/blog/2026/10/03/the-boring-state-of-stalled-timelines/ "11:35 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

The subject of timelines & supertimelines used to dominate many discussions in the digital forensic world… 10-15 years ago. At that time the concept of temporal proximity was super hot and for a good reason – once you put events in a chronological order you can quickly draw conclusions and easily explain what happened.

Today this topic is kinda dead because many modern forensic and EDR/XDR tools do a great job democratizing and commoditizing the concept of timelines, and these simply became a part of what we can call ‘the business as usual’.

BUT

I believe there is still more to it, so much more that I decided to write a longer post about it.

In 2012 I described a Windows file system-based [PE files clustering technique](https://www.hexacorn.com/blog/2012/09/01/perfect-timestomping-a-k-a-finding-suspicious-pe-files-with-clustering/) that relies on PE file compilation timestamps to detect suspicious executables. While the newer Windows versions (10+) use the very same PE file field for a [different purpose (reproducible builds)](https://devblogs.microsoft.com/oldnewthing/20180103-00/?p=97705/) there is still some merit to this technique for non OS PE files found on the system.

In 2015 I introduced a new analysis technique that I called [filighting](https://www.hexacorn.com/blog/2015/04/10/introducing-filighting-and-the-future-of-dfir-tools/). The idea relies on targeted file content analysis focused on installed software packages. The assumption being that all the files belonging to the (atomically) installed software somehow reference each other, at least once. My hypothesis was that by mapping these internal cross-references one can quickly find outliers (possibly malicious files residing in the software’s directory; potential supply chain-attacks). A few follow-up posts demonstrated a visual representation of inter-file connections found in many popular software packages, rendered with a help of d3 library.

10-15 years ago forensic analysis relied on running many separate tools to extract the content/data of many forensic artifacts, individually. Today’s forensic tools often take care of these in an uniform way and simply parse and extract data + put these extracted information pieces on a timeline… This is all cool, but it doesn’t take into account the complexity of today’s ecosystems.I want forensic tools to start clustering these atomic data points a bit more.

The presence of EDR’s telemetry, the .bash\_history files and their backups, the auditd and sysmon logs are now a norm. We can also easily take snapshots of file system’s metadata for Windows, Linux and macOS. What these snapshots often tell us in 2026 is that unlike in 2000s, many systems today are often set up not from the scratch but by leveraging massive ‘copy events’ where old data from an old file system X is being blindly copied to a new file system Y. Such activity introduces a lot of challenges to digital forensic professionals who see file system-based timelines that are often massively distorted.

Additionally, many (primarily) Linux systems hosting web sites end up (over time) with many copies of the same website content spread across many similarly looking directories. A proper (and automatic) timeline analysis should detect these clusters of similarly-looking files spread across many ‘backup’ directories. Such analysis may help to immediately highlight files added / changed in different iterations of the same directory (e.g. web shells or files uploaded via file upload vulnerability).

There is also the issue of systems/endpoints heavily utilized by legitimate, authorized internal security teams. Analysis of such systems pose a huge challenge as many activities observed on these systems usually correspond with legitimate activities of internal soc, pentesting, red team operators.

I guess the point of this post is that our timelines need more juice.

The EDR/XDR telemetry is very metadata-centric, but DFIR-access level gives us all the content we need. So, when a forensic software is analysing the file system I want it to find more than just known-knowns. This is the easy bit. I want it to explore use cases where someone copied many files, someone created a copy of another directory, where potential TA uploaded web-shells, even if they cannot be executed, where company employees hone their tradecraft, run offensive tools, do stupid but explainable stuff, where they bypass security controls, harmlessly download and analyze malware, use bad tools for a good reason, and so on and so forth.

I want timelines to be presented as clusters of activity, with attribution and with perceived intent.

This entry was posted in [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/), [Preaching](https://www.hexacorn.com/blog/category/preaching/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2026/10/03/the-boring-state-of-stalled-timelines/ "Permalink to The boring state of stalled timelines…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")