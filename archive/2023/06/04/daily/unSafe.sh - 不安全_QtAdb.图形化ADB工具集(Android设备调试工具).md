---
title: QtAdb.图形化ADB工具集(Android设备调试工具)
url: https://buaq.net/go-167072.html
source: unSafe.sh - 不安全
date: 2023-06-04
fetch_date: 2025-10-04T11:44:38.339278
---

# QtAdb.图形化ADB工具集(Android设备调试工具)

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

![](https://8aqnet.cdn.bcebos.com/488779279078a54d1b8a8295944dcaad.jpg)

QtAdb.图形化ADB工具集(Android设备调试工具)

QtAdb 是一个基于 Qt 的PC端 Android 工具集合。集成了Android 调试桥 (adb) (opens new window)的一系列
*2023-6-3 14:44:0
Author: [blog.upx8.com(查看原文)](/jump-167072.htm)
阅读量:51
收藏*

---

![](https://img.imgdd.com/f210f3.3dd59dec-4931-4af1-a332-ab7e72220e5f.png)

QtAdb 是一个基于 Qt 的PC端 Android 工具集合。集成了Android 调试桥 (adb) (opens new window)的一系列常用命令。

Android (opens new window)系统的可玩性在 adb 的加成下变得更加丰富，由此涌现出众多的命令用法。非开发者的Android 爱好者经常根据需求运行 adb 命令以提升使用体验。

但由于 adb 涉及到环境配置、终端执行等操作，对于不会使用的人可能造成困扰；一些参数对于并不熟悉的人来说同样头疼。

所以可供一键式操作，并且已内置环境的GUI有一定需求，QtAdb应运而生。

软件作者@LapplandSP

## 软件特点

QtAdb 已内置 adb 环境，并可在运行时自行配置，使用者无需关心环境变量的配置情况。封装命令的具体内容将在后文说明。

支持 Windows 11 中的 Android 子系统（WSA）。应在 WSA 运行时连接 WSA。

支持 Android R (11) 及以上版本的无线调试。

提供命令模板，使用者可直接复制命令并自行执行。可直接在 QtAdb 中打开 adb 环境下的命令行窗口。

支持多种设备状态：开机、Recovery 及 adb sideload

## 设备信息

* 获取设备型号、屏幕分辨率、屏幕密度（DPI）、Android Id、安卓版本以及处理器型号的信息
* 修改 DPI、修改屏幕分辨率
* 实时监控CPU使用率、内存使用率。

## ✔️激活

* 提供主流工具应用的激活：
  + [黑阈(opens new window)](https://brevent.jianyv.com/)
  + [冰箱(opens new window)](https://iceboxdoc.catchingnow.com/)
  + [小黑屋(opens new window)](https://stopapp.https.gs/)
  + [Shizuku(opens new window)](https://shizuku.rikka.app/zh-hans/)
  + *黑洞*
  + [太极(opens new window)](https://taichi.cool/)
  + [Island(opens new window)](https://island.oasisfeng.com/)
  + Scene
  + [看帧数+(opens new window)](https://www.coolapk.com/apk/com.watchfps)
  + [权限狗(opens new window)](https://www.coolapk.com/apk/com.web1n.permissiondog)
  + [雹(opens new window)](https://github.com/aistra0528/Hail)
  + [安装狮(opens new window)](https://www.coolapk.com/apk/com.modosa.apkinstaller)

## 🎮设备控制

* 电源控制：
  + 关机
  + 重启到系统
  + 重启到 Recovery
  + 重启到 Fastboot

* 按键模拟：
  + 系统导航：返回键、主页键、菜单键、任务键
  + 实体按键：电源键、音量 + 、音量 - 、静音、拍照（处于相机应用中时）、唤起助理应用
  + 媒体控制：播放音乐、停止播放、上一曲、继续、暂停、下一曲
  + 其他指令：亮度 - 、亮度 + 、系统休眠、点亮屏幕、挂断电话
  + 拉起系统应用：设置、通讯录、拨号、浏览器、音乐、日历、计算器

* 命令行：
  + 运行自定义的 adb 命令
  + 直接在 adb 环境中打开命令行窗口

## 📦软件包管理器：

* 安装应用
* 列出已知的权限
  + 可单独打开大窗口查看列表
  + 可按以下要求输出：
    - 按权限组进行整理
    - 输出所有信息
    - 输出简短摘要
    - 仅列出危险权限
    - 仅列出用户将看到的权限

* 列出已知的权限组

* 列出软件包
  + 卸载、停用、启用、清除数据
  + 获取软件包包名、安装者、关联文件等信息

* 列出系统的所有功能

* 列出当前设备支持的所有库

* 用户
  + 列出当前设备中的所有用户
  + 删除选中用户

## 🔮其它功能

* 账户
  + 查看设备中各个用户已登录的账户

* 去除叹号
  + 修改验证服务器，提供了多个预设选项（MIUI、EMUI等国内验证服务器）

* 修改过渡动画
  + 修改动画时长
  + 修改过渡动画
  + 修改窗口动画

* 状态栏与导航栏
  + 隐藏状态栏图标：静音/震动、定位、麦克风、录屏状态、WIFI、热点、飞行模式、耳机、闹钟、蓝牙、NFC
  + 重置状态栏图标
  + 全局隐藏状态栏、导航栏

## 💣不稳定功能

* 侧载：
  + 设备处于 sideload 模式时，可以使用侧载功能刷入 .zip 包。
  + 侧载不稳定，**使用该功能刷入过大的ROM时，可能会在没有刷入完成时显示已完成，请以设备端显示为准**，此时请不要切换页面，更不要关闭程序，这将导致刷入失败；
  + sideload 本就是危险功能，即使程序正确运行，也可能导致刷入失败，无法开机。

## 更新日志

理论上解决了闪退的恶性bug

## 软件下载

开源地址：<https://github.com/LapplandSP/QtAdb>

<https://www.123pan.com/s/HQeA-Yd4Sh>

<https://pan.quark.cn/s/d3959d7a94e7>

文章来源: https://blog.upx8.com/3615
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)