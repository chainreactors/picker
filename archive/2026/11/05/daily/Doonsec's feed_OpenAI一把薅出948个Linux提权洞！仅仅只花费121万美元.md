---
title: OpenAI一把薅出948个Linux提权洞！仅仅只花费121万美元
url: https://mp.weixin.qq.com/s/PdpjjDHuhB-U4aLPWcxaow
source: Doonsec's feed
date: 2026-11-05
fetch_date: 2026-11-06T08:39:17.552024
---

# OpenAI一把薅出948个Linux提权洞！仅仅只花费121万美元

# OpenAI一把薅出948个Linux提权洞！仅仅只花费121万美元

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 兄弟们，这波真不是吓人。

## OpenAI刚发报告：

## 用一个还没发布的网络安全模型跑自动化流水线，直接在Linux内核里验证出 **948个本地提权（LPE）漏洞**，普通用户能一路摸到root。

##

而总价，只要 **121.3万美元** API费，摊到每个可用提权利用上约 **1279美元**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicK2oYxkpX4IKooDzCwUXQX8nqhAdDwbVODQl46vtSM8klI58BxyfoKGDUsHR9bOxnknhQ9fQMgZlVhtAbic2ddVTUgTkPK8sQjo/640?wx_fmt=jpeg)

## 一、4000万行代码，被AI压成“提权流水线”

##

以前挖内核洞是手艺活：跟操作系统底层死磕几个月，拼直觉、拼竞态。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKawOPsMpk8KC1tV5tEic2hku8Bg6ia9A5rdtbxQm7QrcBiauQcZiaHBjCp6VphAYvCC5gKEJTsHHkwk4JuwkYps7MGE1B3Lb60RKI/640?wx_fmt=jpeg)

现在OpenAI把活儿拆给一群Agent：

* **Scout**：从4000万行里圈出约280万行高价值代码（~7%）
* **Analyst**：12小时吐出2308个候选
* **Triage**：隔离机里跑PoC，复现1724个，误报仅3.1%
* **ExploitDev**：顶着SMEP/SMAP/KASLR写利用，最终并成948个独立提权洞

7月用旧模型才166个，10月直接翻5倍多。**同一份代码，在更强模型眼里就是筛子。**

## 二、最恐怖的不是数量，是“战术自主性”

##

抽样166个利用，AI自己搓出 **至少10种业内没见过的攻击技法**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicK40VQRESQhIYlW8jKckktuG5XpdluB8JZ8Q4icJ62O6gYo9JzVCs4dickxgibZrI0ky5yqEibsItTTBG4aou5kZfrH3VGXNibh1ptM/640?wx_fmt=jpeg)

还有个名场面：

让Agent打指定漏洞，200个成功提权里，有20个是它嫌原洞难啃，**顺手挖了个新0-day** 把root拿了的。

说白了，它已经不是“按工单干活的工具”，是会自己换路径的对手。

## 三、防守方的账，彻底算不平了

##

攻击侧：

1279美元买一个root利用，黑产看了笑醒。

防守侧：

审计、修补丁、回归测试、灰度发布……一个洞的人力成本能甩出十条街。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicImrfQIU0FJ7LJqRxW0MD82VSia6w2s6jtR9K2YRGGib4OJGIUvNPGqWl8PDIFQ0kTVj4SBFHJ8ReXo97iaL4e2OgmS3ibibnypD8AU/640?wx_fmt=jpeg)

但OpenAI这次没把锤子递给坏人，走的是 **Patch the Planet**：出利用的同时给候选补丁，人工复核后喂给内核社区。扫描10天里，上游已合入61个、43个进暂存、近300个在吵。

结论很直白：

**未来不是“有没有漏洞”，而是“你补得有没有AI挖得快”。**

服务器别拖更新，低权限账户别乱发，容器沙箱给我钉死。Linux都被打成这样，你那堆Vibe Coding产物，真别挂公网。

-- END --

\*本文作者：hacking。文章内容或图片来自网络，经AI优化，如果存有侵权，请留言，第一进行处理。

> 参考：OpenAI《A thousand fewer paths to root》+ 量子位/FreeBuf 转述

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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