---
title: Pikachu靶场-Unsafe Fileupload
url: https://buaq.net/go-144136.html
source: unSafe.sh - 不安全
date: 2023-01-05
fetch_date: 2025-10-04T03:03:39.786423
---

# Pikachu靶场-Unsafe Fileupload

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

![](https://8aqnet.cdn.bcebos.com/5396dc4b41c1cc0c0060ae1e94b3554d.jpg)

Pikachu靶场-Unsafe Fileupload

1.不安全的文件上传漏洞概述不安全的文件上传漏洞概述文件上传功能在web应用系统很常见，比如很多网站注册的时候需要上传头像、上传附件等等。当用户点击上传按钮后，
*2023-1-4 17:12:12
Author: [xz.aliyun.com(查看原文)](/jump-144136.htm)
阅读量:17
收藏*

---

## 1.不安全的文件上传漏洞概述

不安全的文件上传漏洞概述

文件上传功能在web应用系统很常见，比如很多网站注册的时候需要上传头像、上传附件等等。当用户点击上传按钮后，后台会对上传的文件进行判断 比如是否是指定的类型、后缀名、大小等等，然后将其按照设计的格式进行重命名后存储在指定的目录。 如果说后台对上传的文件没有进行任何的安全判断或者判断条件不够严谨，则攻击着可能会上传一些恶意的文件，比如一句话木马，从而导致后台服务器被webshell。

所以，在设计文件上传功能时，一定要对传进来的文件进行严格的安全考虑。比如：

--验证文件类型、后缀名、大小;

--验证文件的上传方式;

--对文件进行一定复杂的重命名;

--不要暴露文件上传后的路径;

--等等...

## 2.client check

查看源码

```
function checkFileExt(filename)
    {
        var flag = false; //状态
        var arr = ["jpg","png","gif"];
        //取出上传文件的扩展名
        var index = filename.lastIndexOf(".");
        var ext = filename.substr(index+1);
        //比较
        for(var i=0;i<arr.length;i++)
        {
            if(ext == arr[i])
            {
                flag = true; //一旦找到合适的，立即退出循环
                break;
            }
        }
        //条件判断
        if(!flag)
        {
            alert("上传的文件不符合要求，请重新选择！");
            location.reload(true);
        }
    }
```

分析，前端限制，可以通过禁用javascript绕过

上传php文件，显示不允许

![](https://img-blog.csdnimg.cn/b443cb70d08d40fe8bf3d925acdb1b90.png)

使用火狐浏览器，直接禁用javascript，到这个界面，点击取消

![](https://img-blog.csdnimg.cn/0a1fefb672c841208083a49c355a5ec7.png)

使用谷歌浏览器，同样禁用javascript，

![](https://img-blog.csdnimg.cn/2394b9fd22a74403b43fee746192f077.png)

点击上传，找到路径并访问

![](https://img-blog.csdnimg.cn/84ce751502ee471fb1af7e5ca1d15ed6.png)

<http://x.x.x.x/vul/unsafeupload/uploads/phpinfo.php>

![](https://img-blog.csdnimg.cn/a39298e86e234444a43443cde252c6b8.png)

## 3.MIME type

选择非图片的文件时, 不会拦截; 点击上传时, 服务器端检测到非图片格式, 就被拦截

![](https://img-blog.csdnimg.cn/380912b48c1e498ba269fa5df518028f.png)

MIME (Multipurpose Internet Mail Extensions）多用途互联网邮件扩展类型

MIME 是设定某种扩展名的文件用一种应用程序来打开的方式类型，当该扩展名文件被访问时，浏览器会自动使用指定应用程序来打开。多用于指定一些客户端自定义的文件名，以及一些媒体文件打开方式。

每个MIME类型由两部分组成，前面是数据的大类别，例如声音audio、图象image等，后面定义具体的种类。常见的 MIME 类型，比如：

超文本标记语言：.html，.html text.html

普通文件：.txt text/plain

RTF文件：.rtf application/rtf

GIF图形：.gif image/gif

JPEG图形：.jpeg，.jpg image/jpeg

查看源码， 定义了一个数组 并且调用了uploadfile函数

![](https://img-blog.csdnimg.cn/5267090ba4eb496aa8674f85f7ac9584.png)

上传1.jpg ,抓包查看type类型

![](https://img-blog.csdnimg.cn/7c419da2e7a44d6a97644c5f78819c58.png)

上传1.php ,抓包查看type类型

![](https://img-blog.csdnimg.cn/d9299a2300254b5f96f81c58dccb22f0.png)

修改phpinfo.php的type类型为image/jpeg

![](https://img-blog.csdnimg.cn/6ea56dc706b546ebb539dc0f23f3fae5.png)

上传成功

![](https://img-blog.csdnimg.cn/bfed626002344a42b18e1a2432d1500f.png)

![](https://img-blog.csdnimg.cn/6019630233744732b82b17ab084bc098.png)

## 4.getimagesize

getimagesize函数更是限制了上传文件的文件头必须为图像类型

修改文件的type类型不可用

第一种方法，可以通过添加jpg图片的格式头到脚本文件里进行绕过

首先在文本文档里写入<?php phpinfo();?>文件后缀修改为.jpg

![](https://img-blog.csdnimg.cn/f4105317764f49c6b190f9db5f6f7d99.png)

上传文件，抓包，在脚本文件前加上GIF89，放包

![](https://img-blog.csdnimg.cn/0e33e4eb0103438abc808ddeca04d5f0.png)

成功上传

![](https://img-blog.csdnimg.cn/152b02091b1c4735aec729afb82d4724.png)

第二种方法，在图片文件内容后添加<?php phpinfo();?>

命令行输入copy 1.png/b + phpinfo.php/a 2.png

![](https://img-blog.csdnimg.cn/6cc88267a7db461e886f77f42d29b149.png)

点击上传

![](https://img-blog.csdnimg.cn/50da9a46b6a04d21bf530027b37cff53.png)

文件上传成功

![](https://img-blog.csdnimg.cn/b07ad2e5c5c84297ba3c9073d4634771.png)

服务器会将木马文件解析成图片文件，因此向其发送执行该文件的请求时，服务器只会返回这个“图片”文件，并不会执行相应命令。

可以利用之前的文件包含漏洞，将图片格式的文件当做php文件来解析执行:

```
http://x.x.x.x/vul/fileinclude/fi_local.php?filename=../../unsafeupload/uploads/2020/10/20/5936185f8e5245666f2586884965.jpg&submit=%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2
```

![](https://img-blog.csdnimg.cn/97cafeeb06f740f0bd0d5566f1dd9795.png)

```
http://x.x.x.x/vul/fileinclude/fi_local.php?filename=../../unsafeupload/uploads/2020/10/20/6950415f8e7cda64b46247514668.jpg&submit=æäº¤æ¥è¯¢
```

![](https://img-blog.csdnimg.cn/45b4e6adb3f74b1daa51405115c07c88.png)

免责声明：由于传播或利用此文所提供的信息、技术或方法而造成的任何直接或间接的后果及损失，均由使用者本人负责， 文章作者不为此承担任何责任。

转载声明：儒道易行 拥有对此文章的修改和解释权，如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经作者允许，不得任意修改或者增减此文章的内容，不得以任何方式将其用于商业目的。

博客:

<https://rdyx0.github.io/>

先知社区：

<https://xz.aliyun.com/u/37846>

CSDN:

<https://blog.csdn.net/weixin_48899364?type=blog>

公众号：

<https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg5NTU2NjA1Mw==&action=getalbum&album_id=1696286248027357190&scene=173&from_msgid=2247485408&from_itemidx=1&count=3&nolastread=1#wechat_redirect>

FreeBuf：

<https://www.freebuf.com/author/%E5%9B%BD%E6%9C%8D%E6%9C%80%E5%BC%BA%E6%B8%97%E9%80%8F%E6%8E%8C%E6%8E%A7%E8%80%85>

文章来源: https://xz.aliyun.com/t/12007
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)