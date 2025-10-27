---
title: 【安全圈】微软SharePoint RCE漏洞，安装火绒杀毒后导致安全防护崩溃
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065731&idx=2&sn=ec1234ec73aa6227c6092ac7f59a2a1d&chksm=f36e6383c419ea95b652d8e0d3e28f413e419b31f88142e6e6631f248ff8921ae09270e90b14&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-06
fetch_date: 2025-10-06T19:19:51.089211
---

# 【安全圈】微软SharePoint RCE漏洞，安装火绒杀毒后导致安全防护崩溃

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhwuPJNeqicbczHxTHJ7Ok9aVJAlphqQyrNccV46FLOmtm05lHI9rzRx2nu6X8QicOuibLVP13iamIO7Q/0?wx_fmt=jpeg)

# 【安全圈】微软SharePoint RCE漏洞，安装火绒杀毒后导致安全防护崩溃

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

据媒体报道，微软SharePoint存在远程代码执行（RCE）漏洞，漏洞编号CVE-2024-38094（CVSS评分：7.2） ，并且正在被黑客利用，以此获取对企业系统的初始访问权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhwuPJNeqicbczHxTHJ7Ok9aJAHs0YNbCUmTeErCjbbAr4Twpqvx43h9EZ6VqsgRJttib98gd74vhZA/640?wx_fmt=jpeg&from=appmsg)

微软SharePoint是一个流行的协作平台，与微软365无缝集成 ，允许企业创建网站、管理文档、促进团队协作，并提供一系列工具来自动化业务流程，提供了细粒度的控制和恢复功能，确保数据的安全性。企业可以通过定期备份来防止数据丢失，并确保在发生硬件故障或其他意外事件时能够迅速恢复数据。

2024年7月9日，微软星期二补丁月已发布该漏洞修复措施，并将其标记为“重要”。10月底，CISA将CVE-2024-38094添加到已知被利用漏洞目录中，但没有分享该漏洞在攻击中是如何被利用的。

近日，安全公司Rapid7发布了一份安全报告，阐明了攻击者是如何利用SharePoint漏洞入侵企业，并获得系统访问权限。Rapid7表示，已确定初始访问向量是对本地SharePoint服务器中漏洞CVE 2024-38094的利用。

起初，攻击者利用CVE-2024-38094漏洞公开披露的PoC获得了对服务器的访问权限，并植入webshell。随后，该攻击者入侵了一个具有域管理员权限的微软Exchange服务账户，以此获得更高级别的访问权限。

接下来，攻击者在目标系统中安装了未授权的杀毒软件（例如火绒，海外未被系统环境信任）。有意思的地方来了，由于该杀毒软件并没有被系统信任，导致与微软安全防护体系造成冲突，最终结果是微软防护体系会因此崩溃。此时攻击者可以安装Impacket（红队人员内网横向使用频率最多的工具之一 ）进行横向移动。

此类攻击方式是利用未授权的杀毒软件和安全防护体系之间的冲突，从而导致资源分配和驱动程序加载无法顺利进行，最终实现安全防护效果被削弱，甚至是崩溃，让攻击者可以从容进行后续攻击行为（例如横向移动）。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhwuPJNeqicbczHxTHJ7Ok9aq24Od2zsF5uOfsibicjScyl6NiadalymYZYovrXTn2icw6fZPIh6dbicsRQ/640?wx_fmt=jpeg&from=appmsg)

攻击时间线（来源：Rapid7）

在接下来的阶段，攻击者使用Mimikatz进行凭证收集，FRP进行远程访问，并设置计划任务以实现持久性。为了避免检测，他们禁用了Windows Defender，更改了事件日志，并操纵了被妥协系统上的系统日志记录。

其他工具如everything.exe、Certify.exe和kerbrute被用于网络扫描、ADFS证书生成和暴力破解Active Directory票据。尽管试图擦除备份在勒索软件攻击中很典型，但Rapid7并未发现数据被加码的迹象，因此不能去确定是勒索攻击。

随着类似攻击行为的出现，微软建议未更新SharePoint的用户尽快完成漏洞修复，以免造成更加严重的损失。

参考来源：https://www.bleepingcomputer.com/news/security/microsoft-sharepoint-rce-bug-exploited-to-breach-corporate-network/

***END***

阅读推荐

[【安全圈】微软正式推出Windows Server 2025服务器操作系统 支持到2034年10月](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065716&idx=1&sn=5b3532550832d4ca38067a529e8bdc54&chksm=f36e63f4c419eae2a500676eb102c8f8c2c17aa30bb355abd81f9229eb63e6ffa0b11a771ef9&scene=21#wechat_redirect)

[【安全圈】ChatGPT网络搜索功能使用微软必应搜索技术 爬虫名称为OAI-SearchBot](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065716&idx=2&sn=3c84e8540d99ae9a81e5c396504ca3c2&chksm=f36e63f4c419eae2133d645496e425508bb4f99e52efa633eede08a6369cf9f89e002e4d60da&scene=21#wechat_redirect)

[【安全圈】近100万台存在高危漏洞的 Fortinet、SonicWall设备正暴露在公开网络中](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065716&idx=3&sn=4ec937a68fa76b1dd2f7886b3dd43d0d&chksm=f36e63f4c419eae26346e5c246903fa5cc2a9c17201ee9dd85aeef72b7c9d75b82527433ca2e&scene=21#wechat_redirect)

[【安全圈】Lunar SPIDER重整旗鼓：金融业成为最新恶意广告活动的目标](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065716&idx=4&sn=ea31cc52f299e5e6a2b3cb7ac382bdef&chksm=f36e63f4c419eae2a411e15f4c973f9ba21536820946b3c0db1617f4673d9ccefc4e701aa046&scene=21#wechat_redirect)

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