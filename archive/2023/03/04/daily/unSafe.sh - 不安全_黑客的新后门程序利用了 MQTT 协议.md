---
title: 黑客的新后门程序利用了 MQTT 协议
url: https://buaq.net/go-151906.html
source: unSafe.sh - 不安全
date: 2023-03-04
fetch_date: 2025-10-04T08:37:13.388205
---

# 黑客的新后门程序利用了 MQTT 协议

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

黑客的新后门程序利用了 MQTT 协议

安全公司 ESET 报告，黑客组织 Mustang Panda aka TA416 和 Bronze President 部署了一种新的后门程序 MQsTTang。恶意程序主要通过钓鱼邮件
*2023-3-3 23:17:48
Author: [www.solidot.org(查看原文)](/jump-151906.htm)
阅读量:33
收藏*

---

安全公司 ESET 报告，黑客组织 Mustang Panda aka TA416 和 Bronze President 部署了一种新的后门程序 MQsTTang。恶意程序主要通过钓鱼邮件传播，通过一个 GitHub 软件库下载负荷，它会在注册表增加一个启动时运行的注册表项去实现持久存在。为了躲避监测它利用了 MQTT 协议去进行指令通信。MQsTTang 还会检查主机上是否存在调试器或监控工具，如果有发现，它会相应的改变行为。

https://www.welivesecurity.com/2023/03/02/mqsttang-mustang-panda-latest-backdoor-treads-new-ground-qt-mqtt/

文章来源: https://www.solidot.org/story?sid=74296
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)