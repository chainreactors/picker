---
title: Bark一个iOS通知应用程序，可自定义消息推送到iPhone（源码）
url: https://blog.upx8.com/3553
source: 黑海洋 - WIKI
date: 2023-05-14
fetch_date: 2025-10-04T11:39:03.238361
---

# Bark一个iOS通知应用程序，可自定义消息推送到iPhone（源码）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Bark一个iOS通知应用程序，可自定义消息推送到iPhone（源码）

发布时间:
2023-05-13

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
12064

![](https://pic5.58cdn.com.cn/nowater/webim/big/n_v233a3714ddafe409997184ccd5dcc5419.png)

今天发现一个可以向iOS推送消息的程序，Bark 提供一个 http 接口，简单调用即可给自己的 iPhone 发送推送。 APP 完全免费，完整开源 ，APP 与后端源码都可以随意使用，有需要的 V 友可以看看下面的链接。

#### Bark 的优点

1. 稳定 使用苹果 APNS，我自用以来基本没掉过通知（建议自建后端服务器）
2. 及时 一般 1 秒左右就能收到推送
3. 绝对的隐私安全
   * 服务端可以选择自行部署 /编译 /自行实现，数据将在 你的服务器-APNS-你的设备 之间传输， 确保任何推送信息都不会被泄漏。
   * APP 是通过 Github Action 编译上传，保证上传到 App Store 的版本是由开源代码编译，**未经任何人修改**（验证方法请在 APP 内查看)。
   * 历史消息记录是通过 NotificationServiceExtension 扩展，在收到推送时将推送信息保存在本地，再由个人 iCloud 同步，你的推送将只保留在你的设备与你的 iCloud 中。
   * 即将支持端对端加密，秘钥由你设置~

#### 链接

AppStore 链接 [https://itunes.apple.com/cn/app/bark-customed-notifications/id1403753865](https://blog.upx8.com/go/aHR0cHM6Ly9pdHVuZXMuYXBwbGUuY29tL2NuL2FwcC9iYXJrLWN1c3RvbWVkLW5vdGlmaWNhdGlvbnMvaWQxNDAzNzUzODY1)

源码 [https://github.com/Finb/Bark](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0ZpbmIvQmFyaw)

[https://github.com/Finb/bark-server](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0ZpbmIvYmFyay1zZXJ2ZXI)

使用教程 [https://github.com/Finb/Bark/blob/master/README.md](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0ZpbmIvQmFyay9ibG9iL21hc3Rlci9SRUFETUUubWQ)

[取消回复](https://blog.upx8.com/3553#respond-post-3553)

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