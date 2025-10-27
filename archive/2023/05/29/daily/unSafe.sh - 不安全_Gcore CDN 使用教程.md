---
title: Gcore CDN 使用教程
url: https://buaq.net/go-166082.html
source: unSafe.sh - 不安全
date: 2023-05-29
fetch_date: 2025-10-04T11:36:58.351985
---

# Gcore CDN 使用教程

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

![](https://8aqnet.cdn.bcebos.com/3869d326ae1df41727c7d688e10d06b1.jpg)

Gcore CDN 使用教程

Gcorelab CDN类似 AWS 的 Cloudfront CDN，提供每月 1T 的免费流量。效果不如 Cloudfront 但是也还不错http
*2023-5-28 13:27:6
Author: [blog.upx8.com(查看原文)](/jump-166082.htm)
阅读量:57
收藏*

---

## Gcorelab CDN

类似 AWS 的 Cloudfront CDN，提供每月 1T 的免费流量。效果不如 Cloudfront 但是也还不错

<https://cdn.gcore.com/>

## 注册账号

Gcore 地址

<https://cdn.gcore.com/>

Porkbun 购买域名（便宜）

[https://porkbun.com](https://porkbun.com/)

因为 Gcore 的 CDN 需要更改 Nameservers，所以比较建议买个新的域名然后专用 CDN

## 使用 CDN

输入要加 CDN 的域名

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-32-18.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-32-18.png)

解析个根域名到你的网站所在的 VPS 的 IP（必须是跟域名）

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-33-41.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-33-41.png)

更改 nameserver 为 Gcore 的 nameservers

nameserver 生效需要等待比较久的时间，最长大概可能需要几小时，快的话几分钟。

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-35-03.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-35-03.png)

这几个全开就行

这个选择 http 和 https

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-39-39.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-39-39.png)

可以把 Browser caching 开启

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-40-20.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-40-20.png)

并开启 https 强跳

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-40-49.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-40-49.png)

然后允许 SSL 证书，他就会给该根域名自动申请一个证书

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_23-50-42.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_23-50-42.png)

然后保存就行了。

## 修改回源地址

回到主页面，选择 Origins groups，

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_23-51-45.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_23-51-45.png)

修改为你需要加 CDN 的地址，注意这个回源地址不能开 CDN，要直接解析到那个 VPS 网站的 IP。

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_23-52-48.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_23-52-48.png)

等待一段时间生效即可。

## 流量

注意每月免费流量只有 1T。

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_23-55-24.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_23-55-24.png)

文章来源: https://blog.upx8.com/3595
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)