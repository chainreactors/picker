---
title: bsptab — tabs in bspwm with tabbed! | Herbort
url: https://buaq.net/go-135318.html
source: unSafe.sh - 不安全
date: 2022-11-13
fetch_date: 2025-10-03T22:36:14.328169
---

# bsptab — tabs in bspwm with tabbed! | Herbort

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

![](https://8aqnet.cdn.bcebos.com/02128bc4968ffe033d3393f93bd357e4.jpg)

bsptab — tabs in bspwm with tabbed! | Herbort

Today, I’m going to show you a project I’ve been working on the last days.It is now more than two ye
*2022-11-12 14:54:49
Author: [herbort.me(查看原文)](/jump-135318.htm)
阅读量:17
收藏*

---

Today, I’m going to show you a project I’ve been working on the last days.

[![albertored11/bsptab - GitHub](https://gh-card.dev/repos/albertored11/bsptab.svg?fullname=)](https://github.com/albertored11/bsptab)

It is now more than two years that I came back to Linux. I tried Manjaro first, then moved to Arch. And at first I used KDE Plasma as my desktop environment, but I’ve always been curious about using a standalone tiling window manager, so a few months ago I took that step and tried bspwm and i3.

Now, bspwm has become my favorite WM. I really like its architecture (binary space partitioning-based algorithm, dedicated socket…), its simplicity (it’s just a WM, nothing else), its scriptability (bspc provides a lot of useful commands, and the subscribe command is really helpful)…

However, there is a feature that I liked from i3 that is missing in bspwm: tabbed layouts, which is a really useful feature for many workflows.

A few months ago I knew about [tabbed](https://tools.suckless.org/tabbed/), a tool from [suckless](https://suckless.org/) to create tabbed containers in X environments, and saw [this script](https://github.com/Bachhofer/tabc) which helps to integrate it into any WM.

Now, since lately I’ve been interested in bash scripting, I decided to rewrite that script and add more features and workarounds to bugs, and the result is quite usable!

## Features

* Adds tabbed layouts to bspwm.
* Each tabbed container handles multiple windows, but not any more tabbed containers.
* Automatically attach new windows to tabbed containers.

## bsptab in action!

* `tabc create` command

![tabc create command](https://raw.githubusercontent.com/albertored11/albertored11.github.io/main/assets/img/bsptab-demos/bsptab-create.gif)

Open a Chromium window, create a tabbed container using a keyboard shortcut and open new windows as tabs.

* `tabc attach` command

![tabc attach command](https://raw.githubusercontent.com/albertored11/albertored11.github.io/main/assets/img/bsptab-demos/bsptab-attach.gif)

Attach window (right) to a tabbed container (left) using a keyboard shortcut.

* `tabc detach` command

![tabc detach command](https://raw.githubusercontent.com/albertored11/albertored11.github.io/main/assets/img/bsptab-demos/bsptab-detach.gif)

Detach a couple of windows from a tabbed container and then combine them to create a new container(again, using keyboard shortcuts).

* `tabc autoattach` command

![tabc autoattach command](https://raw.githubusercontent.com/albertored11/albertored11.github.io/main/assets/img/bsptab-demos/bsptab-autoattach.gif)

Toggle autoattach function using a keyboard shortcut: first, it is enabled, so new windows appear as tabs; then, it is disabled, so new windows are placed as usual.

* `tabbed-auto` script

![tabbed-auto script](https://raw.githubusercontent.com/albertored11/albertored11.github.io/main/assets/img/bsptab-demos/bsptab-tabbed-auto.gif)

Open an instance of pcmanfm-qt, and a tabbed container is automatically created, so every new window opened is added as a tab.

## Find out more

I hope you like my project! :)

If you find it interesting, feel free to try it and please report any bugs you find, and let me know about any new features you’d like to see.

Also, I am not a bash expert at all, so if you think any part of the code should be rewritten in a better way, let me know as well!

I created [a post](https://www.reddit.com/r/bspwm/comments/pfajrd/bsptab_tabs_in_bspwm_with_tabbed/) in the [r/bspwm](https://www.reddit.com/r/bspwm/) subreddit, so, if you prefer, leave a comment there.

文章来源: https://herbort.me/posts/bsptab-tabs-in-bspwm-with-tabbed/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)