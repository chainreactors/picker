---
title: 【安全圈】AI 圈地震：月安装量约 9500 万次的 API 网关 LiteLLM 遭投毒
url: https://mp.weixin.qq.com/s/kLSaBqbeuitCvQxYskGUig
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:28:09.405441
---

# 【安全圈】AI 圈地震：月安装量约 9500 万次的 API 网关 LiteLLM 遭投毒

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGiaSmnFAqwzibSts3Re4sH5RBAvuF5YOWCOR8Qj2H96CAAM1WDXM6Nh7fafXiccnXxHeW1cF3fspktvGJFfoEUM63tNCg1pvhic3c/0?wx_fmt=jpeg)

# 【安全圈】AI 圈地震：月安装量约 9500 万次的 API 网关 LiteLLM 遭投毒

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

大模型投毒

科技媒体 cyberkendra 昨日（3 月 24 日）发布博文，**报告称月均安装量达 9500 万次的 AI 基础设施工具 LiteLLM 遭到供应链投毒。**

IT 之家注：LiteLLM 是一个开源的 AI API 网关，作为支撑数千家企业 AI 架构的关键工具，支持开发者通过统一的格式调用 OpenAI、Anthropic、Azure 等 100 多家服务商的 API 调用。

该工具于 2026 年 3 月 24 日在 PyPI 官方仓库发布了两个带有后门的版本（1.82.7 和 1.82.8）。这两个恶意版本携带了复杂的 " 三阶段 " 攻击负载：首先通过凭据收集器窃取数据，随后利用 Kubernetes 横向移动工具在集群节点间渗透，最后植入伪装成 " 系统遥测服务 " 的持久后门。

**恶意版本目前已从仓库撤下，最后一个安全版本确认为 1.82.6。**

此次投毒在技术手段上表现出极高的隐蔽性。1.82.7 版本将恶意代码隐藏在 proxy\_server.py 文件中，只要用户导入该模块，代码就会静默执行。

而 1.82.8 版本则进一步升级了破坏力，攻击者利用了 Python 的 .pth 配置文件特性。由于 Python 解释器在启动时会自动处理此类文件，这意味着恶意软件会在任何 Python 调用时触发，用户无需手动导入任何模块或进行交互，环境即会被完全感染。

黑客为了模仿 LiteLLM 的官方服务，通过伪造的域名 models.litellm.cloud 进行数据回传，而该域名极具误导性。

被窃取的数据范围极广，涵盖了 SSH 密钥、AWS 和 GCP 云凭据、Kubernetes 机密、加密货币钱包以及 CI / CD 令牌等。

LiteLLM 本身就是一个 API 密钥管理网关，黑客精准打击了这一掌握各类资源 " 钥匙 " 的核心节点。此外为规避流量检测，所有外传数据在发送前都经过了 AES-256-CBC 和 RSA-4096 的高强度加密。

安全公司 Endor Labs 调查发现，此次攻击由黑客组织 TeamPCP 发起。该组织本月早些时候曾入侵过 Aqua Security 的 Trivy 扫描器。

由于 LiteLLM 在自身的 CI / CD 流水线中使用了已被入侵的 Trivy 工具，导致 TeamPCP 获取了 LiteLLM 的发布权限，从而成功推送了带毒版本。

受影响的用户应立即采取行动以挽回损失。首先，请运行命令 pip show litellm | grep Version 确认当前版本，并检查 site-packages 目录下是否存在 litellm\_init.pth 文件。

如果确认安装过恶意版本，必须立即强制更换所有云端密钥、SSH 私钥、数据库密码及 Kubernetes 令牌。同时，建议用户将 LiteLLM 降级至 1.82.6 版本，并安全审计过去 48 小时内运行过的所有 CI / CD 流水线，确保没有残留的持久化后门。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyHZqbGbT1m1QYX7Om2icW5v2PWoBc2g0sM8FhAzyGk9uqjTvpXs9PM20a9IEIzgwqfMvfM1G6mzM0uvbRoMc8hLvePlsQwQ17ia0/640?wx_fmt=jpeg&from=appmsg)

***END***

阅读推荐

[【安全圈】马自达通报安全事件：员工和合作伙伴数据遭泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075041&idx=1&sn=ae9e793a53a8639e64c1a2ab362f1677&scene=21#wechat_redirect)

[【安全圈】朝鲜黑客滥用 VS Code 自动运行任务部署 StoatWaffle 恶意软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075041&idx=2&sn=5ef9c2fe6a9380067fe867df753048fc&scene=21#wechat_redirect)

[【安全圈】微软警告：IRS 钓鱼邮件波及 2.9 万用户，远程管理工具成攻击新载体](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075041&idx=3&sn=92dcf5afd39cf49ed5a78059f7727089&scene=21#wechat_redirect)

[【安全圈】为博眼球使用 AI 造谣“烟花厂爆炸致 2 死 2 伤”，男子被依法处罚](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075014&idx=1&sn=6aa9f243824f0e6dc0c601151e0e09a0&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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