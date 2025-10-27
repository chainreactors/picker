---
title: 免费容器NorthFlank搭建V2教程
url: https://buaq.net/go-165394.html
source: unSafe.sh - 不安全
date: 2023-05-24
fetch_date: 2025-10-04T11:36:51.305386
---

# 免费容器NorthFlank搭建V2教程

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

![](https://8aqnet.cdn.bcebos.com/af3b67058f0c974a6c964b866a8c0839.jpg)

免费容器NorthFlank搭建V2教程

NorthFlank使用的是Google云服务器，速度方面还算可以，优势就是：需要绑定信用卡，可以过滤很多人，所以使用的人不太多。实际测试Youtube
*2023-5-23 23:2:50
Author: [blog.upx8.com(查看原文)](/jump-165394.htm)
阅读量:97
收藏*

---

NorthFlank使用的是Google云服务器，速度方面还算可以，优势就是：需要绑定信用卡，可以过滤很多人，所以使用的人不太多。

实际测试Youtube最高跑4万，勉强8K，当然不同的网络、不同的时段表现肯定不同，大家可以在视频下方进行反馈！

![未标题-1.jpg](https://iweec.com/usr/uploads/2023/05/1625864422.jpg "未标题-1.jpg")

Northflank 是一个云原生应用部署和管理平台，旨在简化开发人员和团队在云环境中部署、扩展和管理应用程序的过程。它提供了一套强大的工具和功能，帮助开发人员更轻松地构建、部署和运行应用。

免费用户需要绑定信用卡（部分虚拟卡可用），默认免费项目可以部署0.2 vCPU / 512MB的应用，而对于V2来说，可以部署2个Node。

本次部署的源码网址： <https://github.com/fscarmen2/V2-for-Koyeb> ，一看便知是写Koyeb的，不过Koyeb不仅需要绑卡，现在申请需要人工审批，很难申请到，操作方法一致，以后再给大家做Koyeb。

1、信用卡一张，最好是实体。

2、GitHub账号一个；

1、首先在 <https://app.northflank.com/login> 登陆账号，谷歌账号、github是可以直接登陆的。为了简单，我们就直接谷歌登陆吧。

2、然后就是输入用户名，同意协议就可以继续了；

3、当我们要激活默认项目的时候，需要绑定信用卡，自己绑定吧。

4、在 <https://github.com/fscarmen2/V2-for-Koyeb> 页面，Fork一下项目，别忘了给大佬点个赞。

5、在 northflank个人仪表盘中，点击Git，链接你的github账号，然后就在默认项目中创建新的服务。

6、Service name（随便写）；存储库就选择我们刚刚的；Branch 选择（main）type选择dockerfile 、端口选择：80，其他默认，开始构建；

7、构建完成，访问你的项目地址看到：Welcome to nginx，这里提一下，NorthFlank给到的是有root权限的ssh，用于联系Linux命令也非常不错（弱弱说一下，可以测试一下安装宝塔，我就不测试了）。
![截屏2023-05-22 21.47.23.png](https://iweec.com/usr/uploads/2023/05/1180657668.png "截屏2023-05-22 21.47.23.png")

8、客户端设置：
网址：你的项目地址
端口：443
UUID：de04add9-5c68-8bab-950c-08cd5320df18
PATH：/vmess 或者/vmess

1、在仪表盘中，可以添加域名：点击添加域名，然后输入你的域名；

2、按照提示进行TXT解析，然后添加cname，验证后即可绑定在项目上；

NorthFlank部署简单，而且暂时没有发现有流量限制，免费的东西可要珍惜了。

文章来源: https://blog.upx8.com/3584
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)