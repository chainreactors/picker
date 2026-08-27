---
title: Your SIM card can give orders to your phone, and you can’t turn it off
url: https://andreafortuna.org/2026/08/26/hostile-sim-at-commands-catana/
source: Instapaper: Unread
date: 2026-08-26
fetch_date: 2026-08-27T12:14:40.730403
---

# Your SIM card can give orders to your phone, and you can’t turn it off

[Andrea Fortuna](/)
[ ]

[About](/about/)[Search](/search/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# Your SIM card can give orders to your phone, and you can't turn it off

Aug 26, 2026

by [Andrea Fortuna](/about/)

If you have spent any time worrying about phone security, you have almost certainly worried about the wrong layer. Malicious apps, phishing links, dodgy Wi-Fi hotspots: all reasonable concerns, all addressed by settings you can actually change. Nobody ever told you to worry about the little gold-contact card sitting under your battery tray, because nobody imagined it needed worrying about. A [paper presented on August 11, 2026 at USENIX WOOT](https://www.usenix.org/conference/woot26/presentation/lisowski), one of the most respected offensive security venues in the world, makes the case that this was an oversight, not an omission.

![cover](/assets/2026/catana-sim-at-commands.jpg)

## In brief

* Researchers from the University of Birmingham built a toolkit called **CATana** to test how far a SIM card can push commands onto the device it sits in.
* The mechanism is **Proactive SIM**, a legitimate feature of the cellular spec (3GPP TS 31.111, ETSI TS 102 223) that lets a SIM issue a **RUN AT** command, executed directly by the modem using the decades-old AT command language.
* Out of 26 tested devices (18 smartphones, 8 cellular IoT modules), the team found 4 exploitable vulnerabilities, including forced 4G-to-2G downgrades, silent lock-screen browser launches, file exfiltration, and code execution on a modem’s application processor.
* Google fixed the Android lock-screen browser bypass as **CVE-2025-48618** in the December 2025 security bulletin; Qualcomm has shipped a configuration that disables the vector by default.
* The researchers argue that patching individual bugs is not enough. They want RUN AT deprecated and stripped out of firmware entirely.

## A command channel nobody expected to defend

The interface at the center of this research is called the **AT interface**, named after the AT (ATtention) command set that Dennis Hayes and Dale Heatherington designed in 1981 to control the Hayes Smartmodem. It became the universal control language for modems, and it never really left: your phone’s baseband processor still speaks it internally, decades after anyone last heard a modem’s dial tone.

Normally the flow runs one way. The phone queries the SIM to authenticate you on the network, fetch your contacts, or read carrier settings. **Proactive SIM** commands invert that relationship: they let the card initiate a request toward the device instead of just answering one. This is a documented part of the standard, specifically Section 6.4.23 of 3GPP TS 31.111, which defines the **RUN AT COMMAND** that lets a SIM ask the terminal to execute an arbitrary AT command. As Dr. Marius Muench, one of the paper’s authors, put it in the [University of Birmingham’s writeup](https://www.birmingham.ac.uk/news/2026/who-tests-the-chip-in-your-phone):

> “What people don’t realise is that SIM cards are tiny computers. They don’t just store secrets to access the network; they can directly interact with the phone. And there is a full specification defining what a SIM is allowed to request from the phone.”

Most phones filter this channel or ignore it outright. The point of CATana, the toolkit built by Tomasz Piotr Lisowski, Muench, and Kristian Covic of Fuzzware, was to stop assuming that filtering works and start measuring it. According to the [project’s Zenodo archive](https://zenodo.org/records/21863906), the suite includes CATtty, for driving AT commands into a target through a SIMtrace-connected software SIM, CATlet, for running the same experiments through an applet on a real programmable SIM, and CATauto and CATview for scaling and analyzing the results. It is, in effect, adversarial fuzzing applied to a component the industry has spent forty years treating as inherently trustworthy.

This is not the team’s first pass at SIM security either. The same Birmingham group previously built [SIMurai](https://www.usenix.org/system/files/usenixsecurity24-lisowski.pdf), a software SIM emulator for adversarial testing, and readers of this blog will recognize the general shape of the problem from the [WIBattack disclosure](https://andreafortuna.org/2019/09/28/wibattack-not-only-s-t-browser-but-also-wib-sim-toolkit-is-vulnerable-to-simjacker-attacks/) covered here back in 2019, when the SIMJacker family of attacks first showed that SIM toolkits could be weaponized over SMS. CATana targets a different direction of the same trust relationship: not “can I attack the SIM,” but “what can the SIM do to me.”

## OPPO’s stuck 2G radio and Android’s lock-screen browser

Two results from the paper illustrate why this matters in practice rather than just in theory. On the OPPO Reno 14 F 5G, which according to [Help Net Security’s coverage](https://www.helpnetsecurity.com/2026/08/11/malicious-sim-cards-hijack-phones-ev-chargers/) accepted 198 distinct AT commands and variants through the SIM interface, a proactive command can force the phone’s connection down to 2G, the standard that shipped in the 1990s and never got proper mutual network authentication. That gap is exactly what makes 2G a favorite for rogue base station attacks, the same weakness this blog covered when looking at [how smartphones react to IMSI catching](https://andreafortuna.org/2021/05/01/how-smartphones-reacts-to-imsi-catching-attacks/). What makes the OPPO case worse is persistence: the downgrade survived airplane mode, disabling the SIM, and manually changing network settings. There is, at the time of writing, no user-facing toggle that undoes it.

On Android more broadly, a proactive command called **LAUNCH BROWSER** let a hostile SIM open an attacker-chosen URL even on a locked screen, with zero user interaction. Google tracked this as **CVE-2025-48618**, an elevation-of-privilege flaw in `processLaunchBrowser` inside `CommandParamsFactory.java`, and fixed it in the [December 2025 Android security bulletin](https://source.android.com/docs/security/bulletin/2025-12-01), covering Android 13 through 16. The CVSS score sits at a modest 6.8, largely because the attack requires physical access to swap or control the SIM, but modest CVSS scores have a way of undercounting real-world impact when the access requirement is “steal the phone,” which is precisely the scenario a locked screen is supposed to defend against in the first place.

## Beyond phones: EV chargers and the Quectel problem

The most interesting result may not be about phones at all. The team achieved code execution on an **AUTEL EV charger** built around a Quectel EC25-AFX cellular module, chaining a SIM-issued command injection flaw in the modem’s Linux-based application processor into full control of the module. Quectel modems are not exotic; they turn up in industrial routers, telematics units, and automotive control systems well beyond EV chargers, which is why the disclosure list for this research includes Google, OPPO, Quectel, Qualcomm, and Semtech. Qualcomm has already published a configuration that disables the vulnerable channel by default, a mitigation that will quietly protect a much larger population of devices than the headline phone examples suggest.

The reasoning behind why IoT devices are especially exposed is almost mundane: an EV charger or industrial router typically has no USB port, no exposed debug header, nothing an attacker can plug into from outside. It does, however, always have a SIM slot, because cellular connectivity is the whole point. On a device engineered to minimize its attack surface, the SIM interface becomes the one gap nobody closed, precisely because it was assumed to be the trusted anchor rather than a possible entry point.

## Four ways a SIM turns hostile

None of this works unless someone controls the SIM in the fir...