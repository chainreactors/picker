---
title: Kali Linux 2023.3 Release (Internal Infrastructure & Kali Autopilot)
url: https://www.kali.org/blog/kali-linux-2023-3-release/
source: Kali Linux
date: 2023-08-24
fetch_date: 2025-10-04T12:03:30.754438
---

# Kali Linux 2023.3 Release (Internal Infrastructure & Kali Autopilot)

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

![](https://www.kali.org/blog/kali-linux-2023-3-release/images/banner-2023.3-release.jpg)
Wednesday, 23 August 2023

# Kali Linux 2023.3 Release (Internal Infrastructure & Kali Autopilot)

Table of Contents

* [Internal Infrastructure](#internal-infrastructure)
  + [Mirror Traces](#mirror-traces)
  + [Packaging Tools](#packaging-tools)
* [Kali Autopilot](#kali-autopilot)
* [New Tools in Kali](#new-tools-in-kali)
  + [Rekono - Community Package Submission](#rekono---community-package-submission)
* [Miscellaneous](#miscellaneous)
* [Kali NetHunter Updates](#kali-nethunter-updates)
* [Kali ARM Updates](#kali-arm-updates)
* [Kali Website Updates](#kali-website-updates)
* [Community Shout-Outs](#community-shout-outs)
  + [New Kali Mirrors](#new-kali-mirrors)
* [Kali Team Discord Chat](#kali-team-discord-chat)
* [Get Kali Linux 2023.3](#get-kali-linux-20233)

Today we are delighted to introduce our latest [release of Kali](https://www.kali.org/releases/), 2023.3. This release blog post does not have the most features in it, as a lot of the changes have been behind-the-scenes, which brings a huge benefit to us and an indirect positive effect to you as end-users. It always goes without saying, but there are a number of new packages and tools as well as the standard updates. If you want to see what’s new for yourself [download](https://www.kali.org/get-kali/) or [upgrade *if you have an existing Kali Linux installation*](https://www.kali.org/docs/general-use/updating-kali/).

The highlights of the [changelog](https://bugs.kali.org/changelog_page.php) since the [2023.2 release from May](https://www.kali.org/blog/kali-linux-2023-2-release/):

* **[Internal Infrastructure](#internal-infrastructure)** - Major stack changes is under way
* **[Kali Autopilot](#kali-autopilot)** - The automation attack framework has had an major overhaul
* **[New Tools](#new-tools-in-kali)** - 9 new tools added this time round!

---

## Internal Infrastructure

With the release of Debian 12 which came out this summer, we took this opportunity to re-work, re-design, and re-architecture our infrastructure. It is as massive as it sounds, and should not be a surprise that its not yet complete! This is where a good amount of our focus has been for this release-cycle (and also the next one unfortunately). We are hoping that the majority of it will be done by the end of the year (so we can get back to what we do best!)

This gives an excuse and the motivation to simplify our software stack as much as possible.
Example, using one single:

* OS version (Debian 12)
* CDN/WAF (Cloudflare)
* Web server service (Nginx)
* Infrastructure as Code (Ansible)

We also have some other goals, and replacing certain software with others (phase #2).

At the same time, we have automated some actions such as:

* The cleaning up of suites (aka [branches](https://www.kali.org/docs/general-use/kali-branches/) - kali-experimental and [kali-bleeding-edge](https://www.kali.org/docs/general-use/kali-bleeding-edge/))

We are very much underway with these projects already (as bug bounty hunters may notice the changes)!

### Mirror Traces

We have a new sub-domain, [mirror-traces.kali.org](https://mirror-traces.kali.org/)! This is to help mirror admins for our community mirrors. This now gives everyone using it more details and insight which is useful when troubleshooting and debugging issues.

True to our word, we are doing more in the open, the git repository can be found here: [gitlab.com/kalilinux/tools/mirror-status](https://gitlab.com/kalilinux/tools/mirror-status).

### Packaging Tools

For a long time, we have shared our [home-made scripts](https://gitlab.com/kalilinux/tools/packaging) publicly, which is our helping aid to manage all our packages in Kali.
Recently we have expanded on them by giving the existing files a refresh by adding additional features and various quality-of-life improvements, as well as including new ones.

As a recap, if you want to have a peek at some back-end development:

* [Autopkgtest](https://autopkgtest.kali.org/) - Using `debci` in a CI fashion, we can test packages being built.
  + This integrates into Britney.
* [Britney2](http://repo.kali.org/britney) ([Git repo](https://gitlab.com/kalilinux/tools/britney2)) - Migrates packages between all of our suites (aka [branches](https://www.kali.org/docs/general-use/kali-branches/), such as “debian-testing”, “kali-rolling”, and “kali-last-snapshot” to name a few).
* [Build-Logs](http://repo.kali.org/build-logs/) - Output of [our images/platform](https://gitlab.com/kalilinux/build-scripts/) as well as [packages](https://gitlab.com/kalilinux/packages) being created on each supported architecture.
* Janitor - **Kali Bot** - This is our automated packager as it will apply everything from minor formatting changes to preparing an package update.
  + *The long term goal of this is to have it handle kali-bleeding-edge, linking into Autopkgtest.*
* [Package Tracker](https://pkg.kali.org/) - Tracks each packages version’s history.
* [Packaging CI Overview](https://kalilinux.gitlab.io/tools/packaging/) ([Git repo](https://gitlab.com/kalilinux/tools/packaging/-/blob/main/bin/gitlab-overview?ref_type=heads)) - Quick (and dirty) overview of our package’s CI status.
* [Upstream-Watch](https://kalilinux.gitlab.io/tools/upstream-watch/) ([Git repo](https://gitlab.com/kalilinux/tools/upstream-watch)) - Monitors when there is an update upstream.

## Kali Autopilot

With the release of [Kali Purple](https://gitlab.com/kalilinux/kali-purple/documentation/-/wikis/home) in [Kali 2023.1](https://www.kali.org/blog/kali-linux-2023-1-release/), we also had the debut of [Kali Autopilot](https://gitlab.com/re4son/kali-autopilot/-/wikis/home). Since then, its been worked on and is unrecognizable with its redesigned GUI and multitudinous amount of features added.

**What is Kali Autopilot? We are glad you asked!**
Kali Autopilot is an automated attack framework. It is a bit like an “AutoPwner”, which follows pre-defined “attack scenarios”.
The motivation originally started its development for the defensive side of Kali.

It is a lot easier to demonstrate Kali’s offensive side, *especially when you start...