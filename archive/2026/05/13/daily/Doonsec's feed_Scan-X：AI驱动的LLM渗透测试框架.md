---
title: Scan-X：AI驱动的LLM渗透测试框架
url: https://mp.weixin.qq.com/s/SH8ZsSR88G-PzM8QftBWwQ
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:41:51.828008
---

# Scan-X：AI驱动的LLM渗透测试框架

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODxHeedGmYKDHTx0nW3GurU4IYwuH6dRkcqIejwibqG6P2CfJlP8jxtTZj9GGp9YBYicvNVyaiazD0aMymNZBPluhQ8ibI1S5w1jCzU/0?wx_fmt=jpeg)

# Scan-X：AI驱动的LLM渗透测试框架

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# Scan-X：AI驱动的LLM渗透测试框架

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

**Scan-X** 是 Go 开发的 **AI 驱动渗透测试框架**，集成 *12 个智能 Agent* 与 Kali 原生 CLI，适用于智能化安全评估与自动化攻防场景。

## 🚀 一句话优势

  通过 **Kali-Native Agent** 直调 CLI，LLM 原生调用工具，解决 MCP 封装冗余。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| AI智能扫描 | 12个Agent覆盖SQLi、XSS、RCE等漏洞 |
| Kali原生CLI | Agent直调系统命令行工具 |
| 传统规则扫描 | 高速基础检测保障覆盖 |
| 智能爬虫 | 自动化接口发现与JS审计 |
| Burp集成 | 联动Burp Suite深度测试 |

## 📸 运行截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODw8p9dUiaBMnYhY4LCybJqS0qvxKgtQsqP9U1XtgSen7icicS3icvmbicSsib4Gb0ia50Y254bc667omr4515zcYzHt54lUQiarfxUnPVk/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzsUPFB6kmUmQ4VnH6DL430pjPjZDGROvQXAWuAQ69MgrTD4JqUzNC60IK7Th5HXtERdveAg02p2YblpIuP3diaCicT1U902oPUQ/640?wx_fmt=png&from=appmsg)

## ✨ 核心亮点

### 1. Kali-Native Agent 直调 CLI

  Scan-X 引入 **Agent 直调命令行架构**，让 LLM 在原生 Kali 环境中直接调用 *nmap、sqlmap、ffuf* 等已有工具知识。相比传统 MCP 的过度封装，这种设计保留了 *复杂交互能力* 与 *持续状态管理*，让真实渗透测试中高度迭代的工作流得以顺畅执行。

### 2. 12 个 AI 智能扫描 Agent

  内置 **SQL\_AIagent、XSS\_AIagent、RCE\_AIagent** 等 12 个专项 Agent，覆盖从注入到越权、从 WAF 绕过至 CVE 验证的完整攻击面。每个 Agent 具备 *上下文感知* 与 *对抗性 Payload 生成* 能力，例如 XSS Agent 可分析反射型、存储型及 DOM 型的具体上下文，而非仅依赖固定模板。

### 3. 双轨扫描架构

**AI 智能扫描 + 传统规则扫描** 并行运行。传统模块基于 *finger.json 指纹库* 与高效正则完成快速初筛，AI Agent 负责深度逻辑漏洞挖掘。实测相比纯人工测试，效率提升 *10 倍*，漏洞发现率提升 *60%*，测试覆盖率提升 *3 倍*。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Go语言 | 高性能并发原生支持 | 适合大规模分布式扫描 |
| LLM深度集成 | 智能Payload生成与逻辑推演 | 发现传统规则难以覆盖的漏洞 |
| Kali原生调用 | 直接执行系统CLI工具 | 避免MCP封装带来的交互限制 |
| 自然语言规则 | DIY Agent支持自定义检测 | 降低非编程人员使用门槛 |
| 本地模型适配 | 支持Ollama本地部署 | 满足数据不出域的合规要求 |

## 📖 使用指南

① **准备工作**（环境配置）下载对应版本，如需本地模型支持，配置 Ollama 并在配置文件中调整延时参数。商业版本需联系获取授权与技术支持

② **核心操作**（启动扫描）选择 **AI 智能扫描** 模式，输入目标域名后 Agent 自动规划测试路径；或启用 **传统扫描** 模块进行基于规则的高速初筛。通过 *任务进度看板* 实时监控各 Agent 执行状态，使用 *AI 对话助手* 随时调整测试策略

③ **结果查看**（分析与导出）在 **数据包扫描** 面板查看流量深度分析结果，AI Agent 会标注 *漏洞类型、利用路径、修复建议*。支持导出结构化报告，Burp Suite 集成模式下可直接将发现发送至 Repeater 验证

## 📖 项目地址

```
https://github.com/kk12-30/Scan-X
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