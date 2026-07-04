---
title: 开源CVE挖掘利器：AI自动审计并生成CVE报告，7天覆盖14个项目挖出30个漏洞
url: https://mp.weixin.qq.com/s/V1o2q8CDlZcqOJc8BxC4rA
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:40:01.399850
---

# 开源CVE挖掘利器：AI自动审计并生成CVE报告，7天覆盖14个项目挖出30个漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODw4K6RXz9wsegpvS6AlgML4Z7b0UL88hXcBxKhJ4dEPF4G3WBdyhnAzMsWcrJo23t9t287vK1icNs8tTusEe4w0hf20l7JvdpJY/0?wx_fmt=jpeg)

# 开源CVE挖掘利器：AI自动审计并生成CVE报告，7天覆盖14个项目挖出30个漏洞

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 开源CVE挖掘利器：AI自动审计并生成CVE报告，7天覆盖14个项目挖出30个漏洞

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除，*****推荐的Skills/MCP/工具，建议大家先进行检测分析或者在沙箱/虚拟机等使用确保无误后，在进行日常工作或者本机使用，避免后门或者投毒受到影响。***

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  AutoCVE 是一款全流程自动化CVE挖掘平台，从 **项目筛选、仓库导入、审计任务创建、Agent漏洞挖掘到CVE申报报告生成**，一键完成。适用于 *安全研究员* 和 **代码审计团队**。![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwn5oDXh51NEDm7JAiayLpM7weqHEI05icuia2pIwHFRhjvbcQEF3q0JP4mZibhkuWbIIEDPyhlvUksSSN3fwrrzPrLS0XbT6ZGwHs/640?wx_fmt=png&from=appmsg)

## 🚀 一句话优势

  7天挖出30个CVE，Multi-Agent协同实现CVE挖掘全链路自动化。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 一键CVE挖掘 | 从项目筛选到报告生成全自动化 |
| Multi-Agent协同 | 多个专用Agent分工协作完成审计 |
| 三种审计模式 | 增强扫描、智能审计、综合审计灵活选择 |
| 智能漏洞管理 | 全生命周期跟踪，支持导出CVE报告 |
| Skills扩展 | 支持自定义审计技能和规则 |

## ✨ 核心亮点

### 1. 7天产出30个CVE，实战验证有效

  在为期一周的测试中，AutoCVE共发现并提交 **30个安全漏洞**，覆盖 *14个开源项目*，最高CVSS评分 **9.9**。涉及Chartbrew、Lemmy、typebot.io、Tautulli等知名项目，涵盖越权、SSRF、SQL注入、RCE等关键漏洞类型。

### 2. 专为CVE挖掘设计的Finding Agent

**Finding Agent** 是AutoCVE的核心审计能力，专为CVE挖掘场景设计。它基于 **ReAct Loop** 状态机运行，支持专项工具调用和 **Nudge纠偏机制**，最终通过 **FinalizeFinding结构化终止** 机制输出符合CVE申报条件的 *高价值漏洞*。相比通用扫描器，更注重漏洞的 *可复现性和利用价值*。

### 3. 三种审计模式按需选择

  AutoCVE提供三种审计模式适应不同场景：**增强扫描**（Scan→Triage）快速分析工具扫描结果并过滤误报，适合快速摸底；**智能审计**（Finding）深度挖掘高价值漏洞，适合CVE和0Day研究；**综合审计**（Scan→Triage+Finding）融合工具扫描与源码分析，适合 *全量审计*。用户可根据目标灵活切换，兼顾效率与深度。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| FastAPI后端 | 高性能Python异步框架 | 支持高频并发API请求 |
| React前端 | 现代Web用户界面 | 交互流畅，支持实时审计跟踪 |
| PostgreSQL数据库 | 关系型数据存储 | 保证漏洞数据的一致性和查询效率 |
| ReAct Loop状态机 | Agent推理-行动循环 | 结构化控制Agent行为，避免发散 |
| Nudge纠偏机制 | 当Agent偏离目标时主动修正 | 提升审计结果的准确性与稳定性 |
| Orchestrator调度 | 统一协调多个Agent工作流 | 分工明确，协同高效 |

## 📖 使用指南

① **准备工作**：确保环境已安装 **Docker** 和 **Docker Compose**。一键部署命令：`curl -fsSL https://raw.githubusercontent.com/larlarua/AutoCVE/v1.0.3/docker-compose.prod.yml \| docker compose -f - up -d`。启动后，前端服务访问 **http://localhost:3000**，后端API访问 **http://localhost:8000**。

② **核心操作**：在界面中 **配置模型**（支持多种大语言模型），然后 **导入项目**（支持Git仓库URL直接导入）。创建审计任务时，根据目标选择 **三种审计模式** 之一：增强扫描适合快速分析，智能审计适合CVE研究，综合审计适合全量审计。在审计过程中可通过前端 *实时跟踪Agent执行进度*。

③ **结果查看**：审计完成后，在 **漏洞管理** 模块查看所有发现的安全漏洞，每个漏洞包含详细的技术描述和复现步骤。可直接 **导出或编辑CVE申报报告**，复制报告内容并提交至CVE申请平台即可完成后续流程。系统还支持 **Skills扩展**，允许自定义审计规则以适应特定场景。

## 📖 项目地址

```
https://github.com/larlarua/AutoCVE
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

⚠️打广告的勿进，会直接踢掉！！！

| 网络安全全栈知识库 | 钉钉漏洞威胁情报群 |
| --- | --- |
| ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzDcbialtDJB2iauRibULjWbzQk2oeHEyuNcGjibhWw6SpJia0RYGY3D7UhMASYr1QPAicb1LaSL1XlDrVowaibjeB41IKYSBHE8z9sN8/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwMu4dL9ZhibwZKibzwdD01Btq6ia2183uH0ibzaGibkr1aribDe1jicrtW0px8pd6Rz1kT7QpTtzfdmicibiaFZHSqI40srWZhLQ9HpR1JY/640?wx_fmt=png&from=appmsg) |

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