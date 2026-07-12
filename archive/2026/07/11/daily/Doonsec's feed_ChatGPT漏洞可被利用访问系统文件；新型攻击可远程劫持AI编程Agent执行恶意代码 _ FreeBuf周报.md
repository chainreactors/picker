---
title: ChatGPT漏洞可被利用访问系统文件；新型攻击可远程劫持AI编程Agent执行恶意代码 | FreeBuf周报
url: https://mp.weixin.qq.com/s/H-BZW4cvdDmvbtED7bk_CA
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:07:41.324344
---

# ChatGPT漏洞可被利用访问系统文件；新型攻击可远程劫持AI编程Agent执行恶意代码 | FreeBuf周报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymyA0AYWle3Wnao3wWyHqsDzMGH37D4XINGFb1Us09fC8ibRIH5cvgDSw/0?wx_fmt=jpeg)

# ChatGPT漏洞可被利用访问系统文件；新型攻击可远程劫持AI编程Agent执行恶意代码 | FreeBuf周报

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

各位 Buffer 周末好，以下是本周「FreeBuf周报」，我们总结推荐了本周的热点资讯、一周好文，保证大家不错过本周的每一个重点！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icJ1UiaObonmWJbuLyoLXdutZ6T0GL6AXwFA0IHVJ9Tl93JicaeTmN55VJBw0JKrJg4sQXdypbdzqibg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

📥 ChatGPT 文件下载流程漏洞可被利用访问系统文件

🤖 新型攻击可远程劫持 Claude Code、GPT-5.5 等 AI 编程 Agent 执行恶意代码

🎫 黑客利用 Claude AI 窃取全美音乐节门票的网络安全事件

🐧 Bad Epoll 漏洞使攻击者可获取 Linux 及 Android 系统 root 权限

🔍 GitHub 公共 API 正成为企业级侦查工具

📱 首个一键式 Android 17 漏洞利用链可使攻击者完全控制手机

⚠️ 当 Claude、Cursor 和 Codex 触发了终端安全检测报警

🔗 AI 双 Agent 攻击：利用 Claude 桌面版在目标机器上执行远程代码

📂 SharePoint 远程代码执行漏洞 PoC 及技术细节公开

🕵️ 通过 Telegram 租用的 RedWing 恶意软件：任何人都能获取 Android 间谍工具

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5NY7KgXpwrAo5WHiaX2SOibeoicce3vxyZozGALjYSLtYPrDiceL0UV2D3A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

### ChatGPT文件下载流程漏洞可被利用访问系统文件

ChatGPT存在漏洞链，结合防护绕过和路径遍历缺陷，可访问系统文件如/etc/passwd。研究员通过社会工程和路径构造绕过限制，OpenAI已修复。案例凸显LLM需兼顾AI和传统Web安全测试。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1RksgtyXuQDibgIOSVYTyXw1MhgN5QbGNkaScJicoTHdfnq82oolBR0xX1lqXZ8UTwODFTKU7apgVViacbFV2AP1HwDpObejHJNs/640?wx_fmt=png&from=appmsg)

### 新型攻击可远程劫持Claude Code、GPT-5.5等AI编程Agent执行恶意代码

"友好火"攻击利用AI代码审查漏洞，通过伪装恶意文件诱导Claude和GPT模型执行远程代码，暴露自动审查机制缺陷，威胁供应链安全，建议限制AI对不可信代码的执行权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sx6rjO9G7380OmXVswJIz5DicRSMp9gqeUShX9t7XDyml91E9vvZNFddu96ibwSSqpj0mic2MQN4tyA4yJickJmakiaI6UMVYUkVI/640?wx_fmt=png&from=appmsg)

### 黑客利用Claude AI窃取全美音乐节门票的网络安全事件

