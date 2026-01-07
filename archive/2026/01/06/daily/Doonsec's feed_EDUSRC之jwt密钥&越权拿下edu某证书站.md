---
title: EDUSRC之jwt密钥&越权拿下edu某证书站
url: https://mp.weixin.qq.com/s/zcSCqHyFEhfKPf34JWygqQ
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:28:25.090545
---

# EDUSRC之jwt密钥&越权拿下edu某证书站

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIgXY84ZAuoBeOoNkTDl1D0b18c97Zsf1ga5wmia8IpOLRNTIPwVvgMyQ/0?wx_fmt=jpeg)

# EDUSRC之jwt密钥&越权拿下edu某证书站

安全小生

![]()

在小说阅读器中沉浸阅读

以下文章来源于安全笑笑生
，作者安全笑笑生

![](http://wx.qlogo.cn/mmhead/XxT9TiaJ1ibf0Giak19prl3BFkhC9pXxqtAjrwfiaXz8SKRqpsfViaHCn8KXqJ8Wg6mYiaTeLsW2AETas/0)

**安全笑笑生**
.

这条路会很长，我会尽我的力走的更远

# 如何利用jwt漏洞拿下edu某证书站

## 前言

某次挖掘过程中发现一个很简单的系统，本来是感觉可能是企业资产，但是发现title的图片居然是某证书站的校徽，那么机会让我遇见了可不能错过，果断拿下

## 正文

##

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/98XEXnUkvMicvXYsibVPBFv2MDibNjMMD5d7PXicibticX5G6unjBCD3piakF2nyv2hWJAgEqQ0DuJAbyiaiaUogX5HBAhw/640?wx_fmt=jpeg)

某在线系统，查看icon发现是证书站校徽，于是注册进去测测

### 存储型xss

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIMkZmBicfO61gT8ZDckibfAZ5ZliauYJ3tkLkaLQl47Ms0CiaJ8oGVmblbw/640?wx_fmt=png)

进入后也不必说，看到头像必然是要测试一下个人资料的，头像上传点是首当其冲

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIoyX4B0icHC2iaDOicticmKA6NCUcH2X2ichmv18aCHxZ3bKkPC1tV8HQacQ/640?wx_fmt=png)

抓包后直接上传xsspayload，这个payload自然是谁都要备一份的，能水谁不想水一个呢：

```
<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">   <rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />   <script type="text/javascript">      javascript:top[`al`+`ert`](document.domain);   </script></svg>
```

后缀名改成xml然后狠狠入：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIa2t4ONA5N5DDPoJ6kH4yEntV7dHiaHIia4mbSTI2mxCm2PjELbDu8DqQ/640?wx_fmt=png)

弹窗：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIpBibiawarcStA0LA4rJvtdsgicyF6t1esNdXmnRf6gAL8AQGRjdmTxuIg/640?wx_fmt=png)

妙哇~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIT2mfVNEI36YJtOxPa433nwUDzeAicggMY0yfBfia8kCDicgorSuMtXRkw/640?wx_fmt=png&from=appmsg)

### 爆破JWT秘钥导致重置管理员密码

###

本来都要退出系统了，因为实在没得测试了，但是退出之前依旧习惯性的爆破了一下jwt密钥：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDI4P6glsiaicwlmQTdTzY9Mk8fAmtpkicMdGEYZibnG15Zfp6Gtn5EWmcghw/640?wx_fmt=png)

竟然有意外之喜，可以看到载荷中的参数有user\_id还有username两个参数其他的参数对于身份认证没有意义

只要把账户的uid和uname替换掉然后就可以越权操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIrHCWHfWczaSew3ujSiaZkLsoakibQsQd2nb1F4ccEicIH7pEpk3JkGdWw/640?wx_fmt=png)

在忘记密码处，点击“更新”进行抓包

于是我创建了两个test账号账号，用这两个账号看看能不能进行忘记密码的操作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIiaBYTgP9mwgsZODicuBEPXoPevl9Bicb55IVgDXBSkOOAmUUeokwpicYXQ/640?wx_fmt=png)

在把JWT解析替换了再换掉user\_id和username，直接发送：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIzfNt8ke5TuUdjXz7szWferzpoeyfbm8vqTKyhlsgNpQbnDuIBk3Eqw/640?wx_fmt=png)

成功了，于是尝试登录，发现果然可以

那么就看看管理员的可不可以，直接猜管理员的username是admin，user\_id自然是1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIBsTlajIhicExVB3x3G9bMiaVQSgZiaicnqt5Uy9SdTiaL7SqOJAmDxAUkzA/640?wx_fmt=png)

没有成功？先不急，笑笑生的英语不好但是也可以看出来返回的这段话的意思是：该key对应的账户名不是admin，而是username

于是猜测username就是admin用户的名字

果断替换：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIVibIj75LX9CKnQUDVXQN3icM1ZHqZibQSOFHuwBJG1adVeXMXt1qicTn2Q/640?wx_fmt=png)

噫嘘唏！快哉快哉

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIstwb7y7BZ0cDq1bBPzHULMeSSryIEAWJZiaOgtYmRaHm9pJQqeDKFLQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/98XEXnUkvMibTcyl0ylAdnOqIXNvjMibDIE8CzicLrILLyzwugzLvibvamDR9RzUsLcodRU3EGcRI4C0hwUkPERQVw/640?wx_fmt=png)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/qERLC0KMKDEgJVBZMIbBDn9eXk3PiaYAb3eOgyyHjyHLNorf3J9Kxe3ibPiaIy6M5qQtLLyxQXsXQloJ6obbjFv6Q/0?wx_fmt=png)

安全小生

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/qERLC0KMKDEgJVBZMIbBDn9eXk3PiaYAb3eOgyyHjyHLNorf3J9Kxe3ibPiaIy6M5qQtLLyxQXsXQloJ6obbjFv6Q/0?wx_fmt=png)

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