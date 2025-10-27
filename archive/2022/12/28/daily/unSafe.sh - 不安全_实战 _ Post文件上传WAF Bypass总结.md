---
title: 实战 | Post文件上传WAF Bypass总结
url: https://buaq.net/go-141568.html
source: unSafe.sh - 不安全
date: 2022-12-28
fetch_date: 2025-10-04T02:34:55.141679
---

# 实战 | Post文件上传WAF Bypass总结

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

实战 | Post文件上传WAF Bypass总结

本文介绍的思路主要围绕针对于 POST 参数的 multipart/form-data 进行讨论。multipart/form-data 是为了解决上传文件场景下文件内容较大且内置字符不可控的问
*2022-12-27 15:54:21
Author: [www.secpulse.com(查看原文)](/jump-141568.htm)
阅读量:37
收藏*

---

本文介绍的思路主要围绕针对于 POST 参数的 `multipart/form-data` 进行讨论。

`multipart/form-data` 是为了解决上传文件场景下文件内容较大且内置字符不可控的问题。在最初的 http 协议中，并没有上传文件方面的功能。RFC1867 为 HTTP 协议添加了这个能力。常见的浏览器都已经支持。按照此规范将用户指定的文件发送到服务器，可以按照此规范解析出用户发送来的文件。

HTTP 传输的内容通过 boundary 进行了分割，以 `--boundary` 开始，并以 `--boundary--` 结尾。

multipart/form-data 格式也是可以传递 POST 参数的。对于 Nginx + PHP 的架构，Nginx 实际上是不负责解析 multipart/form-data 的 body 部分的，而是交由 PHP 来解析，因此 WAF 所获取的内容就很有可能与后端的 PHP 发生不一致。

通过一个简单的脚本来验证上面的说法。

```
<?php
echo file_get_contents("php://input");
echo '$_POST Contentn';
echo '';
var_dump($_POST);
echo '$_FILES Contentn';
echo '';
var_dump($_FILES);
?>
```

正常情况下使用 multipart/form-data POST 传输一个参数 `f`，其值为 `1`：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125302.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041521288.png-water_print")

上面说到，multipart/form-data 用来解决传输文件的问题，那什么情况是上传文件？什么情况是 POST 参数呢？关键点在于有没有一个完整的 `filename=`，这 9 个字符缺一不可。加上了 `filename=` 以后的回显：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125303.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041524972.png-water_print")

由于一些 WAF 产品对用户上传文件的内容不做匹配，直接放行。因此，关键问题在于，WAF 能否准确有效识别出哪些内容是传给 POST 数组的，哪些传给 FILES 数组？如果不能，那就可以想办法让 WAF 以为我们是在上传文件，而实际上却是在 POST 一个参数，这个参数可以是命令注入、SQL 注入、SSRF 等任意的一种攻击，这样就实现了通用型的Waf Bypass。

## **Bypass 思路 - 初级**

### **0x00 截断**

在 filename 之前加入了 0x00 (%00 url decode)，有些 WAF 在检测前会对 HTTP 协议中的 0x00 进行过滤， 这样就导致了 WAF 认为是含有 filename 的普通上传，而后端 PHP 则认为是 POST 参数。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-16721253031.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041534841.png-water_print")

### **文件描述双写混淆**

双写 `Content-Disposition`，一些 WAF 会取第二行，而实际 PHP 会获取第一行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125304.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041535090.png-water_print")

另外针对 `Content-Disposition` 的双写混淆还有可以包括 `Content-Type`:

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125305.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041539002.png-water_print")

但是这种方式会将 `f` 变量中加入一些垃圾数据，在进行注入时需要进行闭合处理。

### **multipart 混淆**

通过构建一个新的 multipart 部分，是两个部分传递的参数名相同，达到混淆的目的。

**带有垃圾数据的情况**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-16721253051.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041542734.png-water_print")

**不带垃圾数据的情况**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125307.png)

