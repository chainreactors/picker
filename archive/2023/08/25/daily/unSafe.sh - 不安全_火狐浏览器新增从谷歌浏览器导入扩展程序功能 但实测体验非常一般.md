---
title: 火狐浏览器新增从谷歌浏览器导入扩展程序功能 但实测体验非常一般
url: https://buaq.net/go-175318.html
source: unSafe.sh - 不安全
date: 2023-08-25
fetch_date: 2025-10-04T11:59:26.659199
---

# 火狐浏览器新增从谷歌浏览器导入扩展程序功能 但实测体验非常一般

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

![](https://8aqnet.cdn.bcebos.com/a90841e258b5c6788b48010de6ca2e15.jpg)

火狐浏览器新增从谷歌浏览器导入扩展程序功能 但实测体验非常一般

德国科技博客GHACKS日前发现火狐浏览器最新稳定版已经支持从谷歌等浏览器里导入已经安装的扩展程序。该功能没有默认启用说明还在测试，当然没默认启用也是有原因的，蓝点网测试后发现这个功能
*2023-8-24 23:31:13
Author: [www.landiannews.com(查看原文)](/jump-175318.htm)
阅读量:19
收藏*

---

德国科技博客[GHACKS](https://www.ghacks.net/)日前发现火狐浏览器最新稳定版已经支持从谷歌等浏览器里导入已经安装的扩展程序。

该功能没有默认启用说明还在测试，当然没默认启用也是有原因的，蓝点网测试后发现这个功能体验很一般。

原因在于并非所有扩展程序都同时支持谷歌和火狐浏览器，所以火狐靠着人工匹配常用扩展实现导入和下载。

而且这里的导入并非直接从谷歌浏览器获得扩展文件，而是识别这个扩展是什么然后从火狐商店里自动安装。

**以下是启用方法和原理：**

启用方法：在火狐地址栏输入 about:config 然后搜索 browser.migrate.chrome.extensions.enabled 选项。

点击后面的切换按钮将这个实验性选项由false修改为true，然后重新启动火狐并转到设置、常规、导入数据。

选择谷歌或其他浏览器然后勾选扩展进行导入即可，选择后火狐浏览器开始导入进程，这个过程要一定时间。

功能原理：火狐浏览器检测用户安装的扩展，然后去火狐商店里匹配，如果匹配到就自动从火狐商店里安装。

问题在于不同商店扩展名称、开发者可能都不同，所以火狐靠着人工对部分常用扩展进行匹配，支持数量少。

蓝点网测试发现谷歌浏览器安装12个扩展程序，去掉重复的，最后只有篡改猴成功安装，多数没有成功导入。

**下面是操作配图：**

[![火狐浏览器新增从谷歌浏览器导入扩展程序功能 但实测体验非常一般](https://img.lancdn.com/landian/2023/08/99929-1.png)](https://img.lancdn.com/landian/2023/08/99929-1.png)

[![火狐浏览器新增从谷歌浏览器导入扩展程序功能 但实测体验非常一般](https://img.lancdn.com/landian/2023/08/99929-2.png)](https://img.lancdn.com/landian/2023/08/99929-2.png)

[![火狐浏览器新增从谷歌浏览器导入扩展程序功能 但实测体验非常一般](https://img.lancdn.com/landian/2023/08/99929-3.png)](https://img.lancdn.com/landian/2023/08/99929-3.png)

[![火狐浏览器新增从谷歌浏览器导入扩展程序功能 但实测体验非常一般](https://img.lancdn.com/landian/2023/08/99929-4.png)](https://img.lancdn.com/landian/2023/08/99929-4.png)

[![火狐浏览器新增从谷歌浏览器导入扩展程序功能 但实测体验非常一般](https://img.lancdn.com/landian/2023/08/99929-5.png)](https://img.lancdn.com/landian/2023/08/99929-5.png)

[![火狐浏览器新增从谷歌浏览器导入扩展程序功能 但实测体验非常一般](https://img.lancdn.com/landian/2023/08/99929-6.png)](https://img.lancdn.com/landian/2023/08/99929-6.png)

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/99929.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/99929.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)