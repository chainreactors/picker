---
title: MAME Devs Spent 628 Years Cracking Protection on 712 Retro Games
url: https://torrentfreak.com/mame-devs-spent-628-years-cracking-protection-on-712-retro-games-250118/
source: TorrentFreak
date: 2025-01-19
fetch_date: 2025-10-06T20:19:06.565368
---

# MAME Devs Spent 628 Years Cracking Protection on 712 Retro Games

[![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/search.svg)

* News ▼
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/x.svg)

# MAME Devs Spent 628 Years Cracking Protection on 712 Retro Games

January 18, 2025 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [DRM](https://torrentfreak.com/category/anti-piracy/drm/ "Go to the DRM category archives.") >

Those capable of quickly bypassing video game copy protection are revered by impatient pirate players. On average, games protected by anti-tamper tech Denuvo enjoy 68 days crack-free before succumbing to piracy. Yet new research focused on MAME (Multiple Arcade Machine Emulator) and video game preservation, reveals that a sample of 712 protected games, released as far back as 1979, took an average of 10.6 months each to crack. Total cracking time: 628 years.

![mame-retro-s1](https://torrentfreak.com/images/mam-retro-s1.png)
With the next cutting-edge big-budget AAA masterpiece never too far away, thousands of 8bit and 16bit classics dating back almost 50 years sit quietly by, waiting for the arrival of the next wave of curious explorers.

The magic of emulation makes all of this happen and for many retro gaming enthusiasts, the Multiple Arcade Machine Emulator ([MAME](https://www.mamedev.org/release.php)) rules them all. First released on February 7, 1997, development of this [open source](http://mamedev.org/legal.html) giant continues to this day, supporting a wide range of systems popular with millions of gamers of the past, and millions more today in pursuit of nostalgia.

## Emulation, ROMs and Legal Friction

While emulators like MAME are legal, gaming code dumped from arcade machines, 8bit computer disks, or the cartridges of veteran consoles, find friction in the presence of copyright law. Commonly known as ROMs, these relatively tiny files contain the games but unlike other pieces of software in the emulation jigsaw, ROMs are less likely to be distributed openly for legal reasons.

Rest assured, tens of thousands are rarely more than a few clicks away, but how they came to exist at all is a minor miracle. Video game preservation is seen as the only practical way of keeping games alive when companies fold and abandoned hardware begins to decay. Liberating software from ncient hardware is therefore key to preservation, but with anti-piracy systems of yesteryear still intact, circumvention is vital.

A new study published by data scientists Kristofer Erickson and Felix Rodriguez Perez, in collaboration with the CREATe Centre at the University of Glasgow, considers the effect of Technological Protection Measures (TPM) on video game preservation. The researchers focused on MAME, which to date has successfully emulated over 14,377 legacy devices, including 3,783 arcade machines dating back to 1979.

## TPMs Not Omnipresent, But Their Presence is Undeniable

According to [live product data](https://irdeto.com/denuvo/datasheet-anti-tamper) for the modern anti-piracy system Denuvo, on average protected games enjoy 68 crack-free days after their initial release. Even for a state-of-the-art system like Denuvo, an average of a couple of months of circumvention resilience seems to be the limit. Of the sample 3,783 arcade machines considered in the study, 712 machines contained TPMs, all of which required circumvention to enable preservation.

“We measured the time delay introduced by the need to circumvent TPMs to the preservation effort, finding that this added an additional 10.6 months per item to preservation,” the researchers reveal.

“Taking the 712 games from our sample that required circumvention, this represents 628 additional years required to preserve those games protected by TPMs. This represents a social cost in terms of additional labour from community volunteers, as well as missing use from the absence of preserved copies of games available for research, innovation and other productive uses.

“Moreover, as preservation is delayed, technical costs for knowledge institutions may rise. Digital materials that depend on TPM-protected formats and devices can become permanently inaccessible to research and preservation when rightsholders or TPM manufacturers can no longer be located.”

## Move Over Denuvo, It’s Grandpa’s Turn Now

The researchers’ conclusion, that legacy TPMs present “a considerable and statistically significant impediment” to preservation, suggests the presence of sophisticated TPMs that have stood the test of time. The key challenges to circumvention were as follows:

• Encryption of game data: In the supported device list for MAME 0.258 and the sample of all arcade games released between 1979 and 2023, at least 1,072 games (29%) had some kind of protection against copying. The researchers report that encryption of game data was most common, present on 370 devices (10%) of the arcade sample.

• Memory Controller Units: A similar number of game boards featured Memory Controller Units (MCUs). These devices manage the flow of data to and from a game’s main memory and with memory scrambling available, access to game data was further complicated.

## Self-Destruction

• Suicide Chips: “The Hitachi FD1089 / FD1094 found on Sega System 16 boards used an encryption key to verify the contents of a game before running the code. The chip required battery power to operate correctly, so when batteries died the chip would no longer function, resulting in a fault,” the researchers explain.

“Because such systems rely on inaccessible sources of power inside TPM modules in order to function, they have been dubbed ‘suicide boards’ by the preservation community. In 2018, researcher Eduardo Cruz published a method for backing up and restoring (‘de-suiciding’) Hitachi FD1094 modules. He indicates that circumvention required work by several individuals over a span of years.”

• Slapstick Protection: Present on many 16-bit Atari games including Marble Madness (1984), Gauntlet (1985), and Paperboy (1985), the ‘Slapstic’ protection chip was reportedly one of the earliest TPM challenges faced by game preservationists.

The researchers cite MAME developer Aaron Giles, who explained that the chip was unique to Atari games. Its purpose was to prevent machine operators from burning new EPROMs and “upgrading” their PCBs (circuit boards) to a new game without having to buy official upgrade kits from Atari. That’s an all-too-familiar story even today, one that has an equally familiar outcome.

“In 1998, Giles successfully reverse engineered functionality of the Slapstic security, enabling full emulation of the 8- and 16-bit Atari arcade games that used the protection,” the researchers note.

## Conclusion

In the context of game preservation, the researchers conclude that TPMs inhibit several positive effects, including the denial of benefits to society when games enter the public domain. The researchers conclude their study (available [here](https://eprints.gla.ac.uk/343838/)) with recommendations to guide future law and policy.

The future costs of TPMs on society should be carefully considered, weighing the benefits of statutory exceptions for circumvention, to facilitate preservation, research, and interoperabili...