研究人员借助Claude AI发现Front Gate Tickets平台存在SQL注入漏洞，可接管管理员账户，获取客户数据、发放免费门票等。案例凸显AI辅助漏洞研究的威胁，传统票务系统安全风险高。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2Q6oEm3TIDice5KKBkBicPjic1cY4Oege4RCgsbxdtEcrFibHWwju8hU48ia9eTf7UnfXVNFfNNJ55qfGTrzgZwcEhSibGdSWibU8h00/640?wx_fmt=png&from=appmsg)

###

### Bad Epoll漏洞使攻击者可获取Linux及Android系统root权限

Linux内核漏洞Bad Epoll（CVE-2026-46242）允许本地攻击者获取root权限，影响Linux 6.4+及Android设备。该释放后使用漏洞通过epoll子系统竞争条件实现提权，利用成功率高达99%。AI曾发现类似漏洞但遗漏此问题，凸显AI检测竞争条件漏洞的局限性。建议立即安装补丁。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3vbsGLBBviaLTp2MBdklHuzSqCG8LGyELxTk7O5NHEZEYsGYmyZy0XOvJKjXkopdxzdibdJcGTs1y85RtiaH3iaUJZibl7I7Gooia38/640?wx_fmt=png&from=appmsg)

###

### GitHub公共API正成为企业级侦查工具

攻击者滥用GitHub公共API和幽灵账户对企业软件环境进行隐蔽侦查，窃取源代码和密钥。这些活动与正常开发行为高度相似，利用休眠账户和定制工具，难以察觉。企业需监控异常行为、启用审计日志并加强基础安全措施。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1XdnM5VteVuxKMzPhoNDIWKO11Gicgc3daicnCIvfYoCQLWH74KpLTk7XPesiaLKLicpxfBle2LGryZHrSFnGlW1fGlVib7YGh2LhA/640?wx_fmt=png&from=appmsg)

###

### 首个一键式Android 17漏洞利用链可使攻击者完全控制手机

全球首个Android全链漏洞"IonStack"曝光，通过Firefox和Linux内核0Day漏洞实现一键远程控制设备，15年潜伏漏洞威胁数十亿设备。建议立即更新Firefox并关注内核补丁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2zTHb7NJ83kXbPDmjI4Cia9yTIVrsar7bIWlc4RJfvvoxBrxBEWag08XepGEyE5BBhZW4h9IzHic0TQvIlvp2rw9zQ7iaw1bA6E4/640?wx_fmt=png&from=appmsg)

### 当Claude、Cursor和Codex触发了终端安全检测报警

AI编程工具如Claude、Cursor和Codex在企业中的使用频繁触发安全警报，涉及凭据访问和LOLBins滥用等高风险行为，模糊了合法自动化与攻击活动的界限，迫使安全团队重新评估检测策略以区分威胁与AI工具操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3x6typ9jEYAB0ME6oE614HZRWUdqucvHEH9ThDJ64eJvYrqcUZLlk4GMwgdMicuFdId88icnIIaR0kHtiaO2rY98kvqwNwBsJn3k/640?wx_fmt=png&from=appmsg)

### AI双Agent攻击：利用Claude桌面版在目标机器上执行远程代码

安全研究发现电子邮箱被入侵后，攻击者可利用Claude桌面助手实现远程代码执行，通过同步"个人偏好"字段注入恶意指令。该攻击无需恶意软件或钓鱼链接，能将助手变成持久控制通道。研究揭示AI助手扩展生态存在系统性漏洞，厂商却称此为预期功能。建议将AI应用视为特权软件，监控设置变更并限制扩展配对。

### ![文章配图](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0ZIU3Z2ZUuZTuwVIdicFkMRB5ibob3Hnl4h5EJQOgoCWNcBBV8ibO1WMxKj6Xmz4PXqzxQSN9k0jlhFo8PibejKdEElmaz1DialjC4/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

###

### SharePoint远程代码执行漏洞PoC及技术细节公开

