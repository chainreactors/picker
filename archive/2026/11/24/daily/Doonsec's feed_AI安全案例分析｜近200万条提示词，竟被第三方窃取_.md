---
title: AI安全案例分析｜近200万条提示词，竟被第三方窃取?
url: https://mp.weixin.qq.com/s/7nl21IhfYYreYU1NB2re_g
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:41:02.714137
---

# AI安全案例分析｜近200万条提示词，竟被第三方窃取?

# AI安全案例分析｜近200万条提示词，竟被第三方窃取?

原创

天元实验室
天元实验室

M01N Team

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**01 事件背景**

2026年11月19日，Dragos 首席研究官 HD Moore 发布了一项关于 AI 供应链安全的研究。研究团队在2026年7月至11月期间，向多个 AI 服务提交了近200万条包含唯一 URL 和 Canary Token 凭据的测试提示词，并持续监测这些数据在模型推理结束后的访问情况。

研究发现了三类安全问题：

* **AI服务商遭入侵：**至少三家 AI 托管服务商发生数据泄露，攻击者获取测试提示词中的 AWS 凭据，并尝试访问云资源。
* **第三方卖家窃取提示词：**AI 推理市场中的部分卖家通过请求日志获取客户提示词，无需利用漏洞。
* **隐私策略执行异常：**部分服务商未遵循客户设置的 ZDR（Zero Data Retention）策略，提示词被转发给其他组织，甚至在数周后仍被访问。

研究人员利用唯一 URL、AWS 测试密钥等诱饵数据，记录提示词提交后的访问行为，并结合请求特征追踪了约2000条 AI 推理路由。

**02 三家AI托管服务商遭入侵**

Dragos 发现，至少三家 AI 托管服务商存在数据遭窃取的证据。最早一起事件发生在2026年7月中旬，三家服务商在收到 Dragos 通知之前，都没有发现相关入侵活动。

其中规模最大的一起事件发生在10月下旬。研究人员向一家服务商提交了数百条包含 AWS 测试密钥的提示词，每个密钥只出现在一条请求中。在几个较短的时间窗口内，研究人员提交的所有测试请求均遭到复制，并且部分被窃取的请求在模型推理开始前就已经被服务商拒绝。部分请求在模型推理开始前就已被复制，泄露环节可能位于服务商的请求接入或转发层。攻击者获取 AWS 密钥后，进行了以下操作：

1. 验证密钥是否有效。
2. 枚举 AWS S3 Bucket。
3. 查询 Secrets Manager 和 Parameter Store。
4. 尝试启用 AWS Bedrock 托管模型。
5. 创建 Bedrock API Key。
6. 添加新的 IAM 用户，以维持访问权限。

Dragos 记录到，这些诱饵密钥累计触发了数万次 AWS API 调用。

![](https://mmbiz.qpic.cn/mmbiz_png/uZT6kWW1jCnhNx9PtFK1ujtd86icyy6qRTHQ4KB2hwCfxs0xpzIjUGkqqZLewD3sedvctf2frtYDc08RoCl8c1j1XEjM1jmdfVZ6icpKy7xNs/640?wx_fmt=png&from=appmsg)

图1：被窃取的 AWS Key 使用情况。研究人员于10月21日植入密钥，次日发现其被使用，三周后仍有访问活动。图中名称使用化名，部分地址经过脱敏。

另一组证据显示，同一名攻击者可能同时入侵了两家服务商。来自两家服务商的测试凭据几乎同时在同一台租用服务器上被使用。

攻击者的工具链在三周内发生了变化：

* 初期使用伪装成 Windows Chrome 的脚本。
* 随后使用运行在 OrbStack 中的 Boto3。
* 后期切换到 Kali Linux 环境中的 AWS CLI。

11月1日，攻击者开始使用 ARTEX，这是一款基于 LLM 的渗透测试框架。Dragos 观察到的 ARTEX 活动主要是验证已经获取的密钥是否仍然有效，并未发现其完成复杂的自动化攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uZT6kWW1jCngqTic1sxHtCafyqqYyF1bvMJSZ9L2NL5I3gEo7EUMbh6JovaJwoGyqcNCLbqbia8jgNsjSRaU88MEI0l5WQicibNeYBawpFQALic0/640?wx_fmt=jpeg&from=appmsg)

