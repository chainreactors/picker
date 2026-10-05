---
title: 冰霄IceSky  ——提示词注入综合工具
url: https://mp.weixin.qq.com/s/Z_UF9tFV4ok1KUoGhbJ7mg
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:52:54.852353
---

# 冰霄IceSky  ——提示词注入综合工具

# 冰霄IceSky ——提示词注入综合工具

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 项目地址

# https://github.com/spindriftpapilio/icesky

**冰霄 IceSky** 是一个面向 AI 安全测试的**提示词注入（Prompt Injection）综合工具**，以纯前端静态 Web 应用形式交付，将文本变换、Unicode 隐写、多轮对话编辑，以及图像、音频、PDF、DOCX、富文本等多模态测试样本生成整合在一个浏览器工具箱中。

**核心定位**：面向 AI 红队 / 安全研究 / 教育场景的一体化测试样本生成器；全部功能在浏览器本地运行（AI 辅助功能除外），无需后端、无需构建。

**技术栈**：Vue.js（本地打包）、原生 CSS（组件化拆分）、FontAwesome 6、PDF.js（含完整 CMap 与标准字体）、OpenAI 兼容 API 客户端（可选 AI 功能）；无 npm、无打包器。

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFz3sK0n72YBPxcDdVKNwS6Rsh9eaxPEWK8PT51cJeiaWVUrHjbZibKz2gcYmBZv2dBd2rhzElps1ibdAn96uMTSlUpy0norUoSiapw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFxUvfLXm0Y1K4Sb2XmSEF0njdsdMic8dJJXnLnyvZFgib9PXDLJ62jwxbuTbrtSkOR5SjKF3hK5vpISLI1dyJzK8S9VILYMNuNX8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFzDSmBwhGdWq1CbxmpyTTdzhice6yS84YxxbexGgEkSJeSjLXlg48Zd2bJOYmwtHuFZ2OzPvXkOtLoiagAUEaib53dFCJpiaFRgVibM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFwiaBRusSw9MUP79X4elfknsXZjE8nO33MLrum8xT2RkZYFGjicMahbhsRZpUB54vwsXicw0RtTcaKY24zAvBy6xNYfia2Whz3T02E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFySa1c6HkzFjX27p4Y90qZp9uZ0Apu19TJib96e9UtdhprjWYl2xxiakVVxWDemiaD7GBsBICNJurKRxKl64LWAicyfTQkRHib2icabg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFyj8vXiaI92GIPK9v2oQeAy8a9z6A6oe2icAbIsYHY9ytGUoPUA52OA2T6MJLpqPFTbTkf5YWLWFB3TtibC7ribRhw3oY9Bky56vds/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFwRDz3zgDHPjO0mO18hCia15fb3Rg2FczIBwpbDb9d0SS8BvNwZGUeufzUZ5tX5k7iaVU5aMHK2jH25Ojb3kwiaB9pC9HeoZunNyI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFxa0pr5ZiakklPW4AZI4CKR5kuIQmgCDUCib9Zk48SJPwwVfBFpKKftyPo0AzFRNwz3MWK8SicMuf1c0ESDQjpm7fdjYEyhLts0nY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFyOFwCBceGnCFN6pLUVMEwVokQ2nicq05jYxaI2lb5cict8L3D9HX9paTE5590gQmRhObzb6XHjxib1G5CUagya33MeKMJW82IOjM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFzGZmyAykMveDQ7yrYATwhC1X17JXKKcFWODAfT1cFsH0ymobsTvQ84xah61gIp4BKUQqhxBPl1Ej18dDF4ooualjETshG5V0s/640?wx_fmt=png&from=appmsg)

## 功能体系

六大模块、21 个内置工具：

