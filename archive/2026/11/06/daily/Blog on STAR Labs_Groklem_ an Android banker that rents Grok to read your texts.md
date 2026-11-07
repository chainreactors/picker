---
title: Groklem: an Android banker that rents Grok to read your texts
url: https://starlabs.sg/blog/2026/11-groklem-an-android-banker-that-rents-grok-to-read-your-texts/
source: Blog on STAR Labs
date: 2026-11-06
fetch_date: 2026-11-07T07:59:50.010095
---

# Groklem: an Android banker that rents Grok to read your texts

[![STAR Labs](/images/logo.png)](/)

[About](/about/)
[Services](/services/)
[Advisories](/advisories/)
[Blog](/blog/)
[Achievements](/achievements/)
[Publications](/publications/)
[Team](/team/)
[RSS](/index.xml)

MENU

Research
November 6, 2026
By Jacob Soo
28 min read

# Groklem: an Android banker that rents Grok to read your texts

![GROKLEM, the rent-an-AI banker: a parody movie one-sheet. An eye with a dollar-sign pupil reads SMS bubbles (OTPs, balances, PIN resets) rising from a smartphone, over the tagline “She reads every message. She already knows your balance.” Billing block: starring Grok-4.20-non-reasoning as the oracle, a stolen SMS inbox, the device’s own ADB daemon and a silent accessibility grant; rated M for malware.](/blog/2026/images/fig00-poster-groklem.png)

A bank OTP lands on a phone somewhere in South Asia. Before the owner has even glanced at it, a background service has copied the message, scraped the last ten days of their texts to go with it, and shipped the bundle off with one instruction: *find the money*. Seconds later an answer comes back, not to the victim, but to a stranger on the other end of a socket: a tidy JSON summary of the victim’s bank accounts, their latest balance, and a guess at what’s in there right now. OTPs, card alerts, PIN resets, all sorted and labelled. The thief never read a single text himself.

He didn’t have to. He rented someone smarter. The service reading those messages is **xAI’s Grok** and the malware is just the courier that feeds it.

For lack of a better word, I named it Groklem. The theft is the boring part: Android banking trojans have been siphoning SMS over the same raw-TCP plumbing for a decade. What is new is that this one doesn’t bother to understand what it steals. Working out which bank a victim uses, which message is a balance and which is spam, how much money is in the account, that is the hard, fiddly work that used to take a human analyst or a brittle pile of hand-written rules. Groklem skips it. It hands your texts to a frontier model and lets the model do the thinking.

There is a catch for the operator, and it is the most interesting thing in the whole sample: the Grok key is not in the malware. None of the six payloads we unpacked carries one. The code is built so each operator supplies their *own* xAI key at runtime, pushed in over the C2 command channel, and the malware then attaches that key as the `Authorization: Bearer` token on its calls to Grok. That is a claim about what the code does, traced statically through the binary, not something we watched happen: we did not run the sample and every build we have ships unprovisioned with the feature switched off until a key arrives, so no key ever crossed the wire for us to capture. But the path is unambiguous in the bytecode (the next sections walk it end to end), and the design has a consequence the operator cannot avoid: the one credential that turns the feature on authenticates their own paid xAI account, so if they ever provision it, it is also a receipt with their name on it. And the sample is not a one-off. Six builds, two different packers, six different C2 servers, six different lures, all beaconing home to the same Telegram chat. One operator, running a production line.

The rest of this writeup follows that production line end to end: the anti-analysis packer, the raw-TCP command channel, the full command set, the Grok pipeline from stolen text to financial dossier, and the thread that ties all six builds back to one person.

## The name

We gave this family the name, **Groklem**, a portmanteau of Grok and golem. A golem is a mindless body animated by an external word; here the animating word is a rented Grok key. The malware has no intelligence of its own: it is a courier-body that scoops up a victim’s SMS, hands them to a frontier model, and acts on whatever verdict comes back. The thinking is rented, the code just carries the messages and does what it is told, so that is what we call it.

(The binary’s own debug log tag is `Main_Socket`, misspelled `MianSocket` once in the Telegram beacon; we keep both only as hunt strings in the indicators, not as the family name.)

