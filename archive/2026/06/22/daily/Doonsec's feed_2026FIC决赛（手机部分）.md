---
title: 2026FIC决赛（手机部分）
url: https://mp.weixin.qq.com/s/5mKN2_HYHkDmC2x_BlqDSQ
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:03:40.578810
---

# 2026FIC决赛（手机部分）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T5C6icTcSx9MiaJFh6wZ4T86kXOqYUurQ4ho1Kc9xZQL020anTkaQicZ9FU6XGZia4cdcbicEMUtwApdHcxcEDrPYBeO6N5vlVs6egm6aKMFS6R4/0?wx_fmt=jpeg)

# 2026FIC决赛（手机部分）

原创

Serendipity
Serendipity

Serendipity的小屋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

容器密码：`\/a15f5b1d-a9fbdb79-de9ee6bf-28b9fce1\/`

## 手机部分

> 看见好多大佬都写了手机，那就照着大佬们的复现了😁

> 借鉴玫幽倩佬和mumuzi大佬的博客

> https://mumuzi.blog/docs/Forensic

### 1 分析手机检材，该手机设备名称为

### 【参考格式：小米 17 pro】

**REDMAGIC 9 Pro+**

火眼什么都没分析出来

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MicVhV6hpmlK2zHVmv5tELYmczEOmsNpwzn3wxy4Xu0jLLoNrsiaonwQsuuIC7bFEX15V3XJL98okrX1g5fDR1LPmbXFxNOXQeI/640?wx_fmt=png&from=appmsg "null")

那就只能翻文件了，跳转wifi源文件，查看到手机型号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9PXI5SoVvuGOqOjkibf9FvB0ryhAia8ArDqnjGdU3C9fx3icpLicia7C4QN796fgeRIaGUopS8h51WCicph9PoAL94kmTqv7PoD9BC2U/640?wx_fmt=png&from=appmsg "null")

在手机图片中也可以看到

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Nn9nVnemibNW5ueiafvETGjq0EKCTWMqqUahEJaEHXA5iaTTwVxj1riaicgUSsicHm52yGKb4Rk9r5oyvqm3W3pzK4HiaBqMliaWw0A0s/640?wx_fmt=png&from=appmsg "null")

### 2 分析手机检材，该手机系统magisk【环境版本】为

### 【参考格式：26000】

**30600**

全局搜索magisk

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MrDZicEhTqoh6TQS0VK7tV24micybbryh6FQ4DPtNku8v1dny4olEBuBqU1KusOWL0EEM17PeiapC4lsYIJ5J5NQdKAtYvEb735g/640?wx_fmt=png&from=appmsg "null")

在data/adb目录下看到了关于magisk的文件夹

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MQL8qZOPP9J17vLZNnRiaXrd3YKSq3nY08qqF6lsEnRJ8hYajhXEx8NulvrM7TdzsExyUxic3OODxp5JShb6d02F9bIs39JxYDI/640?wx_fmt=png&from=appmsg "null")

在util\_functions.sh文件中找到magisk版本

### 3 分析手机检材，嫌疑人通过盖世游戏app安装的《最终幻想》游戏版本是(罗马数字)

**XIII**

先看看盖世游戏的app报名是什么

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MH5icO5xIpicic4TKGKezR9icic7zX0sEH6WDFomNZuqzft3xEDEpzo2plK2IcTFUfBebqTV5BKMdCx4DVluWCkSuwM9OYJKawnQGs/640?wx_fmt=png&from=appmsg "null")

再去翻翻该应用的数据文件夹，有文件的文件夹不多

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9PhpXbicGSia1q4JiaUDdzR3Mz7LN1nbx2QCctbomtzzDLhbEdz9Wuia7revWmia5cTN4qesoBx1iblf2FGW0MpnuveI23WYmoAkLuxE/640?wx_fmt=png&from=appmsg "null")

一个个翻，最后定位到`/data/com.xiaoji.egggame/files/Documents/XiaoKunLogcat/XiaoKunLogInfo-5.txt`文件，搜索幻想的英语`fantasy`可以找到

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MXUZNYUl1lm0Y3LicKxWT9v4Dib54wagcjl2ZrQbo3v4Dsae9Ceq2ib6e10BJz7icmTsyZz3uNjCu4WkDT8NInMzK05stnOGbXMGQ/640?wx_fmt=png&from=appmsg "null")

