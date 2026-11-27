---
title: Takedown Notice Hits 102,000 Wand-Enhancer Repositories on GitHub
url: https://torrentfreak.com/takedown-notice-hits-102000-wand-enhancer-repositories-on-github/
source: TorrentFreak
date: 2026-11-26
fetch_date: 2026-11-27T10:17:39.114530
---

# Takedown Notice Hits 102,000 Wand-Enhancer Repositories on GitHub

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

# Takedown Notice Hits 102,000 Wand-Enhancer Repositories on GitHub

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Takedowns and Seizures](https://torrentfreak.com/category/anti-piracy/takedowns-and-seizures/ "Go to the Takedowns and Seizures category archives.") >

A takedown notice that targeted four files of Wand-Enhancer, a popular patcher that unlocks Pro features in the game trainer app Wand, affected more than 100,000 GitHub repositories. GitHub processed the notice, sent by Web Sheriff, against the project's entire fork network. The original repo is still online, minus the four files, but the developer has since retired it and now points users to an alternative trainer client.

![game trainer wandenhancer](https://torrentfreak.com/images/wandenhancerlogo.png)
[Game trainers](https://en.wikipedia.org/wiki/Trainer_%28games%29) are handy tools that allow players to give themselves infinite health, extra money, or other perks in single-player games.

One of the best-known trainer apps is WeMod, which says that more than 40 million gamers have used its software.

The tool rebranded as [Wand](https://wand.com/) late last year and a basic version is free to use. However, some features are missing and Wand also [brought back](https://wand.com/en/news/changes-to-wands-free-plan) a two-hour daily limit on mods for free users.

These limitations are removed by the paid Pro version but not everyone is willing to pay, of course. This is where the open-source Wand-Enhancer project comes in, which built up more than 33,000 stars on GitHub.

The tool patches a local Wand installation and according to an older README it offered troubleshooting tips for when “Pro or mods stop working.” Wand is not at all pleased with this. The company sees it as a pirate tool that people use to avoid paying and it recently took action.

## Four Files, 102K Repos

Earlier this month, anti-piracy outfit [Web Sheriff](https://torrentfreak.com/web-sheriff-targets-ubuntu-com-urls-with-overbroad-takedown-notices-210613/) filed a DMCA notice with GitHub on behalf of WeMod LLC.

The notice lists four specific files from the Wand-Enhancer repository. It alleges copyright infringement and claims that the patcher circumvents Wand’s technological protection measures.

“Wand Enhancer changes the ASAR integrity fuse and rewrites account-handling code; the rewritten code supplies a subscription object that causes specific Wand client gates to evaluate as Pro,” the notice reads.

*Wand’s protection measures*
![protection wand](https://torrentfreak.com/images/wandprotect.png)

Put simply, [ASAR integrity](https://www.electronjs.org/docs/latest/tutorial/asar-integrity) is a feature that checks whether an app’s packaged code was modified. According to the notice, the patcher changes that safeguard and rewrites code so specific features treat the user as Pro.

While only four files were listed, Web Sheriff also stated that, after reviewing several of the repository’s copies, it believes “all or most” of these forks are also copyright infringing.

On GitHub, the original repositories and all its forks (copies made by other users) form a “network,” and Wand-Enhancer’s was massive. The project didn’t publish ready-made executables. Instead, it told users to build their own copy in a fork.

“The project publishes no prebuilt executables. You build your own in your fork with GitHub Actions,” the README previously read.

This likely explains why the network grew so large. With more than 100 repositories in the network, combined with Web Sheriff’s “all or most” claim, GitHub’s policy for large fork networks kicked in.

“Because the reported network that contained the allegedly infringing content was larger than one hundred (100) repositories, and the submitter alleged that all or most of the forks were infringing to the same extent as the parent repository, GitHub processed the takedown notice against the entire network of 102K repositories, inclusive of the parent repository,” GitHub notes.

On top of the DMCA, GitHub says that one or more of the repositories were processed under its Acceptable Use Policies, which prohibit sharing software that bypasses checks for product licensing keys.

## Largest Takedown We’ve Seen

GitHub has published network sizes with its fork takedowns since 2021, and as far as we know, this is the largest so far. The previous record holder we could find, [from August 2025](https://github.com/github/dmca/blob/master/2025/08/2025-08-13-n8n.md), covered 9,225 repositories.

The Wand notice even exceeds the 47,228 repositories that GitHub’s takedowns [affected](https://torrentfreak.com/github-reports-dmca-takedown-record-and-surging-anti-circumvention-claims/) in all of 2025.

This is not WeMod’s first attempt to remove a Pro unlocker from GitHub either. In 2024, the company [targeted](https://github.com/github/dmca/blob/master/2024/06/2024-06-25-wemod.md) the “wemod-pro-unlocker” repository and 47 forks.

At the time, GitHub wrote that it “did not find sufficient information to determine a valid anti-circumvention claim,” but that the notice contained other valid copyright claims. This time, GitHub’s note doesn’t mention the anti-circumvention claim at all.

## Patcher Retired

Before disabling anything, GitHub says it contacted the owners of some or all of the affected repositories to give them an opportunity to make changes. It also provided information on how to file a counter-notice.

The Wand-Enhancer developer responded quickly, too. On November 11, a warning was added to the README, stating that the files named in the notice were removed from the repository and its history. The file links in the notice now [return a 404 error](https://github.com/k1tbyte/Wand-Enhancer/blob/c6ae7a3ad49388ab9ad0ef6e06d235b59cc573cb/WandEnhancer/Core/EnhancerConfig.cs).

When we checked today, the main repository was online with about 1,100 forks.

The live forks we checked all carry the updated README, which suggests that they were made after the cleanup. At least some older forks remain disabled, though. The fork of a user who complained in the issue tracker, for example, still shows GitHub’s DMCA notice.

On November 20, the developer also announced that Wand-Enhancer will no longer be maintained. The README now points to a “continuation” of the project, an alternative trainer client that uses the player’s own Wand account. That project doesn’t advertise any Pro unlocking features.

*Wand-Enhancer’s README*

![Wand-Enhancer's README](https://torrentfreak.com/images/wand-enhancer-readme-dmca.png)

Whether that’s enough to satisfy WeMod has yet to be seen. So far, we haven’t seen any lawsuit in U.S. federal court.

However, the November notice, and an [October notice](https://github.com/github/dmca/blob/master/2026/10/2026-10-16-wand.md) that targeted two other Wand-Enhancer repositories, both warn that an evidence dossier has been prepared for legal proceedings against “THE ‘PIRATES’ CONCERNED” and everyone who facilitates them, “INCLUDING, BUT NOT LI...