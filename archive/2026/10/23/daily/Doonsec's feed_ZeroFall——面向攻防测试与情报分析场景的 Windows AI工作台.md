---
title: ZeroFall——面向攻防测试与情报分析场景的 Windows AI工作台
url: https://mp.weixin.qq.com/s/dAz_qqVtJlnHLPwrD_8b3A
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:45:15.992393
---

# ZeroFall——面向攻防测试与情报分析场景的 Windows AI工作台

# ZeroFall——面向攻防测试与情报分析场景的 Windows AI工作台

一个人挺好
一个人挺好

一个人挺好 wa

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 项目地址

https://github.com/0ofo/zerofall

## 项目简介

**ZeroFall（中文名：烬）** 是一款面向**攻防测试与情报分析**场景的 Windows 桌面工作台。它将**类 Burp Suite 的 HTTP 流量截获、检视与重放**能力，与**资产测绘、SQL 分析、AI 助手、交互式终端**整合到同一个项目中，避免在多个工具之间来回倒数据。

核心理念：**打开文件夹即项目**。侦察结果、流量记录与终端记录全部落在项目本地数据库（`.zerofall.db`）中，可直接在同一工作区内用 SQL 和 AI 进行分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFxaoica8B13phIXAAaIMmOwPtSLtZfdSmZyhfkTk3b99wsNfFF8JRylTiaQ0JyiaRpyQqZRny2jac505LMcDgLG5YwbXrFhu2PgTE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFylH0QHjq1YJIicsEaRbGI3Xw7Jgvp7AxOfJ5VrwMRuMz3LNhmeM2g3KuicAbgB37MWsJAicO10vauoTw7QK2cSCgiclzRN2rXF45U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qqiaD4wiajgFwYZq8oCyOme2z8IEkTPHLrynic8PR6GuO9rxvCIoxkibcXF8sbh7RfNjJQLcRHOAJupibyGS0orFOm7JZ68icO14icw7mdyae03NUs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qqiaD4wiajgFwV0rr2micFdsYX0VmJAtH1Gjne7kyw6QNgKCUtjHJOJ2s7fwko83IWrEuroBZic24Y0LuDX7Vc3lLHKRwiaOH3yITCWujlicUCxMw/640?wx_fmt=png&from=appmsg)

---

## 核心特性

| 能力 | 说明 |
| --- | --- |

|  |  |
| --- | --- |
| **HTTP 流量（类 Burp）** | 内置浏览器经本地 Fluxzy 网关截获流量，历史记录 SQLite 持久化；支持检视、重放、Intruder、Decoder/Diff 等 HTTP 工作流；网站树按会话组织请求 |
| **项目管理** | 打开工作目录作为项目，侧边栏文件树浏览，数据文件索引入库 |
| **SQL 分析** | 内置 SQL 编辑器与结果表格，直接查询项目数据库 |
| **文件编辑** | 基于 AvaloniaEdit 的编辑与保存；支持 Markdown 等文件预览 |
| **资产测绘** | FOFA / Hunter / Quake / Shodan 等多源聚合、去重与入库 |
| **AI 助手** | OpenAI 兼容 API，WebView 流式对话，内置工具与 MCP，可联动终端与项目数据 |
| **交互式终端** | 多会话 PTY，可与 AI 协同工作 |
| **代理** | 本地拦截网关，与内置浏览器及出站请求联动 |

###

* **类 Burp Suite**：内置浏览器 + 本地拦截代理，HTTP(S) 流量全量入库；
* **一张工作台**：测绘、抓包、查库、跑命令、问 AI 不必切换工具；
* **从源码运行**：基于 .NET SDK 构建，代码便于阅读、修改与二次开发。

---

## 界面布局

主界面采用**五区域 Dock 布局**，一屏协作：

1. **资源树**（左侧）— 浏览项目文件，双击表或文件在中间打开；
2. **浏览器**（中间）— 多标签页访问网站并抓包分析；
3. **终端 / 网络监控**（底部）— 运行命令、查看 HTTP 流量；
4. **AI 面板**（右侧）— 与 AI 对话、查询数据、执行工具；
5. **资产侦察**（左侧面板）— 聚合 FOFA、Hunter 等查询与端口扫描。

---

## 环境要求

| 依赖 | 要求 |
| --- | --- |

|  |  |
| --- | --- |
| 操作系统 | Windows 10 / 11（x64） |
| .NET SDK | **.NET 10 SDK** |
| WebView2 | Microsoft Edge WebView2 Runtime（浏览器、AI 聊天与流量相关功能需要） |
| Node.js | 仅修改 AI 聊天前端 `ai-chat-web` 时需要 |

---

## 构建与运行

### 从源码构建

```
dotnet restore
dotnet build src/ZeroFall.App/ZeroFall.App.csproj
dotnet run --project src/ZeroFall.App/ZeroFall.App.csproj
```

### 修改 AI 聊天前端后重新构建

```
cd src/ZeroFall.AiPanel/ai-chat-web
npminstall
npm run build
cd../../..
dotnet build src/ZeroFall.App/ZeroFall.App.csproj
```

---

## 快速上手

1. **打开文件夹**：启动后选择一个工作目录作为项目；
2. **配置设置**：在设置中按需配置 AI API、资产测绘 Key、代理等；
3. **开始抓包**：点击 TopBar 地球图标（或 视图 → 新建浏览器标签）新建浏览器标签页，在底部「网络监控」查看流量；
4. **HTTPS 明文**：在 设置 → 代理 中开启 **HTTPS 解密**，并信任 Fluxzy 根证书；
5. **继续分析**：用 SQL 编辑器、AI 面板或终端对项目数据做进一步分析。

> 使用 AI、资产测绘、MCP 等功能前，请先在设置中完成相关配置。各测绘源 API Key 需用户自行申请，费用与配额以各平台为准。

---

## 技术栈概览（基于源码结构推断）

| 模块 | 技术 |
| --- | --- |

|  |  |
| --- | --- |
| 桌面框架 | .NET 10 + Avalonia（跨平台 UI 框架） |
| 代码编辑 | AvaloniaEdit |
| 拦截代理 | Fluxzy（本地 HTTPS 拦截网关） |
| 数据存储 | SQLite（项目库 `.zerofall.db`） |
| AI 面板 | WebView2 + `ai-chat-web`（Node.js 前端构建） |
| AI 接口 | OpenAI 兼容 API + MCP |
| 终端 | 多会话 PTY |

---

## 免责声明

本软件仅供**授权**的安全测试、研究与学习使用。使用者须遵守当地法律法规，对使用本软件产生的一切行为自行负责；向第三方测绘平台发起的查询及产生的费用由使用者自行承担。

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