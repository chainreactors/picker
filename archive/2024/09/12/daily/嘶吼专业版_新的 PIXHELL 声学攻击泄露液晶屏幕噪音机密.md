---
title: 新的 PIXHELL 声学攻击泄露液晶屏幕噪音机密
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247577928&idx=2&sn=14bd88e98bafaa91803607b4829c46e2&chksm=e9146172de63e864450462ce78ed6530d45164f6eece88dcb2ff7906b73f11c175be4b0ff239&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-09-12
fetch_date: 2025-10-06T18:29:09.877032
---

# 新的 PIXHELL 声学攻击泄露液晶屏幕噪音机密

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28Ibhic6uiccSsiblALaF6VJU7D7mD8oNhqFP1oPQA0t79B1Q8oAWPd4uDibq3sRmHkIouZQPDzbwEX9A/0?wx_fmt=jpeg)

# 新的 PIXHELL 声学攻击泄露液晶屏幕噪音机密

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

一种名为“PIXHELL”的新型声学攻击可以通过连接到的 LCD 显示器，无需扬声器而泄露物理隔离和音频隔离系统中的机密。

在 PIXHELL 攻击中，恶意软件会调制 LCD 屏幕上的像素模式，以在 0-22 kHz 的频率范围内产生噪声，并在这些声波中携带编码信号，这些信号可以被附近的设备（例如智能手机）捕获。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28Ibhic6uiccSsiblALaF6VJU72e8EThxk0vAZSog3QYREOXZoKJ1QoHvGYwKeHlC9SQUicwWCSSXds0Q/640?wx_fmt=jpeg&from=appmsg)

PIXHELL 攻击设置

研究人员的测试表明，数据泄露的最大距离为 2 米，数据速率达到 20 比特每秒。

虽然这对于实现大文件传输来说太慢，但实时键盘记录和窃取可能包含密码或其他信息的小文本文件仍然是可能的。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28Ibhic6uiccSsiblALaF6VJU7qYXxWmNoH1SVovEE53h1J27mks7YEpNDFMh8shIa51tAvSCXoTTStg/640?wx_fmt=png&from=appmsg)隐蔽音频通道

PIXHELL 由 Mordechai Guri 博士开发，他因对从隔离环境中泄露数据的方法进行广泛研究而闻名。就在上周，这位研究人员发表了另一篇关于一种新型侧信道攻击的论文，这种攻击被称为“RAMBO”，用于攻击的隔离内存总线辐射，它可以通过从设备的 RAM 组件产生电子辐射来窃取隔离环境中的数据。

PIXHELL 攻击方法利用了 LCD 屏幕因线圈噪音、电容器噪声或设备无法物理消除的固有振动而产生的意外声发射。

使用特制的恶意软件，攻击者可以使用以下调制方案将加密密钥或击键等敏感数据编码为声音信号：

**·**开关键控 (OOK)：通过打开和关闭声音对数据进行编码。

**·**频移键控 (FSK)：通过在不同频率之间切换对数据进行编码。

**·**幅移键控 (ASK)：通过改变声音的幅度（音量）对数据进行编码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28Ibhic6uiccSsiblALaF6VJU7IcpTYc1YafAlmUx41nibLzqHpn2J7rZpL5hbhL6RicUXIo2XRZNNvzTA/640?wx_fmt=png&from=appmsg)

调制不同频率的声音信号

接下来，通过改变液晶屏上的像素图案，调制后的数据会通过液晶屏传输，从而改变设备组件发出的声音。

笔记本电脑或智能手机等恶意或受感染设备附近的麦克风可以拾取声音信号，随后可能将其传输给攻击者进行解调。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28Ibhic6uiccSsiblALaF6VJU7CK842ybM9rIylhyicecV7FNu5H1EcUD1xNeZEC4QWUqmBnx4uUGWuKA/640?wx_fmt=png&from=appmsg)

附近麦克风接收到的声学信号的频谱图

值得注意的是，PIXHELL 可以在涉及多个信号源和单个接收者的环境中执行，因此如果这些系统被恶意软件感染，则可以同时从多个隔离系统中捕获秘密。

PIXHELL 恶意软件发出的声音频率通常在 0 - 22 kHz 频率范围内，人类几乎听不到。相比之下，人类通常能听到 20Hz 至 20kHz 频率范围内的声音，而普通成年人的上限通常在 15-17kHz 左右。

同时，攻击中使用的像素图案对用户来说是低亮度的或不可见的，这使得攻击特别隐蔽。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28Ibhic6uiccSsiblALaF6VJU7qYXxWmNoH1SVovEE53h1J27mks7YEpNDFMh8shIa51tAvSCXoTTStg/640?wx_fmt=png&from=appmsg)应对策略

可以实施多种防御措施来抵御 PIXHELL 和其他类型的声学侧信道攻击。在高度关键的环境中，出于谨慎考虑，应完全禁止在某些区域使用携带麦克风的设备。干扰或噪声生成也是一种解决方案，即引入背景噪声来干扰声学信号并增加信噪比 (SNR)，使攻击变得不可行。

安全研究人员还建议使用摄像头监控屏幕缓冲区，以检测与系统正常运行不匹配的异常像素模式。

参考及来源：https://www.bleepingcomputer.com/news/security/new-pixhell-acoustic-attack-leaks-secrets-from-lcd-screen-noise/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28Ibhic6uiccSsiblALaF6VJU78L0HMYicicAzZKvd59bsChUwn1QDEAAia9QkVuOicBJvOpOqkGGX7iae57w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28Ibhic6uiccSsiblALaF6VJU72uteAlaLmbd3l1icEoDpBGU7UuNedFaPsIC4HcXW7IRxcrlLnyz7MUQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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