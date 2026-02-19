---
title: AYA，图形化ADB桌面应用神器
url: https://mp.weixin.qq.com/s/A7pENZaR9eABwC-_LJupwg
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:16:55.995511
---

# AYA，图形化ADB桌面应用神器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KysoJFiczHUsaSuaATegQYyzfQLhpn116PMzm2ibIuPxDLQs8Ucr4O3ybFUrJMwpibPWbumBpIGQWoIxaJm5rDkmHVhdU36Toxw6B2UfZjmXBk/0?wx_fmt=jpeg)

# AYA，图形化ADB桌面应用神器

柠檬赏金猎人

![]()

在小说阅读器中沉浸阅读

### 概述

AYA 是一款开源的桌面应用程序，旨在为开发者、测试人员以及任何需要与安卓设备进行深度交互的用户提供一个图形化、便捷的控制界面。它本质上是一个功能丰富的 ADB（Android Debug Bridge）图形化封装工具，让你无需记忆复杂的命令行指令，即可轻松完成屏幕镜像、文件管理、应用调试、性能监控等一系列操作。支持 Windows、macOS 和 Linux 三大主流操作系统。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KysoJFiczHUs45Tic3Y2OCqNWjdbF0Y2sR6MBbCoqXSR29kC4ltzPYgFnicBYWY7lcMxUT7ibApYDVt1iaweF0oDf8zHBfTlXVw2AyiauQBGmyf5c/640?wx_fmt=jpeg)

### 技术/功能

AYA 基于现代 Web 技术栈构建，核心特性包括：

* **核心技术栈**：采用 Electron 框架，结合 TypeScript、SCSS 等前端技术，实现了跨平台的桌面应用体验。
* **核心功能模块**：
  + **屏幕镜像**：实时投射安卓设备屏幕到电脑桌面，支持触控操作。
  + **文件浏览器**：可视化浏览、上传、下载和管理设备上的文件系统。
  + **应用管理器**：轻松查看、安装、卸载应用程序，管理应用权限。
  + **进程监视器**：实时监控设备上运行的进程及其资源占用情况。
  + **布局检查器**：分析应用界面布局层级，辅助UI调试。
  + **性能监控**：实时查看设备的 CPU、内存使用率以及应用帧率（FPS）。
  + **日志查看器（Logcat）**：图形化界面查看和筛选设备系统及应用的运行日志。
  + **交互式 Shell**：内置终端，可直接执行 ADB 命令，兼顾便捷与灵活。

### 使用示例

以下是一个简单的使用流程，展示如何通过 AYA 进行屏幕镜像和文件管理：

1. **安装与连接**：

   * 从 GitHub Releases 页面下载对应系统（Windows/macOS/Linux）的安装包并安装。
   * 确保你的安卓设备已开启“开发者选项”和“USB调试”模式。
   * 使用 USB 数据线将设备连接到电脑。首次连接时，设备上可能会弹出授权提示，请点击“允许”。
   * 启动 AYA 应用，它通常会自动检测并列出已连接的设备。
2. **屏幕镜像操作**：

   * 在设备列表中选中你的设备。
   * 点击左侧功能栏的“Screen Mirror”（或类似图标）按钮。
   * 稍等片刻，设备的屏幕画面就会显示在 AYA 的窗口中。你可以直接用鼠标在镜像画面上点击、滑动来操作设备。
3. **文件管理操作**：

   * 点击功能栏的“File Explorer”按钮。
   * 界面会分为左右两栏，左侧是电脑本地文件系统，右侧是安卓设备的文件系统。
   * **上传文件**：在左侧本地目录找到文件，直接拖拽到右侧设备目录中。
   * **下载文件**：在右侧设备目录找到文件，直接拖拽到左侧本地目录中。
   * **删除/重命名**：在设备文件列表上右键点击文件或文件夹，会弹出操作菜单。
4. **查看应用日志（Logcat）**：

   * 点击“Logcat Viewer”按钮。
   * 你将看到一个不断滚动的日志面板。你可以使用顶部的筛选框，通过进程ID（PID）、标签（Tag）或日志级别（如 Error, Warning）来过滤信息，快速定位问题。

### 注意事项

1. **设备准备**：使用前务必在安卓设备上开启“开发者模式”和“USB调试”。不同品牌手机开启方式略有不同，通常需要在“设置”-“关于手机”中连续点击“版本号”7次。
2. **驱动与ADB**：在 Windows 系统上，首次连接某些品牌的手机可能需要安装对应的 USB 驱动程序。AYA 通常自带 ADB，但如果遇到连接问题，可以尝试在系统上单独安装完整的 Android SDK Platform-Tools。
3. **安全授权**：每次连接新电脑或重启ADB服务后，设备端会弹出调试授权请求，必须点击“允许”才能建立连接。
4. **性能影响**：屏幕镜像功能会占用一定的设备资源和网络带宽（如果是无线连接），在高帧率或高分辨率下可能影响设备性能。
5. **开源协议**：AYA 采用 AGPL-3.0 开源协议。这意味着如果你要修改其代码并进行分发，需要遵循相应的开源义务。

### 参考链接

* 项目主页与在线文档：https://aya.liriliri.io
* GitHub 仓库与下载：https://github.com/liriliri/aya
* Product Hunt 页面：https://www.producthunt.com/posts/aya-1

---

仅限交流学习使用，如您在使用本工具或代码的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。“如侵权请私聊公众号删文”。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/OkRKg4J9smV0q1aJxxA7GF9uXFH0S6D3QRb0jNcE13icxpHvErdgibarS4mwYYE2aicga15MMmcOCdTazgj9ibn0RA/0?wx_fmt=png)

柠檬赏金猎人

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OkRKg4J9smV0q1aJxxA7GF9uXFH0S6D3QRb0jNcE13icxpHvErdgibarS4mwYYE2aicga15MMmcOCdTazgj9ibn0RA/0?wx_fmt=png)

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