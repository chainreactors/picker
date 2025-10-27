---
title: 第三方测试：AWS云原生防火墙的防护有效率仅0.38%
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513184&idx=1&sn=b6dc6e8e6a0b2acc50c58a53929f1ac7&chksm=ebfaf340dc8d7a56dc29af2fefb064e93ad83b8ca53ae17fbdcccf08b3301d85a047227b4993&scene=58&subscene=0#rd
source: 安全内参
date: 2024-11-30
fetch_date: 2025-10-06T19:16:08.036846
---

# 第三方测试：AWS云原生防火墙的防护有效率仅0.38%

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tcYCybNnTu4y4vAqICX7bx717OSEM2cOibfPXO2wde9PuZ2JxCRFBPwsicBY1QADCYJvEHJKEON5tQ/0?wx_fmt=jpeg)

# 第三方测试：AWS云原生防火墙的防护有效率仅0.38%

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tcYCybNnTu4y4vAqICX7bxWpp2wrK7iaDQaRAnLI2lLiaVnpPUictRkpgXnANBejia3ia1piaribyhRsaGg/640?wx_fmt=jpeg&from=appmsg)

**此次测试仅针对已知漏洞利用的防护能力，测试结果为依赖云厂商防火墙保护数字基础设施的企业敲响了警钟。**

前情回顾·**网络安全产品安全动态**

