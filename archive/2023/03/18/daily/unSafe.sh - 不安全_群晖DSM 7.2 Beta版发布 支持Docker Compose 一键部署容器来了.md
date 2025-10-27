---
title: 群晖DSM 7.2 Beta版发布 支持Docker Compose 一键部署容器来了
url: https://buaq.net/go-153973.html
source: unSafe.sh - 不安全
date: 2023-03-18
fetch_date: 2025-10-04T09:56:27.560374
---

# 群晖DSM 7.2 Beta版发布 支持Docker Compose 一键部署容器来了

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

![](https://8aqnet.cdn.bcebos.com/6cda1a49fca1d808ee7f3b496ce03bba.jpg)

群晖DSM 7.2 Beta版发布 支持Docker Compose 一键部署容器来了

群晖中国官方公众号今天宣布了 DSM 7.2 Beta 版更新，这也是目前 DSM 7.2 系列的第三个大公测版本，带来部分功能改进。不过相较于消费者端的改进，DSM 7.2 其中重点
*2023-3-17 22:58:52
Author: [www.landiannews.com(查看原文)](/jump-153973.htm)
阅读量:37
收藏*

---

群晖中国官方公众号今天宣布了 DSM 7.2 Beta 版更新，这也是目前 DSM 7.2 系列的第三个大公测版本，带来部分功能改进。

不过相较于消费者端的改进，DSM 7.2 其中重点是面向企业的性能和效率，这些改进是通过套件获得的，例如 Hyper Backup 对块级全系统备份的支持可以显著加快大量数据的备份速度，不过这些还在测试，Beta 版中也无法使用。

[![群晖DSM 7.2 Beta版发布 不过建议用户谨慎使用测试版](https://img.lancdn.com/landian/2023/03/97887.png)](https://img.lancdn.com/landian/2023/03/97887.png)

另一个显著的改进是随着技术的发展，NVMe SSD 已经不再单纯的作为缓存盘使用，毕竟现在 NVMe SSD 价格已经非常低且容量越来越大，所以 DSM 7.2 支持将 NVMe SSD 作为存储空间，不再限制只能作为存储盘。

要使用 NVMe 存储空间首先需要 NAS 支持 NVMe SSD，所以只有近年来的新机型支持，SSD 组建的存储空间可以大幅度提升读写性能，对专业用户来说是个好消息。

**DSM 7.2 Beta 版最新更新日志如下：**

* 新增以下机型 NVMe 存储空间支持：DS1522+、DS1621+、DS1821+、DS1621xs+，特别说明：**使用此功能需使用兼容的群晖 SNY3400/3500 NVMe SSD**，目测现在还不支持其他品牌的 NVMe SSD。
* Docker 套件更名为 Container Manager (容器管理)，升级 UI 以便于更新和清理容器
* 容器管理套件新增支持 Docker Compose，可以通过配置文件一键部署容器
* 以下机型新增支持容器管理：DS420J、DS223、DS423
* Synology Photos 新增支持 WebP 格式的图像
* Synology Photos 新增支持安卓动态照片（Motion Photos）

**普通用户不要使用测试版：**

测试版的目的就是测试，要测试是因为还不够稳定还存在 BUG，蓝点网的 DS916 + 就曾在某年更新测试版时翻车，所幸还在保修期内，寄给群晖无法修复，换了一台新机器，虽然数据没丢但当时转移数据也花了很大的功夫。

因此如果你只有一台 NAS 且作为主力服务器存储个人数据，还是不要安装 Beta 版吧。

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/97887.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/97887.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)