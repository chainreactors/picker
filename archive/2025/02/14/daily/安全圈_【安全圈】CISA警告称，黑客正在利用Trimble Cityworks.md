---
title: 【安全圈】CISA警告称，黑客正在利用Trimble Cityworks
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067800&idx=2&sn=11fb69d2e4e67b48bda863f690f2a652&chksm=f36e7b98c419f28e038b01ffc3729b9b70775a43046598f47be4be9b10f61166bce22cd8c668&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-14
fetch_date: 2025-10-06T20:36:30.484647
---

# 【安全圈】CISA警告称，黑客正在利用Trimble Cityworks

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylian7dYBcH4FqP33t54OpgM0mwGk95z6LRyklSoqFuRYQkHuoYyPNAXnBnNnKOlgYICLEVQw0BwHKA/0?wx_fmt=jpeg)

# 【安全圈】CISA警告称，黑客正在利用Trimble Cityworks

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络安全

![Hackers Are Exploiting Trimble Cityworks, CISA Warns](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylian7dYBcH4FqP33t54OpgM0gNjn6MNiaqyiapFicresnRhSaNJ5K2mFia7X45oiaGGRiaMWicN8fL1XrWxDg/640?wx_fmt=jpeg&from=appmsg)

黑客正在利用一个被政府机构广泛使用的基础设施管理系统中的严重漏洞，该漏洞可使攻击者在微软 IIS Web 服务器上执行远程代码。

美国网络安全与基础设施安全局（CISA）命令联邦民用机构在 2 月 28 日前修复天宝（Trimble）公司的 Cityworks 平台中被追踪为 CVE-2025-0994 的严重漏洞。

根据天宝公司的网站介绍，Cityworks 服务器资产管理系统是 “一个以地理信息系统（GIS）为核心的解决方案，供地方政府、公用事业公司、机场和公共工程部门在整个生命周期内管理和维护基础设施”。黑客正在利用这一漏洞，引发了人们对关键服务可能受到干扰的担忧。

总部位于科罗拉多州的天宝公司披露了这一漏洞，并警告用户存在远程代码执行攻击的风险。该漏洞源于一个反序列化漏洞，这使得威胁行为者能够未经授权访问系统并部署恶意负载。

美国网络安全与基础设施安全局将该漏洞列入了其已知被利用漏洞目录，敦促管理员立即安装安全更新，并检查系统是否存在被入侵的迹象。

天宝公司的调查证实，存在未经授权试图入侵特定 Cityworks 部署系统的行为。一些本地安装的系统存在 IIS 身份权限过高以及附件目录配置错误的问题。

此次安全公告突出了多个入侵指标（IOC），包括恶意文件的 SHA256 哈希值、暂存 IP 地址以及 Cobalt Strike（一款渗透测试工具）的命令与控制域名。

攻击者正在使用经过混淆处理的 JavaScript 有效负载和基于 Rust 语言的恶意软件加载器，以便在被攻陷的服务器上保持持久控制。

建议使用 Cityworks 系统的联邦机构和地方政府采取以下措施：

1.分别为 15.x（15.8.9 版本）和 23.x（23.10 版本）应用最新补丁，这两个版本的补丁分别于 1 月 28 日和 29 日发布。

2.检查 IIS 身份权限，确保其不具备域或本地管理员权限。

3.限制附件目录的访问权限，以防止未经授权的修改。

***END***

阅读推荐

[【安全圈】网络攻击扰乱了Lee报纸在美国各地的运营](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067786&idx=1&sn=6b219161a3c6923cd9dffc601b4abff2&scene=21#wechat_redirect)

[【安全圈】OpenSSL 修补了高严重性漏洞 CVE-2024-12797](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067786&idx=2&sn=c497b609a80250b639e05ac4c19e5d69&scene=21#wechat_redirect)

[【安全圈】OmniGPT AI 聊天机器人涉嫌入侵：黑客泄露用户数据和 3400 万条消息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067786&idx=3&sn=2f7e62e02af6dbbc8efc5add1acf93e2&scene=21#wechat_redirect)

[【安全圈】Microsoft补丁积极利用零时缺陷-CVE-2025-21418 & CVE-2025-21391](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067786&idx=4&sn=290289ab17f0f8e7dea5feaad426fb1b&scene=21#wechat_redirect)

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