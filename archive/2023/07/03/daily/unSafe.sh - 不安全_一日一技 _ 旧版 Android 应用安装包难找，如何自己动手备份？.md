---
title: 一日一技 | 旧版 Android 应用安装包难找，如何自己动手备份？
url: https://buaq.net/go-170979.html
source: unSafe.sh - 不安全
date: 2023-07-03
fetch_date: 2025-10-04T11:52:30.694701
---

# 一日一技 | 旧版 Android 应用安装包难找，如何自己动手备份？

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

![](https://8aqnet.cdn.bcebos.com/685cc108389657e67a628b866930b70d.jpg)

一日一技 | 旧版 Android 应用安装包难找，如何自己动手备份？

一日一技 | 旧版 Android 应用安装包难找，如何自己动手备份？ 在图标下方加了个促销活动的横幅广告，舍弃了对你来说不可或缺的重要功能，加入了应用更加臃肿甚至导致 bug 的无聊特性，抑或是耗
*2023-7-2 10:3:57
Author: [sspai.com(查看原文)](/jump-170979.htm)
阅读量:28
收藏*

---

一日一技 | 旧版 Android 应用安装包难找，如何自己动手备份？

在图标下方加了个促销活动的横幅广告，舍弃了对你来说不可或缺的重要功能，加入了应用更加臃肿甚至导致 bug 的无聊特性，抑或是耗电更快、界面更丑、后台行为更流氓……国内 app 适配 Android 平台新特性的积极性很低，所以我们选择旧版本的原因也有很多。

不幸的是此前我们[推荐](https://sspai.com/post/62634)过的豌豆荚，最近也关闭了历史版本的下载通道（感谢少数派会员 [@造纸陀螺](https://sspai.com/u/zd512y1z) 的[提醒](https://sspai.com/t/wb7npvytob9j)），考虑到酷安一般仅提供一个历史版本可选，历史版本齐全但对网络环境有要求的 APKMirror 又几乎没有国内应用，历史版本存档这件事也就自然而然地落在了用户自己的头上。

![UtI1bx2TooZnEzxaXU0crUP1nee](https://cdn.sspai.com/editor/u_/cigdjndb34tflhqmngtg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

本文介绍三种免 root 备份应用安装包的方法。

## adb

**注：需要一定的 adb 基础，觉得麻烦的朋友请跳过该部分选择其他解决方案**。

理论上来说，大部分免 root 玩机解决方案都绕不开 adb 这个简单又神奇的工具。对于应用备份需求，我们同样可以在开启 USB 调试之后借助几条命令来搞定（# 号后面注释可以不用复制）：

```
adb shell
pm list packages #列出本机应用包名，如果你看着包名依然难以确定其对应的应用，也可以通过查看对应的酷安下载页面 URL 链接后缀来进行确认
pm path com.abc.def #列出包名 com.abc.def 对应 app 的所有安装包文件路径
adb pull 导出路径 存放路径 #将安装包推送至指定位置
```

**关联阅读**：[如何从零开始使用 adb](https://sspai.com/post/57427)

用这种方法最简单、除了 adb 环境配置外也无需安装任何第三方工具。但随着多 APK 特性以及 AAB 分发格式的推广与普及，运行 `pm path` 这条命令后，你可能会遇到同一个应用对应数个安装包的情况。

![U9P6bTYlkogLyuxt38Kct9pWnye](https://cdn.sspai.com/editor/u_/cigdjndb34tfk9qgdvog?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

比如当前最新的 Play 版微信就包含这么多组件

为了保证下一次使用时能够正常安装，我们必须将这些 apk 文件一一导出然后打包，并且后续使用以下命令完成安装：

```
adb install-multiple "a.apk" "b.apk" "c.apk"
```

**关联阅读**：[看懂「非典型」APK 文件](https://sspai.com/post/60228)

## Skit & Swift Backup

不难看出，应用所对应的组件越多，导出后进行打包、备份和管理以及后续的安装流程就越麻烦。对于不想折腾的朋友，我们推荐操作更简单、打包方式更优雅的图形化应用解决方案：[Skit](https://sspai.com/post/63479) 或者 [Swift Backup](https://sspai.com/post/55454)。

打开 Skit，首先前往应用「设置 - 应用程序」界面，在「提取」部分选择备份目录，格式设定为 `Split APK（APKS）优先`，同时将「APK/APKS 的名称」设定为对你而言更容易记忆和管理的格式。

![IAltb2Il7o9eWuxcBjdcXE82nRe](https://cdn.sspai.com/editor/u_/cigdjnlb34tfka09pl40?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Skit 设置

设置完成后，我们只需前往「应用程序」标签，通过顶部的搜索和过滤器找到想要备份的应用，长按选中并通过底部的导出按钮进行备份。你可以同时选中多个需要备份的应用来进行批量导出。

![Qqw2bUEV8oc8HmxLAJ4cJL0jnDc](https://cdn.sspai.com/editor/u_/cigdjntb34tflnodqvug?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

支持批量导出

导出后我们就可以借助自己喜欢的工具对这些应用安装包进行存档和备份了。如果你导出的应用主要为 `.apks` 格式，后续在恢复时则需要用到 SAI 这样的工具来进行安装。我们此前在 APKS 和 Shizuku 的文章中对这款工具均有介绍，这里便不再赘述了。

**关联阅读**：[Shizuku：让 Android 免 root 玩机更简单](https://sspai.com/post/73294)

除了 Skit，Android 老牌备份工具 Swift Backup 同样可以在免 root 的前提下解决最基本的安装包备份需求：安装应用后在主界面的「应用」标签中借助搜索或过滤器找到目标应用，点击进入详情界面后即可对当前版本对应的安装包进行备份。

![Gd4Ybe7B6oIrSdx2Bf5cAdc0nFh](https://cdn.sspai.com/editor/u_/cigdjo5b34tflnodqvv0?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Swift Backup 的备份、恢复与设置

相比 Skit，Swift Backup 还支持直接在应用内对 `.apks` 格式文件进行恢复，针对历史版本保留这一特殊需求，这里也建议大家前往应用「设置 - 应用备份」界面勾选启用「保存应用备份的旧版本」功能，同时借助应用内的自动化「计划」功能配置定期备份。

![EEKjbJ5aZoIcFhxwtV8cTnHPnMf](https://cdn.sspai.com/editor/u_/cigdjodb34tflnodqvvg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

通过「计划」功能配置定期备份

以上便是本文的全部内容。还有哪些地方可以下载 Android 应用的历史版本，你又有什么特别的应用安装包备份方案？欢迎在评论区留言补充。

> 下载 [少数派 2.0 客户端](https://sspai.com/page/client)、关注 [少数派公众号](https://sspai.com/s/J71e)，解锁全新阅读体验 📰

> 实用、好用的 [正版软件](https://sspai.com/mall)，少数派为你呈现 🚀

文章来源: https://sspai.com/post/80776
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)