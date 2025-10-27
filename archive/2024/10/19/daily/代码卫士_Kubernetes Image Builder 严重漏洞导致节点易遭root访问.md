---
title: Kubernetes Image Builder 严重漏洞导致节点易遭root访问
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521146&idx=2&sn=671909f46dea5c8b54973aff9c570634&chksm=ea94a210dde32b06ee8de3eb6a5b2d7a1eac4ace624827b816fa13689f076425780451afa345&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-19
fetch_date: 2025-10-06T18:52:50.388440
---

# Kubernetes Image Builder 严重漏洞导致节点易遭root访问

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTGcUT8A7hNUn6waAHhyqpM7gRYCiapCq3XtPyZwD0y0av8n8AE0YOWVWiaQU2Lz8CoZwyaEn8Xjibaw/0?wx_fmt=jpeg)

# Kubernetes Image Builder 严重漏洞导致节点易遭root访问

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTGcUT8A7hNUn6waAHhyqpMaoYRyafO0SqIT6iaTjickLwCnicZ3rng5EhFnvaMfOjgWs2q65D5f1HVQ/640?wx_fmt=gif&from=appmsg)

**Kubernetes Image Bulder 中存在一个严重漏洞 (CVE-2024-9486)，在某些情况下可被滥用于获取 root 访问权限。**

该漏洞已在0.1.38中修复，项目维护人员向发现并报送该漏洞的研究员 Nicolai Rybnikar 致谢。

Red Hat 公司的 Joel Smith 在一份告警中提醒称，“Kubernetes Image Builder 中存在一个安全问题，默认凭据在镜像构建流程中被弃用。另外，使用 Proxmox 提供商构建的虚拟机镜像并未禁用这些默认凭据，使用这些镜像的节点可通过这些默认凭据进行访问。这些凭据可用于获得 root 访问权限。”

话虽如此，只有当 Kubernetes 集群节点使用的虚拟机镜像是通过提供商 Proxmox 的 Image Builder 项目创建时，这些集群才受漏洞影响。作为临时缓解措施，建议禁用受影响虚拟机上的构建者账户。另外建议用户使用已修复的 Image Builder 版本重构受影响镜像并在虚拟机上重新部署。

Kubernetes 团队部署的修复方案避开了在镜像构建过程中设置的随机生成密码的默认凭据。另外，该构建者账户在镜像构建流程结束时被禁用。

Kubernetes Image Builder 0.1.38版本还修复了一个相关漏洞（CVE-2024-9454，CVSS评分6.3）。该漏洞与通过 Nutanix、OVA、QEMU或其它提供商创建镜像构建时使用的默认凭据有关。该漏洞的严重性更低是因为通过这些提供商构建镜像的虚拟机，“只有在攻击者能够触及构建镜像的虚拟机且利用该漏洞在构建过程中修改镜像时”才会受影响。

此前，微软发布可导致提权和信息泄露的服务器端补丁：

* CVE-2024-38139（CVSS评分8.7）：微软 Dataverse 中的认证不当漏洞，可导致授权攻击者在网络中提升权限。
* CVE-2024-38204（CVSS评分7.5）：Imagine Cup 中的访问控制不当漏洞，可导致授权攻击者在网络中提升权限。
* CVE-2024-38190（CVSS评分8.6）：Power Platform 中的授权缺失漏洞，可导致未认证攻击者通过网络攻击向量查看敏感信息。

前不久，Apache Solr 开源企业搜索引擎也修复了一个漏洞（CVE-2024-45216，CVSS评分9.8），可导致在可疑实例上绕过认证。该漏洞影响自 Solr 5.3.0起至8.11.4之前的版本以及9.0.0起至9.7.0之前的版本，已在8.11.4和9.7.0中修复。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[谷歌云修复影响 Kubernetes 服务的提权漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518533&idx=1&sn=2cd4cf6cb64d8674ff01d4eb89b22c43&chksm=ea94b82fdde33139a30d7d743eee2c64a91f8291a4eba9f5bf73b936e2e833a01aebbabd7c9d&scene=21#wechat_redirect)

[研究员发现敏感 Kubernetes 机密被暴露，引发供应链攻击担忧](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518215&idx=1&sn=c0e545f46d3bd573206f0ce36185c98d&chksm=ea94b96ddde3307b28636fd37b7a1d0a2992b0db21d28c06cbb61f036e2b3139839a63b02852&scene=21#wechat_redirect)

[多个Kubernetes 高危漏洞可用于在 Windows 端点执行远程攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517654&idx=2&sn=652c4e44e960ea1468d3f6e14aa9ca26&chksm=ea94b4bcdde33daab2669f9abe0ceb5579f5b0531002bffd15cee9657a03daba686913b68c5b&scene=21#wechat_redirect)

[适用于Kubernetes 的AWS IAM 验证器中存在漏洞，导致提权等攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512889&idx=4&sn=bd3623a8d3f38a4206124b8681f1c510&chksm=ea948253dde30b457da57e1cfc42ab6fc1b7c06335250b93b2f6b89654f0b83884057e98fbd5&scene=21#wechat_redirect)

[Kubernetes的开源GitOps 平台 Argo CD 中存在严重的提权漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511966&idx=2&sn=4d118084132be27daf3b30f265d2a43a&chksm=ea949ef4dde317e2288e7a4fe13293b18d1063fa90b1f31ab148d05aa255b0f652281b244c1b&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/10/critical-kubernetes-image-builder.html

题图：Pixabay License

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