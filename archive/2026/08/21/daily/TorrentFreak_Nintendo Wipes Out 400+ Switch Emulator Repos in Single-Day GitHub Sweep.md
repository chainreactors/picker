---
title: Nintendo Wipes Out 400+ Switch Emulator Repos in Single-Day GitHub Sweep
url: https://torrentfreak.com/nintendo-wipes-out-400-switch-emulator-repos-in-single-day-github-sweep/
source: TorrentFreak
date: 2026-08-21
fetch_date: 2026-08-22T02:52:46.909309
---

# Nintendo Wipes Out 400+ Switch Emulator Repos in Single-Day GitHub Sweep

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

# Nintendo Wipes Out 400+ Switch Emulator Repos in Single-Day GitHub Sweep

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [DMCA](https://torrentfreak.com/category/anti-piracy/dmca/ "Go to the DMCA category archives.") >

Nintendo has filed seven DMCA anti-circumvention notices at GitHub in a single day, wiping out more than 400 Switch emulator repositories in one coordinated campaign. The targets include copies of the Suyu emulator, several Yuzu forks, and Skyline, an emulator that shut itself down years ago. The takedown effort was successful as most repositories are offline now, but it also shows how quickly the code can resurface.

![nintendo-sw-emu-s](https://torrentfreak.com/images/nintendo-sw-emu-s.png)GitHub is home to hundreds of millions of code repositories, including some repositories that rightsholders would rather not see online.

For Nintendo, Switch emulators have become the main challenge, one that keeps rearing its head.

Most of these emulators were killed off long ago. [Yuzu settled](https://torrentfreak.com/nintendos-yuzu-lawsuit-aims-to-pour-banana-peels-over-all-emulators-240228/) in February 2024, for example, [Ryujinx shut down](https://torrentfreak.com/ryujinx-switch-emulator-project-shuts-down-under-nintendo-pressure-241002/) that October, and the successors that tried to keep edited versions online have been targeted in waves ever since.

These waves keep coming. Earlier this week, Nintendo filed seven separate DMCA anti-circumvention notices at GitHub, all on the same day, targeting a variety of Switch emulator repositories and their forks. The combined reach is substantial. In the seven notices, more than 400 repositories were targeted.

## More Than 400 Repos

The most detailed notice targets suyu, an emulator that became popular after Yuzu’s collapse. Because the reported network was larger than 100 repositories, GitHub processed the notice against the entire network, which covered 311 repos.

The remaining six notices ranged from a lone repository to networks of a few dozen, including the independent Skyline emulator, as shown below.

| Parent repo (notice) | Project | Targets |
| --- | --- | --- |
| [vstyler96/suyu](https://github.com/github/dmca/blob/master/2026/08/2026-08-17-nintendo.md) | suyu (yuzu successor) | 311 repos (full network) |
| [skyline-emu/skyline](https://github.com/github/dmca/blob/master/2026/08/2026-08-17-nintendo-7.md) | Skyline (Android, independent) | 29 repos (full network) |
| [NicolasArvani/yuzu](https://github.com/github/dmca/blob/master/2026/08/2026-08-17-nintendo-6.md) | yuzu fork | 14 repos (full network) |
| [liushuyu/yuzu-android](https://github.com/github/dmca/blob/master/2026/08/2026-08-17-nintendo-4.md) | yuzu (Android port) | 8 repos (full network) |
| [exverge-0/yuzu-EA4176](https://github.com/github/dmca/blob/master/2026/08/2026-08-17-nintendo-5.md) | yuzu (Early Access build 4176) | 21 forks listed |
| [irlbunny-archive/MonoNX](https://github.com/github/dmca/blob/master/2026/08/2026-08-17-nintendo-2.md) | MonoNX (C#-based) | 17 forks listed |
| [IpwnedU/yuzu-master](https://github.com/github/dmca/blob/master/2026/08/2026-08-17-nintendo-3.md) | yuzu fork | Parent only |

For four of the seven notices, the table shows GitHub’s own count of the processed network, including the parent repo. For the other three, no network details were published, so the table shows the repositories named in the notice itself, including some that were redacted as “[private].”

The legal argument is the same in all seven. Nintendo argues that the emulators exist to bypass the encryption that protects its games, which violates the DMCA.

“During operation, the emulators at the reported repositories necessarily use unauthorized copies of these cryptographic keys to decrypt unauthorized copies of Nintendo Switch games, or ROMs, at or immediately before runtime without Nintendo’s authorization,” the notice read.

*Repository Unavailable*

![suyu](https://torrentfreak.com/images/suyu-1.png)

Most of these repositories now link to notices [informing visitors](https://github.com/vstyler96/suyu) that they were removed. In some cases, they point to a 404 error, suggesting that the developer voluntarily removed the repository after being notified.

## Precedents Without a Trial

To back the circumvention argument, every notice cites two court decisions as precedents, neither of which was challenged in court.

The first is the 2024 consent judgment against Tropic Haze, the company behind Yuzu, which ended in a [$2.4 million settlement](https://torrentfreak.com/nintendo-hits-circumvention-tool-linkers-with-dmca-trafficking-violation-240314/). The second is newer: Nintendo’s case against streamer Jesse Keighin, aka “EveryGameGuru,” who was [ordered to pay $17,500](https://torrentfreak.com/nintendo-wins-lawsuit-against-defiant-pirate-streamer-everygameguru/) last October after a Colorado court entered a default judgment against him.

One was a settlement, the other a default judgment after Keighin reportedly stopped responding and destroyed evidence. In neither case did a court weigh the emulator circumvention question on the merits.

*From Nintendo’s notice*
![suyu](https://torrentfreak.com/images/suyu-git.png)

At the takedown stage Nintendo does not need to show a legal precedent. GitHub says it [reviews circumvention claims carefully](https://torrentfreak.com/github-reports-dmca-takedown-record-and-surging-anti-circumvention-claims/) and will “err on the side of the developer, and leave the content up” when validity is unclear. The Yuzu framework has made Nintendo’s notices close to routine anyway.

## Defunct Skyline & Future Horizon

Among the targeted emulators Skyline stands out, as it was a Switch emulator for Android devices, not a yuzu fork. Skyline’s developers shut the project down voluntarily in 2023, but as is often the case, the open source code survived.

This week, Nintendo’s takedown notice cleared a network of 29 Skyline repos, including code that has been dormant for years. This doesn’t necessarily deal with the problem permanently, as future takedown efforts are likely on the horizon.

Every emulator on this week’s list was already supposed to be gone. However, they were forked, mirrored, or revived, which put them on Nintendo’s radar again.

For Nintendo, getting these emulator repos removed from GitHub is the easy part. Keeping the code offline is a bigger challenge, as forks may reappear faster than the notices can remove them.

* [Previous Post![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-right.svg)](https://torrentfreak.com/filmmaker-who-sued-ptp-btn-and-four-other-private-torrent-trackers-may-be-an-impostor/)

### Tagged In:

* [Emulators](https://torrentfreak.com/tag/emulators/)
* [Github](https://torrentfreak.com/tag/github/)
* [Nintendo](https://torrentfreak.com/tag/nintendo/)
* [suyu](https://torrentfreak.com/tag/suyu/)
* [yuzu](https://torrentfreak.com/tag/yuzu/)

### You Might Also Like:

[![](https://torrentf...