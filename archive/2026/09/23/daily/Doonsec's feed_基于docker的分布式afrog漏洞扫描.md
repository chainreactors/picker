---
title: 基于docker的分布式afrog漏洞扫描
url: https://mp.weixin.qq.com/s/urTPXg_QLn7WRK3gLNlKcA
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:59:56.698350
---

# 基于docker的分布式afrog漏洞扫描

# 基于docker的分布式afrog漏洞扫描

原创

文峰SEC
文峰SEC

文峰SEC

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

为了提升渗透扫描的工作效率，受到AI应用启发，特开发基于docker的分布式afrog漏洞扫描，效果不错，记录下。

* 架构设计

主控平台 (master)：FastAPI 提供 Web UI 与 REST API，输入 URL、下发任务、呈现扫描结果。Web 界面一比一复刻 afrog-web 的展示效果（漏洞列表、Severity 配色、Request/Response 详情、分页等）。

工作节点 (worker)：轮询 MongoDB 抢占任务，调用本地 afrog 二进制扫描，将结果回传 MongoDB。

Redis：worker 心跳/在线状态监控（TTL 自动判定离线）。

MongoDB：任务下发、任务状态、漏洞结果持久化。

* 部署方式

系统默认复用你已运行的 beholder 的 redis / mongo，不另外启动中间件，具体看我合集里的另外一篇文章。

```
cp .env.example .envdocker compose up -d --builddocker compose exec worker download-afrog   # 可选，自动下载 afrog 到 afrog-bin/
```

* 使用效果

1. 浏览器打开 http://localhost:8080，登录。

2. New Scan：粘贴目标 URL（每行一个），可选 PoC 关键字(`-s`)、等级过滤(`-S`)与\*\*代理\*\*（HTTP/HTTPS/SOCKS5，支持多代理轮换，常用于经代理扫描内网目标），提交。

![](https://mmbiz.qpic.cn/mmbiz_png/LN0NvtXia47GgicOpeP88X9U25UlKs2jXtoQgLbJhk4zKQqH1Uoia2GlkL7WZuicDicIhV39IEkUm6Z4U4xE0CDKFX6drLHX0nic87MQKALzShKBI/640?wx_fmt=png&from=appmsg)

3. Tasks：查看各 Scan 进度（pending/running/done/failed、漏洞数）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LN0NvtXia47HfRysTdVGGR4yqticJW94AR8tY34o2jKC1cwfn8s1u43bNnV0g5q7akb55mwiaKcxj2zic8bYUc6UwLNvYbVkprNt872G0aJIKgI/640?wx_fmt=png&from=appmsg)

4. Reports：复刻 afrog-web 的漏洞列表 —— Severity 复选筛选、POC ID/名称搜索、点击表头展开漏洞详情与 Request/Response 对比、Copy 按钮、分页。

![](https://mmbiz.qpic.cn/mmbiz_png/LN0NvtXia47HoqL4fP5nJePaePywjQfiaMxqiaPE9hVh7ic8M8RaZG2mH4hjglkx3D6NnLNodLnrluEmrL95ovv8rLbbYsIV1VlbEKrNpiauATlg/640?wx_fmt=png&from=appmsg)

5. Workers：查看在线 worker、状态(idle/busy)、当前任务、心跳时间。

回复关键字【202609】获取下载链接

免责声明：本工具仅用于已获授权的安全测试，请勿对未授权目标发起扫描。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YhFqYGhfZqJylvnQ3BPoa403aeBoTOwTmC64iaDKicdxMh4BUQQH1zQ09NibvfGsk0G1hxEyD719qeiaeAMosnmBDA/0?wx_fmt=png)

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