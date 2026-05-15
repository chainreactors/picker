---
title: AI Agent渗透测试必备：结构化知识库和方法论（200+技能、600+漏洞）
url: https://mp.weixin.qq.com/s/NE3xOJYmcR1zwadeR62FnA
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:46:50.329596
---

# AI Agent渗透测试必备：结构化知识库和方法论（200+技能、600+漏洞）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODxL2UluHfRvkc3rlpnMwMO0ZeyMoicytHnQqzybTJ3Kja2UylBice3jQ9OO4rSkiaugKKALiboG1govXP0lj66Ex1gYolmibpKPdFSs/0?wx_fmt=jpeg)

# AI Agent渗透测试必备：结构化知识库和方法论（200+技能、600+漏洞）

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# AI Agent渗透测试必备：结构化知识库和方法论（200+技能、600+漏洞）

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  AboutSecurity 是一个覆盖渗透测试全链条、采用 AI Agent 可执行格式的结构化知识库，为安全人员提供**200+技能方法**与**600+漏洞条目**。

## 🚀 一句话优势

 将零散的安全知识转化为 AI 代理可直接调用的**结构化技能**与数据，提升渗透测试的自动化与准确度。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 技能方法论 | 从侦察到后开发，覆盖全流程的200+结构化技能 |
| 词典库 | 按场景分类的用户名、密码、端口、Web目录等词典 |
| 攻击载荷库 | XSS、SQLi、SSRF等主流攻击类型载荷 |
| 漏洞数据库 | 600+按产品分类的漏洞条目，含PoC与利用步骤 |
| MCP服务适配 | 通过context1337将知识库转为AI可查询的API |

## 📸 核心模块

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxOjAP9LNSnvfbO7TrSTibCSeVWAvsGQ7hwPkpG7pG7qrUVYDb8UhHOW7ral3UulkDZrCDGgBhiahV1icXYFLYicVw6NnEYTOCU9N4/640?wx_fmt=png&from=appmsg)

## ✨ 核心亮点

### 1. AI Agent 原生可执行的知识结构

  项目将渗透测试知识按照 **AI Agent 可执行格式** 进行结构化处理。200+ 技能方法不是纯文档，而是可以被 Claude Code 等 AI 代理通过 `sanps` 机制直接同步并调用的技能文件。这意味着，你说一句“侦察目标子域”，AI 代理就能自动定位并执行相关技能，大大缩短从知识到行动的链路。

### 2. 层级化的攻击资源库与词典体系

  项目区分了面向执行的**技能**和面向数据的**词典/载荷**。`Dic/` 目录下，按 `auth`、`port`、`web` 等场景组织词典，例如 `port/` 下包含了针对 mysql、redis、ssh 等 *19种服务* 的专用爆破字典。`Payload/` 则按攻击类型（如 xss、sqli、ssrf）组织，所有数据文件都附带 `_meta.yaml` 元数据，方便 AI 代理按 description 和 `tags` 精准检索。

### 3. 技能与漏洞数据的互补闭环

  项目巧妙设计了 `postexploit/` 与 `Vuln/` 的分工：**技能告诉你“进入后该做什么”**（如权限提升、横向移动），而**漏洞库告诉你“如何进入”**（PoC、受影响版本）。这种设计让整个渗透测试的知识流形成一个闭环，从发现漏洞到利用后的下一步操作，都有对应的结构化内容支撑。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Claude Code skills格式 | 采用 Anthropic 官方定义的技能文件格式 | 可直接被Claude Code等AI代理发现和调用 |
| MCP协议集成 | 通过context1337项目提供MCP服务 | 将知识库转换为标准化API，可被多种AI工具使用 |
| YAML结构化元数据 | 每个字典/载荷目录附带`_meta.yaml` | AI可以按描述、用途、标签精确检索，无需人工翻找 |
| 模块化目录体系 | 技能/Dic/Payload/Vuln/各司其职 | 结构清晰，易于扩展和维护，适合团队协作 |
| 自动化同步脚本 | 提供`sync-claude-skills.sh`脚本 | 一键将技能同步到任何项目中，降低使用门槛 |

## 📖 使用指南

① **准备工作** 克隆仓库到本地 **`git clone https://github.com/wgpsec/AboutSecurity.git`**。如果你是 AI 代理用户，可使用脚本 **`./scripts/sync-claude-skills.sh --target /path/to/your-project`** 将技能同步到你的工作目录。

② **核心操作** 在 AI 代理对话中直接引用仓库路径来使用资源，例如：`“使用 /path/to/AboutSecurity/Dic/auth/ 下的词典爆破SSH”`。或者，部署 *context1337* MCP 服务，运行 `make run` 后，在 Claude Code 中添加 MCP 服务 `claude mcp add aboutsecurity --transport http http://localhost:1337/mcp`，之后即可用自然语言查询。

③ **结果查看** AI 代理会通过 Read/Glob 工具直接读取文件内容并给出结果。在 MCP 模式下，你可以直接 搜索资源（如“查找关键Apache漏洞”），列出载荷（如“列出所有XSS负载”），所有操作都通过对话完成。

## 📖 项目地址

```
https://github.com/wgpsec/AboutSecurity
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