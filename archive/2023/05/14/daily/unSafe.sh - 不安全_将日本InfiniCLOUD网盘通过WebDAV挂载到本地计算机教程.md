---
title: 将日本InfiniCLOUD网盘通过WebDAV挂载到本地计算机教程
url: https://buaq.net/go-163191.html
source: unSafe.sh - 不安全
date: 2023-05-14
fetch_date: 2025-10-04T11:37:48.052470
---

# 将日本InfiniCLOUD网盘通过WebDAV挂载到本地计算机教程

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

![](https://8aqnet.cdn.bcebos.com/38eb7353c94a3b1763e85de299decfe2.jpg)

将日本InfiniCLOUD网盘通过WebDAV挂载到本地计算机教程

日本的InfiniCLOUD网盘迎来了6岁生日的活动：可免费注册享100M速度的网盘。虽然简单的写了下将InfiniCLOUD网盘通过WebDAV挂载到
*2023-5-13 16:16:22
Author: [blog.upx8.com(查看原文)](/jump-163191.htm)
阅读量:62
收藏*

---

日本的InfiniCLOUD网盘迎来了6岁生日的活动：可免费注册享100M速度的网盘。虽然简单的写了下将InfiniCLOUD网盘通过WebDAV挂载到本地计算机，但是有很多人不知道具体操作。今天就来写一下这个具体操作过程！还没有注册的小伙伴可以移步：

## 准备软件工具

* RaiDrive 软件
* InfiniCLOUD 网盘的 WebDAV 连接 URL （可在[`我的页面`](https://teracloud.jp/ja/modules/mypage/usage/)查看）

首先 InfiniCLOUD 网盘的 WebDAV 连接 URL 地址是通用的，均为：https://kita.InfiniCLOUD.jp/dav/

那么根据 RaiDrive 这个软件顺序（如下图箭头所示）就是点击`Add`→设置`盘符和名称`→设置`WebDAV URL`地址→输入`账号密码`→点击`OK`即可。

**缙哥哥温馨提醒：**需要注意的是，`WebDAV URL` 地址要根据 RaiDrive 这个软件分离，将`dav`放在第二行，因为对于该网盘来说，dav属于二级目录，而 RaiDrive 软件的第一行是输入主域名。很多小伙伴就是这里设置错误导致无法挂载到本地。

![](https://pic4.58cdn.com.cn/nowater/webim/big/n_v2e920818e00fa4c65bf2c877e5f6fe7ca.png)

设置完成后会自动跳出其对应的资源管理器，同时你可以在我的电脑（计算机）根目录的网络位置看到名为InfiniCLOUD的盘。

![](https://pic2.58cdn.com.cn/nowater/webim/big/n_v259c894673f334cffa450d00836ee8e2f.png)

OK，这样就已经成功挂在到自己的计算机当中了，是不是很简单呢！

文章来源: https://blog.upx8.com/3554
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)