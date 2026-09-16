---
title: 45 美元把 ESP32-P4 变成开源 IP-KVM 远程控制卡
url: https://mp.weixin.qq.com/s/wMXWhYqmW1MOsNqLkfm8xQ
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:02:49.090905
---

# 45 美元把 ESP32-P4 变成开源 IP-KVM 远程控制卡

# 45 美元把 ESP32-P4 变成开源 IP-KVM 远程控制卡

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PG4iajS4WhF81xBPIGxpS1sGez31pPiaiawy3O4yUdPxCfk1FljDACt8NhjeIN8kMbU2GjUP6eEAluXLA9v9pcebYOCOHlUwA55c/640?from=appmsg)
> **导语**：商用 IP-KVM 一台上千美元，树莓派的 PiKVM 也要 100 多美元。GitHub 上的 espkvm 项目只用一块 ESP32-P4 开发板加一个 HDMI 转 CSI 桥接器，就把价格砍到 45 美元——能远程操作目标机器的 BIOS、引导菜单、死机蓝屏，甚至能读回字符模式下的屏幕文本。

---

## 它是什么

IP-KVM（基于 IP 网络的键盘、视频、鼠标）是个老品类：把键盘、视频、鼠标信号通过网络投到另一台机器上操控。传统 IP-KVM 是机房管理员的命根子，机器没操作系统、起不来、内网断了都能用，远程桌面（RDP/VNC）干不了的活它全包。

espkvm 是这个老品类里的新派玩家。核心是两块硬件：Waveshare ESP32-P4-ETH（带 32MB PSRAM 和 100M 网口的 RISC-V 开发板，约 30 美元）加 Geekworm C790 HDMI 转 CSI-2 桥接板（约 15 美元）。两块板用一条 15 针 CSI 软排线对接，目标机器的 HDMI 输出一接、键盘鼠标 USB 一接，浏览器打开 `https://espkvm.local` 就能用。

整套 BOM（物料清单）45 美元，是 PiKVM 同档方案的 1/3，是商业 IP-KVM 的 1/20。

![espkvm 系统架构图：ESP32-P4-ETH 板通过 CSI 软排线连接 C790 HDMI 桥接器，可挂 OLED 状态屏和 GC9A01 圆形 LCD](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6ORRe8DO4CDGYEqPiaX8nm06nalKhsk9zUWFIW94ArqIDWa3pbibVmpTvTnjkpd2zWJej690icytMzLNfTEq1E5TxHCgVGOAMYs0M/640?from=appmsg "espkvm 系统架构图：ESP32-P4-ETH 板通过 CSI 软排线连接 C790 HDMI 桥接器，可挂 OLED 状态屏和 GC9A01 圆形 LCD")

## 硬件拆解

为什么是 ESP32-P4？因为这颗芯片内置硬件 H.264 编码器和 MIPI-CSI-2 摄像头接口，刚好能吃下 HDMI 桥接器的输出流。TC358743 把 HDMI 信号转成 CSI-2 摄像头协议，ESP32-P4 当摄像头用就行，JPEG 引擎和 H.264 编码器都是硬件的。

项目支持的板子一长串：Waveshare ESP32-P4-ETH、Espressif 自家的 Function EV Board、ESP32-P4-NANO、M5Stack Unit PoE-P4、VIEWE ESP32-P4-Pi，还有带 PoE（以太网供电）、WiFi 6、5GHz 频段的型号。最低门槛 32MB PSRAM（1080p 帧缓冲要 12.5MB），16MB 闪存（装双 OTA 槽位和救援镜像）。

有一点红队味儿很足：芯片分两个版本。v1.x 走 PPA（像素加速器）做颜色空间转换，H.264 1080p 只能跑到 7fps；v3.x 走原生 YUV422 直送编码器，同样的负载能跑 22-24fps，温度还低 12 度。默认构建是 v1.x，要跑 v3.x 得换 overlay 镜像。芯片版本烧错不致命，启动不了重刷就行，但别指望日志里有友好的提示。

## 软件特性

控制台是个 Vue 3 单页应用，整个 gzipped 后大约 70KB，没有外部字体、脚本、请求——离线网络也能用。

视频流两个选项：MJPEG 走 HTTP，任何浏览器都能看，1080p 大约 20fps；H.264 走 WebCodecs，码率压到 MJPEG 的 1/10，但只在 HTTPS 安全上下文里能解码。带宽紧张时自动切文本模式——把字符模式下的屏幕读回文字字符，几 KB 就传完。

键盘鼠标是单个 USB HID 复合设备：一个启动协议键盘（BIOS 认）、一个绝对指针（点击落到你瞄准的像素）、一个相对指针（捕获光标的软件用）、一组消费键。WebSocket 断了所有键自动释放，不会把目标机器卡在按住某键的鬼状态。

文本模式识别是杀手锏。BIOS 设置、UEFI 引导菜单、memtest、Linux 控制台——这些字符模式的屏幕，espkvm 不做 OCR，而是查字符生成器的字体表，要么精确匹配要么返回乱字符符号，不会"识别错了还一本正经"。

Runbook 自动化脚本：把"等 Press F2 to enter setup、按 f2、等 Boot、输入密码"这种操作写进脚本，扔在设备上自己跑，浏览器关了也能继续。每个 runbook 是家庭助理（Home Assistant）里的一个按钮，深夜三点服务器崩了不用爬起来开电脑。