### **Boundary 混淆**

#### **构造双重 boundary**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125308.png)

在 PHP 中，只识别到 `boundary=a`，即真正的 `boundary` 为 a。若 WAF 中识别到的 `boundary` 为 `b`，就会将第 13 行到第 18 行做为文件 `pic.png` 的内容进行传输，达到混淆的目的。

#### **构造双重 Content-Type**

这种混淆方式与上一种情况类似，只是将 `Content-Type` 进行混淆，指定不同的 boundary。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125310.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041551351.png-water_print")

#### **空白 boundary**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125311.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041557946.png-water_print")

在 PHP 中，只识别到 `boundary=空` 。若 WAF 中错将 `;` 识别到为 `boundary`，就会将第 13 行到第 18 行做为文件 `pic.png` 的内容进行传输，达到混淆的目的。

#### **空格 boundary**

同样的 boundary 也可以是空格

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125312.png)

#### **boundary 中的逗号**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125314.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041608384.png-water_print")

事实上，在 PHP 中会将 Boundary 中的逗号作为分隔符，即 boundary 遇到逗号就结束。

只标识一个逗号也可以：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125315.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041609039.png-water_print")

## **Bypass 思路 - 进阶**

### **0x00 截断进阶**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125317.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041625935.png-water_print")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125318.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041641335.png-water_print")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125319.png)

这三个位置都可以。将其替换为 0x00 和 0x20 与之同理。

此外，将 0x00 放到参数名中也可以绕过：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125326.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041649598.png-water_print")

### **Boundary 混淆进阶**

boundary 的名称是可以前后加入任意内容的，WAF 如果严格按 boundary 去取，就会出现混淆。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125327.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041654246.png-water_print")

在双写 Content-Type 的混淆中，将第一个 Content-Type 和冒号部分填入了空格，实现绕过。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125328.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203041701548.png-water_print")

Boundary 的取值混淆：

### **单双引号混合**

Content-Disposition 中的字段使用单引号、双引号进行混淆
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125330.jpeg)

### **urlencoded 与 multipart 混淆**

在 Content-Type 头中，分别指定为：`urlencoded` 与 `multipart`。实际上 PHP 识别到的为 `urlencoded`，若 WAF 识别到的为 multipart，就可以绕过检测。通过 & 来作为参数分隔符，截取参数 `sqlInjectionParam` 的前后部分，完整保留该参数。

由于 `multipart/form-data` 下的内容不进行 `urldecoded`， 一些 WAF 也正是这样设计的，这样做本没有问题，但是如果是 `urlencoded` 格式的内容，不进行 url 解码就会引入 `%0a` 这样字符，而这样的字符不解码是可以直接绕过防护规则的，从而导致了绕过。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125331.png)

## **Bypass 思路 - 高级**

此章节通过结合 PHP 源码来讨论 WAF Bypass 的可能性。

### **skip\_upload - 1**

在 PHP 源码中，处理 multipart 时存在这样一段代码：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125334.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203051556856.png-water_print")

其中的 param 就是 `name="f"`，当程序进入 `c < 0` 这个分支时，就会跳过当前 part 的上传流程。由于初始化时 `c = 0`，遇到 `[` 时，`c += 1`，遇到 `]` 时，`c -= 1`。因此，可以构造 `name="f]"`，即可让 `c = -1`。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125335.png)

### **skip\_upload - 2**

在 PHP 源码中，有这样一段代码：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194100-1672125339.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202203051608783.png-water_print")

当文件上传数量超出最大值后，会跳过当前 part 文件的处理。在 php 5.2.12 和以上的版本，有一个隐藏的文件上传限制是在 `php.ini` 里没有的，就是这个 `max_file_uploads` 的设定，该默认值是 20, 在 php 5.2.17 的版本中该值已不再隐藏。文 件上传限制最大默认设为 20，所以一次上传最大就是 20 个文档，所以超...