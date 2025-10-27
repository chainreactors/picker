---
title: 更换/更新内核导致内存减少的处理办法
url: https://buaq.net/go-154743.html
source: unSafe.sh - 不安全
date: 2023-03-23
fetch_date: 2025-10-04T10:21:03.175191
---

# 更换/更新内核导致内存减少的处理办法

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

更换/更新内核导致内存减少的处理办法

很多时候，我们DD完Linux后，都会更新或是更换BBR内核来达到网络加速的效果。但是在更换完内核后会经常会出现可用内存减少的情况，一般表现为两种：•
*2023-3-22 22:48:24
Author: [blog.upx8.com(查看原文)](/jump-154743.htm)
阅读量:19
收藏*

---

很多时候，我们DD完Linux后，都会更新或是更换BBR内核来达到网络加速的效果。但是在更换完内核后会经常会出现可用内存减少的情况，一般表现为两种：

• 可用内存数值比实际应有内存数值小得多；

对于内存大的也就无所谓了，但是对于本身内存就很小的小鸡而言，无疑是一种“灾难”。遇到这种情况该怎么处理呢？下面直接上教程：

1、编辑grub启动文件，位置在 /etc/default/grub。找到“GRUB\_CMDLINE\_LINUX”项，在后面加上参数“iommu=off”

```
GRUB_CMDLINE_LINUX="iommu=off"
```

2、重新生成grub文件

```
sudo update-grub
```

3、此时你就会发现你的内存数值恢复正常了。如果没有恢复的话，执行重启命令即可

```
reboot
```

4、检查是否生效，如果没有任何反馈输出，即代表已经成功。否则检查前面额步骤

```
dmesg | grep SWIOTLB
```

**原理：**iommu用于支持硬件直通，会启用SWIOTLB，直接让你很大一部分内存被吃掉，对于内存不大的小鸡来说这部分内存的占用完全是一种浪费。

文章来源: https://blog.upx8.com/3328
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)