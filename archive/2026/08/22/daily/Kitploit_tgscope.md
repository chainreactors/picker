---
title: tgscope
url: https://kitploit.com/en/tools/github/itsmoorgrove/tgscope
source: Kitploit
date: 2026-08-22
fetch_date: 2026-08-23T02:57:09.892656
---

# tgscope

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

tgscope — Telegram OSINT, scraping and archival as a local web app. Multi-account collection, profile lookup with historic photos and change diffs, ten export formats. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/itsmoorgrove/tgscope

![](https://assets.kitploit.com/production/public/tools/50674/6510d9a24d76b7e7be23ef6c5ada0068d3421213d08d78f3885b63cb68909486-display-v1.webp)

[OSINT (Open Source Intelligence)](/en/categories/osint)[Information Gathering](/en/categories/information-gathering)[Digital Forensics](/en/categories/digital-forensics)[Crawler](/en/categories/crawler)

![GitHub](/providers/github.png)itsmoorgrove/tgscope

# tgscope

Telegram OSINT, scraping and archival as a local web app. Multi-account collection, profile lookup with historic photos and change diffs, ten export formats.

[View Repository](https://github.com/itsmoorgrove/tgscope)

21h 3m ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# tgscope

**Telegram OSINT, scraping and archival.**
A local web app that runs entirely on your machine and talks only to Telegram.

![Walkthrough of the tgscope interface](https://assets.kitploit.com/production/public/readmes/50674/6510d9a24d76b7e7be23ef6c5ada0068d3421213d08d78f3885b63cb68909486/5eb5f470c28f29c04e6be1e1bb901dce301165d167ac4f5ea486078da24049f2-display-v1.webp)

root@kitploit:~

```
npm install
npm start
```

Then open **<http://127.0.0.1:5173>**. The first run walks you through API credentials, a QR sign-in
and loading your dialogs. Telegram is the only server it talks to. There is no account to create,
no telemetry and no service in between: what you collect stays in a SQLite file you own.

Successor to `telegram-scraper`, `telescope` and `Harrier`, built on Telethon 1.44.

|  |  |
| --- | --- |
| **Collect** | Channels, groups and forum topics across several accounts, with media, dedup and resume |
| **Investigate** | Phone, `@username`, id or `t.me` link to a profile, every historic photo, and a diff since last time |
| **Export** | Ten formats, from a plain CSV to a hashed evidence bundle |
| **Runs on** | Node 18+, Python 3.12+, SQLite. One database, one folder, no services |

## What it does

**Collect**

* Every channel, group, forum topic and chat, across every signed-in account, in one selectable
  tree with the full `-100` id alongside the name and a badge for the account that sees it
* Each dialog is collected under the account that can actually read it, so a selection spanning two
  accounts starts one run per account
* Messages with full metadata: views, forwards, reactions, edit dates, albums, polls, geo, links,
  reply chains, post authors and the forward source of every message
* Forum groups split by topic — collect single topics rather than whole groups
* Media downloaded in parallel and deduplicated by SHA-256 and Telegram file id, so a file
  forwarded to five channels is stored once
* Resume from a per-dialog watermark; continuous mode re-checks on an interval
* Saved collections re-run a selection with one click

**Investigate**

* Look up a phone number, `@username`, user id or `t.me` link
* Bio, flags, last-seen precision as a privacy indicator, chats in common, personal channel
* Anything Telegram chooses to volunteer about the account: the month it was registered, the
  country its phone number belongs to, when the person last renamed themselves or swapped their
  photo, their auto-delete timer, the name shown on restricted forwards. Be warned that it usually
  volunteers none of it. Those fields ride along on the anti-scam panel Telegram shows when a
  stranger writes to you, and come back empty for a profile you look up directly, so treat them as
  a bonus rather than something to plan around
* Business accounts do reliably give a street address, coordinates and a timezone
* **Every** visible profile photo, hashed with SHA-256 and a perceptual hash, shown as a gallery
* Perceptual hashes are matched across accounts, so the same picture on a second profile surfaces
* Message senders are recorded as they are scraped, so a name in the browser is a working link to a
  lookup even when the person has no username; "Sync members" fills that in for anything collected
  earlier
* Every lookup is snapshotted and diffed: username changes, display-name changes, bio edits, photos
  added or removed, changed privacy

**Export**

## Requirements

* Node.js 18+
* Python 3.12+
* API credentials from [my.telegram.org/apps](https://my.telegram.org/apps)

`npm install` creates the Python environment under `server/.venv` and installs both sides.

## Where things live

| What | Where |
| --- | --- |
| Config | `~/.config/tgscope/config.json` (mode 600) |

One database holds everything, which is what makes cross-dialog search, the shared user table,
media dedup and the forward graph possible.

### Media layout

Files are filed by dialog type, then dialog, then forum topic, then media kind:

root@kitploit:~

```
media/
├── channels/technews_-1002116176890/
│   ├── photos/00004711-8001-conference-slides.jpg
│   └── documents/00004802-8210-quarterly-report.pdf
├── groups/pythondev_-1001597139842/
│   ├── general/photos/…
│   └── help/voice/00000004-9004-voice.ogg
└── profiles/123456789/000-5544332211.jpg
```

Directory names combine the handle with the full id, non-ASCII titles are transliterated, and file
names are zero-padded so they sort chronologically.

## Rate limits and account safety

Every Telegram call goes through a per-account governor with a token bucket and `FloodWait`
backoff, and every paged read - messages, dialogs, members, profile photos - waits a flood out and
resumes rather than failing the run. Three profiles:

Longer waits are announced in the activity log and waited out; twelve in a row on one read gives
up and reports it.

Multiple accounts are supported. Mark one as a **burner** in Settings and phone lookups run on it
automatically, because that is the one risky operation:

> A phone lookup imports the number as a contact for a moment and deletes it again. If the owner
> already has your number saved, they may see a "joined Telegram" notification. tgscope asks first,
> every time, and the profile card records which account it used.

## Development

root@kitploit:~

```
npm test                    # 92 backend and 42 frontend tests, no network needed
npm run build               # production bundle of the client
```

The backend is FastAPI over a Telethon core, tested against a fake Telethon client: the scraper,
the exporters, the media layout and every schema migration. The frontend tests cover the pure logic
behind the browser, period arithmetic, histogram bucketing and the number and timestamp formatting,
and render every screen twice, once empty and once populated.

`scripts/demo/` regenerates `docs/preview.gif` from seeded fake data. It needs `chromium` and
`ffmpeg`, touches nothing in your real workspace, and is not part of the app.

**The source carries no comments** — naming and structure carry the meaning, and a test ...