---
title: RDP 优化操作 微软远程桌面 开启显卡加速、60FPS、USB设备重定向_csdn_life18的博客-CSDN博客_远程桌面60帧
url: https://buaq.net/go-141029.html
source: unSafe.sh - 不安全
date: 2022-12-23
fetch_date: 2025-10-04T02:18:05.788465
---

# RDP 优化操作 微软远程桌面 开启显卡加速、60FPS、USB设备重定向_csdn_life18的博客-CSDN博客_远程桌面60帧

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

![](https://8aqnet.cdn.bcebos.com/72c0f6b3d7cc780a944fc5ec5c06676e.jpg)

RDP 优化操作 微软远程桌面 开启显卡加速、60FPS、USB设备重定向\_csdn\_life18的博客-CSDN博客\_远程桌面60帧

于 2020-08-2
*2022-12-22 20:20:6
Author: [blog.csdn.net(查看原文)](/jump-141029.htm)
阅读量:48
收藏*

---

![](https://csdnimg.cn/release/blogv2/dist/pc/img/reprint.png)

于 2020-08-27 00:42:46 首次发布

### 文章目录

* + [显卡加速](#_6)
  + [提升传输帧率](#_28)
  + [开启RemoteFX USB重定向](#RemoteFX_USB_64)
  + [使用软件强制调节](#_95)
  + [测试屏幕刷新率](#_102)
  + [注意](#_107)
  + [结语](#_112)

有一说一，Windows自带的远程桌面服务(RDP)非常优秀，不考虑云服务（可以自己搭建）的情况下，在表现上可以胜过任意一款第三方远程控制软件（包括且不限于VNC、Teamviwer……），毕竟是原生功能。

RDP本身是可以无显卡运行的，显示远程桌面的时候并不调用显卡，可以做一些基本的管理操作。最近研究了一下怎样将提升RDP的性能，开启显卡加速（OpenGL，DX支持），提高传输帧率（默认30fps，设置为60fps），以及USB设备重定向（将客户端的USB设备挂载到远程主机，不需要USB Network Gateway）

## 显卡加速

首先打开远程主机上的组策略（Win+R打开运行，输入`gpedit.msc`）

依次找到计算机配置->管理模板->Windows组件->远程桌面服务->远程桌面会话主机->远程会话环境

在右边选择**将硬件图形适配器应用于所有远程桌面服务会话**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200827003633866.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NzZG5fbGlmZTE4,size_16,color_FFFFFF,t_70#pic_center)

文章来源: https://blog.csdn.net/csdn\_life18/article/details/108250846
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)