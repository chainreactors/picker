---
title: 网络流量包练习题解题详解（附详细解题视频）
url: https://mp.weixin.qq.com/s/NYrpMLuGZOMpiECowW5meg
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:26:38.437568
---

# 网络流量包练习题解题详解（附详细解题视频）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaZxV0LSm5uCTUIgibzvyibMLKEVNzciaZTp9nwzcjice6N8VseQF6JgOLQA/0?wx_fmt=jpeg)

# 网络流量包练习题解题详解（附详细解题视频）

原创

小谢取证
小谢取证

小谢取证

![]()

在小说阅读器中沉浸阅读

给大家带来一期详细的网络流量包解析，文末有解析视频与检材。

51.攻击者的IP为？（答案格式：192.168.1.1）

参考答案：10.211.75.6

先试用IPV4地址统计分析，出现次数最多的3个IP地址。192.168.1.9和59.110.185.49

和10.211.75.6

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiavMsOA198RPhLnJAic7Z66cfia1cJgeH9IFSPavCzYsQBBbmawFbMELiaQ/640?wx_fmt=png)

再使用会话统计，可以看到会话最多的几组
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaicQiaBL6nyiaYkXh1EibqD0xlIwZDmCVDuPNib8halmYEbCqox3W1xcXE9g/640?wx_fmt=png)

但这样好像也不太好看出来，我们可以使用过滤条件http.request.method=="POST" 进行过滤，因为攻击机一定会对被攻击机进行后台登录。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaDVavAmuXLLuZWBT4KWRLhEP4ztBMCTyP8rQ6ovgdxtHI7d1U5WV8MQ/640?wx_fmt=png)

所以攻击机是10.211.75.6 被攻击机是192.168.0.177

使用AI验证一下
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5Pmia0d3Z5pFaF0Nb31IggzPIFk5H1Eya67zVYibOHEycIFyqZwiaAic73BvyQ/640?wx_fmt=png)

52.被攻击服务器的网站框架是？

参开答案：zend      (PbootCMS?)

既然能够确定攻击机与被攻击机，那么网站框架的信息就在被攻击的服务器的应用层，所以这个时候我们可以过滤源IP地址是192.168.0.177。使用过滤条件ip.src==192.168.0.177 过滤源IP地址。并且要满足源IP地址是192.168.0.177，目标IP地址是10.211.75.6
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiafX8DbFeCLWgZiarWzRpWeTkFG4F3ZPPtVv7BkGXIV7PbrojrVcVSjtg/640?wx_fmt=png)

答案疑问 因为
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaicGxfOQazzyZUml0iaI4NzJy4lZtsLEB1NlA6jqicIj0NJOtd9tUYYH3w/640?wx_fmt=png)

用AI验证一下
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5Pmiaq53BVRWE3mIiaZLUcqE5PMjV5licfcMd5MNODQfLbTH7icdoNp0QEI7Eg/640?wx_fmt=png)

后续详细的解答在下面的题目当中。

53.攻击者对网站后台登录进行了暴力破解，成功获取到的用户密码为？格式：按实际值填写）

参考答案：admin123

既然是进行登录的行为，那么所做得动作是POST，所以可以使用过滤条件http.request.method=="POST"进行过滤。又因为是网站后台，所以一般登录的地址是带有admin关键词，又得看下最近的时间。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5Pmia8mro1SMCreN9HomEeRouWZfsSroZm1jBTz4NXgQ83dCqxoFHUUOOww/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiammZxecRBabXiaUfOaGoicGVHJLbuMGibAaLic3kLHEH8micYswcK51yYR7w/640?wx_fmt=png&from=appmsg)

所以密码是admin123

54.攻击者第一次成功登录网站管理后台的UTC时间为？ 2025-01-01 00:00:00）

参考答案：2025-05-27 16:17:10

所以第一次登录后台的时间如上题，换算一下时区的时间可得。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5Pmia66ZZ9IkuE2iavzFDC3fiadYOictoJKWudeN192b0SG591wB8Y0iaXsG7cA/640?wx_fmt=png)

涉及到密码也可以尝试使用过滤条件
http.request.method =="POST" and http matches "password[^a-zA-Z0-9]lpasswad[^a-zA-Z0-9]pwd[^a-zA-Z0-9]mima[^a-zA-Z0-9]"

55.攻击者上传后所执行的一句话木马文件名为？（答案格式：1.doc）

1657037870691680.phtml

题干已提示为一句话木马

所以一句话木马就可以直接使用语句http contains "POST["进行过滤，因为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5Pmiaah5oh9oib7VVf8cszdNKGQlbawF0ziawhnhhVMkQicNTMJqiaIVcZaxibdg/640?wx_fmt=png)

所以过滤出来
   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaxoUjibiaFmpY3JbiacN9sgEdzGWwfJrxvyyLA1luAcWEZ5F5I9tqAic0pQ/640?wx_fmt=png)

