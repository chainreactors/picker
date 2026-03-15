---
title: 跟着红队笔记打靶:holynix
url: https://mp.weixin.qq.com/s/2i0eWwUq-YQZwOf68ll_Fg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:25:02.370153
---

# 跟着红队笔记打靶:holynix

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hAugh98lMaQXMcWSvON6MLjFehcK9LsbkYwLeW1FOl2U8KSMIib75Lr2iaz26YECYgG9IzfY9zvoupD8s3ssavF3LYVPG6rOmF8DuibFIHSicjA/0?wx_fmt=jpeg)

# 跟着红队笔记打靶:holynix

原创

网安热爱者week
网安热爱者week

week的杂货铺

![]()

在小说阅读器中沉浸阅读

# 靶场地址：

#

https://www.vulnhub.com/entry/holynix-v1,20/

大佬的视频：

【「红队笔记」靶机精讲：Holynix - 巧用SQL注入，不用大杀器；手动拦截，让Burp Suite下岗。】https://www.bilibili.com/video/BV1aK411S7jr?vd\_source=3caf2dac9c9273de4d9b0fead4712250

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaTj9RLuciapCoqgSscUfpjXbqumMbYy3MqW23An9GyjfKibMSianFwuH0ic8T5ejccbcwzXwFleOYEJnsfzm28ZUbjcrE8icWheZSqI/640?wx_fmt=png&from=appmsg)

# 1. 信息搜集：

## 1.1. 主机发现：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaTOggCM5eqc3PRSefib5icpmFibibaL3icRsLbnBwEu4gibwyDdecDsOZzzYlRYxXc7T8LxUDncrhyj4VTMZGRAXoeQFH0ICXeDWYPZI/640?wx_fmt=png&from=appmsg)

130是靶机

## 1.2. 端口扫描：

TCP：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaTP5BygOT6PxlLACRhHicZic6hDeD5XO3VrJ47HNtl600tRCNb1OJjGjCrSoa6wPZJx8oIjtoic4VwibCLOn8Wl5e5Yhz34ZK5qCEw/640?wx_fmt=png&from=appmsg)

UDP：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaR77oz8BUbtQhp4EfHyyXvNHWW2qO5pj8uWSHXzL2C8ZVu4aGiaIchhica91YYU7VwtDcQRc1iagEMiaNhrDY90xMQ0KdTWh6icj4QA/640?wx_fmt=png&from=appmsg)

## 1.3. 详细扫描：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQJWcW1raCiciaGHEibibDcubZWfQ0QRib2mWXoicxlu9eNImFQzhIoOmBesAaRlfgX0vFyAqEICHPicxU7icTBm6hqKLicB9L6h5KAUO3c/640?wx_fmt=png&from=appmsg)

nmap默认脚本扫描：
![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSeiaInquwkY8v1abviaHCcjNY059NJknK4f6j5mh9jjWUIpODooSv7TEByqxq06H11SVTjwg0OfJj5oJibkXpg1uvKhs094ShrU4/640?wx_fmt=png&from=appmsg)

# 2. 渗透测试：

扫目录时候发现的一些很奇怪的路径 记一下。。。

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaR5ob9RO7EUaFNzGV5StkaURSlnqaEBcAl0a981YOHuot146rLXjDibO3Sdj4NCrMwvZx3E0jqEfxLOVpVf3tL5z2kaBWx6ZJVY/640?wx_fmt=png&from=appmsg)

首页是一个登入框：page参数可以文件包含，但看不了敏感文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaRDWh9nQfS5GL0ZRFdw4h2z3hMfNQx2mFW2H8bvu2fGl2VjYqWIvfzwBNqNfzkYS0tMV4vPN1y6cibPlHxsHMb9QWUUpTZMTXUQ/640?wx_fmt=png&from=appmsg)

试一下SQL注入:

```
' or '1'='1
```

成功进入~~

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaRrGBxJ8MLviavmsjclgfy4G0c70fOnH9UrPOEWDxBz1IJNs7nDoh992LDxShIEHxOvpzaMj1eibPuZiaxXR9bJ9EY2opP29rvtjs/640?wx_fmt=png&from=appmsg)

upload页面可以文件上传 但是这个用户没有权限。。。

security存在文件包含 可以看到/etc/passwd

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaRFBd6SicQB2XPzhfkh5qdguA8oCZgYtKwL6NiaNAmVCfUNbMiaAicrbXKDmtZDLWUJDhqZ3unJicc06WjYALDuwC4SBKoiaZlBasLYw/640?wx_fmt=png&from=appmsg)

但是这个alamo没有传文件的权限

试一下使用sql注入去登录其他用户

```
111' or username="etenenbaum" -- a
```

用etenenbaum用户可以实现登入，并且可以传文件。

上传成功之后没有返回上传的文件地址

用文件包含的方式看一下uoload.php源码

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSJNS7zL3magsCKpFHm2CBGtmrg1D5ibDBiaWVsvmKCp9QTXVOEAF747yOa4hy3deC8QrPXQ2b3o599lThN7TE42RWVJmuEOxT44/640?wx_fmt=png&from=appmsg)

这里引用了一个transfer.php 进一步看一眼

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQXqRr9RqsUonxRAXhus3OwZLzW9WdBSKJCAbtq9mP8CeLewWjfJUX3IbZ1rQTLoANSicWYEcoxALY9mkw3VdlL4kqCeHGZq2Qw/640?wx_fmt=png&from=appmsg)

确实是放到了/home/目录下。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaRtIfqnibbTqics8CypUx9V0xNaSmkibCY7FnOzjeRw7Do36KrN8elYUXAIGBKGMcKd28ucw78dKMNXj8icUeE2fjTtgI9mVPcqGRA/640?wx_fmt=png&from=appmsg)

和标题说的home directory是一致的

根据之前扫到的路径 尝试访问/~etenenbaum/

看看会不会有结果。

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaTVxlVgnX5pJbfmicmSNGYNEKyl0y6ZAeFMbMX2u6DHNxicRHqibOSibM8ezvicntMmPrkLGujCEwRIoo5RJe7iaibTicwicPWmLZic4wACM/640?wx_fmt=png&from=appmsg)

确实有这个目录

这里根据transfer.php的源码 它的解压是用的tar命令 所以我们压缩也要使用tar

上传之后运行就可以了

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaROabM7DjOWFZWJFeXJK4kxYzppPMiauSD9e4fa65X7zLPyKVqvqjia13Yd87rZR6hL7hL8vMNgJgACUBycZwHmriaOzxUgfriaAa4/640?wx_fmt=png&from=appmsg)

这边也试了很多其他办法：

直接传.php文件，没有运行权限

用gzip进行压缩 解压不成功

尝试使用文件包含运行这个目录里面的文件 不成功。。。

sudo -l 发现一堆东西 那就很好了

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaRRjSMjbib23jib0Gh1UNWWAvy5qyktmXwLbMgEib1q6B6BbculZAfHu1vY3nO0qKBCSk7ubXY6cEYgJLv52BK5IG1QCxialfJswTE/640?wx_fmt=png&from=appmsg)

这个提权就很简单了：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSGCqRX8w8H9hFVVBFTH2czV2YvicLImibNZA0OGQ1YkhVVT6oEMScIgJiavDiaY1nlseQ7eFVQR1AgFVG37NG0eIfK2AianLp473bQ/640?wx_fmt=png&from=appmsg)

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