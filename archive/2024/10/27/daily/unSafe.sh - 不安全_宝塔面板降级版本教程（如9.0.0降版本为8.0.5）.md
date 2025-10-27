---
title: 宝塔面板降级版本教程（如9.0.0降版本为8.0.5）
url: https://buaq.net/go-269452.html
source: unSafe.sh - 不安全
date: 2024-10-27
fetch_date: 2025-10-06T18:46:06.130769
---

# 宝塔面板降级版本教程（如9.0.0降版本为8.0.5）

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

宝塔面板降级版本教程（如9.0.0降版本为8.0.5）

发布时间: 2024-10-26（New Article）
*2024-10-26 23:19:0
Author: [www.upx8.com(查看原文)](/jump-269452.htm)
阅读量:7
收藏*

---

发布时间: 2024-10-26（New Article）

宝塔面板的专业版都到9.2.0了，免费版才到9.0.0。如果遇到宝塔的最新版本有BUG，那么如何降级到低版本呢，这篇笔记就来简单说说。

> 宝塔服务器面板，一键全能部署及管理 <https://www.bt.cn/u/d2y84I>

如何降级安装，这里列举从9.0.0版本降级到8.0.5，如果需要其他版本，自己更改版本号即可。脚本如下：

```
cd /root
mkdir bt
cd bt
# 这里以 8.0.5 版本为例，可以自行更改想降级的版本
wget https://download.bt.cn/install/update/LinuxPanel-8.0.5.zip
unzip LinuxPanel-8.0.5.zip
cd panel/
bash update.sh
```

之后强制刷新一下面板即可。

文章来源: https://www.upx8.com/4369
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)