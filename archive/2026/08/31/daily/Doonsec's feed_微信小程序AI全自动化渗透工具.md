---
title: 微信小程序AI全自动化渗透工具
url: https://mp.weixin.qq.com/s/CE6Bkg60qCObXz6mJpBpfQ
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:58:44.813840
---

# 微信小程序AI全自动化渗透工具

# 微信小程序AI全自动化渗透工具

hello-xiaoniao
hello-xiaoniao

HACK之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

### 工具介绍

这是一个面向已授权调试场景的本地工作流整合包，把下面三部分串成了一套更容易复用的流程：

* `偏移提取工具/：从本机最新 WMPF 运行时提取偏移`
* `WMPFDebugger/：负责 Frida 注入`
* `e0e1-wx/：负责调试引擎、GUI 和 MCP Server`

这次整理的目标很明确：让项目不只“我自己能跑”，而是“别人拿到仓库后也更容易跑起来、排障、更新和继续维护”。

`QUICKSTART.md` 适合第一次上手时照着跑，`CHANGELOG.md` 记录版本变化。

### 安装

### 1. 偏移提取工具

```
cd 偏移提取工具pip install -r requirements.txt
```

验证：

```
python extract_wmpf_offsets.py --version 25297
```

### 2. WMPFDebugger

```
cd WMPFDebuggernpm installnpm install frida@16.6.6    # 必须锁 v16.6.6，否则 ESM 不兼容！npm install -g ts-node       # 全局安装 ts-node
```

> **重要：** frida 的二进制文件与 Node.js 版本强绑定。
> 如果你使用 Node.js v20，frida@16.6.6 会自动下载对应的二进制。
> 如果你使用 Node.js v22+，frida 会报 `NODE_MODULE_VERSION` 错误。
> 解决方案：降级到 Node.js 20 LTS，或使用 `nvm` 管理版本。

验证：

```
node -e "const f = require('frida'); console.log('frida OK:', typeof f.getLocalDevice)"# 输出: frida OK: function
```

### 3. e0e1-wx

```
cd e0e1-wxpython -m venv .venv.\.venv\Scripts\Activate.ps1pip install -r requirements.txt
```

### 启动流程（关键！顺序不能错）

### 完整启动顺序

```
第 1 步：启动 WMPFDebugger（Frida 注入）         双击 WMPFDebugger/一键启动.bat                  或: cd WMPFDebugger && node -r ts-node/register src/index.ts                  等待出现: [frida] script loaded, WMPF version: xxx
第 2 步：启动 e0e1-wx 引擎（debug server + proxy server）         打开新终端，cd e0e1-wx                  运行: python start_engine.py                  等待出现: [OK] debug server (9421) + proxy server (62000) started
第 3 步：打开微信小程序         在微信中点击打开一个小程序（不是拖拽）                  小程序会自动连接到 debug server (9421)
第 4 步：启动 e0e1-wx GUI（MCP Server）         在 e0e1-wx 目录运行: python main.py                  MCP Server 在 49999 端口自动启动
第 5 步：连接 Claude Code         注册 MCP: claude mcp add wxcdp --transport http http://127.0.0.1:49999/mcp                  开始渗透测试
```

### **重要：** 如果顺序搞反了（先开小程序再启动引擎），小程序不会自动连接 debug server。 此时需要关掉小程序重新打开，或者重启微信。

### 微信更新后的操作

```
第 1 步：双击 WMPFDebugger/auto-extract.bat         （自动检测最新 flue.dll，提取偏移，写入 config 目录）                  或手动:                  python 偏移提取工具/extract_wmpf_offsets.py --version 新版本号
第 2 步：按上面的启动流程重新启动
```

### 端口

| 端口 | 用途 | 由谁启动 | 必须先启动 |
| --- | --- | --- | --- |
| 9421 | debug server（小程序连接） | `start_engine.py` | WMPFDebugger |
| 62000 | CDP 代理（DevTools 连接） | `start_engine.py` | WMPFDebugger |
| 49999 | MCP Server（AI 工具链） | `python main.py` | 引擎 + 小程序 |

### 修改说明

### WMPFDebugger 修改内容

| 文件 | 修改 |
| --- | --- |
| `src/index.ts` | **Frida-only 模式** — 不启动 debug/proxy server，由 e0e1-wx 接管 |
| `src/index.ts` | **轮询等待** — frida\_server 每 2 秒重试，最多等 60 秒 |
| `src/index.ts` | **异常保护** — .catch() 防止 Frida 注入失败导致进程退出 |
| `src/index.ts` | **保底逻辑** — PPID 查找失败时用第一个 WeChatAppEx 进程 |
| `一键启动.bat` | [新增] 启动脚本，带 Node.js 版本检查 |

### e0e1-wx 修改内容

| 文件 | 修改 |
| --- | --- |
| `package/devtools/engine.py` | `start()` 跳过 Frida 注入，只启动 debug/proxy server |
| `package/devtools/engine.py` | `_start_frida_sync()` 返回 `(None, None)` |
| `start_engine.py` | [新增] 独立启动引擎脚本（不依赖 GUI） |

### 项目地址

https://github.com/hello-xiaoniao/WMP-pentest-automation

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GzdTGmQpRic1orFibqtmBJd06F33KoWTM6qEUAG7ZbwicA5MhTqx9stelHv8cMgibthiahUBTtgbPgn3ia2bYLpBElTQ/0?wx_fmt=png)

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