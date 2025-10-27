---
title: Implement but never move
url: https://buaq.net/go-170910.html
source: unSafe.sh - 不安全
date: 2023-07-01
fetch_date: 2025-10-04T11:51:11.815090
---

# Implement but never move

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Implement but never move

I really appreciate well-written implementation guides for server-cli
*2023-6-30 19:24:36
Author: [fyr.io(查看原文)](/jump-170910.htm)
阅读量:26
收藏*

---

I really appreciate well-written implementation guides for server-client software, but what really gets me excited is seeing *migration* guides for when you need to decommission that legacy OS and move onto something supported and current. Even the bad migration guides are great to have, but some that I’ve come across are works of art – numbered-list instructions that are clear and concise, incorrect assumptions busy sysadmins have during the migration are highlighted then corrected, screenshots where required, mid-migration tests to ensure things are going as smoothly as they seem… ahh, dreamy.

One of my personal pet peeves, however, is purchased server based software products that *don’t* come with any migration guidance or instructions.

I’m spending a lot of time at the moment moving niche (read: there’s only a couple of options and they all suck) and poorly made software from older server OS’s to newer ones, and whilst some of them are fine and can be figured out right away, most of them have… issues. Typically you can just install $dumpsterFire fresh to the new server, dump the existing database and throw it over the fence to the new server (yes, some of this terrible software *rEqUiReS tHe DaTaBaSe Is oN tHe SaMe SeRvEr*), maybe I’ll need to update some config files and point the new install at the existing database. One CNAME change later for the clients and you’re golden. Simple stuff.

Sometimes, however, you need to perform some forbidden magical incantations, and the kick to the teeth in many cases is that nobody in $org will write down what they are publicly. So you gotta pick the phone up and get some overworked and underpaid $tech at $org to walk you through the process, shooting down the constant stream of bugs and errors that occur along the way due to the shoddy quality of $dumpsterFire with bullets of solidified experience (that’ll no doubt be lost when $tech has had enough and leaves for greener pastures.)

Or, even worse than that… the $org requires payment for a migration because migrations aren’t considered “support” and are “optional”. Yes, it is support. And no, it isn’t optional.

Dear organisations that explicitly hide their migration guides to force an already-paying customer to pay you yet again to migrate your horrible software from one server to another (immoral), that INSIST that you “must TeamViewer in to do this” (in business hours only!?), that there’s no possible way anyone else can do it (false and stupid), that require DA/root accounts (you don’t), that have to be installed on a Domain Controller (I’m crying), that MUST have unmitigated 24/7 access by installing un-licensed teamviewer (Oh no you won’t)… There’s even one software solution here which “requires” a physical server. In 2023. The software won’t work in a virtual machine. (Oh, wait, spoiler: *it works fine in a VM and has been working fine for over a decade*)

To those organisations I say: fuck you. Do better.

Because I’m writing this all down, I’m recording my screen when you connect to solve unhelpful errors in your hidden log files, I’m fixing your stupid permission requirements and immediately uninstalling any additional or third party crap that isn’t a business requirement.

And I’m publishing those guides online for free.

文章来源: https://fyr.io/2023/06/30/implement-but-never-move/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)