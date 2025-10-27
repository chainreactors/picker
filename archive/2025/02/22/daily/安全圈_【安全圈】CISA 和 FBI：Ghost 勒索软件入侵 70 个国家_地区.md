---
title: 【安全圈】CISA 和 FBI：Ghost 勒索软件入侵 70 个国家/地区
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067926&idx=2&sn=0bc4542c5c841ae852d1fa22d333b2dd&chksm=f36e7416c419fd0027ea0734cd634c163f2d1a630eeaeeac0ca5e6e3832b96b6576a14daf720&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-22
fetch_date: 2025-10-06T20:37:32.199233
---

# 【安全圈】CISA 和 FBI：Ghost 勒索软件入侵 70 个国家/地区

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgoGN68urjja0Qn4If7Y9vCc7ujUo6nrSgR2NKmhgdu8ia21Cy9CsetPTk6JWtmibN2oJ1yy1dvf9Tg/0?wx_fmt=jpeg)

# 【安全圈】CISA 和 FBI：Ghost 勒索软件入侵 70 个国家/地区

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

勒索软件

![鬼](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgoGN68urjja0Qn4If7Y9vCHKXac7BCgeyapcSDKK3mdCZn5pJW0NPYibKONZxuNO62yibEVjsT23Pw/640?wx_fmt=jpeg&from=appmsg)

CISA 和 FBI 表示，部署 Ghost 勒索软件的攻击者已经攻击了 70 多个国家多个行业的受害者，其中包括关键基础设施组织。

受影响的其他行业包括医疗保健、政府、教育、科技、制造业以及众多中小型企业。

CISA、FBI 和多州信息共享与分析中心 (MS-ISAC) 在周三发布的联合公告中表示： “从 2021 年初开始，Ghost 攻击者开始攻击那些面向互联网的服务运行着过时版本软件和固件的受害者。”

“这种不加区分地针对存在漏洞的网络的攻击已经导致超过 70 个国家的组织受到攻击，其中包括中国的组织。”

Ghost 勒索软件运营商频繁轮换其恶意软件可执行文件、更改加密文件的文件扩展名、更改其勒索通知的内容，并使用多个电子邮件地址进行勒索通信，这经常导致该团体的归属随着时间的推移而波动。

与该组织有关的名称包括 Ghost、Cring、Crypt3r、Phantom、Strike、Hello、Wickrme、HsHarada 和 Rapture，其攻击中使用的勒索软件样本包括 Cring.exe、Ghost.exe、ElysiumO.exe 和 Locker.exe。

这个勒索软件组织以牟利为目的，利用可公开访问的代码来利用易受攻击的服务器中的安全漏洞。他们的目标是 Fortinet（CVE-2018-13379）、ColdFusion（CVE-2010-2861、CVE-2009-3960）和 Exchange（CVE-2021-34473、CVE-2021-34523、CVE-2021-31207）中未修补的漏洞。

为了防御Ghost勒索病毒攻击，建议网络防御者采取以下措施：

1. 定期进行异地系统备份，这些备份无法被勒索软件加密，
2. 尽快修补操作系统、软件和固件漏洞，
3. 重点关注 Ghost 勒索软件针对的安全漏洞（例如 CVE-2018-13379、CVE-2010-2861、CVE-2009-3960、CVE-2021-34473、CVE-2021-34523、CVE-2021-31207），
4. 隔离网络以限制受感染设备的横向移动，
5. 对所有特权帐户和电子邮件服务帐户强制实施防网络钓鱼的多因素身份验证 (MFA)。

在 2021 年初Amigo\_A和Swisscom 的 CSIRT 团队首次发现 Ghost 勒索软件后，其操作员就开始投放定制的 Mimikatz 样本，然后投放 CobaltStrike 信标，并使用合法的 Windows CertUtil 证书管理器部署勒索软件负载以绕过安全软件。

除了在 Ghost 勒索软件攻击中被利用进行初始访问之外，扫描易受攻击的 Fortinet SSL VPN 设备的国家支持的黑客组织还将 CVE-2018-13379 漏洞作为攻击目标。

攻击者还利用同样的安全漏洞来攻击可通过互联网访问的美国选举支持系统。

Fortinet 于2019 年 8 月、2020 年 7 月、2020 年 11 月以及2021 年 4 月多次警告客户修补其 SSL VPN 设备以防范 CVE-2018-13379 漏洞。

CISA、FBI 和 MS-ISAC 今天发布的联合咨询还包括与 FBI 最近在 2025 年 1 月调查期间发现的先前 Ghost 勒索软件活动相关的妥协指标 (IOC)、策略、技术和程序 (TTP) 以及检测方法。

来源：https://www.bleepingcomputer.com/news/security/cisa-and-fbi-ghost-ransomware-breached-orgs-in-70-countries/

***END***

阅读推荐

[【安全圈】国家网信办依法集中查处一批侵害个人信息权益的违法违规App](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067911&idx=1&sn=7e609708df11dd4fd5db116fdd3991fb&scene=21#wechat_redirect)

[【安全圈】与俄罗斯有关的威胁行为者利用 Signal 的“链接设备”功能劫持账户](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067911&idx=2&sn=2bff61f8a1dd9ad950eef1a27e02540e&scene=21#wechat_redirect)

[【安全圈】Sophos 斥资 8.59 亿美元成功收购 Secureworks](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067911&idx=3&sn=6a03d738e3a7cb11f91482d431d77f9e&scene=21#wechat_redirect)

[【安全圈】Windows磁盘清理工具漏洞被利用获取系统权限，PoC已公开（CVE-2025-21420）](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067911&idx=4&sn=dc16ae2f429d6a98d49cbc1c5cc21999&scene=21#wechat_redirect)

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