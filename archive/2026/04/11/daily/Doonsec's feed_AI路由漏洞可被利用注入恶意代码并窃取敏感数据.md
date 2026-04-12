---
title: AI路由漏洞可被利用注入恶意代码并窃取敏感数据
url: https://mp.weixin.qq.com/s/GfMl2I7h0Rgou8U1V2rzXw
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:43:09.666465
---

# AI路由漏洞可被利用注入恶意代码并窃取敏感数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3XJaS81ww3BViaHXQC6vC7gKu22ia16ucMqKTKn3yp0TwukGKDQyGrvlooazrelwQM0xEO28TalQjlkEwhLKkPB7wf8zxQ8jcms/0?wx_fmt=jpeg)

# AI路由漏洞可被利用注入恶意代码并窃取敏感数据

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

##

在 AI Agent 生态系统中，第三方 API 路由正成为一个关键且长期被忽视的攻击面。攻击者可将其武器化，悄无声息地劫持工具调用、清空加密货币钱包，并大规模窃取敏感凭证。

随着 AI Agent 越来越多地自动化执行高风险任务（如运行代码、管理云基础设施和处理金融交易），它们依赖名为 LLM API 路由的中介服务将请求分发给 OpenAI、Anthropic 和 Google 等供应商。

##

**Part01**

## ****危险的信任边界****

加州大学圣塔芭芭拉分校研究人员在题为《你的 Agent 归我所有：测量 LLM 供应链中的恶意中介攻击》的新研究中揭示，这些路由代表着危险且无防护的信任边界。

LLM API 路由位于 AI Agent 客户端与上游模型供应商之间，作为应用层代理运行，能够完全明文访问每个传输中的 JSON 有效载荷。与需要伪造 TLS 证书的传统中间人攻击不同，这些中介是由开发者自愿配置为 API 端点的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1YVuia2rBZh0ZkqYXPQVXHiavBOlpkKDl4ib1fgrGRDeLzFFWvibQian7By6ZFicDibNMeSXs6RAh9yIBtEJNZYltOc8sjcQqYTGzxbI/640?wx_fmt=jpeg&from=appmsg)

路由会终止客户端 TLS 连接并重新建立上游连接，使其处于理想位置来读取、修改或伪造任何工具调用有效载荷而不被发现。目前没有主流 AI 供应商强制实施客户端与上游模型之间的加密完整性验证，这意味着无法阻止恶意路由重写 Agent 执行的命令。

**Part02**

## ****恶意代码注入实践****

研究团队从淘宝、闲鱼和 Shopify 托管商店等平台购买了 28 个付费路由，并从公共社区收集了 400 个免费路由，发现：

* 9 个路由在返回的工具调用中主动注入恶意代码（1 个付费，8 个免费）
* 17 个免费路由在拦截研究人员拥有的 AWS 凭证后触发后续未授权使用
* 1 个路由清空了研究人员持有的以太坊私钥中的 ETH
* 2 个路由实施自适应规避，仅在 50 次请求后激活恶意载荷，或针对运行 Rust/Go 项目的自主 "YOLO 模式"会话

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2mrVEYqic0IcJibictaDJVvibZWcvDhsJLuiau3bQb6UltXcrpoicTYwmWXcqAgcPv1CdpiaSI9yUiatAeEHt1sBP0aI5BTYCkEYPEsgs/640?wx_fmt=jpeg&from=appmsg)

特别危险的攻击类别 AC-1（载荷注入）通过将良性安装程序 URL 或包名替换为攻击者控制的端点实现。由于被篡改的 JSON 载荷在语法上仍然有效，它能通过模式验证并避开大多数自动化安全检查。仅需重写一条 `curl` 命令就可在客户端机器上实现任意代码执行。

**Part03**

## ****路由污染实验****

威胁不仅来自主动恶意的路由。研究表明即使表面良性的路由也可能被污染：

* 在中国论坛和聊天群组故意泄露一个研究用的 OpenAI API 密钥后，该密钥生成了 1 亿个 GPT-5.4 token，并在多个下游 Codex 会话中暴露凭证
* 通过在 20 个域名和 20 个 IP 地址部署故意设置薄弱的路由诱饵，吸引了 4 万次未授权访问尝试，提供了约 20 亿计费 token，在 398 个不同项目的 440 个 Codex 会话中暴露 99 组凭证。值得注意的是，其中 401 个会话已处于自主 YOLO 模式（工具执行无需逐条确认）

**Part04**

## ****防御方案****

虽然研究者指出客户端防御无法完全验证返回工具调用的来源，但有三项无需供应商配合即可部署的缓解措施：

* 故障关闭策略门：通过仅允许本地白名单命令，以 1.0% 误报率拦截所有 shell 重写和依赖注入攻击（若攻击者将载荷托管在白名单域名仍可绕过）
* 响应端异常筛查：使用基于良性工具调用模式训练的 IsolationForest 模型，以 6.7% 误报预算标记 89% 的载荷注入尝试
* 只追加透明日志：记录完整请求/响应元数据、TLS 数据和响应哈希以支持事后取证分析（每条记录仅约 1.26 KB）

研究团队认为，要彻底解决来源验证问题，需要供应商签署响应信封——类似电子邮件的 DKIM 机制，通过加密方式将 Agent 执行的工具调用与上游模型的实际输出绑定。在 OpenAI 等主要供应商实施此类响应完整性机制前，通过第三方路由部署 AI Agent 的开发者应将每个中介视为潜在对手，并相应实施分层客户端防御。

**参考来源：**

AI Router Vulnerabilities Allow Attackers to Inject Malicious Code and Steal Sensitive Data

https://cybersecuritynews.com/ai-router-vulnerabilities/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0BoYQFaEKibEe5x5vA7Nt2y5GrK420ck8h2br3pAshqL3C2gBcBzibxicXsGkMtOdWbOAsfgfRfuaftcw8pQJTdwE0YtUQicJKavA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651336774&idx=1&sn=408127059513eb158f86aa2cfc845a5b&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3spxg6eNGaglroiaTIHUKMic8uvvkEeAsNmnn8AeHsjRKujlaUPiavLo83wZqicrvkLP3s98KWBBVmvIbicPOpAwgU4qInObvQnvwo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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