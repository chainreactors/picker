---
title: timwhitez starred Taichi
url: https://buaq.net/go-145785.html
source: unSafe.sh - 不安全
date: 2023-01-17
fetch_date: 2025-10-04T04:02:08.337921
---

# timwhitez starred Taichi

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

![](https://8aqnet.cdn.bcebos.com/c1ffeef6cece65e663ca19f961c968da.jpg)

timwhitez starred Taichi

簡介基於go語言實現的高交互滲透測試框架，已實現如下功能：1、"RDP","JAVADEBUG","REDIS", "FTP", "SNMP", "POSTGRESQL
*2023-1-16 19:15:13
Author: [github.com(查看原文)](/jump-145785.htm)
阅读量:36
收藏*

---

## 簡介

基於go語言實現的高交互滲透測試框架，已實現如下功能：

## 編譯運行

1、安裝第三方庫（命令：go get xxx）
2、go run main.go
3、編譯
go build

## 基本使用

1.加載模塊
load <模塊> <協議>
e.g:
load portscan
load burt ftp
2.設置參數
set ip/file xxx
3.展示參數
show
4.運行
go

## 端口掃描

1.load portscan
2.set ip 127.0.0.1
可設置文件 set file xxx.txt
c段 set ip 192.168.1.1-255
3.go

## 敏感路径扫描（需要本地有urldic.txt）

1.load urlscan
2.set ip/domain xxx
3.go

## 子域名扫描（需要本地有subdic.txt）

1.load subscan
2.set domain <http://xxx.cn>
3.go

## url存活扫描

[![TAICHI](https://github.com/sulab999/Taichi/raw/main/test/livescan.png)](https://github.com/sulab999/Taichi/blob/main/test/livescan.png)
1.load urlscan live
2.set file url.txt
3.go

## poc功能

本地创建taichi-pocs文件夹，用于存放yml文件
1.poc
2.init（首次使用或新增poc時）
3.show
4.use xxx 或set xxx（poc）
5.set ip/url xxx
6.go
扫描结束后，生成的报告在reports文件夹中

## 更新：

後期更新見realse
v0.1
1、已實現端口掃描和爆破模塊

## 来元世界交流一下啊

[![TAICHI](https://github.com/sulab999/Taichi/raw/main/nworld.jpg)](https://github.com/sulab999/Taichi/blob/main/nworld.jpg)
[![TAICHI](https://github.com/sulab999/Taichi/raw/main/webchat.png)](https://github.com/sulab999/Taichi/blob/main/webchat.png)

该程序及其相关技术仅用于安全自查检测。

由于传播、利用此程序所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。

本人拥有对此程序的修改和解释权。未经网络安全部门及相关部门允许，不得善自使用本程序进行任何攻击活动，不得以任何方式将其用于商业目的。

下載地址：<https://github.com/sulab999/Taichi/releases/tag/v0.4>

文章来源: https://github.com/sulab999/Taichi
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)