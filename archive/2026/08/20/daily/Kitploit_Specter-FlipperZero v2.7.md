---
title: Specter-FlipperZero v2.7
url: https://kitploit.com/en/posts/github-at0m-b0mb-specter-flipperzero-v27
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:27.074194
---

# Specter-FlipperZero v2.7

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/42070/5e58ca77d3caccf3c1102ab897985174b22fc5fe0d826371230e52a176c35aca.png)

New releaseAug 20, 2026

# Specter-FlipperZero v2.7

👻 Specter — passive 13.56 MHz NFC reader/skimmer bug-sweep for Flipper Zero. Counter-surveillance EMF meter using the onboard NFC chip. No extra hardware.

Share

![Specter — NFC reader & skimmer bug-sweep for Flipper Zero](https://assets.kitploit.com/production/public/readmes/42070/74bc06f0a6a1b0731b4768b4256f662b34a582f5b9701a9bce44cb1b10bedd0d.png)

# Specter 👻

*Sweep for the readers you can't see.*

![Flipper Zero](https://img.shields.io/badge/platform-Flipper%20Zero-FF8200?style=for-the-badge&logo=flipper&logoColor=white)
![Version 2.3](https://img.shields.io/badge/version-2.3-FF3DAE?style=for-the-badge)
![Onboard NFC](https://img.shields.io/badge/radio-13.56%20MHz%20NFC%20(onboard)-26E8CA?style=for-the-badge)
![No extra hardware](https://img.shields.io/badge/hardware-none%20required-9B5DE5?style=for-the-badge)
![ufbt](https://img.shields.io/badge/build-ufbt-2da0ff?style=for-the-badge)
![MIT](https://img.shields.io/badge/license-MIT-3ad17a?style=for-the-badge)

**Specter** turns your Flipper Zero into a pocket **counter-surveillance bug-sweep** for
**active 13.56 MHz NFC readers**. It *passively listens* for the RF field that a powered-on
reader is constantly emitting — a hidden card skimmer slipped into a payment terminal, a covert
reader behind a door panel, a rogue logger taped under a desk — then tells you **where it is**,
**what kind of thing it is**, **whether the room is clean**, and — left on watch — **the
moment one appears while you're away**. It never transmits.

The readers are invisible. Specter makes them visible.

---

## 📟 On the Flipper

![Specter screens](https://assets.kitploit.com/production/public/readmes/42070/699dd459291672508e6afe010c4ce78feab043f271829d084276afdfff49f3fe.png)

**Sweep** (quiet)  ·  **Sweep** (reader locked)  ·  **Fingerprint**  ·  **Survey** (running)  ·  **Survey** (verdict)
**Watch** (clear)  ·  **Watch** (reader!)  ·  **Logbook**  ·  **Calibrate**  ·  **Settings**

---

## ✨ What it does

Specter answers four different questions — *where is it, what is it, is the room clean,* and *did one
show up while I was away* — and each has its own screen.

### 🔍 Sweep — *where is it?*

![Sweep — active reader found](https://assets.kitploit.com/production/public/readmes/42070/aa65e60e27ed187f32a080df23e848faf38b04bd43f19868c973f0c68b2f0227.png)

The showpiece: an **analog-style EMF gauge**. The needle rides the **FIELD %** in real time, a
peak-hold marker remembers the strongest hit, and the top of the dial is a **hot zone**. A live
waveform traces the noise floor while it's quiet.

The instant a reader's carrier is sensed the screen frames itself in an **alarm border**, a throb
ring pulses around the dial, and the strip flips to **`● ACTIVE READER`** with a proximity readout
(`FAINT → NEAR → CLOSE → STRONG`). Optional **geiger clicks speed up as the field gets stronger**, so
you can sweep a surface with the Flipper in your pocket and *hear* yourself getting warmer.

`OK` resets peak/contacts · `hold OK` logs the reading · `LEFT` calibrates to the room you're in.

### 🔬 Fingerprint — *what is it?*  `NEW in 2.0`

![Fingerprint — polling reader identified](https://assets.kitploit.com/production/public/readmes/42070/32d848018dfcafd8bfaa20fda954e922f9ac8c7534de54fac861c35f6c5d496c.png)

Found something? Hold still on it. Specter stops chasing proximity and starts **timing the carrier's
on/off edges**, then tells you what kind of emitter you're looking at:

| Class | What it means |
| --- | --- |
| **CONTINUOUS** | Carrier held permanently up |
| **POLLING** | Fixed poll cycle — the period is shown in ms |
| **INTERMITTENT** | Bursty but irregular |

You get the **polling period**, **burst width**, **jitter**, **duty-cycle** and a **confidence bar** —
plus a **logic-analyser pulse train** of the raw carrier along the bottom, so the verdict is never
asked to be believed on its own. A reader's polling loop is crystal-timed, so a genuine poll shows up
as an unmistakable square wave.

`OK` saves the finding to the logbook · `hold OK` restarts the measurement.

### 🗺️ Site Survey — *is this room clean?*  `NEW in 2.0`

![Site Survey — verdict](https://assets.kitploit.com/production/public/readmes/42070/f76773c10ad1e58d4b0ae5fa67f9d0cd3ebcfd748e928166c7e90082d962de6a.png)

A **timed sweep** of a whole space. Start it, walk the room, and get **one verdict** at the end
instead of having to watch a needle the entire time:

* **`CLEAN`** — nothing crossed the noise floor
* **`TRACE`** — brief or faint hits, worth a second pass
* **`ACTIVE READER`** — something was up and emitting for real

…with max/average field, contact count, and **how much of the survey a carrier was actually up**.
Runs for 30 s, 60 s or 2 min, and auto-logs the result.

### 🛰️ Watch Mode — *tell me if one shows up*  `NEW in 2.1`

![Watch Mode — reader present](https://assets.kitploit.com/production/public/readmes/42070/567845e8106ba7dcdbd37d3464add123cdef6ae343ac549fd6c98f336b29a5f2.png)

Where Sweep is you hunting and Survey is a bounded verdict, **Watch stands guard indefinitely**. Arm
it, set the Flipper down, and walk away. It keeps a running clock and a **detection count**, remembers
**when the last contact was**, and — the whole point — **wakes the screen and sounds off the instant a
reader appears**. Each new contact is auto-logged with its timestamp.

It deliberately **ignores stealth**: a silent, dark guard that never tells you it saw something would
be worse than useless. `OK` re-arms it (clears the count and clock).

### 📖 Logbook + live CSV  `CSV NEW in 2.1`

Every finding is written **twice, from one action** — so it's readable on the device *and* already a
spreadsheet, with no export step to remember:

| `logbook.txt` — grouped, for the on-device viewer | `logbook.csv` — one flat row per entry |
| --- | --- |
| root@kitploit:~   ``` 2026-07-18 14:35:11   SURVEY 60s ACTIVE max74… 2026-07-18 14:32:07   READER POLLING 204ms… ``` | root@kitploit:~   ``` timestamp,type,detail 2026-07-18 14:35:11,SURVEY,60s ACTIVE … 2026-07-18 14:32:07,READER,POLLING 204ms … ``` |

Both live in `apps_data/specter/` on the SD card. Nothing leaves the device.

### 🎯 Auto-calibration  `NEW in 2.0`

Press **LEFT** on the Sweep screen and Specter listens to the **ambient noise floor for 3 seconds**,
then sets the detection threshold just above whatever it measured — saved as your **Custom**
sensitivity. Every room has a different RF floor; this tunes to the one you're standing in rather
than a number baked in at build time.

### 🕶️ Stealth mode  `NEW in 2.0`

Keeps the **screen and LED dark** for the whole sweep, so the Flipper doesn't glow while you're the
one doing the looking. Sound and vibration keep working — the point isn't to disable the feedback
you're sweeping by. Exiting a stealth screen **re-lights the display**, so `BACK` always lands you on
a lit menu (fixed in 2.2 — it used to leave the screen dark, which made `BACK` look dead).

### 📏 Reading the meter  `FIXED in 2.3`

**Why a reader you're touching doesn't emit 100% of the time.** The detector measures one physical
thing: what fraction of the time a 13.56 MHz carrier is actually up. But readers **poll** — a short
burst, a sleep, another burst. A typical terminal or access reader is only radiating **20–35% of the
time**, so raw duty-cycle *saturates* around 30% no matter how close you get.

Specter used to print that raw number on the gauge, which made a perfect detection look like...