图2：攻击者使用的工具，包括 AI 渗透测试框架 ARTEX 和 Kali Linux 环境中的 AWS CLI。

Dragos 还指出，Kali 和 ARTEX 的部分请求会在 AWS CloudTrail 中留下 User-Agent 特征，包括 artex-agent 和 artex-judge-r121。这些特征可以作为检测线索，但只出现在少量流量中。

需要说明的是，Dragos 没有公开三家遭入侵服务商的名称。原文提到，一家服务商已经发布初步安全通告，但没有在研究报告中明确列出三家公司的身份。

**03 AI推理市场第三方卖家获取客户提示词**

第二类问题发生在 AI 推理市场的第三方卖家，卖家通过请求日志获取客户提示词，无需利用软件漏洞。部分 AI 推理市场允许第三方卖家提供模型推理服务。用户通过统一 API 提交请求，平台将请求分发给不同卖家。卖家开启请求日志后，就能够读取客户提交的提示词。

Dragos 在研究中发现，部分卖家利用这一机制获取提示词中的秘密 URL 和测试凭据。在一次测试中，研究人员通过某个卖家的模型服务提交了两条包含秘密 URL 的提示词。约一天半后，一名使用家庭宽带网络的人员通过桌面浏览器访问了这两个 URL，并开始在登录页面猜测用户名。

研究人员随后将相同模型的请求发送给另一名卖家，没有发现类似访问行为。更换卖家后，研究人员没有观察到类似访问行为，相关数据访问可能与该卖家的日志处理方式有关。

另一起事件中，一名使用法国住宅宽带网络的人员从提示词中获取密码，尝试通过 SSH 使用 root 账户登录测试服务器。研究人员观察到，对方在两分钟内手动尝试了四次密码，随后又在同一会话中测试了多组 AWS 密钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uZT6kWW1jClmYplGQ7ftu47lbty1AsIfkXBgcVhVHcKI8B4Du5ffMmCicW0P070yTtDPib9oknSibnDWWwicib9tFuCZnibE8rnoTx3fkw3KgGwTE/640?wx_fmt=jpeg&from=appmsg)

图3：攻击者尝试使用提示词中的密码登录 SSH。图中展示了密码被重复尝试的情况，以及请求经过的两个 Router。

调查还发现，另一组通过独立 Router 提交的 AWS 密钥，最终也被转发至上述推理市场。说明部分 AI Router 存在未公开披露的下游转发节点，客户从表面上看到的服务商，并不一定是最终处理提示词的组织。

**04 Canary Token怎么追踪提示词泄露？**

**为提示词植入唯一诱饵**

Dragos 从2026年7月开始使用 Thinkst Canarytokens 开展测试，之后开发了专门用于 LLM 提示词追踪的服务。研究人员为每条提示词生成唯一种子，并通过种子派生不同的域名、URL 和凭据。每条测试请求都携带独立的诱饵数据，包括：

* AWS 测试密钥；
* DNS 域名；
* HTTP URL；
* SSH 凭据；
* Git 仓库访问标识。

研究团队为这些诱饵数据部署了对应的监测服务，包括 DNS、Web、Git、SSH、数据库和邮件服务。其中 AWS 密钥采用真实格式，并关联到空白 AWS 账户，所有访问行为均保留日志。当某个 URL 被访问，或某个 AWS 密钥被尝试使用时，研究人员可以根据唯一标识回溯到对应的提示词、模型、Router 和隐私设置。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uZT6kWW1jCk4PWvWfg1NUcQRynEyGKID05xhHQSBoUVcsZ94WNJns6xFRxxogFkjMdqyyt7ic1uNJa9b9MIqEsC7UmTPZphoy5EodGzFAHSs/640?wx_fmt=jpeg&from=appmsg)

