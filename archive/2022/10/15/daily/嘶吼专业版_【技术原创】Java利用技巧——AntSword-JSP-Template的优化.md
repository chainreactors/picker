---
title: 【技术原创】Java利用技巧——AntSword-JSP-Template的优化
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247552091&idx=1&sn=061377d83ca103c5d0ddbe36e914d2e8&chksm=e915dc61de6255770aee47e7bdf1d50bc6814a99def28b64ed63164faa547c08e28f7c1864c9&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-10-15
fetch_date: 2025-10-03T19:59:50.166916
---

# 【技术原创】Java利用技巧——AntSword-JSP-Template的优化

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyKt61lFrtDRRnQep29epqZ93P9MmAvHHQzxXDF0Jf1EiasrKyGDIdudw/0?wx_fmt=jpeg)

# 【技术原创】Java利用技巧——AntSword-JSP-Template的优化

原创

3gstudent

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyXXVicn0lvfkajFapJXGCHp1meaImEc8spwI5BtufTeZKpPonW9PKW7g/640?wx_fmt=png)0x00 前言

在之前的文章[《Java利用技巧——通过反射实现webshell编译文件的自删除》](http://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247536158&idx=1&sn=bf2ac369a371e9dbc147dd362f6dd4c7&chksm=e9159e24de6217326ce07dd2da34cf561f69ff81cb6ddaa1670cd7a8737e48674c6783669902&scene=21#wechat_redirect)曾介绍了通过反射实现AntSword-JSP-Template的方法。对于AntSword-JSP-Template中的shell.jsp，访问后会额外生成文件shell\_jsp$U.class。《Java利用技巧——通过反射实现webshell编译文件的自删除》中的方法，访问后会额外生成文件shell\_jsp$1.class。

在某些特殊环境下，需要避免额外生成.class文件。本文将以Zimbra环境为例，介绍实现方法，开源代码，记录细节。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyXXVicn0lvfkajFapJXGCHp1meaImEc8spwI5BtufTeZKpPonW9PKW7g/640?wx_fmt=png)

本文将要介绍以下内容：

**·** 实现思路

**·**实现代码

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyXXVicn0lvfkajFapJXGCHp1meaImEc8spwI5BtufTeZKpPonW9PKW7g/640?wx_fmt=png)0x02 实现思路

基于[《Java利用技巧——通过反射实现webshell编译文件的自删除》](http://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247536158&idx=1&sn=bf2ac369a371e9dbc147dd362f6dd4c7&chksm=e9159e24de6217326ce07dd2da34cf561f69ff81cb6ddaa1670cd7a8737e48674c6783669902&scene=21#wechat_redirect)中的方法，访问后会额外生成文件shell\_jsp$1.class，这里可以通过构造器避免额外生成.class文件。

在具体使用过程中，需要注意如下问题：

**(1)反射机制中的构造器**

正常调用的代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyXknYEwFJNE2MGCgChibnQ9yTwezJM32pd1q1ic1SicOBWicg2ibNOWsYDnw/640?wx_fmt=png)

通过反射实现的代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyXsabPic2xBxHicQtwU2vz1RhQTF0KF0GPteLwEfysicZ5hGXOZ1AftvicQ/640?wx_fmt=png)

**(2)选择合适的defineClass()方法**

在ClassLoader类中，defineClass()方法有多个重载，可以选择一个可用的重载。

本文选择defineClass(byte[] b, int off, int len)

**(3)SecureClassLoader**

使用构造器时，应使用SecureClassLoader，而不是ClassLoader

示例代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyJOD3qH1rMM7NHz9vibSCGnI0nICFhALh28jF0WOgziaJXzNRAHILPLcQ/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyXXVicn0lvfkajFapJXGCHp1meaImEc8spwI5BtufTeZKpPonW9PKW7g/640?wx_fmt=png)0x03 实现代码

为了方便比较，这里给出每种实现方法的代码:

**(1)test1.jsp**

来自AntSword-JSP-Template中的shell.jsp，代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyqQ2h8gqWibqj4Yhxak0xUMbgQ1ibFrWBDqxuo6iczrdkIUYORSCgN2OWA/640?wx_fmt=png)

保存在Zimbra的web目录：/opt/zimbra/jetty\_base/webapps/zimbra/

通过Web访问后在目录/opt/zimbra/jetty\_base/work/zimbra/jsp/org/apache/jsp/生成以下文件：

**·** \_test1\_jsp.java

**·**\_test1\_jsp.class

**·**\_test1\_jsp$U.class

**(2)test2.jsp**

来自[《Java利用技巧——通过反射实现webshell编译文件的自删除》](http://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247536158&idx=1&sn=bf2ac369a371e9dbc147dd362f6dd4c7&chksm=e9159e24de6217326ce07dd2da34cf561f69ff81cb6ddaa1670cd7a8737e48674c6783669902&scene=21#wechat_redirect)中通过反射实现AntSword-JSP-Template的方法，代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLytZXaUwVmNTswMtemoWhmeXI2o8OE8LVDpuAQhoD6yiaXZxJR5N9cSmQ/640?wx_fmt=png)

通过Web访问后生成以下文件：

**·** \_test2\_jsp.java

**·**\_test2\_jsp.class

**·**\_test2\_jsp$1.class

**(3)test3.jsp**

基于test2.jsp，通过构造器实现，代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyUicUCMo94jl0pyyZESicdLmeKK8TtmcwmIpuoE6bQQQ8cQ5wAeUczR3w/640?wx_fmt=png)

通过Web访问后生成以下文件：

**·**\_test3\_jsp.java

**·** \_test3\_jsp.class

**(4)test4.jsp**

基于test3.jsp，不使用base64Decode()，代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyCD0hiaSe7gPwkV2mSNbsU4wwVJJHQnD7O6iaykoULhVZ4PsgCwoZRlCg/640?wx_fmt=png)

通过Web访问后生成以下文件：

**·** \_test4\_jsp.java

**·** \_test4\_jsp.class

在代码实现上需要注意Java语言中数组必须先初始化，然后才可以使用。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyXXVicn0lvfkajFapJXGCHp1meaImEc8spwI5BtufTeZKpPonW9PKW7g/640?wx_fmt=png)0x04 小结

本文分享了一种不额外生成.class文件的实现方法，对于开源的代码test4.jsp，还可以应用到Java文件的编写中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyNJ7sPbBCIiaesWxs4ZJ8iaWVZoFbL5CxwMrKjyKRbDSeGc9rRrqjCqmQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLy25nJqrS3dpqubo41iaY2uw9H4XiatorZiawBbILY6kzBGaeelXPopiccfA/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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