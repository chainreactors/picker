---
title: Beyond good ol’ Run key, Part 142
url: https://buaq.net/go-158747.html
source: unSafe.sh - 不安全
date: 2023-04-16
fetch_date: 2025-10-04T11:31:38.537209
---

# Beyond good ol’ Run key, Part 142

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

Beyond good ol’ Run key, Part 142

April 14, 2023 in Autostart (Persistence)
*2023-4-15 05:47:41
Author: [www.hexacorn.com(查看原文)](/jump-158747.htm)
阅读量:28
收藏*

---

![](https://www.hexacorn.com/blog/wp-content/uploads/2011/10/Adam_Avatar_2_50x50.png)

April 14, 2023 *in [Autostart (Persistence)](https://www.hexacorn.com/blog/category/autostart-persistence/)*

I never heard of OBS (Open Broadcaster Software), until I saw [this](https://twitter.com/irsdl/status/1645764384214450176) Twitter thread.

After [downloading](https://obsproject.com/) it, trying it, tinkering with it… I actually found it far more confusing than [Screen2Gif](https://www.screentogif.com/), but this is because it offers a lot more advanced options, tweaking, and… supports scripting.

A-HA!

The moment I learnt about scripting, I immediately went to OBS’ [Scripting Help section](https://obsproject.com/kb/scripting-guide) and started reading it with an intention of creating a small PoC. My thought process was: if I can write an OBS script that executes program or command of my liking anytime OBS starts, I am totally writing a new blog post in the series…

BUT

I also browsed the OBS Forum posts… and while doing so, I quickly discovered [this OBS script](https://obsproject.com/forum/resources/obs-autostarter.1265/) that implements everything that I wanted to demo in the ‘I will write it when I can PoC it’ post.

Booooo to me actually learning OBS Scripting, Hurrah to you reader.

This script is a beauty. It executes programs of your liking at the time OBS starts, and kills them when OBS exits.

And now I feel terrible, because I have contributed NOTHING to this post other than describing other peoples’ work.

文章来源: https://www.hexacorn.com/blog/2023/04/14/beyond-good-ol-run-key-part-142/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)