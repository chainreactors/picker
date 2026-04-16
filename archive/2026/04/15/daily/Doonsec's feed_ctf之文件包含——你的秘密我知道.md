---
title: ctf之文件包含——你的秘密我知道
url: https://mp.weixin.qq.com/s/UQpnYk6z3WiWjKAjkA489g
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:50:43.527552
---

# ctf之文件包含——你的秘密我知道

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/njicUbJnVlIw10WE2gaLzFGRgMSOa3AnmukjoDIVhXXFU4tJXxQrIQ8P68iaJh88lrdbMlbguwSfkAspYQQ9sNgJskx5NsJvpsrT5s0iaSPSc4/0?wx_fmt=jpeg)

# ctf之文件包含——你的秘密我知道

原创

书中自有代码来
书中自有代码来

书中自有代码来

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、什么是文件包含

文件包含可以直接执行被包含文件中的代码，包含的文件格式是不受限制的，只要能正常执行即可。文件包含又分为本地文件包含(Local file include)和远程文件包含(Rmote file include)，不管是哪种都是非常高危的，渗透过程中文件包含漏洞大多可以直接利用获取webshell。在php中，一般使用这些函数：include(), include\_once(), require(), require\_once()，它们之间的区别在于： include()和include\_once()在包含文件时即使遇到错误，下面的代码依然会执行；而require()和require\_once()则会直接报错退出程序。

# 二、包含文件的位置

## （一）本地文件包含

### 漏洞演示

本地文件包含，顾名思义就是包含本地的文件，即相对于对方服务器的本地，目标服务器上。

漏洞代码示例：

```
<? php
    $file =$_GET['file'];//GET方式获取参数
    include($file);//包含该文件
?>
```

> 这是个典型的本地包含漏洞，并没有限制后缀，可以包含任意格式的文件，利用”../”可以跨目录，另外如果包含的文件非php可执行代码，会把文件内容打印出来。
>
> 访问链接是：
>
> ```
> http://xxx.xxx.xxx/web3/index.php?file=tips.php
> ```

> 绝对路径和相对路径的区别：
>
> | 特性 | 绝对路径 | 相对路径 |
> | --- | --- | --- |
> | **定义** | 从文件系统的**根目录**或**盘符**开始的完整路径。 | 从**当前文件**或**当前工作目录**开始的路径。 |
> | **特点** | 定位精准，不受当前文件位置影响，但灵活性较低。 | 灵活，但容易因当前目录改变而失效（如文件嵌套时）。 |
> | **示例** | **Windows:** `C:\Windows\System32\` **Linux:** `/var/www/html/index.php` | `./index.php` `../config.php` `web/index.php` |
>
> `.` 代表当前目录,`..` 代表上级目录

本地文件包含漏洞可以帮助攻击者获取webshell。

### 绕过技巧

1. 限制访问目录时，使用相对路径跳转到指定目录，使用绝对目录时会报错。
2. 限制包含的文件名时，可以在包含文件名后面加上%00隔断，但该方法只支持PHP<5.3且magic\_quotes\_gpc = Off，即使用php中字符的结束标识符来截断字符串。
3. 通过加长url来实现自动截断，但部分服务器可能已有应对策略，但一般情况下，Windows下240个”.”,Linux下4096个”./”就可以。

## （二）远程文件包含

当服务器满足前面本地文件包含的条件并打开allow\_url\_fopen选项和allow\_url\_include这两个选项时，可以使用远程文件包含。

### 绕过技巧

1. 在url后面加入？截断，因为”?”后面再加上任何内容都不会影响远程的txt文件输出。
2. 伪协议

> | 协议 | 描述 | 典型利用 |
> | --- | --- | --- |
> | **file://** | 访问本地文件系统 | 用于读取本地源码或敏感文件（如 `file:///etc/passwd`） |
> | **http://** | 访问 HTTP(s) 网址 | 用于远程文件包含 |
> | **ftp://** | 访问 FTP(s) URLs | 用于远程文件包含 |
> | **php://** | 访问各个输入/输出流 | `php://filter/read=convert.base64-encode/resource=flag` |
> | **zlib://** | 压缩流 | 用于处理压缩数据 |
> | **data://** | 数据（RFC 2397） | 用于直接执行数据流中的代码 |
> | **glob://** | 查找匹配的文件路径模式 | 用于探测目录下的文件列表 |
> | **phar://** | PHP 归档 | `phar://zip文件名/shell名` ,PHP5.3后才加入此协议 |
> | **ssh2://** | Secure Shell 2 | 用于 SSH 连接 |
> | **rar://** | RAR | 用于访问 RAR 压缩包 |
> | **ogg://** | 音频流 | 用于访问音频文件 |
> | **expect://** | 处理交互式的流 | 用于执行系统命令（需开启相关扩展） |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

书中自有代码来

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/r57aCSG0dAvRdibKXBVSFWfFICJEzZvhogOeVscgwnjia8ZpicPMOOaE8t68cXrJE6oib5x8FjWNmd076icCj9nvWMw/0?wx_fmt=png)

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