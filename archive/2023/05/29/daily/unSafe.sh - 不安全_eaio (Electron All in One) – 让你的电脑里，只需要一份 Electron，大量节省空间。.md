---
title: eaio (Electron All in One) – 让你的电脑里，只需要一份 Electron，大量节省空间。
url: https://buaq.net/go-166072.html
source: unSafe.sh - 不安全
date: 2023-05-29
fetch_date: 2025-10-04T11:37:00.508742
---

# eaio (Electron All in One) – 让你的电脑里，只需要一份 Electron，大量节省空间。

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

![](https://8aqnet.cdn.bcebos.com/b41efd1c2a99f9c4eac7ec080079ea17.jpg)

eaio (Electron All in One) – 让你的电脑里，只需要一份 Electron，大量节省空间。

HomeWindowseaio (Electron All in One) – 让你的电脑里，只需要一份 Electron，大量节省空间。
*2023-5-28 12:57:55
Author: [www.appinn.com(查看原文)](/jump-166072.htm)
阅读量:49
收藏*

---

[Home](https://www.appinn.com)

[Windows](https://www.appinn.com/category/windows/)

eaio (Electron All in One) – 让你的电脑里，只需要一份 Electron，大量节省空间。

**eaio (Electron All in One)** 是一个通过将磁盘上所有 [Electron](https://github.com/electron/electron) 应用中相同文件硬链接到统一位置来减少磁盘占用的解决方案，就像 `pnpm` 一样。@[Appinn](https://www.appinn.com/eaio-electron-all-in-one/)

![eaio (Electron All in One) - 让你的电脑里，只需要一份 Electron，大量节省空间。](https://static1.appinn.com/images/202305/eaio-electron-all-in-one.jpg!o "eaio (Electron All in One) - 让你的电脑里，只需要一份 Electron，大量节省空间。 1")

## Electron 是什么？

Electron 是一个用于构建跨平台桌面应用的开源框架。对于开发者来说，它简化了跨平台的开发，并且拥有强大的调试工具和丰富的插件与生态。但对用户来说，每一个使用 Electron 的软件都会引入一整套程序，于是就有了这个：

* [CEF Detector – 你的电脑上共有几个 Chromium/Electron 内核的应用？](https://www.appinn.com/cef-detector/)

![eaio (Electron All in One) - 让你的电脑里，只需要一份 Electron，大量节省空间。 1](https://meta-cdn1.appinn.com/uploads/default/optimized/3X/1/3/13b48fd747a9d1b24197518ad943cfc971cd84df_2_936x1000.jpeg "eaio (Electron All in One) - 让你的电脑里，只需要一份 Electron，大量节省空间。 2")

每个人的电脑里有 5+ 以上的重复 Electron 都属于常规 😂

又于是，就有了这个：

## eaio (Electron All in One)

来自[**发现频道**](https://meta.appinn.net/c/faxian/10)，手搓大佬 @**[wankkoree](https://meta.appinn.net/u/wankkoree)** 的作品。

还在苦恼大前端趋势下，硬盘中 Electron 应用越来越多吗？本工具可以将 Electron 应用硬链接到其所在磁盘分区根目录的`.electron`仓库中，从而实现一份文件多应用使用，大大减少磁盘占用。（最终效果取决于：同一磁盘分区中，同一 Electron 版本和架构的应用有多少）

### 原理

硬链接会将多个文件指向同一磁盘位置，使得多个相同的文件只占用一份空间。

本工具支持自动识别应用入口、自动判断 Electron 版本和架构、自动判断是否应该被硬链接。

具体效果可通过 `[WizTree](https://www.appinn.com/wiztree/)` 查看。

![eaio (Electron All in One) - 让你的电脑里，只需要一份 Electron，大量节省空间。 2](https://meta-cdn1.appinn.com/uploads/default/original/3X/1/c/1c1d67d49de3ab476bd3e4d306971eb4aac0b22e.jpeg "eaio (Electron All in One) - 让你的电脑里，只需要一份 Electron，大量节省空间。 3")

![eaio (Electron All in One) - 让你的电脑里，只需要一份 Electron，大量节省空间。 3](https://meta-cdn1.appinn.com/uploads/default/original/3X/3/a/3a730ec4d82d04f26edbb8bc17402ec775b21864.jpeg "eaio (Electron All in One) - 让你的电脑里，只需要一份 Electron，大量节省空间。 4")

### Q&A

1. Q: 为什么不用更优雅的软链接？A: 软链接状态下的`electron.exe`无法正确判断运行目录(如有解决方法欢迎讨论)，且可能因为一些原因造成误删。
2. Q: 为什么不用`electron`命令行指定`resources`路径？A: 一些应用会在运行目录下放置额外的`.exe`或`.dll`文件，指定应用路径可能会造成应用无法找到这些文件。
3. Q: 只支持 Windows 吗？A: 其他系统暂未测试有效性，如本方案可用于其它系统，后续会支持。

### 注意事项

1. 本工具会在执行`link`或`check`操作时，在目标应用所在的磁盘分区下创建`.electron`仓库，用于存储硬链接的源文件，如无特殊情况请**不要删、改**。
2. 本工具的`status`操作可以检查所有磁盘分区下`.electron`仓库中所有版本的完整性和有效性，可用于检查**下载完成**情况、源文件**存在**情况、源文件**改动**情况。
3. 本工具的`download`操作可以下载目标版本和架构的`Electron`预编译程序到指定磁盘分区的`.electron`仓库中，如果已存在则会进行**覆盖**，所以也可用于对源文件的**恢复/修复**。
4. 请不要对已链接的`Electron`应用进行**文件粉碎**操作，可能会导致源文件改动。
5. 请不要对`.electron`仓库进行**文件粉碎**操作，可能会导致已链接的`Electron`应用文件改动。

## 获取

* [GitHub](https://github.com/WankkoRee/eaio)
* [下载页面](https://github.com/WankkoRee/eaio/releases)

有使用疑问的同学可以前往[**发现频道**](https://meta.appinn.net/c/faxian/10)与开发者沟通：

* 发现频道：<https://meta.appinn.net/t/topic/43916>

另外，开发者提到：Linux 与 MacOS 待适配。

---

文章来源: https://www.appinn.com/eaio-electron-all-in-one/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)