高危漏洞CVE-2025-53770影响本地SharePoint，允许远程代码执行。攻击者利用ExcelDataSet控件绕过验证，通过恶意XSD触发反序列化漏洞。微软已发布补丁，建议立即更新并监控可疑活动。![文章配图](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3ZblicrPEvPABmIvWibo4AK3JzmHXGHTFwdZe0lrPhtDhicKhLIv9Fhic2W8BwLZSHnBLRDHL6n4DvVSh3KkLKJnPgywUn9vE1EUI/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

###

### 通过Telegram租用的RedWing恶意软件：任何人都能获取Android间谍工具

RedWing是Telegram上租赁的Android间谍软件，仿冒应用商店窃取银行数据，可远程监控设备并发动DDoS攻击。其MaaS模式降低攻击门槛，无需编码能力即可定制恶意应用，依赖社会工程获取权限，威胁BYOD环境安全。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0cQxuYhPHQCmmYibOqzAUwWe5oOuyZPQJFDsE1PNVcSKEvprYr9TS7WwOUdiaziaBE5yoib2BUeVoPZicvZn6YRLNNnOjH1RIKwnfA/640?wx_fmt=png&from=appmsg)

###

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5Ce9OricKgAogLRlHYat9jaelbVESLOylPBnQQrU63TlHEs2zCbdNrKg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**本周好文推荐指数**

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

### 我的Mac潜伏了一个月木马：AI Agent时代，真正危险的不是“手滑”

Mac用户因AI Agent执行恶意命令中招，木马潜伏盗取账号。AI Agent时代风险在于其自动执行外部指令，缺乏安全边界。建议开启2FA，使用OpenGuardrails等工具监控Agent行为，防止远程脚本等危险操作自动执行。

![大模型分析信息时出现幻觉错误怎么办？解决方案汇总 - Raccoon-Raccoon](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2iaLiab3k0Qa5qcY5BZo4ZqTic56PhM8rLaIU8k1q3yf5v54NiaCNfOubQY5I52MKkokku40GvGDOfCJlHNOrFSvuMEd9Vce5tp30/640?wx_fmt=jpeg&from=appmsg)

###

### 监控后门：深扒Claude Code暗藏的「中国特供」监控后门

Claude Code通过代理中转时秘密收集用户环境指纹，包括中国时区、代理域名及AI实验室信息，通过隐写术编码到系统提示词中发送至Anthropic。新版重命名函数但功能不变，新增未公开环境变量可关闭遥测。

![1776334708_69e0b7746bb1f15f5b22d.jpg!small?1776334707433](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1HUFrWPkLx2Dy7vj0tLMIjuQicT9QoxOcIZU2Uo0zPUw290oZagJhbiacUD0SKiavvXaZCbaMjoOGZnaMuH8RnHwnrWNEvE9icK4k/640?wx_fmt=jpeg&from=appmsg)

###

### 藏在锦囊里的刀子：SkillCloak如何用自解压打包让恶意AI插件骗过所有扫描器

AI Agent Skill生态面临严重安全威胁，恶意Skill通过结构混淆和自解压打包技术绕过主流扫描器，窃取敏感数据。SkillCloak攻击框架对静态扫描器绕过率高达99.8%，而动态检测工具SkillDetonate通过沙箱审计和污点分析能有效识别恶意行为。AI编程助手权限过高，供应链安全亟待加强，需从代码审查转向行为监控。

![Infostealer malware found stealing OpenClaw secrets for first time](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2lzhIuoEqtPMIibz1WqoZ1icPuqwNkctyhmk5FzQbjXTeoQWgn1kGfUGBicp77EPPM38y19KYE0v2lU89DR64zVtdZON0wCnyjkc/640?wx_fmt=jpeg&from=appmsg)

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3y34M5GAibwcktqAsbKu2ibamWeibVrPpa709ynHMljYolGiaw7cPCyW5sCvL9sRS4lJVTOahlPKkMD7YuL5JjW6tibNyibD9QErkrc/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1cNPEia7j7bXCX8P8iaDo801yQlaF965NduoqX5nEfgC2mLLgM6...