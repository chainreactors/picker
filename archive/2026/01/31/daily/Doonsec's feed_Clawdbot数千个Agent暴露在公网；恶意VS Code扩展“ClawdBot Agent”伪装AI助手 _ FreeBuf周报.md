---
title: Clawdbot数千个Agent暴露在公网；恶意VS Code扩展“ClawdBot Agent”伪装AI助手 | FreeBuf周报
url: https://mp.weixin.qq.com/s/jPwb7qMVST6kKbQ46dMRKA
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:25:04.887023
---

# Clawdbot数千个Agent暴露在公网；恶意VS Code扩展“ClawdBot Agent”伪装AI助手 | FreeBuf周报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymyA0AYWle3Wnao3wWyHqsDzMGH37D4XINGFb1Us09fC8ibRIH5cvgDSw/0?wx_fmt=jpeg)

# Clawdbot数千个Agent暴露在公网；恶意VS Code扩展“ClawdBot Agent”伪装AI助手 | FreeBuf周报

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

各位 Buffer 周末好，以下是本周「FreeBuf周报」，我们总结推荐了本周的热点资讯、一周好文，保证大家不错过本周的每一个重点！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icJ1UiaObonmWJbuLyoLXdutZ6T0GL6AXwFA0IHVJ9Tl93JicaeTmN55VJBw0JKrJg4sQXdypbdzqibg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**🤖“AI网红”Clawdbot数千个Agent暴露在公网“裸奔”**

🐎恶意 VS Code 扩展“ClawdBot Agent”伪装AI助手传播木马

✔️耐克公司就WorldLeaks宣称的数据泄露事件展开调查

🕳️SolarWinds再曝重大RCE漏洞，企业安全团队旧伤复发

🗳️微软紧急更新修复Office 0Day漏洞（CVE-2026-21509）

🛠️MEDUSA安全测试工具：集成74种扫描器与180余项AI Agent安全规则

🛡️PyTorch“安全”模式被严重RCE漏洞攻破，可执行任意代码

📕日历间谍：揭秘“间接提示注入”如何将Google Gemini变成监控工具

💻攻击者利用React2Shell漏洞（CVE-2025-55182）针对IT行业发起攻击

🐴虚假验证码攻击升级：黑客滥用微软脚本与可信服务传播窃密木马

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5NY7KgXpwrAo5WHiaX2SOibeoicce3vxyZozGALjYSLtYPrDiceL0UV2D3A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

“AI网红”Clawdbot数千个Agent暴露在公网“裸奔”

Clawdbot因默认配置漏洞导致大量实例暴露，攻击者可窃取敏感数据。漏洞源于认证逻辑与部署模式冲突，本地开发配置误将外部请求视为本地流量。官方已更新安全指南，用户需立即加固防护。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38JdicabhF81Im3gEDpQN7BFuTkQonJPOlicPjWaYdbW3O8Vr8UMeZTH8Xe1Td1mxfj0wesHK2CUicxA/640?wx_fmt=png&from=appmsg)

恶意 VS Code 扩展“ClawdBot Agent”伪装AI助手传播木马

###

AI编程助手热潮引发新型攻击，恶意VS Code扩展"ClawdBot Agent"伪装成热门工具，表面提供AI功能实则植入木马。攻击者精心设计界面和功能，利用真实API麻痹用户，通过复杂C2架构实施攻击。虽被及时下架，但警示开发者需核实工具真实性。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF8ObPrzvVD430Wo17hxNK8FtQPSZWQCHNK00HS1PQbxYpa7N5DFoZmkA/640?wx_fmt=png&from=appmsg)

###

耐克公司就WorldLeaks宣称的数据泄露事件展开调查

###

###

###

网络犯罪组织WorldLeaks宣称窃取耐克1.4TB数据，耐克正调查。该组织由勒索转型为纯数据窃取，已入侵数百机构。运动品牌频遭攻击，Under Armour此前7200万客户数据泄露。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR388AGxy8tNdrUb1ia7DfM1X4PRrP4ouKibthiamxq8TIrdC5BkQbicQBDBxdTQicHI1fQqjpfxfV97H6TQ/640?wx_fmt=png&from=appmsg)

###

###

###

SolarWinds再曝重大RCE漏洞，企业安全团队旧伤复发

SolarWinds旗下Web Help Desk软件曝出6个高危漏洞，含4个严重级RCE漏洞，攻击者可绕过认证执行远程代码。专家警告漏洞极易被利用，企业须立即升级至2026.1版本。这已是该产品近年第三次重大漏洞，凸显代码质量问题的紧迫性。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF8iaKHD0q0ODaicQh8huf7gzB8GeIMTudxlNZZC4I5eNZMLEGlCdttiaZIQ/640?wx_fmt=jpeg&from=appmsg)

微软紧急更新修复Office 0Day漏洞（CVE-2026-21509）

###

###

###

###

###

微软紧急修复Office 0Day漏洞（CVE-2026-21509），影响多个版本，攻击者可利用恶意文件绕过安全机制。建议用户及时更新或手动修改注册表防护。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38p1qHebKib5H8RBpPYAibsIcQnVibbj299J5ST1yqbFjwYLoqug27tqWUubDh7v4dDgayJMbcTxrXfg/640?wx_fmt=png&from=appmsg)

MEDUSA安全测试工具：集成74种扫描器与180余项AI Agent安全规则

