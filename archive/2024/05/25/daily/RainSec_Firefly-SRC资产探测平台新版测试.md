---
title: Firefly-SRC资产探测平台新版测试
url: https://mp.weixin.qq.com/s?__biz=Mzg3NzczOTA3OQ==&mid=2247486045&idx=1&sn=4bb6e0bd1018da76af746fbb64755321&chksm=cf1f2775f868ae63529f28cc34214fc1e8b892c73af2ecb0aad0352ef352908dacd275d36826&scene=58&subscene=0#rd
source: RainSec
date: 2024-05-25
fetch_date: 2025-10-06T17:18:27.818491
---

# Firefly-SRC资产探测平台新版测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0z2k3m16wCNKhcORwBFia9px7nqzXuU098aR3d0mUS9WrGSVNObW4xGNMqIXsQibic6Kia7abTekynrsjjcC4qSlfQ/0?wx_fmt=jpeg)

# Firefly-SRC资产探测平台新版测试

RainSec

编者荐语：

新版测试 师傅们快来试试吧

以下文章来源于安全小工坊
，作者Young

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5uT8aDPr3cJ9q0MXAtJORHTMIEvoyicXOsLC7vuLWULFg/0)

**安全小工坊**
.

网络安全，渗透测试，自动化，web安全，白帽子

![](https://mmbiz.qpic.cn/mmbiz_png/0z2k3m16wCNeoEWtPaH5iasHtQKaTCZiaibRkF6HysMXloO7FNwLJVrYsO87BQqOghUK4WumUfWibmKOOwtYFYCyeg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

先回复下师傅们的问题，虽然前端没什么变化，但平台一直在更新，由于精力问题，日常主要是更新及优化后端的任务调度及各个节点的功能。

之后为了解决师傅们反馈的问题及原平台的一些缺陷，整体架构又花了很长一段时间重新调整，导致新旧数据不再互通，现新版各项功能基本完成，先给出新版的地址给各位师傅体验，旧版正常使用，等后续新版稳定后将停止旧版的维护，只保留新版平台。

## 新版地址

```
https://firefly-src.geekyoung.com/
```

## 主要更新

1. 新平台主要以公司主体进行收集，资产归属将更加明确。
2. 开放搜索和添加公司，师傅们可以标记其SRC归属。
3. 开放支持非SRC目标收集，平台空闲时间可进行探测。
4. 小程序，APP等资产可以稳定更新。
5. 提供更多的资产收集及搜索维度， 后续会开放推送功能等。

## 简单说明

* 测试版目前依旧使用原平台的认证方式，首页各功能暂不可用。
* 师傅们可正常体验新版的其他功能，新版正式使用后会把旧版用户数据同步过来。
* 新版的接口等会有部分调整，界面功能基本保持原有风格，详细文档等正式使用后再更新。

本次主要简单展示下师傅们如何添加平台未收录的公司：

功能入口：实验功能--企业查询

输入企业关键字可以查询相关企业信息，对于属于该src但是未被收录的企业，师傅们可以自行添加及标记，在后台通过后平台会自动化收集其相关资产。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0z2k3m16wCNKhcORwBFia9px7nqzXuU09PW4E5S6OmrcTnPxLfteFRa1tQpasuiajSMhYfoUrNAk22LTLTMK656A/640?wx_fmt=png&from=appmsg)

点击添加后选择对应的src，下拉框src较多，支持搜索src名称。

添加时请师傅们正确选择对应的src，后台审核过后才会开始收集。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0z2k3m16wCNKhcORwBFia9px7nqzXuU09AFR98l0EtU8o6Y1oFXCk03eT8UsnuQ8Z2xcuCYYuevwiaxBTo8UmUDA/640?wx_fmt=png&from=appmsg)

不少师傅对非赏金目标也有兴趣，所以平台现也可提供非赏金目标的收集。

师傅们如果有这方面需求，可以将目标SRC标记为`公益`，通过审核后平台会在`空闲时间`进行公益类的探测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0z2k3m16wCNKhcORwBFia9px7nqzXuU09k1NJYByF6Zgcof4A3gLuCOGD1AQCsQIrnEvILVlnC8X8UibKwI1gTcQ/640?wx_fmt=png&from=appmsg)

如果有需要实时的周期监控的可另外私聊。

## 附原平台使用方式

[Firefly-SRC使用手册](http://mp.weixin.qq.com/s?__biz=MzU5MTE4Mzk0NQ==&mid=2247484408&idx=2&sn=7019b6d6575fb1d5fad3029b8e68c18e&chksm=fe33aadec94423c8adca327a884580787832713db072b708e905348fd8251c8222ba2f8ac273&scene=21#wechat_redirect)

如有问题可以通过公众号菜单添加微信反馈

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkY86urnibFC82ElAnl936OYpgurccPJLeWWfS9jjC6aNOyHhbicBKkNw8O8dpyR5boygH1pzBVDakaQ/0?wx_fmt=png)

RainSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LxlshmzkAkY86urnibFC82ElAnl936OYpgurccPJLeWWfS9jjC6aNOyHhbicBKkNw8O8dpyR5boygH1pzBVDakaQ/0?wx_fmt=png)

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