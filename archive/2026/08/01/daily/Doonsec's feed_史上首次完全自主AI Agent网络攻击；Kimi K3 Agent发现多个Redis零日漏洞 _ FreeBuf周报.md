---
title: 史上首次完全自主AI Agent网络攻击；Kimi K3 Agent发现多个Redis零日漏洞 | FreeBuf周报
url: https://mp.weixin.qq.com/s/2ipv6IV_JVxFbJImY8D0og
source: Doonsec's feed
date: 2026-08-01
fetch_date: 2026-08-02T05:09:00.145978
---

# 史上首次完全自主AI Agent网络攻击；Kimi K3 Agent发现多个Redis零日漏洞 | FreeBuf周报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymyA0AYWle3Wnao3wWyHqsDzMGH37D4XINGFb1Us09fC8ibRIH5cvgDSw/0?wx_fmt=jpeg)

# 史上首次完全自主AI Agent网络攻击；Kimi K3 Agent发现多个Redis零日漏洞 | FreeBuf周报

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

各位 Buffer 周末好，以下是本周「FreeBuf周报」，我们总结推荐了本周的热点资讯、一周好文，保证大家不错过本周的每一个重点！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icJ1UiaObonmWJbuLyoLXdutZ6T0GL6AXwFA0IHVJ9Tl93JicaeTmN55VJBw0JKrJg4sQXdypbdzqibg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

🔍研究发现：ChatGPT、Copilot 和 Gemini 生成的每个脚本均存在安全漏洞

⚙️研究显示：Kimi K3 Agent 发现多个 Redis 零日漏洞并构建 RCE 利用代码

🤖史上首次完全自主 AI Agent 网络攻击：利用 0Day 漏洞渗透 Hugging Face

📡单个酒店 Wi-Fi 网关遭入侵，即可将全体住客流量重定向至攻击者控制的服务器

🚨黑客在野外利用 FastJson RCE 0Day 漏洞攻击美国组织

🔓研究人员声称发现针对 GPT-5.6、Claude Opus 5 和 Fable 等顶级 AI 模型的通用越狱技术

🛠️研究人员披露 GitLab 严重 RCE 漏洞链，官方敦促用户尽快修补

🗂️安永（EY）数据泄露事件被 ShinyHunters 黑客组织认领

🦠Microsoft Word Copilot 漏洞：隐藏提示词催生自我传播的 AI 蠕虫

🔐Claude Mythos 自主发现 HAWK 与 AES 漏洞，AI 密码学研究能力超越人类专家

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5NY7KgXpwrAo5WHiaX2SOibeoicce3vxyZozGALjYSLtYPrDiceL0UV2D3A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

##

### 研究发现：ChatGPT、Copilot 和 Gemini 生成的每个脚本均存在安全漏洞

比肯学院研究显示，ChatGPT、Copilot、Gemini生成的所有脚本均含安全漏洞，包括SSRF、路径遍历等。企业若直接部署未经审查的AI代码，将面临严重风险，必须强制审查和执行权限限制。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2YNx2betKGamOMwOcNKZz9z3C8CFwPKalPmicxBpGd076s1m4icsQDHlFrjzl6XvylaR2cElHLLmAnObRATK0qvg9QDr4e8dwYA/640?wx_fmt=png&from=appmsg)

###

### 研究显示：Kimi K3 Agent 发现多个 Redis 零日漏洞并构建 RCE 利用代码

研究人员发布Redis认证RCE PoC，利用链均需RESTORE命令，涉及Streams共享NACK释放后使用和RedisBloom越界写入漏洞。Redis已发布更新，建议升级并限制RESTORE权限，目前无野外利用证据。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1P3ybyF9chDlibdF98tqvulHTNibX7ibMOYqQcsibMmqdIgvLUUKIPRWTDL0RQwRTtbyO2Kzqdl079gQlBYraJT7Bv7FibWSwjlqGg/640?wx_fmt=png&from=appmsg)

