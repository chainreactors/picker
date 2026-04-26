---
title: Claude Mythos安全神话：炒作还是名副其实？；白宫拟开放Claude漏洞挖掘AI | FreeBuf周报
url: https://mp.weixin.qq.com/s/2EQYYSa6HEcGEvEtIE4c5Q
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:56:49.324901
---

# Claude Mythos安全神话：炒作还是名副其实？；白宫拟开放Claude漏洞挖掘AI | FreeBuf周报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymyA0AYWle3Wnao3wWyHqsDzMGH37D4XINGFb1Us09fC8ibRIH5cvgDSw/0?wx_fmt=jpeg)

# Claude Mythos安全神话：炒作还是名副其实？；白宫拟开放Claude漏洞挖掘AI | FreeBuf周报

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

各位 Buffer 周末好，以下是本周「FreeBuf周报」，我们总结推荐了本周的热点资讯、一周好文，保证大家不错过本周的每一个重点！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icJ1UiaObonmWJbuLyoLXdutZ6T0GL6AXwFA0IHVJ9Tl93JicaeTmN55VJBw0JKrJg4sQXdypbdzqibg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

🤖Claude Mythos 安全神话：炒作还是名副其实？

🗽白宫拟向联邦机构开放Anthropic的Claude Mythos漏洞挖掘AI访问权限

🍎苹果AI服务曝漏洞：失窃令牌可在其他设备重复使用

💉GitHub评论可触发Claude Code、Gemini CLI和GitHub Copilot的提示注入漏洞

🖥️研究人员利用 Claude Opus 构建可实际运行的 Chrome 漏洞利用链

💳全球SIM卡农场即服务网络曝光：17国87个控制面板浮出水面

💻Windows 截图工具NTLM哈希泄露漏洞PoC利用代码公开

📦OpenAI 更新 Agents SDK 新增沙箱环境保障代码安全执行

📕SGLang 高危漏洞（CVE-2026-5760，CVSS 9.8）可通过恶意 GGUF 模型文件实现远程代码执行

📱黑客利用篡改版安卓NFC应用窃取非接触式支付数据

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5NY7KgXpwrAo5WHiaX2SOibeoicce3vxyZozGALjYSLtYPrDiceL0UV2D3A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

Claude Mythos 安全神话：炒作还是名副其实？

VulnCheck质疑Claude Mythos（Project Glasswing）实际成效，仅1个CVE明确由其发现，40个归功于Anthropic。专家对其72%漏洞利用成功率表示认可，但企业防护难匹配AI速度，需待7月完整报告评估真实能力。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX34UBEicNueQPyhF8S0OyMwrgUuFmGDCSXoiaRpHUE2VWlj8cu2q9KONL1LicnkWkA0FGhiaaKSoiaewwG93NAibNPQk3MewvVQWILPQ/640?wx_fmt=png&from=appmsg)

白宫拟向联邦机构开放Anthropic的Claude Mythos漏洞挖掘AI访问权限

美国政府计划授权联邦机构使用Anthropic公司修改版Claude Mythos模型，以提升网络安全防御能力。该模型能快速识别漏洞，但需严格防护措施确保数据隔离和安全。此举可能绕过五角大楼禁令，为其他政府和企业采用开创先例。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1bOMnMZnm7eOkRhic8GjcNdSepR1xgytkKXqplODE1VHHZ6N5tiakOMNSqwlnubpDTQ8pVqVND9AXAL3jianedBnO9exl3NibTQf4/640?wx_fmt=png&from=appmsg)

苹果AI服务曝漏洞：失窃令牌可在其他设备重复使用

### 苹果生成式AI服务Apple Intelligence因令牌存储漏洞（CVE-2025-43509）可被窃取滥用，导致服务配额耗尽或跨设备攻击。macOS 26.2更新改进了存储方式，但仍有绕过风险，需硬件绑定彻底解决。

### ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3kpc6cLfr7ibgneHy5AicyoibgOHL2CgTxQSOU4uAILqj1vwML8U6xmIcDSibDjCtHHibYIGojAp8BYpRr1mFOxrL1VicdhXNJuet2s/640?wx_fmt=png&from=appmsg)

###

GitHub评论可触发Claude Code、Gemini CLI和GitHub Copilot的提示注入漏洞

### 新型"评论控制"攻击利用GitHub评论劫持AI编程Agent，窃取API密钥。Claude、Gemini和Copilot三大主流AI Agent均受影响，攻击完全在GitHub内部完成，无需外部服务器。漏洞暴露AI系统架构缺陷，需加强权限控制和人工审批。 ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3hHqMxRIBBYhY9FmjE1ocPuJ3094QYxP88LpdeqTltEHJGW4brTlcuwn96TC7xWw7Iv2819l9loIFib3wTMD7tgrhM0BkzVUaI/640?wx_fmt=png&from=appmsg)

###

### 研究人员利用 Claude Opus 构建可实际运行的 Chrome 漏洞利用链 研究人员利用Claude Opus成功构建Chrome漏洞利用链，串联两个漏洞实现远程代码执行，揭示AI辅助攻击的经济可行性和补丁滞后风险，警示网络安全威胁升级。 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0J4dA6OicFgp1w67uAf5JC7sIgCIgodh2xtZRnvUDaqOZTvMBZt9RC2YgaQLEM7iaShwbVP8NpmQeJiarQ5TFbKtxwNia2pbMPNX0/640?wx_fmt=png&from=appmsg) 全球SIM卡农场即服务网络曝光：17国87个控制面板浮出水面 全球调查揭露ProxySmart驱动的工业级移动代理网络，横跨17国87个控制面板，关联94个手机农场站点，支持大规模欺诈、机器人活动及身份规避。平台提供IP轮换、指纹欺骗等功能，降低犯罪门槛，挑战全球反欺诈系统。 ![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0jDicRN4OmWQgpx9n5JSYOQVPNvWjiaZ4rdkUjM8yeYQQ12jcxBuRicL12vicELlL7hym2sGPjuk3d8frJk8ApToAs6NmFaVAxI6k/640?wx_fmt=jpeg&from=appmsg) Windows 截图工具NTLM哈希泄露漏洞PoC利用代码公开 微软截图工具漏洞CVE-2026-33829曝光，攻击者可诱骗用户访问恶意链接窃取Net-NTLM凭证哈希，利用门槛低且隐蔽性强。微软已发布补丁修复，建议用户立即更新并监控异常SMB连接。 ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3bJeiasld7yPDOBs2Yn22kmCARjwVHnpaQaNTias7kJL2H00nqey2ibBoGTTIiaTZMMSqicqdVLHFbotX64qhXlFP1tgZYvcQkS6bw/640?wx_fmt=png&from=appmsg) OpenAI 更新 Agents SDK 新增沙箱环境保障代码安全执行 OpenAI升级Agents SDK，提供标准化框架和沙箱环境，支持文件操作、代码执行等任务，内置安全措施和状态恢复机制，简化开发流程，提升Agent可靠性和扩展性，适用于法律等复杂场景。 ![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0ic5BibGibkx9oqyZgJVib1LUG9LsnYZAUwmHvlYIFTZt0A6SU3GuOTTAjQ9C1HlicLC3cTW4tNdXoEWpoIb4YZ88hHjdnkiaEsveWI/640?wx_fmt=jpeg&from=appmsg)

SGLang 高危漏洞（CVE-2026-5760，CVSS 9.8）可通过恶意 GGUF 模型文件实现远程代码执行

### SGLang框架曝出高危漏洞CVE-2026-5760（CVSS 9.8），攻击者可通过恶意GGUF模型文件在/v1/rerank端点实现远程代码执行。漏洞源于未沙箱化的Jinja2模板渲染，建议改用ImmutableSandboxedEnvironment修复。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX36sp8SBD3kdKsybp1gyQUgYR7ibCK27X0aAa8CmVbXmiaM1pUjg6XtnPrvh7hkn8IvxoZOSvz5BAHrB0lOq8yL7PIJ3wEOWsEbA/640?wx_fmt=jpeg&from=appmsg)

