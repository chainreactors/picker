---
title: 快普M6 GetPositionOfStaff接口存在sql注入漏洞 附POC
url: https://mp.weixin.qq.com/s/Ju3JvUI3f7FQtB4iEgi4NA
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:15:05.414274
---

# 快普M6 GetPositionOfStaff接口存在sql注入漏洞 附POC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6xQBhJ9waI51ib71CibJaKyaez76F5JUhvouvh25BQqdicoh0wWTdEHHib1OvEG8vVrqDKuj7H95qc3Yjvr5QqztrRibXzQ9xBZ8Tg4/0?wx_fmt=jpeg)

# 快普M6 GetPositionOfStaff接口存在sql注入漏洞 附POC

2026-3-18更新
2026-3-18更新

南风漏洞复现文库

![]()

在小说阅读器中沉浸阅读

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. 快普M6 简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

本人只有 南风漏洞复现文库 和 南风网络安全 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。

快普M6

## 2.漏洞描述

快普M6 GetPositionOfStaff接口存在sql注入漏洞

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

快普M6
![快普M6 GetPositionOfStaff接口存在sql注入漏洞](https://mmbiz.qpic.cn/mmbiz_png/b9KQYsB8q6zGjN0vkIQTym8Rtx2RkC15WJ30FicBkZ6axdgiaCUDUGk9vpg3QuFYCv48vcreMIlCriabseibguVAH7TEetSrEU1KWqhdVDYdzfA/640?wx_fmt=png&from=appmsg "null")

快普M6 GetPositionOfStaff接口存在sql注入漏洞

## 4.fofa查询语句

body="Resource/JavaScript/jKPM6.DateTime.js"

## 5.漏洞复现

漏洞链接：http://xx.xx.xx.xx/WebService/StaffService.asmx/GetPositionOfStaff

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xRNqwNXpGX75NYvC20nM3da3iaOFSO7JKWxjRD1SjfCicwghrRzJu5ChicoMKFIbNlKDibT8u29FSuQYzHzW0icxCNtxJQmSsAQVSM/640?wx_fmt=jpeg&from=appmsg "null")

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zg0C3S9Q8zj4ST7LJY579kIHVdXTfXUS838QrDgSLe67FnGXybpABefhW1smyjZkWCzq0pKiaT7gIgRQMXhQhic7UpvG2rIn8vU/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yYzk09TibrejiajDicKJaia0C4C8AAG23lDeQfyXxSbwUOzmGLZ6za0HEuye0iaUxZcyFyZRdgpGzWoicNa5OojktYpOtVBHIF09NcM/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6y5T2IASiaUK1GXoSFjjN98iceS0MqibXcpIibopiaVibf2OO2ty2bEoCPY2pGcAHUZhsf2OaLxiaBuqsRXCrHicYYCGxic9icU4P4Fhh72E/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6xvHxsJNUtUXINPKqjKNzTxiaZOdbficp3drkyuWLvaZcvh4HDeXfgArOibqaOSrzIbNXFo46b9RVNcK38upgib9llpNYFytEBGpog/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yic691GPIEBWVpo4KY9IpJncIqT4fpI8tKyuTe66Rw31IHgEHG5nWeiaJnK4YOia13iaviajNLr4R1nBzx57Cva9JcKTNvy4K0x8bs/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6yuQr8XiakDrtnvk7Dz91dvovTPqQTm6Taialp7btdmfyla1UjV8TNibfYQtKcgn2fhnUQxf3NY2R0eWnf4uE8hKJ1sBcFEIlicIPU/640?wx_fmt=jpeg&from=appmsg "null")

## 7.整改意见

打补丁

## 8.往期回顾

[畅捷通TPlus FormReportOperateAction.aspx接口存在任意文件读取漏洞 附POC](https://mp.weixin.qq.com/s?__biz=MzIxMjEzMDkyMA==&mid=2247490159&idx=1&sn=9c0883fe2d892517c3c24c71df70b937&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HsJDm7fvc3a95GFchUA48sGQuaFpFPPmL593YvcFo4IPeV2QPL2L72h5t4ibNq9IyXI9GmRWmvV2eh8zo3ldtmg/0?wx_fmt=png)

南风漏洞复现文库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HsJDm7fvc3a95GFchUA48sGQuaFpFPPmL593YvcFo4IPeV2QPL2L72h5t4ibNq9IyXI9GmRWmvV2eh8zo3ldtmg/0?wx_fmt=png)

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