### 4 分析手机检材，5月6日，嫌疑人最后一次使用谷歌套件中的某个app，其包名是

**com.google.android.googlequicksearchbox**

过滤一下使用时间与谷歌，就剩下两个软件了

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NK0ddSZtiatZPysWhSvnsibx9bvCfia2N5qd7QmTD2E3b6jjbnCDZnhM07pCbAvIgZY2jQYAtQOKX3EAByIDiasoWpnpRw1NiaGZLA/640?wx_fmt=png&from=appmsg "null")

> Google Play服务是安卓设备的核心后台服务，提供身份验证、定位、云存储、API支持和安全功能，确保应用和系统功能正常运行

由下题的推新闻可知，是第一个

### 5 分析上述app5月6日推送新闻的相关痕迹和缓存，新闻《男子拾获钱包以为天降横财》中事件发生的地点是

**柔佛麻坡**

追踪该应用的数据文件夹

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MX65nqVOF6jkoPunHibuB6Am710KaySLT7be7eJVtBL9ciaL5JJ5SmpkGvRXZxiaTvdt9E23Hx5A5NJ7xK4aR9gcKOwicnoWQdfFA/640?wx_fmt=png&from=appmsg "null")

题目上说了缓存，那就直接去cache目录下看，看到有image，看看有没有可用的信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9Ml1NK8qOy6ofVH45awrQYuT7XyibWo0Gk1ZUEPciavd0DkHiaXtxxy0o3Jcl2OrspUTmWhqXojMr8cq4EibOsDDsS0R3mhCuBKxWU/640?wx_fmt=png&from=appmsg "null")

筛选一下时间并排序一下图片大小可以看到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9PMBWYKTY9OyJJkl3iaRHUOHn5Mvicic8G4MebxQyJQGRbqmwlM8GEA2R520ZByha6FlUwtuibNAvHDwhrMnibqAH0GSmKAcQGfAAMk/640?wx_fmt=png&from=appmsg "null")

### 6 分析该手机关机信息情况，最近一次因电池电池异常过热导致关机的北京时间为 (格式:1970-01-01 00:11:22)

**2026-01-21 17:28:02**

搜索showdown，看到一个记录开关机的文件夹![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9POoiaFjAibsTI5ia6Fe3j4ib7zIIzjOBTzgaaQ34vdcnHYAt81Tu3PTkMXQdFVCfwMqdEYhicmWWteeqfibUj8ibTgr6U93KoibxaPDc0/640?wx_fmt=png&from=appmsg "null")打开文件夹看到每一次关机的时间与原因，那就直接看描述了

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OTRia3bPCKIHYpnibZvywcCU9qJDodxicKPuh6IWHIBjlau8u7nXoy3P6uYpYcqdyHibdp3jTR0GXtaAWebWOmv83heiaM30icIuYoE/640?wx_fmt=png&from=appmsg "null")

在checkpoints-1768987682434文件中看到

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OD6ia5HTbYvMsoT5wAyQwoeoibQeicmO8KPVichrgbiaiac8P4JCicS53bFbDLnZOXNgvdnFhVUzX2EymB47yD7yF7AgfeL6ugnO7lfE/640?wx_fmt=png&from=appmsg "null")

### 7 分析手机检材，北京时间2026-05-06 10:43:38左右那些应用的通知被查看了？

A. com.v2ray.ang

B. com.quark.browser

C. com.ai.assistance.operit

D. com.stevesoltys.seedvault

**AC**

> 这里借鉴mumuzi大佬和玫幽倩大佬的wp

这里我们需要查看使用统计数据库`/data/system_ce/0/usagestats/daily`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NNC2xzFDuZROBdCOp2Zo9ZoFj0HWcia0qj82kIdVia9eOsZ1jdfacJxLqX2ribeWyxEL7bo8e9TZ2k9Ugdn5FPYBKknTHadU5CMM/640?wx_fmt=png&from=appmsg "null")

