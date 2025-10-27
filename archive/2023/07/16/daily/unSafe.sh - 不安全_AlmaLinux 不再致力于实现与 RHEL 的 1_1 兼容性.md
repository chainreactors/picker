---
title: AlmaLinux 不再致力于实现与 RHEL 的 1:1 兼容性
url: https://buaq.net/go-172120.html
source: unSafe.sh - 不安全
date: 2023-07-16
fetch_date: 2025-10-04T11:51:03.750460
---

# AlmaLinux 不再致力于实现与 RHEL 的 1:1 兼容性

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

AlmaLinux 不再致力于实现与 RHEL 的 1:1 兼容性

Red Hat 前不久宣布其企业发行版 RHEL（Red Hat Enterprise Linux）相关源码仅通过 CentOS Stream 公开。此举加大了社区发行版如 Alma Li
*2023-7-15 14:28:13
Author: [www.solidot.org(查看原文)](/jump-172120.htm)
阅读量:9
收藏*

---

Red Hat 前不久宣布其企业发行版 RHEL（Red Hat Enterprise Linux）相关源码仅通过 CentOS Stream 公开。此举加大了社区发行版如 Alma Linux 和 Rocky Linux 构建 1:1 兼容性的难度。AlmaLinux OS 基金会董事会主席 Benny Vasquez 通过官方博客宣布该项目放弃了构建与 RHEL 发行版 1:1 兼容性的目标，改为实现 Application Binary Interface (ABI)兼容性，即能在 RHEL 上运行的软件也能在 Alma Linux 上运行。对用户而言，他们在使用过程中将基本不会体验到任何差别。RHEL 兼容应用仍然能在 Alma Linux 上运行，操作系统能继续及时收到安全更新。变化在于，Alma Linux 项目不再坚持于与 Red Hat 的 bug-for-bug 兼容性，意味着 Alma Linux 将接受 Red Hat 发布周期之外的 bug 修正，部分用户可能遭遇到 Red Hat 发行版上没有的 bug，它也将能接受未被上游接受或向下游发布的 bug 修正补丁。

https://almalinux.org/blog/future-of-almalinux/

文章来源: https://www.solidot.org/story?sid=75522
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)