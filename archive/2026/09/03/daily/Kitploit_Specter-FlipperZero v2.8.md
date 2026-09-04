---
title: Specter-FlipperZero v2.8
url: https://kitploit.com/en/posts/github-at0m-b0mb-specter-flipperzero-v28
source: Kitploit
date: 2026-09-03
fetch_date: 2026-09-04T06:42:34.773331
---

# Specter-FlipperZero v2.8

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

New releaseSep 3, 2026

# Specter-FlipperZero v2.8

👻 Specter — passive 13.56 MHz NFC reader/skimmer bug-sweep for Flipper Zero. Counter-surveillance EMF meter using the onboard NFC chip. No extra hardware.

Share

![Specter — NFC reader & skimmer bug-sweep for Flipper Zero](https://assets.kitploit.com/production/public/readmes/42070/74bc06f0a6a1b0731b4768b4256f662b34a582f5b9701a9bce44cb1b10bedd0d.png)

# Specter 👻

*Sweep for the readers you can't see.*

[![Latest release](https://img.shields.io/github/v/release/at0m-b0mb/Specter-FlipperZero?style=for-the-badge&color=FF3DAE&labelColor=0a0f16)](https://github.com/at0m-b0mb/Specter-FlipperZero/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/at0m-b0mb/Specter-FlipperZero/total?style=for-the-badge&color=26E8CA&labelColor=0a0f16&label=downloads)](https://github.com/at0m-b0mb/Specter-FlipperZero/releases)
[![Stars](https://img.shields.io/github/stars/at0m-b0mb/Specter-FlipperZero?style=for-the-badge&color=FFB000&labelColor=0a0f16)](https://github.com/at0m-b0mb/Specter-FlipperZero/stargazers)
[![Build](https://img.shields.io/github/actions/workflow/status/at0m-b0mb/Specter-FlipperZero/build.yml?branch=main&style=for-the-badge&labelColor=0a0f16&label=build)](https://github.com/at0m-b0mb/Specter-FlipperZero/actions/workflows/build.yml)

![Flipper Zero](https://img.shields.io/badge/platform-Flipper%20Zero-FF8200?style=for-the-badge&logo=flipper&logoColor=white&labelColor=0a0f16)
![Onboard NFC](https://img.shields.io/badge/radio-13.56%20MHz%20NFC%20(onboard)-26E8CA?style=for-the-badge&labelColor=0a0f16)
![No extra hardware](https://img.shields.io/badge/extra%20hardware-none-9B5DE5?style=for-the-badge&labelColor=0a0f16)
![Listen-only](https://img.shields.io/badge/transmits-never-3ad17a?style=for-the-badge&labelColor=0a0f16)
![MIT](https://img.shields.io/badge/license-MIT-2da0ff?style=for-the-badge&labelColor=0a0f16)

**Specter** turns your Flipper Zero into a pocket **counter-surveillance bug-sweep** for
**active 13.56 MHz NFC readers**. It *passively listens* for the RF field that a powered-on
reader is constantly emitting — a hidden card skimmer slipped into a payment terminal, a covert
reader behind a door panel, a rogue logger taped under a desk — then tells you **where it is**,
**what kind of thing it is**, **whether the room is clean**, and — left on watch — **the
moment one appears while you're away**. It never transmits.

The readers are invisible. Specter makes them visible.

**As featured in**
[Help Net Security](https://www.helpnetsecurity.com/2026/07/29/specter-flipper-zero-skimmer-detector/)
 ·
[Cyber Security News](https://cybersecuritynews.com/specter-with-flipper-zero/)

---

## 📟 On the Flipper

![Specter in use: sweeping a quiet room, closing in on a reader, locking on at MAX, fingerprinting its polling cadence, then a site-survey verdict](https://raw.githubusercontent.com/at0m-b0mb/specter-flipperzero/main/images/demo.gif)

A sweep, start to finish: quiet room → closing in → locked on → **what** it is → the room's verdict.

![Specter screens](https://assets.kitploit.com/production/public/readmes/42070/699dd459291672508e6afe010c4ce78feab043f271829d084276afdfff49f3fe.png)

**Sweep** (quiet)  ·  **Sweep** (reader locked)  ·  **Fingerprint**  ·  **Survey** (running)  ·  **Survey** (verdict)
**Watch** (clear)  ·  **Watch** (reader!)  ·  **Logbook**  ·  **Calibrate**  ·  **Settings**

---

## ✨ The five modes

Specter is five tools around one sensor. Each answers a different question, so
the right one depends on what you are actually trying to find out:

| Mode | The question it answers | Use it when |
| --- | --- | --- |
| 🔍 **Sweep** | *Where is it?* | You suspect a device and want to pinpoint it by moving around |
| 🔬 **Fingerprint** | *What kind of thing is it?* | You have found an emitter and want to know how it behaves |
| 🗺️ **Site Survey** | *Is this room clean?* | You want one verdict for a whole space, hands-free |
| 🛰️ **Watch Mode** | *Did one appear while I was away?* | You are leaving the Flipper somewhere to stand guard |
| 📖 **Logbook** | *What did I find, and when?* | You are writing it up, or comparing today with last week — filter by finding type |

---

### 🔍 Sweep — *where is it?*

![Sweep — reader found, meter pegged](https://assets.kitploit.com/production/public/readmes/42070/06802c4e2722498a0d83928c4264833ca0a767e5e157f9c221c4d5a6f56f2fbe.png)

**What it does.** A live EMF-style meter. Hold the Flipper flat and move it slowly
over the thing you're checking — a card terminal, a door reader, the underside of
an ATM lip, a parcel, a desk. The needle rides the field strength in real time.

**What you see.**

* **The dial** — needle = live reading, the small dot = *peak-hold* (the strongest
  spot you've touched, so you can compare positions).
* **`FIELD %`** — the same reading as a number, with a **▲ / ▼ trend arrow**
  telling you whether the last half-second made things *warmer or colder*. When
  you're hunting, that arrow matters more than the number.
* **`PK` / `C`** — peak reading and how many separate contacts you've had.
* **Bottom strip** — the live waveform and your current sensitivity while quiet;
  it flips to a black **`● ACTIVE READER`** alarm bar with a proximity word the
  moment a carrier is detected.
* **Proximity** — `FAINT → NEAR → CLOSE → STRONG → MAX`. `MAX` means the meter is
  *pegged*: you're as close as this measurement can resolve.

**Sound.** Optional geiger clicks that **speed up as you get closer**, so you can
sweep with the Flipper in your pocket and hunt by ear alone.

| Key | Action |
| --- | --- |
| `OK` | Reset peak-hold and contact count |
| `hold OK` | Save this reading to the logbook |
| `LEFT` | Calibrate to the room's noise floor (3 s) |

### 🔬 Fingerprint — *what kind of thing is it?*

![Fingerprint — polling reader identified](https://assets.kitploit.com/production/public/readmes/42070/32d848018dfcafd8bfaa20fda954e922f9ac8c7534de54fac861c35f6c5d496c.png)

**What it does.** Once Sweep has found something, hold the Flipper **still**
against it. Fingerprint stops measuring proximity and starts **timing the
carrier's on/off edges**, which is what actually distinguishes one kind of
emitter from another.

**What you see.** A verdict, a confidence bar, and the evidence behind both:

| Class | What it means in practice |
| --- | --- |
| **CONTINUOUS** | The carrier is held permanently up |
| **POLLING** | A fixed, crystal-timed poll cycle — the period is shown in ms |
| **INTERMITTENT** | Bursty but irregular — often a phone or a reader in use |

Underneath are `PER` (poll period), `BST` (burst width), `JIT` (jitter) and
`DUTY` (true duty-cycle), plus a **logic-analyser pulse train** of the raw
carrier — so the verdict is never something you have to take on faith. A genuine
polling reader shows up as an unmistakable square wave.

> A `~` before a timing means it's close to the 2 ms sampling floor, and the
> confidence is discounted to match.

| Key | Action |
| --- | --- |
| `OK` | Save the finding to the logbook |
| `hold OK` | Restart the measurement |

### 🗺️ Site Survey — *is this room clean?*

![Site Survey — verdict](https://assets.kitploit.com/production/public/readmes/42070/f76773c10ad1e58d4b0ae5fa67f9d0cd3ebcfd748e928166c7e90082d962de6a.png)

**What it does.** A **timed** sweep of a whole space. Start it, walk the room
normally, and get a single verdict at the end — no needle-watching.

**What you see.** A countdown and progress bar while it r...