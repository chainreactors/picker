---
title: 黑客入侵GitHub上万个代码库植入恶意软件
url: https://mp.weixin.qq.com/s/mAy2GdVzudcntRF1OHB3Tg
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:00:41.775348
---

# 黑客入侵GitHub上万个代码库植入恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3B6ZY1iamj3WKqoHfKnb8E5a8aDolmzI4pyM1ibhFy6GSrw7Zv20Sko8VDp9qH31kmReGnHwMCAPeVAFAUJxm3DYDYCn4pOp7Z0/0?wx_fmt=jpeg)

# 黑客入侵GitHub上万个代码库植入恶意软件

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1ammibJqhr4KH7y5cqF4pF0aHuc5vC47JlOkajl8Aczwsut5CAe9O9Wc2MeJcdBthIFljkCn2xiaichPdzlhqdxqFjjMgTicpic41s/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2fyPeRzhLU9o9rvoZ4XgaWCSRLqeiaNkkQugMOTs1bHQoCXYggc5h35bSFjpmYCrEp571AmwrBghDL4t080WAlbtvYtZ1jcR5E/640?wx_fmt=png&from=appmsg)

研究人员发现 GitHub 平台上存在大规模恶意软件传播活动，超过 10,000 个代码库分发含有木马的压缩包，这引发了对平台信任模型滥用及自动化检测局限性的担忧。

Part01

恶意活动发现过程

调查始于研究人员在搜索引擎结果中发现其个人代码库的克隆版本。虽然项目名称、描述和提交历史完全相同，但新增的提交记录在 README 文件中植入了指向可下载 ZIP 压缩包的恶意链接。随后在多个无直接派生关系的代码库中观察到相同行为，表明这是有组织的攻击活动而非孤立事件。

Part02

攻击手法分析

深入分析显示攻击者采用统一模式：完整复制合法代码库（包括提交历史和贡献者资料）以建立可信度，随后定期修改 README 文件添加外部 ZIP 压缩包链接。这些提交通常每隔几小时就会被覆盖重推，并标注为"Update README.md"，这种策略可能有助于规避检测机制或维持索引系统可见性。

Part03

恶意载荷特征

关联的 ZIP 压缩包包含少量文件，包括命令脚本、可执行加载器和动态库。虽然单个文件链接在 VirusTotal 上常显示无威胁，但下载完整压缩包扫描后即检出木马恶意软件。这表明攻击者可能采用分割或混淆载荷组件的规避技术来绕过自动化扫描工具。

Part04

活动规模确认

为评估活动规模，研究人员利用 GH Archive 的 GitHub 事件数据开发脚本。该脚本聚焦于提交频繁的代码库（因 API 速率限制无法扫描全部），在分析的 5 天内约 1600 万次提交事件中，发现 3000 个代码库存在可疑更新模式。经过排除机器人账户、强制贡献者多样性检测及异常提交时间筛选后，最终确认约 10,000 个代码库符合恶意特征模式。

Part05

平台安全挑战

根据 Orchid 分享给 Cybersecurity News 的报告，许多被入侵代码库已潜伏数月甚至数年未被发现。研究还推翻"高频提交即恶意"的假设——部分恶意代码库更新频率极低。其他特征包括无实际文件变更的提交和标准化命名惯例，进一步凸显自动化部署特征。

该活动专门利用 GitHub 在搜索引擎和开发工作流中的可见性：通过克隆新创建或低流量代码库，攻击者提高了在细分查询结果中的出现概率。保留提交历史和贡献元数据增强了可信度，促使用户信任并下载恶意文件。

尽管已提交报告，处置效果参差不齐。GitHub 仅移除了研究人员明确列出的代码库，新发现的恶意库仍保持活跃，表明平台采取的是被动响应而非主动防御策略。公开报告显示此类攻击手法至少从 2025 年初就已出现，类似活动曾分发 SmartLoader 和 StealC 等恶意软件家族。

此次事件凸显代码托管平台面临的核心挑战：如何检测模仿合法开发行为的恶意活动。若缺乏对代码库内容、提交模式和外部链接的可扩展分析，此类活动将持续潜伏。对开发者而言，该事件再次强调验证外部下载源的重要性——即使它们来自看似合法的代码库。

参考来源：

Hackers Compromised 10,000+ GitHub Repositories to Inject Malicious Script

https://cybersecuritynews.com/hackers-github-malicious-script/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2hnMwPwS6lmzbFHf7S8ibkCSGSF9zbd12puFsqvAeRIjLV7b95iaBhzib3wR12ia2WNVDpNOZvF8yaZcGaQ3kXTL8YePjicoGiajOTg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340988&idx=1&sn=0937f2692c838e2a62e89dde8d9dbe41&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3BRs1SIg3pvHw9PNmLlib6c3rX0W3PemrBoDibgBD3WXIWDcs94DXZpBy9YuU36icJ4NHEE98mUbqcOYyicrZBiblxE3uy64Zibo1PY/640?wx_fmt=png&from=appmsg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0UGcrYtIkSYDEgbDkib0yMF23VlKQibpJyRnibia1cD3no5XF7Je0Sic98ytMyvbY9LhO8tKoxBlnibsAXh8CnBTYoAxLReujuqjomI/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1cNPEia7j7bXCX8P8iaDo801yQlaF965NduoqX5nEfgC2mLLgM6VdzcRdkYkeGebHaia3JRK31e08ibfS1WnmYl8DtvPf83e6XW6k/640?wx_fmt=png&from=appmsg)

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