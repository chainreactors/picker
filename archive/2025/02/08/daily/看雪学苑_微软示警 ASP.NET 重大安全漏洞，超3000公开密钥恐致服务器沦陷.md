---
title: 微软示警 ASP.NET 重大安全漏洞，超3000公开密钥恐致服务器沦陷
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589336&idx=2&sn=71772d009fe80e5339e6925f517765da&chksm=b18c281286fba104fefc248eff29454d426e3b33dfce1cbf82b6862933f414c4a29875564fb8&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-08
fetch_date: 2025-10-06T20:37:50.868852
---

# 微软示警 ASP.NET 重大安全漏洞，超3000公开密钥恐致服务器沦陷

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EOR8xOggn0o7qcI6pM5mibA2iapRs55fc7WoSyibTVBu6moEtD1Oiao7pVYiaAymd1QySEbYPnM9GAVqA/0?wx_fmt=jpeg)

# 微软示警 ASP.NET 重大安全漏洞，超3000公开密钥恐致服务器沦陷

看雪学苑

看雪学苑

微软近期发出重要安全示警，指出**攻击者正在利用网上公开的ASP.NET静态密钥，通过ViewState代码注入攻击部署恶意软件。**

微软威胁情报专家发现，一些开发者在软件开发中使用了在代码文档和代码库平台上公开的ASP.NET validationKey和decryptionKey密钥。这些密钥原本用于保护ViewState免遭篡改和信息泄露，但如今却被攻击者利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EOR8xOggn0o7qcI6pM5mibAAicBIvgmfjlrq5MyfickGKKzQL2qXLK2Gkc9icxFswWdRTJXZkiadr7yEA/640?wx_fmt=png&from=appmsg)

ViewState是ASP.NET Web窗体用于控制状态和保存页面信息的机制。**攻击者通过附加伪造的消息认证码（MAC），创建恶意ViewState，并通过POST请求将其发送到目标服务器。****目标服务器上的ASP.NET Runtime使用正确的密钥解密并验证这些伪造的ViewState数据，随后将其加载到工作进程内存中并执行，从而让攻击者在IIS服务器上实现远程代码执行，并部署其他恶意载荷。**

微软在2024年12月观察到一起攻击事件，攻击者使用公开的密钥向目标IIS服务器部署了Godzilla后渗透框架，该框架具备恶意命令执行和Shellcode注入功能。微软已识别出超过3000个公开的密钥，这些密钥都可能被用于ViewState代码注入攻击。**以往的ViewState代码注入攻击多使用从暗网论坛购买的被盗密钥，而此次攻击中使用的公开密钥存在于多个代码库中，开发者可能直接将其复制到代码中而未进行修改，因此风险更高。**

为应对这一威胁，微软建议开发者采取以下措施：

* 安全地生成机器密钥，不使用默认密钥或网上找到的密钥；
* 加密machineKey和connectionStrings元素以阻止对明文机密的访问；
* 升级应用程序以使用ASP.NET 4.8，从而启用反恶意软件扫描接口（AMSI）功能；
* 通过使用攻击面减少规则（如阻止服务器上的Webshell创建）来加固Windows服务器。

此外，微软还分享了使用PowerShell或IIS管理器控制台在web.config配置文件中移除或替换ASP.NET密钥的详细步骤，并从其公开文档中删除了密钥示例，以进一步阻止这种不安全的做法。

微软警告称，如果已经发生利用公开密钥的攻击，仅仅轮换密钥是不够的，因为攻击者可能已经建立了后门或持久化机制以及其他后渗透活动，可能需要进一步调查。特别是面向网络的服务器，应进行全面调查，并在发现公开密钥被使用的情况下，强烈考虑在离线环境中重新格式化和重新安装，因为这些服务器面临更高的被利用风险。

资讯来源：bleepingcomputer

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibExiboJzOiafqGLvlOkrmU6NIr3qSr7ibpkIo2N5mhCTNXoMl37s2oRSIDw/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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