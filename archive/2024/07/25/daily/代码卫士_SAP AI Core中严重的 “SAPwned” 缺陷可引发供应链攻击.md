---
title: SAP AI Core中严重的 “SAPwned” 缺陷可引发供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520194&idx=2&sn=7b4dbeae684f3e9a1f79148a5bacf221&chksm=ea94bea8dde337bef23eba6e45455dcd8628e9612a3fe48edfb13b4eb3d31ab510a7d6df1a85&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-25
fetch_date: 2025-10-06T17:44:23.912985
---

# SAP AI Core中严重的 “SAPwned” 缺陷可引发供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFeRMhfAe89ZanXmpN705uxssFViaMSKU0Sqia5b9kNfwe5cTqTO5cbAAg/0?wx_fmt=jpeg)

# SAP AI Core中严重的 “SAPwned” 缺陷可引发供应链攻击

Do Son

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Wiz 公司的安全研究员在负责开发和部署AI模型的 SAP AI Core 中发现了一系列严重漏洞，可导致攻击者访问敏感的客户数据、操纵AI模型，甚至发动大规模的供应链攻击。这些漏洞被统称为 “SAPwned”。**

这些漏洞的根因在于配置不当和安全控制不正确，可导致恶意人员利用 SAP AI Core 复杂的基础设施。攻击者本可访问大量机密的客户数据，包括AI模型、训练数据集和转悠算法。另外，被暴露的漏洞可导致AI 模型被操纵，从而导致数据被篡改和遭攻陷。

研究首先在 SAP AI Core 上创建了一款标准的 AI 应用，它利用 Argo Workflow 生成 Kubernetes Pods。最初，该环境受限，Istio 代理边车执行有限的网络访问权限。然而研究人员发现可通过特定的不被SAP控制元件拦截的 Pod 配置来绕过这些限制。

**第1个bug：绕过网络限制**

研究人员通过 shareProcessNamespace 和 runAsUser（UID 1337，Istio的UID）配置 Pod，与 Istio 代理共享进程名称空间，从而访问 Istio 的配置以及访问该集群中心化 Istiod 服务器的访问令牌，从而删除网络流量限制。

**第2个bug：Loki 泄露AWS 令牌**

研究人员发现 Grafana Loki 的一个实例，通过 /config 端点暴露其配置，包括 AWS 机密可用于访问包含来自 AI Core 服务和客户 Pods 的S3存储桶。

**第3个 bug：未认证的EFS Shares**

多个AWS Elastic 文件系统 (EFS) 实例具有公开配置，可导致在没有凭据的情况下免费访问其内容。这就导致大量AI数据被暴露，包括按照客户ID分类的代码和训练数据集。

**第4个bug：未认证的 Helm 服务器**

被暴露的 Helm 服务器组件 Tiller，可使研究人员访问 SAP Docker 注册表和 Artifactory 服务器的权限机密。这种访问权限可用于提取商业机密并执行供应链攻击。

**第5个bug：Cluster 完全接管**

Helm 服务器的写权限可导致完整的 Kubernetes 集群遭接管。研究人员部署了一个恶意的 Helm 报，获得集群-管理员权限，从而访问并操纵客户Pods、窃取敏感数据并干扰AI模型的完整性。他们还访问了 SAP AI Core 范围以外的客户机密，包括 AWS、SAP HANA和 Docker Hub凭据。

SAP已证实并修复了这些漏洞，向客户保证数据未被攻陷。然而，该事件说明企业尤其是依赖于云的AI平台面临着网络威胁。SAPwnd 漏洞为整个AI行业拉响警报。该事件强调了采用主动安全措施保护敏感数据、保护AI完整性以及缓解供应链攻击的重要性。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Ollama AI 基础设施工具中存在严重的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519855&idx=1&sn=7088d05b2e6a3cdf56986e480ea5119e&chksm=ea94bf05dde3361305094408f06ff54a8d271116378e3c9f710153b2dcb7f133fb984b7373ff&scene=21#wechat_redirect)

[PyTorch 严重漏洞可导致AI敏感数据被盗](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519716&idx=2&sn=df8e16d464e733a183fadfc8e360cc10&chksm=ea94bc8edde335986daf0ff0d4e2bdf8751fd9df7c47d7cf2d9e614452e475a020ef01df0b6c&scene=21#wechat_redirect)

[SAP产品存在4个严重漏洞，其中1个位于ABAP内核中](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516897&idx=2&sn=f40a38c1290acb6b5b7f6553de58ab62&chksm=ea94b38bdde33a9dfd1c0f15390089765ee003e5d7bc0529f13b2ec62049364a5a72e57bfeab&scene=21#wechat_redirect)

[SAP 修复多个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516461&idx=2&sn=1319c4b17cbfce2602f31c1375378a21&chksm=ea94b047dde33951dc262c284fcf1d6aac308d66672887728510ab05882edc873667a4dcb89f&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/sap-ai-cores-critical-sapwned-flaws-raise-supply-chain-attack-concerns/

题图：Pexels License

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