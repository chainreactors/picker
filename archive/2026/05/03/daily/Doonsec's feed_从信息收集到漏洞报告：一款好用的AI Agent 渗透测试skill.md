---
title: 从信息收集到漏洞报告：一款好用的AI Agent 渗透测试skill
url: https://mp.weixin.qq.com/s/DuTi56EjgJxUpOeLBW1URA
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:26:51.219311
---

# 从信息收集到漏洞报告：一款好用的AI Agent 渗透测试skill

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODyhs0L0EoEFWagLzDGAqTS5iaK4CbxDxOEngAeibcGGxY4pFKicvGa47y9Qt9nNMCm0Clo6awIeetHStuKTMnh5icLCVcHuOL4U0Vs/0?wx_fmt=jpeg)

# 从信息收集到漏洞报告：一款好用的AI Agent 渗透测试skill

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 从信息收集到漏洞报告：一款好用的AI Agent 渗透测试skill

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

**claude-code-pentest** 是一款 **纯Python渗透测试自动化Skills套件**，集成43个脚本覆盖侦察到报告全流程，*无需编程基础* 即可运行。

Skills如何进行使用可以参考下面的文章来学习和使用，下面的的文章来自C4安全团队，需要的师傅可以参考来进行学习：

[AI Agent 渗透测试skill实战测试（二）](https://mp.weixin.qq.com/s?__biz=MzkzMzE5OTQzMA==&mid=2247490292&idx=1&sn=c212d4110755e7f8f9a5161455050501&scene=21#wechat_redirect)

## 🚀 一句话优势

 通过 **43个零依赖脚本** 将渗透测试压缩为单域名输入，解决初学者工具链配置复杂痛点。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 域名侦察 | 自动收集子域名与IP信息 |
| 漏洞扫描 | 检测常见安全弱点与入口 |
| 利用链测试 | 串联漏洞验证深度访问 |
| 报告生成 | 输出漏洞赏金式文本报告 |
| 模块化配置 | 通过文本文件自定义扫描项 |

## ✨ 核心亮点

### 1. 零依赖纯Python架构

 套件由 **43个独立Python脚本** 组成，不依赖第三方库或外部工具。你只需安装 Python 3.8+ 即可运行全部功能，*无需配置 nmap、masscan* 等复杂环境。这种设计让 Windows 用户也能在 5 分钟内完成部署，降低了渗透测试的入门门槛。

### 2. 漏洞赏金式报告

扫描完成后自动生成 **结构化文本报告**，包含漏洞描述、风险等级与修复建议。报告格式参考 *漏洞赏金平台标准*，可直接用于提交或内部评审。你只需编辑简单的文本配置文件，即可调整报告模板与扫描深度。

### 3. 模块化工作流

6个主工具按 **侦察→扫描→利用→报告** 顺序编排，每个阶段可独立运行或跳过。通过修改纯文本配置文件选择特定模块，*无需编程知识* 即可定制测试范围。这种设计让不同经验水平的用户都能找到适合的操作粒度。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Python原生 | 纯标准库实现43个脚本 | 零依赖，跨平台兼容 |
| 文本配置 | 通过简单文本文件调整参数 | 非技术人员可修改 |
| 单域名输入 | 仅需提供目标域名启动 | 降低操作复杂度 |
| 利用链验证 | 串联多漏洞测试深度访问 | 发现隐藏攻击路径 |
| 报告模板 | 内置漏洞赏金格式 | 可直接用于提交 |

## 📖 使用指南

① **准备工作**（环境搭建）

从 Release 下载压缩包并解压，确保已安装 Python 3.8+ 并勾选 *添加至 PATH* 选项

② **核心操作**（启动扫描）

在解压目录执行 `python main.py`，输入 *目标域名*，按提示选择扫描模块与深度。工具自动完成 **子域名收集、IP探测、漏洞扫描** 等步骤，通Claude/OpenCode等相关工具调用。

③ **结果查看**（报告分析）

扫描完成后在输出目录查看 **文本格式报告**，包含漏洞详情与修复建议，支持直接用于漏洞赏金提交

## 📖 项目地址

```
https://github.com/KaQus/claude-code-pentest
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

⚠️打广告的勿进，会直接踢掉！！！

| ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzDcbialtDJB2iauRibULjWbzQk2oeHEyuNcGjibhWw6SpJia0RYGY3D7UhMASYr1QPAicb1LaSL1XlDrVowaibjeB41IKYSBHE8z9sN8/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwMu4dL9ZhibwZKibzwdD01Btq6ia2183uH0ibzaGibkr1aribDe1jicrtW0px8pd6Rz1kT7QpTtzfdmicibiaFZHSqI40srWZhLQ9HpR1JY/640?wx_fmt=png&from=appmsg) |
| --- | --- |

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