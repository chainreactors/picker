---
title: Take-Two Targets Hundreds of GTA V Mobile Ports on GitHub Ahead of GTA VI Launch
url: https://torrentfreak.com/take-two-targets-hundreds-of-gta-v-mobile-ports-on-github-ahead-of-gta-vi-launch/
source: TorrentFreak
date: 2026-11-19
fetch_date: 2026-11-20T09:23:11.030434
---

# Take-Two Targets Hundreds of GTA V Mobile Ports on GitHub Ahead of GTA VI Launch

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

# Take-Two Targets Hundreds of GTA V Mobile Ports on GitHub Ahead of GTA VI Launch

yesterday by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Piracy](https://torrentfreak.com/category/piracy/ "Go to the Piracy category archives.") >

Just hours ahead of the Grand Theft Auto VI launch, GitHub published four takedown notices from Take-Two, targeting unofficial GTA V ports for iPhone, Mac and Android. The notices also cover hundreds of forks, and the main repositories are now offline. Notably, only one of the four notices says that a repository actually hosted an infringing copy of the game.

![GTA 5 logo](https://torrentfreak.com/images/gta5-1-600x547.png)After a series of delays, [Grand Theft Auto VI](https://www.rockstargames.com/newswire/article/ak3ak31a49a221/grand-theft-auto-vi-is-now-set-to-launch-november-19-2026) finally goes on sale today, more than thirteen years after its predecessor came out.

While fans count down the final hours, [Take-Two Interactive](https://en.wikipedia.org/wiki/Take-Two_Interactive) is still busy with GTA V.

Yesterday, GitHub published four takedown notices from the company, targeting unofficial ports of the 2013 game that allow it to run on iPhones, Macs, Android phones and Windows PCs.

These ports trace back to early October, when GTA V suddenly became playable in a regular web browser. An unofficial port of the game at playgta5.com went viral on social media. That didn’t last, as the website disappeared within hours.

At the time, [press reports](https://beebom.com/rockstar-shuts-down-free-gta-5-browser-port/) credited Rockstar and Take-Two with the removal, but [neither company commented](https://godisageek.com/2026/10/gta-v-browser-port-pulled/) on it. [Reports](https://games.gg/news/rockstar-shuts-down-gta5-browser-port/) that the port was built with help from leaked GTA V source code have not been confirmed either.

While the port was shot down in hours, the genie was out of the bottle and the WebAssembly build of the game lived on. Within days, developers turned this into native apps for Apple devices and Android phones, which were widely shared on GitHub.

## Four Notices, Hundreds of Forks

The notices, sent by Rockstar’s parent company Take-Two, target four projects. These are the iOS and macOS port Muguet, the multi-platform runtime glue5, the Android port gta5mobile-android, and three repositories from the developer behind PlayGTA5.

*According to Take-Two’s DMCA notices*

| Project (links to notice) | Platforms | Forks (per Take-Two) | Alleged infringement |
| --- | --- | --- | --- |
| [Muguet](https://github.com/github/dmca/blob/master/2026/11/2026-11-18-take-two.md) | iOS, macOS | 263 | Infringes and facilitates infringement; “bring your own files” disclaimer |
| [glue5](https://github.com/github/dmca/blob/master/2026/11/2026-11-18-take-two-4.md) | iOS, macOS, Android, Windows | 349 | Build workflow on GitHub; streaming of roughly 20 GB of game files |
| [gta5mobile-android](https://github.com/github/dmca/blob/master/2026/11/2026-11-18-take-two-2.md) | Android | 14 or 16 (18 repositories listed) | APK downloads and tools to load and run the game |
| [PlayGTA5, gtav-mobile, playgta5-enhanced](https://github.com/github/dmca/blob/master/2026/11/2026-11-18-take-two-3.md) | Browser, Android, iOS | Not stated | Full game (21.2 GB) offered in a GitHub release |

In the Muguet notice, Take-Two quotes the project’s own instructions, which tell users to supply their own game files.

“Because I care about me not getting sued, you will need your own copy,” the developer wrote, according to the notice. Take-Two reads this as a confirmation that the developer is aware of potential copyright concerns. “That statement expresses awareness of Take-Two’s rights and what they are facilitating,” the notice adds.

The PlayGTA5 notice goes further. According to Take-Two, a release published in the PlayGTA5 repository on October 9 offered the full game, which totals 21.2 GB.

Before the takedown, the repository’s README file also mentioned that the game data was included in its GitHub release downloads, explaining that some files were too large for regular commits. The developer archived the repository on October 15.

In addition to the main repositories, Take-Two also asks GitHub to disable all their forks, including 263 Muguet forks and 349 glue5 forks by its own count. GitHub’s published notices don’t say how many repositories it processed, but it’s likely several hundred.

When we checked this morning, the Muguet, glue5 and PlayGTA5 repositories, as well as the copies and forks we’ve seen, all showed a DMCA takedown “unavailable” message. The first gta5mobile-android repository listed in the notice now returns a ‘page not found’ error, which typically means that the developer took it offline of made it private.

*Unavailable*

![unavailable](https://torrentfreak.com/images/muguet.png)

“This repository is currently disabled due to a DMCA takedown notice,” the messages [read](https://github.com/c22dev/muguet), adding that developers “have the right to file a counter notice and have the repository reinstated.”

## ‘Bring Your Own’ Disclaimers

The Muguet, glue5 and gta5mobile-android projects all relied on users supplying the game files themselves. The ‘own copy’ in question is the data of the unofficial web port, not a regular PC or console installation.

The PlayGTA5 case aside, the notices don’t claim that the targeted repositories host Take-Two’s code or game files. Instead, they say that the projects infringe, and that they facilitate copyright infringement.

*GitHub Takedown*
![takedown](https://torrentfreak.com/images/mudtakedown.png)

Take-Two’s notice against glue5 is more detailed. It describes a GitHub build process that turns the web build users provide into apps, and a streaming option that can transfer roughly 20 GB of game files, including a “Download the whole game” feature.

According to Take-Two, the disclaimers aren’t enough. All four notices make this point, and two of them use the same words: “bring your own” disclaimers “do not automatically shield developers from secondary copyright liability where their conduct knowingly facilitates infringement.”

*Bring your own files*
![bring your own](https://torrentfreak.com/images/bto.png)

## One Port Survives

Not all GTA V ports were targeted. The 5★ Port, which runs the same web build on iPhones and Macs, went offline in late October, according to [PortedGames](https://portedgames.com/gta-5-iphone/). It returned in early November and was still online this morning. However, the project no longer offers a way to build the app through GitHub’s workflow system.

The project’s README even invites rights holders to get in touch by email, promising that the repository will be removed promptly.

*Not Affiliated*

![rightsholders](https://torrentfreak.com/images/rightsholderg.png)

For the targeted developers, not everything is lost. They can file a DMCA counter-notice, after which GitHub has to restore the code, unless Take-Two takes the matter to court.

That has worked before. When the developers of the GTA multiplayer mod Multi Theft...