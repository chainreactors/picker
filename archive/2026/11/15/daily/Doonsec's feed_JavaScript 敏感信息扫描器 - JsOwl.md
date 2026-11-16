---
title: JavaScript 敏感信息扫描器 - JsOwl
url: https://mp.weixin.qq.com/s/UtTJ8aw_mcc7AOSsIM5_OA
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:47:03.671442
---

# JavaScript 敏感信息扫描器 - JsOwl

# JavaScript 敏感信息扫描器 - JsOwl

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

01项目地址

`https://github.com/Spade-sec/jsowl`

02项目介绍

渗透测试的信息收集阶段，JS 文件永远是个宝库——API 端点、内部路由、硬编码的密钥 Token，全藏在前端代码里。但手工翻 JS 的痛苦谁都懂：

`一个 SPA 站点几十个 chunk 要逐个下载分析，
Webpack 打包后的变量名全是混淆过的天书，
正则匹配抓一堆误报，真密钥反而漏掉，
source map 没还原等于白看，
翻完一晚上，收获只有几行 URL 列表。`

**JsOwl** 是一个用 Go 编写的高性能 JavaScript 信息收集与安全分析工具，同时也是一个可复用的 Go 库。它自动收集目标站点的页面、JavaScript、Webpack/RequireJS chunk 与 SPA 运行时资源，通过**正则 + AST（Tree-sitter）双引擎**提取 API 端点、参数、路由和敏感信息（密钥、Token、身份证、内网 IP 等），并生成 JSON 与自包含的交互式 HTML 报告——Web 安全测试、渗透信息收集和攻击面梳理的自动化利器。

![JsOwl](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA19FyVG8oP4pV7Bn1OibetGfJpe0R6NicFJcH7mzK6v3LgjFb6lPz007JKictzqmTY9g6a0Vz50WVRgCkw6BDU3gCTbrSInbpReLzo/640?from=appmsg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=0)

JsOwl

**一句话概括：从 JS 里自动"刨"出 API、路由和密钥，AST 双引擎降误报，兼容 HaE 规则，一个命令跑完出交互式报告。**

03核心亮点

`🕷️ 三种采集模式：direct（高速 HTTP）/ browser（Rod 驱动本地 Chrome 渲染）/ auto（默认，先 direct 后按 SPA 信号自动升级浏览器）
🔍 深度资源发现：递归发现脚本、Webpack chunk、RequireJS 配置、框架路由与 API，支持 source map 还原原始源码
🧬 敏感信息提取：兼容 HaE 规则格式，正则 + AST 双引擎，内置密钥/凭证/指纹规则集
🖱️ 运行时交互：自动填表提交、事件点击、SPA 路由爬取，捕获页面真实发出的 API 请求（可选，默认关闭）
🔐 登录态扫描：--login 打开可见浏览器手动登录后，携带会话 Cookie 完成整批扫描，可不带 -u 在浏览器里自行导航
🤖 AI 辅助分析：-ai 接入大模型做参数完整性与敏感发现评级（可选，需配置 API Key）
📡 MCP Server：通过 Model Context Protocol 把扫描能力暴露给任意 LLM 客户端
📊 多格式报告：JSON + 自包含交互式 HTML 总览与分项报告（API / URL / 敏感信息 / 参数 / 路由 / 资源）+ 纯文本清单`

04快速上手

需要 Go 1.25+ 与 C 编译器（AST 用 Tree-sitter，必须启用 CGO）：

`git clone https://github.com/Spade-sec/jsowl.git
cd jsowl
go build -o jsowl ./cmd/jsowl`

常用姿势一览：

`jsowl -u https://example.com                  # 基础扫描
jsowl -u https://example.com -m browser       # 强制浏览器渲染模式
jsowl --login                                 # 打开浏览器自行导航，登录后扫描当前页
jsowl -l targets.txt -o reports               # 批量目标 + 自定义输出目录
jsowl --check                                 # 检查配置、规则与本地浏览器`

扫描完成后在 `jsowl-report/example.com/` 下生成 `report.html`（交互式总览入口）、`report.json` 与分项报告，脚本和 chunk 也会保存下来供人工深挖。

规则体系直接兼容 **HaE**（BurpSuite 信息提取插件）的规则库文件，存量规则无缝迁移；自动填表算法适配自 projectdiscovery/katana，SPA 站点的运行时交互有成熟实现兜底。

⚠️ 免责声明

注：工具仅供安全研究与学习之用，若将工具做其他用途，由使用者承担全部法律及连带责任，作者及发布者不承担任何法律及连带责任。信息及工具收集于互联网，真实性及安全性自测！！

文章来源：GSDK安全团队  如有侵权，请联系删除。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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