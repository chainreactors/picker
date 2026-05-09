---
title: Object by Object — RealmDB Forensics with crush
url: https://bebinary4n6.blogspot.com/2026/05/object-by-object-realmdb-forensics-with.html
source: Instapaper: Unread
date: 2026-05-08
fetch_date: 2026-05-09T05:09:03.664335
---

# Object by Object — RealmDB Forensics with crush

# [Be-binary 4n6](https://bebinary4n6.blogspot.com/)

This is my blog about topics in the field of digital forensics.

## Tuesday, May 5, 2026

### Object by Object — RealmDB Forensics with crush

Moin! 👋

After the SQLite deep dive with crush, the next stop is Realm. This post walks through what the
crush Realm viewer can do — and as before, what the features actually mean for an investigation.
I am using the Android app **de.formel1** — the German Formula 1 news app —
as the example throughout. I enjoy watching F1, and it turns out the app stores some
of its data in its Realm database.

With v0.7.0, the [crush](https://github.com/kalink0/crush-forensics) Realm viewer has been significantly extended and improved. This post walks through what it can do — and as before, what the features actually mean for an investigation.

## What is Realm — and Why Should I Care?

Realm is an object-oriented database developed for mobile platforms. Unlike SQLite which
stores data in tables with rows and columns, Realm stores data as objects — think classes
with properties rather than spreadsheet rows. It was originally developed by Realm Inc.,
acquired by MongoDB in 2019, and has seen adoption in a range of Android and iOS apps.

Forensically, Realm matters because it shows up in real cases — and most tools either
support it poorly or not at all. If you have never encountered a `.realm` file
in an acquisition, you may simply not have noticed: the file has no extension-based
prominence and the format is far less documented than SQLite.

For a thorough introduction to Realm and its physical structure, Damien Attoe's
*The Realm Files* series is the best starting point available:

* [Vol 1 — Intro to RealmDB](https://digital4n6withdamien.blogspot.com/2025/09/the-realm-files-vol-1-intro-to-realmdb.html)
* [Vol 2 — Physical Structure](https://digital4n6withdamien.blogspot.com/2025/11/the-realm-files-vol-2-physical.html)
* [Vol 3 — The Realm Header](https://digital4n6withdamien.blogspot.com/2026/01/the-realm-files-vol-3-realm-header.html)

## Finding the Database

Realm databases use the `.realm` extension and are typically found under the
app's data directory. For the Formula 1 news app it is:

```
/data/data/de.formel1/files/
```

The extension alone is not always reliable — some apps store Realm files without it or
under an unexpected name. A more robust identifier is the magic bytes: at offset 16 in
the file, Realm stores the 4-byte value `54 2D 44 42` — the ASCII string
**"T-DB"**. If you see that signature, you are looking at a Realm database
regardless of the filename.

In crush, `.realm` files are now labelled **Realm** in the VFS
tree panel — the same way SQLite files show their type at a glance. Previously they showed
no label at all, which made them easy to overlook when browsing a large acquisition.

## The Header

The Header tab is my first stop when opening a Realm file — before looking at any data.
It shows the fundamental structural information of the database: the file format version,
the positions of both top-level references in the file, and which one is currently active.

This matters because everything else in the viewer builds on this foundation. The active
Top Ref determines which snapshot is the current state of the database; the inactive one
points to the previous commit. Knowing where both live in the file is the starting point
for understanding what the database currently contains — and what it contained before.

[![RealmDB Header Tab in crush](https://blogger.googleusercontent.com/img/a/AVvXsEiBOtT4GzzzkMpo36PNON7bKodWM69j82zSCwWOaGIVSn_wGzX9yaMXCHe4jnrmly4F1QToFEAbP_yLKfDsmq4l8vQPQG54Dxbb-pYNqe8dRnFDOkMl1wOAgLKrIyGFZQQgxAzb6QNqMzl4_6JR4IGhpvlAZXodOb8nxJq5-D4CR4tf1EqJoFI082BgzHmi=w400-h225)](https://blogger.googleusercontent.com/img/a/AVvXsEiBOtT4GzzzkMpo36PNON7bKodWM69j82zSCwWOaGIVSn_wGzX9yaMXCHe4jnrmly4F1QToFEAbP_yLKfDsmq4l8vQPQG54Dxbb-pYNqe8dRnFDOkMl1wOAgLKrIyGFZQQgxAzb6QNqMzl4_6JR4IGhpvlAZXodOb8nxJq5-D4CR4tf1EqJoFI082BgzHmi)

## The Schema Tab

The Schema tab shows every table (class in Realm terminology) as an expandable node
listing all column names with their Realm type: `int`, `bool`,
`string`, `date`, `link`, and so on.

This is important context before looking at data. Which tables exist? What properties do
they have? Are there `link` columns that reference other tables — and can I
join across them? Tables without decoded data still appear as leaf entries so nothing
is hidden.

[![Realm Schema tab in crush](https://blogger.googleusercontent.com/img/a/AVvXsEjYk6uUUtF0EiorTFtUbp6UYEBmvvcacGDqdEA5JG7otQ9H9E89DtNPFOuvz3FsFutvCjinr4mYF9puU52haUD0-CQ2a43ZgBaHpu4EoEGuITYJU_2KGT-rosXkJzDC4-tCyK-HUI2ikh2y-MJk2ALEDgTAcvl0Eae-_D9SgSZl16l3B5k-BPCxF3WcuALz=w384-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEjYk6uUUtF0EiorTFtUbp6UYEBmvvcacGDqdEA5JG7otQ9H9E89DtNPFOuvz3FsFutvCjinr4mYF9puU52haUD0-CQ2a43ZgBaHpu4EoEGuITYJU_2KGT-rosXkJzDC4-tCyK-HUI2ikh2y-MJk2ALEDgTAcvl0Eae-_D9SgSZl16l3B5k-BPCxF3WcuALz)

In earlier versions of the crush Realm parser, every column was labelled
`col_0`, `col_1`, … regardless of the actual schema names.
That is now fixed — column names are read directly from the Realm spec node.

## Top Refs — Deleted Data and Schema Diff

Before diving into tables, the **Top Refs** tab is worth checking first.
This is specific to Realm's internal architecture and has direct forensic relevance.

Realm maintains two top-level references — Top Ref 0 and Top Ref 1 — as part of its
copy-on-write architecture. At any point, one of them is active (the current state of
the database) and the other represents the previous commit. The Top Refs tab shows
both references, which one is currently active, and key settings and metadata for each.

Beyond the low-level header comparison, the tab now also shows a **Diff — schema**
section. This is where it gets forensically useful: crush compares the schema of both
Top Refs and lists tables that exist only in the active ref (added since the last snapshot),
tables that exist only in the inactive ref (deleted since the last snapshot), and tables
present in both but with a changed row count. A drop in row count between the inactive
and active ref is a direct indicator that records were deleted between the two commits.

[![Top Refs tab with schema diff in crush](https://blogger.googleusercontent.com/img/a/AVvXsEiMv2LoYVW2YsVLjZbrA98rLLJa-gg7YRkEfvWDz5tU3erVfadX6MIM4Xu881S8O7ZFzLaC-FtNQ-PVgDIOyljO-lb_E5LAHBcKPZ_VLlkJJXo1cBlKuP-anIn4dFbuWNJWbv3JsskL3SG35YnPSS319R5I6gvIsozSqeMIu927ZdxdVpd7rr1NJxFtHWqd=w445-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEiMv2LoYVW2YsVLjZbrA98rLLJa-gg7YRkEfvWDz5tU3erVfadX6MIM4Xu881S8O7ZFzLaC-FtNQ-PVgDIOyljO-lb_E5LAHBcKPZ_VLlkJJXo1cBlKuP-anIn4dFbuWNJWbv3JsskL3SG35YnPSS319R5I6gvIsozSqeMIu927ZdxdVpd7rr1NJxFtHWqd)

## Freed Data — Inspecting Unallocated Space

In addition to active and previous snapshots, crush also exposes
**freed data** directly. Unlike the Tables tab, this is not
reconstructed into rows — it is a view into unallocated regions of the
Realm file.

When objects are deleted in Realm, their space is marked as free but not
immediately overwritten. These regions may still contain residual data
from previously stored objects. The Freed Data tab surfaces these regions
as individual entries with:

* **Offset** — where the free region is located in the file
* **Size** — the length of the region
* **Source** — whether the region originates from the active or inactive Top Ref
* **Content** — decoded where possible (currently it looks for null terminated strings)

Selecting an entry reveals the raw data, including a full hex view at the
bottom of the tab. This keeps the representation close to the underlying
file structure and avoids introducing assumptions about object boundaries
or schema correctness.

In practice, these regions can still contain recognizable artefacts such
as strings, timestamps, or fragments of previously stored objects.
However, interpretatio...