---
title: PivotHub · 链透中枢 — 多层内网渗透辅助工具
url: https://mp.weixin.qq.com/s/2S7-SibBzT-6ZJnpNGJvPg
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:54:30.449385
---

# PivotHub · 链透中枢 — 多层内网渗透辅助工具

# PivotHub · 链透中枢 — 多层内网渗透辅助工具

ProbiusOfficial
ProbiusOfficial

菜鸟学信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

项目介绍页：https://probiusofficial.github.io/pivothub/（能力总览 · 界面预览 · 真机评测速览）

依据《多层内网渗透辅助工具 · 产品设计文档（PRD）v1.0》实现。 技术栈：**Vue 3（本地化全局构建）+ ECharts 5（Graph 拓扑）+ 原生 CSS**，后端 **FastAPI + SQLite + WebSocket**。 数据全部来自本地后端：`python -m pivothub` 启动后，前端经 REST + WebSocket 读写 SQLite； 后端不可用时界面显式报错，**不用假数据兜底**。

## 快速开始

### 环境要求

| 项 | 要求 |
| --- | --- |
| Python | 3.10+（本机实测 3.13） |
| 依赖 | `pip install -r requirements.txt` （FastAPI / Uvicorn / SQLAlchemy / Pydantic…） |
| 可选 | Docker（跑 `scripts/lab/` 靶场做全流程真机验证） |
| 浏览器 | 任意现代浏览器（前端零构建，Vue / ECharts 已本地化于 `assets/vendor/`） |

### 三步启动（后端一体化托管前端）

```
pip install -r requirements.txtpython run.py            # 等价 python -m pivothub，监听 127.0.0.1:8000# 浏览器打开 http://127.0.0.1:8000/
```

后端以 StaticFiles 原样托管前端，`/api/*` 与 `/ws` 同源，**无需另起静态服务器**。 数据全部来自本地 SQLite；后端不可用时界面显式报错。

> 首次打开会弹出**合规声明**（PRD §5 合规要求），顶栏另有常驻入口。 空库首次启动会按 `data/seed_project.json` 播种一场三层内网演示项目（见 §4），库非空则不动。

常用环境变量（均定义在 `pivothub/config.py`）：

| 变量 | 默认 | 说明 |
| --- | --- | --- |
| `PIVOTHUB_PORT` / `PIVOTHUB_HOST` | `8000` / `127.0.0.1` | 监听端口 / 地址（**仅允许回环**，有断言硬约束） |
| `PIVOTHUB_DB_PATH` | `<根>/pivothub.db` | SQLite 路径（WAL） |
| `PIVOTHUB_DATA_DIR` | `<根>/data` | 数据目录（命令库 / 技法库 / 种子项目 / 插件） |
| `PIVOTHUB_STAGE_BIND` / `_PORT` / `_TTL` | `0.0.0.0` / 随机 / 15 分钟 | 文件暂存 HTTP 服务（上传「HTTP 拉取」通道） |
| `PIVOTHUB_PLUGIN_REGISTRY` | `data/plugins/registry.json` | 插件清单来源（可指向远程清单） |

### 前端资源已本地化（离线可用）

`index.html` 引用的是 `assets/vendor/` 下的 Vue 3 与 ECharts，**不依赖 CDN**，断网环境可直接使用； ECharts 缺失时仅拓扑图降级，其余界面不受影响（`app.js` 另有 Vue 加载失败提示）。

### 只想调界面？

用任意静态服务器打开本目录（如 `python -m http.server 8777`）即可看 UI， 但没有 `/api` 与 `/ws` 时面板会**显式提示后端不可用**（不会退化成假数据）。

## 界面预览

> 以下截图取自空库首次启动播种的演示项目（§4），运行于`python run.py`+ 浏览器。

**阶段看板 · 进度总览与链路健康**

