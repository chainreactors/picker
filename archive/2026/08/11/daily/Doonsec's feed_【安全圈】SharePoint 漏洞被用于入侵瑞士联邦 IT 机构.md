---
title: 【安全圈】SharePoint 漏洞被用于入侵瑞士联邦 IT 机构
url: https://mp.weixin.qq.com/s/vQxfGlaMPaEC1ZqtMmcUKQ
source: Doonsec's feed
date: 2026-08-11
fetch_date: 2026-08-12T03:59:54.571336
---

# 【安全圈】SharePoint 漏洞被用于入侵瑞士联邦 IT 机构

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGpibibT57kPKQGqHeZ9eNOicSnPRibSfcqIF0J2Tsxvt5CzUvREFbYaI8KGpxuKwx1qUfYJmyKaKbqiaRrFiaPDBKhtCnhViaZZ4XJu8/0?wx_fmt=jpeg)

# 【安全圈】SharePoint 漏洞被用于入侵瑞士联邦 IT 机构

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

瑞士联邦信息与通信技术办公室（FOITT）披露，未知攻击者利用微软SharePoint软件中的漏洞，攻破了其本地部署的SharePoint服务器上约**200个用户和技术账户**。

## 🏛️ 谁被攻击了？

FOITT是瑞士联邦政府最大的IT服务提供商，负责管理约**50,000个工作站系统**，与各行政单位共同开发安全、用户友好的IT解决方案，并在其自有的现代数据中心运营超过**1,000个专业应用**。

## ⏰ 事件时间线

* **7月14日**

  ：微软在7月补丁星期二中披露了多个严重的SharePoint漏洞
* **7月28日**

  ：FOITT检测到服务器上的异常访问行为
* **7月28日当天**

  ：FOITT立即屏蔽了SharePoint的外部互联网访问，并开始安装安全补丁
* **7月31日**

  ：确认约200个用户和技术账户的登录凭证已被泄露

FOITT表示："这次网络攻击由先前未知的行为者实施，据推测是利用了SharePoint软件中的这些漏洞。"

## 💥 漏洞有多严重？

其中一个被利用的漏洞编号为**CVE-2026-50522**，CVSS评分高达**9.8分（满分10分）**，可使攻击者通过网络远程执行代码。微软表示该漏洞的利用复杂度较低，攻击者无需深入了解系统即可完成攻击。

> 更关键的是：攻击者窃取了机器密钥（Machine Keys）以维持长期访问权限。机器密钥是IIS用于签署会话令牌的加密密钥，一旦被窃取，攻击者可以伪造看起来合法的请求，即使是已完全打补丁的服务器也会接受这些请求。

## 🔧 当前应对措施

* FOITT已**重置**所有受影响账户的密码
* 正在**重新安装**受影响的SharePoint服务器
* 外部互联网访问在工作完成前保持**屏蔽**状态
* 联邦员工仍可通过替代渠道访问和共享文档
* 国家网络安全中心（NCSC）和微软正在协助调查

FOITT指出，该SharePoint平台并非用于存储机密信息或高度敏感的个人数据。

## ⚠️ 对所有组织的警告

> "CERT-EU强烈建议尽快更新受影响的服务器，轮换任何可能暴露在互联网上的易受攻击资产的凭据，并进行入侵评估以识别潜在受影响的SharePoint实例。鉴于近期影响SharePoint的关键漏洞数量众多，各组织应重新考虑将任何Microsoft SharePoint Server直接暴露在互联网上。"——CERT-EU安全公告

打补丁可以关上大门，但不能换掉锁。SharePoint因其与微软认证系统的深度集成，正日益成为网络犯罪分子和国家级行为者的目标。攻击者可以将其作为入侵更广泛网络的入口点，使SharePoint服务器的直接互联网暴露成为越来越大的安全风险。

从漏洞披露到实际被利用的窗口期是以**天**计算，而非以周计算。对于仍在运行暴露在互联网上的本地SharePoint服务器的组织，正确的做法是：先打7月补丁，再轮换机器密钥，最后重启IIS——这个顺序不能变。

***END***

阅读推荐

[【安全圈】OpenAI紧急暂停！新AI模型竟会自学"黑客技术"](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078224&idx=1&sn=cc5cca1ffdaf71baba9728066f84d777&scene=21#wechat_redirect)

[【安全圈】200万人身份告急！比利时电子身份证曝致命漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078224&idx=2&sn=cdb595c396ed85c7d7cbec78a2e74951&scene=21#wechat_redirect)

[【安全圈】开发者小心！VS Code扩展暗中窃取加密钱包](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078224&idx=3&sn=27ac74789ce072180bb82f5b25e79d15&scene=21#wechat_redirect)

[【安全圈】服装品牌李维斯遭黑客攻击，部分企业数据被窃取](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652078212&idx=1&sn=82c69a11c8cde7ebde9dbae49bcc8da3&scene=21#wechat_redirect)

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