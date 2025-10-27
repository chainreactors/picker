---
title: 事件响应必备：DNS攻击与防御矩阵
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247508005&idx=2&sn=439441a777df8d0de859aec74b2564d8&chksm=ebfae705dc8d6e13c5f2f4f49ec37b8ae318746994af5ddcc9452641e2218817dd9abffffbbe&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2023-03-08
fetch_date: 2025-10-04T08:55:27.212522
---

# 事件响应必备：DNS攻击与防御矩阵

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tL1ucq8VVgvSyje00apAgaDuiaYLfUicDzarPG0p2jP6yPBRI0lJYwyH8zLPgUdQcRJa3XaP1ibY1AA/0?wx_fmt=jpeg)

# 事件响应必备：DNS攻击与防御矩阵

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvbCgdx2mjc9nxVAzKTX4RhOTY7I8o4CrVIDYpMUGNlibDJFbxh6bdffljFYhwNtZ8Ks4w0JlnmkUug/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**攻击者采用了哪些DNS攻击技术，哪些组织可以帮助事件响应团队检测、缓解和预防这些技术？FIRST近日发布的DNS攻击与防御矩阵提供了答案。**

DNS作为互联网基础架构的一项核心服务，安全问题严峻，各种攻击层出不穷。F5发布的数据显示，DNS/DDoS攻击已经成为主要网络安全威胁之一。并且攻击手段逐渐变得复杂和隐蔽，如DNS隧道、DNS流量劫持攻击等，对网络安全和数据隐私提出了更高的要求。

不仅是攻击技术的多样化和复杂化，DNS攻击的检测、缓解和预防所涉及的实体和措施同样趋于复杂化，这给处理DNS攻击事件的企业事件响应团队带来不小难度。

面对以上挑战，由来自政府、商业和教育组织的计算机安全事件响应团队(CSIRT)组成的协会FIRST推出了DNS攻击与防御矩阵。

FIRST目前在全球拥有600多名成员。在众多特殊兴趣小组(SIG)中，DNS滥用兴趣小组负责编制了DNS攻击与防御矩阵。

“CERT不断接到雪片般飞来的DNS滥用报告，同时又严重依赖DNS分析和基础设施来保护网络。”DNS滥用兴趣小组指出：“DNS攻击与防御矩阵从全球事件响应社区的角度解读检测和缓解DNS滥用的国际习惯规范，这对于开放互联网的稳定性、安全性和弹性至关重要。”

**21种DNS攻击技术**

DNS攻防矩阵定义了21种DNS滥用技术，包括DNS欺骗、本地递归解析器劫持、DNS作为拒绝服务攻击载体或命令控制通信通道、二级域名恶意注册等。

为帮助用户、事件响应团队和不同利益相关者提升DNS安全事件响应效率，DNS攻击防御矩阵提供了“检测”、“缓解”和“预防”三个版本。例如，在DNS缓存中毒事件中，事件响应团队可以通过“缓解矩阵”查看哪些实体可以帮助缓解事件。”

以下为三个版本的局部截图：

**检测：**

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvbCgdx2mjc9nxVAzKTX4RhOUmDuq7TIxCej79b59taicQsMhsiaRbN2MG00n4sibaFfJiaLbNwfBlEJHw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**缓解：**

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvbCgdx2mjc9nxVAzKTX4RhO1AhXDc5NRiaF5V9kbEOtLMf7uCj45e4YYWVicNA8LWlD38WcfYNPWtAw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**预防：**

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhvbCgdx2mjc9nxVAzKTX4RhOfYubVvhYzKb5jjpDJ6J8JgE2waQ9VkbJiabl1tuWNsJhvWjjDicsBj5w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

DNS攻防矩阵涉及的实体（利益相关者）包括从注册商、注册管理机构和各种提供商（托管、应用程序服务、威胁情报）到CSIRT和ISAC（信息共享和分析中心）以及执法和公共安全机构的所有DNS安全利益相关者。

值得注意的是，DNS攻防矩阵目前不包括攻击者可能与DNS攻击技术结合使用的其它技术，也没有涵盖事件响应者在处理DNS攻击时可以探索的相关政策、政府和司法途径。

**DNS安全五大趋势**

未来，DNS安全将呈现以下五大发展趋势：

（1）全球化趋势：DNS安全问题是全球性问题，需要全球范围内的安全协作和共享，未来DNS安全将更多呈现国际化、全球化的趋势。

（2）多维度保护：未来DNS安全需要多种技术手段的协同应用，例如DNSSEC、HTTPS等，将多个安全点的保护形成全面地多维度保护。

（3）智能化趋势：随着人工智能和机器学习技术的不断发展，未来DNS安全将更加智能化、自适应和自我防御。

（4）DANE与DoH趋势：新兴的DNS技术DANE和DoH，它们可以帮助解决DNS缓存污染、欺骗、劫持等问题，未来会越来越多地应用到实际领域。

（5）强调人员教育：未来DNS安全也将越来越重视人员教育，为管理员和用户提供更好的安全意识和知识，使他们能够更好地应对DNS安全挑战。

DNS安全是互联网安全的重点之一，随着互联网快速发展，未来DNS将更加全球化、多维度、智能化，DNS安全防御也需要不断引入新技术、新手段，加强协作和共享，本文介绍的DNS攻击与防御矩阵也将随之更新和扩展，是事件响应团队必备的参考工具之一。

参考链接：

*https://www.first.org/global/sigs/dns/DNS-Abuse-Techniques-Matrix\_v1.1.pdf*

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：GoUpSec

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