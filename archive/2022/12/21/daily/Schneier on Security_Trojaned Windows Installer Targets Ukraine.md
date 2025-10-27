---
title: Trojaned Windows Installer Targets Ukraine
url: https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html
source: Schneier on Security
date: 2022-12-21
fetch_date: 2025-10-04T02:07:12.077412
---

# Trojaned Windows Installer Targets Ukraine

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

## Trojaned Windows Installer Targets Ukraine

Mandiant is [reporting](https://www.mandiant.com/resources/blog/trojanized-windows-installers-ukrainian-government) on a trojaned Windows installer that targets Ukrainian users. The installer was left on various torrent sites, presumably ensnaring people downloading pirated copies of the operating system:

> Mandiant uncovered a socially engineered [supply chain](https://services.google.com/fh/files/blogs/perspectives_on_security_volume_one_digital.pdf) operation focused on Ukrainian government entities that leveraged trojanized ISO files masquerading as legitimate Windows 10 Operating System installers. The trojanized ISOs were hosted on Ukrainian- and Russian-language torrent file sharing sites. Upon installation of the compromised software, the malware gathers information on the compromised system and exfiltrates it. At a subset of victims, additional tools are deployed to enable further intelligence gathering. In some instances, we discovered additional payloads that were likely deployed following initial reconnaissance including the STOWAWAY, BEACON, and SPAREPART backdoors.

One obvious solution would be for Microsoft to give the Ukrainians Windows licenses, so they don’t have to get their software from sketchy torrent sites.

Tags: [backdoors](https://www.schneier.com/tag/backdoors/), [malware](https://www.schneier.com/tag/malware/), [Russia](https://www.schneier.com/tag/russia/), [supply chain](https://www.schneier.com/tag/supply-chain/), [torrents](https://www.schneier.com/tag/torrents/), [Ukraine](https://www.schneier.com/tag/ukraine/)

[Posted on December 20, 2022 at 7:30 AM](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html) •
[13 Comments](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html#comments)

### Comments

stephen •
[December 20, 2022 7:53 AM](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html/#comment-414313)

Or, the Ukrainians could leverage Linux, instead of relying on software and the charity of one monopolistic company.

Clive Robinson •
[December 20, 2022 8:29 AM](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html/#comment-414315)

@ Bruce, ALL,

**Side Note :** Although not directly connected to this “supply chain” attack, it’s been noted that 2022 has been the year of “Signed Driver” supply chain attacks,

<https://news.sophos.com/en-us/2022/12/13/signed-driver-malware-moves-up-the-software-trust-chain/>

Oh and an update on “Azov” the fake Ransomware loosly designed to look like it came from the Ukraine but did not (it has the hallmarks of some “old School” Russian virus writer going back decades).

<https://research.checkpoint.com/2022/pulling-the-curtains-on-azov-ransomware-not-a-skidsware-but-polymorphic-wiper/>

dorukayhan •
[December 20, 2022 1:20 PM](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html/#comment-414320)

> One obvious solution would be for Microsoft to give the Ukrainians Windows licenses, so they don’t have to get their software from sketchy torrent sites.

Or just advertise [their already existing ISO download page](https://www.microsoft.com/uk-ua/software-download/windows10ISO)?

lurker •
[December 20, 2022 1:43 PM](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html/#comment-414323)

@dorukayhan

@stephen
Linux is all well and good, until you have to deal with files or foreign correspondents who insist on using some MS format. Wine is perpetually “not quite there yet”. Where do you get an affordable Windows installer for a VM?

Arclight •
[December 20, 2022 2:17 PM](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html/#comment-414325)

Also, you can just download Windows images directly from Microsoft. Even if you purchase license keys from a questionable source (such as an e-waste recycler or refurbisher), you can just install from clean media and not worry about about the binaries. In this case, the worst possible outcome is that Windows doesn’t activate.

Ted •
[December 20, 2022 4:14 PM](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html/#comment-414327)

“The use of trojanized ISOs is novel in espionage operations”

Really? That surprises me a little bit.

It was interesting to see how the ISO was altered. Two legitimate tasks were modified with additional instructions. The trojanized ISO also contains an original batch script that does several things, including disabling Windows updates and activating a Windows license.

Mandiant reported that three Ukrainian organizations were targeted for follow on activity following an installation. They don’t say anything about the details of these installations.

Ismar •
[December 21, 2022 3:53 AM](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html/#comment-414337)

&Clive- reading the article- I don’t think any rootkits were used, rather some post-installation tasks were used to disable / hijack some of the windows functionality to exploit the machines.
You are really asking for it, though, if installing from torrents

Clive Robinson •
[December 21, 2022 9:10 AM](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html/#comment-414344)

@ Ismar,

> “reading the article”

Which one?

@Bruce posted links to one article (Mandiant), and I posted two links to related stories (from Sophos and Checkpoint).

Dex •
[January 15, 2023 6:44 AM](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html/#comment-415574)

Sure, give them free Microsoft licenses. We’ve already given them billions of dollars, the UK’s giving them tanks, and unlike me, they have eggs.

This is pretty funny considering the other snippet about instructions on surrending to a drone.

I know Bruce has gone off the deep end, gulping the koolaid, but come on.

tl;dr No, American businesses shouldn’t give free licenses to nations which aren’t even are allies, who have crappy cyber policies.

And no one should voluntarily run Windows 10 or 11 any way. Sure, linux sucks, but it’d solve this problem.

Clive Robinson •
[January 15, 2023 9:25 AM](https://www.schneier.com/blog/archives/2022/12/trojaned-windows-installer-targets-ukraine.html/#comment-415586)

@ Dex,

Re : Ukraine

> “to nations which aren’t even are allies”

You might want to have a think on that claim.

The Ukraine was a nation with a lot of Russian nuclear technology including weapons it had inherited, that they did not want. As although they had the technical abilities to maintain them they did not want the problems associated with the badly designed and rapidly ag...