---
title: Go MusicFox – 终端里的「网易云音乐」，就该这么用电脑
url: https://buaq.net/go-153762.html
source: unSafe.sh - 不安全
date: 2023-03-17
fetch_date: 2025-10-04T09:49:49.586224
---

# Go MusicFox – 终端里的「网易云音乐」，就该这么用电脑

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

![](https://8aqnet.cdn.bcebos.com/7327ca65b9948533f8cf6d5509b91abd.jpg)

Go MusicFox – 终端里的「网易云音乐」，就该这么用电脑

*2023-3-16 20:47:26
Author: [www.appinn.com(查看原文)](/jump-153762.htm)
阅读量:57
收藏*

---

**Go MusicFox** 是一款在终端中运行的网易云音乐播放器，通过命令行的方式实现登录、播放、下载、搜索、歌词、Last.fm、签到等功能。很酷，电脑就该这么用。@[Appinn](https://www.appinn.com/go-musicfox/)

![Go MusicFox - 终端里的「网易云音乐」，就该这么用电脑](https://static1.appinn.com/images/202303/go-musicfox.jpg!o "Go MusicFox - 终端里的「网易云音乐」，就该这么用电脑 1")

来自[**发现频道**](https://meta.appinn.net/c/faxian/10)，@touchmii 同学的推荐：<https://meta.appinn.net/t/topic/41717>

青小蛙看到这款软件的第一反应是：终端居然也可以发出声音 😂

## 什么是终端？

终端（Terminal）可以指代一个软件程序，它允许用户与计算机进行交互式的会话。终端程序通常提供一个文本界面，用户可以在其中输入命令或操作系统指令，以完成特定的任务。

一般的终端软件，有命令提示符（CMD）、PowerShell、Windows Terminal、iTerm、Kitty 等。

## Go MusicFox

先来看视频吧，反正青小蛙觉得非常有意思：

就像B站 @幕恪l 同学说的：「妙啊，有种返璞归真的美」，青小蛙也这样觉得。

虽然终端在视觉上一向给人功能不全的感觉，但 Go MusicFox 可以实现相当多的 macOS 交互，包括通知、菜单栏播放中状态、歌词显示、快捷键，甚至可以在 Mac 下实现睡眠暂停、蓝牙耳机连接断开响应、菜单栏控制等。

（这方面 Windows 版本要弱一点 😂）

### 快捷键 && 下载

支持扫码登录，支持切换不同播放引擎（beep / mpd / osx），支持下载，只需要在听歌的时候，按下快捷键 `d` 就能下载到本地…

其它快捷键：

| 按键 | 作用 | 备注 |
| --- | --- | --- |
|
|  |
| h/H/LEFT | 左 |  |
| l/L/RIGHT | 右 |  |
| k/K/UP | 上 |  |
| j/J/DOWN | 下 |  |
| g | 上移到顶部 |  |
| G | 下移到底部 |  |
| q/Q | 退出 |  |
| space | 暂停/播放 |  |
| [ | 上一曲 |  |
| ] | 下一曲 |  |
| – | 减小音量 |  |
| = | 加大音量 |  |
| n/N/ENTER | 进入选中的菜单 |  |
| b/B/ESC | 返回上级菜单 |  |
| w/W | 退出并退出登录 |  |
| p | 切换播放方式 |  |
| P | 心动模式(仅在歌单中时有效) |  |
| r/R | 重新渲染UI | 如果UI界面因为某种原因出现错乱，可以使用这个重新渲染 |
| c/C | 当前播放列表 |  |
| , | 喜欢当前播放歌曲 |  |
| < | 喜欢当前选中歌曲 |  |
| . | 当前播放歌曲移除出喜欢 |  |
| > | 当前选中歌曲移除出喜欢 |  |
| t | 标记当前播放歌曲为不喜欢 |  |
| T | 标记当前选中歌曲为不喜欢 |  |
| d | 下载当前播放歌曲 |  |
| D | 下载当前选中歌曲 |  |
| / | 搜索当前列表 |  |
| ? | 帮助信息 |  |
| a | 播放中歌曲的所属专辑 |  |
| A | 选中歌曲的所属专辑 |  |
| s | 播放中歌曲的所属歌手 |  |
| S | 选中歌曲的所属歌手 |  |
| o | 网页打开播放中歌曲 |  |
| O | 网页打开选中歌曲/专辑… |  |
| ;/: | 收藏选中歌单 |  |
| ‘/” | 取消收藏选中歌单 |

另外，还可以手动修改配置文件 go-musicfox.ini，位于用户目录下的 `.go-musicfox/go-musicfox.ini`，比如 Windows 就是 `C:\Users\用户么\.go-musicfox\` 下，macOS 下是 `/Users/用户名/.go-musicfox`，里面有不少设置。

## 支持 UnblockNeteaseMusic

支持通过 kuwo,kugou,migu,qq 来解锁灰色的音乐。

## 获取

* [GitHub](https://github.com/go-musicfox/go-musicfox?utm_source=appinn.com)
* [搬运](https://d.appinn.com/go-musicfox/)

Mac 用户可以通过 `brew install anhoder/go-musicfox/go-musicfox` 安装。

对于终端爱好者来说，真是一款不错的工具。

原文：https://www.appinn.com/go-musicfox/

文章来源: https://www.appinn.com/go-musicfox/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)