MEDUSA是一款高效开源SAST工具，支持42种语言，配备74个扫描器和180+AI安全规则，大幅降低误报并提升扫描速度10-40倍。专为AI安全设计，覆盖OWASP LLM风险，集成CI/CD，47秒可扫描145个文件，确保开发安全。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF8QBOkWKlVsYOPvfjLgHgvtTNIe9Hzib4VPySVgH0aBDqNeV7aQYdaqZg/640?wx_fmt=jpeg)

PyTorch “安全”模式被严重RCE漏洞攻破，可执行任意代码

PyTorch修复高危漏洞（CVE-2026-24747，CVSS 8.8），其weights\_only=True反序列化器存在缺陷，可导致任意代码执行。影响2.9.1及之前版本，建议立即升级至2.10.0修复版本。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF876TNxo0fbbPMpA1Ra5ibdZu2ib0gPec16lJdxOcxLaZNgibiavPvpFcWibw/640?wx_fmt=png&from=appmsg)

日历间谍：揭秘“间接提示注入”如何将Google Gemini变成监控工具

###

###

###

###

研究人员发现Google Calendar存在"间接提示注入"漏洞，攻击者可通过日历邀请隐藏恶意指令，诱使Gemini AI泄露私人会议数据。该漏洞利用自然语言绕过现有防御，凸显AI时代语义攻击的新威胁，需开发基于意图识别的防护系统。

![Google launched a powerful new AI model Gemini](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF8DSkK9LtIqzzYKIeoEvew4rbquZFG1tyaHfL0R6tk55D2ukhRbv0gVg/640?wx_fmt=png&from=appmsg)

攻击者利用React2Shell漏洞（CVE-2025-55182）针对IT行业发起攻击

###

###

###

###

威胁行为者利用React2Shell漏洞（CVE-2025-55182）攻击保险、电商和IT行业，通过不安全的反序列化执行恶意代码，投放挖矿程序和僵尸网络。补丁已发布，但需检查系统是否被入侵。建议更新依赖项并限制实验性功能使用。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38JdicabhF81Im3gEDpQN7BF4ibjoNKc6KprDK5yvYFJbYLp492Cvo7nibSOBbv8vMnFxH0LwDLjN6Lg/640?wx_fmt=png&from=appmsg)

虚假验证码攻击升级：黑客滥用微软脚本与可信服务传播窃密木马

###

###

###

###

###

黑客利用微软签名脚本SyncAppvPublishingServer.vbs结合虚假验证码传播Amatera木马，通过企业版系统组件规避检测，并借助Google日历等可信服务动态配置攻击链，使防御和分析更困难。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF8UmrOeKY13KkTdPibQy2zIZliciblrSzwWob8HLT1oDs6C96X5F6TAia5aQ/640?wx_fmt=jpeg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5Ce9OricKgAogLRlHYat9jaelbVESLOylPBnQQrU63TlHEs2zCbdNrKg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**本周好文推荐指数**

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

OWASP Top 10 十年技术演变：从代码注入到云原生供应链的攻防博弈

###

###

### 技术栈演进重塑攻击面：从应用层漏洞转向供应链、云配置和内核层威胁。访问控制、安全配置错误和软件供应链问题成为核心风险，需全栈防御体系应对。攻击面下沉至构建流水线、容器和开源依赖，防御需覆盖代码、依赖、配置和运行时层。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF8zYdq5gHjkicfO5ZYHGzuhUyKVicjRcqgnLPib33XpMe3t03OpkfUNB28g/640?wx_fmt=jpeg&from=appmsg)

###

启用Canvas后，Gemini 3.0安全性降级了？

###

###

### Gemini 3.0 Pro安全测试显示其整体防护优于前代，但复杂场景仍存风险。编码越狱攻击部分失效，但Canvas功能导致安全降级。RAG抗投毒能力提升，沙箱防护稳固。需警惕多轮对话泄露敏感信息，安全需持续迭代。

### ![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF8ZPbyK2ctBcdcic5Fg7lbTuHAnbVsTB4dBbbPhDPcianzYEC4JEothN8Q/640?wx_fmt=jpeg&from=appmsg)

权限与身份欺骗类攻击：比漏洞利用更致命的企业内网威胁

###

###

###

### **企业安全防护需从传统漏洞管理转向身份安全，60%入侵源于凭证滥用而非漏洞。攻击者通过窃取合法凭证绕过防护，行为在日志中"完全合法"，极难发现。防御需构建Zero Trust架构，引入身份行为分析、权限最小化和凭证生命周期管理，识别"合法但不合理"行为。**

### ![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF8dr0OZIsniaaoYRibGgsON4j6ETKD66thuN48ckG1IoMXwQHjwAtHqichQ/640?wx_fmt=png&from=appmsg)

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF8tTYRNsg6a0FfibX0r25TSibsMNZQhtboVibXRZU0vs9tRR2kk7BHa4oFQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334591&idx=1&sn=7a53f598d945f86ed376200b93146133&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLq7T2qZrtcsoq5PRQ2cjDU1HUaakGzExOsSIU2Quxiasf7W9ibLiaEsmWA/640?wx_fmt=png&from=appmsg)

###

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)**

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38TJMDLxr9EPGGib49oQymrvRy7vGw1iakQXBCr1Udmia4dpY3JSWYEEicajmhhcyfHly9YYPIziaCVPOg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

内容含AI生成图片

阅读原文

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