## Sample

|  |  |
| --- | --- |
| Dropper SHA-256 | `0b0367d67d16658ad6dd850b3df3848f0e95c2d87bfa75f8a1ac9e55c7af2b5f` |
| Dropper MD5 | `c3ba064323d1662893550ba9b67bfb1f` |
| Payload dex SHA-256 | `0bf9340d048a941a709d2546a5883d50588e985cf2767fbf1d9aea75e354b655` |
| First seen | 2026-11-05 |
| Outer package | `com.sov.gxwmrppjo.wvnrts.xflal` (loader) |
| Inner package | `com.cdcp.wjqdfnw` (payload, obfuscated to `z9q4n3k8x1m7`) |
| Internal log tag | `Main_Socket` (`MianSocket` once in the Telegram beacon); detection string only |
| Signing cert | `a40da80a59d170caa950cf15c18c454d47a39b26989d8b640ecd745ba71bf5dc` |

That certificate is the stock **Android debug certificate** (CN=Android, Mountain View). It signs huge numbers of unrelated apps and is **not** a family anchor; do not pivot on it.

## Stage 0: the packer (and its anti-analysis)

The APK ships a thin `Application` subclass and one 1.9 MB encrypted asset. The loader class `cYqRgQJmQpdmWf7rSZtNNxtZcc0PL` is hardened against decompilers: jadx fails to produce either Java **or** smali for its methods (`DecodeException: newPosition < 0` on decompile, `Invalid element width: 5` on disassembly), from crafted dex corruptions that break tooling without affecting the runtime. The `AndroidManifest.xml` is also inflated into a zip-bomb shape (168 KB compressed, 54 MB uncompressed), which is why static manifest parsers return nothing for these samples.

![jadx cannot decompile the loader: an obfuscated Application subclass with a 33-entry string table and a hard decode failure on every method](/blog/2026/images/fig07-packer-loader-antianalysis.png)

Read from raw dex, `attachBaseContext` is simple:

```
in = DataInputStream(getAssets().open("pPogPmRHrE"))
in.skipBytes(24); n = in.readInt()
for i in 0..n:
    len = in.readInt(); buf = new byte[len]
    for j in 0..len:
        buf[j] = (byte)(((in.readByte() ^ 0xD1) - 178) ^ 0x4E)   # per-byte transform
    GZIPInputStream(buf) -> getDir("p_dex")/payload_<i>.dex
ihdozmtf(ctx, <joined paths>, dir)   # reflection class-loader -> real Application
```

Reimplemented, that recovers one payload dex, byte-identical to the analysed code: SHA-256 `0bf9340d048a941a709d2546a5883d50588e985cf2767fbf1d9aea75e354b655` (3,658,408 bytes, magic `dex\n039`). Everything below is that inner dex.

## Where the signals point: India and Bangladesh

The hardcoded artifacts lean toward two countries. This is where the baked-in signals point, not a confirmed victim set: because bank identification is delegated to Grok (below), the malware itself is not geographically constrained, so treat the following as indicators of intent rather than proof of who was hit.

**India.** The lure is **eChallan**, the Indian government’s traffic-fine service, carrying its real URL `https://echallan.parivahan.nic.in/challan` (`appname` / `web_site_link` in `z9q4n3k8x1m7.pp0`, in the config figure below). And the accessibility engine `com.cdcp.wjqdfnw.PZjnhgSFxw.r0` carries a hardcoded hook for `com.phonepe.app`, India’s dominant UPI payment app: `event.getPackageName().equals("com.phonepe.app")`, present in five of the six builds.

**Bangladesh.** The Grok SMS prompt ships with a worked example built around `"service": "bKash"`, Bangladesh’s dominant mobile wallet, and `"currency": "BDT or other"`, the Bangladeshi Taka. That is not incidental: you do not pick bKash and BDT as your default example unless Bangladesh is a target, and the rule sitting right next to it, `"Currency must be auto-detected. Do NOT hardcode only BDT."`, is the operator telling the model to look past the BDT default they started from.

Two more details fit the same picture across all six builds: a government-themed companion-app package name `com.mentorship.national.govt` (the separate installer the RAT delegates ...