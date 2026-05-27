---
title: Telegram evidence beyond the cloud
url: https://andreafortuna.org/2026/05/25/telegram-forensics/
source: Instapaper: Unread
date: 2026-05-26
fetch_date: 2026-05-27T06:12:43.540982
---

# Telegram evidence beyond the cloud

[Andrea Fortuna](/)
[ ]

[About](/about/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# Telegram evidence beyond the cloud

May 25, 2026

by [Andrea Fortuna](/about/)

In September 2024, Telegram quietly rewrote its own mythology. For years, the platform had positioned itself as the privacy-conscious alternative to WhatsApp: end-to-end encryption for secret chats, no cooperation with governments except in terrorism cases, and a founder who publicly clashed with Russian authorities. Then came the transparency report. Between January and December 2024, Telegram responded to 900 U.S. law enforcement requests, handing over phone numbers and IP addresses for 2,253 users. The policy shift, reflected in Telegram’s [official privacy policy](https://telegram.org/privacy), extended cooperation beyond terrorism to any criminal activity, including cybercrime. The app that investigators once filed in the “too hard” drawer is now significantly more cooperative than it used to be. That context matters, but it does not change the core forensic reality: the most valuable Telegram artifacts are almost never in what the platform will send you on request.

![cover](/assets/2026/telegram-forensics.jpg)

This guide focuses on practical Telegram forensic analysis across the artifacts investigators actually parse in the field: Android `cache4.db`, iOS `db_sqlite`, Telegram Desktop `tdata`, and time-sensitive WAL/freelist remnants.

## The architecture investigators actually face

Telegram organizes its storage around a fundamental distinction that shapes every forensic decision you make. **Regular chats** (cloud chats) are synchronized on Telegram’s servers, accessible from any device, and stored server-side in a format Telegram can read. **Secret chats** are device-only, established via a Diffie-Hellman key exchange, and genuinely end-to-end encrypted: Telegram holds no copy, no key, nothing. This distinction has direct investigative impact. If you send a legal request to Telegram, you may receive phone numbers and IP addresses for criminal cases after September 2024. You will not receive message content, including content from regular cloud chats, because the platform generally declines to provide it across most jurisdictions.

This means that for any investigation where message content matters, the device is your primary target. The server is a fallback for identity attribution, not content recovery. Understanding that asymmetry is the prerequisite for everything that follows.

### Version boundaries and validation discipline

Telegram forensic behavior is version-sensitive. Storage schema details, WAL persistence windows, and cache retention patterns can shift across Telegram releases and operating system updates. In practice, every parser output should be treated as a version-scoped hypothesis until confirmed with manual byte-level validation on the same build family.

If your lab workflow includes iOS acquisitions, the methodology discussed in this article should be read together with this practical guide to [iOS evidence acquisition without jailbreak](https://andreafortuna.org/2026/02/04/ios-forensics-without-jailbreak-a-practical-guide-to-modern-mobile-evidence-acquisition/), especially for AFU/BFU handling and extraction constraints.

### Field priorities in the first 60 minutes

If you have a narrow acquisition window, sequence matters more than tool choice.

1. Preserve volatile state first: keep the device powered, isolate network paths when possible, and document lock state (AFU/BFU on iOS).
2. Acquire app containers before broad triage exports: for Telegram, that means grabbing `cache4.db`/WAL artifacts on Android and `postbox/db_sqlite` plus WAL on iOS.
3. Pull attachment caches immediately after database extraction, because media lifetimes are often shorter than message metadata lifetimes.
4. Defer enrichment steps (timeline decoration, attribution correlation, reporting formatting) until core artifacts are safely duplicated and hashed.

## Android artifacts in cache4.db

On Android, Telegram stores its local data under `/data/data/org.telegram.messenger/files/` inside the app’s private sandbox. Access generally requires root, a full filesystem/physical acquisition method, or a forensic agent with sufficient privileges (legacy ADB backup methods may work only on older devices and app versions). The main database is `cache4.db`, a standard SQLite file. Depending on journal mode, it may be accompanied by rollback journal artifacts or WAL files (`cache4.db-wal` and `cache4.db-shm`). The schema is readable without any proprietary decryption. For broader context on mobile artifact persistence on recent Android versions, this analysis of [Android pattern-of-life artifacts](https://andreafortuna.org/2026/04/23/android-pattern-of-life-hidden-artifacts-reconstruct-daily-routine/) is a useful companion.

The tables you want first are these:

* **messages**: stores message ID, date (Unix timestamp), dialog ID, sender ID, message text, and a `data` BLOB for media and service messages
* **users**: maps numeric user IDs to first name, last name, username, and phone number where available
* **dialogs**: maps dialog IDs to type (user, group, channel, secret chat), unread count, and top message ID
* **media**: stores references to local file paths for attachments that have been downloaded to the device
* **chat\_settings\_v2**: stores per-chat notification and privacy settings

A basic query to reconstruct a conversation timeline in SQLite3:

```
SELECT
  m.date,
  datetime(m.date, 'unixepoch') AS readable_time,
  u.first_name || ' ' || COALESCE(u.last_name, '') AS sender,
  m.message
FROM messages m
LEFT JOIN users u ON m.uid = u.uid
WHERE m.dialog_id = <target_dialog_id>
ORDER BY m.date ASC;
```

The `data` column in `messages` is a serialized BLOB for non-text messages (photos, voice notes, documents, geo-pins). Parsing it requires understanding the **MTProto TL serialization format**, which Telegram uses internally. The [teleparser](https://github.com/RealityNet/teleparser) tool by RealityNet handles this deserialization and extracts structured records from the BLOB fields, including media file references, forwarded message metadata, and geo-coordinates. For manual verification, the TL constructor ID is stored in the first four bytes of each BLOB in little-endian order: for example, `0x9c4e19c1` identifies a `messageMediaPhoto` record.

Group membership history and admin changes live in `chat_settings_v2` and in service messages within the `messages` table itself, where the `media` field will contain a TL-encoded `messageActionChatAddUser` or `messageActionChatDeleteUser` object. These are forensically significant for establishing who was present in a group at a given time.

The `cache4.db` also stores **search index data** for in-app full-text search, which means that message fragments from conversations the user has actively searched for can persist in the database even if the conversation itself has been archived or the messages deleted. This is an underexplored artifact source.

## iOS artifacts in db\_sqlite

On iOS, Telegram stores data outside the standard app backup mechanism. iTunes and iCloud backups do not contain Telegram data. The only reliable path is a **full filesystem extraction** via an agent-based method (Belkasoft X, Cellebrite UFED with iOS agent), checkm8-based physical acquisition on supported devices (A5-A11 chipsets), or a jailbroken device. For devices in **AFU (After First Unlock)** state, the keychain is accessible and the Telegram data partition is decryptable at acquisition time.

After acquisition, Telegram data sits under:

```
/private/var/mobile/Containers/Shared/AppGroup/{GUID}/telegram-data/{account_id}/postbox/
```

The GUID is assigned at install time and changes if the app is reinstalled. Inside the `postbox/` directory you will find a `db/` subfolder con...