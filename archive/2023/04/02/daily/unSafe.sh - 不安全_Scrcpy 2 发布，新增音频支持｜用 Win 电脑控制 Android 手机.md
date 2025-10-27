---
title: Scrcpy 2 发布，新增音频支持｜用 Win 电脑控制 Android 手机
url: https://buaq.net/go-156456.html
source: unSafe.sh - 不安全
date: 2023-04-02
fetch_date: 2025-10-04T11:26:33.409239
---

# Scrcpy 2 发布，新增音频支持｜用 Win 电脑控制 Android 手机

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/d40b7335c73af848876fe4f927858b57.jpg)

Scrcpy 2 发布，新增音频支持｜用 Win 电脑控制 Android 手机

*2023-4-1 14:21:16
Author: [www.appinn.com(查看原文)](/jump-156456.htm)
阅读量:51
收藏*

---

**[Scrcpy](https://www.appinn.com/tag/scrcpy/)** 是一款可以在电脑上通过鼠标键盘控制 Android 手机的开源工具，无需 root 权限，支持数据线与 Wi-Fi 连接。[上个月](https://blog.rom1v.com/2023/03/scrcpy-2-0-with-audio/?ref=its-foss-news)发布了 2.0 版本，新增对低延迟音频的支持，Android 11 以上设备可用。@[Appinn](https://www.appinn.com/scrcpy-2/)

![Scrcpy 2 发布，新增音频支持｜用电脑控制 Android 手机](https://static1.appinn.com/images/202303/scrcpy-2.jpg!o "Scrcpy 2 发布，新增音频支持｜用 Win 电脑控制 Android 手机 1")

眼看着 Scrcpy 一路走来：

* 命令行版：[Scrcpy – 用电脑控制 Android 手机[Win/macOS/Linux]](https://www.appinn.com/scrcpy-remote-android-from-computer/)
* 图形界面：[用电脑控制 Android 手机的 Scrcpy 拥有更易使用的图形界面了](https://www.appinn.com/scrcpy-gui/)(第三方)
* [Scrcpy Remote – 用 iPhone 远程控制 Android 设备[iOS]](https://www.appinn.com/scrcpy-remote/)
* [ws-scrcpy – 用浏览器远程控制 Android 手机，实现云手机效果](https://www.appinn.com/ws-scrcpy/)

## Scrcpy 2

根据 [itsfoss](https://news.itsfoss.com/scrcpy-2-0-release/) 的描述，Scrcpy 2.0 主要新增的功能是在 Android 11+ 设备上引入了实时音频转发。

这意味着现在可以将连接的 Android 设备上的音频流式传输和录制到主机，而不会出现明显的延迟。

Scrcpy 一直都是一个备受欢迎的程序，这项新功能是自第一个版本发布以来最受欢迎的功能之一。

经过大量实验，开发团队最初采用了名为“USBaudio”的解决方案，但效果不佳。后来，他们开发了一个名为“sndcpy”的原型，但也遇到了一些问题。

幸运的是，Scrcpy 用户提供了一个概念验证，可以使用 Android 上的 shell 权限捕获设备音频，并提供了 Android 11 的解决方法。新功能使用 Android 的低延迟友好 API 来录制音频，“MediaCodec”API 来编码捕获的音频，并使用新的“音频播放器组件”提供音频输出，延迟非常小。此外，音频和视频流由“解复用器”解复用为数据包。

### 哪些设备可用

在 Android 12 及更高版本上，音频转发功能**开箱即用**。但是，对于 Android 11，您必须在启动 Scrcpy 时**解锁屏幕**才能成功捕获音频。

### 如何使用

使用简单，首先确认你的手机与电脑连接，并且在命令行输入 adb devices 可以看到它（需要先安装 adb 命令），然后输入：

就能在电脑上看到手机屏幕了。是的，非常简单。

![Scrcpy 2 发布，新增音频支持｜用 Win 电脑控制 Android 手机 1](https://static1.appinn.com/images/202303/screenshot-debian-600.jpg!o "Scrcpy 2 发布，新增音频支持｜用 Win 电脑控制 Android 手机 2")

对于其他需求，可以使用以下命令：

可以通过以下方式禁用音频：

如果启用了音频，则还会录制音频：

与视频不同，音频需要一些缓冲，即使是实时的。缓冲区大小 需要足够小以保持可接受的延迟，但又足够大以尽量减少缓冲区欠载，这会导致音频故障。默认缓冲区大小设置为 50 毫秒，但可以调整：

为了提高播放流畅度，可以故意增加延迟：

```
scrcpy --audio-buffer=200
```

例如，这很有用，可以将个人视频投影到更大的屏幕上：

```
scrcpy --video-codec=h265 --display-buffer=200 --audio-buffer=200
```

还可以选择音频编解码器和比特率（默认为 128Kbps 的 Opus）

```
scrcpy --audio-codec=opus --audio-bit-rate=16k
scrcpy --audio-codec=aac --audio-bit-rate=16k
```

---

文章来源: https://www.appinn.com/scrcpy-2/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)