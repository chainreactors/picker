---
title: Windows VPS DD重装为 Linux 一键脚本
url: https://buaq.net/go-148964.html
source: unSafe.sh - 不安全
date: 2023-02-12
fetch_date: 2025-10-04T06:25:27.259056
---

# Windows VPS DD重装为 Linux 一键脚本

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

![](https://8aqnet.cdn.bcebos.com/aa39fe714bdd85f7f5cde9de87788228.jpg)

Windows VPS DD重装为 Linux 一键脚本

最后编辑时间: 2023-02-11（New Article）
*2023-2-11 17:0:0
Author: [blog.upx8.com(查看原文)](/jump-148964.htm)
阅读量:25
收藏*

---

最后编辑时间: 2023-02-11（New Article）

![](https://sunpma.com/usr/uploads/2021/06/2597889658.jpg)

**适用于将`Windows VPS`重装为`Linux`系统，无需`VNC`和`DHCP`支持；**

需要用到的三个文件`win32loader.bat` `initrd.img` `vmlinuz`
下载地址：

**下载地址：<https://sunpma.lanzoui.com/iPo2xq07ycj>**

将下载的三个文件上传到Windows服务器；
右键以管理员身份运行`win32loader.bat`文件；
然后根据提示输入`2`选择`[2] Local file`使用本地文件；
出现提示后将`initrd.img`和`vmlinuz`两个文件移动至`C:\win32-loader\`目录后继续回车确认；
再次回车确认就开始重装系统为Linux；
**预览**
[![](https://sunpma.com/usr/uploads/2021/06/673566456.png)](https://sunpma.com/usr/uploads/2021/06/673566456.png)
**说明：默认安装系统为Debian9；用户名：`root`密码：`MoeClub.org`**
**成功安装`Debian9`后就可以用网络重装脚本重新安装其它系统了；**
**Debian/Ubuntu/CentOS 网络重装一键脚本：<https://blog.upx8.com/3035>**

脚本来源：[https://moeclub.org](https://moeclub.org/)

文章来源: https://blog.upx8.com/3215
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)