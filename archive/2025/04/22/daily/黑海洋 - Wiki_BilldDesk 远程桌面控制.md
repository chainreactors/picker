---
title: BilldDesk 远程桌面控制
url: https://blog.upx8.com/4760
source: 黑海洋 - Wiki
date: 2025-04-22
fetch_date: 2025-10-06T22:06:57.267916
---

# BilldDesk 远程桌面控制

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# BilldDesk 远程桌面控制

发布时间:
2025-04-21

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
85751

## ![](https://cdn.skyimg.de/up/2025/4/21/4a5gla.webp)

## 简介

BilldDesk 远程桌面控制，目前实现了类似 ToDesk、向日葵等远程桌面的功能。

## 市场上的远控产品对比

> 作者使用过很多远程软件：TeamViewer、向日葵、ToTesk、AnyDesk、RustDesk、UU远程、连连控，还有qq自带的远程协助等等，但用ToDesk免费个人版比较多，因此用ToTesk和BilldDesk作对比~

| **工具名称** | **类型** | **国内稳定性** | **跨国延迟** | **免费政策** | **付费价格（年）** | **画质/流畅度** | **安全性** | **适用场景** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **BilldDesk** | 免费 | ★★★★★ | ★★★★★ | 免费 | 免费 | ★★★★★ | 开源可审计 | 技术用户/需求自定 |
| **TeamViewer** | 商业 | ★★★★☆ | ★★★★☆ | 限时免费 | $348起 | ★★★★☆ | AES-256加密，商用限制 | 跨国企业/高安全性需求 |
| **向日葵** | 商业 | ★★☆☆☆ | ★☆☆☆☆ | 严重限速+广告 | ￥298起 | ★★☆☆☆ | 基础加密，国内服务器 | 轻度国内办公 |
| **ToDesk** | 商业 | ★★★★☆ | ★★☆☆☆ | 单限1小时/天 | ￥118起 | ★★★☆☆ | 国内服务器，AES-256 | 国内短期远程 |
| **AnyDesk** | 商业 | ★★☆☆☆ | ★★★★☆ | 限速（商用需授权） | $179起 | ★★★★☆ | TLS 1.3，端到端加密 | 跨国团队/低延迟需求 |
| **RustDesk** | 开源 | ★★★★☆ | ★★★★☆ | 完全免费（需自建服务器） | - | ★★★☆☆ | 开源可审计，自建更安全 | 技术用户/长期隐私需求 |
| **UU远程** | 商业 | ★★★☆☆ | ★★★☆☆ | 免费（侧重游戏） | 免费 | ★★★★☆ | 游戏加速专用 | 游戏串流/低延迟需求 |
| **连连控** | 商业 | ★★☆☆☆ | ★★☆☆☆ | 免费版功能受限 | ￥199起 | ★★☆☆☆ | 国内小众工具，加密一般 | 临时应急使用 |
| **QQ远程协助** | 免费 | ★★☆☆☆ | ★☆☆☆☆ | 被时代淘汰 | 免费 | ★☆☆☆☆ | 腾讯服务器，基础加密 | 临时帮家人/朋友修电脑 |

以上的产品对比，显而易见，用过向日葵、todesk都很绝望了，特别是向日葵 已经没办法使用了，只能临时用下。

## 项目生态

