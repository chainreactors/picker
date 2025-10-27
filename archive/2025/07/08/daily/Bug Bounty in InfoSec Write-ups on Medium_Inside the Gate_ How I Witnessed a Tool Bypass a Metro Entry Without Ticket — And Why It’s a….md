---
title: Inside the Gate: How I Witnessed a Tool Bypass a Metro Entry Without Ticket — And Why It’s a…
url: https://infosecwriteups.com/inside-the-gate-how-i-witnessed-a-tool-bypass-a-metro-entry-without-ticket-and-why-its-a-f795a29f0280?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-08
fetch_date: 2025-10-06T23:24:50.849826
---

# Inside the Gate: How I Witnessed a Tool Bypass a Metro Entry Without Ticket — And Why It’s a…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff795a29f0280&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Finside-the-gate-how-i-witnessed-a-tool-bypass-a-metro-entry-without-ticket-and-why-its-a-f795a29f0280&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Finside-the-gate-how-i-witnessed-a-tool-bypass-a-metro-entry-without-ticket-and-why-its-a-f795a29f0280&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f795a29f0280---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f795a29f0280---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 🧠 Inside the Gate: How I Witnessed a Tool Bypass a Metro Entry Without Ticket — And Why It’s a Security Wake-Up Call

[![Aditya Sunny](https://miro.medium.com/v2/resize:fill:64:64/1*XcAW_t_riaR4a4fPbM4VcA.webp)](https://adityasunny06.medium.com/?source=post_page---byline--f795a29f0280---------------------------------------)

[Aditya Sunny](https://adityasunny06.medium.com/?source=post_page---byline--f795a29f0280---------------------------------------)

3 min read

·

Jun 4, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

ai contant

## 🕵️ A Normal Day, An Abnormal Entry

It was just another busy evening. Rush hour. As I queued at the metro station, something unusual caught my attention.

A man ahead of me approached the entry gate.

* He didn’t scan a card.
* He didn’t carry a token.
* Instead, he held a **small device**, possibly a **key fob or smart tool**.

He waved it subtly in front of the RFID reader.

> *✅ The gate opened — without any official card or beep pattern from a metro token.*

No alarm. No flag. Just a seamless bypass.

## 🔍 Initial Doubt → Deeper Observation

Was it a coincidence? A staff override? A glitch?

But over the next few days, I saw this pattern again — similar devices used by individuals who:

* Didn’t tap any card visibly.
* Didn’t visit the token counters.
* Simply “waved” and entered.

Clearly, something more technical was happening.

## ⚙️ The Hypothesis: NFC UID-Based Gate Exploitation

Modern metro gates use **13.56 MHz NFC tech** like:

* MIFARE Classic (insecure)
* MIFARE DESFire (more secure)
* Other RFID-based tokens

In insecure implementations, gates only validate:

* The **UID (Unique Identifier)** of a card/token
* Not the **cryptographic handshake** with backend servers

## 🧨 That’s where the problem begins.

If the gate trusts only the UID —
 Then any tool that can **emulate or clone a valid UID** can easily **fool** the system.

## 🧪 Technical Breakdown: How The Exploit Might Work

## 🔧 Tools Involved:

Tool Purpose Risk Level **Flipper Zero** Portable NFC/RFID emulator ⚠️ High **Proxmark3** Clone & sniff MIFARE cards 🛠️ Research **ChameleonMini** UID replay & real-time emulation 🔥 Critical **Custom Keyfobs** Pre-flashed clones sold online ❗Medium

## 📲 Attack Steps (Theoretical):

1. **Scan** a valid metro card’s UID (once)
2. **Store** the UID into device memory

**3. Replay** the UID using NFC emulator

4. Metro gate identifies valid UID → Gate opens

No balance check. No backend token verification. Just UID = access.

## 🔓 Other Possibilities: Debug Mode Abuse

Metro gates used by maintenance staff may have:

* **Magnetic override ports**
* **IR triggers**
* **BLE test apps**
* **NFC developer modes**

If such **debug triggers** are not secured or are hardcoded, tools like Flipper Zero can:

* Emulate **NFC debug triggers**
* Send “**Open Gate**” command in maintenance protocol

> *This leads to a gate opening* ***without any valid ticket****, just like what I observed.*

## 📉 Real-World Risks

This isn’t just a “cool trick” — it’s a **critical infrastructure vulnerability**.

## ⚠️ Impact Breakdown:

* 💸 **Revenue Leakage:** Millions per year in unpaid entries
* 👤 **Zero Traceability:** Logs show “valid UID” but no ticket
* 🧑‍💻 **Insider Abuse:** Maintenance staff may leak tools/methods
* 🪧 **No Deterrent:** No alarms, no CCTV alerts, no logs
* 🧍‍♂️ **Mass Exploitability:** Tools easily available online

## 🔐 Solutions for Metro Systems

To avoid such UID-based or debug-based bypasses:

Solution Description ✅ Cryptographic Authentication Use DESFire EV2/EV3 with AES-based challenge 🔄 Dynamic UIDs / Session IDs Tokens should rotate UID or use session key 🧠 Gate-to-Server Sync Don’t make offline UID decisions 📡 Tamper Detection Alert on unknown debug/NFC tools 📊 Behavioral Monitoring Detect UID overuse or time-based patterns

## 📢 Ethical Disclosure Attempt

I tried to report this through:

* Official metro feedback form
* Social media (DM to metro’s account)
* Customer helpline
* But — no concrete response yet.

> *⚠️ I did not clone or replay any UID myself.
>  I only observed behavior, researched tools, and documented the possibilities.*

## 🧠 The Bigger Picture

Most people think metro systems are “unhackable” because they’re physical.
 But this case shows: **if the software trust model is weak, physical access is meaningless.**

> *What’s stopping someone from mass distributing pre-cloned UID tokens?
>  Or making an app that turns a phone into a metro entry bypass tool?*

Nothing — if gate logic is weak.

## 🧢 About the Author

👨‍💻 **Aditya Sunny**
 *Cybersecurity Enthusiast | Honoured by Bajaj Finance Security Heroes | Secured Meta (FB, IG, WA), Dell, Maffashion & more | Ex-Navodayan | Bug Hunter*

**#cybersecurity #rfid #nfc #metrohack #hardwaresecurity #bugbounty #flipperzero #infosec #redteaming**

[Metro](https://medium.com/tag/metro?source=post_page-----f795a29f0280---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----f795a29f0280---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----f795a29f0280---------------------------------------)

[Programming](https://medium.com/tag/programming?source=post_page-----f795a29f0280---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----f795a29f0280---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f795a29f0280---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f...