| 模块 | 能力 |
| --- | --- |
| 文本变换 | Base64/Hex/URL 等编码、古典密码、Unicode 字形替换、大小写格式转换，支持**组合变换管线** |
| 解码与隐写 | 格式自动识别解码、Emoji 变体选择符隐写、不可见字符、ASCII Smuggler（U+E0000 标签区段隐藏文本） |
| 多模态样本 | 图像 / 音频 / PDF / DOCX / 富文本载体中嵌入注入载荷并导出文件 |
| 对话编辑 | 多轮消息编辑、角色构造、材料与载荷组合、批量样本构造（Sample Builder、Dialog Template） |
| 文本扰动 | Bijection 字符映射、Splitter 文本拆分、Mutation 批量变异、Gibberish 噪声、Tokenade 压力样本 |
| 分析工具 | Tokenizer 计数可视化、Glitch Tokens 异常库、注入技术 Taxonomy 分类参考、Jailbreak Library 越狱库 |

另有 Prompt Craft（AI 生成提示词变体）与 Translate（翻译）两个**需自配 OpenAI 兼容 API** 的可选工具。

##

**零依赖构建的单页应用**，分四层：表现层（`index.html` 约 330 KB，集中定义全部工具面板模板）→ 应用层（`js/app/`：导航、历史、命令、模型配置）→ 工具层（`js/tools/` 21 个工具 + `js/core/` 核心）→ 支撑层（`js/utils/`、`js/data/`、`js/vendor/`）。

关键设计：

1. **工具注册表模式**：`js/core/toolRegistry.js` 为中枢，各工具实现统一基类 `Tool.js` 后登记注册，新增工具无需改框架代码。
2. **数据与逻辑分离**：领域数据独立存放于 `js/data/`——如 `emojiData.js`（约 624 KB）、`injectionTemplates.js`（约 123 KB）、`promptInjectionTaxonomy.js`（约 80 KB）、`glitchTokens.js`（约 38 KB）。
3. **本地优先**：除两个 AI 工具外全部在浏览器内完成，API 凭据仅存 localStorage。
4. **变换管线**：`js/bundles/transforms-bundle.js`（约 229 KB）打包全部变换器，支持多阶段串联扰动。
5. **多模态生成**：PDF Inject 基于本地 PDF.js（含 1 MB worker 与 CMap/字体资源）+ 专用 `pdfinject/config.js` 与 `library.js`；图像/音频走 Canvas / Web Audio API；DOCX/富文本通过拼装 OOXML / HTML 结构导出。

## 部署与使用

零依赖，整个目录上传至任意静态托管即可（GitHub Pages / Cloudflare / Netlify / Vercel / S3+CloudFront / 任意 Web 服务器）。本地运行：`python3 -m http.server 8080` 后打开浏览器即可。

典型工作流示例：

* **隐写注入测试**：Injection Generator 生成载荷 → Emoji/ASCII Smuggler 隐写 → Tokenizer 检查 Token 分布 → Sample Builder 包装为多轮对话样本 → 投喂目标模型。
* **多模态注入**：PDF/Image/Audio Inject 嵌入载荷 → 结合 Taxonomy 与 Jailbreak Library 选技术路线 → 投喂多模态模型评估。

## 特点与局限性

**特点**：零构建零后端、离线可用、隐私友好（数据不出浏览器）、覆盖字符级到文档级的完整注入测试链、工具注册表带来低扩展成本、中英文双语界面与模板。

**局限性**：单文件体积偏大（HTML/CSS 均数百 KB，模板数据硬编码需发版更新）；纯 GUI 无 CLI/API，难接入自动化红队流水线；仓库未见测试、CI 配置及 LICENSE 文件（商用再分发前需确认授权）；AI 功能受第三方接口与账户权限制约。

## 合规声明

工具仅供安全研究与教育用途，使用者应遵守法律法规，建议仅对自有或获书面授权的模型与应用进行测试。

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AGUhPQZ04zyTvSBegohhPkdl4ZiaID39hGjT55M6GNVWWYfpt8Q146OaDEU4xQ0E4VtxLO4zfGia16VE6qHb001g/0?wx_fmt=png)

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