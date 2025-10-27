---
title: 用 Myurls 轻松部署个短链接网站
url: https://buaq.net/go-263255.html
source: unSafe.sh - 不安全
date: 2024-09-22
fetch_date: 2025-10-06T18:20:34.817603
---

# 用 Myurls 轻松部署个短链接网站

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

![](https://8aqnet.cdn.bcebos.com/bcf73b1db1281b93d17ae7b2bb739357.jpg)

用 Myurls 轻松部署个短链接网站

介绍：Myurls 是一个开源的短链接项目，基于 Go 1.20 与 Redis 实现，轻松部署。效果图：部署方法：第一步：更新源Ubuntu/Debi
*2024-9-21 17:52:2
Author: [www.upx8.com(查看原文)](/jump-263255.htm)
阅读量:20
收藏*

---

## 介绍：

Myurls 是一个开源的短链接项目，基于 Go 1.20 与 Redis 实现，轻松部署。

## 效果图：

![](https://pic.imgdb.cn/item/64d3b1ea1ddac507ccd2c514.jpg)

## 部署方法：

### 第一步：更新源

**Ubuntu/Debian：**

**Centos：**

### 第二步：安装并配置Docker

安装Docker：

启动Docker：

设置Docker在开机时自动启动：

### 第三步：安装Docker compose

### 第四步：下载docker-compose.yml

1. 新建目录：
2. 下载docker-compose.yml：
3. 修改其中内容：

   修改`MYURLS_DOMAIN`为你的域名
4. 保存并退出：
   使用 Ctrl+X/Command+X

   ### 第五步：安装并运行 myurls 容器

   部署完成后可以访问 `http://<your-ip>:8002`（修改端口号为自己填入的端口） 来访问"myurls"

   ### 第六步：反向代理到域名

   此处使用一种非常简单的方式：Cloud flare 提供的 Origin Rules
   配置如下：
   ![](https://pic.imgdb.cn/item/64d257d91ddac507ccc556f4.jpg)
   修改Field为Hostname，Value为选择的完整域名，Rewrite to 刚才在左侧填写的端口
   ![](https://pic.imgdb.cn/item/64d2582e1ddac507ccc6419d.jpg)
   记得解析自己的子域名到服务器IP：
   使用A记录，Name为域名前缀，Content为服务器地址
   ![](https://pic.imgdb.cn/item/64d2585d1ddac507ccc6c0c5.jpg)

   ## 相关地址：

   GitHub地址：<https://github.com/stilleshan/dockerfiles/tree/main/myurls>
   Demo：[https://s.ops.ci](https://s.ops.ci/)

文章来源: https://www.upx8.com/4345
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)