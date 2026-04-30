---
title: Introducing crush A DFIR Workbench for Surfing Through Data Formats
url: https://bebinary4n6.blogspot.com/2026/04/introducing-crush-dfir-workbench-for.html
source: Instapaper: Unread
date: 2026-04-29
fetch_date: 2026-04-30T05:30:48.970391
---

# Introducing crush A DFIR Workbench for Surfing Through Data Formats

# [Be-binary 4n6](https://bebinary4n6.blogspot.com/)

This is my blog about topics in the field of digital forensics.

## Saturday, April 25, 2026

### Introducing crush: A DFIR Workbench for Surfing Through Data Formats

Moin! 👋

Today I want to share something a little different from the usual artifact analysis posts —
I am releasing **crush-forensics v0.5.0**, a digital forensic analysis workbench I have been
building for a while.

You can find it on GitHub:
[github.com/kalink0/crush-forensics](https://github.com/kalink0/crush-forensics)

## The Problem

When I work with acquisitions — especially mobile ones — I often find myself wanting to quickly
look at a specific file without firing up a full forensic platform. Maybe I want to check
a PLIST, peek into a SQLite database, or just confirm what a binary blob actually contains.
Opening the whole acquisition in a heavy tool just to answer a quick question felt like overkill.

At the same time, reaching for a hex editor or writing a one-off script every time also
gets old fast. I wanted something in the middle: a lightweight, dedicated workbench that knows
about the file formats we actually work with in DFIR — and that lets me navigate directly inside
ZIP and TAR archives without extracting anything to disk first.

That is what crush is.

## Why "crush"?

I am a big Finding Nemo fan. Crush is the laid-back sea turtle who surfs the East Australian Current —
and that is exactly the vibe I wanted for this tool: just riding through data formats, going with the flow. 🐢

The idea of *surfing* through file formats felt like the right metaphor —
you open an archive, navigate the structure, and glide from a PLIST to a SQLite DB to a hex view
without fighting the current. Dude.

## What Can It Do?

crush is a Python-based GUI application (built with PySide6). It supports:

* Opening and navigating inside **ZIP and TAR archives** directly — no extraction to disk needed
* Opening single files and folders
* **Export files/folders** and open them directly in external software
* **Hex Viewer**
* **SQLite Viewer**
* **Text Viewer** with syntax highlighting and encoding detection
* **JSON Viewer** (collapsible tree)
* **XML Viewer** (collapsible tree)
* **PLIST and BPLIST Viewer**
* **SEGB v1 and v2 Viewer**
* **ABX Viewer** (Android Binary XML)
* **LevelDB Viewer** (Chrome LevelDB / Android app databases)
* **Image Viewer**
* **Media Viewer** (audio and video)
* **Multi-Log Studio** — multi-source log analysis with format auto-detection, including Apple Unified Log / `.tracev3` / `.logarchive`, syslog, and more *(note: Unified Log support is currently alpha — decoding can be slow, this is actively being worked on)*
* **Protobuf Viewer** — schema-less, with optional schema decoding
* **PDF text extraction**
* **Realm Database Viewer** — header, schema/class extraction, top-ref comparison, table/column data decoding

[![Android ABX viewer in crush (Linux)](https://blogger.googleusercontent.com/img/a/AVvXsEgXmOEbsRoWf7QOBZ-5MY05NVTGZiXK6KBHDtWINwsY6zUjeAN3PNVW6ZjlZ4FVfeihOQw6wYSqZFjrpg0PgcZBWX_5NCrSayFPJFtbaZCpIzhhd9SU5gkkVNGDKxKfsDie5LkqXWHwoiRntic6_Lb_P1dHMJ1blPmLHhpUPPZOJTW-Le1J0XyJjr3IG6Cm=w640-h334)](https://blogger.googleusercontent.com/img/a/AVvXsEgXmOEbsRoWf7QOBZ-5MY05NVTGZiXK6KBHDtWINwsY6zUjeAN3PNVW6ZjlZ4FVfeihOQw6wYSqZFjrpg0PgcZBWX_5NCrSayFPJFtbaZCpIzhhd9SU5gkkVNGDKxKfsDie5LkqXWHwoiRntic6_Lb_P1dHMJ1blPmLHhpUPPZOJTW-Le1J0XyJjr3IG6Cm)

[![iOS SQLite viewer in crush (Windows)](https://blogger.googleusercontent.com/img/a/AVvXsEjqScnmsxHJX7Sy8qYoXL9Dtd56H1aIIRHRZaqgqMmViP8vCcEdTE39uaHpp1VI_183JSxrc2WejIN6ys8UyBErgeIBKMAmRaXYxrHiLexCrSYr_FSH1gAZXKCdMpTK2U9ydFd5I7zlUOf3mun72Owp_ZTCEs6hFWL5-w-nZE8rwEjOIEuk8wVBK-v1QTnf=w640-h414)](https://blogger.googleusercontent.com/img/a/AVvXsEjqScnmsxHJX7Sy8qYoXL9Dtd56H1aIIRHRZaqgqMmViP8vCcEdTE39uaHpp1VI_183JSxrc2WejIN6ys8UyBErgeIBKMAmRaXYxrHiLexCrSYr_FSH1gAZXKCdMpTK2U9ydFd5I7zlUOf3mun72Owp_ZTCEs6hFWL5-w-nZE8rwEjOIEuk8wVBK-v1QTnf)

## Built-in Data Format Database

One feature I am particularly happy with is the built-in **data format database**.
Crush identifies forensically relevant formats by magic bytes and extension, and surfaces the
information directly in the UI for every selected file — including formats that do not have a
dedicated viewer yet.

For each format it shows:

* Full name and abbreviation
* Category (database, configuration, log, ...)
* **Forensic relevance** — what an investigator is likely to find here
* Relevant **platforms** (iOS, Android, macOS, Windows, ...)
* **Magic bytes** with offset and description
* Links to format specs and relevant forensic research

[![Format Reference — the built-in data format database in crush](https://blogger.googleusercontent.com/img/a/AVvXsEh-U3iCMU6joiH62dMbN1AUUIn9CwXYXejR7oAYRiSXvyFGGmmcXx-UKTkVcSQxFSGyevOGl4NZ_xLLIkhAc-GKScm34HVMKBbIdG-DwbInDp_mnBZdBhfLTfR0kDZt9d0TQpJ4l1rqT4nbXldCSeArxS0QcEESYPSLCdLC6Pgb-0-V0Us1pQmGW99WE_f9=w400-h259)](https://blogger.googleusercontent.com/img/a/AVvXsEh-U3iCMU6joiH62dMbN1AUUIn9CwXYXejR7oAYRiSXvyFGGmmcXx-UKTkVcSQxFSGyevOGl4NZ_xLLIkhAc-GKScm34HVMKBbIdG-DwbInDp_mnBZdBhfLTfR0kDZt9d0TQpJ4l1rqT4nbXldCSeArxS0QcEESYPSLCdLC6Pgb-0-V0Us1pQmGW99WE_f9)

So for example, when you open an ABX file, crush identifies it via its magic bytes,
opens it in the ABX viewer, and right there in the UI you can see that this is an
Android Binary XML file used for system and app settings — plus links to the AOSP source
and relevant research from CCL Solutions. No more alt-tabbing to a browser to remember
what a format is.

## Integrity Mode

Crush also has an optional **integrity mode** for auditability. When enabled:

* Records **SHA-256 hashes** when files are opened or exported
* Hashes ZIP/TAR/file sources on open (folders are not hashed)
* Writes hashes to the log
* Creates a `crush-export-hashes.txt` file next to exported data

You can toggle it via the status badge in the bottom right of the UI. It can also be turned off
for faster opening of large ZIP/TAR sources. A small but useful addition for anyone who needs
to demonstrate that what they examined is what they got.

[![Integrity Mode dialog in crush](https://blogger.googleusercontent.com/img/a/AVvXsEha_HU6d7h1wmOlXLJm1YZIQz6FYTyRJs5gY6GEI2lWxI4VCdGdNm4If5VYX5dHRiMHUmFfcdyXSwLW1S5mOFoS6Bctbcr8j2fay6c7Tn0tzOTrrfl0EhRXo_bC_yFZVQJD7fI48LOzuD2372Mr6ObPNLIz1vmhdGqJuJll8V0OnBsmJJbR7kjH1F6HE5Z4=w400-h224)](https://blogger.googleusercontent.com/img/a/AVvXsEha_HU6d7h1wmOlXLJm1YZIQz6FYTyRJs5gY6GEI2lWxI4VCdGdNm4If5VYX5dHRiMHUmFfcdyXSwLW1S5mOFoS6Bctbcr8j2fay6c7Tn0tzOTrrfl0EhRXo_bC_yFZVQJD7fI48LOzuD2372Mr6ObPNLIz1vmhdGqJuJll8V0OnBsmJJbR7kjH1F6HE5Z4)

## Installation

**v0.5.0 ships with pre-built binaries for Windows, Linux, and macOS** — available directly from the
[GitHub releases page](https://github.com/kalink0/crush-forensics/releases).
No Python environment needed, no dependency wrangling — just download and run.

One honest caveat: the **macOS binary is currently untested** as I do not have a macOS system
available. If you are on macOS and give it a try, please let me know how it goes via GitHub issues
or direct message — that feedback would be really valuable.

If you prefer to run from source (e.g. for development), the
[README](https://github.com/kalink0/crush-forensics) has full instructions,
including the platform-specific system dependencies and how to download the Unified Log parser binaries.

## Credits

Crush builds on some excellent work from the DFIR community. Bundled third-party modules include:

* [ccl\_bplist](https://github.com/cclgroupltd/ccl-bplist) by CCL Solutions Group — binary plist parsing
* [ccl\_segb](https://github.com/cclgroupltd/ccl_segb) by CCL Solutions Group — SEGB parsing
* [ccl\_leveldb](https://github.com/cclgroupltd/ccl-leveldb) by CCL Solutions Group — LevelDB / Chrome LevelDB parsing
* [macos-UnifiedLogs](https://github.com/mandiant/macos-UnifiedLogs) by Mandiant — Apple Unified Log parsing

Thank you to everyone in the co...