家庭助理集成走 MQTT 自动发现，所有传感器、按钮、更新实体、相机快照全部自动出来。

![espkvm 浏览器控制台：左边是目标机器实时画面，右边是设置面板，能调码率、帧率、编解码器](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NPQibYia9icicic3pcic7KXkc7IkGCywVI5yGgXcmp2s7FMqneCQmfHJGCPLGiaGAK9ficFfhGa9W08Ah98kOTGCdyhNVjiaeiawibptBudg/640?from=appmsg "espkvm 浏览器控制台：左边是目标机器实时画面，右边是设置面板，能调码率、帧率、编解码器")

![espkvm 在家庭助理里的设备详情页：传感器、诊断、实时帧率、芯片温度、运行时间全部暴露](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NjqFMM4UNvCHFYeTEf4we0SjCqjXZ4PYNjv1pgQTvnEaSd3YialQs3YBqZKDGXfIDAGWiaDgCqVCnIRkvadhIWRYyRzhjEQJlCU/640?from=appmsg "espkvm 在家庭助理里的设备详情页：传感器、诊断、实时帧率、芯片温度、运行时间全部暴露")

## 安全边界

作者自己写了一段警告，原文翻译过来：登录有了，TLS 有了，但这些东西没经过安全审计。一台握着别人机器键盘的设备，值得被攻击。放可信网络里，或者用 VPN。设备内置了两种 VPN：Tailscale（不要端口映射、不用网关、证书在 tailnet 上也有效）和 WireGuard（自建 split tunnel，公钥在设备的 VPN 标签页里显示）。

admin/admin 是默认密码，登录后强制改。PBKDF2 加盐哈希，HttpOnly cookie 只在内存里（重启即失效），多次失败有指数退避。忘密码？长按板子上的物理按钮 2 秒，注意是重启之后按住，不是按住之后重启——后者会把芯片扔进固件下载模式。

有个细节很诚实：pre-3.0 芯片的 SD 卡控制器只读不写，4GB 以上 SDXC 卡可能完全不识别（FAT32 驱动没实现 64-bit LBA）。项目文档原话："要上传到卡上就买 16-32GB 的小品牌 SDHC 卡，大卡当只读媒体用读卡器预先准备好"。

## 性能实测

1080p 实测数据：Waveshare ESP32-P4-ETH（v1.3 芯片）MJPEG 20fps / H.264 7fps；Function EV（v3.2 芯片）MJPEG 23fps / H.264 22-24fps。空屏 MJPEG 0 kbit/s（不变化的帧直接丢），H.264 170 kbit/s（关键帧得发）。动屏 MJPEG 8.5 Mbit/s，H.264 500 kbit/s。芯片满载温度 46°C（v1.3）/ 34°C（v3.2），过温保护阈值是 70/85°C——到了先半帧率再停编码，但键鼠不断。

## 安装与获取

下载对应板子的 `espkvm-<版本>-<板子>-merged.bin` 镜像（覆盖 8 种官方板），用 esptool 烧录：

```
esptool --chip esp32p4 -b 921600 write-flash 0x0 espkvm-<version>-<board>-merged.bin
```

或者直接用浏览器刷：espkvm.io/flash，Chrome 或 Edge 都能用，不用装东西。

源码仓库：github.com/espkvm/espkvm，Web 控制台是子模块，记得 `git clone --recursive`。自带演示：demo.espkvm.io。

## 总结

espkvm 不是要取代 PiKVM 或 JetKVM——后者树莓派的算力能做更多事，比如 4K 捕获、ATX 全套控制、VNC 旁路。espkvm 的价值是把这事的入门门槛砍到 45 美元，让"机房里每台机器挂一个 KVM"从奢侈品变成常态。

对红队来说，多一个能藏在机房角落、待机功耗不到 2W、看上去就是个普通嵌入式开发板的远程控制设备，意味着应急响应和带外管理多了一种廉价冗余。Hackaday、CNX Software、Circuit Rocks 等七八家技术媒体已经做过专题，RISC-V International 的周报也收过它。

代码全部 MIT 协议，板子照片归各家厂商（仅作硬件识别用途），3D 打印外壳是 CC BY-NC 协议作者公开的 Printables 模型。fork、改造、量产随便——但别放公网。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6Pnb9I7u2Jiacw5WrZLKxRLdrW1yXwXZPTXYr9hfMicfMiaBqoME3Le5xfv7wxysC3HRNEoZ9wHQ4INBgWWANK14FAIibGXKjT0SLY/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6No8AkqBnkqEVAlWg9AKP78nCBc5IIuFqYkXpUq2ZRXt2QicY6OiaWR3iaD4aQ4vRwziaKhZrQyvZySIwvT7sn8qXyJr83BejSNh5o/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MlyBA0e1ibd7oGTr9rQC3t6aavo8siaE7XKJAgXO4N5TFzsgk5Gtt2kO0aeONfoOUzZhvrcD5NP1pNnubcIJ3OwuctWDWiczaDZE/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6P2oiauBGvqhLl8hbswURttkibvoV1NQSfOGvdHTic4icjwicKKku6Y8aeqphtG3NJ6ELwAXSx4lt1XdJ820OsHC7v16iaYUjtz5brIs/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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