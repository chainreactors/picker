---
title: 安全警报 | 预警！黑客组织发布广东政务服务网漏洞工具，个人信息面临泄露风险
url: https://mp.weixin.qq.com/s/n8ydL_-lP8WzealSy3L2kw
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:54:56.958675
---

# 安全警报 | 预警！黑客组织发布广东政务服务网漏洞工具，个人信息面临泄露风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/m7SEcCOKaqb3b4vgwFhQAXibQBwuzdYGGJ5vibzRNEmNRkgS3lymz6Mlc40X2uShLvdFRfuUDeWVG6pYYdCZIEYHDb1wjVcWFR4v45jxticbEQ/0?wx_fmt=jpeg)

# 安全警报 | 预警！黑客组织发布广东政务服务网漏洞工具，个人信息面临泄露风险

原创

懒虫零信噪
懒虫零信噪

懒虫零信噪

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、事件概述

懒虫零信噪威胁情报中心5月1日监测到，某黑客组织在电报群中公开了一款针对广东省政府服务平台（gdzwfw.gov.cn）的私有身份查询漏洞利用工具。声称该工具利用平台某应用接口的访问控制失效漏洞，可无需验证码、无速率限制地通过姓名+身份证号查询注册手机号及身份确认信息，直接威胁广东地区数千万用户的个人信息安全。

![](https://mmbiz.qpic.cn/mmbiz_png/m7SEcCOKaqZ2YG0ibibffUlexp2L75LbPgbibfxbzUoJhOYRFFicqdicWIRoX3GYHNic7VBcCPiavyaUj7MIRB0e5iarKlZico9IBucTjzvVkHy0ScjM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/m7SEcCOKaqZSzm09ZFEhKTpnyTtMFWraQUGU4XoTiafjJmLSSTbOATiaRCoRsUP6QPkzPRqMZhgFcPrv44NtGgXFPq3vFSKIwwfVynkfOuRuA/640?wx_fmt=png&from=appmsg)

二、事件细节

根据黑客发布的工具说明，此次漏洞的核心问题在于广东在线政务服务某个应用接口存在访问控制失效与身份信息枚举漏洞，具体特征如下：

攻击方式：通过伪造信息，绕过常规身份验证流程；

输入条件：仅需提供目标的姓名+中国身份证号码；

输出结果：可直接获取该身份证对应的注册手机号及身份确认状态；

漏洞优势：无速率限制、无需会话Cookie、无需验证码，可批量自动化查询。

这意味着，攻击者只需掌握个人的姓名和身份证号（如通过社交工程、数据泄露等途径获取），即可轻松查询到其在广东政务服务网的注册手机号，进而可能实施精准诈骗、账号盗用等恶意行为。

三、紧急应对

针对此次漏洞风险，我们建议：

立即核查漏洞：请平台方技术团队紧急排查相关接口的访问控制策略，修复身份验证逻辑，增加速率限制与验证码机制，阻断自动化工具的批量查询。

加强API安全：对平台所有对外API接口进行安全审计，确保敏感信息接口具备严格的权限控制、数据加密与异常访问监控，防止类似漏洞再次发生。

用户通知与防护：若确认漏洞影响范围，需及时通知用户修改密码、绑定手机号，并提醒用户警惕陌生来电与短信，避免信息泄露后遭遇诈骗。

免责声明：本文基于暗网监测信息整理，所涉攻击声明及数据细节均源自黑客单方面宣称，尚未获官方证实；内容仅作安全预警参考，不构成事实认定，请以权威通报为准。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vMByMwrmicRJuiblD41h1JXI8fg8OIgE0Doz0GqFMeoGxmZI0q4XfxFmM3YM25Q3mrKy7Up92YOL1XpEI3S3xFgg/0?wx_fmt=png)

懒虫零信噪

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vMByMwrmicRJuiblD41h1JXI8fg8OIgE0Doz0GqFMeoGxmZI0q4XfxFmM3YM25Q3mrKy7Up92YOL1XpEI3S3xFgg/0?wx_fmt=png)

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