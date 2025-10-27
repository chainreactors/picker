---
title: Happy 10th anniversary & Kali's story ...so far
url: https://www.kali.org/blog/10-years/
source: Kali Linux
date: 2023-03-30
fetch_date: 2025-10-04T11:09:36.686042
---

# Happy 10th anniversary & Kali's story ...so far

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

![](https://www.kali.org/blog/10-years/images/banner-kali-10-year.jpg)
Wednesday, 29 March 2023

# Happy 10th anniversary & Kali's story ...so far

Table of Contents

* [Yesterday is History: The Past](#yesterday-is-history-the-past)
  + [Dragon Logo](#dragon-logo)
  + [BackTrack 6?](#backtrack-6)
  + [Kali’s Name](#kalis-name)
  + [Screenshot Tour](#screenshot-tour)
* [Today: The Present](#today-the-present)
  + [Kali 2023.1](#kali-20231)
  + [Online Puzzle](#online-puzzle)
  + [Song](#song)
  + [Sneakers](#sneakers)
  + [PEN-200/PWK Refresh](#pen-200pwk-refresh)
  + [AMAs](#amas)
* [Tomorrow: The Future](#tomorrow-the-future)
* [Timelines](#timelines)
  + [Talks](#talks)
  + [Trailer Videos](#trailer-videos)
  + [Hacked](#hacked)
  + [April Fools](#april-fools)
    - [Kali4Kids](#kali4kids)
  + [Kali Dojo](#kali-dojo)

Wednesday 13th, March 2013, 10 years ago, Kali Linux v1.0 was [first released](https://www.kali.org/docs/introduction/press-release/). Today we want to celebrate Kali’s 10th anniversary!

Time has flown. And gosh, a lot has changed since then!
*They grow up so fast!*

This is the story of how Kali came to be, and some of the challenges along the way.

## Yesterday is History: The Past

How did we get to where we are today? There is a quick answer, and a not so quick answer.

**[Quick](https://www.kali.org/releases/) history lesson**

It all began in 2004, with **Whoppix**, a security operating system based on Knoppix. This lead into **WHAX** in 2005, which used Slax. In 2006, **BackTrack Linux** happened which was based initially on Slax, then moved to Ubuntu.
Every one of these OSes and its changes were done to solve different problems. Using everything which was learnt, **Kali Linux** was born. A fresh start in March 2013.

**[Longer](https://www.kali.org/docs/introduction/kali-linux-history/) history lesson**

*Knoppix - Initial two weeks work*

Whoppix *(White-Hat and knOPPIX)* came about as the founder, @Muts, was doing an in-person air-gap network penetration test lasting for two weeks in 2004. It was a government contract, and he was not allowed to bring in his own laptop nor allowed to install any software on their machines. So every day, he was only allowed to take in software on a CD-ROM, before it was destroyed at the end of each day. At the time, Live CDs were the “in thing”. They would allow you to run a Linux OS completely off a disk, using RAM as a temporary HDD, without leaving a trace behind. Knoppix was chosen as the base OS which is Debian-based.
He created one for this assessment and pre-loaded it with various tools that he believed he would need for the job. Each night, he would go back, tweak it by adding more tools or bug fixes. After the assessment was over, he cleaned it up and shared it online on a forum in August 2004.
He then left for a vacation. Upon getting back he checked the logs to see the download numbers, and could not believe that it was so popular! He started to get requests from people, asking for tools to included as well as bug reports.

[![whoppix 2.x](images/Whoppix2-1.png)](https://www.kali.org/blog/10-years/images/Whoppix2-1.png)

---

*Slax - Starting to take it seriously*

What had started off as a “quick small thing” for single assessment, had started to gain traction. With Whoppix growing in popularity, it was becoming harder to develop for. At the time, Slax had a more mature toolchain for generating Live-CDs and working with OverlayFS. Thus it was a better suited option.
*Editors note: We cannot say for certain, but the image file size may have become an issue. With more tools wanting to be added, space was running out. This was at a time when CD-R were at their peak, giving you 650-700 MB and USB media was not yet on the scene. By switching to Slax, the base OS size dropped, and allowed for more custom packages to be included as well as tighter compression (LZMA). Overall, this gave a lot more space to grow.*

[![Whax 3.0](images/Whax3-5.png)](https://www.kali.org/blog/10-years/images/Whax3-5.png)

---

*Merging into BackTrack*

At the same time, there was a similar project happening over at remote-exploit, **Auditor Security Collection** (based on Knoppix), which first started in 2005. Auditor and WHAX had similar goals, but different strengths. At the time, cooperation on “Open-Source projects” was very different to what it is today, as it was “I made this thing, I’m sharing it.” It was more a few large players contributed, rather being able to accept work from lots of smaller submissions. After a bit of discussion between the authors, it made sense rather than both projects tackling the same problems, for the projects to merge together. This created BackTrack in May 2006. Initially, it was still based on Slax, but moved to Ubuntu later on.
*Editors note: We cannot say for certain, where the name “BackTrack” originated from. At the time, when internally debugging problems, the phrase “Back tracking through the logs” got said frequency. We cannot say which came first, the phrase or the name.*

[![BackTrack 1](images/BackTrack1-3.png)](https://www.kali.org/blog/10-years/images/BackTrack1-3.png)

---

*OffSec’s Start*

Walking around Black Hat USA 06, the team noticed how many people were using their project, and offering training using it. After listening to a few sales pitches, and training offerings, the team noticed just how many people were getting it wrong. As a result, [OffSec (previously known as Offensive Security)](https://www.offsec.com/?utm_source=kali&utm_medium=web&utm_campaign=blog), was created. Training from the people who made the tools. Who else would know it better?!

---

*USB - Live-Boot & Persistent*

BackTrack now had a stable, mature Live-CD project and it was exactly what was needed for the problem which was air-gap networks at the time. Whilst these Live-CDs were the answer for some scenarios, the team wanted to expand into more areas. The cost of USB flash drives/sticks had came down dramatically, as a result were more freely available. There was then a shift to “Live-Boot” (either CDs or USBs). The next item to solve would be getting their data to be “persistent” rather than losing it when p...