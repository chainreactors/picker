---
title: Kali Linux 2024.3 Release (Multiple transitions)
url: https://www.kali.org/blog/kali-linux-2024-3-release/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-12
fetch_date: 2025-10-06T18:29:55.721994
---

# Kali Linux 2024.3 Release (Multiple transitions)

* [Join Free CTF](https://www.offsec.com/events/the-gauntlet/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* [Get Kali](https://www.kali.org/get-kali/)
* [Blog](https://www.kali.org/blog/)
* Documentation

  [Documentation Pages](https://www.kali.org/docs/)
  [Tools Documentation](https://www.kali.org/tools/)
  [Frequently Asked Questions](https://www.kali.org/faq/)
  [Known Issues](https://bugs.kali.org/search.php?project_id=1&category_id[]=General%20Bug&category_id[]=Kali%20Package%20Bug&category_id[]=Kali%20Package%20Improvement&status[]=30&status[]=40&status[]=50&sticky=on&sort=id%2Clast_updated&dir=DESC%2CDESC&hide_status=-2&match_type=0)
* Community

  [Community Support](https://www.kali.org/community/)
  [Forums](https://forums.kali.org/)
  [Discord](https://discord.kali.org/)
  [Join Newsletter](https://www.kali.org/newsletter/)
  [Mirror Location](https://http.kali.org/README?mirrorlist)
  [Get Involved](https://www.kali.org/docs/community/contribute/)
* [Courses](https://www.offsec.com/kali-training/courses/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* Developers

  [Git Repositories](https://gitlab.com/kalilinux)
  [Packages](https://pkg.kali.org/)
  [Auto Package Test](https://autopkgtest.kali.org/)
  [Bug Tracker](https://bugs.kali.org/)
  [Kali NetHunter Stats](https://nethunter.kali.org/)
* About

  [Kali Linux Overview](https://www.kali.org/features/)
  [Press Pack](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip)
  [Wallpapers](https://www.kali.org/wallpapers/)
  [Kali Swag Store](https://offsec.usa.dowlis.com/kali/view-all.html)
  [Meet The Kali Team](https://www.kali.org/about-us/)
  [Partnerships](https://www.kali.org/partnerships/)
  [Contact Us](https://www.kali.org/contact/)

LIGHT
[ ] DARK

![](https://www.kali.org/blog/kali-linux-2024-3-release/images/banner-2024.3-release.jpg)
Wednesday, 11 September 2024

# Kali Linux 2024.3 Release (Multiple transitions)

Table of Contents

* [New Tools in Kali](#new-tools-in-kali)
* [Kali NetHunter Updates](#kali-nethunter-updates)
* [Kali ARM SBC Updates](#kali-arm-sbc-updates)
  + [Kali Documentation](#kali-documentation)
* [Community Shout-Outs](#community-shout-outs)
  + [New Kali Mirrors](#new-kali-mirrors)
* [Get Kali Linux 2024.3](#get-kali-linux-20243)

With summer coming to an end, so are package migrations, and Kali 2024.3 can now be released. You can now start [downloading](https://www.kali.org/get-kali/) or [upgrading *if you have an existing Kali installation*](https://www.kali.org/docs/general-use/updating-kali/).

The summary of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2024.2 release from June](https://www.kali.org/blog/kali-linux-2024-2-release/) is:

* **[Qualcomm NetHunter Pro Devices](#kali-nethunter-updates)** - Qualcomm Snapdragon SDM845 SoC now supported
* **[New Tools](#new-tools-in-kali)** - 11x new tools in your arsenal

---

Our focus has been on a lot of behind the scenes updates and optimizations since the last release. There have been some messy migrations, with multiple stacks, all interrelating (transition have been like buses, all coming at once!). After the [t64 transition](https://www.kali.org/blog/kali-linux-2024-2-release/) finished up, it was straight into **multiple** other transitions: **GCC 14**, the **glibc 2.40**, and **Python 3.12**.

This last one is the most significant! This new Python release removed some long-deprecated APIs, breaking a fair number of packages. We have been busy fixing it all *(weeks of work!)*, we are almost there, Python 3.12 will be the default in the **next** version of Kali - 2024.4. **With Python 3.12, there will be a major change for users: it won’t be possible to install Python packages with `pip` anymore**. [We wrote about that a year ago already](https://www.kali.org/blog/python-externally-managed/), we invite you to read that again if you are an avid user of `pip`.

But that will be for the *next Kali release, 2024.4*, due by the end of the year. In the meantime, **this new release 2024.3 still has Python 3.11 as the default Python interpreter**.

An unfortunate consequence of this situation is that, as the whole Python 3.12 stack did not enter [Kali-rolling](https://www.kali.org/docs/general-use/kali-branches/) yet, it also blocked *other packages* *(seemingly unrelated to Python)* from entering Kali-rolling. In other words, over the last 2 months the pace of updates in Kali-rolling went down, making this release less exciting than usual. This temporary slowdown should end in the coming days and weeks, as Python 3.12 finally hits Kali-rolling. At this point packages will resume flowing as usual, so users of Kali-rolling should be ready for a lot of updates!

To finish: apart from packaging, various projects either got started or continued to make progress, but are not ready for release just yet (such as having a new Kali forum, NetHunter Store updates and refreshing Kali-menu).

---

## New Tools in Kali

This Kali release is about package updates.
For end users its mostly about new tools added, for us, its about the updated stacks!

The community once again has set up and added various new tools. Long term contributor [Arszilla](https://gitlab.com/arszilla) has been busy again!
Here is a highlight of what new tools have been added *(to the network repositories)*:

* [goshs](https://www.kali.org/tools/goshs/) - Think SimpleHTTPServer, but written in Go, and with more features
* [graudit](https://www.kali.org/tools/graudit/) - Grep Rough AUDIT: source code auditing tool
* [gsocket](https://www.kali.org/tools/gsocket/) - Allows two machines on different networks to communicate with each other
* [hekatomb](https://www.kali.org/tools/hekatomb/) - Extract and decrypt all credentials from all domain computers *(Submitted by [Arszilla](https://gitlab.com/arszilla))*
* [mxcheck](https://www.kali.org/tools/mxcheck/) - Info and security scanner for e-mail servers *(Submitted by [Arszilla](https://gitlab.com/arszilla))*
* [netexec](https://www.kali.org/tools/netexec/) - Network service exploitation tool that helps automate assessing the security of large networks *(Submitted by [Arszilla](https://gitlab.com/arszilla))*
* [netscanner](https://www.kali.org/tools/netscanner/) - Network scanner & diagnostic tool with modern TUI *(Submitted by [Arszilla](https://gitlab.com/arszilla))*
* [obsidian](https://www.kali.org/tools/obsidian/) - Private and flexible writing app that adapts to the way you think
* [sippts](https://www.kali.org/tools/sippts/) - Set of tools to audit SIP based VoIP Systems *(Submitted by [Arszilla](https://gitlab.com/arszilla))*
* [sprayhound](https://www.kali.org/tools/sprayhound/) - Password spraying tool and Bloodhound integration *(Submitted by [Arszilla](https://gitlab.com/arszilla))*
* [sqlmc](https://www.kali.org/tools/sqlmc/) - Check all URLls of a domain for SQL injections *(Submitted by [Arszilla](https://gitlab.com/arszilla))*

*It goes without saying, that there has been numerous packages updates and new libraries as well.*

Again, we want to shout out Arszilla and his multiple contributions. Always remember, you can contribute as well! We are always open for engagement from you if you want to get involved.

As hinted in [our previous 2024.2 release](https://www.kali.org/blog/kali-linux-2024-2-release/#new-tools-in-kali), the [Kali kernel](https://pkg.kali.org/pkg/linux) is now also at 6.8.

## Kali NetHunter Updates

Kali NetHunter 2024.3 has been held back for the the time being, as we are busy upating the build infrastructure.
We will release the updated images when they are ready (hopefully in a few weeks), and talk whats new with them in the next Kali release 2024.4 *(Bye Mana!)*.

Fortunately, we can say there are new supported devices!
We are excited to release Kali NetHunter Pro images for devices with a Qualcomm Snapdragon SDM845 SoC (System on a Chip), such as:

* OnePlus 6 (enchilada)/6T (fajita) [SDM84...