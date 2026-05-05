---
title: What Hides in the WAL — SQLite Forensics with crush
url: https://bebinary4n6.blogspot.com/2026/05/what-hides-in-wal-sqlite-forensics-with.html
source: Instapaper: Unread
date: 2026-05-04
fetch_date: 2026-05-05T05:04:21.225543
---

# What Hides in the WAL — SQLite Forensics with crush

# [Be-binary 4n6](https://bebinary4n6.blogspot.com/)

This is my blog about topics in the field of digital forensics.

## Friday, May 1, 2026

### What Hides in the WAL — SQLite Forensics with crush

Moin! 👋

SQLite is everywhere in digital forensics. iOS, Android, macOS, Windows — virtually every
app that needs to store structured data uses it. Messages, call logs, browser history,
location data, app state — if it is on a mobile device, there is a good chance it lives
in a SQLite database. If you want to go deeper on the file format itself, the
[official SQLite file format documentation](https://www.sqlite.org/fileformat.html)
is the right starting point.

With v0.6.0, the crush SQLite viewer has grown significantly. This post walks through
what it can do — and more importantly, what the features actually mean for your investigation.

## Opening a Database

crush opens SQLite databases directly from inside ZIP or TAR archives, from folders, or as
standalone files. No extraction needed. When you select a SQLite file, the SQLite
viewer opens automatically. The combo box at the top lets you switch between tables,
views, and the generated entries described below.

One important detail: crush opens all SQLite connections in read-only mode. This matters because closing a WAL-mode database that was opened with a read-write connection triggers an automatic checkpoint — which commits and clears the Write-Ahead Log, potentially destroying forensic data. More on WAL below.

## The Summary View

The default view when opening a database is the **Summary**. It shows all
tables and views with their row counts, and a status label giving the full schema object
count — tables, views, indexes, and triggers at a glance.

This is useful for orientation before diving in: how many tables are there, which ones
have data, and are there any views worth looking at?

[![DB summary overview in crush](https://blogger.googleusercontent.com/img/a/AVvXsEhyh39d7pwLw1FzX_EPzysSmGn3mpjOztwInlGNBHHqoBWuJrVU72siX8xV0KSundQX90vcov5WuNdJcQJkjKFemb8ObY92i5TdfcGN2uKyvU1IvagdMX7ZtFtZ8fq4Psv4uvkDYMGptL0SV5NjYx1t4YDk38AMuTpFIrXRzOU1C148wcGUse2eYMunNzyt=w400-h268)](https://blogger.googleusercontent.com/img/a/AVvXsEhyh39d7pwLw1FzX_EPzysSmGn3mpjOztwInlGNBHHqoBWuJrVU72siX8xV0KSundQX90vcov5WuNdJcQJkjKFemb8ObY92i5TdfcGN2uKyvU1IvagdMX7ZtFtZ8fq4Psv4uvkDYMGptL0SV5NjYx1t4YDk38AMuTpFIrXRzOU1C148wcGUse2eYMunNzyt)

## DB Structure

The **DB Structure** entry in the combo box lists every schema object in the database — tables, views, indexes, and triggers — with structural details: column definitions for tables, CREATE SQL for views, index definitions, and trigger signatures.

When I open an unfamiliar database, this is where I start, direclty after taking a look on the summary. What tables are there? What do the columns tell me about what the app stores? I also pay attention to indexes — they often hint at what the app queries frequently — and triggers, which can automatically update timestamps or delete records without the user doing anything. Understanding the schema is the foundation for everything that follows

[![DB structure view in crush](https://blogger.googleusercontent.com/img/a/AVvXsEj-8av0a73N_BqO8_gk7dXMSmoQwAj-N5GFE7AweNNekjG0AOU8V9StFoNBWixQXKiJc935pMkuDGsO9kOeTL0z3MnLuMapFWEqm7XSZOKyx81lO5kC8Lc8Vsp0bLKNSH8p6Veje42jp-gByM1WCXYVvljRUt9m3TK7ryF2JbW_s4NhjmiL_Y-mUz2U8bw4=w400-h268)](https://blogger.googleusercontent.com/img/a/AVvXsEj-8av0a73N_BqO8_gk7dXMSmoQwAj-N5GFE7AweNNekjG0AOU8V9StFoNBWixQXKiJc935pMkuDGsO9kOeTL0z3MnLuMapFWEqm7XSZOKyx81lO5kC8Lc8Vsp0bLKNSH8p6Veje42jp-gByM1WCXYVvljRUt9m3TK7ryF2JbW_s4NhjmiL_Y-mUz2U8bw4)

## DB Info — PRAGMA Settings

The **DB Info** entry shows 28 SQLite PRAGMA settings with their current
values and plain-English descriptions. PRAGMA statements are essentially configuration
queries — they reveal things like the page size, the journal mode, the encoding, and
the application ID.

The journal mode is particularly relevant: a value of `WAL` means the database
uses a Write-Ahead Log, which has significant forensic implications (see below). The
`application_id` PRAGMA can sometimes identify the application that created
the database. The `user_version` field is used by many apps to track database
schema versions — useful for understanding which version of an app created or last
modified the database.

[![DB Info PRAGMA view in crush](https://blogger.googleusercontent.com/img/a/AVvXsEh1jGUYryu-OT2wMt8xpmLS67o5ROmQ4it7k_QVDqdhyP3rLYxzad_dZq66PdqXff1rgyiQSDO6Y6VKAMDHlqAVJGjQad6xuW_f1x_7jaOBUx4QgXvvPRrwJi7OX3oElPNeHYYzjwv73VShcwmS-QX3-_3NcfNhcJOtAOXwiq3XIsBlx50jK8RplLmsLi0I=w400-h340)](https://blogger.googleusercontent.com/img/a/AVvXsEh1jGUYryu-OT2wMt8xpmLS67o5ROmQ4it7k_QVDqdhyP3rLYxzad_dZq66PdqXff1rgyiQSDO6Y6VKAMDHlqAVJGjQad6xuW_f1x_7jaOBUx4QgXvvPRrwJi7OX3oElPNeHYYzjwv73VShcwmS-QX3-_3NcfNhcJOtAOXwiq3XIsBlx50jK8RplLmsLi0I)

## Timestamp Decoding

Timestamps in SQLite databases are stored as raw numbers — but the epoch and unit
vary wildly between apps and platforms. Right-clicking any column header and selecting
**"Decode column as timestamp"** lets you tell crush how to interpret the values.

Supported formats:

* **Unix seconds** — seconds since 1970-01-01 UTC (most common on Android)
* **Unix milliseconds** — same epoch, millisecond precision
* **Unix microseconds** — same epoch, microsecond precision
* **Mac Absolute Time** — seconds since 2001-01-01 UTC (Apple's CoreData default)
* **Windows FILETIME** — 100-nanosecond intervals since 1601-01-01 UTC
* **Chrome / WebKit time** — microseconds since 1601-01-01 UTC (Chrome history databases)

The decoded values are displayed as `YYYY-MM-DD HH:MM:SS UTC` and the column
header shows the active format as a suffix — for example `created_at [mac abs]`.
Sorting still works correctly because the raw numeric value is preserved internally.
Select "Clear timestamp format" to revert to the raw value.

If you are unsure which format a column uses, a quick sanity check is to look at the
magnitude of the values: Unix seconds for recent dates are around 1.7 billion; Mac
Absolute Time values for recent dates are around 750 million; Chrome time values are
around 13 trillion.

The following pictures show one column converted, the other in original state.

[![Timestamp decoding in crush SQLite viewer](https://blogger.googleusercontent.com/img/a/AVvXsEj1PsRrqO7nN5Zb7iKDir9RGDZoBxAj1Vtz1MABLR0-iiKiQkzCiD8omr7r87dcV2zGapT-fQmPq9uLTiWkJfAPAO_6QXDEjb8SUbBb7K1WyBgvxTvVsHMrJLkjz3iN853Sk4Hc-2tG3aI_JIeO_SKZ9IXikV2x8z6nOQaPUttjCCQts0R9cAREaPrfo5Hp=w400-h230)](https://blogger.googleusercontent.com/img/a/AVvXsEj1PsRrqO7nN5Zb7iKDir9RGDZoBxAj1Vtz1MABLR0-iiKiQkzCiD8omr7r87dcV2zGapT-fQmPq9uLTiWkJfAPAO_6QXDEjb8SUbBb7K1WyBgvxTvVsHMrJLkjz3iN853Sk4Hc-2tG3aI_JIeO_SKZ9IXikV2x8z6nOQaPUttjCCQts0R9cAREaPrfo5Hp)

Just to mention it: It is also possible to convert timestamps directly in the SELECT query - this is basic SQLite-Syntax one can use (Reference: <https://sqlite.org/lang_datefunc.html> ).

## Inspect Cell

BLOB cells are common in SQLite databases — and they often contain the most interesting data.
Right-clicking any cell and selecting **"Inspect cell…"** opens a dedicated window
that tries to auto-detect the content format. If it recognises something — a binary plist, xml, base64 (more format to come) — it opens the data directly in the appropriate viewer. If auto-detection does
not find a match, I can manually select from the available formats or fall back to the hex view.

In practice I use this constantly. A BLOB that looks like noise in the table view often turns
out to be an bplist or base64  — and Inspect Cell gets
me there in two clicks without touching the filesystem.

[![Inspect cell in crush SQLite viewer](https://blogger.googleusercontent.com/img/a/AVvXsEi1fr0diGXSrOsCYE_17Z4d2Dg4Lv18az_BwXMf5ns-4Pwvg8RRe3nqMg0fVGd2z_KWjnwKPEfUN3hMv_oJmJusEr91Bstt06aNeEiw8cc_FdmSiEx0aqVwpvO9w8GzNa_NwREETCk9m52u7eu5qeavRkQbCqV9k32Q8GAII2ZuFNaJ-sVeC_hWIKv9496X=w...