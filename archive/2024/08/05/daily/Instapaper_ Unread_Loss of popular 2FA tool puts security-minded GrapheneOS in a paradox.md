---
title: Loss of popular 2FA tool puts security-minded GrapheneOS in a paradox
url: https://arstechnica.com/gadgets/2024/07/loss-of-popular-2fa-tool-puts-security-minded-grapheneos-in-a-paradox/
source: Instapaper: Unread
date: 2024-08-05
fetch_date: 2025-10-06T18:04:39.013815
---

# Loss of popular 2FA tool puts security-minded GrapheneOS in a paradox

[Skip to content](#main)
[Ars Technica home](https://arstechnica.com/)

Sections

[Forum](/civis/)[Subscribe](/subscribe/)[Search](/search/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

* [Feature](/features/)
* [Reviews](/reviews/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

[Forum](/civis/)[Subscribe](/subscribe/)

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Pin to story

Theme

* HyperLight
* Day & Night
* Dark
* System

Search dialog...

Sign In

Sign in dialog...

Sign in

Just a bit too custom for their taste

# Loss of popular 2FA tool puts security-minded GrapheneOS in a paradox

Losing access to Authy leads to another reckoning with Google's security model.

[Kevin Purdy](https://arstechnica.com/author/kevinpurdy/)
–

Jul 30, 2024 12:36 pm
| [140](https://arstechnica.com/gadgets/2024/07/loss-of-popular-2fa-tool-puts-security-minded-grapheneos-in-a-paradox/#comments "140 comments")

[![Scientist looking at a molecular model of graphene in a laboratory](https://cdn.arstechnica.net/wp-content/uploads/2024/07/graphene.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2024/07/graphene.jpg)

Graphene is a remarkable allotrope, deserving of further study. GrapheneOS is a remarkable ROM, one that Google does not quite know how to accommodate, due to its "tiny, tiny" user numbers compared to mainstream Android.

Graphene is a remarkable allotrope, deserving of further study. GrapheneOS is a remarkable ROM, one that Google does not quite know how to accommodate, due to its "tiny, tiny" user numbers compared to mainstream Android.

Text
settings

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Minimize to nav

"If it's not an official OS, we have to assume it's bad."

That's how Shawn Wilden, the tech lead for hardware-backed security in Android, [described](https://x.com/shawnwillden/status/1817928318039237001) the current reality of custom Android-based operating systems in response to a real security conundrum. [GrapheneOS](https://grapheneos.org/) users [discovered recently](https://discuss.grapheneos.org/d/14374-authy-device-does-not-meet-integrity-requirement) that [Authy](https://authy.com/), a popular (and [generally well-regarded](https://arstechnica.com/information-technology/2020/05/choosing-2fa-authenticator-apps-can-be-hard-ars-did-it-so-you-dont-have-to/)) two-factor authentication manager, will not work on their phones—phones running an OS intended to be more secure and hardened than any standard Android phone.

"We don't want to punish users of alternative OSes, but there's really no other option at the moment," Wilden added before his blunt conclusion. "Play Integrity has absolutely no way to guess whether a given custom OS completely subverts the Android security model."

[Play Integrity](https://developer.android.com/google/play/integrity), formerly [SafetyNet Attestation](https://developer.android.com/privacy-and-security/safetynet/deprecation-timeline), essentially allows apps to verify whether an Android device has provided permissions beyond Google's intended models or has been rooted. Root access is not appealing to the makers of some apps involving banking, payments, competitive games, and copyrighted media.]

There are many reasons beyond cheating and skulduggery that someone might root or modify their Android device. But to prove itself secure, an Android device must contact Google's servers through an API in Google Play Services and then have its bootloader, ROM signature, and kernel verified. GrapheneOS, like most custom Android ROMs, does not contain a Google Play Services package by default but will let users install a sandboxed version of Play Services if they wish.

Wilden offered some hope for a future in which ROMs could vouch for their non-criminal nature to Google, [noting](https://x.com/shawnwillden/status/1817928681618305278) "some discussions with makers of high-quality ROMs" about passing the [Compatibility Test Suite](https://source.android.com/docs/compatibility/cts), then "establishing some kind of relationship we can use to trust them." But it's "a lot of work on both sides, including by lawyers," Wilden notes. And while his team is happy to help, higher-level support is tough because "modders are such a tiny, tiny fraction of the user base."

The official GrapheneOS X account was [less hopeful](https://x.com/GrapheneOS/status/1817977093264937225). It noted that another custom ROM, LineageOS, disabled verified boot at installation, and "rolls back security in a lot of other ways," contributing to "a misconception that every alternate OS rolls back security and isn't production quality." A typical LineageOS installation, like most custom ROMs, does disable verified boot, though it can be re-enabled, except [it's risky and complicated](https://www.reddit.com/r/LineageOS/comments/1e8m2a2/comment/ledtg3a/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button). GrapheneOS has [a page on its site](https://grapheneos.org/articles/attestation-compatibility-guide) regarding its stance on, and criticisms of, Google's attestation model for Android.

Later on Tuesday, GrapheneOS responded to this Ars post with [a thread on X](https://x.com/GrapheneOS/status/1818414579153596422) (and [Mastodon](https://grapheneos.social/%40GrapheneOS/112878067304840664)) about Google's actions in banning GrapheneOS from the Play Integrity API. In particular, GrapheneOS states that it has "irrefutable proof that the majority of certified Android devices" do not comply with Google's Compatibility Test Suite or Compatibility Definition Document, such that "Play Integrity API is based on lies." Should Google not permit GrapheneOS into its Play Integrity API, GrapheneOS claims it will "be taking legal action against them and their partners."

"We've started the process of talking to regulators and they're interested," the project's official account [writes](https://x.com/GrapheneOS/status/1818415391791570995).

Ars has reached out to Google and Authy (via owner Twilio) for comment. At the moment, it doesn't seem like there's a clear path forward for any party unless one of them is willing to majorly rework what they consider proper security.

*This post was updated at 7:30 pm Eastern on July 30 with response from GrapheneOS. It was later updated to fix an incorrect link pointer.*

[![Photo of Kevin Purdy](https://cdn.arstechnica.net/wp-content/uploads/2022/08/kevin_headshot.jpg)](https://arstechnica.com/author/kevinpurdy/)

[Kevin Purdy](https://arstechnica.com/author/kevinpurdy/)
Senior Technology Reporter

[Kevin Purdy](https://arstechnica.com/author/kevinpurdy/)
Senior Technology Reporter

Kevin is a senior technology reporter at Ars Technica, covering open-source software, PC gaming, home automation, repairability, e-bikes, and tech history. He has previously worked at Lifehacker, Wirecutter...