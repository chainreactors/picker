---
title: Reading the CURRENT — LevelDB Forensics with crush
url: https://bebinary4n6.blogspot.com/2026/05/reading-current-leveldb-forensics-with.html
source: Instapaper: Unread
date: 2026-05-14
fetch_date: 2026-05-15T05:53:30.716878
---

# Reading the CURRENT — LevelDB Forensics with crush

# [Be-binary 4n6](https://bebinary4n6.blogspot.com/)

This is my blog about topics in the field of digital forensics.

## Sunday, May 10, 2026

### Reading the CURRENT — LevelDB Forensics with crush

Moin! 👋

LevelDB is everywhere — you just don't see it. If your workflow starts and ends with SQLite,
you're walking past a surprising amount of data on every acquisition. Chrome, Electron-based
desktop apps, iOS, Android — LevelDB shows up constantly in real cases, often unnoticed,
and often holding data that other tools quietly skip over.

With the current release, the [crush](https://github.com/kalink0/crush-forensics)
LevelDB viewer has grown significantly. This post walks through what it can do — and more
importantly, what it means for your investigation.

## What Is LevelDB — and Why Should I Care?

LevelDB is an on-disk key-value store developed by Google. Unlike SQLite, it does not
present itself as a single file with a recognisable header — instead, a LevelDB database
occupies an entire folder, containing a mix of files with `.log`, `.ldb`,
and metadata files named `MANIFEST-######`, `CURRENT`, and `LOG`.
If you have ever opened an acquisition and seen a folder full of files like that and moved on,
there is a good chance you left data on the table.

The forensic value of LevelDB depends on what the application chose to store there — and that varies enormously. In Chrome and Chromium-based browsers you will find browsing history fragments, sync metadata, IndexedDB entries from web applications, session state, and local storage data. Electron apps like Signal Desktop, Discord, or WhatsApp Desktop use LevelDB for app configuration, cached user data, and UI state.

On top of that, there is a structural property worth understanding: deleted records are not immediately gone. Every write to LevelDB — including deletions — is appended as a new entry with a sequence number. A deletion creates a "tombstone" entry: the key remains, but the value is empty. In `.ldb` files, superseded or deleted records are eventually cleaned out during compaction — but until that happens, they can still be read. In `.log` files, the active write log, everything is there. A tombstone without a value is not nothing: the key alone can tell you that something existed and was deliberately removed.

Alex Caithness from CCL wrote the definitive primer on this in 2020 — if you have not read
it yet, it is required reading before going further:

* [Hang on! That's not SQLite! Chrome, Electron and LevelDB](https://www.cclsolutionsgroup.com/post/hang-on-thats-not-sqlite-chrome-electron-and-leveldb) — CCL Solutions Group (September 2020)
* [IndexedDB on Chromium](https://www.cclsolutionsgroup.com/post/indexeddb-on-chromium) — CCL Solutions Group (October 2020)

The open-source Python library that came out of that research —
[ccl\_chrome\_indexeddb](https://github.com/cclgroupltd/ccl_chrome_indexeddb) —
is also the foundation that the crush LevelDB viewer builds on. Full credit to Alex and the
CCL team for that work.

## Where to Find LevelDB

LevelDB shows up more often than most people expect — and the pattern is consistent enough that you can learn to spot it without memorising paths.

On **iOS and Android**, look for any Chromium-based browser (Chrome, Edge, Brave) and any app built on a Chromium WebView or Electron runtime. The LevelDB stores typically live under the app's data container, in subdirectories named `IndexedDB`, `Local Storage/leveldb`, or `Sync Data/LevelDB`. The folder name is usually your first hint.

On **desktop systems** — Windows, Linux, macOS — the same logic applies, but the surface area is larger than most people assume. Every Chromium-based browser and every Electron app on the system has its own LevelDB stores. On Linux alone, a standard workstation running Chrome, Signal Desktop, Discord, and Slack will have dozens of LevelDB databases under `~/.config/`. It is easy to treat LevelDB as a mobile-only concern. It is not.

The reliable indicator is always the folder structure: a directory containing a `CURRENT` file, one or more `MANIFEST-######` files, and a mix of `.log` and `.ldb` or `.sst` files is a LevelDB database — regardless of what the folder itself is named.

[![Example LevelDB folder content](https://blogger.googleusercontent.com/img/a/AVvXsEgoGgfOvgSdz9Z0Xy1yJA8IxjfMJj15aKudfFHve_n4QTTQkTMmv1cbw_PmMcLBVDYMOqmxVX036qWGzerDQaEzmjvR1VJ6W4uz7t_8y3VvHfMf2we3DO4UZUz2BOUzNJ-IMP-bS7hOUIhYhumMYIEEAvuSs29y0WkleNZcoO3RA8PFUzFSd8fD3IW2QjIZ=w400-h141)](https://blogger.googleusercontent.com/img/a/AVvXsEgoGgfOvgSdz9Z0Xy1yJA8IxjfMJj15aKudfFHve_n4QTTQkTMmv1cbw_PmMcLBVDYMOqmxVX036qWGzerDQaEzmjvR1VJ6W4uz7t_8y3VvHfMf2we3DO4UZUz2BOUzNJ-IMP-bS7hOUIhYhumMYIEEAvuSs29y0WkleNZcoO3RA8PFUzFSd8fD3IW2QjIZ)

For this post, I am using the **Spotify Client App** from an iPhone acquisition (Public iOS 17 Image from Josh Hickman) as the example throughout. The path to the LevelDB looks like this:

```
/private/var/mobile/Containers/Data/Application/E81161FB-2689-4DF6-B98B-C8F95B056440/Library/Application Support/PersistentCache/Users/7jlf2hrgerxu6n0pp8l35r5h0-user/primary.ldb/
```

## Opening a LevelDB Database in crush

LevelDB databases don't announce themselves — there is no single file to click on.
A LevelDB database is a plain directory, typically named `LevelDB` (or sometimes
`leveldb`), containing a mix of `.log`, `.ldb`, `.sst`, and metadata
files. There is no special label or icon that distinguishes it from any other folder in the
file panel. The `.sst` (Sorted String Table) extension is functionally identical to
`.ldb` — it is an older naming convention still used by some non-Chrome LevelDB
implementations. crush handles both.

To open it in crush, **right-click the folder** in the file panel and select
**Open**. A single left-click only selects the folder — the right-click menu
is what triggers crush to read the directory structure and open the LevelDB viewer.
That is the step that is easy to miss the first time.

No extraction needed — crush reads directly from inside ZIP or TAR archives, or from a
folder on disk.

[![File panel showing right-click context menu on a LevelDB folder, with](https://blogger.googleusercontent.com/img/a/AVvXsEjQzrzOywt0Do4t4b-gPGLMpAT9YNGhQ9Wl_7mKh_BLrUjZVsiQaP1uT6Jx1XciKQ6sgvyKMAdLIdplCRfZovNQubYOTtNgY7bUqPdOslBAiWjKPT4UV5AL6LCdR8yX9X_fGXdXAoyAP-w07P-b86rUdUa9ITehI2nAjC13KjinhfymnGlh63v3kRt6bHox=w400-h141)](https://blogger.googleusercontent.com/img/a/AVvXsEjQzrzOywt0Do4t4b-gPGLMpAT9YNGhQ9Wl_7mKh_BLrUjZVsiQaP1uT6Jx1XciKQ6sgvyKMAdLIdplCRfZovNQubYOTtNgY7bUqPdOslBAiWjKPT4UV5AL6LCdR8yX9X_fGXdXAoyAP-w07P-b86rUdUa9ITehI2nAjC13KjinhfymnGlh63v3kRt6bHox)

## The Overview Tab

The first tab is the **Overview**. Before looking at any records, this is where
I orient myself.

It shows the MANIFEST metadata for the database: the comparator in use, the last sequence
number, the log number, and the files that make up the database grouped by compaction level.
crush parses *all* `MANIFEST-*` files present in the directory — not just
the current one. The active MANIFEST is labelled *(current)*; older ones expose
compaction history from before the last recovery, potentially referencing file numbers that
are no longer on disk. The `CURRENT` pointer itself is shown as a separate entry,
and where present, the `prev_log_number` field identifies the WAL log file that
preceded a recovery — useful context when you are trying to reconstruct the write history
of a database that has been through a crash or a clean shutdown cycle.

The **last sequence number** tells you how many write operations have been
performed on this database across its lifetime — including updates and deletions,
not just inserts. A low number (like 0 or close to it) means the database is fresh or
barely touched. A high number is a signal that there has been a lot of activity — and
potentially a lot of deleted data worth looking at.

The **compaction level** of the files tells you how mature the da...