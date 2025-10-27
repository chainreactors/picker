---
title: 两种方式获取安卓App的uid，供eBPF过滤使用
url: https://mp.weixin.qq.com/s?__biz=MzU3MTY5MzQxMA==&mid=2247484077&idx=1&sn=78f786ba0ee667913ceef7b1f22c1214&chksm=fcdd02a0cbaa8bb6e7ce5f6a8bfa5eed509f7e093290b9445e832e854274101e6021baec6fa6&scene=58&subscene=0#rd
source: 软件安全与逆向分析
date: 2023-03-17
fetch_date: 2025-10-04T09:53:11.772949
---

# 两种方式获取安卓App的uid，供eBPF过滤使用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/k9S5z61JPnZSgPaWpLV36aoyq0x7n0Fic4qMOXQIE8UlVxLPwI1S6B5N7gtzXjTjEfRquibgNm9y49DVNNNfHBeA/0?wx_fmt=jpeg)

# 两种方式获取安卓App的uid，供eBPF过滤使用

软件安全与逆向分析

非虫‍

读完需要

2

分钟

速读仅需 1 分钟

开发 eBPF 程序的时候，有时候需要按 uid 来过滤 App，这与 Linux 是一个不同的地方。

简单总结了两种方式获取 App 的 uid。以本人开发的名为 com.fc.ebpfapp 的 eBPFApp 为例。

***1***

##

**第一种方法**

使用 Frida 读取 uid 的值，方式是操纵 Java API 接口：

```
[Pixel6::PID::xx]-> Java.use('android.app.ActivityThread').currentApplication().getApplicationContext().getPackageManager().getApplicationInfo('com.zui.position.travel', 0).uid.value
10110
```

***2***

##

**第二种方法**

使用 adb shell 查看，传入 ls -n 的参数可以查看 uid：

```
% adb shell ls -n /data/data/com.fc.ebpfapp
total 24
drwxrws--x 2 10110 20110 4096 2023-03-15 11:47 cache
drwxrws--x 2 10110 20110 4096 2023-03-15 11:47 code_cache
drwxrwx--x 2 10110 10110 4096 2023-03-15 11:47 files
```

![](https://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnZSgPaWpLV36aoyq0x7n0FicFx45ricqchjbofecpRtPhicTEdt0SqRDcUFicibVDd2fq77rN3t1qic9icHA/640?wx_fmt=png)

输出的第 3 列就是了。

拿到 uid 后，做 eBPF hook 的时候，就可以使用这个值来过滤特定的 App 了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

软件安全与逆向分析

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

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