* [重磅！美光未通过网络安全审查，关基设施禁止采购其产品](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247508670&idx=1&sn=c918f2f48497b400931232da552890af&scene=21#wechat_redirect)
* [主张“利润高于安全”的微软产品又被黑！美国前网络高官再谈软件安全监管](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247509179&idx=1&sn=20c1238377c2f3a40bc84e1fe66e558d&scene=21#wechat_redirect)
* [谷歌爆料！微软安全功能遭绕过，对勒索软件放行](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247508093&idx=1&sn=36436766f20c05ca1723a590207e12f9&scene=21#wechat_redirect)
* [美国政府要求软件供应商为其产品自证安全将带来怎样影响？](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247505955&idx=3&sn=b66ba84115eab3f7738ff8b1e23b6064&scene=21#wechat_redirect)

安全内参11月29日消息，近日，一项云网络防火墙开放性测试的结果引发了广泛关注。

云网络防火墙的功能与传统防火墙类似，均根据预定义的安全规则监控和控制入站及出站的网络流量。与保护本地数据中心或边缘IT系统的防火墙相比，云网络防火墙还具有一些独特的特性。

在一次云网络防火墙产品测评中，美国非营利组织CyberRatings重点测试了亚马逊AWS、微软Azure和谷歌云平台（GCP）的产品。测试结果令人震惊，其中AWS的表现最差。**它相比今年4月的同类测试性能甚至有所退步，拦截常见黑客攻击的有效率从0.54%下降到0.38%**。

这些结果暴露了云原生防火墙在安全能力上的明显不足，为依赖这些工具的企业敲响了警钟，敦促他们重新审视数字基础设施的安全保护措施。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FzZb53e8g7tcYCybNnTu4y4vAqICX7bxwyp2BOf778jQzepxQyV1ZhuQcoYYicyK28yZkjMPvBXzYIicvNdY7iaug/640?wx_fmt=png&from=appmsg)

*图：测试拓扑*

CyberRatings首席执行官Vikram Phatak表示：“测试结果既令人惊讶，又在意料之中。老实说，这些产品完全没有达到我认可的任何标准。它们的表现确实很糟糕。”

**关键发现**

CyberRatings将此次测试描述为“小型测试”，**旨在评估基本功能，仅关注已知漏洞，没有涉及高级技术（如规避攻击）**。Phatak指出，这种“开卷式”的测试方法相当于提前告知厂商问题和答案，但结果仍令人失望。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FzZb53e8g7tcYCybNnTu4y4vAqICX7bx6zNF7WHib6yqhiaIOg9Uw6d0VptXuGtVVwpwq7E1ZLSRgJxGepHM8RkA/640?wx_fmt=png&from=appmsg)

*图：测试结果对比*

* **AWS的表现**

AWS仅得分0.38%，相比今年4月测试中已经令人担忧的0.54%进一步下降。尽管AWS有6个月时间解决已知问题，其防火墙产品未取得实质性改进。CyberRatings指出：“这不是单一漏洞，而是其检测方法存在根本性缺陷。”

* **Azure和GCP的表现**

这是首次对Azure和GCP防火墙进行测试，其结果同样令人担忧。尽管Azure和GCP的防火墙在某些功能上成绩尚可，但在阻止已知漏洞方面仍未达到基本预期。

测试中表现最好的GCP防火墙的保护水平仅为50.57%，而Azure的表现仅为24.14%。整体来看，三款防火墙的安全覆盖能力均严重不足。

**行业影响**

测试结果揭示了一个令人不安的现实：当前的云原生防火墙甚至无法满足基本的安全标准。Phatak表示：“企业依赖知名品牌来满足最低期望本是合理的，但这些产品远远未能达到市场需求。”

尤其是AWS未能改进的情况，引发了外界对其内部流程和核心任务的质疑。尽管6个月前已被明确指出问题所在，AWS仍未解决其网络防火墙产品的根本缺陷。这种失败反映了云安全领域的重大挑战：云环境与传统数据中心架构的差异，使得部署有效安全解决方案变得复杂。

CyberRatings强调，此次低分并非因特定漏洞或零日攻击导致。Phatak形象地说：“这不是什么零日漏洞。这就像车子的安全气囊完全没用，不是我敲三下车窗就能打开车门的问题。”

**可能的原因**

导致这些云原生防火墙表现不佳的原因可能包括以下几个方面：

1. 优先级错位：用户可能更关注其他功能增强，而忽视了安全能力的改进。

2. 资源分配不足：云服务商可能过于注重性能或成本效率，导致对安全的投入不足。

3. 组织孤岛问题：工程团队与运营团队之间的沟通不畅，可能使问题得不到有效解决。

4. 技术限制：云环境的独特架构需要专门的解决方案，而这些解决方案可能无法与传统安全框架很好地兼容。

**AWS的回应**

在被外媒SDxCentral询问回应时，AWS于11月25日发表声明，内容与其5月提供给SDxCentral的回复如出一辙。

AWS发言人通过电子邮件回应称：“AWS网络防火墙允许客户定义规则以实现对网络流量的精细控制，其运行符合设计预期。该报告不准确且不完整，我们建议客户参考AWS网络防火墙最佳实践指南，以选择适合其环境的部署方式及规则配置。”

根据Statista数据，截至11月1日，AWS在全球云基础设施即服务（IaaS）市场中占据31%的份额（多年保持领先），微软Azure占20%，谷歌云则为11%。

**对企业的建议**

Phatak指出，这些发现提醒了依赖云原生防火墙的企业，迫切需要重新评估其安全策略。CyberRatings提出以下建议：

1.考虑第三方解决方案：如Palo Alto Networks、Fortinet、Check Point和Cisco等老牌第三方防火墙供应商，在云部署中表现良好，值得评估。

2.开展独立测试：使用Azure或GCP防火墙的企业应自行进行测试，以全面了解其面临的风险。

3.要求厂商改进：企业应敦促云服务商优先解决安全问题，并提供产品功能的透明信息。

Phatak透露，CyberRatings计划在未来几个月内进行更全面的测试，评估第三方防火墙解决方案在AWS、Azure和GCP环境中的表现。这些结果将帮助企业增强云安全态势，提供更多选择机会。

随着云计算的加速普及，对原生安全工具的依赖应保持谨慎。本次报告再次提醒企业，不能默认网络安全措施已经到位，必须通过严格验证以应对不断演变的威胁环境。

**参考资料：sdxcentral.com**

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