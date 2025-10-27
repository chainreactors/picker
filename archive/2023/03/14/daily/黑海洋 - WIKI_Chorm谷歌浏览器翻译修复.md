---
title: Chorm谷歌浏览器翻译修复
url: https://blog.upx8.com/3270
source: 黑海洋 - WIKI
date: 2023-03-14
fetch_date: 2025-10-04T09:30:37.764044
---

# Chorm谷歌浏览器翻译修复

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Chorm谷歌浏览器翻译修复

发布时间:
2023-03-13

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
19511

众所周知谷歌在2022年底宣布谷歌翻译退出中国市场，原因竟然是由于“使用率低”！退出中国后，很多用Chrome浏览器的小伙伴发现自带翻译已经无法使用，今天就给大家分享一个小工具来解决修复这个问题！

其原理就是ping IP，基本上都是**自动获取可用的IP，并且选择一个最低延迟的IP，修改HOST，然后一键修复Google翻译功。**

使用说明：

1、解压后打开主程序，管理员运行，等待软件测试结束后，出现下图提示，输入Y按回车即可，然后重启Chrome内核浏览器即可使用；
2、软件自动设置与自己延迟最低的服务器IP地址，无需手动选择

3、命令行输入Y就可以设置到hosts文件里，但是，自动设置到hosts可能被安全软件拦截，所以，最好还是手动添加到hosts文件里面。不过，要是按照地址去逐层找hosts文件比较费时，这里我们分享一个hosts文件编辑器，一键即可定位hosts文件，然后将刚才测试出的延迟最低IP复制粘贴到里面就可以。

4、最后，可用测试一下翻译接口是否正常。正常的话，本机所有使用Google翻译的功能，将恢复使用。Google浏览器翻译功能英语-中文演示

360极速浏览器Google翻译功能演示，英语-中文简体

## 软件原理

原理很简单，通过修改Google翻译指向IP，达到访问正常。

![](https://i2.100024.xyz/2023/02/01/ytb82v.webp)

## 特别说明

**软件非常有可能会被杀毒干掉，请关闭或者信任以后使用。**

GitHub项目地址：

[https://github.com/Ponderfly/GoogleTranslateIpCheck](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1BvbmRlcmZseS9Hb29nbGVUcmFuc2xhdGVJcENoZWNr)

ip来源

[https://github.com/Ponderfly/GoogleTranslateIpCheck/blob/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/ip.txt](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1BvbmRlcmZseS9Hb29nbGVUcmFuc2xhdGVJcENoZWNrL2Jsb2IvbWFzdGVyL3NyYy9Hb29nbGVUcmFuc2xhdGVJcENoZWNrL0dvb2dsZVRyYW5zbGF0ZUlwQ2hlY2svaXAudHh0)

原理

对ip列表逐个ping，取响应时间最小的，作为最佳ip。
将ip地址和translate.googleapis.com拼接，复制到剪贴板，方便**手动**写入到Hosts文件（C:\Windows\System32\drivers\etc\hosts）里面。
只提供设置参考，不能直接帮你设置hosts文件，懒得写！
与IP来源提供的软件相比，唯一优势就是，快!一般10秒内出结果。

GitHub项目地址：

[https://github.com/thedaviddelta/lingva-translate](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3RoZWRhdmlkZGVsdGEvbGluZ3ZhLXRyYW5zbGF0ZQ)

这是一个傻瓜式Google翻译修复程序，非常简单，双击运行即可
双击运行即可修复

![](https://i.postimg.cc/JhFz8whQ/image.png)

夸克下载地址：

https://pan.quark.cn/s/da4e3a01b844

UC下载地址：

https://fast.uc.cn/s/db150441034f4

## **GoogleTranslateIpCheck**

GoogleTranslateIpCheck是一款可以自动扫描国内可用的谷歌翻译IP小工具，以Windows系统为例。**右键管理员方式**，打开这款工具他便会自动筛选谷歌翻译延迟最低的IP，筛选后是输入`Y` 便可自动将IP地址设置到你的hosts文件中。然后你的谷歌翻译就可以使用了。

你也可以手动复制下面的IP地址，粘贴到你的你的hosts文件中，hosts文件地址：**`C:\Windows\System32\drivers\etc`**

**谷歌翻译IP地址筛选工具：[https://lanzoui.com/b06p2pexg](https://blog.upx8.com/go/aHR0cHM6Ly9sYW56b3VpLmNvbS9iMDZwMnBleGc)**

[取消回复](https://blog.upx8.com/3270#respond-post-3270)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")