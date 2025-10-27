---
title: Encryption Backdoor in Military/Police Radios
url: https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html
source: Schneier on Security
date: 2025-08-27
fetch_date: 2025-10-07T00:50:20.932170
---

# Encryption Backdoor in Military/Police Radios

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Encryption Backdoor in Military/Police Radios

I [wrote about](https://www.schneier.com/blog/archives/2023/07/backdoor-in-tetra-police-radios.html%20) this in 2023. Here’s [the story](https://www.wired.com/story/tetra-radio-encryption-backdoor/):

> Three Dutch security analysts discovered the vulnerabilities­—five in total—­in a European radio standard called TETRA (Terrestrial Trunked Radio), which is used in radios made by Motorola, Damm, Hytera, and others. The standard has been used in radios since the ’90s, but the flaws remained unknown because encryption algorithms used in TETRA were kept secret until now.

There’s [new news](https://www.wired.com/story/encryption-made-for-police-and-military-radios-may-be-easily-cracked-researchers-find/):

> In 2023, Carlo Meijer, Wouter Bokslag, and Jos Wetzels of security firm [Midnight Blue](https://www.midnightblue.nl/), based in the Netherlands, discovered vulnerabilities in encryption algorithms that are part of a European radio standard created by ETSI called TETRA (Terrestrial Trunked Radio), which has been baked into radio systems made by Motorola, Damm, Sepura, and others since the ’90s. The flaws remained unknown publicly until their disclosure, because ETSI refused for decades to let anyone examine the proprietary algorithms.
>
> […]
>
> But now the same researchers have found that at least one implementation of the end-to-end encryption solution endorsed by ETSI has a similar issue that makes it equally vulnerable to eavesdropping. The encryption algorithm used for the device they examined starts with a 128-bit key, but this gets compressed to 56 bits before it encrypts traffic, making it easier to crack. It’s not clear who is using this implementation of the end-to-end encryption algorithm, nor if anyone using devices with the end-to-end encryption is aware of the security vulnerability in them.
>
> […]
>
> The end-to-end encryption the researchers examined recently is designed to run on top of TETRA encryption algorithms.
>
> The researchers found the issue with the end-to-end encryption (E2EE) only after extracting and reverse-engineering the E2EE algorithm used in a radio made by Sepura.

These seem to be deliberately implemented backdoors.

Tags: [backdoors](https://www.schneier.com/tag/backdoors/), [encryption](https://www.schneier.com/tag/encryption/), [military](https://www.schneier.com/tag/military/), [police](https://www.schneier.com/tag/police/), [radio](https://www.schneier.com/tag/radio/)

[Posted on August 26, 2025 at 7:06 AM](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html) •
[14 Comments](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html#comments)

### Comments

TimH •
[August 26, 2025 10:46 AM](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html/#comment-447398)

Sadly, the gov reaction is likely to making reverse-engineering proprietary encryption algos illegal, under trade secret or copyright excuse.

Peter A. •
[August 26, 2025 10:51 AM](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html/#comment-447399)

There are several “levels” of standardized encryption algorithms in TETRA, and the higher levels are just not sold to some “inferior” nations or agencies. This is deliberate insecurity engineering.

Joseph Kanowitz •
[August 26, 2025 12:12 PM](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html/#comment-447400)

ב”ה, does the INTC-USG merger create opportunity for an “iPhone Xi” product to Apple Wallet smart passports and associated runtime-modified software?

lurker •
[August 26, 2025 1:11 PM](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html/#comment-447401)

YT vids, Blackhat slides, more to come

<https://www.midnightblue.nl/research/2tetra2burst>

Joseph Kanowitz •
[August 26, 2025 3:00 PM](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html/#comment-447402)

ב”ה, no obvious legal barrier to National Guard handing out DoD cash directly in an evidence-based crime prevention technique. It is a shame persons of Jewish heritage are left out as usual, if true.

This may have bearing on Lisa Cook’s inertia.

Joseph Kanowitz •
[August 26, 2025 3:05 PM](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html/#comment-447403)

ב”ה, from this perspective, DC and Chicago martial law become tax refunds for those too busy or marginalized to have filed or recognized their entire income including immediate contributions on their behalf to tourism.

Joseph Kanowitz •
[August 26, 2025 3:07 PM](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html/#comment-447404)

ב”ה, does DoD have enough forensic accountants on staff for this workload or will it be a real world test of “AI”?

Anonymous •
[August 26, 2025 3:50 PM](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html/#comment-447405)

@lurker

Nice link to more Midnight Blue research.

In their [FAQ](https://www.midnightblue.nl/blog/sepura-device-vulnerabilities) for Sepura device vulnerabilities, they say two CVEs are scheduled to be patched, but an unassigned vuln is “deemed by Sepura to be a design decision and as such, shall not be fixed.”

They say this key exfiltration vuln cannot be patched due to architectural limitations. How do you deal with that?

(These three vulns are specifically related to Sepura’s particular Embedded E2EE solution, right?)

lurker •
[August 26, 2025 5:06 PM](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html/#comment-447408)

@Anonymous, ALL

“deemed by Sepura to be a design decision and as such, shall not be fixed.”

I read this as a proper fix will require a new, better handset, and Sepura have made a management decision to not impose that on their customers. I long ago made a management decision to stay away from people like that.

Note that exploitation requires, even briefly, physical access, so some people may describe that device as lost or stolen and block its access to their network (if possible). But those device owners seem to have a more basic security failure.

Clive Robinson •
[August 26, 2025 7:06 PM](https://www.schneier.com/blog/archives/2025/08/encryption-backdoor-in-military-police-radios.html/#comment-447410)

@ Bruce,

The original driver behind weak crypto in ETSI was the French Government Agencies as I’ve mentioned before.

The idea of “compressing keys” comes from William Friedman and later the NSA in military “field ciphers” and got taken to extraordinary lengths in the design of Clipper / Capstone.

Originally the id...