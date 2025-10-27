---
title: 200+开发者中招！冒充DeepSeek供应链攻击：PyPI 平台恶意软件包事件警示
url: https://mp.weixin.qq.com/s?__biz=MzI1MDU5NjYwNg==&mid=2247496679&idx=1&sn=ea6bed63ed5a0044bddb23a0347d1bb3&chksm=e9fd6e76de8ae760725579de85e98b8cdea543486d135c0c2134d5acfb5c5f662ab84574c4b8&scene=58&subscene=0#rd
source: 恒脑与AI
date: 2025-02-23
fetch_date: 2025-10-06T20:37:16.686714
---

# 200+开发者中招！冒充DeepSeek供应链攻击：PyPI 平台恶意软件包事件警示

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vBt6OmTmXXB2ZTnpjj4q7lnHLHRvOqM7bZN4EuB6EiaFw6mPVGyGIkziazKwePdsxXznKZicjcQv1ldxRosHp7r2A/0?wx_fmt=jpeg)

# 200+开发者中招！冒充DeepSeek供应链攻击：PyPI 平台恶意软件包事件警示

AI前沿

恒脑与AI

**一、事件概述**

2025 年 2 月 3 日，Positive Technologies 的研究人员发现，在 Python 软件包索引（PyPI）中出现了两个恶意软件包 “deepsekai” 和 “deepseeek” 。这两个软件包名称与 DeepSeek 极为相似，明显是在冒充 DeepSeek。实际上，它们是加载了信息窃取程序的恶意软件，目标直指对 DeepSeek 技术感兴趣的开发人员、机器学习工程师和人工智能爱好者，企图窃取他们的敏感数据，如 API 密钥、数据库凭据和权限等重要信息。

经调查发现，攻击者利用了一个早在 2023 年 6 月就创建的名为 “bvk” 的账户。该账户在创建后的很长一段时间内处于休眠状态，直到 2025 年 1 月 29 日才突然活跃起来，并上传了这两个恶意软件包。

虽然在恶意行为被发现后，PyPI 迅速采取行动，删除了相关恶意软件包，但它已经被下载了超过200次，涉及美国、中国、俄罗斯等多个国家的开发者。

![](https://mmbiz.qpic.cn/mmbiz_jpg/vBt6OmTmXXB2ZTnpjj4q7lnHLHRvOqM7EP0CFKz6Hiao8Q48kicWXDeEOtwUoTgeoba4f1xVvzU0p64comb3pWeQ/640?wx_fmt=jpeg&from=appmsg)

**二、攻击手段**

DeepSeek在PyPI平台上遭遇的恶意软件包事件涉及多种攻击手法

**01恶意软件包的伪装与传播**

攻击者利用名称拼写变体的方式，在PyPI上传了名为deepseeek和deepseekai的恶意软件包，伪装成与DeepSeek相关的开发工具。这种伪装手段极具迷惑性，开发者很容易在搜索相关工具时误下载这些恶意包

**02恶意载荷的“三重收割”**

窃取环境变量：恶意软件包在执行时会提取系统环境变量中的敏感数据，包括云服务API密钥、数据库访问凭证、SSH密钥等。

回传数据至C2服务器：攻击者利用Pipedream平台作为命令与控制（C2）节点，将窃取的数据隐蔽地传输到攻击者的服务器。

持久化潜伏：代码中预留了后续加载远程恶意模块的接口，为横向渗透埋下伏笔

**03攻击者的技术手段**

恶意代码中出现了大量详细的函数注释，这些注释风格与AI编程助手（如GitHub Copilot或ChatGPT）生成的代码高度相似，表明攻击者可能借助AI工具快速构建恶意载荷

**04攻击账户的特征**

上传恶意包的PyPI账户bvk自2023年6月注册后长期处于休眠状态，直至攻击前突然活跃。这种“低信誉账户发布高关注度包”的模式是典型的供应链攻击特征

**05其他攻击手段**

除了恶意软件包攻击，DeepSeek还遭受了多种DDoS攻击，包括UDP泛洪攻击、SYN泛洪攻击、GRE泛洪攻击等。这些攻击通过消耗网络带宽和系统资源，导致服务器无法正常响应

![](https://mmbiz.qpic.cn/mmbiz_jpg/vBt6OmTmXXB2ZTnpjj4q7lnHLHRvOqM7j8GAibxaXatEfviaXBsOGxcXliciaQyzgGYibc3HDkUFwoUUAk8LI2k6HXA/640?wx_fmt=jpeg&from=appmsg)

**三、对生态的影响**

**①开发者信任受损**

开源软件是现代技术生态的重要组成部分，开发者通常依赖像PyPI这样的平台获取和使用工具。此次事件暴露了开源软件供应链的脆弱性，攻击者利用开发者对知名项目的信任，通过伪装软件包名称（如“deepseeek”和“deepseekai”）来传播恶意代码。

**②数据安全风险**

环境变量中通常包含API密钥、数据库凭证等敏感信息，这些信息一旦被窃取，可能导致开发者使用的云服务、数据库和其他基础设施资源被非法访问。受影响的开发者需要立即更换API密钥和身份验证令牌，并检查相关服务是否受到进一步损害。

**③AI技术的双刃剑**

此次事件还揭示了AI技术可能被用于恶意目的。研究人员发现，攻击者可能借助AI工具编写了恶意代码，这为AI的滥用敲响了警钟。

**④对AI生态的警示**

随着AI技术的快速发展，其相关的软件包和工具也越来越多。此次事件提醒开发者和企业，必须加强对开源软件的审查和验证，避免因疏忽而引入恶意代码。

**网络安全无小事。在享受AI带来的便利和创新的同时，我们也要时刻警惕潜在的安全威胁。**

![](https://mmbiz.qpic.cn/mmbiz_png/vBt6OmTmXXB2ZTnpjj4q7lnHLHRvOqM7oPP4MuiaGolvoqqxsAoGK4J8yF5qRxxXQsPpMGbE0mYoe1PK2TL9Plg/640?wx_fmt=png&from=appmsg)

**你有什么看法？欢迎在评论区留言分享你的观点！**

![](https://mmbiz.qpic.cn/mmbiz_png/vBt6OmTmXXB2ZTnpjj4q7lnHLHRvOqM7BxMX89ooB0qicsKD8ryAgUhGDn3Va06ZEt7AviaJJuY0dM3IYWeEgTVQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vBt6OmTmXXB4teTJe4cicFkCR5yYmhkQl8GdM82NiciaujRc9tc5UREZboCcFzIbUF0KrqKWgRqdhQ5vmBUXR9bYw/0?wx_fmt=png)

恒脑与AI

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vBt6OmTmXXB4teTJe4cicFkCR5yYmhkQl8GdM82NiciaujRc9tc5UREZboCcFzIbUF0KrqKWgRqdhQ5vmBUXR9bYw/0?wx_fmt=png)

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