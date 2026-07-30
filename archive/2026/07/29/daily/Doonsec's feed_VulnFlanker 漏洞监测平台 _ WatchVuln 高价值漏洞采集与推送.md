---
title: VulnFlanker 漏洞监测平台 | WatchVuln 高价值漏洞采集与推送
url: https://mp.weixin.qq.com/s/s1vS1aW6lCzGn1Jd1rKXbw
source: Doonsec's feed
date: 2026-07-29
fetch_date: 2026-07-30T04:50:47.690738
---

# VulnFlanker 漏洞监测平台 | WatchVuln 高价值漏洞采集与推送

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMJYE1JDfo0J6tZFZKea5IwmUUSOsibJqaibR6XWhITtSWRNPQ78E1ZKosibSnPJhvuoFo2tT2KicJJEMQf3eiaGag8cEyILExpoofcY/0?wx_fmt=jpeg)

# VulnFlanker 漏洞监测平台 | WatchVuln 高价值漏洞采集与推送

ZonWin
ZonWin

夜组安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！**所有工具安全性自测！！！VX：****NightCTI**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把**夜组安全**“**设为星标**”，否则可能就看不到了啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg)

## 工具介绍

VulnFlanker 是一个面向内部安全运营的漏洞影响评估与受控验证平台。它将漏洞情报、主机资产快照、资产与漏洞匹配、风险优先级排序、只读验证任务和审计日志连接为一套完整工作流。

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMJXEcsaC8prpuXiaeicdpAjU0ib1ibjvNPicj9AhPxGQvPXstmuArYoDDFKibc8JudV6xzZAiasfR4BCFHjelM603XtTbgibYMCiczy2TE8/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLOO4SJts5C1nA5naNt2sdeAJpfB6B7606exdMy3X1BcjT3AqicSWHfIbObyN0dpWgVdDBEC0rmz0u3iaa7lRmoDnPeqhP43SgQE/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMIWGBbqRiaQ1U9DZ5U7K3XdL3RAR4bJibA9VaCXiblZZOX5omTP57f7wPIfD7cNXibNXxfV2VBEtWMosUnssfZaBruvs0Z0p57RDxc/640?wx_fmt=webp&from=appmsg)

## 功能

* 从 CISA KEV、阿里云 AVD 和内置 WatchVuln 采集器收集并标准化漏洞情报。

+ WatchVuln 高价值漏洞采集与推送 'https://github.com/zema1/watchvuln'
+ WatchVuln 项目功能非常好用，初期考虑以此作为采集器，不过效果不佳，但还是感谢原作者。

* 通过 Agent 接入 API 接收 Linux 主机快照。
* 跟踪资产、组件、网络暴露情况、Agent 状态和快照新鲜度。
* 依据产品、版本、操作系统、功能和暴露规则，评估漏洞是否影响资产。
* 生成包含优先级、风险因素、说明和稳定风险代码的风险队列条目。
* 创建只读验证任务，并记录 Agent 返回的证据。
* 提供 React 控制台，用于管理资产、漏洞、匹配结果、风险处置、验证任务、AI 设置、平台设置和审计日志。
* 支持通过可配置的服务提供商，使用 AI 辅助补充漏洞信息。

## 架构

```
漏洞情报源
    |
    v
情报采集 -> 标准化 -> 漏洞目录
    |                    |
    |                    v
Linux Agent -> Agent 接入 -> 资产 -> 匹配引擎 -> 风险队列
    ^                            |
    |                            v
    +----------- 验证任务 <- 匹配详情
```

主要运行时服务：

* 控制台 API：位于 `/api/v1` 下、需要身份认证的控制平面 API。
* Agent 接入服务：位于 `/agent/v1` 下、面向 Agent 的 API。
* Worker 和 Beat：负责情报采集、信息补充和监控的后台任务。
* PostgreSQL 和 Redis：提供持久化存储和任务队列基础设施。
* 前端：由 Vite 构建的 React 控制台，在演示用 Compose 技术栈中通过 Nginx 提供服务。

