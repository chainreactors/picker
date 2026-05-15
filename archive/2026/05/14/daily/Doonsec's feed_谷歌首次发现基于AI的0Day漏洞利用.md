---
title: 谷歌首次发现基于AI的0Day漏洞利用
url: https://mp.weixin.qq.com/s/HzDqxxqI24YxLVY-JiQ7Pw
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:50:22.693366
---

# 谷歌首次发现基于AI的0Day漏洞利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0a0uIDgepFFRLF28Emd1iaRu2edp5IfYyPRiaowib6iankrd0wH6n0LcCF9uzib8hO7fB0IOnnhE3qZzJb0bian837vTm2pNzd9wsSs/0?wx_fmt=jpeg)

# 谷歌首次发现基于AI的0Day漏洞利用

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX22NPFQPmnmYRD8yL64ibRFm11aFqF2XvSd4bzVee3iczBnvicu75WuMB8DuRuWpdlJPvYemdWa4U13NSqFGYcw1s1W7vLheZUxDM/640?wx_fmt=png&from=appmsg)

谷歌威胁情报小组（GTIG）近日发布报告，首次确认有网络犯罪分子利用人工智能（AI）独立发现并武器化了一个零日漏洞，并计划用于大规模攻击。

据谷歌的报告，该漏洞存在于一款流行的开源Web管理平台中，是一个双因素认证（2FA）绕过漏洞。犯罪分子疑似使用AI模型完成了漏洞发现和利用代码的开发，并试图将其用于一场大规模入侵行动。

谷歌表示，他们已与受影响的供应商合作，披露并解决了这一安全漏洞。

**Part01**

## ****漏洞细节****

## ****开发者“硬编码”信任埋下隐患****

此次攻击针对的是企业广泛使用的基于网页的系统管理工具。

此类工具用于远程配置和管理服务器、网站及应用程序，涵盖安全设置、员工账户管理及系统数据访问权限等核心功能，一旦被攻击者突破，将对企业信息安全构成严重威胁。

漏洞根源在于开发者在认证流程中硬编码了一个信任例外：系统默认来自内部IP地址的请求无需2FA验证。攻击者可通过伪造HTTP头（如X-Forwarded-For）轻松绕过这一机制。

谷歌指出，这种高层次的逻辑缺陷正是现代AI模型越来越擅长发现的类型：“模糊测试工具和静态分析工具擅长检测数据流崩溃问题，但前沿大语言模型（LLM）却擅长识别这类高层语义缺陷和硬编码的静态异常。”

**Part02**

## ****AI生成代码的“指纹”****

## ****教学式注释与幻觉评分****

谷歌分析师在逆向攻击脚本时，发现了多处典型的AI生成痕迹：

* 教学式文档字符串：代码中包含大量教程性质的注释，人类恶意软件开发人员不会写这种多余内容。
* 虚构的CVSS评分：脚本中出现了一个现实中不存在的CVSS分数，属于典型的AI“幻觉”。
* 教科书式代码结构：严格遵循PEP8规范，包含整洁的帮助菜单和完整的ANSI颜色类，与LLM训练数据风格高度一致。

谷歌在报告中未透露涉事网络犯罪组织的名称、受影响的软件，以及黑客所使用的大型语言模型。并明确表示，该攻击未使用自家的Gemini模型，也大概率不是Anthropic的Claude Mythos。

**Part03**

## ****安全专家警告****

## ****AI漏洞竞赛已经开始****

谷歌威胁情报小组首席分析师John Hultquist直言：“有一种误解认为AI辅助漏洞挖掘还是未来的事，现实是它早已开始。每一个我们能追溯到AI参与的零日漏洞背后，可能还有更多我们没发现的。”

他强调，攻击者正在利用AI提升攻击的速度、规模和复杂程度，包括测试攻击路径、持久化控制、构建更先进的恶意软件等。尽管犯罪团伙的手法目前仍显“笨拙”——本次漏洞利用实现中的一些错误可能干扰了攻击计划——但这种情况不会持续太久。

**Part04**

## ****防御启示：时间窗口已被压缩****

谷歌报告还披露了其他AI恶意软件案例，例如利用Gemini API实现自主操作的Android后门。这些案例共同表明：AI大幅降低了漏洞挖掘与利用的门槛，传统的“补丁后利用”时间窗口已变为负数。防御方必须尽快部署AI对抗AI，才能在这场竞赛中不落下风。

**参考来源：**

Google entdeckt erstmals KI-basierten Zero-Day-Exploit

https://www.csoonline.com/article/4170601/google-entdeckt-erstmals-ki-basierten-zero-day-exploit.html

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2WOichlYJst28QicxZVpXP1ibeVdB4iawibWIFgqV6Ry4LzdhyQbspxEr3NAqQviatF6AoAYMl0qboYWSzKwjM7zPSKtD3ncv5joxpM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337950&idx=1&sn=12d64571335d50c1b93389447dfb8ef1&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ibzbO8hNu1jchaRibLfz5ZHmRibzmT7nmjUqZSAswml2TEozpdNFMZw8N1ShpFef0a2bibN2crXGM5BZhMQjgAbAOY0DN1yjl1Cc/640?wx_fmt=png&from=appmsg)

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