![阶段看板](https://mmbiz.qpic.cn/mmbiz_jpg/AFjuWEpVxUIJlPrichQibGibOcWsrffyAJ9guoqpfM0V2DgmV0otY7zmbz5RuOJbFLoHyuun3dBuBoFecWt4jf5smhANtC5iaK4ibOYiaiaZNwQy9c/640?wx_fmt=jpeg&from=appmsg)

**网络拓扑 · 跳板链**

![网络拓扑](https://mmbiz.qpic.cn/mmbiz_jpg/AFjuWEpVxUIvzlEPeC5gUniaibUgCU0mk2S2zgWwKic5VLQctuQyjPhVxbIZmYQ6gOZsYmClcU2NFYKmYh4o6XorgTgml2IHBWP9EXo4O1HcFg/640?wx_fmt=jpeg&from=appmsg)

|  |  |
| --- | --- |
| **资产列表** · IP / OS / 层级 / 权限 / 服务，支持扫描导入与移除 ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFjuWEpVxUJOdYiaJ0qU6KaicC28zFQnpKTClUotMaLSOzJaF8TWiaaXN2bsQ7wia5nkzUkzaAuAfdT0fJHiaNoiba7X3ialKuvJibOPz7X2ibcAkic6I/640?wx_fmt=jpeg&from=appmsg)![]() | **Shell 管理** · 会话登记 / 心跳 / 虚拟终端 / 一键提权 ![](https://mmbiz.qpic.cn/mmbiz_jpg/AFjuWEpVxUL13uGozxPdBCHxuVXKXcXGzDBdE7zT8RQn5zTAS42FcUwBZWD5Y58J5M22JKRFectwOB7ESQyUVIXRRJyziaRIZ7dneQAPRgYM/640?wx_fmt=jpeg&from=appmsg)![]() |
| **SSH 会话** · 独立纳管 SSH 主机，与 Shell 管理并存 ![](https://mmbiz.qpic.cn/mmbiz_jpg/AFjuWEpVxUJ6G9Pqp3PlzGz3NXfE2XKU7mUa7PehtuAAMbo3E23WPDBh5bQHbvpYpIZTJawkFCpzoZwQAbEqq9EZ69JaNDnv5X1qIuMiav1Y/640?wx_fmt=jpeg&from=appmsg)![]() | **资产探测** · 内网信息收集 + 内置 fscan 扫描 + 结果导入 ![](https://mmbiz.qpic.cn/mmbiz_jpg/AFjuWEpVxUKd6TDSM5WXfHmBVQLIkcL7tCss2RrKrHRargkMY1o1iauGUlLeens5yl0GmydKjAKiachqlg5SaHB2d15Gy7p3Z3YKsnRqYklzs/640?wx_fmt=jpeg&from=appmsg)![]() |
| **反弹 Shell** · 攻击机监听 → 靶机回连 → 自动登记会话 ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFjuWEpVxUJVOGkpwe9Jt7TP9YcgIEPO79ibS9snyxpzocticKERWxrDyicC619rDIIFU9UUrw1XBrSBCxtaKMeN6NgPIg2icJ3WqVdDtZQ4bGQ/640?wx_fmt=jpeg&from=appmsg)![]() | **马生成器** · PHP/JSP/ASP/ASPX 一句话马与自定义加密马 + 写马姿势速查 ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFjuWEpVxUJCLvo1YBy2JaKOhu0EMIq6qOL5w5mGou2ovglk0qRM4qack729N1GJQq8f62JPeZibt2fkdDTLia8SwQk6sxmv7EmnSk0Bvc7t4/640?wx_fmt=jpeg&from=appmsg)![]() |
| **编排台** · 出网探测 → 隧道选型 → 部署命令 → 健康看板 ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFjuWEpVxUIwFqukMoFh0YSCyib8nKnDjUREicl8ER6Nzz4TibiacMgIg7zcpz4hJPqI8ZCESHyYxsjulOiaz3VHuZ0WxhHOxUC4gWxQlvr6zhzM/640?wx_fmt=jpeg&from=appmsg)![]() | **数据库面板** · 选中连接自动探测结构，点表预览数据（命令经会话执行） ![](https://mmbiz.qpic.cn/mmbiz_jpg/AFjuWEpVxUK30JN9v7KEibfxuayriaiaDuL5RNNRaRIGDHib12dxYH9FpcmIuGmnnKR8nQZ5fUKro2KAB7F1rEUj909P1RrBwT0ibJyH4z44yvgE/640?wx_fmt=jpeg&from=appmsg)![]() |
| **凭据库** · 账号 / 哈希 / 密钥登记 + 跨层复用推荐打分 ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFjuWEpVxULZKCibKzPtaJhB1zj78lLTTE9Us5TznDybRkgFkMILyia6BT6zl9PPTJbO1Rf2FsLswbo2icvyEOmIic5tOHLJcb1e0unjXibuj574/640?wx_fmt=jpeg&from=appmsg)![]() | **Flag 收集墙** · 卡片墙 + 进度环 + 阶段进度 + 一键复制提交 ![](https://mmbiz.qpic.cn/mmbiz_jpg/AFjuWEpVxUILq7ZEyQGib0SZUSY7VQc3ZsWIMfnypJ9ibkmntc0OcG1RmzGT5XTRibJWl2oibRTUfCib2X2IX3XxQRDDa3taaOCBsfJI75Ieox5I/640?wx_fmt=jpeg&from=appmsg)![]() |
| **操作时间线** · 自动事件 + Markdown 笔记，可回溯每步命令 ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFjuWEpVxUIzOxPPr6ibb4jCTSIpcwCX2j6qdLBMkoKaiaPIWbxichIgyopE5zib1Z2NY6MwPiaHibMVHZ8ZlcwZibibBfLIsUQusvdwEiaQGTy3gWrg/640?wx_fmt=jpeg&from=appmsg)![]() | **命令速查** · 场景化命令模板 + 变量替换 + 提权智能匹配 ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFjuWEpVxUJFuYVscm2LEDO6icVI4uDCrKZE6xJ1eib1272cCianke7CY369QU4QibJ6b9seqfZUCDmk1tlN2ibzw8oaJGEwgQBFurZvkrVzqdEY/640?wx_fmt=jpeg&from=appmsg)![]() |
| **插件市场** · 数据插件（命令库 / 技法 / 提权规则），安装即并入视图 ![](https://mmbiz.qpic.cn/mmbiz_jpg/AFjuWEpVxULic44DYIaKYBpC0nK7yrYo0Lh1xQDvibk2f8kK8QL9bIquRqr9dcUp7xa8AN1Qaoj3BulJKP5KP1mmpEHb6Cn5yJV1bc5R9oy7s/640?wx_fmt=jpeg&from=appmsg)![]() | **复盘导出** · Markdown / HTML / JSON 三格式 + 实时预览 ![](https://mmbiz.qpic.cn/mmbiz_jpg/AFjuWEpVxUKJ6XHAL9UhGTuh0RmJSx3jnibmSxF6yu0ADdqAx9uRApoiaSgK67dya5ZZ9SsyCjDxce7vHTfaGw3bFslXKib7TrtOSicnjrDR0qU/640?wx_fmt=jpeg&from=appmsg)![]() |
| **合规声明** · 启动提醒 + 顶栏常驻入口 ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFjuWEpVxULxlZWHBncn7kZKTsedrz6B7nGOK6PWAiaPcwv6SxYfzuy5MtSKsnD7jpAp7ibiceGNnibVSicOqlntSClTOWENoicVmGmI4SzIt0ibK0/640?wx_fmt=jpeg&from=appmsg)![]() |  |

