---
title: 【安全圈】微软 Win11 BitLocker 存在物理接触即可绕过的重大漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067148&idx=3&sn=d0e8225dafa1c2fb13ad0e7f22376327&chksm=f36e790cc419f01a20528cc722e7f75d6c77ce8bb1bb4ac0f0503c3e9f9a6357c34f2172a526&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-05
fetch_date: 2025-10-06T20:08:27.103501
---

# 【安全圈】微软 Win11 BitLocker 存在物理接触即可绕过的重大漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljuqthRVHV1bzlHGntXrW7eE9E0HcJBgp6ZV7pJm96eY5Fr7n6Z1Hy2VFILAwbcuXnwyRXicDNr2lg/0?wx_fmt=jpeg)

# 【安全圈】微软 Win11 BitLocker 存在物理接触即可绕过的重大漏洞

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

1月2日，安全专家揭示，微软Windows 11中的BitLocker加密技术存在一个严重漏洞。黑客只需通过一次物理接触，就能将设备置入恢复模式，并通过网络连接，轻松解密Windows 11系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljuqthRVHV1bzlHGntXrW7e5iaLBK09ibZmClttd4AKZnAVgy3rx3eiafbcvsJVzWD1JDRy7wCq1FYBg/640?wx_fmt=jpeg&from=appmsg)

在最近的混沌通信大会上，安全研究员兼硬件黑客Thomas Lambertz（th0mas）发表了题为《Windows BitLocker: Screwed without a Screwdriver》的演讲，展示了如何利用CVE-2023-21563漏洞攻破BitLocker加密。该漏洞允许攻击者在设备未开机的情况下，通过简单的物理访问，成功突破BitLocker防线。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljuqthRVHV1bzlHGntXrW7e1KRxWic17F9EaUsZAGzwwGIicCNlpL0y34hqYicy92H0KmtxibV88voD3w/640?wx_fmt=jpeg&from=appmsg)

虽然微软在2022年发布了针对CVE-2023-21563漏洞的修复，演示却表明漏洞依然未完全解决。在较新的Windows 11系统中，BitLocker默认启用“设备加密”功能，在硬盘静态时进行加密，但一旦启动合法的Windows系统，硬盘会自动解密。

Lambertz通过一种名为“bitpixie”的攻击方式，利用旧版Windows引导加载程序的漏洞，提取加密密钥到内存中，再通过Linux系统读取内存内容，最终破解BitLocker加密。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljuqthRVHV1bzlHGntXrW7e5vfwHD8k80MXXpHCmmzAfGd7aExL0RGT42iaIlPBTa0UjmicHianMP97A/640?wx_fmt=jpeg&from=appmsg)

尽管微软已经意识到这个问题，并计划通过撤销易受攻击的引导加载程序证书来永久解决该问题，但由于UEFI固件存储证书的内存空间有限，全面防御仍然困难。微软计划从2026年开始分发新的安全启动证书，这将要求主板制造商更新UEFI固件。

在此之前，用户可以通过设置PIN码来备份BitLocker密钥，或者在BIOS中禁用网络访问来增强安全性。

Lambertz警告称，哪怕是简单的USB网络适配器，也足以执行这一攻击。虽然对于普通用户而言，这种攻击的风险较低，但对于企业、政府等注重网络安全的机构来说，一旦遭遇物理接触并且具备USB网络适配器，BitLocker加密防线将毫无抵抗力，这无疑是一个严重的安全隐患。

***END***

阅读推荐

[【安全圈】揭穿虚假人气：研究揭露 GitHub 上有 450 万个假星星](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067112&idx=1&sn=425e0c2e12fd7778269f7fa579522d47&scene=21#wechat_redirect)

[【安全圈】美国陆军士兵因涉嫌出售 AT&T 和 Verizon 客户通话记录而被捕](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067112&idx=2&sn=80ba8f697fada6825cb2276649351bf5&scene=21#wechat_redirect)

[【安全圈】伪造的 7-Zip 漏洞代码被追溯到人工智能产生的误解](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067112&idx=3&sn=7e0c3ed063040f28dd8bb8c3ead818df&scene=21#wechat_redirect)

[【安全圈】勒索软件团伙泄露罗德岛 RIBridges 遭窃取的数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067112&idx=4&sn=93ea0083002288cd3c773772b6ffad0e&scene=21#wechat_redirect)

[【安全圈】2024 年最大的网络安全和网络攻击事件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067095&idx=1&sn=a9ecd46a4afe0c77216a405c825a1e9a&scene=21#wechat_redirect)

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