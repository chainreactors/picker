---
title: 微软Azure新漏洞可导致RCE，研究员获3万美元奖励
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515363&idx=2&sn=36927e449388a6dc1fcc5e7ccbf92a2e&chksm=ea948d89dde3049ffbff2cf56bcfbaa5d4e844e193a9391619d310ac4f075848d0fc66a2cf00&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-01-21
fetch_date: 2025-10-04T04:29:26.659642
---

# 微软Azure新漏洞可导致RCE，研究员获3万美元奖励

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRho1FFpvibp3OAQVj3gDZXXpOV47wm21Uhql8auTjzViaqH0WU0ibD6lI8P2iaZrG8C44xgiaicssiaubnw/0?wx_fmt=jpeg)

# 微软Azure新漏洞可导致RCE，研究员获3万美元奖励

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**和微软Azure关联的多款服务中存在一个严重的远程代码 (RCE) 漏洞，可被恶意人员用于完全控制目标应用。**

发现该漏洞的Ermetic 公司的研究员 Liv Matan 在报告中提到，“该漏洞是通过SCM服务Kudu 上的跨站请求伪造 (CSRF) 实现的。通过利用该漏洞，攻击者可将包含 payload的恶意ZIP文件部署到受害者的Azure应用上。”

Ermetic公司将该漏洞命名为 “EmojiDeploy”，它还可导致敏感信息被盗并横向移动到其它Azure服务。

微软在2022年10月26日收到漏洞报告后已在12月6日将其修复，并颁发3万美元的奖励。微软将Kudu描述为“与基于源控制的部署有关的以及和其它部署方法如Dropbox和OneDrive 同步的Azure App Service多个特性背后的引擎”。

在由Ermetic 部署的假设性攻击链中，攻击者可利用位于Kudu SCM面板中的CSRF漏洞绕过保护措施，通过向 “/api/zipdeploy”端点发布特殊构造请求的方式发动同源攻击，传播恶意文档并获得远程访问权限。

跨站点请求伪造即攻击者诱骗web应用程序的认证用户执行越权命令。该ZIP文件在HTTP请求的主体中编码，使得受害者应用导航至受攻击者控制的域名，而该域名绕过服务器的同源策略托管恶意软件。

研究人员指出，“该漏洞对组织机构的影响取决于应用管理身份的权限。应用最低权限原则可大大限制其影响范围。”

就在几天前，Orca Security 公司发布了服务器端请求伪造攻击的四个实例，这些攻击影响Azure API Management、Azure Functions、Azure Machine Learning 和 Azure Digital Twins。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奥利地公司利用Windows 和 Adobe 0day 攻击欧洲和中美洲实体](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513235&idx=2&sn=24037f6d2d1bec62277ccbb930f55444&chksm=ea9485f9dde30cefdbbe497a8cbe9b23231a2d757bcac7219a0783c35a19d018309cb22bbe8e&scene=21#wechat_redirect)

[Adobe 修复Commerce 和 Magento 平台中的又一个严重RCE](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510609&idx=2&sn=53c80ddb9a02f50ed2226e24d72d4729&chksm=ea949b3bdde3122d4cc06192a8aa07ef4ebe973574bd842b816eb983e8b79de9054b03b2fb29&scene=21#wechat_redirect)

[十多年前的 Adobe ColdFusion 漏洞被用于勒索攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507998&idx=2&sn=fd44dbdbf72b7df83e081524bebf4667&chksm=ea949174dde318623fad2d710dd6603f2144e71e5ab47ff56088e63eb917ccc2beabfea3ef2c&scene=21#wechat_redirect)

[Adobe 修复严重的 Photoshop 缺陷](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247507239&idx=3&sn=4cfd707b7ba6e80005e9bb54f87e9d4d&chksm=ea94ec4ddde3655b5469cdf70296f84561ad7aaceb4d84801e445b65b529af5cd24a81dee39b&scene=21#wechat_redirect)

[黑客在野利用 Adobe Reader 0day 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247504175&idx=2&sn=ea4ef39dae4444a76addf9fa2b4ccb9f&chksm=ea94e045dde36953fca23ce3e96680d7ce5a1a25fe727f4d2fabf36357d403700b303d3d275d&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2023/01/new-microsoft-azure-vulnerability.html

题图：Pixabay License‍

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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