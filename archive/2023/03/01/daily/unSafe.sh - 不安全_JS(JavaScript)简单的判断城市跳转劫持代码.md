---
title: JS(JavaScript)简单的判断城市跳转劫持代码
url: https://buaq.net/go-151413.html
source: unSafe.sh - 不安全
date: 2023-03-01
fetch_date: 2025-10-04T08:19:01.193519
---

# JS(JavaScript)简单的判断城市跳转劫持代码

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

![]()

JS(JavaScript)简单的判断城市跳转劫持代码

最近在工作中有一个需求根据不同的地区，跳转不同页面，考虑到PHP的效率问题最后使用js来实现，接下来编程为大家介绍一下js判断用户当前地区，有需要的小伙
*2023-2-28 22:4:0
Author: [blog.upx8.com(查看原文)](/jump-151413.htm)
阅读量:39
收藏*

---

最近在工作中有一个需求根据不同的地区，跳转不同页面，考虑到PHP的效率问题最后使用js来实现，接下来编程为大家介绍一下js判断用户当前地区，有需要的小伙伴可以参考一下：

### 1、IP获取代码：

```
    <script src="https://pv.sohu.com/cityjson?ie=utf8"></script>
```

### 2、souhu接口各项参数：

```
{
    "cip": "192.168.115.178",  //用户IP
    "cid": "CN",  // 英文缩写
    "cname": "CHINA"
}
```

### 3、根据地区显示跳转不同页面：

```
  var city = returnCitySN.cname; //获取城市信息
  //判断是否是上海，然后做不同的判断
  if (city.indexOf('上海') != -1) {
    window.location.href = '/1.html';
  }else{
    window.location.href = '/2.html';
  }
```

文章来源: https://blog.upx8.com/3247
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)