这里的文件名的时间戳其实是统计区间的一个开始时间，转换一下题目所说的时间戳

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9N9OuDZhRuaFiajzlCoqiaNv4AicibCS0cXv7kynUjkgdguibfOztTUJDoqyyG5lqn1nBiaiaHEc5RdSoyR2MFF84ZrJTjXV7RxNT00kE/640?wx_fmt=png&from=appmsg "null")

按时间来看，大概率就是第一个文件，看文件明文是一对乱码，因为他们把很多内容都是保存成了数字token，而映射表是mappings文件

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NIXBngZOrCPAuI4esspwkSME6daAC0sK8GibjQJfYbXs7GeVeW5N2OdxTa1naetGUiauGzibMaguzgbwpTjiacAjv5tAqz2bjyj4c/640?wx_fmt=png&from=appmsg "null")

写个代码整合为csv文件

```
#!/usr/bin/env python3from pathlib import Pathfrom datetime import datetime, timezone, timedeltaimport csv
EVENT_TYPES = {    0: 'NONE', 1: 'ACTIVITY_RESUMED', 2: 'ACTIVITY_PAUSED', 3: 'END_OF_DAY', 4: 'CONTINUE_PREVIOUS_DAY',    5: 'CONFIGURATION_CHANGE', 6: 'SYSTEM_INTERACTION', 7: 'USER_INTERACTION', 8: 'SHORTCUT_INVOCATION',    9: 'CHOOSER_ACTION', 10: 'NOTIFICATION_SEEN', 11: 'STANDBY_BUCKET_CHANGED', 12: 'NOTIFICATION_INTERRUPTION',    13: 'SLICE_PINNED_PRIV', 14: 'SLICE_PINNED', 15: 'SCREEN_INTERACTIVE', 16: 'SCREEN_NON_INTERACTIVE',    17: 'KEYGUARD_SHOWN', 18: 'KEYGUARD_HIDDEN', 19: 'FOREGROUND_SERVICE_START', 20: 'FOREGROUND_SERVICE_STOP',    21: 'CONTINUING_FOREGROUND_SERVICE', 22: 'ROLLOVER_FOREGROUND_SERVICE', 23: 'ACTIVITY_STOPPED', 24: 'ACTIVITY_DESTROYED',    25: 'FLUSH_TO_DISK', 26: 'DEVICE_SHUTDOWN', 27: 'DEVICE_STARTUP', 28: 'USER_UNLOCKED', 29: 'USER_STOPPED',    30: 'LOCUS_ID_SET', 31: 'APP_COMPONENT_USED',}
def read_varint(data, i):    shift = 0    result = 0    while True:        if i >= len(data):            raise EOFError('truncated varint')        b = data[i]        i += 1        result |= (b & 0x7f) << shift        if not (b & 0x80):            return result, i        shift += 7        if shift > 70:            raise ValueError('varint too long')
def skip_value(data, i, wire):    if wire == 0:        _, i = read_varint(data, i)        return i    if wire == 1:        return i + 8    if wire == 2:        n, i = read_varint(data, i)        return i + n    if wire == 5:        return i + 4    raise ValueError(f'unsupported wire type {wire}')
def iter_fields(data):    i = 0    while i < len(data):        key, i = read_varint(data, i)        field = key >> 3        wire = key & 7        val_start = i        if wire == 0:            value, i = read_varint(data, i)            yield field, wire, value        elif wire == 1:            value = data[i:i+8]            i += 8            yield field, wire, value        elif wire == 2:            n, i = read_varint(data, i)            value = data[i:i+n]            i += n            yield field, wire, value        elif wire == 5:            value = data[i:i+4]            i += 4            yield field, wire, value        else:            raise ValueError(f'bad wire {wire} at {val_start}')
def parse_event(msg):    e = {}    for f, w, v in iter_fields(msg):        if w != 0:            continue        if f == 1: e['package_token'] = v        elif f == 2: e['class_token'] = v        elif f == 3: e['time_ms'] = v        elif f == 4: e['flags'] = v        elif f == 5: e['type'] = v        elif f == 7: e['shortcut_id_token'] = v        elif f == 8: e['standby_bucket'] = v        elif f == 9: e['notification_channel_id_token'] = v        elif f == 10: e['instance_id'] = v        elif f == 11: e['task_root_package_token'] = v        elif f == 12: e[...