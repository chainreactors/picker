---
title: Google Cloud 依赖混淆漏洞影响数百万台服务器
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520848&idx=4&sn=5dd6c8f2b2d48123ef978d8ef1b071ff&chksm=ea94a33adde32a2cfb349b7e9cc119746f3287400e9fd952e369f64de22f4b7a706240b85d71&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-19
fetch_date: 2025-10-06T18:25:52.651849
---

# Google Cloud 依赖混淆漏洞影响数百万台服务器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTfLbX6nWbEgIoIYUH9hASkyia61voS6nzF5GzV9hTJQvUescBoV3G4h57E5o4yryZ2lOvIzFwic4iaA/0?wx_fmt=jpeg)

# Google Cloud 依赖混淆漏洞影响数百万台服务器

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Tenable 公司分享了一种依赖混淆攻击方法，本可将 Google Cloud Platform (GCP) 客户暴露到远程代码执行攻击中。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMT7lctusib0CJe6kmfLUSPUwffoqp44kZ7BSibPFbNZyhCdngYicKiauxY4cDvXjKp8BydaPibyEWzYHVg/640?wx_fmt=png&from=appmsg)

该问题被命名为 “CloudImposer”，本可导致攻击者劫持在谷歌 Cloud Composer 管道协同工具每个实例上预安装的一个内部软件依赖。GCP的 App Engine 和 Cloud Functions 服务也受影响。

Tenable 公司提到，该问题的根因在于在 Python 中使用 “-extra-index-url” 参数，要求应用除了特定的私钥注册表外，查找公开钥 (PyPI) 中的私密依赖。

该公司指出，“这一行为导致攻击者执行依赖混淆攻击：上传与合法包名称相同的恶意包，劫持包安装流程。”攻击者还可利用其它情况如 “pip”，在遇到名称相同的的两个程序包时，优先处理版本号更高的程序包。

Cloud Composer 的情况也并不乐观。Tenable 公司发现，当指令要求仅安装某个版本的程序包时，如果使用了 –extra-index-url 参数，则pip会优先公开注册表。Python Packaging 和 GCP 文档都建议在非公开仓库中托管依赖时使用 “-extra-index-url” 参数，而开发人员对包管理系统的信任易引发依赖混淆。谷歌在服务器上安装非公开程序包时本身就使用了该函数，发现所引用的包不存在于公开注册表中时，Tenable 创建了名称相同的包，将其上传到一个公开仓库并启动了针对 Cloud Composer 的依赖混淆攻击。而Cloud Composer 就是谷歌管理服务版本的 Apache Airflow。

成功验证该 PoC 导致在谷歌内部服务器上执行代码后，Tenable 公司将该 CloudImposer 漏洞告知谷歌，后者将其判为RCE漏洞并立即修复。谷歌还更新了GCP文档，删除了使用 –extra-index-url 参数的建议，并以 –index-url 参数取而代之，后者仅检查所定义注册表中的程序包，从而减小了依赖混淆攻击的风险。

Tenable 公司还将这些问题告知 Python 软件基金会，后者表示虽然在2023年2月收到了关于缓解依赖混淆攻击风险的论文，但并未接受或完成该实现。

Tenable 公司在2024美国黑帽大会上展示了自己的研究成果，说明了CloudImposer 类的漏洞如何可被用于影响云互联服务。和叠叠高游戏一样，云提供商开始在其它服务的基础上构建其服务。这意味着一旦有服务遭攻击，那么其它服务也会受影响。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Apache 项目中存在依赖混淆漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519338&idx=2&sn=c65a447c216d55afbb9483c48c34f453&chksm=ea94bd00dde334161df74aa1e15e2b728e866bddfe2a1e21bfb5e44dfcf65213634e19fe8ad7&scene=21#wechat_redirect)

[什么鬼？我能通过依赖混淆攻击在 Halo 游戏服务器中执行命令，微软不 care？！](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506074&idx=1&sn=40b66f0cbedbc7f81a5e8ea6b5f96000&chksm=ea94e9f0dde360e67dbf52f5a486a65d76eebbf2b03155baf27f8d153092d152d111d2c93f9b&scene=21#wechat_redirect)

[依赖混淆 exploit 已被滥用于攻击亚马逊等多家大厂](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247501946&idx=2&sn=225e6c564f5f6957cd3c58ebccd0de5f&chksm=ea94f910dde3700643f0f0c3841e2db050dcdc7ad21103e54f1bd01f21cad834d44cec9937ad&scene=21#wechat_redirect)

[“依赖混淆”供应链攻击现身 微软苹果特斯拉优步等超35家企业内网失陷](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247501483&idx=1&sn=6760f3d9cbc218e9a54bd48566ab568c&chksm=ea94f7c1dde37ed7c8142f37407e1f92f46a3cece525ea70963ce322db51571b30e2d2f19d2b&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/dependency-confusion-could-have-led-to-rce-in-google-cloud-platform/

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