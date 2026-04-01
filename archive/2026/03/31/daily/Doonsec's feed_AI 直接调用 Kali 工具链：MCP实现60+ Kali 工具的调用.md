---
title: AI 直接调用 Kali 工具链：MCP实现60+ Kali 工具的调用
url: https://mp.weixin.qq.com/s/kVF9GB0R6x6r_9hDZCzapQ
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:42:18.293417
---

# AI 直接调用 Kali 工具链：MCP实现60+ Kali 工具的调用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODxS9UHyytozTRDfGO7lzHomIn3BicXE5lxic8e6bjib923Hnea5OWWDw2bmoTkhIFaqhnj5m4GtbGLdhX185CXBwJsqM6axxRd6S0/0?wx_fmt=jpeg)

# AI 直接调用 Kali 工具链：MCP实现60+ Kali 工具的调用

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器中沉浸阅读

# AI 直接操控 Kali 工具：MCP实现60+ Kali 工具的调用

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  Kali-Mcp-Toolkit 是 **Kali Linux 的 MCP 协议适配层**，将 60+ 安全工具通过 **Model Context Protocol** 暴露给 Claude、Warp 等 AI 客户端，实现 AI 驱动的自动化渗透测试与安全审计，面向**安全研究员**与**渗透测试工程师**。

## 🚀 一句话优势

**AI 直接调用 Kali 工具链**，通过自然语言完成**信息收集到报告生成**的全流程渗透测试。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 工具引擎 | 执行 60+ Kali 工具，12 大分类，风险分级 |
| 交互式终端 | PTY 会话、异步读写、反弹 Shell 监听 |
| 代码工坊 | 12 种语言沙箱执行、依赖自动安装 |
| MCP 资源 | 系统信息、工具目录、网络接口暴露 |
| 工作流模板 | 信息收集、Web 渗透、CTF、应急响应 |

## ✨ 核心亮点

### 1. 自然语言驱动渗透测试

  通过 **MCP 协议**将 nmap、sqlmap、nikto、gobuster 等 60+ Kali 工具封装为标准化的 AI 可调用的 **exec\_tool** 接口。AI 客户端（如 Claude、Warp）无需理解工具命令行参数，只需通过自然语言描述目标（如"对 192.168.1.100 进行 Web 渗透测试"），系统即可自动编排 **nmap 端口扫描 → whatweb 指纹识别 → nikto 漏洞扫描 → gobuster 目录爆破**的完整工作流，并自动汇总结果生成报告。

### 2. 企业级安全防护体系

  针对 AI 自动执行安全工具的高风险场景，构建了**五层防护**：**API Key + JWT 双认证**（细粒度作用域控制）、**输入过滤与危险命令阻断**（默认阻断 rm -rf、mkfs 等）、**速率限制防滥用**、**进程隔离与超时控制**（SIGTERM→SIGKILL 级联）、**JSON Lines 审计日志**。高风险工具（如 msfconsole、mimikatz）与反弹 Shell 默认**显式关闭**，需手动开启并配置白名单。

### 3. 交互式终端与代码执行

  支持创建 **PTY 伪终端会话**，AI 可实时读取终端输出缓冲区，实现交互式工具（如 msfconsole）的自动化操作。配套 **CodeForge 模块**提供 12 种语言的沙箱代码执行环境，支持依赖自动安装，满足渗透测试中的**漏洞验证脚本编写**与**后渗透工具定制**需求。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| FastMCP 框架 | 原生 MCP 协议服务端 | 标准化工具暴露，多客户端兼容 |
| Pydantic v2 | 配置校验与数据模型 | 类型安全，环境变量自动映射 |
| PTY + asyncio | 伪终端异步会话 | 支持交互式工具自动化 |
| 信号量并发 | 进程池控制工具执行 | 防止资源耗尽，超时强制终止 |
| 路径安全 | 符号链接解析与穿越防护 | 沙箱工作区隔离 |
| 审计日志 | 异步 JSON Lines 轮转 | 操作可追溯，合规审计友好 |

## 📖 使用指南

① **准备工作**：在 Kali Linux 上执行 git clone 克隆仓库，创建 Python 3.11+ 虚拟环境后运行 pip install -e ".[dev]"。编辑 **config/default.yaml** 配置 *API Key* 与 目标白名单，高风险工具保持默认关闭。

② **核心操作**：本地测试执行 kalimcp stdio 启动 stdio 模式，或在 Claude Desktop 配置中指向该命令。远程部署使用 kalimcp serve --host 0.0.0.0 --port 8443 开启 HTTP 模式，配合 systemctl enable kalimcp 配置 systemd 自启。

③ **结果查看**：AI 客户端中直接输入渗透测试需求（如"扫描 192.168.1.1 的开放端口"），系统自动调用对应工具并返回**结构化结果**。复杂任务（如 Web 渗透）AI 会自动编排多工具执行，最终通过 **code\_create** 生成 *report.md* 报告文件。

## 📖 项目地址

```
https://github.com/trymonoly/Kali-Mcp-Toolkit
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

| ![img](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODwHdUbwzDLq3nh7hplKZNDBERhMYooic5cPGwPHEJRonMYCoupeaa6fPuwOKehMek9HTEvnLaG0uuiaScGxWWmibtK9XNFHF4PJD0/640?wx_fmt=jpeg&from=appmsg) | ![img](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwTIuKGmnGNWdp04KFRDHLuy2sn430a7pFSLwaOhaAb2sddKZ3uDapQ5II45nXqiaUicl8IXcdcpazmOVgV0o1v63mbpXicFlZYibQ/640?wx_fmt=png&from=appmsg) |
| --- | --- |
| ![img](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODxHicicgIE0gTVhia5o7wNZiaPBibHFSAbvchW91fT05Nhp3rnNNDmoiauT4jK4JBicGHSBwFvcABEjrMB9fhnQc7xGkVx2t52CKzLW4k/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L9cic5ql9ODzCtog7ElLXnrLg7t9j99DftdLLjjVKFwP6unsUPX1EquflicE51wMFjB3zIBWLf6W3qFHA5modicNn3XbwJE8roDq7njXZRfjuo/640?wx_fmt=jpeg&from=appmsg) |

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