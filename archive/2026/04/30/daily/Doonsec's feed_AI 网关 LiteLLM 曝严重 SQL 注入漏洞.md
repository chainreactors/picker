---
title: AI 网关 LiteLLM 曝严重 SQL 注入漏洞
url: https://mp.weixin.qq.com/s/EXpa4Mlvj4jaXPW9fGLRmA
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:37:01.202601
---

# AI 网关 LiteLLM 曝严重 SQL 注入漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/757fvrbk7oZPpM9poALtUY8gcCN51Z7N6MZNKvgPib5UNtdYhu8WjtOiaQ4d9HOInF1yT8CknLm4EvEb4cAxNFaSNdRvjPr6aoYb2JlhTCzqI/0?wx_fmt=jpeg)

# AI 网关 LiteLLM 曝严重 SQL 注入漏洞

安世加

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**新闻**

*News Today*

广泛部署于企业 AI 基础设施的开源大模型代理网关 LiteLLM 被发现存在一个严重的预认证 SQL 注入漏洞（CVE-2026-42208，CVSS 9.3）。该漏洞于2026年4月20日首次公开披露，36小时内安全研究人员即观察到攻击者在真实环境中发起定向利用。

漏洞的根源在于 LiteLLM 对 HTTP 请求头 Authorization: Bearer 的处理逻辑中，未对用户输入进行参数化查询处理，导致攻击者可将恶意 SQL 代码直接注入后端数据库并执行任意查询。由于这是一个预认证漏洞，攻击者无需持有任何有效账号或密码，任何对外暴露的 LiteLLM 实例均可在未登录状态下被直接攻击。

Sysdig 威胁研究团队监测到，攻击者并非无差别扫描，而是具有明确目标：通过列枚举技术逐步摸清数据库结构，并持续轮换 IP 地址以规避检测。攻击的核心目标是三张关键数据表——存储虚拟 API 密钥和主密钥的 LiteLLM\_VerificationToken 表、存储上游 AI 服务提供商凭证的 litellm\_credentials 表，以及包含数据库连接字符串和运行时配置的 litellm\_config 表。一旦这些数据被盗，攻击者即可以受害企业的身份调用 OpenAI、Anthropic、Azure 等高成本 AI 服务，或进一步渗透企业内部系统。

LiteLLM 作为统一接入多家大模型供应商的 AI 网关，在企业内部 AI 应用部署中使用极为广泛，尤其是将其暴露在互联网上作为对外 API 端点的场景风险最高。研究人员指出，鉴于该漏洞已被积极利用，所有运行受影响版本且对外开放的实例都应被视为"已被攻陷"进行处置，而非仅仅打补丁了事。

修复版本为 LiteLLM 1.83.7，建议立即升级，并同步轮换所有存储在实例中的 API 密钥和上游服务凭证，审计数据库访问日志排查可疑查询记录。

来源：Cyber Press / Sysdig

本公众号发布的文章均转载自互联网或经作者投稿授权的原创，文末已注明出处，其内容和图片版权归原网站或作者本人所有，并不代表安世加的观点，若有无意侵权或转载不当之处请联系我们处理！

安世加为出海企业提供SOC 2、ISO 27001、PCI DSS、TrustE认证咨询服务（点击图片可详细查看）

[![](https://mmbiz.qpic.cn/mmbiz_jpg/757fvrbk7oZM6vQ3mkLGPTCRxVBvgpHhzpB1KjGfDkShPP3DpWVk3mXv9wW8EUXnUUZlFV0ZsWhibeEa2AwVKO5bz3GBEy8msw3HiaJsPqzus/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2MTQwMzMxNA==&mid=2247540448&idx=1&sn=165f2bc3b3233827b2c601a32073aca8&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

安世加

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

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