---
title: 【安全圈】微软 SharePoint Server 0Day漏洞遭在野利用
url: https://mp.weixin.qq.com/s/I4knZFuMN6uYTJqscwjHfA
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:47:50.936197
---

# 【安全圈】微软 SharePoint Server 0Day漏洞遭在野利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFOEpzO7O70tiakbmB00agN7ib0d5KP4VsOedPveUoCWVJcFCBQthicOSIBUKUsOCHICQcRZp0kUWz1vf7BAZHS2ABIKFWROgpRLs/0?wx_fmt=jpeg)

# 【安全圈】微软 SharePoint Server 0Day漏洞遭在野利用

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHJeUEujjuURZicTqfGrria9yY9tKDsgict1tJt7KGX1Fm6KJJ8C3VwmxhdFImYDQicGQTY9DRDchNWMRRkjzCY2ED9LUicauHpczeU/640?wx_fmt=jpeg&from=appmsg)

微软在2026年4月的月度安全更新中确认，SharePoint Server存在一个关键的0Day欺骗漏洞（CVE-2026-32201）正遭在野利用。该漏洞影响多个SharePoint Server版本，CVSS基础评分为6.5（重要级），考虑到官方补丁已发布，调整后的时序评分降至6.0。

## 漏洞技术细节

该漏洞源于Microsoft Office SharePoint的输入验证缺陷（CWE-20），允许未经认证的远程攻击者通过网络实施欺骗攻击。其攻击向量被归类为网络传播，攻击复杂度低，且无需特权或用户交互，为企业SharePoint部署提供了低门槛的攻击入口。

微软公告指出，成功利用该漏洞可能导致攻击者查看部分敏感信息并篡改公开数据，但不会影响目标资源的可用性。尽管对机密性和完整性的单独影响评级为"低"，但由于无需认证且存在在野利用，实际风险显著提升。

## 在野利用态势

微软安全公告将该漏洞标记为"已检测到利用"，意味着补丁发布前已观测到实际攻击活动。漏洞利用代码成熟度标记为"功能性"，报告可信度确认为"已证实"，这一组合使该漏洞成为企业修补优先级之首。

该漏洞在微软发布补丁前未公开披露，表明威胁行为者可能已将其武器化为真正的0Day漏洞。微软已为所有三个受影响版本发布安全更新：

* SharePoint Server订阅版——KB5002853（Build 16.0.19725.20210）
* SharePoint Server 2019——KB5002854（Build 16.0.10417.20114）
* SharePoint Enterprise Server 2016——KB5002861（Build 16.0.5548.1003）

## 应急响应建议

鉴于漏洞已遭在野利用，企业应将以下更新视为紧急修补：

* 立即为所有受影响SharePoint Server版本安装相应安全更新
* 审计SharePoint Server访问日志，排查异常网络欺骗活动或认证模式
* 在应用补丁前尽可能限制面向外部的SharePoint实例
* 监控威胁情报源，获取与在野利用活动相关的入侵指标（IOCs）
* 确保未部署WAF规则或网络分段等额外防御措施的SharePoint实例不直接暴露于互联网

作为全球部署最广泛的企业协作平台之一，SharePoint Server始终是国家背景黑客和牟利型威胁组织的高价值目标。协作工具中的欺骗漏洞常被用作横向移动、凭证窃取或商业邮件入侵攻击的初始立足点。

微软特别强调，运行本地SharePoint部署（尤其是2016或2019版本）的企业应优先处理此补丁。微软同时感谢了安全社区就该漏洞开展的协同披露工作。

***END***

阅读推荐

[【安全圈】金山毒霸、360 安全卫士被曝存在内核驱动高危漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075647&idx=1&sn=fa2ee897d05ae80591734bbcffa07abd&scene=21#wechat_redirect)

[【安全圈】开源监控平台 Grafana 曝漏洞，黑客可诱导 AI 助手泄露企业数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075647&idx=2&sn=8b9601124f9fd4627498d6920d66e5c9&scene=21#wechat_redirect)

[【安全圈】旅游平台 Booking.com 遭黑客入侵，旅客姓名电话号码等信息外泄](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075647&idx=3&sn=9b8138c91b5833096a9a449b6af37b4c&scene=21#wechat_redirect)

[【安全圈】黑客利用 Claude 和 ChatGPT 入侵多家墨西哥政府机构](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075617&idx=1&sn=ae5ccccf31e54fadb3a3ae3a96442518&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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