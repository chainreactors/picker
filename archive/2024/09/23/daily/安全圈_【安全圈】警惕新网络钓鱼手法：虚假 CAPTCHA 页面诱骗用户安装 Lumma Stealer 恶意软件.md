---
title: 【安全圈】警惕新网络钓鱼手法：虚假 CAPTCHA 页面诱骗用户安装 Lumma Stealer 恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064597&idx=3&sn=10396f2711c45e64515ea2d5aeb8b048&chksm=f36e6715c419ee03936d3da0cdb3d3a6f96afe8fdaa6173dcaf004c1dce37846a39fa14a1220&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-23
fetch_date: 2025-10-06T18:24:41.154486
---

# 【安全圈】警惕新网络钓鱼手法：虚假 CAPTCHA 页面诱骗用户安装 Lumma Stealer 恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0Dc1F34tTvBrk4ueb1nA60ZecTNxGyQyVYp32nrrumGNXAhRuVGqlUWA/0?wx_fmt=jpeg)

# 【安全圈】警惕新网络钓鱼手法：虚假 CAPTCHA 页面诱骗用户安装 Lumma Stealer 恶意软件

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

网络钓鱼

一个新的网络钓鱼活动使用虚假的 CAPTCHA 验证页面来诱骗 Windows 用户运行恶意 PowerShell 命令、安装 Lumma Stealer 恶意软件并窃取敏感信息。随时了解和保护。

CloudSec 的网络安全研究人员发现了一种新的网络钓鱼活动，该活动诱骗用户通过虚假的人工验证页面运行恶意命令。该活动主要针对 Windows 用户，旨在安装 Lumma Stealer 恶意软件，导致敏感信息被盗。

#### 攻击的工作原理

威胁行为者正在创建托管在各种平台上的网络钓鱼网站，包括 Amazon S3 存储桶和内容分发网络 （CDN）。这些网站模仿合法的验证页面，例如虚假的 Google CAPTCHA 页面。当用户单击 “Verify” 按钮时，他们会看到不寻常的指示：

1. 打开“运行”对话框 （Win+R）
2. 按 Ctrl+V
3. 按 Enter 键

在用户不知道的情况下，这些操作会执行一个隐藏的 JavaScript 函数，该函数将 base64 编码的 PowerShell 命令复制到剪贴板。当用户粘贴并运行命令时，它会从远程服务器下载 Lumma Stealer 恶意软件。

CloudSec 在周四发布之前与 Hackread.com 分享的报告显示，下载的恶意软件通常会下载额外的恶意组件，这使得检测和删除变得更加困难。虽然目前用于传播 Lumma Stealer，但这种技术可以轻松适应提供其他类型的恶意软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0DfViaolehrE0SLhFzVv5to0UbE4tlDmkibsOKGiaI44LubqLcdz7cK9ia4w/640?wx_fmt=jpeg&from=appmsg)

当用户点击虚假的 Google CAPTCHA 提示时触发攻击流和虚假验证过程（截图：CloudSec）

供您参考，Lumma Stealer 旨在从受感染的设备中窃取敏感数据。虽然目标的具体数据可能有所不同，但通常包括登录凭据、财务信息和个人文件。就在这次最新的活动是在恶意软件被发现伪装成 OnlyFans 黑客工具感染其他黑客的设备几天后进行的。

2024 年 1 月，发现 Lumma 通过受感染的 YouTube 频道分发的破解软件进行传播。早些时候，在 2023 年 11 月，研究人员发现了 LummaC2 的新版本，称为 LummaC2 v4.0，它使用三角技术来窃取用户数据来检测人类用户。

### 现在怎么办？

既然已经报道了新的 Lumma 窃取者感染狂潮，企业和毫无戒心的用户需要保持警惕，避免陷入最新的虚假验证骗局。以下是一些常识性规则和简单而必要的提示，用于防范 Lumma 和其他类似的窃取者：

* 教育自己和他人：与朋友、家人和同事分享这些信息，以提高对这种新威胁的认识。
* 警惕不寻常的验证请求：合法网站很少要求用户通过 “Run” 对话框执行命令。对任何提出此类请求的网站保持警惕。
* 不要复制和粘贴未知命令：避免从不受信任的来源复制和粘贴任何内容，尤其是要在终端或命令提示符下运行的命令。
* 保持软件更新：确保您的操作系统和防病毒软件是最新的，以修补已知漏洞。
* 重要：关注 Hackread.com 了解最新的网络安全新闻。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhAK7Fv8oWpNiaXrhevHW8p6kdV6HyKu4P3iatdHBicGce4lg5vw9qxMJRvnoFwx4Dm5EZAqNNWZC3dQ/640?wx_fmt=jpeg&from=appmsg)[【安全圈】速更新！GitLab发布更新修复CVSS满分漏洞](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064581&idx=1&sn=a8d25f47e9142354cddaccee15a9e264&chksm=f36e6705c419ee130f4d3f0e49710c74c10402ee7aa922bcf4c208d71d1956c64caa923497ee&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhWaD223ARVtJuibmk6sDanjyOZS5Kk0TGsv1JzicUqOfHsp2yK3LP3kXUNleGsywC3B2PQsOX1fdYA/640?wx_fmt=jpeg&from=appmsg)[【安全圈】遭受 Medusa 勒索软件攻击，1TB护照、驾驶执照泄露](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064581&idx=2&sn=cc2983b9d05d015a0f637bceb468f01d&chksm=f36e6705c419ee13ca8b24c68f94deeeacf830cf6d2652b28a978286ea96b2e562962312ae52&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgiaaXeNGKfYJo9KNnBhco0DpbEBKQIluVUGMEuBiaVuYxcOEkDyMZOR1cjqDxE2EibDicuN4x1Ib7tjQ/640?wx_fmt=jpeg)[【安全圈】迪士尼宣布弃用 Slack 平台](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064581&idx=3&sn=83152847e2afad70f1324f5da5de3b7a&chksm=f36e6705c419ee139a7eb75252f0506a83e391436f819a10b3ae2739680efe9a3f58c30584c3&scene=21#wechat_redirect)

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