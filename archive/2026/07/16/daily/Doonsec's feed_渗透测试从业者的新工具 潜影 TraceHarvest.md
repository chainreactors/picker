---
title: 渗透测试从业者的新工具 潜影 TraceHarvest
url: https://mp.weixin.qq.com/s/wRyYs_Mtn22GfKHEQtzexg
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:58:14.720456
---

# 渗透测试从业者的新工具 潜影 TraceHarvest

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/yJLbez93fl8R1uInEViaUB4C0alcM4lib707mb7bYdfgDO9LY5ic0KgPetjDmqxoU9MkMMtozpew0cAPmy8PpMeu5Kx97OqNX4QUyro0n0pRicU/0?wx_fmt=jpeg)

# 渗透测试从业者的新工具 潜影 TraceHarvest

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导语：** 你好，我是网络安全老宋。安全攻防干货准时送达！

你做一次攻防演练的信息收集，靠人工要翻一天；潜影把它压到一杯咖啡的时间。攻防演练自动化信息收集，Windows 双击即跑。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flicDVib7ctNSEeiafIOyTn7elxu1xMicgXkvLBkZrjgc68icQOGqSQozelQ9XDmY3blDiaWnK7iaiasogY3bicwFicBashBWMibdXMonicQQLo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flicKVbYPWEWVCB6bLP7gRfZyoNoCuI1lpTt5DpSD77pKncaPaI11bPN6wKYASG0UUFyU0j8NTZSlGIZepTDeWeZ3LOiamhG4CRdM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fliccUswdqkiaWBib2d66gVHBWicjm3bwna5Q4scC8sJIA9qzaz8lZtiaQ3uuZm2WmMNMM7002ibNPaJ5fzyxkYAPxW74ebTYd4OoibPgk/640?wx_fmt=png&from=appmsg)

00

## 为什么人工收集又慢又漏

上周有个做红队的兄弟跟我吐槽，说他们队进场前的信息收集阶段，三个人对着电脑搜了整整两天，百度、Bing、微信来回切，关键词还漏了一半，最后交上去的侦察报告被裁判说"攻击面不全"。说实话，这事儿太常见了，人工搜敏感信息就是个又慢又漏的苦力活。

**潜影（TraceHarvest）**就是冲着这个痛点来的。它是个 Windows 上的 GUI 工具，专做攻防演练场景的自动化信息收集，从自动检索到敏感信息识别到报告导出一条龙跑完。作者 i-am-xjizhi，今年 5 月还在更新，是个新鲜出炉的项目，GitHub 上已经能看到完整的界面和说明。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flibx60ohOnJnfBianIe7JEqzukoxdfclXWJaSdzBadQ4arMlwIWzfkJoqib5qcFdVK9icUKXwiaPEV3RcSyFkcA7nJNb424Y9rf6e2M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flibylmcyz4uweE4xomEThibWsWuHICGKkicOdFeuBm7dtoaYBZBub1ibNxRjalSgVOxBUH6N191cJ54B1CIebMf7ib1DIDMAHQFHRU8/640?wx_fmt=png&from=appmsg)

01

## 潜影的四大核心能力

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flicCmIEWwVzzbT1jibRszicHgUTib9RerCM8GwHoedNhlJlj4JNRUkGqzzArr0MSnvzNx7TkbGGe5HOwlAtV0sU174UqibrGV2kicVNQ/640?wx_fmt=png&from=appmsg)

02

## 怎么跑起来（环境 + 用法）

运行环境

Windows 10 / 11（64 位）。无需安装 Python、Node、Java 任何依赖，下载 exe，解压，双击，完事——对不写代码的安全从业者最友好的一点就在这。

⏺ 项目地址 · GitHub

```
https://github.com/i-am-xjizhi/TraceHarvest/# 下载 Release 里的 exe，解压后双击运行# 主词 / 副词填好，设好采集深度与请求间隔即可开跑
```

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flibzGyAgKZG0Vw3pTh8kIfibibXdN46z4LeRG7bv5TaCUO7icwhjjAwNcOoDcNm6wM4P5wxPqgVJ5okpN4YoOlmmwv13ZCf4CjVVtI/640?wx_fmt=png&from=appmsg)

03

## 边界与合规提醒

这是 Windows-only 的工具，macOS 和 Linux 用户用不了。红队如果有跨平台需求，得另想办法，或者准备一台 Windows 跳板机专门跑它。

⚠️ 它只能用于授权范围内的攻防演练和企业自查。拿去扫未授权目标，违法——作者和发布方都明确写了免责声明，风险你自己担。看到这，如果你身边还有兄弟在用手动搜敏感信息，转给他，省下的时间够他多睡两晚。

// 老宋说：这工具的本质，是把攻防演练里最枯燥、最容易出错的信息收集环节，从"人力苦力"变成"算力流水线"。它不是新发明，但这种一体化 GUI 的体验，比一堆脚本拼起来顺手太多。行业里这类工具不少，但大多要配环境、要懂命令行，潜影把门槛砍到"双击就能跑"，对不写代码的安全从业者是个实在的友好。如果你最近有演练任务，现在就去 GitHub 把它下下来，先用自己公司名跑一遍做自查，既能验工具又能顺手看看自家敏感信息有没有漏在外面。

---

### 往期精彩

[运维的内网DNS进阶：Split Horizon 配置指南](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247486737&idx=1&sn=16b7072c71aec9e71b22dc8f41519a75&scene=21#wechat_redirect)

[渗透测试从业者的全能工具箱：76,700+ Star、185+工具一键到位（HackingTool 从零到实战）](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247486737&idx=1&sn=16b7072c71aec9e71b22dc8f41519a75&scene=21#wechat_redirect)

[甲方运维应急响应的日志分析利器：Klogg 大文件秒开，朴实可靠](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247486706&idx=1&sn=5d012122194fb80d041c59f83bbdbf8a&scene=21#wechat_redirect)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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