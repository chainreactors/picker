---
title: Anthropic模型也失控了！3家企业遭静默入侵，被通知后才知晓
url: https://mp.weixin.qq.com/s/SWFOOWiJ6zq3Qlmk_Fh8PQ
source: Doonsec's feed
date: 2026-07-31
fetch_date: 2026-08-01T05:08:56.444101
---

# Anthropic模型也失控了！3家企业遭静默入侵，被通知后才知晓

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcscAWg4iaA0QibQFc5zvRfCibznLHnaIbIQcRMBSuP6vemfXBxJbZ2nvhEBf0rVAe8ic9nIUMHtezUhjwambNFiaW2XQJGKKemDgBM/0?wx_fmt=jpeg)

# Anthropic模型也失控了！3家企业遭静默入侵，被通知后才知晓

安全内参
安全内参

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

![](https://mmbiz.qpic.cn/mmbiz_jpg/wT9KAyOic0NAzO5gsrU6wSxV7QfqKN3teSphzWlOiaI4Nq65CLzkiaPavg8v3lmx3NlOxicGicnezarjImxV8kzRUsg7rdCqcp46ibuQrWTqxw6uM/640?wx_fmt=webp&from=appmsg&watermark=1#imgIndex=0)

Anthropic披露，近期针对网络安全评估任务进行安全审查，发现了3起意外事件，Claude模型接入互联网并未授权访问了3家企业的真实业务系统；

据悉，这3起事件中，一起开源软件包投毒误伤了一家安全公司，一起入侵了生产数据库，还有一起破解了一款线上应用，在官方告知前它们并未发现此次攻击活动；

尽管Anthropic与其竞争对手OpenAI一样，都极力淡化了模型失控带来的影响，但两家龙头公司接连披露此类安全事故足以引发行业警惕，防御方需要对此做好准备。

前情回顾·AI网络攻击能力动态

* [OpenAI失控模型在互联网上“游荡”了4天，并袭击了另一家AI公司](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516343&idx=1&sn=05b3383792b82d14b3194c7aee039e50&scene=21#wechat_redirect)
* [泰国财政部遭AI智能体攻陷！攻击基础设施全曝光](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516327&idx=1&sn=97a2eec5fc3226d99f3761bada1e9d77&scene=21#wechat_redirect)
* [AI失控后入侵知名企业：系OpenAI内测模型 自主逃离隔离环境](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516299&idx=1&sn=38ca1a8c468c6a566544146b9d070dd7&scene=21#wechat_redirect)
* [AI攻击真实案例验证：中国模型比美国模型更适合做网络防御](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516294&idx=1&sn=048f366500a76988235c8a1ed254b8d5&scene=21#wechat_redirect)

安全内参7月31日消息，AI巨头Anthropic日前披露，在内部安全测试期间，旗下某个Claude模型创建了一个恶意Python软件包，并上传至PyPI。该软件包在被平台自动化防御机制移除之前，已在15个真实系统上运行。

该公司称，这只是近期审查发现的3起事件中的1起。此前Claude模型从本应封闭的评估环境中访问了开放互联网，并破坏了3个组织的生产基础设施。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wT9KAyOic0NBM2LqXaMibEYAh1k3bnXjMynhOMHrPWrPk9fSvbvuvNpgpBsZDibNAXuich6f3ZrxibibPQN6AzwgVXHXiclDHpzRMUNwpw2QPt6ySA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

这次审查是在OpenAI于7月21日披露其模型逃离隔离测试环境并访问Hugging Face生产基础设施之后展开的。JFrog随后确认，这些模型是通过利用自托管Artifactory中的零日漏洞实现突破的。

开源软件包投毒误伤了一家安全公司

这3起事件均发生在通过第三方评估合作伙伴Irregular开展的夺旗演练（CTF）期间。Anthropic给Claude的提示中告知其无法访问互联网，且环境为模拟环境。但由于配置错误，这两点均不属实，两家公司直到上周才发现这一问题。

在PyPI事件中，Claude在测试环境里发现了一份文档，该文档伪装成某虚构公司开发人员的设置指南。

这份指南要求新员工安装一个从未发布过的Python软件包，即一个虚假依赖项。

Claude推断，如果它自行注册这个名称，目标机器就会自动下载其代码。

完成上传并非易事。Claude需要一个PyPI账号，注册账号需要电子邮件地址，而电子邮件地址又需要电话号码。

它未能找到免费的电话号码服务，随后尝试通过多种途径获取资金购买号码，但均告失败。最终，它退回一步，找到了一家未被阻止的电子邮件服务提供商，注册了账号，并上传了恶意软件。

Anthropic表示，该软件包在公开可用状态下存在了大约1小时。

在此期间，15个真实系统下载并执行了该软件包。其中一个属于一家安全公司，该公司经常从PyPI安装软件包并进行恶意软件扫描，其工作流程默认将软件仓库中的内容视为可以安全运行。

Claude的载荷启动后，将该公司的凭证发送至其预先设置的收集点，随后利用这些凭证进一步深入该公司的基础设施。Anthropic表示，Claude并不知道该公司的存在。

PyPI自身的安全系统自动移除了该软件包。Anthropic称，已通知PyPI团队，并提供了相关指标信息。

执行此次操作的模型是Claude Mythos 5。据Anthropic介绍，该模型在推理过程早期就发现了问题，并指出，如果互联网是真实存在的，发布该软件包将构成现实世界攻击，称其“完全不可接受，也肯定不是预期解决方案”。

随后，它又基于以下理由重新推断该环境是人为搭建的：它无法识别保护其连接安全的证书颁发机构，并且系统显示的日历日期为2026年。

当自动化扫描器开始安装该软件包时，Claude将其理解为演练中预先设定的参与者。

入侵生产数据库，攻破线上应用

最严重的影响来自一起涉及Claude Opus 4.7的独立事件。在该事件中，虚构目标公司的名称与一个真实使用的域名相同。

在4次运行中，Claude难以访问其模拟目标，在发现真实公司可以通过互联网访问后，便认为这就是预定目标。它提取了应用程序和基础设施凭证，并访问了一个存储数百行生产数据的数据库。

这是唯一一起模型在确认自己处于真实系统中后仍继续攻击的案例。Anthropic表示，4次运行最终都识别出目标是真实存在的，其中2次Claude推理认为，真实公司无论如何都应该属于演练的一部分。

第三起事件涉及一个尚未发布的内部研究模型。该模型在无法访问预定目标后，扫描了约9000个目标，随后利用暴露调试页面中的凭证以及SQL注入攻击，攻破了一个面向互联网的应用程序。该模型后来发现该主机位于一个与挑战任务无关的云账号中，判断目标是真实的，并自行停止操作。

这些攻击均未使用新颖技术。Anthropic将其归结为弱密码和未经过身份验证的端点问题。

许多企业不具备

检测AI驱动攻击的能力

Anthropic于7月23日开始审查，并在当天暂停了所有网络安全评估。公司于次日确认了这3起事件，并于7月27日通知了Irregular和受影响组织。目前，公司仍在尝试联系第三个受影响组织。

3起事件中最早的一起可追溯至4月，这意味着部分活动在约3个月内未被发现。

这些评估运行时，没有启用随公开发布版Claude模型一同提供的分类器和监控机制，不过模型仍保留了安全训练。

Anthropic表示，其生产环境中的防护措施本可以阻止这些行为，并认为这些事件更接近于测试框架和运营失败，而非模型对齐失败，因为模型被告知无法访问互联网，实际上却拥有互联网访问权限。

目前，该公司计划扩大对对话记录的监控范围，改进调查工具，并加强与评估供应商合作开展保障工作。

该公司称，正在与专注模型威胁评估的非营利组织METR讨论开展独立审查，并将在下周内发布PyPI事件运行记录的轻度删减版本。

Anthropic联系到的2个受影响组织均未自行发现这些活动。这类事件只有在负责该模型的AI实验室主动检查自身对话记录后，才会被发现。

**参考资料：bleepingcomputer.com**

文章来源微信公众号：安全内参

****END**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AAfIzicyojXwPTCxD0QGZHhyRcRicJAHhUv382sYFibICoxjzktlJwEEPag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibILU2vpTY8kPMvg2uyDyibiaFibHCDibF1vCIjn2tNAKdNicq3Y45vuYuWNUDICSF8dZ206dy1Kzrehug/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247651222&idx=1&sn=0674c7e57249a57240b5ed0fcd6cdcf2&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AApXU9ib7vkMD4KMHhjVfkTqOCUrDibUaBDoH0OGGCMasLLJyv5xppK6rA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38HPkvxLkOy5rLCeVBtj8H9SUbVPNZbibc4N2knPCDFjTKduRLhiaAZVQShUa2IZqsBShI2GG2dpqBg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

点击这里阅读原文**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

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