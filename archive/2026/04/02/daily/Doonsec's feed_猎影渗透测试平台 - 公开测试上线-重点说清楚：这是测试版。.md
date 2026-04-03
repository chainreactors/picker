---
title: 猎影渗透测试平台 - 公开测试上线-重点说清楚：这是测试版。
url: https://mp.weixin.qq.com/s/21QaeKdBnFe8U237e3GBag
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:26:56.156965
---

# 猎影渗透测试平台 - 公开测试上线-重点说清楚：这是测试版。

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3oR6eMARh6x7pqLmkjlbCGD3NdfVoxDE6bT28oLlziajibIFyIXuVd40ctlcgNicKjgxg9prFCnZEgXUnOxMoRJwK5ksI8ZYW1h3U4q3IKvQGU/0?wx_fmt=jpeg)

# 猎影渗透测试平台 - 公开测试上线-重点说清楚：这是测试版。

原创

逍遥
逍遥

逍遥子讲安全

![]()

在小说阅读器中沉浸阅读

说出来有点不好意思，这个版本是赶出来的。匆忙上线的。

本来打算再打磨一段时间，但想了想，与其继续藏着掖着，不如直接拉出来让大家伙儿一起玩玩。有什么问题、有什么想法，你们直接说，我看到都会认真回复。

---

## 猎影是什么？

说白了，猎影就是一个**本地网络渗透测试平台**。

干这行很多年年了，一直想给自己弄个顺手的工具。市面上有的太贵，有的太复杂，有的用着用着就出幺蛾子。后来干脆自己写，写着写着就成了现在这套东西。

**目前版本功能：**

* 信息收集：子域名扫描、端口扫描、指纹识别

* ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6yjym4WF7nq6ejDJSbNVicib5LDRbb25iazJc7BlsxKNKP2gUp7f3RicoeACw5Y38M2hxXYWSr1ic7NzQAWRveBEwofianfxyHsETIicQ/640?wx_fmt=png&from=appmsg)
* 漏洞扫描：支持多种漏洞类型的检测
* ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6yEyRicch3gRIE0K0W438rRF63iclT34qzrzic1wzyme1x3GXf6NZZbF0oYsJ8vv6wCupAPqib6udibRSIYfnrOIWYJg1gMiaP8dlEoQ/640?wx_fmt=png&from=appmsg)
* POC库：内置大量常见漏洞payload
* ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6wzibsOvrXiaKfmLywXiaG66sj5Kl3fQgo4iaawUpqvias0LdXicpel9OO5icMmDia8ic5APqRe2qVuOKN9I8Ulavht7Tn1eOaN8C0e9y8M/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zZMoa7L3zwCic37M2WI1JYemA6icyCCvemNK0icYyjXYcicMQHkp8X6BmxQiaYy6rdAdGMA2Cibb9Tg7olKjs5dYUPvQxiboSW1TS908/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6wnCeQq6ZtL8hicV6skSrhzDwuZow8wuOicQ14xTkAb082EKAksNtX25FZkf3ict3afC1nra2RzfRFth17GsKzYUzpsGbXAT1qiaics/640?wx_fmt=png&from=appmsg)
* 教育SRC：高校域名库，方便做教育SRC测试
* ![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6w2iaEPfmhaBY0A6RoW6FgJSYGhazNfBNfkAjTdT9IXEVOVhmyPvxUw95wpl4PxZicm0WEiacFwz5Rf0qvUF3iaSEVVJliaoO5WGQjA/640?wx_fmt=png&from=appmsg)
* AI辅助：集成AI分析能力（需要Ollama）
* ![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zon6SBl3FxlrOBGXJBrp1YW3TgOyVls1fXjSVnrsP9DR0iah2BQS4ib8pzRtuxvkCFJrn6crstc3TicksLYnHUYiaJiarGmoYxrEC4/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6xCctL5mh0BnzyFyj6DWftBZ34xG9oOehbiaeMNcRGl9Pp3bfiaZnPYnOqZKZ9LsLR39MzoKBHyVujaF3eIKciaZZsL8mpibXWSBL4/640?wx_fmt=png&from=appmsg)
* 报告生成：一键导出测试报告
* ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6xTFUYYS1NpnKiaf2RsJrgRiak29Nww1B59B2QkJ70wMUyuTwhOjkm47HUKNbibfZARuUgcrQkvw5J9AVvy7stZ5gHI7Rf1s7yppw/640?wx_fmt=png&from=appmsg)

  **还在做的：** POC市场、插件系统、团队协作、分布式扫描。这几个模块架构搭好了，功能还没全，后面陆续补。

---

## 为什么开源？

百分之百开源，没有任何藏着掖着。

这行当里很多工具要么收费，要么用着用着就变味了。我不想搞那一套，做安全的人心里都清楚，有些东西藏不得。

代码就在那儿，想看就看，想改就改，想骂就骂。

---

## 现在是公开测试版

**重点说清楚：这是测试版。**

可能遇到的问题：

* 某些功能还不完善
* 可能会遇到各种奇怪的bug
* 界面可能不够好看

但核心功能都能用，扫描、检测、保存结果这些都没问题。

---

## 你们的意见很重要

上线这几天已经收到不少反馈了，有人说UI要改，有人说功能不够，有人发现了bug。

这些我都在看，也在逐个处理。

**后面会定期更新**，你们提的需求、报的bug，只要合理都会安排。不用客气，有什么就说什么。

---

## 想参与测试？

项目地址：https://github.com/xyz-1008/lieying-PublicTestVersion

部署很简单：

1. 下载deploy包
2. 双击启动脚本
3. 浏览器打开就能用

有问题去GitHub提issue，想讨论的去Discussion，想骂的也可以（别太过分就行）。

---

## 最后说几句

做了蛮多年渗透测试，见过太多工具来了又走。这个猎影，我会一直维护下去。

你们的使用和反馈，就是我最大的动力。

有问题随时找我，一起把这个东西做好。

**2026年4月**

专注定制化网络安全以及APP AI工具 小程序 网站 开发 软件系统开发

*PS：觉得有用给个Star，觉得哪里不好提Issue。别客气。*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/sSbvsVNNPos9u6VtI7fxYJUs3bMpfO3mwZxhHdKnmpEKSZKneOA9RkneBJcX9R49XVudcKL3donkHb0uibichPjw/0?wx_fmt=png)

逍遥子讲安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/sSbvsVNNPos9u6VtI7fxYJUs3bMpfO3mwZxhHdKnmpEKSZKneOA9RkneBJcX9R49XVudcKL3donkHb0uibichPjw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过