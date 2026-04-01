---
title: 威胁通缉令 · 红桃4丨RDP Client RCE漏洞（新增）
url: https://mp.weixin.qq.com/s/jDqCPbON8fWbhzJYALrQ4w
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:42:38.549303
---

# 威胁通缉令 · 红桃4丨RDP Client RCE漏洞（新增）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHkicic6pFYHhLdhRu2qmhFJKwibc5ZE0k5qhKb95nhrFPvJ33suEiamHHZECMlq3H7s3MYLMzTZP7uRmjn3caVDYiaS2JpSo5h7Tuibzw/0?wx_fmt=jpeg)

# 威胁通缉令 · 红桃4丨RDP Client RCE漏洞（新增）

安天集团

![]()

在小说阅读器中沉浸阅读

点击上方"蓝字"

关注我们吧！

最新版“**[病毒通缉令](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650213873&idx=1&sn=2f0f13475e95b2b6fb82355840c7ac5f&scene=21#wechat_redirect)**”已在[计算机病毒分类命名百科](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650211459&idx=1&sn=3ce636cfadaec1c3790b6aba9e6507c4&scene=21#wechat_redirect)同步更新：https://www.virusview.net/virusWantedOrder

今日推送：RDP Client RCE漏洞，牌面情况：新增

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XBFaicYdOHkicFbqrLK9UQltwyFyUvSqmREwibibCeQlHIyuyMw3DeaXiaXFibLPpYU6gyjhYrJZ4zudkMdnjkwibcIibVbcFcBzhPl1VWoU7kZYcbs/640?wx_fmt=png&from=appmsg)

**病毒名称：RDP Client RCE漏洞**

**CVE编号：CVE-2025-26645**

**发现时间：2025-03**

**检测规则首次添加至AVL SDK反病毒引擎病毒库时间：**2025-03****

**简介：‌该漏洞存在于 Microsoft Windows 远程桌面客户端（mstsc.exe）中，源于客户端在处理 RDP 连接时，未正确验证路径序列，存在相对路径遍历问题。当受害者使用存在漏洞的 RDP 客户端连接到攻击者控制的恶意 RDP 服务器时，攻击者可通过构造特制的路径序列，绕过客户端的访问限制，向客户端系统的任意目录写入恶意文件（如 DLL、脚本等），并触发远程代码执行，无需用户交互。此漏洞影响所有主流 Windows 版本的远程桌面客户端，包括 Windows 10、Windows 11、Windows Server 2016/2019/2022 等。**

[安天智甲终端防御系统](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650204763&idx=2&sn=2aadffecf8243d8e2267b8bc8733f5de&scene=21#wechat_redirect)（IEP）拥有驱动级主防模块，基于**[安天AVL SDK反病毒引擎](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650211782&idx=1&sn=06dcc3c05ffce88f87cd134034aaf559&scene=21#wechat_redirect)**的检测能力和内核与应用层的防御点，可有效阻断该漏洞攻击链和其他类似的攻击活动。

****往期推荐:**

[“威胁通缉令”年度更新！](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650213873&idx=1&sn=2f0f13475e95b2b6fb82355840c7ac5f&scene=21#wechat_redirect)

[安天历年发布的威胁通缉令，今天正式在计算机病毒百科网站上线](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650201561&idx=1&sn=906106d8d6f4b68a5e381b538d4db91a&scene=21#wechat_redirect)

[手机上的恶意代码知识库——计算机病毒百科服务号上线了](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650211459&idx=1&sn=3ce636cfadaec1c3790b6aba9e6507c4&scene=21#wechat_redirect)

#

[计算机病毒分类命名知识百科上线试运行（安天研究院出品）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650201151&idx=1&sn=747cbd37d1ce21890552174fd5ec43f8&scene=21#wechat_redirect)

# [视频揭秘入选“十四五”硬核科技成果的反病毒引擎](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650211806&idx=1&sn=19e0b44bbc5f420a6fa99fd8f4e6afcc&scene=21#wechat_redirect)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/krU5D4C1q6Su8m4epwZC39J9XTv5TOxXtKXld0O7YvcKGpIweyd5y6LHX1FW1QU1RLuE08hwNZmLTdcd4fOUGg/0?wx_fmt=png)

安天集团

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/krU5D4C1q6Su8m4epwZC39J9XTv5TOxXtKXld0O7YvcKGpIweyd5y6LHX1FW1QU1RLuE08hwNZmLTdcd4fOUGg/0?wx_fmt=png)

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