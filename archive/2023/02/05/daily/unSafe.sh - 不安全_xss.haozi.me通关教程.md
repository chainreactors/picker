---
title: xss.haozi.me通关教程
url: https://buaq.net/go-147952.html
source: unSafe.sh - 不安全
date: 2023-02-05
fetch_date: 2025-10-04T05:45:02.643397
---

# xss.haozi.me通关教程

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

![](https://8aqnet.cdn.bcebos.com/c77dedfb957537d37613020e838809fe.jpg)

xss.haozi.me通关教程

0x00首先整体浏览网站分别是xss注入点，注入后的HTML代码以及网页源码构造常规payload：<script>alert(1)</script>成
*2023-2-4 15:45:0
Author: [xz.aliyun.com(查看原文)](/jump-147952.htm)
阅读量:32
收藏*

---

## **0x00**

首先整体浏览网站

![](https://img-blog.csdnimg.cn/aa795087993d4172831c9e99ee276446.png)

分别是xss注入点，注入后的HTML代码以及网页源码

构造常规payload：

`<script>alert(1)</script>`

成功通关

![](https://img-blog.csdnimg.cn/51bbe92737da4211b6bc1a4a2579b86b.png)

## **0x01**

看到注入点是在<textarea></textarea>标签中, 所以用上一题的方法是不会被解析的, 故需要去构造标签, 闭合<textarea></textarea>, 就可以注入了:

`</textarea><script>alert(1)</script><textarea>`

成功通关

![](https://img-blog.csdnimg.cn/40e66026bf2545129d9b7b3e4c84718a.png)

或者, 利用error事件也可以:

这个img，是用来给页面加入图片的，图片的地址就是由src来设置的，然后后面那个onerror是一个事件，就是一旦出错，就会执行里面的JavaScript代码。所以我们就把图片的地址随便写一个，然后程序出错，最后执行JavaScript代码。

```
</textarea><img src="x" onerror="alert(1)"><textarea>
```

成功通关

![](https://img-blog.csdnimg.cn/ec2f336f020d4be3ae2bba5e39abbfc4.png)

## **0x02**

输入常规payload：

`<script>alert(1)</script>`

我们发现这题的注入点是把值转化为字符串, 然后显示在输入框内, 这样前两题的标签闭合注入也就失效了

![](https://img-blog.csdnimg.cn/86cc2b6b5d7c43928cef16efa5712cb1.png)

可以借鉴sql注入的方法, 将前面的双引号闭合, 然后注入新的标签，上一关是闭合整个标签，这次就闭合一半，使用">把前面的标签给闭合了，然后再写自己的标签:

```
"><img src="x" onerror="alert(1)">
```

成功通关

![](https://img-blog.csdnimg.cn/e46abfb06acf464eb143a16ab226c34e.png)

## **0x03**

审查源码我们发现，括号, 方括号都被过滤了:

![](https://img-blog.csdnimg.cn/f924beb91b1548db9adcfeea58c1e9e1.png)

可以用 `` 来代替进行绕过:

`<script>alert`1`</script>`

成功通关

![](https://img-blog.csdnimg.cn/e1f9deb877dc49e494b973b62aed161a.png)

## **0x04**

审查源码我们发现，这题把括号、正括号和引号都过滤了:

![](https://img-blog.csdnimg.cn/db378bad282441438b5893a0464840a1.png)

可以考虑用html编码来绕过, 将(1)进行html编码:

![](https://img-blog.csdnimg.cn/e3c8a0f1db4e4e799770f031b50afff2.png)

构造payload：

```
<img src="" onerror=alert(1)>
```

成功通关

![](https://img-blog.csdnimg.cn/a08ee957627b444d8febb442ef0a75de.png)

## **0x05**

此题的注入点处于注释符之间, 而注释符的后半部被替换为一个

文章来源: https://xz.aliyun.com/t/12107
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)