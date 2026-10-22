---
title: Cellebrite’s Advanced Unlocks and the case of the missing iPhone 17
url: https://andreafortuna.org/2026/10/21/cellebrite-advanced-unlocks/
source: Instapaper: Unread
date: 2026-10-21
fetch_date: 2026-10-22T06:46:41.855365
---

# Cellebrite’s Advanced Unlocks and the case of the missing iPhone 17

[Andrea Fortuna](/)
[ ]

[About](/about/)[Search](/search/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# Cellebrite's Advanced Unlocks and the case of the missing iPhone 17

Oct 21, 2026

by [Andrea Fortuna](/about/)

Most vendor datasheets tell you what a product does. The one Cellebrite circulates for its new **Advanced Unlocks** service also tells you how far away you can stand while it does it: about eight meters, or 26 feet for customers who think in imperial. Nobody puts a range on a cable. Once I read that line, the rest of the page started to look like a puzzle with a missing piece, and a researcher at [justin.sh](https://justin.sh/blog/2026/10/cellebrite-advanced-unlocks/) has spent weeks trying to work out what the piece is.

His post reached me by email, sent by the author himself, which I took as a polite invitation to poke at it. So I did. What follows is a review of the argument rather than a retelling, with my own opinions attached and a clear line between what the post demonstrates and what it merely suggests.

![cover](/assets/2026/cellebrite-advanced-unlocks.jpg)

## In brief

* A leaked Cellebrite **Advanced Unlocks** datasheet quotes a working range of about eight meters, which points to a wireless vector rather than a cable.
* The coverage stops at the iPhone 16 and iOS 26.4+, leaving the entire iPhone 17 generation and every release since March unsupported.
* A diff of the **bluetoothd** binary between iOS 26.4 and 26.5 turned up a use-after-free in the pre-pairing L2CAP path that could become remote code execution.
* The iPhone 17’s switch to Apple’s own N1 chip does not explain the gap, but **Memory Integrity Enforcement** (MIE) plausibly does.
* Apple patched the Bluetooth code silently, with no CVE, while Cellebrite has been unusually specific about range and appliance requirements.
* If the theory holds, a single point release closed a commercial capability within months, and AFU state becomes fragile evidence that examiners must handle carefully.

## What the datasheet promises and what it leaves out

![cover](/assets/2026/flyer-2026-09-15-large.jpg)

The document is marked CONFIDENTIAL and the author keeps the original under wraps to protect his source, so I am reading it through his screenshots, with the usual caveat that I have not seen the file itself. On the page, Advanced Unlocks (AU from here on) offers **AFU** access, meaning After First Unlock: the phone has been unlocked at least once since boot, so the data protection keys sit in memory and the Secure Enclave will hand them to the kernel on request. The coverage is iPhone 11 to 16 on iOS 26 through 26.4+, with more models promised later. It reportedly works even with Stolen Device Protection enabled, a feature that, as [Elcomsoft explained earlier this year](https://blog.elcomsoft.com/2026/06/forensic-implications-of-apple-stolen-device-protection/), tightens the USB restrictions forensic tools rely on. Every lab needs one dedicated appliance, online deployments require whitelisting, on-prem ones a dedicated server, and the whole thing is sold next to UFED and Inseyets, not instead of them. The pitch is a vector that is “more resilient to Apple’s OS changes”, which in the current climate is the sentence every mobile examiner most wants to read and least expects to be true.

The interesting part is the revision history. The author compared the three versions of the flyer with the iOS releases available on the day each one was issued. In March the datasheet claimed 26.3+, when 26.3.1 was the newest build. In May it claimed up to 26.4.2, nine days after 26.5 shipped. By the September revision it still said 26.4+, a day after iOS 26.7 and iOS 27 appeared. Read charitably, “26.4+” means “and newer, trust us”. Read the way the author reads it, support stopped at 26.4 and the gap has been widening ever since. The iPhone 17 and Air, on the market for about a year, are missing as well, and the flyer does not say whether the SE and e models fall inside “11 to 16”.

I would not hang a theory on a version string. Datasheets are written by people paid to be vague, and a number that has not been updated may simply mean nobody opened the template. What the pattern does is raise a question, and the post’s value lies in how seriously it tries to answer it.

## From eight meters to a Bluetooth daemon

The reasoning starts from the range. The author went through the radios in an iPhone and found that the cellular modem and NFC did not fit, while Bluetooth matched Apple’s own figure of about ten meters rather well. That is an inference, and a good one, but it is worth saying plainly that the datasheet never mentions Bluetooth. Everything below hangs on that first step.

From there he did what researchers do with a suspect: he diffed the patches. He compared the **bluetoothd** binary in iOS 26.4 and 26.5, the daemon that manages every Bluetooth connection on the phone and holds a broad set of entitlements, and found a small cluster of security changes, all in **L2CAP**, the multiplexing layer between the radio and everything above it. The relevant detail is that L2CAP signaling messages are processed before pairing, so any device within range can send them without anyone touching the screen.

One fix stands out. In the channel manager, the loop that receives aggregated L2CAP packets walks through the open connections and calls each one’s handler. In 26.4, if a handler freed its connection object halfway through, the loop kept going with a dangling pointer. That is a textbook **use-after-free**, the kind of memory bug that, with enough skill and patience, becomes code execution. The vulnerable code has been around since at least iOS 17 and probably became easier to exploit when Apple restructured the connection manager in iOS 18. The author is honest that he has not built an exploit, and he separates this bug from a second one in the reassembly path that needs an established channel and is therefore a worse candidate.

Then comes the part that made me raise an eyebrow. iOS 26.6 added bounds checks elsewhere in the Bluetooth stack, and iOS 26.7 and 27 fixed CVE-2026-65414, a separate and uncredited Bluetooth remote code execution bug that lands in the same aggregated-packet path, only earlier. Apple hardened that exact code in 26.5 and was still sitting on a remote code execution flaw in it two releases later.

Put together, the theorized chain goes like this: crafted packets over the air, a hijacked Bluetooth daemon, an escalation to the kernel through one of the many IOKit connections the daemon holds, and finally USB restrictions lifted and the phone imaged over the cable. No passcode is cracked at any point. It is consistent with the Stolen Device Protection claim too, since by the time anyone plugs in a cable the kernel is already compromised.

Here is where I part ways with the post’s enthusiasm. The diff is the solid piece, because anyone with two firmware images and a disassembler can reproduce it, and the bug quite probably exists exactly as described. What cannot be checked is the link between that bug and a commercial product. The chain rests on a range, a stalled version number and a plausible code path, and any pre-authentication parser that received a fix will look plausible to someone who is looking for a candidate. The CVE finding cuts both ways: it shows a target-rich surface, which makes a working exploit believable, and it also means the 26.5 fix was not the only thing standing in the way. The author says as much, and flags the rest of the post as speculation. He deserves credit for that.

## Why the iPhone 17 is the best clue

If I had to pick the single most persuasive argument in the post, it is the hardware gap. Starting with the 17 generation, Apple replaced the Broadcom Bluetooth chip with its own N1 in the 17, 17 Pro and Air, but the 17e kept Broadcom. If AU depended on Broadcom c...