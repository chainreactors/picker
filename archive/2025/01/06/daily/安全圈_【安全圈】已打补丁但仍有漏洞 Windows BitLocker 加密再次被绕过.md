---
title: 【安全圈】已打补丁但仍有漏洞 Windows BitLocker 加密再次被绕过
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067165&idx=3&sn=d144262f4db66660f995538078a1b911&chksm=f36e791dc419f00b53c872da23e5261585cb279c4fa08d939ea682657a5925e791631aa65f37&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-06
fetch_date: 2025-10-06T20:09:39.594253
---

# 【安全圈】已打补丁但仍有漏洞 Windows BitLocker 加密再次被绕过

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljQAx0dKdicxQ1wu2wGacwqj9MibOsWboMRUVJibackW9XmtKSs4PDBEDia6EPWbLHKL8qtvUrHrjBcZw/0?wx_fmt=jpeg)

# 【安全圈】已打补丁但仍有漏洞 Windows BitLocker 加密再次被绕过

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljQAx0dKdicxQ1wu2wGacwqjw8N4YXnmBhibUy6icX21NVVbvsUicQ3czyrTln5v2qlwP12ibTnK2wILibA/640?wx_fmt=other&from=appmsg)上周，在混沌通信大会（CCC）上出现的一个新发现动摇了 Windows 可信赖的 BitLocker 加密技术的基础。安全研究员托马斯-兰伯茨（Thomas Lambertz）在其题为 “Windows BitLocker：没有螺丝刀也能拧紧 ”的演讲中暴露了一个明显的漏洞，该漏洞允许攻击者绕过 BitLocker 加密并访问敏感数据，即使是在据称已针对该漏洞打了补丁的系统上也是如此。

这个被称为 “bitpixie”（CVE-2023-21563）的漏洞最初于 2022 年 11 月被微软解决。然而，Lambertz 演示了攻击者如何利用过时的 Windows 引导加载器通过安全启动来提取加密密钥。这种攻击只需要对设备进行瞬间物理访问和网络连接，无需使用螺丝刀或硬件黑客。

其根本原因在于 UEFI 中的证书存储空间有限，而 UEFI 是启动过程中的一个关键组件。新的安全启动证书预计在 2026 年前无法获得。作为临时措施，Lambertz 建议用户为 BitLocker 设置自定义 PIN 或通过 BIOS 禁用网络访问。不过，即使是基本的联网 USB 设备也有可能为攻击提供便利。

虽然普通用户可能不是主要攻击目标，但对企业、政府和其他高安全环境的影响却很大。只需短暂的物理访问就能完全解密设备，这引起了人们对数据保护的严重关注。

对于那些希望进一步探讨这一话题的人，CCC 媒体中心网站上有兰伯特 56 分钟演讲的完整录音。它深入探讨了错综复杂的技术问题，并解释了为什么解决这一漏洞会带来如此艰巨的挑战。

***END***

阅读推荐

[【安全圈】印度出手！多款VPN应用被谷歌苹果下架，Cloudflare也未能幸免](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067148&idx=1&sn=02a9937aa327a818ad57260c47a32fd6&scene=21#wechat_redirect)

[【安全圈】开源终端工具曝重大安全漏洞，输入信息可能被窃取！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067148&idx=2&sn=b5d58580bfec4388018946e5f03f2ce6&scene=21#wechat_redirect)

[【安全圈】微软 Win11 BitLocker 存在物理接触即可绕过的重大漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067148&idx=3&sn=d0e8225dafa1c2fb13ad0e7f22376327&scene=21#wechat_redirect)

[【安全圈】美国陆军士兵因涉嫌出售 AT&T 和 Verizon 客户通话记录而被捕](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067112&idx=2&sn=80ba8f697fada6825cb2276649351bf5&scene=21#wechat_redirect)

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