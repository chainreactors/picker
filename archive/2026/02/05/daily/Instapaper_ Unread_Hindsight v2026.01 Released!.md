---
title: Hindsight v2026.01 Released!
url: https://dfir.blog/hindsight-v2026-01/
source: Instapaper: Unread
date: 2026-02-05
fetch_date: 2026-02-06T04:10:20.677532
---

# Hindsight v2026.01 Released!

[![dfir.blog](https://dfir.blog/content/images/2019/01/logo.png)](https://dfir.blog)

* [Unfurl](https://dfir.blog/unfurl/)
* [Hindsight](https://dfir.blog/hindsight/)
* [Visualizations](https://dfir.blog/tag/visualizations/)
* [Open Source](https://dfir.blog/tag/open-source/)
* [Presentations & Interviews](https://dfir.blog/tag/media/)

[Hindsight](/tag/hindsight/)

# Hindsight v2026.01 Released!

Hindsight v2026.01 brings new features, including parsing Sync Data, an updated terminal interface, improved output formats, and dozens of fixes and enhancements.

* [![Ryan Benson](/content/images/size/w100/2024/05/30110948-q3l_NL32.jpg)](/author/ryan/)

#### [Ryan Benson](/author/ryan/)

Feb 4, 2026
• 2 min read

![Hindsight v2026.01 Released!](/content/images/size/w2000/2026/02/hindsight-cli.png)

## Sync Data Parsing

A new feature that I'm excited to about in this release is parsing of Chrome's Sync Data. When a user signs into Chrome with their Google account, Chrome can sync bookmarks, passwords, extensions, history, and more across devices.

This sync functionality stores data locally in LevelDB files, and Hindsight can now parse it - at least partially. Most of the LevelDB records hold data encoded in different protobufs, many of which Hindsight now parses. The *meaning* and function of these parsed records is definitely an area for further research, as there is a wealth of information in the data. Hindsight currently only parses out what devices were used for syncing and enhances the existing "Source" column in the timeline with details about the originating device for synced URL visits:

![](https://dfir.blog/content/images/2026/02/hindsight-sync-source.png)

## Updated Terminal Interface

Hindsight's terminal interface has been largely unchanged for almost 10 years (!?) now, and it showed. Hindsight now uses the `rich` library to provide a much more polished command-line interface, while still keeping with the spirit and style of the original version. This is mostly a cosmetic change; the command line syntax remains the same.

![](https://dfir.blog/content/images/2026/02/hindsight-rich-cli.gif)

Hindsight's updated terminal interface

## New Artifacts & Expanded Parsing

Beyond Sync Data, v2026.01 adds parsing for several other Chrome artifacts:

* **Permission Actions** from the Preferences file, showing what permission requests websites have made
* **Login Data For Account** database, used for account-specific saved credentials in recent Chrome versions
* **Account Capabilities** from Preferences, translated into human-readable descriptions
* **Parsing for more timestamped values in Preferences,** as there are many top- or second-level keys that just hold a timestamp and are easy to parse

## Improved Output Formats

All three output formats (XLSX, JSONL, and SQLite) received improvements in this release. The SQLite output in particular was overhauled to be more comparable to the other formats, making it easier to work with Hindsight data in your tool of choice. The JSONL output, which was introduced to make it easier to import Hindsight results into [Timesketch](https://timesketch.org/?ref=dfir.blog), previously only had timestamped records. It now includes all records; those without any intrinsic timestamp (like various storage items) have their timestamp set to the Unix epoch and a timestamp description of "Not a time".

## More Robust Parsing

There are over a dozen fixes and improvements to make Hindsight's parsing more reliable and complete:

* Updated parsing for changes in Chrome v142's DIPS records
* New danger types and interrupt reason codes for download records
* Better handling of extension version strings and preference timestamps
* More tolerant File System logical path creation
* Improved file-closing and resource management

## Get Hindsight!

You can get Hindsight, view the code, and see the full change log on [GitHub](https://github.com/obsidianforensics/hindsight?ref=dfir.blog). Both the command line and web UI versions of this release are available as:

* compiled exes attached to the [GitHub release](https://hindsig.ht/release?ref=dfir.blog) or in the dist/ folder
* .py versions are available by `pip install pyhindsight` or downloading/cloning the [GitHub repo](https://hindsig.ht/github?ref=dfir.blog).

[![Unfurl 2025.03](/content/images/size/w600/2025/03/unfurl-google-udm-3.png)](/unfurl-parses-googe-udm-and-truth-social/)

[## Unfurl 2025.03

Unfurl v2025.03 adds new features, including
parsing Google Search's UDM parameter, support for Mastodon forks (like Truth Social), and a utility parser to "clean up" inputs.](/unfurl-parses-googe-udm-and-truth-social/)

Mar 13, 2025
3 min read

[## Hindsight v2025.03 Released!

Hindsight v2025.03 focuses on Extensions - parsing more activity and state records, highlighting Extension permissions, and making it easier to examine Manifests.](/hindsight-parses-browser-extensions/)

Mar 11, 2025
2 min read

[![Unfurl v2025.02 Released](/content/images/size/w600/2025/02/unfurl-deceptive-ip-address.png)](/unfurl-parses-obfuscated-ip-addresses/)

[## Unfurl v2025.02 Released

Unfurl v2025.02 adds parsing of obfuscated IP addresses, more Bluesky timestamps, and more!](/unfurl-parses-obfuscated-ip-addresses/)

Feb 19, 2025
2 min read

[dfir.blog](https://dfir.blog) © 2026

[Powered by Ghost](https://ghost.org/)