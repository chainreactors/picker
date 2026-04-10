---
title: Fake Battlefield 6 Pirated Versions and Game Trainers Used to Deploy Stealers and C2 Agents
url: https://www.bitdefender.com/en-us/blog/labs/fake-battlefield-6-pirated-games-trainers
source: Over Security - Cybersecurity news aggregator
date: 2026-04-09
fetch_date: 2026-04-10T04:46:54.098950
---

# Fake Battlefield 6 Pirated Versions and Game Trainers Used to Deploy Stealers and C2 Agents

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

6 min read

# Fake Battlefield 6 Pirated Versions and Game Trainers Used to Deploy Stealers and C2 Agents

[![Raul Vasile BUCUR](https://blogapp.bitdefender.com/labs/content/images/size/w100/2025/11/rbucur.jpg "Raul Vasile BUCUR")](/en-us/blog/labs/author/raul-bucur "Raul Vasile BUCUR")[![Silviu STAHIE](https://0.gravatar.com/avatar/c341806f635818bcc6faa8f684e3d9d0?s=64&d=mm&r=g "Silviu STAHIE")](/en-us/blog/labs/author/sstahie "Silviu STAHIE")

[Raul Vasile BUCUR](/en-us/blog/labs/author/raul-bucur "Raul Vasile BUCUR")[Silviu STAHIE](/en-us/blog/labs/author/sstahie "Silviu STAHIE")

November 25, 2025

  ![Fake Battlefield 6 Pirated Versions and Game Trainers Used to Deploy Stealers and C2 Agents](https://blogapp.bitdefender.com/labs/content/images/size/w600/2025/11/0d0c073a-b001-4f77-818b-21eec97e3cbd.png "Fake Battlefield 6 Pirated Versions and Game Trainers Used to Deploy Stealers and C2 Agents")

*Bitdefender Labs has identified malware campaigns exploiting the popularity of EA's Battlefield 6 first-person shooter, distributed via supposedly pirated versions, game installers, and fake game trainers across torrent websites and other easily found domains.*

Electronic Arts' Battlefield 6, developed by DICE and published by Electronic Arts (EA), was released in October, and it's likely one of the most significant game launches of the year.

Cybercriminals take advantage of major events, such as the release of critically acclaimed games, to push their malware.

As soon as the game became available for purchase and download, criminals began spreading fake cracked versions of Battlefield 6 on torrent sites and underground forums. These supposedly cracked games are actually infected installers and apps delivering stealers, advanced evasion payloads and even command-and-control (C2) agents.

As a side note, there are many real groups that routinely crack newly released titles and their names are well known within the online community. **InsaneRamZes** and **RUNE** are just two of the more popular ones right now, which is likely why cybercriminals chose to use their names in the fake releases. It's a similar tactic used in attacks that try to mimic legit brands.

However, users who search for pirated versions of Battlefield are not the only targets. Battlefield 6 players might look for something to give them an advantage, and attackers know this all too well. So cybercriminals built game "trainers" that promise to do just that, only they are designed to steal information.

Our analysis of three such samples has revealed attacks weaponizing the game's popularity to compromise PCs and extract sensitive data.

## Key findings

* Multiple Battlefield 6 "cracks" and "trainers" circulate online, but none are functional.
* The fake trainer is an aggressive infostealer, targeting browsers and crypto-wallets.
* The InsaneRamZes pirated version shows advanced anti-analysis and regional evasion techniques.
* The RUNE pirated version deploys a C2 agent capable of persistence and remote control.
* The malware samples have no real Battlefield-related functionality, and they are very likely from different groups

## Pirated game versions and game trainers explained

**Pirated versions** of games have been around for years. Depending on the type of game and the protection used by the publishers, it's not uncommon to see a pirated version of a title pop up online on the same day as the official release.

Games that integrate advanced protection and have a very heavy multiplayer component, such as **Battlefield 6**, take a longer time to pirate. But not everyone knows this and there will always be potential victims who believe they are actually downloading the pirated version of **Battlefield 6**.

You might also notice that the pirated games investigated here are also accompanied by two additional names, **InsaneRamZes** and **Rune**. If you're not pirating games, they might sound strange. But these are real groups that crack new games releases. In this case, the attackers only use their names to lend credibility, in an effort to convince people that they are getting the real deal.

Making matters worse, the real RUNE group released a cracked version of Battlefield 6, which will only help spread malware. It’s very likely that users will access known torrent trackers and download the malware-ridden version by mistake.

As for game trainers, these are applications – often legitimate – that allow players to make changes to games, such as giving themselves more gold coins, other in-game resources, or even gaining immortality in first-person shooters.

These trainers are usually designed for single-player titles and don't work in multiplayer. Sometimes, the players get banned for using such software in multiplayer.

It's worth noting that some security solutions might detect game trainers as potentially dangerous due to how they work. In some situations, certain types of malware exhibit the same behavior as a legitimate trainer.

## Fake Battlefield 6 trainer (Infostealer)

The first sample poses as a "Battlefield 6 Trainer Installer." Users can easily find the malware by searching for "Battlefield 6 trainers" on Google. Despite its small size and lack of obfuscation, it quickly steals data once executed.

The website (https[:]//flingtrainer[.]io/) is full of "trainers" that only push similar stealers. The name FLiNG is also stolen from a real game trainer developer known for his legitimate apps.

**Behavior overview**

The executable goes through local user directories and Internet browser profiles, retrieving data such as:

* **Crypto Wallets** and **Cookie Sessions** from Chrome, Edge, Firefox, Opera, Brave, Vivaldi, and WaveBrowser.
* Session tokens and credentials from **Discord**.
* Crypto-wallet extension data from Chrome add-ons like **iWallet** and **Yoroi**.

The stolen information is exfiltrated to **198[.]251[.]84[.]9** over plaintext HTTP, with no attempt to hide the traffic.

![](https://blogapp.bitdefender.com/labs/content/images/2025/11/Picture2.png)

The malware's simplicity makes it highly effective, even if it lacks anti-analysis measures and even runs inside virtual machines.

## ‘Battlefield 6.GOG-InsaneRamZes’ (evasive malware)

The second sample, distributed as **Battlefield 6.GOG-InsaneRamZes** via torrent websites uses an entirely different strategy that includes stealth and environmental awareness.

**Regional execution blocking**

Before deploying its payload, the malware builds an array of locale identifiers and stops execution if it detects Russian or CIS regional settings.

![](https://blogapp.bitdefender.com/labs/content/images/2025/11/Picture3.png)

Disassembly showing locale comparison with codes such as RU, AM, AZ, BY, KZ, KG, LT, and UZ, leading to immediate termination on matching systems.

This is a **self-protection measure** often used by Russian malware groups to avoid legal exposure in certain jurisdictions.

**Windows API hashing**

To obscure the way it works, the malware hides API calls behind **hashed strings**. When it runs, it tries to determine the hash of each target API (from system DLLs). When the hash matches, it will save it for later use.

![](https://blogapp.bitdefender.com/labs/content/images/2025/11/Picture1.png)

Decompiled code demonstrating API hashing to obscure calls to GetSystemDefaultLCID, GetLocaleInfoW, and GetUserGeoID.

**Anti-sandbox timing check**

The malware also performs a **GetTickCount()** test, a technique used to detect whether it’s runnin...