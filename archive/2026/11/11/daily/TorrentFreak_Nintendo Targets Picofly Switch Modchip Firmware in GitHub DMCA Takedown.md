---
title: Nintendo Targets Picofly Switch Modchip Firmware in GitHub DMCA Takedown
url: https://torrentfreak.com/nintendo-targets-picofly-switch-modchip-firmware-in-github-dmca-takedown/
source: TorrentFreak
date: 2026-11-11
fetch_date: 2026-11-12T09:02:56.854591
---

# Nintendo Targets Picofly Switch Modchip Firmware in GitHub DMCA Takedown

[![](https://torrentfreak.com/wp-content/themes/torrentfreak/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/torrentfreak/build/assets/img/search.svg)

* News
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/torrentfreak/build/assets/img/x.svg)

# Nintendo Targets Picofly Switch Modchip Firmware in GitHub DMCA Takedown

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [DMCA](https://torrentfreak.com/category/anti-piracy/dmca/ "Go to the DMCA category archives.") >

After taking down Switch emulators and hacking tools on GitHub for years, Nintendo is now going after modchip firmware. The gaming company sent a DMCA notice targeting firmware for modchips such as Picofly, SX Core and HWFLY, after which GitHub disabled 144 repositories. To back its claim, Nintendo cites the criminal case against alleged Team-Xecuter members, which led to a guilty plea from one of its three defendants.

![picofly](https://torrentfreak.com/images/picofly-600x448.png)In 2020, Nintendo [went to court](https://torrentfreak.com/nintendo-sues-stores-selling-new-team-xecuter-switch-piracy-hack-200518/) to stop the sale of SX Core and SX Lite, two Team-Xecuter modchips designed to work on all Switch consoles at the time.

These lawsuits were followed by a [criminal prosecution](https://torrentfreak.com/us-indicts-several-members-of-piracy-group-team-xecuter-two-arrested-201002/) in the United States, and Team-Xecuter’s operation [effectively shut down](https://torrentfreak.com/nintendo-hacker-gary-bowser-released-from-federal-prison-230417/). The chips lived on, however, and remained available through compatible alternatives such as HWFLY and Picofly.

Now, Nintendo is also going after the repositories that host the firmware for these modchips.

In a takedown notice dated November 6, which [GitHub](https://github.com) published on Tuesday, Nintendo of America targets Ansem-SoD/Picofly. According to its description, this repository offered information and firmware for a Switch modchip based on the RP2040-Zero board.

*Picofly*
![picofly notice](https://torrentfreak.com/images/picodown.png)

The [notice](https://github.com/github/dmca/blob/master/2026/11/2026-11-06-nintendo-2.md) names only the parent repository, but its effect doesn’t stop there. Because the network was larger than a hundred repos and Nintendo said that all or most forks are infringing, GitHub disabled the entire network of 144 repositories.

## From Emulators to Modchips

Nintendo’s earlier GitHub notices mostly went after emulators, key dumping tools and so-called [sigpatches](https://torrentfreak.com/why-nintendo-uses-the-dmca-to-take-down-piracy-enabling-sigpatches-220802/). This time, the gaming giant targets repositories offering firmware for SX Core, SX Lite, Picofly and HWFLY modchips.

According to Nintendo, the Switch’s technological protection measures (TPMs) include the console’s boot sequence and various cryptographic signatures. The company says the modchip firmware bypasses that boot sequence, violating the DMCA’s anti-circumvention provisions.

“The firmware allows Nintendo Switch modchips to illegally circumvent Nintendo’s TPMs in order to run illegal copies of Nintendo Switch games,” the notice reads.

*From Nintendo’s notice*
![From Nintendo's notice](https://torrentfreak.com/images/nintendo-pico.png)

As far as we know, this is the first time Nintendo has targeted modchip firmware on GitHub. None of the 90 earlier Nintendo notices in GitHub’s public archive mention modchips. The closest are the 2023 and 2024 notices against key dumping tools such as [Lockpick\_RCM](https://torrentfreak.com/poking-nintendo-why-lockpick-dmca-blitz-should-surprise-no-one-230508/).

## A Team-Xecuter Precedent

To support its circumvention claim, the notice points to the criminal case No. 2:20-cr-00127-RSL. That’s the case against the alleged members of Team-Xecuter.

The U.S. indicted three people in 2020. One of them, [Gary Bowser](https://torrentfreak.com/gary-bowser-how-a-1980s-hacker-became-nintendos-nemesis-decades-later-230702/), [pleaded guilty](https://torrentfreak.com/team-xecuters-gary-bowser-pleads-guilty-to-criminal-charges-211101/) to conspiring to circumvent technological measures and to traffic in circumvention devices. He was later [sentenced to 40 months](https://torrentfreak.com/nintendo-hacker-gary-bowser-40-months-prison-sentence-220210/) in prison.

The other two defendants, including [alleged leader](https://torrentfreak.com/nintendo-nemesis-max-louarn-hacker-rebel-and-wanted-by-the-fbi-220611/) Max Louarn, have not appeared before the U.S. court as far as we know, and both remain at large.

It’s worth noting that Bowser’s guilty plea is not a court ruling on modchip firmware. However, at the takedown stage, Nintendo doesn’t need one, and GitHub appears to have processed the notice regardless.

## Firmware Still Online

When we checked on Wednesday, the [Picofly repository](https://github.com/Ansem-SoD/Picofly) was replaced by GitHub’s standard takedown message, which also explains that the owner can file a counter notice.

*Repository unavailable*

![](https://torrentfreak.com/images/picogit.png)

However, not all modchip firmware is gone. Several other GitHub repositories with Picofly and HWFLY firmware were still online, including what a GBAtemp forum user describes as the original Picofly source. None of these are named in Nintendo’s notice.

Nintendo also sent three emulator notices on the same day. One targets the Citron Neo emulator, where GitHub disabled a network of 71 repositories, and two target single copies of yuzu.

*Nintendo’s November 6 notices (published later)*

| Repository | Project | Repos | Status |
| --- | --- | --- | --- |
| Ansem-SoD/Picofly | Picofly firmware | 144 | Disabled |
| citron-neo/emulator | Citron Neo | 71 | Forks disabled |
| IpwnedU/yuzu-mainline-master | yuzu | 1 | Code removed |
| IpwnedU/yuzu-android-master | yuzu | 1 | Code removed |

These yuzu repositories are still on GitHub, but their owner has since removed the code and cleared the commit history. Both now only host [a README](https://github.com/IpwnedU/yuzu-android-master) which says that the source code can be found on the Internet Archive.

For now, the Picofly network remains offline. Its owner can still file a counter notice, but GitHub’s archive shows no sign of one yet.

*—*

Nintendo’s DMCA notice targeting the Picofly repository is available at GitHub [here](https://github.com/github/dmca/blob/master/2026/11/2026-11-06-nintendo-2.md). The Citron Neo notice can be found [here](https://github.com/github/dmca/blob/master/2026/11/2026-11-06-nintendo-4.md), and the two yuzu notices [here](https://github.com/github/dmca/blob/master/2026/11/2026-11-06-nintendo-3.md) and [here](https://github.com/github/dmca/blob/master/2026/11/2026-11-06-nintendo.md).

* [Previous Post![](https://torrentfreak.com/wp-content/themes/torrentfreak/build/assets/img/arrow-right.svg)](https://torrentfreak.com/pirate-library-welib-hit-with-19-5m-judgment-and-domain-takedown-order/)

### Tagged In:

* [DMCA](https://torrentfreak.com/tag/dmca/)
* [Github](https://torrentfreak.com/tag/github/)
* [modchip](https://torrentfreak.com/tag/modchip/)
* [Nintendo](https://torrentfreak.com/tag/nintendo/)
* [picofly](https://torrentfreak...