图4：Dragos Canary Token 监测控制台，展示不同日期的提示词提交量和安全事件，并按照处理请求的 Router 进行区分。

**通过请求特征追踪AI推理链路**

Canary Token 能记录诱饵数据的访问行为，但单凭访问记录无法定位具体泄露环节，Dragos 设计了一套类似网络 Traceroute 的 AI 推理链路追踪方法。

第一种方法是通过图片 URL 识别中间节点。研究人员在请求中加入指向自己服务器的图片 URL。当某个中间系统获取图片时，服务器就可以记录访问 IP、HTTP 客户端和时间戳。

第二种方法是分析 Router 返回的嵌套错误信息。研究人员构造轻微异常的请求。由于不同 Router 会使用各自的格式封装上游错误信息，一条响应中可能包含三至四层嵌套结构。

通过将这些结构与特征数据库进行匹配，可以推断请求经过的中间节点、软件组件、网络及对应服务商。截至报告发布，Dragos 已追踪约2000条 AI 推理路由，其中数百条涉及无法识别的系统。部分请求经过了公开路由信息未披露的第三方节点。部分卖家还会在每条提示词中额外添加约1000个隐藏 Token，另有卖家通过共享的消费者订阅账户获取图片。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uZT6kWW1jCmoa6jVibCVNdGbAjMeX495iaD9yrDra1y1V8wnsCEcOnqBA9I65I4oLnGibbOzDGvXXZL25ZxDXFTmenEdRYn0FiabVrtTFXNoWick/640?wx_fmt=jpeg&from=appmsg)

图5：AI 推理路由追踪示例。图中展示了从 SurplusIntelligence 到 Anthropic 的请求路径，研究人员通过追踪发现了市场页面未披露的 OpenRouter 中间节点。

**05 事件响应与安全建议**

Dragos 将异常提示词、路由信息和访问记录提供给相关服务商排查。截至报告发布，已与约12家服务商开展沟通，部分服务商启动了内部调查，一家 Router 服务商已停止相关转发行为。

针对上述问题，企业应重点做好以下工作：

1. 审查 Router 的转发配置和下游服务商，确认请求实际由哪些组织处理；
2. 验证 ZDR 配置及执行情况，检查服务日志、缓存和下游服务商是否仍保存请求内容；
3. 过滤敏感信息：在请求发送前检测并处理 API Key、云凭据、内部代码等敏感信息；
4. 对模型托管商、API 聚合平台及第三方卖家开展审计，核查数据处理、转发和留存机制。

**06 总结**

Dragos 在近200万条测试提示词中植入唯一诱饵，追踪其后续访问行为，发现 AI 推理链路中存在服务商入侵、第三方卖家读取请求日志、ZDR 策略执行异常等问题。部分提示词在提交数周后仍被访问，部分请求还经过用户未获披露的下游服务商。

这项研究将 Canary Token 引入 AI 推理链路监测，通过诱饵凭据、URL 访问记录和请求特征分析，追踪提示词在模型服务链路中的流转情况，为 AI 服务供应链审计提供了可复用的检测方法。

**关于 AISS 安全智链社区**

本案例已收录至 AISS 安全智链社区案例库，社区地址：https://aiss.nsfocus.com/#/

**参考链接**

[1] Dragos, HD Moore：Three breaches, endless leaks: Your AI supply chain needs canaries

https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uZT6kWW1jCno5BibotL6cTdT1rZhBNU9xBUzEENeribVzXJibURIxWoDNWfIQ9XWXTbDJtyoAp5GT5ib7AgxicAolcyzzCOVNMDH5LElgCTElUX4/640?wx_fmt=jpeg&from=appmsg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uZT6kWW1jCly1ROyKpMJWg6niaLnomDKsDdDbXqDEcVy6VyWb4ZPy8bRCYcwBkujSIFLvxJicicDEhF1ibIWPf2d1AfrfcKy0hFdVicaicNicbDNGo/640?wx_fmt=png&from=appmsg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

预览时标签不可点

不喜欢

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过