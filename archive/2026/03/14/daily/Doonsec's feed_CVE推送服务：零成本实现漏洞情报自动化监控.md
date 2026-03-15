---
title: CVE推送服务：零成本实现漏洞情报自动化监控
url: https://mp.weixin.qq.com/s/4H2BJWdfiCUVV_tZz9AOUQ
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:24:38.883425
---

# CVE推送服务：零成本实现漏洞情报自动化监控

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODw3Is3nsjicOj2IXkJY0ibXpyK6yjAlemp8cIqeEAqbhG8lXqIwEzyJBKk7ykicUpo2jymVurK6H30FUFZrT3dwgCZJaQiaWojsmM8/0?wx_fmt=jpeg)

# CVE推送服务：零成本实现漏洞情报自动化监控

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# CVE推送服务：零成本实现漏洞情报自动化监控

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

CVE推送服务是基于GitHub Actions的自动化漏洞情报工具，集成*NVD监控*与*POC/EXP仓库追踪*，通过Server酱3实时推送至移动端。

## 🚀 一句话优势

**零服务器成本实现漏洞情报实时推送**，Artifact去重避免重复通知。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| NVD监控 | 自动获取最新高危漏洞情报 |
| POC追踪 | 监控GitHub漏洞仓库更新状态 |
| 智能翻译 | 集成有道API实现描述中文化 |
| 去重存储 | Artifact存储数据库避免重复 |
| 自动运行 | GitHub Actions定时任务零运维 |

## 📸 运行截图

| 截图位置 | 描述 |
| --- | --- |
| 推送效果 | ![](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODywFneibbqVbvdDovB89d6YkTGBmP161szd7ibftkxibRjesKLsNbicDmiceshoK2QyzgWjFfwL42WQ4HCGlZnTOK8zazxhIMCiblpco/640?wx_fmt=jpeg&from=appmsg) |
| 配置界面 | ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwQ5g2sRztGicvakonCBRAQhD7Vcpicicn6W2dHiaujJiciaFY9V8ZDy3xSFmKLEUkgtdP4k042qoYaL1CV4qeb2cr3tZb9W0V095D1c/640?wx_fmt=png&from=appmsg) |

## ✨ 核心亮点

### 1. 双源情报监控

工具同时监控NVD官方漏洞库与*GitHub POC/EXP仓库*，区分标记"new"（新仓库）与"updated"（更新）状态，帮助安全从业者精准掌握武器化利用进展。

### 2. Artifact持久化去重

利用GitHub Actions Artifact存储*vulns.db*数据库，Fork项目独立维护历史记录，既避免重复推送干扰，又实现零成本数据持久化。

### 3. Server酱3实时推送

集成Server酱3服务，Critical漏洞与POC发布时*秒级推送*至微信/移动端，支持有道翻译API自动中文化，适合应急响应与漏洞研究场景。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| GitHub Actions | 原生CI/CD定时任务 | 零服务器成本，自动触发 |
| Artifact存储 | 工作流产物持久化 | 免数据库部署，Fork隔离 |
| Server酱3 | 多通道消息推送 | 微信/APP实时到达 |
| 有道翻译API | 漏洞描述自动中文化 | 降低英文阅读门槛 |
| 状态识别 | 区分new/updated仓库 | 精准控制信息噪声 |

## 📖 使用指南

① **准备工作**：Fork仓库并在Settings → Secrets中配置*SCKEY*（Server酱3密钥）与**GH\_TOKEN**（GitHub令牌）。

② **核心操作**：点击*Actions*启用**Auto CVE Push Service**工作流，默认每日北京时间8:00自动运行，或手动触发测试。

③ **结果查看**：在*Server酱3 App*查看推送的CVE详情，包含*CVSS评分*、翻译描述与GitHub POC链接，Artifact中可下载*vulns.db*审计历史。

## 📖 项目地址

```
https://github.com/hijack1r/CVE_PushService
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

| ![img](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODwwQX3j5Iibfc7cXw3B9fAXHLk14Cu42TqTEEl2XJhzDEN1XLTCicFOMKibEsXELqtBmC41zgwgjyQ3XuTF9vl85bOFesmtwZxqcw/640?wx_fmt=jpeg&from=appmsg) | ![img](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&from=appmsg) |
| --- | --- |
| ![img](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODyfImocuEticymPtIH5whMyss8TnMHibgnWkzicgGACFViaDjJjHtVyiaAknpibdJIwdlFX4kuNicdHHVzCycSX3qTld8FUJ7ic9mLmI4Q/640?wx_fmt=jpeg&from=appmsg) |

### 推荐阅读

✦ ✦ ✦

| [渗透测试人员必备武器库：子域名爆破、漏洞扫描、内网渗透、工控安全工具全收录](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485592&idx=1&sn=818004a6d625c4c4112ce73b83433854&scene=21#wechat_redirect) |
| --- |
| [AI驱动的自动化红队编排框架(AutoRedTeam-Orchestrator)跨平台支持，集成 130+ 安全工具与 2000+ Payload](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485309&idx=1&sn=292afbe37fb95c64f33470f915b0c54e&scene=21#wechat_redirect) |
| [JS逆向必备：这款插件能Bypass Debugger、Hook CryptoJS、抓取路由](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247486181&idx=1&sn=3ace47da643c72cec0d615aeccb955ac&scene=21#wechat_redirect) |
| [上传代码即审计：AI 驱动的自动化漏洞挖掘与 POC 验证平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485488&idx=1&sn=a37acb031febe69db608de53ddee5732&scene=21#wechat_redirect) |
| [AI 原生安全测试平台(CyberStrikeAI)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485208&idx=1&sn=b5181181c1e0800124e3e099706ef2ef&scene=21#wechat_redirect) |
| [多Agent智能协作+40+工具调用：基于大模型的端到端自动化漏洞挖掘与验证系统](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485805&idx=1&sn=8f374a239135f6a753d5cce887f8318b&scene=21#wechat_redirect) |
| [基于DeepSeek的代码审计工具 (Ai-SAST-tool.xjar)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485314&idx=1&sn=56082cd314311ffc15cc0bcf03a395e2&scene=21#wechat_redirect) |
| [基于AI的自主渗透测试平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485127&idx=1&sn=b5eb3fdc1cc23976011e2bca396c1bc7&scene=21#wechat_redirect) |

✦ ✦ ✦

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

0x八月

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

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