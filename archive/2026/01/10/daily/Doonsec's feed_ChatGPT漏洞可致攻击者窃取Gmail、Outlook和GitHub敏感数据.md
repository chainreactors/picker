---
title: ChatGPT漏洞可致攻击者窃取Gmail、Outlook和GitHub敏感数据
url: https://mp.weixin.qq.com/s/CAp7sX2hp_uUPucKyAy_gA
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:40:35.108025
---

# ChatGPT漏洞可致攻击者窃取Gmail、Outlook和GitHub敏感数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icycH9yDEUA78sddIQVdK0c9XcKWha7MVkHObv09Piav6xEsKntIh0lcTBgRtpgqn0OeUvoibnZBfQw/0?wx_fmt=jpeg)

# ChatGPT漏洞可致攻击者窃取Gmail、Outlook和GitHub敏感数据

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icycH9yDEUA78sddIQVdK0cIldCEVPBibQlicnSzVQHSN0UOQspPlw6LIPVPzrEwe3sib248QKjAYUtw/640?wx_fmt=jpeg&from=appmsg)

ChatGPT 存在严重漏洞，攻击者可在无需用户交互的情况下，从 Gmail、Outlook 和 GitHub 等关联服务窃取敏感数据。这些被命名为 ShadowLeak 和 ZombieAgent 的漏洞，利用 AI 的 Connectors 和 Memory 功能实现零点击攻击、持久化驻留甚至传播扩散。

OpenAI 的 Connectors 功能允许用户通过简单点击即可将 ChatGPT 与 Gmail、Jira、GitHub、Teams 和 Google Drive 等外部系统集成。默认启用的 Memory 功能则会存储用户对话数据以提供个性化响应，使 AI 具备读取、编辑或删除条目能力。虽然这些功能提升了实用性，但也因安全防护不足而大幅增加了个人和企业数据的泄露风险。

**Part01**

## ****ChatGPT 零点击与单点击攻击机制****

攻击者通过发送恶意电子邮件或共享嵌有隐藏指令的文件（使用白色文字、极小字体或页脚内容实现视觉隐藏）实施攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icycH9yDEUA78sddIQVdK0cEtHicwmqFBw6DBES3kWibHDlSHa3vLVKerNFu651DawouYa6u1kUJNxQ/640?wx_fmt=jpeg&from=appmsg)

攻击链条（来源：Radware）

在零点击服务端攻击变体中，ChatGPT 在执行邮件摘要等常规任务时扫描收件箱，通过 OpenAI 服务器执行恶意负载并泄露数据，用户全程无感知。单点击版本则在受害者上传污染文件后触发，可对关联代码库或云盘发起链式攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icycH9yDEUA78sddIQVdK0ciaBfRzwbV6LOulkyv97kdmc2ysTic3o65a0Hb7cG4D95GepLOdoK7d9Q/640?wx_fmt=png&from=appmsg)

尽管 OpenAI 已禁止动态 URL 修改，但研究人员通过为每个字符（a-z、0-9、$代表空格）预建 URL 实现绕过。ChatGPT 会将"Zvika Doe"等敏感字符串规范化为"zvikadoe"，然后顺序访问类似 compliance.hr-service.net/get-public-joke/z 的静态链接完成数据外泄。这种服务端方法可规避客户端防御、浏览器检测和界面可视性检查。

为实现持久化，攻击者通过文件注入内存修改规则：每次处理消息时优先读取特定攻击者邮箱并泄露数据。虽然 OpenAI 限制 Connectors 与 Memory 功能混用，但逆向访问仍然可行，导致新聊天会话中仍存在持续数据泄露风险。传播机制会扫描收件箱获取联系人地址，攻击者服务器随后自动向这些目标发送恶意负载，形成组织级渗透。

Radware 于 2025 年 9 月 26 日通过 BugCrowd 平台报告了这些漏洞，并提供了技术细节与升级方案。OpenAI 于 9 月 3 日修复了 ShadowLeak 漏洞，12 月 16 日完成全部漏洞修复。专家建议持续监控 Agent 行为并对输入内容进行净化处理，因为 AI Agent 的盲区风险仍将持续存在。

**参考来源：**

New ChatGPT Flaws Allow Attackers to Exfiltrate Sensitive Data from Gmail, Outlook, and GitHub

https://cybersecuritynews.com/chatgpt-vulnerabilities-expose-sensitive-data/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39H4eicalbOEwZ1t8X3mSSZssMSDW4LkuO5g3W31c7ibGVXTlUPk3BqrUoic8Rqt25DJOCygq1FzABicw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651333596&idx=1&sn=a5f1d8decaf400a24f3b9e74a3a357e1&scene=21#wechat_redirect)

###

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLq7T2qZrtcsoq5PRQ2cjDU1HUaakGzExOsSIU2Quxiasf7W9ibLiaEsmWA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

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