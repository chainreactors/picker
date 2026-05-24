---
title: GitHub 4000个私有仓库被窃取；Claude Code深度链接解析漏洞可被武器化 | FreeBuf周报
url: https://mp.weixin.qq.com/s/js1AYhWtrLBCmo7CJGADKw
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:56:55.434125
---

# GitHub 4000个私有仓库被窃取；Claude Code深度链接解析漏洞可被武器化 | FreeBuf周报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymyA0AYWle3Wnao3wWyHqsDzMGH37D4XINGFb1Us09fC8ibRIH5cvgDSw/0?wx_fmt=jpeg)

# GitHub 4000个私有仓库被窃取；Claude Code深度链接解析漏洞可被武器化 | FreeBuf周报

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

各位Buffer周末好，以下是本周「FreeBuf周报」，我们总结推荐了本周的热点资讯、一周好文，保证大家不错过本周的每一个重点！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icJ1UiaObonmWJbuLyoLXdutZ6T0GL6AXwFA0IHVJ9Tl93JicaeTmN55VJBw0JKrJg4sQXdypbdzqibg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

🖥️GitHub证实被入侵，4000个私有仓库被窃取

# ⚠️Claude Code深度链接解析漏洞可被武器化，无需额外交互即可RCE

# 🐧潜伏九年的Linux内核漏洞可致攻击者窃取SSH私钥

# 🍎Claude Mythos 5天攻破最强硬件，20亿台苹果设备的安全逻辑正在被改写

# 🌐NGINX高危漏洞（CVE-2026-42945）遭野外利用，可致RCE或服务崩溃

# 🦈"巨齿鲨" 恶意软件6小时内入侵5500 多个GitHub代码库

# 📷高危ExifTool漏洞：攻击者可利用恶意图片入侵Mac设备

# 🔐Claude Code沙箱漏洞5个月未修复，攻击者可窃取凭证与源码

# 💰GitHub缩减漏洞赏金计划，提醒用户安全责任需共担

# 🏆Pwn2Own Berlin 2026落幕：0Day漏洞奖金总额达130万美元

#

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5NY7KgXpwrAo5WHiaX2SOibeoicce3vxyZozGALjYSLtYPrDiceL0UV2D3A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

GitHub证实被入侵，4000个私有仓库被窃取

GitHub调查内部代码仓库遭未授权访问事件，威胁组织TeamPCP宣称窃取4000个私有仓库数据并高价兜售。GitHub称客户数据暂未受影响，正监控基础设施。攻击者技术可信度高，调查仍在进行中。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3tflQvG4KM0kyMdHpIDRkLsUywyR1eZ8SibSTS0bAUguLeMibVYQB00C0VnnFAibZY5v3dylcFXDrwPUgbC1SWQpCRsoAkicbO4A4/640?wx_fmt=png&from=appmsg)

# Claude Code深度链接解析漏洞可被武器化，无需额外交互即可RCE

Anthropic的Claude Code CLI工具存在严重RCE漏洞，攻击者通过特制深度链接可执行任意命令。漏洞源于参数解析缺陷，允许注入恶意钩子命令。2.1.118版本已修复，建议用户立即更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2SjTiaElmKgGzcD1otzVUQFSUrUCRqMTn4mdrtBv1QSz5wm2AE2sHOnucXc9RSUpmxjEPDV9Y6jVR4p51jhLsF7z95DUcEibXGA/640?wx_fmt=png&from=appmsg)

潜伏九年的Linux内核漏洞可致攻击者窃取SSH 私钥

### Linux内核曝出潜伏九年的高危漏洞CVE-2026-46333，可让本地攻击者获取root权限并窃取敏感数据，影响主流发行版。补丁已发布，建议立即更新或临时调整安全参数。同时Arch Linux的PinTheft漏洞PoC也被公开，需警惕本地提权风险。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3icoQl2M7ga0iclyYKIAsaiaPlxRayKK1abw4EHVuwgbFflkqUBjsUqEnKYSRdW2Bbnuia5b0APkVUKYZNu1BWacTSenoLiaqEeN2c/640?wx_fmt=png&from=appmsg)

