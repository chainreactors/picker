---
title: AI风险分析 | 攻击组织在多个AWS租户环境劫持LLM模型
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247494056&idx=1&sn=4e236c890b1530189931881acd81dc9b&chksm=c18429b9f6f3a0af3f80e1754671e55d82a71e47ec29f9272b4b4a098b2589be1f97125f789e&scene=58&subscene=0#rd
source: M01N Team
date: 2025-02-02
fetch_date: 2025-10-06T20:38:02.103214
---

# AI风险分析 | 攻击组织在多个AWS租户环境劫持LLM模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7uW5SbSIevlsGntoyp9ibatU63uTe509BnKuDUnBWWdyeHu2GxzqIV1Q/0?wx_fmt=jpeg)

# AI风险分析 | 攻击组织在多个AWS租户环境劫持LLM模型

原创

天元实验室

M01N Team

![](https://mmbiz.qpic.cn/mmbiz_gif/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7I0bg90uG7iacd8J2Ay4aR3UvOBnjmRPNW5PMasRZV0Y3icCO1NLxFjdA/640?wx_fmt=gif&from=appmsg)

**背景**

随着AI技术的迅速发展，以人工智能即服务(AIaaS) 为代表的云化服务也开始被广泛使用，高价值算力集群的“诱惑”，让攻击者的“矛头”直指各类AIaaS服务。以JINX-2401为代表的组织，正在利用配置错误的云环境凭证，实现对云端LLM模型服务的非法访问与劫持，基于受害者的LLM模型服务对外构建各类AI应用程序，例如：性角色扮演的聊天机器人等，给受害者造成了每天数万美元的损失。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7beYWIiaXUHJA5gzAZ9niagrCSeCffDClKSkKZg2cSo8sFK3v348Jd0iaQ/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| **事件名称** | AI风险分析 | 攻击组织在多个AWS租户环境劫持LLM模型 |
| **风险映射** | 身份安全-应用阶段-权限管控不当/利用云凭证劫持云端模型  模型安全-应用阶段-模型越狱攻击 |
| **事件来源** | https://www.wiz.io/blog/jinx-2401-llm-hijacking-aws  https://permiso.io/blog/exploiting-hosted-models |

**01 风险分析**

AWS AIaaS提供了两种核心服务：SageMaker和Bedrock，SageMaker主要用于训练和部署各类机器学习模型，而Bedrock主要用于访问基础模型，通过单个API提供来自各类GenAI厂商的基础模型服务。

此类攻击的核心在于攻击者滥用了现有云平台的身份权限管理缺陷，通过利用已经暴露的云凭证实现对云端模型的劫持，其中使用的云凭证可能来源于社工钓鱼、Github仓库泄露、AI组件漏洞利用获取等多种渠道。攻击者在获取到云凭证后，通常会经过三个阶段来实现目标模型的劫持：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM75tia2SEN69GcQRHW5D3UdSiaPGwO7KzyAvplJ3ibMGtNzwLULyJj4AWyw/640?wx_fmt=png&from=appmsg)

* **检查模型是否可用**

攻击者首先会调用GetFoundationModelAvailability API来检查AWS Bedrock基础模型的可用性，该API会返回包括目标模型是否已授权、是否已启用，以及是否在当前AWS区域可用等关键信息；

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7YTia9WWycSIbdYKRCicmibvt10DrYGHeDEJm0x8grcIpojvF7vjgrsnRg/640?wx_fmt=png&from=appmsg)

* **获取模型的访问实例**

如果当前用户具备模型的操作权限，但模型尚不可访问，AWS提供了一系列的API开通模型实例并获取模型的访问权限，攻击者会通过AWS Web控制台或者API的形式获取模型的访问权限，主要涉及以下几个关键API：

* **PutUseCaseForModelAccess：**该API用于提交模型访问的实例表单，用于说明使用模型的组织名称、公司站点以及模型使用理由等信息；
* **CreateFoundationModelAgreement：**该API用于为基础模型创建访问协议，在正式请求访问模型之前，需要同意AWS的使用协议；
* **PutFoundationModelEntitlement：**该API用于提交模型的授权请求，以便正式获取模型的访问权限；

* **调用目标模型**

攻击者在完成模型的访问权限获取后，进一步通过InvokeModel（大模型返回整个响应内容）和InvokeModelWithResponseStream（流式响应调用）调用目标模型；

攻击者在获取到模型的访问权限后，Permiso监控到在短短的两天时间里，有超过75000次的模型成功调用，并且几乎都用于性角色扮演的聊天机器人等场景，以此获取相关收益。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7TwnpibFGhjeRgITQl1IN9RU1XjOjEoIpOV6VqQ32iaJrCurXDXPDW5aA/640?wx_fmt=png&from=appmsg)

Permiso在深入跟进提示词中暴露的线索后发现，一些社区在大量分享使用模型越狱攻击在LLM上构建性角色扮演机器人的方法，并通过开源的反向代理服务实现对Azure、GCP、AWS等模型托管服务的滥用。

**02 总结**

攻击者利用云凭证劫持云端模型降低LLM调用成本，并结合模型越狱攻击技术绕过内容安全围栏提供色情机器人服务。可以看到针对AIaaS服务的恶意利用，目前国外已经形成了一套完整的攻击流程以及巨大的市场。

随着AIaaS服务的广泛使用，攻击者逐渐将云凭证滥用的目标从传统的云存储或计算服务转向AI模型托管与调用服务，通过非法调用模型实现收益。利用云凭证劫持云端模型的攻击趋势可能会进一步扩展到国内AIaaS服务，特别是在基础模型逐步普及的背景下。国内平台需重点关注身份与权限管理漏洞以及基础模型滥用场景，并通过技术防护、管理机制等的手段实现防范，以确保模型资源的安全与合法使用。

**参考链接**

[1]https://www.lacework.com/blog/detecting-ai-resource-hijacking-with-composite-alerts

[2]https://docs.aws.amazon.com/zh\_cn/bedrock/latest/userguide/model-access-modify.html

[3]https://docs.aws.amazon.com/service-authorization/latest/reference/list\_amazonbedrock.html

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7BOyC9KsVYUYibicIr6EHib4YcuNGeuKd0H1mewbPLG0r6uI5GTIRccvKg/640?wx_fmt=png&from=appmsg)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM7FFiareyibP5lxkWZhvblXPQJ6S8tRWhKAnicfY0fyZU7M2JBr1kFn3gPA/640?wx_fmt=jpeg&from=appmsg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwbM90VWSI8dJ9EScdvqmAM74z7f5nOoL2ia5sMQJPibPLGkJFOqxmNRYV6PCs8E5B6wxvja8S3OKuUg/640?wx_fmt=png&from=appmsg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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