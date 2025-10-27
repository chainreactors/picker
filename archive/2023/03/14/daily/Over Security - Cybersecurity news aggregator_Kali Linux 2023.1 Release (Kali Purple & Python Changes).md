---
title: Kali Linux 2023.1 Release (Kali Purple & Python Changes)
url: https://www.kali.org/blog/kali-linux-2023-1-release/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-14
fetch_date: 2025-10-04T09:31:33.521894
---

# Kali Linux 2023.1 Release (Kali Purple & Python Changes)

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

![](https://www.kali.org/blog/kali-linux-2023-1-release/images/banner-2023.1-release.jpg)
Monday, 13 March 2023

# Kali Linux 2023.1 Release (Kali Purple & Python Changes)

Table of Contents

* [Kali Purple](#kali-purple)
  + [Screenshots](#screenshots)
* [Python Updates & Changes](#python-updates--changes)
  + [APT](#apt)
  + [venv](#venv)
  + [break-system-packages](#break-system-packages)
* [2023 Theme Refresh](#2023-theme-refresh)
  + [All new wallpapers](#all-new-wallpapers)
* [Desktop Updates](#desktop-updates)
  + [Xfce 4.18](#xfce-418)
    - [Panel profiles](#panel-profiles)
  + [KDE Plasma 5.27](#kde-plasma-527)
    - [New tiling system](#new-tiling-system)
  + [GNOME](#gnome)
* [Default Kernel Settings](#default-kernel-settings)
* [Known Issues](#known-issues)
* [Miscellaneous](#miscellaneous)
* [New Tools in Kali](#new-tools-in-kali)
* [Kali NetHunter Updates](#kali-nethunter-updates)
* [Kali ARM Updates](#kali-arm-updates)
* [Kali Documentation Updates](#kali-documentation-updates)
* [Kali Blog Recap](#kali-blog-recap)
* [Community Shout-Outs](#community-shout-outs)
* [Kali Team Discord Chat & Reddit AMA](#kali-team-discord-chat--reddit-ama)
* [Get Kali Linux 2023.1](#get-kali-linux-20231)

Today we are releasing Kali 2023.1 (and on our **10th anniversary**)! It will be ready for immediate [download](https://www.kali.org/get-kali/) or [updating](https://www.kali.org/docs/general-use/updating-kali/) by the time you have finished reading this post.

Given its our 10th anniversary, we are delighted to announce there are a few special things lined up to help celebrate. Stay tuned for a blog post coming out for more information! Edit: [Its out](https://www.kali.org/blog/10-years/)!

The [changelog](https://bugs.kali.org/changelog_page.php) summary since the [2022.4 release from December](https://www.kali.org/blog/kali-linux-2022-4-release/):

* **[Kali Purple](#kali-purple)** - The dawn of a new era. Kali is not only Offense, but starting to be defense
* **[Python Changes](#python-updates--changes)** - Python 3.11 & PIP changes going forward
* **[2023 Theme](#2023-theme-refresh)** - Our once a year theme update! This time, what’s old is new again
* **[Desktop Updates](#desktop-updates)** - Xfce 4.18 & KDE Plasma 5.27
* **[Default Kernel Settings](#default-kernel-settings)** - What makes the Kali kernel different
* **[New Tools](#new-tools-in-kali)** - As always, various new tools added

---

## Kali Purple

> ***We are leveling the playing field**!*

Over the years, we have perfected what we have specialized in, offensive security. We are now starting to branch into a new area, defensive security!
We are doing an initial technical preview pre-launch of “Kali Purple”. This is still in its infancy and is going to need time to mature. But you can start to see the direction Kali is expanding into. You can also be a part of helping to shape the direction!

[![Kali Purple](images/kali-purple-icon.svg)](https://www.kali.org/blog/kali-linux-2023-1-release/images/kali-purple-icon.svg)

---

**What is Kali Purple?**

The one stop shop for blue and purple Teams.

> *Feeling red? Feeling blue?* Kali Purple: You do You!

Remember what we did a decade ago with Kali Linux? Or with [BackTrack](https://www.backtrack-linux.org/) before that? We made offensive security accessible to everyone. No expensive licenses required, no need for commercial grade infrastructure, no writing code or compiling tools to make it all work… Just download Kali Linux and do your thing.

We are excited to start a new journey with the mission to do exactly the same for defensive security: Just download Kali Purple and do your thing.

Kali Purple is starting out as a Proof of Concept, evolving into a framework, then a platform *(just like how Kali is today)*. The goal is to make enterprise grade security accessible to everyone.

---

**What is in Kali Purple?**

On a higher level, Kali Purple consists of:

* A reference architecture for the ultimate SOC In-A-Box; perfect for:
  + Learning
  + Practicing SOC analysis and threat hunting
  + Security control design and testing
  + Blue / Red / Purple teaming exercises
  + Kali spy vs. spy competitions ( bare knuckle Blue vs. Red )
  + Protection of small to medium size environments
* Over 100 defensive tools, such as:
  + [Arkime](https://pkg.kali.org/pkg/arkime) - Full packet capture and analysis
  + [CyberChef](https://pkg.kali.org/pkg/cyberchef) - The cyber swiss army knife
  + `Elastic Security` - Security Information and Event Management
  + [GVM](https://www.kali.org/tools/gvm/) - Vulnerability scanner
  + [TheHive](https://pkg.kali.org/pkg/thehive) - Incident response platform
  + `Malcolm` - Network traffic analysis tool suite
  + [Suricata](https://pkg.kali.org/pkg/suricata) - Intrusion Detection System
  + [Zeek](https://pkg.kali.org/pkg/zeek) - (another) Intrusion Detection System *(both have their use-cases!)*
  + *…and of course all the usual [Kali tools](https://www.kali.org/tools/)*
* Defensive tools [documentations](https://gitlab.com/kalilinux/kali-purple/documentation)
* [Pre-generated image](https://www.kali.org/get-kali/)
* Kali Autopilot - an attack script builder / framework for automated attacks
* Kali Purple Hub for the community to share:
  + Practice pcaps
  + Kali Autopilot scripts for blue teaming exercises
* [Community Wiki](https://gitlab.com/kalilinux/kali-purple/documentation/-/wikis/home)
* A defensive menu structure according to NIST CSF (National Institute of Standards and Technology Critical Infrastructure Cybersecurity):
  + Identify
  + Protect
  + Detect
  + Respond
  + Recover
* Kali Purple [Discord](https://discord.kali.org/) channels for community collaboration and fun
* And theme: installer, menu entries & Xfce!

…And this is just the beginning of our journey.

### Screenshots

This is what it looks like. Some defensive tools:

**Elastic SIEM**:

[![Elastic SIEM](images/Elastic-01-Dashboard-OPNsense.png)](https://www.kali.org/blog/kali-linux-2023-1-release/images/Elastic-01-Dashboard-OPNsense.png)

**Arkime**:

[![Arkime](images/Malcolm-01-Arkime.png)](https://www.kali.org/blog/kali-linux-2023-1-release/images/Malcolm-01-Arkime.pn...