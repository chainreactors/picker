---
title: 【安全圈】“本地回环”成突破口：Clawdbot 默认配置漏洞导致上千实例暴露公网
url: https://mp.weixin.qq.com/s/XungM38kKV8Ptuf4Q5JZew
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:16:23.140085
---

# 【安全圈】“本地回环”成突破口：Clawdbot 默认配置漏洞导致上千实例暴露公网

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyEUNng04IicIyPYsxkmzbicU5iaFHQFEyeuhqSMewialKhlXeXC22YX6Y7LNG8fI6ial7bkSRHqGzzheXbQp3M013SicKr2ZhIV61AsQ/0?wx_fmt=jpeg)

# 【安全圈】“本地回环”成突破口：Clawdbot 默认配置漏洞导致上千实例暴露公网

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

Clawdbot

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyHZP7BD9KsbE3PXx5MDcUCH7dVEmMnCWh9ibMSbDLr7fAvrw1ukonDdvU7PP9hM9vVPToIsCPEbce084V4JZ68Z9uxbBOLiaU27Q/640?wx_fmt=png&from=appmsg)

近期在社交平台走红的 AI 助手工具 Clawdbot，正在被大量用户部署在 Mac mini、容器环境以及 VPS 服务器上。然而，随着使用规模快速扩张，一个危险现象也逐渐浮出水面——大量实例因默认配置问题直接暴露在公网，成为可被扫描和接管的目标。

安全研究人员发现，问题并不在复杂的零日漏洞，而在一个看似“理所当然”的本地信任逻辑上。

**超过 1000 个实例可被公网访问，数百个无认证保护**

根据 O’Reilly 网络安全社区的调查结果，目前通过公网扫描可访问的 Clawdbot 实例超过 1000 个，其中至少 300 个完全没有任何身份验证机制。

Clawdbot 本身具备较高权限，通常持有多个第三方服务的 API 密钥或访问凭证，堪称“数字管家”。一旦实例被未授权访问，攻击者不仅可以操控其执行命令，还可能借此窃取用户数据、滥用集成服务，甚至作为跳板进一步横向移动。

问题的根源出在 Clawdbot 的认证机制与部署方式之间的“错位”。

**“localhost 信任”在生产环境被错误放大**

在默认的本地开发环境中，Clawdbot 控制界面会对来自 localhost（127.0.0.1）的请求自动放行，这是为了方便开发调试。正常情况下，外部访问应当经过身份验证流程，包括设备标识与挑战响应机制。

但当用户将 Clawdbot 部署到生产环境，并通过 NGINX 或 Caddy 等反向代理对外提供服务时，所有流量在应用层看到的来源 IP 都变成了 127.0.0.1。

结果是：来自公网的请求被错误识别为“本地访问”，认证逻辑被绕过，攻击者可以在无需登录的情况下直接执行命令。

这类问题并非传统意义上的代码漏洞，而是典型的“部署安全误用”。但在 AI 代理类产品中，其风险被进一步放大。

**高权限 AI 代理一旦失守，后果远超普通 Web 服务**

Clawdbot 具备调用系统命令、访问文件、读取凭证、连接外部 API 等能力。一旦被接管，攻击者可通过提示注入、指令篡改等方式操纵代理执行恶意任务。

如果该实例连接了代码仓库、云服务、数据库或自动化流水线，攻击面将进一步扩大。攻击者甚至可以利用代理“合法通道”进行数据外传，而不触发传统入侵检测规则。

这种“功能即攻击面”的风险，正在成为 AI 自动化工具的共性安全挑战。

**官方已更新文档，社区推动修复**

安全社区已向 Clawdbot 提交 Pull Request，改进默认配置逻辑，并增强对反向代理场景的识别能力。官方文档也已更新，明确强调在生产环境中必须正确配置代理头部（如 X-Forwarded-For）并启用严格认证机制。

对于已经部署 Clawdbot 的用户，建议立即自查：

* 确认实例是否暴露公网
* 检查是否存在认证绕过风险
* 核实反向代理是否正确传递真实客户端 IP
* 禁止对 0.0.0.0 开放管理接口
* 限制管理端口仅允许内网访问

AI 工具正在快速进入个人与企业生产环境，但“默认可用”不等于“默认安全”。这次 Clawdbot 的暴露事件再次提醒我们——在 AI 代理具备系统级权限的前提下，任何一个本地信任假设，都可能成为真正的“前门漏洞”。

在部署 AI 助手之前，先把门锁好。

***END***

阅读推荐

[【安全圈】CVE-2026-1868：GitLab AI Gateway 严重漏洞（CVSS 9.9），可致远程代码执行](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074106&idx=1&sn=72e574f6313d73bd75cec9f20e036c27&scene=21#wechat_redirect)

[【安全圈】假 AI 助手暗藏木马：恶意“ClawdBot”插件潜伏 VS Code](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074106&idx=2&sn=35bf2ad947c8809281fbfe2d1b3ccd9a&scene=21#wechat_redirect)

[【安全圈】印度最高法院裁定：WhatsApp 不得以数据共享侵蚀用户隐私](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074106&idx=3&sn=ebfc6c6db3752b75c2267fac40b20c6d&scene=21#wechat_redirect)

[【安全圈】法国全面弃用 Zoom 和 Teams：主权视频平台“Visio”落地，数字主权进入实战阶段](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074106&idx=4&sn=d1170311a7623b6060a3294af3b28da2&scene=21#wechat_redirect)

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