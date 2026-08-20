---
title: 攻击者利用 MLflow 漏洞窃取云凭据和机密信息
url: https://mp.weixin.qq.com/s/3VSiAcVZS87Q5rY4lns8gA
source: Doonsec's feed
date: 2026-08-19
fetch_date: 2026-08-20T02:53:26.941625
---

# 攻击者利用 MLflow 漏洞窃取云凭据和机密信息

# 攻击者利用 MLflow 漏洞窃取云凭据和机密信息

Ravie Lakshmanan
Ravie Lakshmanan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

编译：代码卫士

**影响开源人工智能平台****MLflow****和开源、基于网络的****SCADA/HMI****软件****FUXA****的两个严重漏洞（****CVE-2026-64849****和****CVE-2026-25895****），目前正遭到恶意扫描和利用。**

根据两家公司watchTowr和VulnCheck分别发布的报告，两个漏洞如下：

* CVE-2026-64849（CVSS评分：9.3）是位于MLflow中的一个未认证服务器端请求伪造漏洞，可导致攻击者访问Tracking Server（mlflow 服务器）的攻击者向任意内部云元数据端点发出HTTP请求，并提取敏感数据。（影响版本 < 3.15.0）
* CVE-2026-25895（CVSS评分：9.5）是位于FUXA中的一个关键功能缺少身份验证以及路径遍历漏洞，可导致未认证的远程攻击者向服务器文件系统写入任意文件，并实现远程代码执行。（影响版本 <= 1.2.9）

watchTowr公司在LinkedIn上发布的一篇文章中表示：“攻击者正在利用[CVE-2026-64849]直接访问云元数据服务，并窃取云凭据和秘密。”并补充表示在2026年8月17日该漏洞获得编号后的数小时内，就检测到攻击者无差别地扫描互联网上暴露的MLflow实例。

watchTowr公司的首席威胁情报专家Yordan Ganchev在一份声明中表示：“该漏洞可导致攻击者利用MLflow模型注册表webhooks中的缺陷，通过受影响系统代理请求，并与内部服务交互。该漏洞利用它处理web重定向的方式，绕过了先前的补丁。我们的全球蜜罐遥测数据表明，攻击者正在滥用该漏洞，针对云托管的MLflow系统，试图从已知的内部IP地址和服务中提取凭据和秘密。”

建议运行MLflow的组织机构优先为受影响且暴露的系统打补丁，审查审计日志以查找入侵迹象，并检查敏感凭证是否已暴露。

VulnCheck表示，自2026年8月18日起检测到针对CVE-2026-25895的恶意扫描。该公司已观察到单个IP地址广泛扫描互联网上易受攻击的FUXA实例，发现约有60个FUXA安装暴露于公共互联网。VulnCheck研究副总裁Caitlin Condon在LinkedIn上发布文章中表示：“攻击者请求尝试通过CVE-2026-25895路径遍历，用垃圾数据覆盖main.js。尚未发现投放任何RCE有效载荷。”

在过去一年中，FUXA中的另外两个漏洞CVE-2026-25939和CVE-2023-33831也遭活跃利用。Condon表示CVE-2023-33821的利用活动“可追溯至2025年11月，而最近一次发生在昨天”。

代码卫士试用地址：https://sast.qianxin.com/

开源卫士试用地址：https://oss.qianxin.com/

---

**推荐阅读**

[恶意PyPI 包针对 macOS，窃取谷歌云凭据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520240&idx=2&sn=549c4734cb750f652f9105a8e5df0546&scene=21#wechat_redirect)

[塔塔电子数据泄露，苹果和特斯拉机密供应链信息遭暴露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526473&idx=1&sn=40ae1df01b82f1747285dd3b6f1b6b68&scene=21#wechat_redirect)

[GitLab 公开仓库暴露超过1.7万份机密信息](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524561&idx=2&sn=7ed0ade9d82089d6e02e5c90e36d90a4&scene=21#wechat_redirect)

[很多福布斯AI 50强公司的 GitHub 仓库泄露机密信息](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524359&idx=1&sn=f18cc055bc4baae64ee46cf0d4b05e0d&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/08/attackers-exploit-mlflow-ssrf-flaw-to.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]()![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

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