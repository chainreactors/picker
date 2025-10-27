---
title: 安卓权限/android应用和信息使用权限
url: https://blog.upx8.com/3668
source: 黑海洋 - WIKI
date: 2023-07-05
fetch_date: 2025-10-04T11:55:02.192757
---

# 安卓权限/android应用和信息使用权限

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 安卓权限/android应用和信息使用权限

发布时间:
2023-07-04

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
23963

我们可能会调用用户的一些应用和信息使用权限，以下是调用权限对应的业务功能以及我们调用权限的目的。请知悉，用户同意本隐私政策后，相应设备权限并不会默认开启，当涉及重要或敏感的设备权限时，我们会在您使用到相应业务功能时，另行弹窗再次征得您的同意后开启。权限开启后，您还可以随时通过设备设置关闭授权。您不同意开启权限，将不会影响其他非相关业务功能的正常使用。

**1、android 权限**

|  |  |  |
| --- | --- | --- |
| **安卓权限** | **说明** | **应用** |
| android.permission.INTERNET | 网络访问权限 | 允许应用联网 |
| android.permission.ACCESS\_NETWORK\_STATE | 获取网络状态权限 | 允许应用获取网络状态 |
| android.permission.ACCESS\_WIFI\_STATE | 获取 WiFi 状态权限 | 允许应用获取 WiFi 状态 |
| android.permission.FOREGROUND\_SERVICE | 允许启动前台服务权限 | 完成桌面小组件盯盘功能 |
| android.permission.USE\_FINGERPRINT | 指纹识别权限 | 允许指纹登录 |
| android.permission.VIBRATE | 振动权限 | 允许电话振动 |
| android.permission.WAKE\_LOCK | 唤醒锁权限 | 允许保持屏幕唤醒完成KYC功能 |
| android.permission.CAMERA | 摄像头访问权限 | 完成KYC认证、拍照、扫码功能 |
| android.permission.ACCESS\_COARSE\_LOCATION | 粗略位置信息访问权限 | 实现推荐新闻、活动功能 |
| android.permission.READ\_PHONE\_STATE | 允许读取本机识别码权限 | 允许设备指纹、统计信息和面部识别 |
| android.permission.READ\_EXTERNAL\_STORAGE  android.permission.WRITE\_EXTERNAL\_STORAGE | 外部存储读写权限 | 允许读取或写入图像、文件等以确保应用稳定运行 |
| android.permission.WRITE\_SETTINGS | 系统设置读写权限 | 允许设备指纹功能 |
| android.permission.SYSTEM\_ALERT\_WINDOW  android.permission.SYSTEM\_OVERLAY\_WINDOW | 悬停提示框权限 | 完成悬浮框盯盘功能 |
| ClipboardManager | 剪贴板访问权限 | 完成2FA登录、红包和充提功能 |
| android.permission.READ\_APP\_BADGE  com.sec.android.provider.badge.permission.READ  com.sec.android.provider.badge.permission.WRITE  com.htc.launcher.permission.READ\_SETTINGS  com.htc.launcher.permission.UPDATE\_SHORTCUT  com.sonyericsson.home.permission.BROADCAST\_BADGE  com.sonymobile.home.permission.PROVIDER\_INSERT\_BADGE  com.anddoes.launcher.permission.UPDATE\_COUNT  com.majeur.launcher.permission.UPDATE\_BADGE  com.huawei.android.launcher.permission.CHANGE\_BADGE  com.huawei.android.launcher.permission.READ\_SETTINGS  com.huawei.android.launcher.permission.WRITE\_SETTINGS  com.oppo.launcher.permission.READ\_SETTINGS  com.oppo.launcher.permission.WRITE\_SETTINGS  me.everything.badger.permission.BADGE\_COUNT\_READ  me.everything.badger.permission.BADGE\_COUNT\_WRITE | 允许读写系统设置和桌面角标 | 完成桌面角标功能 |
| com.asus.msa.SupplementaryDID.ACCESS freemme.permission.msa | 允许获取设备标识信息，如:oaid | 允许设备指纹功能 |
| com.google.android.c2dm.permission.RECEIVE | 允许创建GCM注册令牌 | 允许GCM推送功能 |
| com.google.android.finsky.permission.BIND\_GET\_INSTALL\_REFERRER\_SERVIC | 允许绑定安装归因服务 | 允许安装归因分析功能 |
| com.google.android.gms.permission.AD\_ID | 允许获取广告ID | 允许应用获取广告ID |
| com.kubi.kucoin.permission.JPUSH\_MESSAGE com.kubi.kucoin.permission.MIPUSH\_RECEIVE com.kubi.kucoin.permission.PROCESS\_PUSH\_MSG com.kubi.kucoin.permission.PUSH\_PROVIDER com.kubi.kucoin.permission.liantian.RECEIVE | 允许推送功能 | 允许推送功能 |
| RECEIVE\_BOOT\_COMPLETED | 开机广播 | Fiat Deposit |
| android.permission.POST\_NOTIFICATIONS | 允许应用程序发送通知 | 应用启动时触发，完成离线推送功能 |
| android.permission.READ\_MEDIA\_VIDEO | 允许应用程序从外部存储读取视频 | 支付P2P申述触发，完成申述视频上传功能 |
| android.permission.READ\_MEDIA\_IMAGES | 允许应用程序从外部存储读取照片 | 完成KYC、P2P申述、扫一扫、充币地址功能 |

**2、iOS 权限**

|  |  |  |
| --- | --- | --- |
| **iOS 权限** | **说明** | **应用** |
| NSFaceIDUsageDescription | 面部或指纹信息访问权限 | 用人脸识别登录 |
| 摄像头 | 摄像头访问权限 | 完成KYC认证、拍照、扫码功能 |
| LocationServices | 粗略位置信息访问权限 | 实现推荐新闻、活动功能 |
| 照片 | 外部存储读写权限 | 允许读/写图像 |
| 推送 | 推送权限 | 允许离线推送通知 |
| UIPasteboard | 剪贴板访问权限 | 完成2FA登录、红包和充提功能 |
| NSMicrophoneUsageDescription | 麦克风权限 | LegendTrading KYC、客服聊天功能 |

用户可以在设备的系统权限管理中选择关闭部分或全部权限，从而拒绝对我们的应用和信息使用授权。使用不同的系统或设备，权限显示方式及关闭方式可能有所不同，如无法找到相应功能，用户可询问设备及系统的提供方获得帮助。

[取消回复](https://blog.upx8.com/3668#respond-post-3668)

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