| 项目名称 | 代码仓库 | star & fork | 线上地址/下载地址 |
| --- | --- | --- | --- |
| 远程桌面网页/客户端 | [billd-desk](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzaw) | [![github](https://camo.githubusercontent.com/e3ae842a1da31cd913afcac45b367591c2cadc6fc6621e478f4f500d70ce0cc0/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f67616c6178792d7331302f62696c6c642d6465736b3f6c6162656c3d73746172266c6f676f3d476974487562)](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzaw) [![github](https://camo.githubusercontent.com/da94e80f6121348a7f5302ac2b9eee44b651cae6313e4210dc134cf1c97c1230/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f67616c6178792d7331302f62696c6c642d6465736b3f6c6162656c3d666f726b266c6f676f3d476974487562)](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzaw) | [https://desk.hsslive.cn](https://blog.upx8.com/go/aHR0cHM6Ly9kZXNrLmhzc2xpdmUuY24v) |
| 远程桌面后台 | [billd-desk-admin](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzay1hZG1pbg) | [![github](https://camo.githubusercontent.com/59994647d3a47567e7f14600a5b3a69abed2b04bef45f1a51963c1c061621b5e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f67616c6178792d7331302f62696c6c642d6465736b2d61646d696e3f6c6162656c3d73746172266c6f676f3d476974487562)](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzaw) [![github](https://camo.githubusercontent.com/08cd4e4c532cbc85cc96cb7d7b3d672da7528545df522bc92560bcc451f23b33/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f67616c6178792d7331302f62696c6c642d6465736b2d61646d696e3f6c6162656c3d666f726b266c6f676f3d476974487562)](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzay1hZG1pbg) | [https://desk-admin.hsslive.cn](https://blog.upx8.com/go/aHR0cHM6Ly9kZXNrLWFkbWluLmhzc2xpdmUuY24v) |
| 远程桌面移动端 | [billd-desk-flutter](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzay1mbHV0dGVy) | [![github](https://camo.githubusercontent.com/b508c35c5393ab49aa3c52f783b8dabbc7dbbb54ec7cf3b1d7adf877f19dba24/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f67616c6178792d7331302f62696c6c642d6465736b2d666c75747465723f6c6162656c3d73746172266c6f676f3d476974487562)](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzay1mbHV0dGVy) [![github](https://camo.githubusercontent.com/132208ecc659a1ad7d51e5173d22f6fb8837c2d4ce0efc907f0c7ee7e763a6cf/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f67616c6178792d7331302f62696c6c642d6465736b2d666c75747465723f6c6162656c3d666f726b266c6f676f3d476974487562)](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzay1mbHV0dGVy) | [https://desk.hsslive.cn/#/download](https://blog.upx8.com/go/aHR0cHM6Ly9kZXNrLmhzc2xpdmUuY24vIy9kb3dubG9hZA) |
| 远程桌面服务端 | [billd-desk-server](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzay1zZXJ2ZXI) | [![github](https://camo.githubusercontent.com/2f3e091d344e94dd8d6cb366358554f027311411b96e8536c5302bdcbc44c8f2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f67616c6178792d7331302f62696c6c642d6465736b2d7365727665723f6c6162656c3d73746172266c6f676f3d476974487562)](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzay1zZXJ2ZXI) [![github](https://camo.githubusercontent.com/81ff0df36a85179ffa8c3602c2d7c1a5ddc5897dcd2f77ccbf45170137eb33c2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f67616c6178792d7331302f62696c6c642d6465736b2d7365727665723f6c6162656c3d666f726b266c6f676f3d476974487562)](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVzay1zZXJ2ZXI) | [https://desk-api.hsslive.cn](https://blog.upx8.com/go/aHR0cHM6Ly9kZXNrLWFwaS5oc3NsaXZlLmNuLw) |

## 技术栈

* 前端相关：[Vue3](https://blog.upx8.com/go/aHR0cHM6Ly92dWVqcy5vcmcv) 以及相关技术栈、`Typescript`、`WebRTC`、`WebCodecs`、`Web Workder`、`Web Audio`、`Canvas`
* 后端相关：[Nodejs](https://blog.upx8.com/go/aHR0cHM6Ly9ub2RlanMub3JnLw) 以及相关技术栈、`Koa2`、`Typescript`、`Sequelize`、`Mysql`、`Redis`、`Socket.io`
* 桌面客户端相关：[Electron](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZWxlY3Ryb25qcy5vcmcv)以及相关技术栈、`WebRTC`
* 移动客户端相关：[Flutter3](https://blog.upx8.com/go/aHR0cHM6Ly9mbHV0dGVyLmRldi8)以及相关技术栈、`WebRTC`
* 流媒体服务器相关：[SRS](https://blog.upx8.com/go/aHR0cHM6Ly9vc3Nycy5uZXQv)、 [FFmpeg](https://blog.upx8.com/go/aHR0cHM6Ly9mZm1wZWcub3JnLw)、[Coturn](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2NvdHVybi9jb3R1cm4)
* Docker 相关：[Docker](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZG9ja2VyLmNvbS8)
* 部署相关：[阿里云云效](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZvcHMuYWxpeXVuLmNvbS8)、[billd-deploy](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dhbGF4eS1zMTAvYmlsbGQtZGVwbG95)

## 兼容性

* [x]
* [x]  macOS
* [x]  Linux
* [x]  Android 12

## 下载

在线web端体验：[https://desk.hsslive.cn](https://blog.upx8.com/go/aHR0cHM6Ly9kZXNrLmhzc2xpdmUuY24v)

客户端下载：[https://desk.hsslive.cn/#/download](https://blog.upx8.com/go/aHR0cHM6Ly9kZXNrLmhzc2xpdmUuY24vIy9kb3dubG9hZA)

1. ![我很温柔](//q2.qlogo.cn/headimg_dl?dst_uin=526527509&spec=100)

   **我很温柔**

   2025-05-30 09:22:06

   [回复](https://blog.upx8.com/4760/comment-page-1?replyTo=30610#respond-post-4760)

   win10，安装了客户端，打不开
2. ![不知不觉](//q2.qlogo.cn/headimg_dl?dst_uin=107670707&spec=100)

   **不知不觉**

   2025-04-27 11:07:34

   [回复](https://blog.upx8.com/4760/comment-page-1?replyTo=30573#respond-post-4760)

   WIN11环境下，无法正常远程，提示连接中后显示连接超时
3. ![不含糖的小姐姐](//q2.qlogo.cn/headimg_dl?dst_uin=852146770&spec=100)

   **不含糖的小姐姐**

   2025-04-22 21:10:17

   [回复](https://blog.upx8.com/4760/comment-page-1?replyTo=30570#respond-post-4760)

   win11 还需要优化
4. ![魏无羡](//q2.qlogo.cn/headimg_dl?dst_uin=123456&spec=100)

   **魏无羡**

   2025-04-22 09:51:06

   [回复](https://blog.upx8.com/4760/comment-page-1?replyTo=30569#respond-post-4760)

   拉了，win7装不了，老实用向日葵吧

[取消回复](https://blog.upx8.com/4760#respond-post-4760)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")