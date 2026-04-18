---
title: 针对Microsoft Defender零日漏洞的新概念验证利用代码发布
url: https://mp.weixin.qq.com/s/vyvfLkl-NExwWLl78qVlxA
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:25:48.383417
---

# 针对Microsoft Defender零日漏洞的新概念验证利用代码发布

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnsiapfYzmzISPemCJt6EV6jWGlaGHn6Wylju0B1GlhPcr4WV3bgLv9095UVnH6JaEabiazibwd6oOPXDgK0ibSfDhlTcTFKnbN4jT8/0?wx_fmt=jpeg)

# 针对Microsoft Defender零日漏洞的新概念验证利用代码发布

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnv1In65cH1yImU7QJWPSGX6ajib4ZpcZ2qaQIBON9CJMvfRCtLHujBr9fORP3tcHYuhlmp36oDpOR3LndbIfmGYXOOaibe0icEGsw/640?wx_fmt=png&from=appmsg)

使用化名"混沌日蚀"（Chaotic Eclipse）的安全研究员已公开发布了一个针对Microsoft Defender漏洞的概念验证（PoC）利用代码。

该利用代码于2026年4月15日发布，针对CVE-2026-33825中的漏洞，这是一个最近已修补的漏洞。这种未经协调的发布凸显了独立安全研究员与微软漏洞披露计划之间日益加剧的冲突。

此类公开发布大大缩短了安全团队在恶意行为者武器化代码之前保护系统的时间。

**RedSun利用代码发布**

这位研究员将新发布的利用代码命名为"RedSun"，并将其上传到一个公开的GitHub仓库。

此次发布遵循了同一研究者最近披露的模式，包括之前被称为"BlueHammer"的拒绝服务工具。混沌日蚀通过其个人博客上的PGP签名消息宣布了RedSun代码。

他们将此次发布描述为对微软针对CVE-2026-33825最近安全更新的直接回应。通过直接向公众提供原始代码，该研究员完全绕过了标准的行业协议。

该研究员为其决定公开披露利用代码而非与供应商公开合作提供了详细解释。

混沌日蚀声称，他们最初尝试遵循标准程序，向微软安全响应中心（MSRC）提交了漏洞报告。根据博客文章，尽管完全意识到公开披露的威胁，MSRC仍驳回了最初的报告。

该研究员指控该公司严重不当对待，声称微软积极破坏其生计并对其提交内容玩弄手段。

他们公开批评微软关于协调漏洞披露的官方立场，将MSRC的公开声明描述为轻视且脱离现实。

这一事件反映了过去独立研究员与大型科技公司在漏洞赏金评估和披露时间表上发生冲突的争议。

**未来威胁与缓解措施**

这一事件引起了依赖Microsoft Defender进行端点保护的企业安全团队的立即关注。混沌日蚀明确威胁将在不久的将来发布更严重的漏洞。

博客文章警告，与微软持续的摩擦正推动该研究员发布关键的远程代码执行（RCE）利用代码。

作者表示其意图是发布新的利用代码以破坏未来的微软补丁发布。

组织必须通过立即采取主动措施来警惕这些未经协调的发布。安全团队应实施以下防御策略：

* 立即在所有企业环境中应用针对CVE-2026-33825的官方微软补丁
* 监控网络流量和端点检测系统，查找与RedSun和BlueHammer GitHub仓库相关的签名
* 持续审查安全日志，查找与Microsoft Defender进程相关的异常活动
* 保持严格的访问控制并分割网络，以限制任何即将到来的远程代码执行利用的潜在影响

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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