---
title: Beyond the C — SEGB and Biome Forensics with crush
url: https://bebinary4n6.blogspot.com/2026/05/beyond-c-segb-and-biome-forensics-with.html
source: Instapaper: Unread
date: 2026-05-19
fetch_date: 2026-05-20T06:05:30.882928
---

# Beyond the C — SEGB and Biome Forensics with crush

# [Be-binary 4n6](https://bebinary4n6.blogspot.com/)

This is my blog about topics in the field of digital forensics.

## Saturday, May 16, 2026

### Beyond the C — SEGB and Biome Forensics with crush

Moin! 👋

This post walks through the SEGB viewer in
[crush](https://github.com/kalink0/crush-forensics), which received a complete
forensic overhaul in the current release. The short version: Protobuf payloads are decoded
automatically, and a built-in SQL editor lets you query every record — including nested
and repeated Protobuf fields — without writing a single line of Python first.

## What Is SEGB — and Why Should I Care?

SEGB is Apple's binary log format used by the **Biome** service. The name comes
from the four-byte magic header at the start of every file: `53 45 47 42` —
ASCII for `SEGB`. Apple has never publicly documented the format; the community
named it informally, and the name stuck.

Biome emerged in iOS 15 alongside `knowledgeC.db`, and by iOS 16 it had largely
replaced it. Today there are well over 130 defined Biome streams on a modern iOS device,
each tracking a specific type of user activity in its own folder — application foreground
and background events, device unlock events, Safari browsing history, Siri interactions,
messaging activity, airplane mode toggles, and much more. Every stream stores its records
in SEGB files. Every SEGB file payload is almost always Protobuf.

There are two versions of the format in the wild. **SEGB v1** was used in iOS 15
and iOS 16. **SEGB v2** arrived with iOS 17 and remains in use through current iOS versions —
the internal structure changed significantly, with the addition of a trailer section that must
be parsed to read the file correctly. crush handles both versions automatically; you do not
need to know which one you are looking at before opening the file.

Two resources from the community worth reading alongside this post:

* [Understanding and Decoding the Newest iOS SEGB Format (v2 / iOS 17)](https://cellebrite.com/en/blog/understanding-and-decoding-the-newest-ios-segb-format/) — Cellebrite Research (2023)
* [iOS 16 — Now You 'C' It, Now You Don't: Breaking Down the Biomes](https://blog.d204n6.com/2022/09/ios-16-now-you-c-it-now-you-dont.html) — D20 Forensics (2022)

The open-source Python library that the crush SEGB parser builds on is
[ccl-segb](https://github.com/cclgroupltd/ccl-segb) by Alex Caithness and the
CCL Solutions Group — full credit to them for that work.

## Where to Find SEGB Files

A full filesystem acquisition is required — logical or backup-level imaging does not expose
Biome data.

**iOS:**

* Primary user streams: `/private/var/mobile/Library/Biome/streams/public/`
* System streams: `/private/var/db/biome/streams/`

**macOS:**

* `/private/var/db/biome/streams/`

These are the well-known paths — but SEGB files are not limited to them. On a full
filesystem image you will find additional SEGB data in locations such as
`Library/DuetExpertCenter/`, `Library/PersonalizationPortrait/`,
and inside app group containers under
`Containers/Shared/AppGroup/<AppID>/`. crush detects SEGB files by
their magic bytes automatically — so when you open a full filesystem image, files in
these locations show up in the file system panel when filtering for
`type:SEGB` without any manual searching.

In the well-known paths each stream lives in its own subdirectory named after the
data it tracks — `_DKEvent.App.inFocus`, `_DKEvent.device.Unlocked`,
`_DKEvent.Safari.History`, `Device.Display.Backlight`, and so on.
Within each stream folder you will find a `local` subfolder (records from this
device) and a `remote` subfolder (records synced from the user's other Apple
devices on the same Apple ID). There is also a `tombstone` folder containing
expired record versions. crush reads all of them.

The SEGB files themselves have no file extension and are named with a large integer —
a Cocoa epoch timestamp in microseconds, which gives you a rough creation time from the
filename alone before you open anything.

For this post I am using SEGB files from an iPhone acquisition, specifically from the
App.inFocus stream:

```
/filesystem1/private/var/mobile/Library/Biome/streams/public/_DKEvent.App.inFocus/local/
```

## Opening an SEGB File in crush

SEGB files appear as plain files in the crush file panel — no extension, no special icon.
To open one, **double-click it**. crush reads the magic header, determines
whether the file is v1 or v2, parses the records, decodes the Protobuf payloads, and
opens the viewer. The detected version and total record count are shown in the
Properties panel.

No extraction needed — crush reads directly from inside ZIP or TAR archives or from a
folder on disk. All connections are read-only.

[![Filesystem Panel - Showing SEGB in well-known folders](https://blogger.googleusercontent.com/img/a/AVvXsEi6pv5SUWeVqxUxt_kYTcXldJBdjaWmFRv7CA9PT7gC0_nIW2ubyfGMAwSGm_qy71jtmVwCp294lBmbMqAcTO_IO3a_8PTUMl8Km_yMHlI_Oaru4MHT6-wXVkKOIcLW58J0qqr2wd3YEXK6Vyj30Z9QMTBU0WCHeLme53RFC_EnKWBJf9z2pCS74WRHYP1a=s0)](https://blogger.googleusercontent.com/img/a/AVvXsEi6pv5SUWeVqxUxt_kYTcXldJBdjaWmFRv7CA9PT7gC0_nIW2ubyfGMAwSGm_qy71jtmVwCp294lBmbMqAcTO_IO3a_8PTUMl8Km_yMHlI_Oaru4MHT6-wXVkKOIcLW58J0qqr2wd3YEXK6Vyj30Z9QMTBU0WCHeLme53RFC_EnKWBJf9z2pCS74WRHYP1a)

## The SEGB Table

The main view is the **SEGB** table — the same name used in the SQL editor.
Each row is one record from the file. The columns present depend on whether the file is
v1 or v2; some are common to both.

**Columns common to v1 and v2:**

| Column | Description |
| --- | --- |
| **Index** | Sequential record number, 0-based. Order of appearance in the file. |
| **Offset** | Byte offset where the payload data begins, after the record header. Useful for correlating with raw hex examination. |
| **State** | Entry lifecycle state: **Written** = active record, **Deleted** = marked for deletion, **Unknown** = empty or unrecognised. Deleted records are colour-coded red. |
| **CRC Stored** | CRC32 value written into the entry header at creation time. |
| **CRC Calc** | CRC32 calculated over the current payload bytes at parse time. |
| **CRC Passed** | `True` if the CRC stored by the system matches the CRC crush calculates over the parsed payload bytes — confirming that what crush read matches what was written. `False` warrants closer examination: it may indicate corruption, an unknown format variant, or a parse issue. |
| **Payload Size** | Size of the raw Protobuf payload in bytes. |
| **Payload** | Schema-less wire-format decode of the raw payload bytes, rendered as human-readable text. Cocoa timestamps are decoded to ISO datetimes automatically, nested messages are expanded inline, repeated fields collected into arrays. Raw bytes remain accessible via the Blob Inspector. |

**v1 only:**

| Column | Description |
| --- | --- |
| **Timestamp 1** | First Cocoa absolute time double from the 32-byte record header (bytes 8–15). Exact semantics not formally documented by Apple; in practice often identical to Timestamp 2, possibly reflecting record creation and commit time. |
| **Timestamp 2** | Second Cocoa absolute time double from the 32-byte record header (bytes 16–23). May differ from Timestamp 1 in some entry states. |

**v2 only:**

| Column | Description |
| --- | --- |
| **Creation** | Cocoa absolute time from the trailer entry at the end of the file. Records when the entry was created. |
| **Trailer Offset** | Byte offset of this entry's trailer record within the trailer table at the end of the file. |
| **Entry End Offset** | End offset of the entry's data area, relative to the start of the entry region (after the 32-byte file header). Used internally to calculate entry length. |

### [![SEGB table showing columns for a v2 file](https://blogger.googleusercontent.com/img/a/AVvXsEgwh5M4JE5nxcHiyF0-rtvZv61cvPOqNoCyFWcxJN03_nQnRjAyxQxMq61Wt6-zYbmU2ciJVjFfzT8yFhPMUyj-7nH_SgkcEUeKyETGSsFxG8dZzOvK6HYfD0bwEalOqUyJVpkU4V--9ibIXmZl3fT56DzGXfQZOukhBe...