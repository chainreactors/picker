---
title: fagent：支持 AI 调用的 C2，让 AI 的手伸进内网
url: https://mp.weixin.qq.com/s/amorUkSXLTv_qxbPSMD30Q
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:32:28.953784
---

# fagent：支持 AI 调用的 C2，让 AI 的手伸进内网

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZesYkB2NEmiaVvtnLWSVgWLkO9AraZOl7zXFDbqYAGrHnqtGiaib3enN4c147s3DPSsjzzOHcCqYibIiblUOlzibgMMY7dtWJFAdXiacVicBOLWZkOc/0?wx_fmt=jpeg)

# fagent：支持 AI 调用的 C2，让 AI 的手伸进内网

emperor
emperor

代码审计Study

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前言

现有的 AI Agent 框架在调用外部工具时，能搜索网页、读写文件、跑代码——但一旦涉及内网渗透，AI
 就成了睁眼瞎：它看不见目标网络的拓扑，摸不到内网主机，更无法在受控主机上执行命令。

传统 C2 框架（Cobalt Strike、Havoc、vshell 等）都是为人设计的——图形界面、手动操作，AI 调不了。

fagent 要填的，就是这个空缺。

fagent 是一个 专为 AI 设计的 C2 框架，核心思路是：把 C2 能力封装成 REST API，让任何 AI Agent 直接通过 HTTP
 调用，从而把 AI 的"手"伸进内网。

---

架构

整体结构极简，三层：

[ AI Agent ]
 │
 │ REST API（X-API-Key 认证）
 ▼
 [ fagent Server（Go/Gin）]
 │
 │ AES-256-GCM 加密 Beacon
 │ 流量伪装：Content-Type: image/jpeg
 ▼
 [ Agent（Go，Win/Linux）]
 └── 运行在目标内网主机上

* Server：Go + Gin，同时提供 AI REST API 和 Web 管理界面
* Agent：纯 Go 编写，交叉编译，单文件投递，Windows/Linux 双平台
* 通信：AES-256-GCM 加密，per-session 密钥，Beacon 伪装成 CDN 图片请求

---

AI API 设计

fagent Server 暴露一组语义化 REST 接口，AI 无需理解 C2 内部细节，只需要发 HTTP 请求：

┌──────────────────────┬─────────────────────────────────────┐
 │ 接口 │ 说明 │
 ├──────────────────────┼─────────────────────────────────────┤
 │ GET /ai/sessions │ 列出所有在线 Agent │
 ├──────────────────────┼─────────────────────────────────────┤
 │ GET /ai/session/{id} │ 查看指定 Agent 信息（OS、IP、CWD…） │
 ├──────────────────────┼─────────────────────────────────────┤
 │ POST /ai/exec │ 在 Agent 上执行命令 │
 ├──────────────────────┼─────────────────────────────────────┤
 │ POST /ai/upload │ 向 Agent 上传文件 │
 ├──────────────────────┼─────────────────────────────────────┤
 │ POST /ai/download │ 从 Agent 下载文件 │
 ├──────────────────────┼─────────────────────────────────────┤
 │ POST /ai/scan │ 通过 Agent 扫描内网端口 │
 ├──────────────────────┼─────────────────────────────────────┤
 │ POST /ai/socks5 │ 启动 SOCKS5 代理，借 Agent 访问内网 │
 ├──────────────────────┼─────────────────────────────────────┤
 │ POST /ai/persist │ 持久化 Agent │
 ├──────────────────────┼─────────────────────────────────────┤
 │ POST /ai/pivot │ 端口转发 │
 ├──────────────────────┼─────────────────────────────────────┤
 │ POST /ai/sleep │ 修改 Beacon 间隔 │
 ├──────────────────────┼─────────────────────────────────────┤
 │ POST /ai/kill │ 终止 Agent │
 ├──────────────────────┼─────────────────────────────────────┤
 │ POST /ai/wait │ 同步等待任务结果（AI 最常用） │
 └──────────────────────┴─────────────────────────────────────┘

AI 调用 exec 后拿到一个 job\_id，再调用 wait 阻塞直到命令执行完毕，整个过程对 AI 来说和调用普通工具没有区别。

---

Agent 能力

Agent 支持 27 种任务类型，覆盖渗透的主要阶段：

执行控制

* exec：命令执行，实时流式回显，CWD 持久跟踪

文件操作

* upload / download：文件传输
* fs\_ls / fs\_read / fs\_write / fs\_mkdir / fs\_delete 等：完整文件系统操作
* fs\_wget：Agent 自行从指定 URL 拉取文件

网络能力

* scan：并发端口扫描，支持 CIDR 和范围格式
* socks5：完整 SOCKS5 代理，借 Agent 访问内网资源
* pivot：TCP 端口转发，内网横向移动
* probe：主机探测

信息收集

* netinfo：网卡、路由、ARP 表
* recon：综合侦察，一键收集主机全貌
* browser\_creds：提取浏览器保存的账号密码（Chrome、Edge 等）
* screenshot：截屏
* fs\_search：按名称/内容搜索文件

持久化

* Windows：注册表、计划任务、Windows 服务
* Linux：Crontab、Systemd、Bashrc

---

流量伪装

fagent 的流量设计从一开始就考虑了对抗检测：

* Beacon URL 伪装成 CDN 资源请求：POST /cdn/v2/assets/{session\_id}.jpg
* Content-Type: image/jpeg，看起来像图片上传
* 随机 User-Agent 轮换
* 通信内容全程 AES-256-GCM 加密，per-session 独立密钥
* Agent 启动时随机延迟，对抗沙箱

---

AI 怎么用它

有专门供ai查看怎么使用的文档

![](https://mmbiz.qpic.cn/mmbiz_png/ZesYkB2NEmgpLoN5OnsY8qsnB8OEtAWUGbG6eY1xmq8janUKibLhY146COLUxrF9yiaAruezpJVcsJCDVP2XHqicicHlZMCwNceFH0jzMT0ibwUA/640?wx_fmt=png&from=appmsg)

下载下来给ai让ai通过文档进行内网渗透

免杀试了一下主流杀软没能检测出来

![](https://mmbiz.qpic.cn/mmbiz_png/ZesYkB2NEmgCVUcfuJ7W0zLiaB3EMpIFF5cia55BymEyY14cfk1Im57iavfFsZ5kUwYtf4g4vjPb3kRicicOQyQiaseXBHp4XGRTFiaekqdIGELhLs/640?wx_fmt=png&from=appmsg)

监控屏幕

文件管理

浏览器保存密码导出等等

功能都可以使用并且ai可以调用这些功能一直横向再横向

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZesYkB2NEmianPyicJkibVZ0tAZ4zz0wnffb84zibW5tHuXW6UnxPk50NAMMjn39jZblD5f6gQPe3EDGHcZd6CNPIHOYPicG78a9c5qFjaH4oWPI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZesYkB2NEmhibymEeicUibWp1U4A8p8IgzjrK2gtFJpoVYuYkpWDb9VL04efw4iaPicSk7rCicrU8eXxdKUqOpCvU1qjrFHWQSOoOzMJJpECDcHc8/640?wx_fmt=png&from=appmsg)

。

怎么说呢新一代c2的时代已经到来支持ai内网渗透。让ai的手高效率伸进内网。

现在fagent目前只提供给学员内测。有内网靶场或攻击环境的也可以找我我刚好训练改进fagent能力。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xqh2MXgFFhcNJa3dwoAm0KMQR2gTeKeHlQHSib3OTNKwMqeQVSZBhgx7t92RQ05uIYNliaVick0zoHMnsCAeSMVEQ/0?wx_fmt=png)

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