---
title: 【安全圈】APT组织开始大量抄袭红队先进的战术和工具
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066682&idx=3&sn=05ca26f017e4cc04fbaee8e8adfb38d9&chksm=f36e7f3ac419f62cdd2c81a721bff0f46cf903216625c5df718c5aaac5d3a0355ed8e2e680cf&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-19
fetch_date: 2025-10-06T19:39:06.798234
---

# 【安全圈】APT组织开始大量抄袭红队先进的战术和工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgVk9gVxegNKwIpcDhDeEbKFZOewIvkkylibtpzic323XAPPEtOUKLG4CZCqibrJH6fRlmhHicELxkxXQ/0?wx_fmt=jpeg)

# 【安全圈】APT组织开始大量抄袭红队先进的战术和工具

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

近日，安全研究人员调查后发现，臭名昭著的APT组织Earth Koshchei（也被称为APT29或Midnight Blizzard）与一项大规模非法远程桌面协议（RDP）的恶意活动相关。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgVk9gVxegNKwIpcDhDeEbKFKNBSHFGiaiaK8tAcpic4STDa0qrb36znibtO3qjoKMyEhzyfibv7F2fqxg/640?wx_fmt=jpeg&from=appmsg)

Earth Koshchei在此次情报收集与数据窃取行动中创新性地采用了先进的战术及红队工具，充分展现出攻击组织在尝试新型攻击的效率。通过商业VPN服务、TOR及居民代理等匿名化层来掩盖其操作，增强隐蔽性，并使归因工作复杂化。该行动于2024年10月达到峰值，目标包括政府、军事组织、智囊团、学术研究人员及乌克兰实体等。

## 攻击机制

Earth Koshchei的行动采用了多层攻击策略，其核心在于嵌入鱼叉式钓鱼邮件中的恶意RDP配置文件。当用户打开该文件时，就有可能会通过攻击者设置的193个中继之一连接到非法RDP服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgVk9gVxegNKwIpcDhDeEbKW3xh53CfHITDCiaLauHRibzUMOw3QhB3azkObJnibANT9w86wAianYRnTg/640?wx_fmt=jpeg&from=appmsg)建立PRD的方法

其攻击方法被称为“非法RDP”，Black Hills Information Security在2022年对其进行了详尽描述，该方法采用了RDP中继、非法服务器及恶意配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgVk9gVxegNKwIpcDhDeEbKkaJT22VQ1xLVywyQOs6wpk44VJ61CK5yicjhy8rOibics3aj5x6Mbekvg/640?wx_fmt=jpeg&from=appmsg)

RDP连接（来源：VirusTotal）

通过类似Python远程桌面协议中间人（MITM）框架（PyRDP）的工具，攻击者拦截并操纵RDP连接，从而获得对受害者机器的部分控制权限。这允许进行数据窃取、文件浏览，甚至执行恶意应用程序，不再需要像以往一样部署传统恶意软件。

Earth Koshchei的行动规模引起行业关注。在2024年8月至10月期间，该组织注册了200多个域名，其中许多仿冒目标组织的身份，如政府、IT公司及研究机构。其准备工作包括建立34个非法后端RDP服务器，并将其作为其行动的指挥节点。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgVk9gVxegNKwIpcDhDeEbKwj7Q9gmeVldZ4Dp7yRRvtCsnMcC1pn5zHJgx1lqLQjqticnSD45CpDw/640?wx_fmt=jpeg&from=appmsg)

Earth Koshchei如何控制其基础设施的架构图

现阶段，Earth Koshchei的动机似乎主要为情报收集。该组织据称与俄罗斯外国情报局（SVR）有关联，历史上曾针对西方国家的外交、军事、能源、电信及IT部门。其最新行动与此模式相符，受害者包括外交部、军事组织及学术研究人员。

## 红队蓝图变成了攻击者的武器

安全专家强调，Earth Koshchei的非法RDP战术可能借鉴了旨在加强组织防御的红队方法，攻击者有效地将这些技术武器化。例如在一项分析中，RDP配置文件将受害者重定向至假冒的亚马逊网络服务（AWS）的恶意服务器。

他们还利用驱动器重定向及资源共享等功能，以隐蔽方式提取敏感数据。在10月的攻击浪潮中，估计有三家关键组织的数据被窃取，包括两家军事实体及一家云服务提供商。

使用TOR、商业VPN及居民代理等匿名化层使检测和归因具有挑战性。，这些战术使攻击者在利用电子邮件服务器分发钓鱼邮件的同时掩盖其活动。

尽管确定性的归因仍具复杂性，但Trend Micro及其他公司仍将此次行动归因于Earth Koshchei，其原因在于该组织独特的战术、技术及程序（TTPs）。

此次攻击还暴露出另外一个令人不安的现象：合法的安全工具、红队战术方法等被大量用于恶意攻击之中。如何改变这一趋势是行业需要重点关注的方向。

参考来源：https://cybersecuritynews.com/hackers-leverage-red-team-tools-in-rdp-attacks/

***END***

阅读推荐

[【安全圈】苹果HomeKit出现安全漏洞被间谍机构利用 目前具体漏洞细节尚未公布](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066655&idx=1&sn=57e7dca07986a799143fbca48a88cb03&scene=21#wechat_redirect)

[【安全圈】黑客通过虚假品牌赞助攻击YouTube视频创作者](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066655&idx=2&sn=2c8e7da1b030528f5d27851baab4a1d7&scene=21#wechat_redirect)

[【安全圈】比特币 ATM 巨头字节联邦遭黑客攻击，5.8 万用户受到影响](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066655&idx=3&sn=f61b178e1eea3cd68d92ec7bb90b61b0&scene=21#wechat_redirect)

[【安全圈】最新的Windows内核漏洞，可获system权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066655&idx=4&sn=c56864b01e3e298b37ea2863eea40424&scene=21#wechat_redirect)

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