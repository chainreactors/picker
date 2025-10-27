---
title: 亚马逊 AWS Cloudfront CDN 使用教程
url: https://buaq.net/go-166073.html
source: unSafe.sh - 不安全
date: 2023-05-29
fetch_date: 2025-10-04T11:36:59.202066
---

# 亚马逊 AWS Cloudfront CDN 使用教程

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

![](https://8aqnet.cdn.bcebos.com/ba0d0a2b1e240d9876c447488da0cfc6.jpg)

亚马逊 AWS Cloudfront CDN 使用教程

Amazon CloudfrontCloudfront 是 Amazon 提供的 CDN 服务，有每月免费 1T 的流量，该流量不可累计。个人小站的话，
*2023-5-28 13:22:0
Author: [blog.upx8.com(查看原文)](/jump-166073.htm)
阅读量:35
收藏*

---

## Amazon Cloudfront

Cloudfront 是 Amazon 提供的 CDN 服务，有每月免费 1T 的流量，该流量不可累计。个人小站的话，这个 CDN 是足够用的了，而且主要是国内访问的速度还不错。但是需要注意不要被攻击了，不然 AWS 的扣费还是很贵的。

<https://aws.amazon.com/cn/cloudfront/>

## 解析域名

首先先解析个三级域名到你的需要加 CDN 的网站的 VPS IP 上，比如

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/photo_2022-10-28_15-50-23.jpg)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/photo_2022-10-28_15-50-23.jpg)

这里的 8.8.8.8 就是你的 VPS IP。这里的 cdn 就是你的三级域名前缀，这个域名是看不到的，这是回源域名用的。用户访问的是后面 Cloudfront 生成的域名地址或者是自己加的 CNAME 域名地址。

## 创建账号

前往 <https://aws.amazon.com/cn/cloudfront/> 注册个账号，并且绑定个信用卡，建议绑定小额的或者限额，否则扣起费来吃不消。

创建个 Distributions

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_15-54-24.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_15-54-24.png)

然后填入你刚刚解析的那个回源域名，比如刚刚解析的 cdn.ednovas.blog

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_15-55-04.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_15-55-04.png)

Protocol 一般选择 https only 保证 TLS。不过如果不清楚的话，可以选择 Match viewer。

然后此页面其他全部默认就行

如果有 TLS 的 https，还是建议开启 https 强跳。

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_15-58-07.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_15-58-07.png)

下面这里 Price class 选择默认即可，或者按需选择

下面的 HTTP versions 可以把 HTTP/3 也勾选上

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_15-58-22.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_15-58-22.png)

如果不想用 cloudfront 默认的奇怪的长长的三级域名的话，这里可以加个 CNAME，当然还需要用 AWS 自己的证书才行。

CNAME 这里输入你想让用户访问用的 CNAME 域名，比如 user.ednovas.blog，用户访问这个地址就会访问你加了 CDN 的网站了。

然后如果要用 CNAME 的话，必须使用 AWS 的证书才可以，需要点下面的 request certicificate 来获取一个证书

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-01-14.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-01-14.png)

直接选择 Next 即可

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-04-24.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-04-24.png)

然后输入你要加证书的域名，然后选择默认的 DNS 验证即可。

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-04-52.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-04-52.png)

点进去

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-05-42.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-05-42.png)

然后在域名中解析对应的 CNAME 名字和值

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-06-02.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-06-02.png)

记得把小云朵关上

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-06-56.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-06-56.png)

然后过几分钟就可以验证成功申请下来了

然后在 CDN 的页面，选择刚刚申请的这个证书（如果一直没有，可以先保存当前的 CDN 设置，然后再点击 Edit 编辑加上这个 CNAME 和证书）

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-08-09.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-08-09.png)

需要等待生效的时间比较久，可能需要几十分钟

然后访问 CNAME 地址就可以了！

## 添加限制

然后在 Distributions 中，还可以设置其他的一些 Behaviors，Error pages，Geopraphic restrictions 等，这里以 Geopraphic restrictions 为例，屏蔽除了中国以外的所有用户访问

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-10-21.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-10-21.png)

Allow list 仅选择国内然后保存，等待几分钟生效即可。

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-11-36.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-11-36.png)

## 效果

用 ping.pe 测试 CDN 的效果还可以

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-12-36.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-12-36.png)

## 开启费用提醒

右上角账户这里选择 billing

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-13-31.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-13-31.png)

可以把这几个全都打开，然后设置提醒免费资源用尽提醒邮箱

[![](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-14-21.png)](https://cdn.jsdelivr.net/gh/wdm1732418365/CDN/New%20folder/Snipaste_2022-10-28_16-14-21.png)

PS：如果aws找的是代付的账号的是没有主账号权限的，设置不了

文章来源: https://blog.upx8.com/3594
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)