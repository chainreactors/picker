---
title: CSRF（跨站请求伪造）SSRF（服务器端请求伪造）
url: https://mp.weixin.qq.com/s/soowj2-btzCeKtn1OPiUwQ
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:22:53.071325
---

# CSRF（跨站请求伪造）SSRF（服务器端请求伪造）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zDpX4yCYbJYqbiaaTasymSDtqHjTHEOdibtCR0lrXjyJ22ocSw0LiaKjDSvRPcYX0Tiaib7XS4icAdjHKDicyNz1Lia7xA/0?wx_fmt=jpeg)

# CSRF（跨站请求伪造）SSRF（服务器端请求伪造）

原创

zoe
zoe

哦0吼

![]()

在小说阅读器中沉浸阅读

**1**

**CSRF**

伪装成已登录的受信任用户，向受信任网站发送伪造请求，利用网站对用户身份的信任，执行非用户意愿的敏感操作（转账、改密、提权、新增账号等）。

核心：

目标用户已经登录了网站，能够执行网站的功能

目标用户访问了攻击者构造的URL。

![](https://mmbiz.qpic.cn/mmbiz_png/zDpX4yCYbJYqbiaaTasymSDtqHjTHEOdibIx9ghAyLEibPbsHicKqq5PLRnnmJjk44ecVc3L2icEWJfXficSmOCtIatg/640?wx_fmt=png&from=appmsg)

绕过

Referer校验：验证请求来源为同源域名。

1、规则匹配绕过：添加<meta name="referrer" content="no-referer">隐藏Referer头

2、URL拼接：构造类似http://xx.xx.xx.xx/http://xx.xx.xx.xx的URL，欺骗网站校验Referer。

3、配合其他漏洞绕过：结合文件上传、存储XSS漏洞，构造同源页面触发请求，使Referer符合校验规则（严谨的同源绕过方式）。

CSRF Token校验：

网站为每个登录用户生成唯一的随机令牌（CSRF Token），用户提交请求时必须携带该Token，服务器校验Token合法性后才执行请求，Token通常一次性有效或定期更新。

1、Token复用：若网站Token未定期更新、可重复使用，攻击者抓取一次有效Token后，可反复用于伪造请求。

2、Token置空/删除：删除请求中的Token参数（如token=）或置空Token，仍可执行请求。

3、逻辑忽略：若网站仅校验Token存在，不校验Token与用户身份的绑定关系，攻击者可使用任意有效Token伪造请求。

同源域名限制：仅允许同源域名发起请求，禁止跨域请求触发敏感操作。

请求方法限制：对敏感操作（如转账、改密）仅允许POST方法，禁止GET方法（减少URL伪造带来的风险）。

**2**

**SSRF**

SSRF漏洞攻击的目标是外网无法访问的内部系统(因为请求是由服务器端发起的，所以能攻击与自身相连而与外网隔离的内部系统)。

![](https://mmbiz.qpic.cn/mmbiz_png/zDpX4yCYbJYqbiaaTasymSDtqHjTHEOdibia0kN8s7uEHjKwl7xj2VedWg1atEwiaiceV4iaEP1MQyOibKm4BmvwYwibSw/640?wx_fmt=png&from=appmsg)

黑盒探针

1、重要业务点：

* 社交分享功能：获取超链接的标题、封面等内容进行显示（需请求目标URL）。
* 转码服务：通过URL地址，将原网页内容调优（如适配手机屏幕），需请求目标URL。
* 在线翻译：输入URL，翻译对应网页的内容（需请求目标URL获取页面文本）。
* 图片加载/下载：富文本编辑器中，通过URL加载/下载图片到本地；或图片预览功能。
* 图片/文章收藏功能：获取目标URL的标题、文本内容，用于展示收藏信息。
* 云服务厂商：远程执行命令判断网站存活状态、采集网站信息等场景。
* 网站采集/抓取：针对用户输入的URL，进行内容采集、页面爬取。
* 数据库内置功能：如MongoDB的copyDatabase函数（可远程请求数据库地址）。
* 邮件系统：配置接收邮件服务器地址，需请求该地址校验可用性。
* 编码/文件处理：如FFmpeg、ImageMagick、docx/pdf/xml处理器等，部分可通过URL请求文件并处理。
* 未公开API：部分API存在URL参数，可用于发起远程请求，未做过滤。

2、关键URL

share、wap、url、link、src、source、target、u、display、sourceURL、imageURL、domain 等（参数值为URL时，易存在SSRF）。

白盒分析

* 查看代码中涉及“文件读取、远程数据加载、URL请求、数据采集”的函数，判断是否对目标地址、协议做了严格过滤（需结合代码审计）。

SSRF伪协议利用

* http://
* file://  :读取服务器本地系统中文件
* dict://   :字典服务器协议，可访问字典资源、探测内网端口、获取服务版本信息
* sftp://      ftp://
* ldap://
* gopher://  分布式文档传递服务，可构造POST/GET请求，攻击内网服务

绕过技术

1、限制请求域名：通过@符号拼接内网地址，欺骗服务器解析内网IP。

eg:  仅允许访问http://www.xxx.com

绕过：http://www.xxx.com@127.0.0.1/flag.php

2、限制请求内网地址：

短网址绕过：

域名解析绕过：

IP地址进制/格式转换绕过：

3XX重定向绕过：

构造一个外网可访问的页面（如http://47.94.236.117/xx.php），页面中写入重定向代码，将请求重定向到内网IP。

重定向代码示例（PHP）：<?php header("Location:http://127.0.0.1/flag.php"); ?>攻击流程：请求http://47.94.236.117/xx.php → 服务器重定向到http://127.0.0.1/flag.php，绕过内网IP过滤。

3、ip省略模式：（如127.1、0），规避服务器对长IP地址的过滤（示例：http://127.1/flag.php）。

IP地址、十六进制、二进制、二进制转换-JSON在线工具

##

```

```

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