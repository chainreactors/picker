---
title: macOS木马DigitStealer活动激增，暴露关键基础设施弱点
url: https://mp.weixin.qq.com/s/s6J4ob_Iwufjhl1rHkv6Yw
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:14:13.362024
---

# macOS木马DigitStealer活动激增，暴露关键基础设施弱点

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2WmFoBJWEwgH4jrhqRePWf84QOQraQ2C9lrV1nicd0h24icLVIHdhp80OM7svQLFDrIpzYzfrFW95tKKNxTEibjyh9eXn6Kl3AI4/0?wx_fmt=jpeg)

# macOS木马DigitStealer活动激增，暴露关键基础设施弱点

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3vjrzw3diaXVKfq9d7JYFdoqc4C0BAGZDA1fMZyvDZNh1xlqDLuSibLbu5IqKq4icsHe4yXPb7Bc0xXu70sSLUlWPqP9JLSHmGb8/640?wx_fmt=jpeg&from=appmsg)

近期，针对macOS系统的复杂信息窃取木马DigitStealer活动激增，引发网络安全界高度关注。这款2025年末首次出现的恶意软件专门针对Apple M2设备，与普通威胁有明显区别。

该木马主要通过窃取敏感用户数据实施攻击，包括18种加密货币钱包信息、浏览器数据以及macOS钥匙串条目。与多数现代信息窃取木马不同，DigitStealer不属于恶意软件即服务（MaaS）生态，其缺乏关联方使用的网络面板，表明其可能由私人或小型专属团队运营。

##

**Part01**

## ****感染机制分析****

主要感染途径是通过伪装成合法应用（如生产力工具"DynamicLake"）进行传播。用户安装被篡改的软件后，木马会启动多阶段感染流程：通过创建Launch Agent实现持久化驻留，确保恶意代码自动运行。

这种后门功能使攻击者能维持长期访问，每10秒轮询一次C2服务器，获取新的AppleScript或JavaScript有效载荷以执行不同恶意功能。

Cyber and Ramen分析团队发现，该木马的基础设施缺乏多样性，表明其采用集中化运营模式。调查显示，其命令服务器集中在特定托管网络，通常通过Tucows等提供商注册域名，并使用Njalla的域名服务器。这种操作安全缺陷为研究人员提供了追踪威胁的重要指标。

**Part02**

## ****规避检测与通信策略****

深入分析DigitStealer技术行为发现，其采用复杂机制规避检测与分析：

* 通过四个特定API端点（/api/credentials、/api/grabber、/api/poll和/api/log）与C2服务器通信，处理凭证窃取和文件上传等任务
* 采用加密质询-响应系统阻止安全研究人员探测：服务器发送唯一"质询"字符串和复杂度等级，客户端需通过哈希运算匹配特定模式才能获得有效会话令牌
* 将系统硬件UUID经MD5哈希处理后发送至C2服务器，形成可识别的数字指纹

![DigitStealer C2服务器加密质询请求示例（来源：Cyber and Ramen）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2vWYzft86D2ngXTkp9Fxic1gBvYQ4EkEDxkOXRRSJt2yl0TL2Awicg4oTkRicypIXMX6dh6z8KeTkzibj1GOjiapwv0dtFfIL2nMA0/640?wx_fmt=jpeg&from=appmsg)

这种反分析特性确保自动化扫描工具难以与命令服务器交互，同时为防御者提供了可主动监控分析的识别特征。

**参考来源：**

DigitStealer Gains Attention as macOS-Targeting Infostealer Exposes Key Infrastructure Weaknesses

https://cybersecuritynews.com/digitstealer-gains-attention/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibzefibicmDdQl5gbj0kdRbbL9PLvNj4Fx7nTwB10Y86ibaau2wMNuvs9xibztEUaON1ehhL0XgD8G5iaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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