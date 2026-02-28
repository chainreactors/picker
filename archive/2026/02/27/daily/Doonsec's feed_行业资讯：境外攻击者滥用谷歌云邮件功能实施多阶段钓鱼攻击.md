---
title: 行业资讯：境外攻击者滥用谷歌云邮件功能实施多阶段钓鱼攻击
url: https://mp.weixin.qq.com/s/sPL7aip7y3jFkFu6goOqAg
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:59:38.785817
---

# 行业资讯：境外攻击者滥用谷歌云邮件功能实施多阶段钓鱼攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sF8ZCSicrH3UTcOPmczDJeBvplCcNq2Sz5ccF14kBxK5fOibdWC02pBPYf5KCequCIuBFibpMER8axa2XriaQ0GibBA/0?wx_fmt=jpeg)

# 行业资讯：境外攻击者滥用谷歌云邮件功能实施多阶段钓鱼攻击

君说安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/sF8ZCSicrH3WYWmfDLDTqrW5PNAwrdyF8hD8H2dtYcaejKFPHJicJaxoAv7NXpDDcoz3AIg3S187nIib9khvj34dg/640?wx_fmt=jpeg)

****分享网络安全知识，提升网络安全认知！****

****让你看到达摩克利斯之剑的另一面！****

---

**“境外攻击者滥用谷歌云邮件功能实施多阶段钓鱼攻击**”****

****![](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3UTcOPmczDJeBvplCcNq2SznZbjpUfiaGuiapzBQYnoom9gyh38X3rvIjpKibJYslOudIhN87lCBLPicg/640?wx_fmt=png&from=appmsg)****

备注：图片来源于网络

---

大家好，我是Jun哥。

最近，国外网络安全研究人员网络安全研究人员期披露了多起恶性钓鱼攻击事件，攻击者借助谷歌云应用集成服务，伪造谷歌官方邮件进行大规模分发。

Check Point 安全专家指出，该攻击手法核心在于滥用谷歌云基础设施的信任背书，通过谷歌官方域名邮箱发送邮件，以此绕过传统邮件安全网关的过滤检测，大幅提升邮件送达用户收件箱的成功率。

安全机构分析表示：“攻击者仿冒企业日常运营中的各类通知场景，包括语音信箱提醒、文件访问授权申请等，利用收件人的信任心理降低其警惕性。”

监测数据显示，截至2025年12月，在为期14天的观测周期内，攻击者累计向全球约3200名企业用户发送9394封钓鱼邮件，受影响组织覆盖美国、亚太地区、欧洲、加拿大及拉丁美洲等多个区域，国内涉外企业及跨国机构存在潜在风险。

![图片](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3W4EHyUwzch09q3ZN66Ib4m1fR9eYqsIkzlzmotk53kic7VxM4dszLlNOoK8dpUkUIVkeHSk6K4Z5w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp) 攻击技术细节解析

此次攻击的核心环节是滥用谷歌云应用集成的“邮件发送”功能模块。

该模块原本用于支持用户通过集成服务发送自定义通知邮件，谷歌官方支持文档明确限制单次收件人数量不超过30人，但攻击者通过技术手段突破限制，实现向任意邮箱地址的批量投递。

值得关注的是，攻击者借助该功能从谷歌官方域名发送邮件，成功规避发件人策略框架（SPF）和基于域名的邮件认证、报告与一致性协议（DMARC）的验证机制。

这类邮件认证机制是当前企业防范邮件伪造的核心技术手段，其被绕过意味着传统邮件安全防护体系存在明显防御盲区。

Check Point安全专家团队补充道：“为进一步强化欺骗效果，攻击者严格仿照谷歌官方通知的格式规范与语言风格设计邮件内容。诱饵信息多围绕语音留言查看、共享文件访问等高频办公场景，尤其常以‘Q4报表’‘季度总结’等工作文件为诱饵，诱导收件人点击嵌入链接并执行操作。”

攻击链呈现典型的多阶段跳转特征，具体流程如下：

首先，受害者点击邮件中托管于storage.cloud.google[.]com的链接——该域名属于谷歌云官方服务，攻击者借此进一步降低用户怀疑；

随后，链接自动跳转至googleusercontent[.]com域名下的恶意页面，页面会展示伪造的图形验证码或字符验证码，既能够阻挡安全扫描工具对攻击基础设施的检测，又不影响真实用户完成验证；

验证通过后，受害者将被最终引导至非微软官方域名的仿冒Microsoft 365登录页面，攻击者通过该页面窃取用户输入的账号密码等核心凭证。

针对上述攻击行为，谷歌方面已采取紧急处置措施，阻断了攻击者对云应用集成邮件通知功能的滥用通道，并表示将持续强化安全管控措施，防范类似攻击再次发生。

![图片](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3W4EHyUwzch09q3ZN66Ib4m1fR9eYqsIkzlzmotk53kic7VxM4dszLlNOoK8dpUkUIVkeHSk6K4Z5w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp) 攻击目标与延伸风险

攻击分析报告显示，此次攻击重点瞄准制造业、科技行业、金融机构、专业服务机构及零售行业，同时也对媒体、教育、医疗健康、能源、政府部门、旅游及交通运输等领域的组织实施精准打击。

“这些行业普遍依赖自动化通知、文档共享及权限管控工作流程，使得谷歌品牌的通知信息具备天然的可信度优势。”

安全机构强调，“此次事件充分暴露了攻击者利用合法云服务的自动化与工作流功能，在规避传统仿冒手段的前提下实施大规模钓鱼攻击的新型攻击模式，给企业网络安全防护带来全新挑战。”

![图片](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3W4EHyUwzch09q3ZN66Ib4m1fR9eYqsIkzlzmotk53kic7VxM4dszLlNOoK8dpUkUIVkeHSk6K4Z5w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp) 攻击手段延伸与扩大化

安全厂商xorlab与Ravenmail后续补充披露了该攻击团伙的凭证窃取细节，其中xorlab指出，攻击者除实施钓鱼攻击外，还同步开展OAuth授权钓鱼活动，并在亚马逊云服务（AWS）的S3存储桶中部署仿冒登录页面。

xorlab分析称：“攻击者通过欺骗手段诱导受害者授权恶意Azure AD应用访问其云资源，一旦授权成功，攻击者可获取Azure订阅、虚拟机、云存储、数据库等核心资源的访问权限，并通过长期有效的访问令牌与刷新令牌维持控制权。”

值得警惕的是，整个攻击流程的每个环节均借助主流可信云服务基础设施——谷歌、微软、亚马逊等厂商的官方服务被依次滥用，导致攻击行为在各个环节均难以被单独检测和阻断。

无论初始攻击入口如何变化，最终均指向Microsoft 365凭证窃取，表明攻击者的核心目标明确锁定企业用户的M365账号权限。

信源：thehackernews

整理和翻译：Jun哥

---

**全文完****，**喜欢**请三连****，**这对我**很重要！**

---

**-End-**

******免责声明：****本文相关素材均来自互联网，仅为传递信息之用。如有侵权，请联系作者删除。******

**★****点赞，转发，设为星标**★

与你**一起分享**网络安全职场故事

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3Wbibleujm785ib7tmND84FBJjMueVpPCeQ7mSYeh9ugVYsmv5LhX1qAAI9OicjlyuvGsBrr8BiaYnv4w/0?wx_fmt=png)

君说安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3Wbibleujm785ib7tmND84FBJjMueVpPCeQ7mSYeh9ugVYsmv5LhX1qAAI9OicjlyuvGsBrr8BiaYnv4w/0?wx_fmt=png)

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