###

黑客利用篡改版安卓NFC应用窃取非接触式支付数据

### 黑客利用木马化安卓支付应用HandyPay窃取NFC数据和PIN码，克隆支付卡盗刷账户。NGate恶意软件新变种植入该应用，通过虚假网站传播，疑似借助AI开发。用户需警惕非官方渠道安装应用。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3FEbVyy4EjibnC1U2EX1CLKIJEMMsQqmE1EIyyuZpibicVJKHSa3icKgwUAp2dAh861X7XyBgPZ8fx5ibQYJCbicnbGkAgxdtJ40QMc/640?wx_fmt=jpeg&from=appmsg)

###

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5Ce9OricKgAogLRlHYat9jaelbVESLOylPBnQQrU63TlHEs2zCbdNrKg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**本周好文推荐指数**

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

AI 系统如何被攻破：NVIDIA Kill Chain 实战攻防全景

### AI安全面临传统防御失效挑战，NVIDIA AI Kill Chain提出新框架应对AI攻击。其核心在于识别AI特有的攻击路径（如语义欺骗、RAG投毒、智能体劫持），强调线性演进与战役化防御，覆盖侦察、投毒、劫持、持久化、影响及迭代重锚六阶段，构建全链路AI原生安全体系。

### ![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2vTh2YjK7dNBKqPygZrSNBKpc9UGyAMuHmeFKmUPXAokSichjvhh7BStNlwGpSSBuyGehyd3FvUiacyOqGENicQrQviaW1JgBiaAcg/640?wx_fmt=jpeg&from=appmsg)

###

AI安全攻防系列（1）：Prompt Injection--威胁建模

### Prompt injection是AI时代的新型攻击，通过外部文本改写模型意图，导致其执行攻击者指令。与传统注入不同，它利用语义边界模糊性，攻击面涵盖网页、文档、邮件等，且具有非确定性。Agent时代风险加剧，因模型能读取外部内容并影响系统行为，需重新定义安全边界。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3iaCK0cYVHqBeZlrHJic0t5BnZEcXSZ0dEoD266icmSNPMU7Lv2WDpgcwqsJCBaRgaNT5oEunbwFXTw0ia2Gj7Itohibtd7aeT8nm8/640?wx_fmt=jpeg&from=appmsg)

Linux 服务器安全加固与防护完整部署方案

### Debian/Ubuntu服务器安全加固方案：UFW防火墙+CrowdSec动态防御+SSH端口修改+雷池WAF应用防护，涵盖系统检查、基础加固、WAF部署及日常维护，确保多层防护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0FTyZR47sNvBJEVVhKxh5mbbiafKqVhr0iaoXZ0bRrzx34p8qlgcwUWnd180k1kWcCWQYdRwhkXXwGFJbbUeSWo9ec5u7Z4BfQE/640?wx_fmt=png&from=appmsg)

###

### ---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1NlibR8DpnkZguk1so3ThwkXScRIP7SKicZdaVeLa1eMHdfLgFsOaFCP6qt2JaDlnDPzLe5MJBV1micoP6YM0SG5C9X1ibsshUiccM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337140&idx=1&sn=134af642d92b85fc1076a8c83c09945c&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bKq2xLKwFuy1Yl63ibm7kJUCW7hP4uRIhllVu6icLPkYcerZIx5264cbnPu5uCLCpb0ic16Gm32GC3B6ou34yFia9Nm4YJTGU4iag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38TJMDLxr9EPGGib49oQymrvRy7vGw1iakQXBCr1Udmia4dpY3JSWYEEicajmhhcyfHly9YYPIziaCVPOg/640?wx_fmt=png&from=appmsg)

###

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5r...