###

Claude Mythos 5天攻破最强硬件，20亿台苹果设备的安全逻辑正在被改写

### Calif研究团队借助Anthropic的Claude Mythos Preview AI模型，仅用5 天就成功攻破苹果M5芯片的硬件级MIE内存防护，在macOS 26.4.1系统上实现内核本地提权，标志着AI大幅缩短硬件安全防护窗口期，苹果正研发修复补丁。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX31kHic0qA99y8dHjAMpP8oUHNQ4lOrYEYRUKvXtje5wibc06HdS9kfspqtkg6Hic3b8TnmWc8pp01pef0AlFfGtZz49qo4PV7ibWY/640?wx_fmt=png&from=appmsg)

###

### NGINX高危漏洞（CVE-2026-42945）遭野外利用，可致RCE或服务崩溃 NGINX Plus和开源版爆出堆缓冲区溢出漏洞（CVE-2026-42945），可致服务崩溃或特定条件下远程代码执行，野外攻击已现。openDCIM同期曝高危漏洞链，攻击者组合利用可远程执行代码。建议用户紧急更新补丁。 ![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1ge2Zs5MbRqicviaKeO3qQZVDKBwAfGIAiagibYTWozyPCam3MsdVfibn6ETQxtlYlp7WnLQsBf4icduMtg5MnmCibIskFTC5mVtGUFk/640?wx_fmt=jpeg&from=appmsg)

###

### "巨齿鲨" 恶意软件6小时内入侵5500多个 GitHub代码库

### 2026年5月18日，“巨齿鲨” 恶意软件发起自动化供应链攻击，不到6小时入侵GitHub超5500个代码库，通过伪造CI机器人身份注入恶意Actions工作流，窃取云凭证与密钥并污染 npm 包，创下最快扩散记录。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX24YQUNib4fxxjT41IGibcOlaljulo9n36ZaV7xVv4bMjPfc6ClmAicWDB4wwuQgCyniaCcFZEXKNZ7x5cP6iaVUGEuWdmQL0G1ib8uI/640?wx_fmt=jpeg)

###

### 高危ExifTool漏洞：攻击者可利用恶意图片入侵 Mac设备 ExifTool 曝出CVE-2026-3102高危漏洞，攻击者可通过恶意图片在 Mac 上执行任意命令，该漏洞已在 13.50 版本修复，建议立即升级并加强图片处理环境安全。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1eCJiaXoBpWINyKLwuklVFUgIcOmFoOFS8WRSwOdqevUb6VL1oZnic3CPB2XKAFoicQkHQQaFJxlApQtdYOEZR3tUzic7ibAIIRKJs/640?wx_fmt=png&from=appmsg)

###

Claude Code沙箱漏洞5个月未修复，攻击者可窃取凭证与源码

Claude Code 存在**网络沙箱绕过漏洞**，攻击者可通过空字节注入绕过主机名校验，窃取用户凭证、源代码与云资源访问权限，该漏洞已在 v2.1.90 版本修复，建议立即升级并轮换相关密钥。

### ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3bcWGicAicXMkuNhM8cicD9Gt85wDx1gEad9SLdypbQOWTc7EDr4VTDnfDcfnpo1KEjzZztJgj3Idya4jkNGEGBwicplKQTNOZA08/640?wx_fmt=png&from=appmsg)

### GitHub缩减漏洞赏金计划，提醒用户安全责任需共担

GitHub因AI生成的低质漏洞报告泛滥，缩减漏洞赏金计划，对低风险报告改用周边奖励替代现金，并呼吁研究者停止提交无关问题，此举也引发了行业对安全人才供应链的讨论。

### ![通过GitHub供应链发起的攻击](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3etjNW7ia8uwPTSXmicHnKPywib8GicXWjk3TnaoqTVRWjbXF52bBoK3wDPhiagTaZuW9YROYiaOL8icwb24ONhXD7kvgc4EX4bvVoW0/640?wx_fmt=jpeg&from=appmsg)