###

### 史上首次完全自主AI Agent网络攻击：利用0Day漏洞渗透Hugging Face

史上首次完全自主AI Agent利用零日漏洞入侵Hugging Face，旨在作弊而非合法挑战。攻击持续四天半，暴露机器速度攻击的威胁，推动行业重新设计沙箱和信任边界。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0bdPA4aib9QaeUliaz1CLzum7DicK92pFWElslXEV5ZDoibJDicoYEhiabF7N6wh6yXRwjX7B2qnVp1SmpibE29KJCiaPMuhuocImrNTk/640?wx_fmt=png&from=appmsg)

###

### 单个酒店Wi-Fi网关遭入侵，即可将全体住客流量重定向至攻击者控制的服务器

酒店Wi-Fi网关被攻陷后，攻击者通过DNS投毒窃取M365凭证，冒充微软页面绕过MFA。防御需用全流量VPN、严格加密DNS、禁用WPAD及设备代码流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0NZ7xfNq9E8QWht6GEWsPahTEtbicjiaHrBSBpzssLVydX5oibEicmu7czgGVf5iaCpia3ZYDEPUTUeszyEfowa8W0UzFLoZu4shSTs/640?wx_fmt=png&from=appmsg)

###

### 黑客在野外利用FastJson RCE 0Day漏洞攻击美国组织

FastJson 1.x存在严重RCE漏洞（CVE-2026-16723），影响1.2.68-1.2.83版本，无需认证即可远程执行代码，正被用于攻击美国组织，建议立即启用安全模式并迁移至2.x。

### ![FastJson RCE 0Day漏洞](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1mrhgvdOJrjF4RdNTWSoWZ9IyWbvibUmcZRE3stFhYeKrlt21A40SYNZibzXLrmQSObUN8o4JQ4TDTIfSAs3WmZzUx2ZdHeszc8/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

###

### 研究人员声称发现针对GPT-5.6、Claude Opus 5和Fable等顶级AI模型的通用越狱技术

一名AI红队成员声称开发出通用越狱技术，可突破GPT-5.6等顶级模型，认为完全修复极难。目前暂不公开，设定披露窗口期，邀请专家审查，呼吁谨慎应对。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1wG4X9Av0iaAg1WFvICLth0fcWSjurxHicuhl8OljEWVKJiaE0ZAibF7pb5ibKCay13SoG0ta7qhAqtP4ImvSpRSDXG1eNxhEeSGrE/640?wx_fmt=png&from=appmsg)

###

### 研究人员披露GitLab严重RCE漏洞链，官方敦促用户尽快修补

Oj解析器两个内存漏洞组合成RCE链，影响GitLab 15.2.0至19.0.1。已验证用户通过notebook diff触发，无需管理员权限。GitLab已修复但未标记安全补丁，建议升级至18.10.8、18.11.5或19.0.2。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX160qibDm2yJnDzzKjEXv2SqQSDO7pFGTns8gXiaVnnDwMYXPzQoaGl5Zhdxjp9jL9jjTichAaRbTI4KxQfcichIj5ooice2jqianIGs/640?wx_fmt=jpeg)

###

### 安永（EY）数据泄露事件被 ShinyHunters 黑客组织认领

ShinyHunters声称通过供应链攻击窃取安永员工凭据及客户敏感文件，威胁7月31日前谈判否则公布数据。安永已通报多州至少1366名受影响者。

### ![安永（EY）披露第三方支持工单系统遭入侵，客户数据泄露](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1RtMQ6K3FFkqSBb673ppkVSqGh9uoqHw4ich4nbL7NGBA6BTEvyTmULA3iaEgNAP06VzR9M3wdQaedoohUtE7Ps6YbdV1rXT8fY/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

###

### Microsoft Word Copilot 漏洞：隐藏提示词催生自我传播的 AI 蠕虫