对其进行追踪，发现一句话木马的密码(h4ck4fun),和上传的小马(/static/upload/other/20220706/1657037870691680.phtml)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5Pmia3xic7LGy7ujsbNL9661o3swcbaOKruptJQOF8P6Q4QicpCZhl3jVh5mA/640?wx_fmt=png&from=appmsg)

56.攻击者获取到的服务器账号权限为？

参考答案：www-data

1.
因而围绕这个小马地址来探索黑客执行了什么命令
继续使用 http contains "/static/upload/other/20220706/1657037870691680.phtml" 过滤，查看黑客上传小马后执行了什么命令。

可以看到，第三条明确标注了请求数据类型是 application/x-www-form-urlencoded（表单编码格式），说明这条请求携带了提交的数据；而第一条没有这类内容，只是单纯的资源请求。

我们可以看一下它第一条执行了phpinfo
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaXkdF23c0Ij5RvLg9VY1QyaSGkvO6RZT3wzdwKhxzibJE7BmYWicMLe3g/640?wx_fmt=png)

且也看到了网站框架zend

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaMOofVzlHr6V8E2UEnpjtiaOAb8cImknxpkC0jNpeXm6ibXnEnuePiafaA/640?wx_fmt=png)

就可以纠正52题网站框架得题

继续追踪命令发现 黑客在执行whoami得命令，显示出的是www-data得用户
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiarITvxIAOBKfmXJiaCfM6ibwO28ePn0X3HeZErlEic92KlymzoQxqNx9Mg/640?wx_fmt=png)

57.网站mysql数据库的连接密码为？（答案格式：按实际值填写）

参考答案：p4ssw0rd

在上一题，我们使用http contains "/static/upload/other/20220706/1657037870691680.phtml"进行过滤，查看黑客在上次小马后进行了什么样的操作，其中就可以发现，黑客有查看了网站源码当中数据库的配置文件行为，我们就可以看到起数据库账号root的连接密码为p4ssw0rd

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5Pmiarb096uZ0NGoFR1uufyLFvrrC92UxPJgn0ibDBjjzxEpS8iaDsn6fwyVA/640?wx_fmt=png)

58.数据表ay\_user中用户名xiaoming的密码为？

参考答案：1qaz2wsx

从上题题干得信息，可以知道被攻击机所使用得是mysql数据库，所以，我们就可以使用过滤条件
tcp contains "mysql"

使用该过滤条件过滤之后出来有四条，优先查看攻击机对被攻击机得操作。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaYDHsPhDvs42bJlCrbrXCopwItjaIOV2UK12tdia1IQj2UcDbWzicLB9w/640?wx_fmt=png)

我们对该条进行追踪一下，可以发现黑客所执行的命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaUaHSZU2ibicvrToPed0ZceunRA5HfpD1DqU5xMpOltf7UCzLKqONUWiaQ/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiasMuAibKTicl0zS3ppBibpWU3gFfVACicFF4YcXJLB5Cbx6CFt6JZxGw8Qw/640?wx_fmt=png)

往下拉发现
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaXBo7X9huicbdx9Gib19XniacuFI2Yg19kozf08wEA0AmIQYINYbRoD2LQ/640?wx_fmt=png)

看到=号像是base64编码，进行解码后可得到密码1qaz2wsx

59.攻击者把网站进行了打包，打包的密码为？

参考答案：5034737377307264
继续使用http contains "/static/upload/other/20220706/1657037870691680.phtml"过滤条件分析黑客输入过的命令，
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaJ9Mc4rN1HANtSIicjEeC09LQTibAZEiavn5JBzURicLZKBCeVZAynXOg0g/640?wx_fmt=png)有%号的话可以使用URL进行解码
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaRIGqs983PkZCQjCq4ZiauBKA9rX0I5fy9ZBmth3dsSnGMLhniboe0iaDg/640?wx_fmt=png)

也可以直接看
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmiaQAibQj3ASg1TFjhhIs1vOfjftxyX6xWpvNTI7sWHicVOevGGhNGuT7ng/640?wx_fmt=png)

可以看到密码是5034737377307264

攻击者在服务器上进行反弹shell，连接的目标IP为？

参考答案：111.123.222.333

继续使用过滤条件http contains "/static/upload/other/20220706/1657037870691680.phtml"进行过滤。查看黑客输入过的命令
可以看到，这是一条经典的 Bash 反弹 Shell 命令。

采用base64解码后得到
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflRSYVcs99v0J0Nk8ViaO5PmialezJxib9bvX8Qc2EurxdhXFUgsepKWQ6y0Gr5KUSN8BM1bjQT1Jh4aA/640?wx_fmt=png)

所以IP地址为111.123.222.333

检材在后台回复“流量包练习案例”即可。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflQTn7rbjfcWYyeHhTPSFnLkeCfGa1T5EZFzrZDdkrmq13K3jn4PtK4CqDhWOpUVZeD2X7rpAuq02g/0?wx_fmt=png)

小谢取证

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflQTn7rbjfcWYyeHhTPSFnLkeCfGa1T5EZFzrZDdkrmq13K3jn4PtK4CqDhWOpUVZeD2X7rpAuq02g/0?wx_fmt=png)

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