## 快速开始

环境要求：

* Docker 和 Docker Compose
* PowerShell、Bash，或其他能够复制 `.env.example` 的 Shell
* 如需采集实时漏洞情报，需要连接互联网

创建本地环境配置文件：

```
Copy-Item .env.example .env
```

启动前编辑 `.env`：

* 将 `VULNFLANKER_REDIS_PASSWORD` 设置为非默认值。
* 将 `VULNFLANKER_INTEL_WEBHOOK_TOKEN` 设置为非默认值。
* 在保存 AI 服务提供商 API 密钥前，设置 `VULNFLANKER_AI_KEY_ENCRYPTION_KEY`。
* 如果要使用首次运行设置页面，请将 `VULNFLANKER_BOOTSTRAP_ADMIN_PASSWORD` 留空。

启动演示环境：

```
docker compose --env-file .env -f .\deploy\docker-compose.yml up --build -d
```

打开控制台：

```
http://127.0.0.1:8100/
```

常用本地服务地址：

* 控制台 API 健康检查：`http://127.0.0.1:8000/api/v1/health/live`
* Agent 接入服务健康检查：`http://127.0.0.1:8001/agent/v1/health/live`

`deploy/docker-compose.yml` 中的 Compose 文件专门针对演示和开发用途进行了优化。它使用源代码绑定挂载，并为后端进程启用了重新加载。

## 工具获取

点击关注下方名片进入公众号

回复关键字【260729】获取下载链接

## 往期精彩

[穷尽一切手段，扒光 CDN 的底裤，找到真实 IP。

2026-07-28

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMI0BwMSbuqyibcNWictWHL1u7PnjTcUju6MvAr3Gt7uP7UKSgib77iccSnUuz59icnXxFt1sxh4BpwKQEcXMD3dow1thcrjBhhxMjXE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497289&idx=1&sn=d50f40bd94b4dbfd1bd56db63bde33f4&scene=21#wechat_redirect)[存储桶遍历漏洞利用工具V2.0  | 存储桶内容搜索、文件预览、文件下载和媒体解码

2026-07-27

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMKf7afhLARLXAic7vqKbEwPIlFn4TtfUQ5JOgeQGQYpiaPIgGsKMT83JyWGWhxxP5YEPDcJnKnRvLgUYp5MmyXh9Q76iaHq2DYaEE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497278&idx=1&sn=3e8169537e95d31ae22ecf0829c2e71c&scene=21#wechat_redirect)[红队多协议跳板代理管理平台 | 支持策略调度、规则分流、健康检查、REST API / WebSocket 自动化

2026-07-24

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLImBfgx6mAy5y7z8NiaKgVr5ibKYflwy2VCS5RFKrtr7mic1awbxDUajO9OmfQN9OFJMgGmQMzLOPwOln4GOSian6Rk3VfdbE05Is/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497272&idx=1&sn=9970aa4122cd9aaa21705b980d4b8581&scene=21#wechat_redirect)[面向 AI 代码审计的本地客观源码读取覆盖率工具，同时支持 Codex、Claude Code 和 OpenCode

2026-07-23

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMKZEdJU5LIrzkRrU2FqK9MagZ88tTGnfGfNZlCCicmuETYjcaffgFL0sUlIx5h6yLecwfibewdyxxk0Wc4wCn3oawekWj8QdOHoQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497262&idx=1&sn=b509f84b7d2dde31b866b390a88d2223&scene=21#wechat_redirect)[RavenEye · 威胁狩猎平台 | 一款面向蓝队与安全分析人员的轻量级桌面工具集

2026-07-22

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLjTRk0vvuLsC8ibr7qb0LjUIibUcKzPajoiaKDQA47K15w7LA7LAqMmSlpibSrARfWgVOhFp2nwRRUUHgxfH85E6yMYg2L0knSsicM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497261&idx=1&sn=28f382637e4ebc1222a1a26eccaebd3a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

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