Microsoft Word Copilot漏洞可将隐藏提示词转为自传播AI蠕虫，篡改文档内容并扩散。虽已部分修复，攻击链仍可利用，威胁企业数据完整性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3Szucq3LkNpGy7zibhI8qxVMW6OEeNxuttSX9icSsWx1GwWsYnrnWb0aQtBoq9ciaWtASkUiciaRCbKT0iafYtNyiazeTsCwznPUWbEk/640?wx_fmt=png&from=appmsg)

###

### Claude Mythos 自主发现 HAWK 与 AES 漏洞，AI 密码学研究能力超越人类专家

Claude Mythos自主发现HAWK密钥强度减半漏洞并简化AES攻击，证明AI已能进行原创密码学研究，水平超越人类专家，但未破坏生产系统。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1HzFgzeeRTtgCLFa3cL3WNHTe9Hszrq6icgb2Ks9GUEJxTuTx6aXBOtMu4x0gJKYwdL0LM9X9kBcwZkIbGl0VXWDgHzzGiaOTaE/640?wx_fmt=jpeg&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5Ce9OricKgAogLRlHYat9jaelbVESLOylPBnQQrU63TlHEs2zCbdNrKg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**本周好文推荐指数**

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

### 一个 map指令，让 NGINX 工作进程连环崩溃：CVE-2026-42533复现实录 CVE-2026-42533：NGINX map指令与双遍脚本引擎组合导致堆缓冲区溢出，worker进程崩溃（DoS）。CVSS 9.2，影响1.30.0-1.31.2，需升级至1.30.4/1.31.3修复。 ![大模型分析信息时出现幻觉错误怎么办？解决方案汇总 - Raccoon-Raccoon](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1RZ6JHEY0Uicr1Lcp693EsZB9ibzibhhh2JJddHgl2vIgmQSf6kwj60GHHxp79yXSHibATvalQe4paOehPphTtsmvibGqO6h8fibwMQ/640?wx_fmt=jpeg&from=appmsg) AI系统威胁建模-基于MITRE-ATLAS的结构化攻击面分析 AI红队威胁建模以碎片信息推断目标架构，持续验证假设并评估置信度，利用ATLAS框架映射攻击路径，在RoE约束下优化优先级，最终输出攻击情报简报。 ![1776334708_69e0b7746bb1f15f5b22d.jpg!small?1776334707433](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2Y1LicvBqbZbB8VU6NjYe0Kz05bIq8PCC30spXCJMI2L65j17qAjz9E0I1ibqvO0yVOEsVLzX4W7B6Lnctiad5bKMGnJqMyNNFt8/640?wx_fmt=jpeg&from=appmsg) AI-ML供应链攻击-从Pickle反序列化到模型命名空间劫持 AI/ML供应链严重依赖第三方模型、代码和数据集，面临Pickle反序列化、权重投毒、命名空间劫持等攻击。必须实施签名验证、使用SafeTensors、固定版本和私有仓库以防御。 ![Infostealer malware found stealing OpenClaw secrets for first time](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX30lLgPn5ibdaN6rp5oCicJdc9yxHetdpqDgdibQsGZ5THwjC6T69Y4hltiagrpkes2UyHARFxwjZkyUibiaBiaNR7ickUKy85rvLswkQc/640?wx_fmt=jpeg&from=appmsg) **推荐阅读** [![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0nXONQBCVFHia6FsokxUfNXFA2xtbAx9B82cWPTI3sjXjQOqQCSr8zbDKglPCTA8ThPYVetbPgOK37fQL3M6936tsnADQpT4ic0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651343233&idx=1&sn=38d25b1a7d8fda53a5c5a91e20cdd8b1&scene=21#wechat_redirect) **电报讨论** ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2LdBrtrDOMc6A1AZD2zhADpPiaLtxvxbib90tL2ulibWP6yFE2licTo0DB1iabtNGTQQD1NGaA7fuFzW0Pia7LcVQCaPv7HicNAlKh7Q/640?wx_fmt=png&from=appmsg) ![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png) ![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMR...