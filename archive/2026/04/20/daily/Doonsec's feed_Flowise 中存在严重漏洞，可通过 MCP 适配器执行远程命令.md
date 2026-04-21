---
title: Flowise 中存在严重漏洞，可通过 MCP 适配器执行远程命令
url: https://mp.weixin.qq.com/s/OoRfZLH7Cp_wFOsPTqdT7w
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:45:43.767742
---

# Flowise 中存在严重漏洞，可通过 MCP 适配器执行远程命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PTkdxV3BV4w1j9MqPGX2Dtk52s2yt4t64zTJRuDAswGzGk0No7xibCGbMIXaqCX14Iru4lPicy7M4qyHZhBWVzs3Cib7OicbeQj4Q/0?wx_fmt=jpeg)

# Flowise 中存在严重漏洞，可通过 MCP 适配器执行远程命令

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

OX Security 发现 Flowise 和多个 AI 框架中存在严重漏洞，使数百万用户面临远程代码执行 (RCE) 的风险。

该缺陷源于模型上下文协议 (MCP)，这是由 Anthropic 开发的广泛用于人工智能代理的通信标准。

与典型的软件漏洞不同，此漏洞源于Anthropic 官方 MCP SDK（涵盖 Python、TypeScript、Java 和 Rust）中嵌入的架构设计决策。

任何基于 MCP 基础架构进行开发的开发者都会在不知不觉中继承这种风险，这意味着攻击面不仅限于单个平台，而是会波及整个 AI 供应链。

## **MCP核心架构缺陷**

该漏洞使攻击者能够在易受攻击的系统上执行任意命令，从而直接访问敏感用户数据、内部数据库、API 密钥和聊天记录。

OX Security 在研究过程中成功地在六个生产平台上执行了实时指令。Flowise 是一款流行的开源 AI 工作流构建器，是受影响最严重的平台之一。

研究人员发现了一种针对 Flowise 的“加固绕过”攻击途径，这表明即使配置了额外保护措施的环境仍然可以通过 MCP 适配器接口被利用。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7PviaLIbUhPnQyTpAlQCaLcZFxxLosHNCLEJy9lDSlHdUUXCNyVabVyVEibAD0U1nmWq5Ros9GQhrlvXQJmF6dvhq9Tokt39BuwU/640?wx_fmt=png&from=appmsg)

更广泛的爆炸范围令人担忧：超过 1.5 亿次下载，超过 7000 个可公开访问的服务器，以及整个生态系统中估计 20 万个易受攻击的实例。

迄今为止，至少已发布了 10 个 CVE，涵盖了包括 LiteLLM、LangChain、GPT Researcher、Windsurf、DocsGPT 和 IBM 的 LangFlow 在内的平台中的关键漏洞。

已确认存在四个不同的剥削家族：

* 在流行的AI框架中存在未经身份验证的UI注入问题。
* 在 Flowise 等“受保护”环境中加固旁路。
* 在Windsurf和Cursor等AI IDE中实现零点击提示注入。
* 恶意 MCP 服务器传播：在测试期间，11 个 MCP 注册中心中有 9 个被成功感染。

## **人类活动减少协议层面的修复**

OX Security 曾多次建议 Anthropic 安装根级补丁，这些补丁本可以保护数百万下游用户。

安特罗皮克公司拒绝了这一请求，并称这种行为“在意料之中”。该公司在得知研究人员打算发表研究结果后，并未提出异议。

安保团队应立即采取行动：

* 阻止与敏感API或数据库连接的AI服务在公共互联网上公开暴露。
* 将所有外部 MCP 配置输入视为不可信，并限制用户输入到达 StdioServerParameters。
* 仅从经过验证的来源（例如官方GitHub MCP Registry）安装 MCP 服务器。
* 在沙盒环境中以最小权限运行启用 MCP 的服务。
* 监控人工智能代理工具的调用情况，以发现异常的出站活动。
* 立即将所有受影响的服务更新到最新的补丁版本。

OX Security 为其客户提供了平台级保护，将包含用户输入的 STDIO MCP 配置标记为可操作的补救措施。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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