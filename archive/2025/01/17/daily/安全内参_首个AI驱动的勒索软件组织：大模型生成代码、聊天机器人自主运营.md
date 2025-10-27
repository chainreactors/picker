---
title: 首个AI驱动的勒索软件组织：大模型生成代码、聊天机器人自主运营
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513518&idx=1&sn=fe28a4824b27c5537d65babed6d5c44f&chksm=ebfaf28edc8d7b9869d2b2b4b8daeb1905fb01803f567a2477bfe3f226caaea259ca1fa79638&scene=58&subscene=0#rd
source: 安全内参
date: 2025-01-17
fetch_date: 2025-10-06T20:10:43.527506
---

# 首个AI驱动的勒索软件组织：大模型生成代码、聊天机器人自主运营

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s5ZMBEzppn6MON12KN9XnRtchWibG6kDwoWnSqDdhwOwyKKVTc6wsMcF8Vp53mvMaX1N6h7wnoPtg/0?wx_fmt=jpeg)

# 首个AI驱动的勒索软件组织：大模型生成代码、聊天机器人自主运营

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7vS26DErGnT6P4KxjbKQRgU6yEXxCkEl1GswhwWS6UHrWibA4eQrG6En7gn8ghL0TNd7qxnW8x67iag/640?wx_fmt=jpeg)

**据安全厂商披露，FunkSec勒索软件组织使用AI支撑多项事情，如生成代码、自主运营等；**

**据分析，FunkSec的成员缺乏经验，依赖于被重复使用的攻击战术，技术能力有限，预计很难长期存活。**

前情回顾·**大模型网络攻击能力动态**

* [攻击者绕过微软OpenAI云安全护栏，对外售卖违规内容生成服务](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513487&idx=1&sn=2bb2b3796dd10a13b4a3bf0ae256a199&scene=21#wechat_redirect)
* [首次利用大模型发现内存安全零日漏洞 (附大模型挖洞经验)](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512989&idx=1&sn=3db390e902ccf6b370d33cf57039a63b&scene=21#wechat_redirect)
* [首次利用大模型在真实环境发现十余个零日漏洞](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512862&idx=1&sn=985a72021a5e4cbab44d293299fed951&scene=21#wechat_redirect)
* [警惕！全球APT组织正在使用大模型辅助网络攻击](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247511272&idx=1&sn=15a7c41e7d5356987f0515a847603f23&scene=21#wechat_redirect)

安全内参1月16日消息，研究人员发现，一个名为FunkSec的新兴勒索软件组织，声称在1个月内攻击了超过80名受害者，这一数字在去年12月超越了其他任何威胁行为组织。

根据网络安全公司CheckPoint的最新报告，该组织于去年年底首次出现，可能由缺乏经验的黑客组成，这些黑客试图通过攻击行为寻求曝光和认可。

研究人员指出：“该组织泄露的许多数据集实际上是从之前的黑客活动中回收得来的，这让人对其披露的真实性产生了质疑。”

FunkSec向受害者索要的赎金金额异常低，有时仅为1万美元。其受害者主要分布在美国、印度、意大利、巴西、以色列、西班牙和蒙古。此外，该组织还将窃取的数据打折出售给第三方。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s5ZMBEzppn6MON12KN9XnRyaLsw3pPqDHdaCRY82U9qvOToo7Avs3d8r465yWaw2qSRpMdkBC9jg/640?wx_fmt=jpeg&from=appmsg)

*图：FunkSec勒索门户网站*

FunkSec网站上列出的受害者包括一家旅游预订公司、一家能源管理服务提供商以及一家家用电器销售公司。然而，这些公司均未公开证实自己遭受了所谓的攻击。

该组织最新版本的勒索软件被命名为FunkSecV1.5，据推测，其创建者可能在阿尔及利亚上传了该软件。该恶意软件包含了一些疑似借助人工智能创建的元素。

研究人员表示，开发者可能利用AI快速开发和优化工具，以弥补其“明显缺乏技术专业知识”的不足。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s5ZMBEzppn6MON12KN9XnRQb7vGZxOIEOjN7NvK4zlmlxK4dWqFUG9HJEr2XV3ouQQ3hd1Pia6Wiag/640?wx_fmt=jpeg&from=appmsg)

*图：疑似AI生成的代码注释*

例如，该组织可能使用AI编写了代码注释。这些注释使用了完美的英语，与其在其他平台上使用的非常基础的英语形成了鲜明对比。此外，FunkSec还推出了一个AI聊天机器人，用于支持其运营。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s5ZMBEzppn6MON12KN9XnRcZiae8ylLCKa9YD8Tzib8mCaJDXkAPyCiaYAyDGcWicmVv44ZROH5hBwIQ/640?wx_fmt=jpeg&from=appmsg)

*图：自主运营的聊天机器人*

根据报告，FunkSec的真实动机尚不明朗，其活动特点兼具黑客主义和网络犯罪的特征。

除了勒索软件，该组织还提供与黑客主义活动密切相关的工具和服务，包括分布式拒绝服务（DDoS）攻击服务、远程桌面管理工具以及密码生成工具。

该组织的一些成员此前曾参与过黑客主义活动。他们还声称以印度和美国为目标，并公开表示支持“巴勒斯坦解放”运动。同时，FunkSec试图与已解散的黑客主义实体（如GhostAlgeria和Cyb3rFl00d）建立关联。

研究人员补充道：“这些关联更可能是FunkSec试图通过与知名组织挂钩来提升其可信度，而非实际表明其成员身份或合作关系。”

FunkSec的出现恰逢勒索软件活动和黑客行动频繁的一年。尽管该组织发展迅速，但行业专家对其长期生存能力表示质疑，因为它依赖于重复使用的战术，技术能力也十分有限。

**参考资料：therecord.media**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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