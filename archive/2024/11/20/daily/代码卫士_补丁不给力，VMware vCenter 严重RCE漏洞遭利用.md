---
title: 补丁不给力，VMware vCenter 严重RCE漏洞遭利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521523&idx=1&sn=286f99df03f25ebd1cb1fb497f991b21&chksm=ea94a599dde32c8fb84c9a7247de810f5f23bf5c0c99f55a79ff59780dc42aa54f886a151327&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-20
fetch_date: 2025-10-06T19:18:29.392411
---

# 补丁不给力，VMware vCenter 严重RCE漏洞遭利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQJzjlfp6wPFXicMoooldtvAhOd0ib4IJ6wQdXoDwbuZG6xYHjcLr8EIs0s8cicLjzDBjzfuPeW8ck2Q/0?wx_fmt=jpeg)

# 补丁不给力，VMware vCenter 严重RCE漏洞遭利用

Jessica Lyons

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**博通未能一次修复后，VMware vCenter 中的两个严重漏洞已遭利用。其中一个是可导致远程代码执行 (RCE) 后果的堆溢出漏洞CVE-2024-38812，另外一个是CVE-2024-38813。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQJzjlfp6wPFXicMoooldtvAKVDwiaTtZjHx4oA42uTIicfgRVSQJEW6CAWaOicVhfHhmvuFxuIBKWicZA/640?wx_fmt=gif&from=appmsg)

博通在9月17日首次尝试修复这两个漏洞，但之后承认“未能完全修复”任何一个漏洞，因此在十月发布补丁更新。当时，博通为这两个 vCenter 漏洞都再次发布补丁，并向客户保证称“并未发现在野利用情况”。

本周一，博通发布安全告警称，这两个漏洞“已证实遭在野利用”。博通公司并未就攻击的范围以及幕后黑手的情报置评。

vCenter 是犯罪分子严重的香饽饽，因为管理员可用该工具管理一系列虚拟机，而且一些组织机构运营数千台。因此所有类别的犯罪分子都热爱VMware 安全漏洞。之前，勒索团伙和国家黑客组织都在利用 VMware 漏洞，说明这些修复方案值得迫切关注。

CVE-2024-38812是一个严重的堆溢出漏洞，因处理 DCERPC 协议而导致，CVSS评分为9.8。具有网络访问权限的攻击者可发送特殊构造的数据包，利用该漏洞在易受攻击的系统上执行恶意代码。

CVE-2024-38813是一个高危的CVSS评分为7.5的提权漏洞。攻击者也需要具有对 vCenter Server 的网络访问权限才能实施利用，可将权限提升至 root。

这两个漏洞如遭利用，均影响 vCenter Server 7和8版本、VMware Cloud Foundation 4和5版本。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[关于VMware vCenter Server存在堆溢出漏洞的安全公告](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521255&idx=2&sn=96000770c62b8decfa9e07a493e63e88&chksm=ea94a28ddde32b9b8ba137aabc05013a57d35ead43238f1f5f4b42cb723d96b1f4792e330c13&scene=21#wechat_redirect)

[VMware 修复HCX 平台上可导致RCE的高危SQLi 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521136&idx=2&sn=092bf2813ecefa63156a83b9d8eab160&chksm=ea94a21adde32b0c330f235f9beca98c24ce44fcacdb92e916ec286a71acd272b5c86b1d517b&scene=21#wechat_redirect)

[博通修复 VMware vCenter Server 中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520848&idx=2&sn=d95814f9037c7711dfcb09cd0e590f0c&chksm=ea94a33adde32a2cc2d70ae1c9f784e58a1068b3439966be8fc0130d96ff48e1aae33021a835&scene=21#wechat_redirect)

[VMware 修复Fusion中的高危代码执行漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520668&idx=3&sn=899efb652a40601d77b2cb2fffa9e4a2&chksm=ea94a0f6dde329e0c294039de56f65cffda877a972c98fbfebe68abac81d4ee415d453a6203e&scene=21#wechat_redirect)

[VMware 修复Aria Automation 中严重的SQL注入漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520038&idx=1&sn=c47470c41eba485c6761c101be23ab04&chksm=ea94be4cdde3375a05493cfa38283ce2ea210148cf20f12ae01666d4ae7d06828b0073a00526&scene=21#wechat_redirect)

**原文链接**

https://www.theregister.com/2024/11/18/vmware\_vcenter\_rce\_exploited/

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