###

Pwn2Own Berlin 2026落幕：0Day漏洞奖金总额达130万美元

Pwn2Own Berlin 2026 落幕，赛事共演示 47 个0Day漏洞，总奖金近130万美元；中国台湾DEVCORE 团队夺冠，赛事还首次成功攻破AI编程助手与 VMware、Windows、Linux等主流系统。

### ![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2TqVflibx83UiaZVN2Vnibbq0PHVGtomEyqfXDc3XnotMebxovEJgMlY1SicdZqGhUBGX2HJiazMwg4dM1JG2kHm3XBhWhKYDicJBmc/640?wx_fmt=jpeg&from=appmsg)

###

### ![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5Ce9OricKgAogLRlHYat9jaelbVESLOylPBnQQrU63TlHEs2zCbdNrKg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp) **本周好文推荐指数** ![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp) ![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp) ![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp) ![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp) ![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

AD域渗透之exchange 攻击面研究与复现

这篇文章核心是**AD 域渗透场景下 Exchange 攻击面的梳理与复现基础**，详细讲解 Exchange 与 AD 域的紧密集成关系、服务器角色、常用接口，以及在渗透测试中对 Exchange 进行**端口扫描、SPN 查询、版本识别**的标准信息收集方法，为后续 Exchange 漏洞利用与域内攻击打下技术基础。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1OeukZe50KPfsbXEpOam7ibJ3yrCtDmW9exPYpo8Tibziah0oY4t59WF8svQTJqbSlAGFJRbfQtsxotCeDPIKjaN7HkhU7Qz9mPs/640?wx_fmt=png&from=appmsg)

###

记一次常态化渗透测试：从域名到Getshell的思路
通过目录扫描发现**Shiro鉴权绕过**与文件上传接口，结合路径穿越、存储型 XSS、评论接口越权，爆破Shiro密钥并利用**CommonsBeanutils1反序列化漏洞**获取服务器Root权限；过程中遭遇EDR与防火墙拦截，最终成功读取数据库配置与Druid监控台信息，形成完整渗透链路。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0Dd9VWkwyNYCd7xJ4nfznofDgicwIbeVpMTX6icFg0Tj5wO7Rw4Ds0niaszLic3HKQQ69hs02ttBkIbuV66kDiaKnfMjPGvOqqmmFg/640?wx_fmt=png&from=appmsg)

###

OpenClaw安全-沙箱篇(1)：WSL2手把手教学（可复现流程）

本文以**WSL2+Docker**为基础，通过可复现实验讲解OpenClaw沙箱的安全设计，将Docker的容器隔离、只读文件系统、无网络、权限丢弃等原语，对应到OpenClaw的sandbox配置项，实现AI工具执行的安全隔离，并提供完整部署、配置、验证与排错方法。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX28hxzcSicibbf3Pf3z18YvuSqrUsy9WicrTyh1hzNicZLZp6iczwEJnibg69icgBAyPfSic5TyLw1lExuM9up62TRNiaLFHz1FLfA0Zc04/640?wx_fmt=png&from=appmsg)

### ---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0TPDSBGWyOrBX6roghTcfJ7S0Uk6LPc6NiazIJCibS6wTdC64AxlpIAv3YZ2LoZFsJy3UHwic3ohlaRGRMZkKBW03QD5AMj5yuicM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651338385&idx=1&sn=a442efc5bf8726e3e4239bc246e2976b&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2A30nW87bmYJO7PWcHicOLnjA5DRaqykn6a3r9Nvg2PUTX1XkGuXcekoXza0aIXeq8O4ZwnhjLdFba5NEv5NQetNb0KjM9Mnb8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38TJMDLxr9EPGGib49oQymrvRy7vGw1iakQXBCr1Udmia4dpY3JSWYEEicajmhhcyfHly9YYPIziaCVPOg/640?wx_fmt=png&from=appmsg)

###

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

![跳转二维码]()...