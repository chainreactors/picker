---
title: 黑客组织滥用google服务进行网络钓鱼攻击活动
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492508&idx=1&sn=292b43e2f759d1aef5a11e2bafbfbfab&chksm=e90dc9b6de7a40a02a0de09e4be4c650c66a180e209fa2ae5901d06c4ba93051121277cc2418&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2025-01-05
fetch_date: 2025-10-06T20:08:38.443817
---

# 黑客组织滥用google服务进行网络钓鱼攻击活动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 黑客组织滥用google服务进行网络钓鱼攻击活动

BaizeSec

白泽安全实验室

随着电子商务的蓬勃发展，网络钓鱼和数据窃取活动日益猖獗。黑客组织不断寻找新的方法来绕过传统的安全防御检测措施，以获取敏感信息，如信用卡数据、个人身份信息和其他财务信息。在最近的一系列攻击活动中，网络安全厂商Sansec Research 发现黑客攻击者开始滥用谷歌提供的服务，包括Google Translate和Google APIs，来隐藏他们的恶意攻击行为，并绕过传统的网络安全防护措施，以执行恶意JavaScript文件和窃取用户数据。

**一、Google Translate的滥用**

攻击者利用Google Translate的页面功能执行恶意JavaScript文件。通过设置目标语言为古吉拉特语（gu）和源语言为英语（en）。由于古吉拉特语使用不同的脚本时，拉丁字符保持不变，因此攻击者能够保持恶意脚本拉丁字符不变，使Google Translate成为传递恶意内容的便捷代理。例如，以下代码片段展示了如何通过Google Translate传递恶意脚本：

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIM805GcHuBRpPzBZBS8DaGOZCQWWsSkI7MFdOS7xtpZ56KeiaSibzEWsvHR4jHnWEX42w9RR7MlaRWA/640?wx_fmt=png&from=appmsg)

该脚本连接到一个命令和控制（C2）WebSocket端点：https://udalzira.com/.well-known/cloud.jswss://cloudflare-stat.net/common?source=。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIM805GcHuBRpPzBZBS8DaGO2CoJwBMbuaVUCZG5VGicmhIibzlMNJicKibZSLVcPBmApnX9zwRGzCV08A/640?wx_fmt=png&from=appmsg)

这一技术被归因于Surki Group，该组织是近期感染数千系统的实施者。

**二、JSONP回调的滥用**

多个谷歌服务允许使用带有callback参数的JSONP格式。即使回调名称无效，它仍然被嵌入在响应中。例如，URL返回：https://www.youtube.com/oembed?format=json&callback=alert(%27sansec%27);

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIM805GcHuBRpPzBZBS8DaGOEcFwYenYBgLyLLN4hdbY0hpmrPFbC4uxicsSYxXgV29UU8TygdoR9nQ/640?wx_fmt=png&from=appmsg)

返回的响应虽然包含错误信息，但仍然是有效的JavaScript代码，因为错误消息被封装在括号中并遵循JavaScript语法。JSONP技术被用来绕过CSP（内容安全策略），如JSONBee等工具演示了使用JSONP技术绕过CSP这种方法。最近的窃取信息活动越来越多地采用这种方法来规避安全措施。

**三、YouTube和Google APIs的滥用**

JSONP漏洞的一个显著例子涉及YouTube的oEmbed功能，该功能在10月份绿湾包装工专业商店遭到入侵。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIM805GcHuBRpPzBZBS8DaGOdns2DxrTK4K4Amzpeaub3yF9r9ia0SXje7lKprbWkicwQQrDzYQd2djw/640?wx_fmt=png&from=appmsg)

在这次攻击中，从https://js-stats.com/getInjectorinputselecttextarea注入了一个脚本。这个脚本从网站上的input、select和textarea字段中收集数据，并将捕获的信息泄露到https://js-stats.com/fetchData。。

另一场窃取信息活动滥用了Google Discovery API中的JSONP回调：https://translate.googleapis.com/$discovery/rest?version=v3&callback=eval(...)。这场攻击至少针对了十几个在线商店。恶意脚本加载了一个托管在https://montina.it/mx/stripe/的假Stripe支付表单。对假表单的源代码分析发现了与Group Polyovki黑客组织（是知名的Magecart黑客组织的分支）常见的关键词有相关关联。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIM805GcHuBRpPzBZBS8DaGODwEiatwDU44N0Pia30vd8dtwQPULBIQFv6SX0ZeXibFTwt4DfaA7Y5D8A/640?wx_fmt=png&from=appmsg)

几周后，攻击者开始滥用Google Accounts OAuth2 API，使用以下端点：https://accounts.google.com/o/oauth2/revoke?callback=eval(...)。假支付位置切换到https://premium.vn/bb/stripe。这一后续活动影响了近100个在线商店。这些攻击活动不仅对受影响的企业和个人用户造成了直接的经济损失，还对整个电子商务生态系统的信任度造成了损害。

参考链接：

https://sansec.io/research/google-services-abused-skimming-campaigns

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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