---
title: MQTT微信小程序5.2 支持电池接入 (完全开源)
url: https://mp.weixin.qq.com/s/c6Slb-9SRy-Je5KrqNeeOw
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T06:00:36.022851
---

# MQTT微信小程序5.2 支持电池接入 (完全开源)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OhGhqyNZyCzSlKV4c7Tb8zCVMy1icpmJmCiaLbHPIlseiasAtD1aO4PsI0OPeGDianjdaZ4bib6iaJLDuRoybGEHUZPVe2aLrBngIJU/0?wx_fmt=jpeg)

# MQTT微信小程序5.2 支持电池接入 (完全开源)

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于kali笔记
，作者大表哥吆

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6DBXaFMbqQ0IcXx6yjOS0WlJOZqJj2a6TyY8zId0YJ0g/0)

**kali笔记**
.

发布关于Kali Linux学习和相关安全领域的文章、致力于网络完全学习和研究。以及Debian Centos等操作系统的安全和运维，同时涉及到对树莓派 ESP8266 Arduino等物联网领域的开发和应用。

> 在上篇文章中，我们讲到了基于ESP8266检查锂电池的电压、容量、状态等信息。让我们对设备的状态能实时监测。

因为是基于MQTT协议，因此可以轻松地接入小程序和HomeAssistant中。便于我们对数据的统计和观察。

> 最新开源地址：https://github.com/Priess0503/WxMQTT

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBoreIicBxnXIDRLkcsJexia0icJ4LAicOEnm4oYoY4DRbBF1CmnaePcc3dPrG6lpozkGSjyntAoLbicKVdFgPlicubG6QiaZ4WbjZvS3IXs/640?wx_fmt=gif&from=appmsg)接入HA![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBorecmtRGwa1jkYfmUCpBQesPghPjoMavzPrRny142ExUrI0Ez7OI56ibeLpDPwCgEbygvZod0kdTwJNF7dicKsq6r538mcL0EKFWA/640?wx_fmt=gif&from=appmsg)

首先我们来看看加入Ha中的效果吧！以下是运行四天的数据效果。

![卡片效果](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorfmWksJhFFDNXN5O7B2pKiclflHPAvCFE6JCgXyZMJVGe58r6JDR7WRIAp1nRibsaLic8BKRK915rMPD5nISYghz2Wg3WCRZRndU8/640?wx_fmt=png&from=appmsg)

卡片效果

![一周内容量变化 中途充电一次](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorfk2RYKHhWVWVFeCDPGwCzeuV6TiaKQu90GwHP7O9VoftfYWItp157XJHURibt4VDTUjAx7FbFGgvsGowepdevCe9uHiaBJPFU6fU/640?wx_fmt=png&from=appmsg)

一周内容量变化 中途充电一次

![一周内电压变化趋势](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoreC8hXbic9ZRcmHZDd8SQo6DQVfYdCkJx0JM7OjRXvicnXwcEvz5AtibJPc68yPhPEIn4iaja851KM2amRibteC4deMguKcibNTlElNM/640?wx_fmt=png&from=appmsg)

一周内电压变化趋势

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBoreEhFtv7IRo9xK3qSWEB2tAgcUFyHv5KOcU8Q86wtRV03aQvibsY7iaj0ATG3CdEMZMkm3jWibT2aEDZHxfibOveQEue8M8Gz1x1Fk/640?wx_fmt=png&from=appmsg)
如何接入HA呢。我们以默认json数据格式为例：

```
{"voltage":4.089,"soc":87.6,"rate":0.00,"state":"Idle"}
```

在`configuration.yaml`配置文件中，添加mqtt参数：

```
# 18650 电池传感器（MAX17048）
   - unique_id: battery_18650_level
     name: "18650 Battery Level"
     state_topic: "18650"
     value_template: "{{ value_json.soc }}"
     unit_of_measurement: "%"
     device_class: battery
     icon: mdi:battery
   - unique_id: battery_18650_voltage
     name: "18650 Voltage"
     state_topic: "18650"
     value_template: "{{ value_json.voltage }}"
     unit_of_measurement: "V"
     device_class: voltage
     icon: mdi:flash
   - unique_id: battery_18650_state
     name: "18650 State"
     state_topic: "18650"
     value_template: "{{ value_json.state }}"
     icon: mdi:chip
   - unique_id: battery_18650_rate
     name: "18650 Rate"
     state_topic: "18650"
     value_template: "{{ value_json.rate }}"
     unit_of_measurement: "%/hr"
     icon: mdi:speedometer
```

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBordauImyRXUiaX4hXqkB6OlgIIpSRFxrnvA6GjKh2W5kXr3lOCUibYe9kraVV2ibf1IBvlxXrXLW5PfuJKX3W1PLKodMyVzTHMEx1g/640?wx_fmt=gif&from=appmsg)小程序![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBordLD7hE5m6xVJQNVt0RtcicsdWEZVflBrR7cAYCyR92D2etpef9oibKvWLlg87EwJPnHkh4X3BEick1kWiaibo5HvwP4tTn2ibUZpgUo/640?wx_fmt=gif&from=appmsg)

当然，作为配套，我在微信小程序中也加入了锂电池监测模块。首先来看看效果！

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfe9CzqID5ZvPfgMZJ7WsylZbLLcFApE1ibQbcMK6r3q4ZgRpthiaDd3b8MprekODXzPg27weRKgO1MwmFL2nvib4kicudm8671Yjo/640?wx_fmt=png&from=appmsg)
**使用：**
为了方便使用，接入也极其简单。点击`设备`-`添加设备`-`电池`输入订阅主题即可。
**版本说明：**
本次版本更新，默认为数据库版本。小程序后端项目及搭建地址：

> https://github.com/Priess0503/WxMQTT/tree/main-mysql

搭建完成后，编辑 `utils/api.js`文件。修改后端服务器地址。![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBordiao1Q9ngkgLcZukduMYN6Iyc89Z5V1FW5ISsfqCmlZTGORmeP5Gqt9J3sofVibL2F6ZZSxZSv2SugTibEoYIroVlFsQ3FnuWOaA/640?wx_fmt=png&from=appmsg)

更多精彩文章 欢迎关注我们

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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