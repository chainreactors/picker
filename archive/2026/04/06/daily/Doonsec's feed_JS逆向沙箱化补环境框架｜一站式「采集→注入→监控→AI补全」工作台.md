---
title: JS逆向沙箱化补环境框架｜一站式「采集→注入→监控→AI补全」工作台
url: https://mp.weixin.qq.com/s/IgyEA34YGqnoEAbW0w7wDA
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:29:08.513425
---

# JS逆向沙箱化补环境框架｜一站式「采集→注入→监控→AI补全」工作台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/veA9QmcJk5mQt8yRlRVHespIAQVTrmoFeWzKz6fmFVaR5sbIzIgJc4yurVOic3gEg6QicPS02r6fAltl1Y2sbVgQ/0?wx_fmt=jpeg)

# JS逆向沙箱化补环境框架｜一站式「采集→注入→监控→AI补全」工作台

原创

菜狗
菜狗

只会看监控的实习生

![]()

在小说阅读器中沉浸阅读

## 🎯 一句话卖点

“把目标页面拖进来，框架自动帮你补齐所有 undefined——20 秒生成可直接跑在沙箱里的『假浏览器』。”

## 🏗️ 工作流程（Mermaid 拖拽图）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5mQt8yRlRVHespIAQVTrmoFuDTnhrzzqwEGwWicDaUM6SbhE0xBvKlNTib0DUJl5rQzhoj40iaAJ9jyg/640?wx_fmt=png&from=appmsg)

## ⚡ 5 分钟上手（Docker 一行）

```
git clone https://github.com/lasawang/js-sandbox-env-framework.git
cd js-sandbox-env-framework
npm install && npm start
# 浏览器自动打开 http://localhost:3000
```

## 📦 已实现环境模块（25+ 一键加载）

| 模块族 | 清单（✅=已完成） |
| --- | --- |
| **Core** | ✅EnvMonitor（mock/调用链/日志导出） |
| **BOM** | ✅window、navigator、location、history、screen、localStorage、sessionStorage、crypto、performance、console、四大 Observer |
| **DOM** | ✅document、Element、Event、50+ HTML 元素（含 Canvas 2D/WebGL、Video/Audio、SVG...） |
| **WebAPI** | ✅fetch、XMLHttpRequest、URL/Blob/File/FormData、Headers/Request/Response、AbortController |
| **编码** | ✅atob/btoa、TextEncoder/TextDecoder |
| **定时器** | ✅setTimeout/setInterval |
| **AI 补充** | ✅自动生成并独立存放 `/env/ai-generated/` |

## 🧪 典型用法（WebUI 零代码）

1. 采集环境 「采集」页输入目标 URL → 一键导出 JSON → 自动注入沙箱
2. 执行脚本 「沙箱」页贴入 JS → 立即运行 → undefined 列表实时刷新
3. AI 补全 选中 undefined → 点击「AI 补环境」→ 预览 → 确认写入
4. 验证&快照 重新运行 → 0 undefined →「保存快照」→ 下次直接回档

## 📊 API 速查（前后端分离）

| 功能 | 方法 | 端点 |
| --- | --- | --- |
| 沙箱执行 | POST | `/api/sandbox/run` |
| 加载环境 | POST | `/api/sandbox/load-env` |
| AI 补环境 | POST | `/api/ai/complete` |
| Mock 规则 | GET | `/api/mock/rules` |
| 快照保存 | POST | `/api/snapshot/save` |

## 🔧 高级配置

* 支持 OpenAI / DeepSeek 双路 AI，可自定义 BaseURL & Key
* 环境变量即配即用： PORT=3000 OPENAI\_API\_KEY=sk-xx DEEPSEEK\_API\_KEY=sk-yy
* Mock 预设模板：反检测、Canvas 指纹、WebGL 指纹、Audio 指纹一键注入

## 🛡️ 安全 & 兼容

* 基于 isolated-vm 真沙箱，宿主 Node 进程完全隔离
* 仅 ai-generated 目录可动态删除，核心模块不可写
* API Key 仅服务端保存，前端无感；支持内网离线部署
* 兼容 Node ≥ 18，Windows / macOS / Linux 全平台通过测试

## 🏁 一句话总结

“JS 逆向补环境从未如此简单：拖页面→采环境→AI 补齐→沙箱验证→快照导出，一条命令全搞定！”

## 回复js逆向获取

## 低价出售安全证书不限于cisp、pte等请Vme～建了一个项目群，想进群的请回复进群即可

### HW投递二维码

![图片](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFl2LNtqTfL6w0xa6cyta6nLOCz4dQuGwviaUsRHMASbyQIxwXiafn7UhPTzkg8sicDYic5Djo3oEwfzcA76wpA0A203SpF12Uo8jU/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

只会看监控的实习生

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

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