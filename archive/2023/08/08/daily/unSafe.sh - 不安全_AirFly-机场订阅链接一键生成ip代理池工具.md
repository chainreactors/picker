---
title: AirFly-机场订阅链接一键生成ip代理池工具
url: https://buaq.net/go-173872.html
source: unSafe.sh - 不安全
date: 2023-08-08
fetch_date: 2025-10-04T11:58:47.686607
---

# AirFly-机场订阅链接一键生成ip代理池工具

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

![](https://8aqnet.cdn.bcebos.com/514ae728ea3e2eecffc92845db07c4c6.jpg)

AirFly-机场订阅链接一键生成ip代理池工具

首页AirFly-机场订阅链接一键生成ip代理池工具
*2023-8-7 21:31:9
Author: [govuln.com(查看原文)](/jump-173872.htm)
阅读量:218
收藏*

---

* [首页](https://zgao.top)
* [AirFly-机场订阅链接一键生成ip代理池工具](https://zgao.top:443/airfly-%E6%9C%BA%E5%9C%BA%E8%AE%A2%E9%98%85%E9%93%BE%E6%8E%A5%E4%B8%80%E9%94%AE%E7%94%9F%E6%88%90ip%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7/)

### AirFly-机场订阅链接一键生成ip代理池工具

![](https://zgao.top/wp-content/uploads/2023/07/image-8-1024x460.png)

很早之前的一个想法，写一个工具支持各种主流的科学上网协议，通过指定订阅链接的就可以实现自动轮询代理ip，很适合爬虫，渗透，攻防的场景。

最近趁工作之余把这个工具写完了，我取名为 AirFLy（Air[port] Fly），意思是 让机场✈️起飞！

* [项目链接](#%E9%A1%B9%E7%9B%AE%E9%93%BE%E6%8E%A5 "项目链接")
* [工具参数](#%E5%B7%A5%E5%85%B7%E5%8F%82%E6%95%B0 "工具参数")
* [测试代理ip](#%E6%B5%8B%E8%AF%95%E4%BB%A3%E7%90%86ip "测试代理ip")

## 项目链接

<https://github.com/zgao264/AirFly>

## 工具参数

![](https://zgao.top/wp-content/uploads/2023/08/image-17-705x1024.png)

工具的使用非常简单，指定两个参数即可。

* -l 本地监听的端口，支持三种协议（http、socks5、mixed），mixed是指http和socks5共用一个端口。
* -u 机场的订阅链接 ，可以同时指定多个机场订阅链接。

![](https://zgao.top/wp-content/uploads/2023/07/image-9-1024x717.png)

## 测试代理ip

以curl为例：

```
curl -sx "http://127.0.0.1:6666" https://ip.tool.lu
```

连续请求测试：

```
seq 1 10 | xargs curl -sx "http://127.0.0.1:6666" https://ip.tool.lu
```

Post Views: 289

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 目前为止有一条评论

###### 卑微小王 发布于4:17 下午 - 8月 3, 2023

确实很实用

文章来源: https://govuln.com/news/url/6nx0
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)