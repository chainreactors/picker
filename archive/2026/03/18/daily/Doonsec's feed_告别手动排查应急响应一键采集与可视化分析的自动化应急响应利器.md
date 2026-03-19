---
title: 告别手动排查应急响应一键采集与可视化分析的自动化应急响应利器
url: https://mp.weixin.qq.com/s/DXNdBHCom1VH5IyblTMsIg
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:14:49.871994
---

# 告别手动排查应急响应一键采集与可视化分析的自动化应急响应利器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODwTArhbKYQguTSp30zKKcPepts6hBrAvBt32dv4GOfEtpSCoSHo8l0iaY96SZ6eb9X3iavFSHXnLXV7MWgrSz2r8fZdG7F0iasRoM/0?wx_fmt=jpeg)

# 告别手动排查应急响应一键采集与可视化分析的自动化应急响应利器

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# 告别手动排查应急响应一键采集与可视化分析的自动化应急响应利器

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

Getfact 是跨平台自动化应急响应工具，支持一键采集**27项主机安全数据**，通过*加密报告*与可视化GUI实现快速入侵排查。

## 🚀 一句话优势

**2分钟完成27项数据采集**，跨平台GUI可视化应急响应。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 一键采集 | 27项主机安全数据自动获取 |
| 跨平台支持 | Windows/Linux/macOS/麒麟统一采集 |
| 加密传输 | AES-256-GCM加密JSON报告 |
| GUI可视化 | 搜索排序分页分析取证信息 |
| 多语言界面 | 中英双语一键切换 |

## 📸 运行截图

| 截图位置 | 描述 |
| --- | --- |
| 概览仪表盘 | 加载报告后27个模块数据统计总览![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzk9pwqV3X5C1JkvnkgqJLqkutic8l7BB0UeC3zDaevreImYPqPeTgnQryr4rqlW81Lq37l9WAvXwt82ZX5BCpmDgWTYBQmp4kE/640?wx_fmt=png&from=appmsg) |
| 进程列表 | 显示CPU/内存/磁盘IO的进程详情表格![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODy9mzCWEehW36PYM3ZpuT8z4ENkRXjgAQXicr5TauPicNPHVa9LKdxqgGBQEkjyfK0wtDpg5HkW4OC2N6MroqehkEUC7pmYia3QP4/640?wx_fmt=png&from=appmsg) |
| 网络连接 | TCP/UDP连接详情与协议筛选界面![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzVbnibDazdPjdaqoesib8rJjgHiboRttKq1hUU7LdhPHEViaVgDHN9GC1icT6RzvCSS8q4fHDvdZrYzNlUwDicSNCLPoXewKwickZx0g/640?wx_fmt=png&from=appmsg) |
| 防火墙规则 | 完整规则列表与搜索功能展示![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyAiaVAGMCGXPR53iceXJNEA3An8wPPKjqXe3eUO5E811Hg4krzZjU75QAwBloIcxDRS9XdV3elLP3z9AH2uqzibefTDrwg5GeKds/640?wx_fmt=png&from=appmsg) |
| 硬件信息 | CPU/GPU/内存/磁盘信息一览![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyJGZPTPU2UofFh0mVZl8m9jLaZvwCuP6X0exPJXI0Uz88moZJuoNibZ1OjZicxd6x9UyV97MMGlxOGkLQPeG1azJU5xF8mePfow/640?wx_fmt=png&from=appmsg) |

## ✨ 核心亮点

### 1. 27项深度采集

Getfact 涵盖系统信息、*进程服务*、**网络连接**及取证数据（剪切板、Prefetch、USB记录、浏览器历史等），比传统脚本覆盖更全，无需多工具拼凑。

### 2. 加密与可视化分离

Agent生成AES-256-GCM加密报告，通过*GUI端*解密分析，实现**采集-分析物理隔离**，保护敏感现场数据不外泄。

### 3. 跨平台一致性

基于Go语言实现Windows、Linux、macOS及*麒麟*系统统一采集逻辑，告别不同平台命令差异导致的排查碎片化。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Go Agent | 单文件可执行程序 | 无依赖，管理员权限即可运行 |
| Wails GUI | Go+Vue3跨平台桌面端 | 现代化界面，WebView2渲染 |
| AES-256-GCM | 采集报告加密存储 | 防止传输与存储泄露 |
| gopsutil | 系统信息采集库 | 跨平台硬件/进程数据获取 |
| 物理隔离 | 采集端与分析端分离 | 符合应急响应操作规范 |

## 📖 使用指南

① **准备工作**：在目标主机下载对应平台Agent（Windows/Linux/macOS/麒麟），建议以*管理员/root*权限运行。

② **核心操作**：执行**agent.exe**或./agent\_linux\_amd64一键采集，生成*主机名\_时间戳.json*加密报告文件。

③ **结果查看**：在分析主机运行**getfact-gui.exe**，加载AES加密报告，通过GUI搜索、排序、分页查看27项数据，支持*Dark/Light*主题切换。

## 📖 项目地址

```
https://github.com/Parad0xss/Getfact
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