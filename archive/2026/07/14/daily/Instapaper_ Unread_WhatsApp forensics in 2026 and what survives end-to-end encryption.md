---
title: WhatsApp forensics in 2026 and what survives end-to-end encryption
url: https://andreafortuna.org/2026/07/14/whatsapp-forensics-2026/
source: Instapaper: Unread
date: 2026-07-14
fetch_date: 2026-07-15T04:49:53.737267
---

# WhatsApp forensics in 2026 and what survives end-to-end encryption

[Andrea Fortuna](/)
[ ]

[About](/about/)[Search](/search/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# WhatsApp forensics in 2026 and what survives end-to-end encryption

Jul 14, 2026

by [Andrea Fortuna](/about/)

In March 2026, WhatsApp told roughly 200 people in Italy that their phones had been compromised by a fake client masquerading as the real app. Meta traced the campaign, publicly named [Spyrtacus](https://andreafortuna.org/2026/04/02/spyrtacus-asigint-whatsapp-spyware/), back to a lawful-interception vendor, a story covered extensively by [SecurityAffairs](https://securityaffairs.com/190276/malware/italian-spyware-vendor-creates-fake-whatsapp-app-targeting-200-users.html) and other outlets. A few months earlier, Russian investigators extracting data from a seized phone in the [Cellebrite-Pivovarov case](https://andreafortuna.org/2026/06/28/cellebrite-russia-pivovarov/) (documented forensically by the [Citizen Lab](https://citizenlab.ca/research/russia-breaks-into-human-rights-activists-phone-with-cellebrite/)) pulled messages straight out of WhatsApp, Telegram, and Viber, then searched them for the names of opposition figures.

![cover](/assets/2026/whatsapp-forensics-2026.jpg)

Two very different stories, one shared lesson: **end-to-end encryption** protects the wire, not the endpoint. Once a device is in your hands, WhatsApp leaves behind more forensic material than most users assume, and knowing exactly where to look separates a productive examination from a wasted evening staring at a locked SQLite file.

## In brief

* WhatsApp’s E2E encryption (based on the Signal Protocol) secures messages in transit, but on-device storage remains the real target for forensic acquisition.
* Android stores conversations in `msgstore.db`, contacts in `wa.db`, and encrypted backups in the evolving crypt12/crypt14/crypt15 formats.
* iOS consolidates almost everything into a single `ChatStorage.sqlite` file, which simplifies parsing once you have filesystem access.
* Decryption always requires the key, which lives on the device or in an escrowed backup, never a bypass of the underlying cryptography.
* Open-source tools like `wa-crypt-tools` and `whapa` now handle the full crypt15 pipeline, reducing the gap with commercial suites.
* Timeline correlation across install provenance, accessibility permissions, and network beaconing matters more than the message table alone, especially in spyware cases like Spyrtacus.

## How WhatsApp actually protects your messages (and where that stops)

WhatsApp implements the **Signal Protocol** for message transport, based on the cryptographic framework detailed in the company’s [encryption whitepaper](https://www.whatsapp.com/security/WhatsApp-Security-Whitepaper.pdf). Every message is encrypted client-side before it leaves the sender’s device and decrypted only on the recipient’s. This has been true since 2016, and it is not going away. What it does *not* do is protect data once it lands on disk. The app still needs to render your chat history when you open it, which means a fully decrypted, human-readable copy of every conversation sits in local storage at all times.

This distinction matters enormously for forensic work. Cracking Signal’s Double Ratchet is not on the table, and does not need to be. The actual objective for a forensic examiner is straightforward: get access to the device’s filesystem, then get access to the key material that protects the local database or its backup. As a [TechNadu LinkedIn post](https://www.linkedin.com/posts/technadu_cybersecurity-encryption-digitalforensics-activity-7412884577863671808-_4is) about `wa-crypt-tools` put it bluntly:

> “The weakest link is never the algorithm, it’s access.”

That single sentence explains why lawful intercept vendors, state-sponsored spyware operators, and DFIR practitioners investigating a compromised laptop all converge on the same target: the device, not the wire.

## Android artifacts from msgstore.db to the crypt15 puzzle

On Android, WhatsApp data is split across several files, and the split has grown more complex with each protocol revision:

* `/data/data/com.whatsapp/databases/msgstore.db`, the live, unencrypted message database (chats and messages tables), accessible only with root or a full filesystem extraction.
* `/data/data/com.whatsapp/databases/wa.db`, which stores the contact list.
* `/sdcard/WhatsApp/Databases/msgstore.db.crypt15` (or the older `.crypt12`/`.crypt14`), the encrypted local backup WhatsApp writes daily.
* `/data/data/com.whatsapp/files/key`, a 64-byte key file used to decrypt the backup, present only if the examiner has application-level access.

Older `crypt12` backups used a static key derivation that made recovery trivial once you had the key file. `crypt14` added versioning and a slightly different header structure. `crypt15`, now the default, moved to a **protobuf**-encoded key file with rotating parameters, which broke a lot of older single-purpose decryptors and forced the community to catch up. The most actively maintained answer today is [wa-crypt-tools](https://github.com/ElDavoo/wa-crypt-tools) by ElDavoo, a Python toolkit that understands all three formats end to end.

A typical decryption pass looks like this:

```
pip install wa-crypt-tools

wa-crypt-tools-decrypt15 \
  --key-file /path/to/extracted/key \
  --input msgstore.db.crypt15 \
  --output msgstore_decrypted.db
```

Once decrypted, `msgstore_decrypted.db` is a plain SQLite file. From there, standard SQL gets you a working timeline in minutes:

```
SELECT
  m.timestamp,
  m.key_remote_jid AS contact,
  m.data AS message_body,
  m.media_wa_type AS media_type
FROM messages m
WHERE m.timestamp BETWEEN 1735689600000 AND 1738368000000
ORDER BY m.timestamp ASC;
```

Pairing the decrypted database with [whapa](https://github.com/B16f00t/whapa) adds structured reporting and media correlation on top, which saves a lot of manual joins across the `message_media` and `jid` tables. For a broader Android artifact baseline, the [Magnet Forensics WhatsApp artifact profile](https://www.magnetforensics.com/blog/artifact-profile-whatsapp-messenger) remains a useful reference for database schemas and storage paths, especially given scoped storage restrictions that affect where these files can be pulled from without root.

One caveat worth stressing to anyone new to this: none of this works without the key file, and the key file only exists where the app was legitimately installed and used. There is no shortcut that turns a bare `.crypt15` file into readable chat history, and any tool claiming otherwise is misrepresenting what it can do.

## iOS artifacts and the forensic value of ChatStorage.sqlite

iOS simplifies the picture considerably by keeping almost everything in one place:
`/private/var/mobile/Containers/Shared/AppGroup/<GUID>/ChatStorage.sqlite`

This single SQLite database holds messages, group metadata, contact mapping, and media references, structured around a `ZWAMESSAGE` table (Core Data-backed apps prefix tables with `Z`). A quick look at message content and timestamps:

```
SELECT
  ZWAMESSAGE.ZMESSAGEDATE,
  ZWAMESSAGE.ZTEXT,
  ZWACHATSESSION.ZCONTACTJID
FROM ZWAMESSAGE
JOIN ZWACHATSESSION ON ZWAMESSAGE.ZCHATSESSION = ZWACHATSESSION.Z_PK
ORDER BY ZWAMESSAGE.ZMESSAGEDATE DESC;
```

Note that `ZMESSAGEDATE` uses Core Data’s epoch (seconds since 2001-01-01), not Unix time, a detail that trips up more examiners than it should.

Getting to this file without a jailbreak requires either a full filesystem extraction via checkm8-based tools, or an iTunes-style encrypted backup if the device passcode or backup password is known. If the target has [Lockdown Mode enabled](https://support.apple.com/en-us/105120), expect the attack surface for physical extraction tools to shrink considerably, which is precisely the point of that feature.

WhatsApp on iOS also writes to iCloud when the use...