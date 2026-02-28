---
title: 多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险
url: https://mp.weixin.qq.com/s/krIV4MyJUrVUa5Yp8oedQA
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:59:19.807506
---

# 多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fHEm7hZn9HIYkdL0etlT4ceMyiatk9ozgIsEl4slqQHAVpn19RuasPlBvUASMkJsbfcsic03fQJmV6yDguSVw7ia4YefWMJF8Sq3lPClMctSEQ/0?wx_fmt=jpeg)

# 多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险

胡金鱼
胡金鱼

嘶吼专业版

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

最新发现，谷歌应用商店中多款下载量达数百万级的心理健康APP存在安全漏洞，可能导致用户的敏感医疗信息遭到泄露。

安全研究人员在其中一款应用中，发现了超过85个中高危漏洞，攻击者可利用这些漏洞窃取用户的心理咨询数据与隐私信息。

部分涉事应用为AI陪伴类工具，旨在帮助患有临床抑郁症、各类焦虑症、惊恐发作、压力应激及双相情感障碍的人群。在研究人员分析的10款应用中，至少有6款宣称用户对话内容为私密信息，或在服务商服务器上进行安全加密存储。据了解，心理健康数据具有极高的风险价值。在暗网中，心理咨询记录每条售价可达1000美元甚至更高。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/fHEm7hZn9HLOoe2Uib7PpibR4Cib8sqvksyoejjUK0sYkyfvuX5CK6z70cXpkT1zzqmAdtHibZ1lAp9GxvYHOXjyrk0DNQhKT9KtxicribjeQ6hI8/640?wx_fmt=png&from=appmsg)累计发现超1500个安全问题

研究人员对十款宣传可辅助解决各类心理健康问题的移动应用进行了扫描，共发现1575个安全漏洞，其中高危漏洞54个、中危漏洞538个、低危漏洞983个。

尽管发现的所有漏洞都不严重，但大量漏洞可被用于窃取登录凭证、伪造通知、执行HTML注入或获取用户位置。

一款下载量超百万的心理咨询类应用，直接对外部可控字符串使用Intent.parseUri()，并在未校验目标组件的情况下启动生成的意图对象，这使得攻击者可强制应用打开任意内部页面，即便该页面本不应对外开放。

由于这些内部页面通常处理认证令牌与会话数据，漏洞被利用后，攻击者可直接获取用户的心理咨询记录。

另一类问题是应用本地数据存储权限不当，设备上的任意应用均可读取，可能暴露心理咨询详情，包括咨询记录、认知行为疗法（CBT）会话笔记及各类评估评分。

研究人员还发现，部分应用的APK资源中包含明文配置信息，如后端API接口地址与硬编码的Firebase数据库链接。此外，部分存在漏洞的应用使用加密安全性不足的java.util.Random类生成会话令牌或加密密钥。

研究人员表示，十款应用中的大多数均未实现任何Root检测机制。在已获取Root权限（越狱）的设备上，任何拥有高权限的应用均可访问本地存储的全部健康数据。

十款应用中仅有六款未发现高危漏洞，但仍存在中危漏洞，导致整体安全防护水平下降。这些应用收集并存储着移动端最敏感的个人数据，包括心理咨询会话转录文本、情绪日志、用药计划、自伤倾向指标，部分信息还受《健康保险流通与责任法案》（HIPAA）保护。

据统计，研究人员扫描的应用总下载量已超过1470万次，其中仅有四款应用在本月进行过更新，其余应用的最近更新时间停留在2025年11月，甚至2024年9月。而扫描时间为1月22日至23日，检测对象为当时最新版本应用。研究人员目前无法确认相关漏洞是否已被修复。

参考及来源：https://www.bleepingcomputer.com/news/security/android-mental-health-apps-with-147m-installs-filled-with-security-flaws/

![](https://mmbiz.qpic.cn/mmbiz_png/fHEm7hZn9HJWU7um2NwicIO0iajmNd2UN7iaLUqIfwfUCDHmBvx3AXmPDzMlmLM4nDbiaANzxhGyeJpeG3V05s1u0jNGkgIibO4ch9HickX0KoRiaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/fHEm7hZn9HLoib2mpicia6pMqPWyTK57o65T1kFc1rmkSWeU7G1mibPd6NAm78JOibXS6RMb0buZItzZdctYXJ9wjibyYxLoXajFO6g5CXRPvqG50/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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