目录结构

```
supershell/├─ index.html                     # 前端骨架 + 全部 Vue 模板（<script type="text/x-template">）├─ run.py  requirements.txt       # 一键启动 / 后端依赖├─ pivothub/                      # 后端包（FastAPI + SQLite + WebSocket）│  ├─ app.py  config.py  db.py  util.py  localinfo.py│  ├─ api/                        # 路由层：projects hosts shells links creds flags timeline│  │                              #   export recon stage tools attack db plugins privesc …│  ├─ service/                    # 服务层：probe tty relay filestage recon dbclient│  │                              #   privesc fingerprint clues plugins export timeline│  ├─ session/                    # 会话层：命令执行 / 文件读写的唯一出口│  │                              #   base http_shell local reverse ssh registry│  ├─ adapters/                   # 代理适配器：chisel / frp / Neo-reGeorg（已接入）│  │                              #   + base / registry（其余工具占位）│  ├─ models/  schemas/           # SQLAlchemy 模型 / Pydantic 接口契约（唯一权威契约）│  └─ ws/                         # WebSocket 连接管理├─ assets/│  ├─ css/                        # theme.css 设计令牌 · layout.css · components.css│  ├─ vendor/                     # Vue 3 + ECharts 本地化（离线可用）│  └─ js/│     ├─ api.js                   # 后端 REST + WebSocket 客户端│     ├─ store.js                 # 全局 store：状态 + 派生数据 + 全部业务动作│     ├─ icons.js  topology.js  app.js  components/common.js│     └─ views/                   # 各视图（dashboard / topology / shell / proxy / …）├─ data/                          # 插件化数据：commands payloads tty_fixes privesc│  │                              #   seed_project.json（演示项目种子） plugins/（市场清单）├─ tests/                         # 后端 pytest 用例（223 passed，见 §8）├─ scripts/                       # 靶场 Compose（lab/）· Windows 防火墙放行脚本├─ tools/                         # chisel / frpc / frps / fscan 等二进制（适配器部署与扫描用）├─ docs/                          # 架构 / 计划 / 进展 / 验证文档 + screenshots/（界面截图）├─ 多层内网渗透辅助工具-产品设计文档.md   # PRD v1.0├─ README.md  LICENSE  HANDOFF.md  PROJECT-STATUS.md  PACKAGE-MANIFEST.md└─ .gitignore
```

**约定**：模板集中在 `index.html`（便于阅读与 IDE 高亮），逻辑按视图拆分在 `assets/js/views/`， 每个文件通过 `global.Components['xxx-view'] = {...}` 注册，`app.js` 统一挂载。

## 项目地址

https://github.com/ProbiusOfficial/pivothub

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9JPpNb7icHg...