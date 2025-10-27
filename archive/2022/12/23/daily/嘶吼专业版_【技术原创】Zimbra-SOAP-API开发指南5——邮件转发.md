---
title: 【技术原创】Zimbra-SOAP-API开发指南5——邮件转发
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247555448&idx=1&sn=3187320e01c03ed4e1a25e52ef4f4c1f&chksm=e915c942de6240545e724b785fc80d46b4e7a39955f4cf2b44502462b8eb8006b7d253970c45&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-12-23
fetch_date: 2025-10-04T02:20:46.277610
---

# 【技术原创】Zimbra-SOAP-API开发指南5——邮件转发

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdaY478yJbrvXMY0CSqmeGF7EMwTRYP4Y6OgHJtDJTq8uaUYIjoLd02w/0?wx_fmt=jpeg)

# 【技术原创】Zimbra-SOAP-API开发指南5——邮件转发

原创

3gstudent

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

本文将要继续扩充开源代码Zimbra\_SOAP\_API\_Manage的功能，通过Zimbra SOAP API修改配置实现邮件转发，分享开发细节。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdgQdHdtNTTvEYAtIYB17QxEBMt3tiasPGq6dCAe775X3RtnW90dwt3ZQ/640?wx_fmt=png)0x01 简介

本文将要介绍以下内容：

添加邮件转发

查看邮件转发的配置

查看文件夹共享的配置

开源代码

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdgQdHdtNTTvEYAtIYB17QxEBMt3tiasPGq6dCAe775X3RtnW90dwt3ZQ/640?wx_fmt=png)0x02 添加邮件转发

Zimbra支持将收到的邮件额外转发至另一邮箱，通过Web界面的操作方法如下：

登录邮箱后，依次选择Preferences->Mail

设置转发邮箱后，点击Save

如果想要转发多个邮箱，可以使用,进行分割，同时转发至两个邮箱的示例：test1@test.com,test2@test.com

接下来，通过抓包的方式分析实现流程，进而使用程序实现这部分功能

抓包获得的soap格式示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdB5WC329bcl0RWCPArvibjic7YI92JibRcoUjWfaQ68jVDxS9xzOU1qYicw/640?wx_fmt=png)

实现代码示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdW39ILyLqys2fRfn6mOJ4rkw8RygicGOtuaNT5icH81ESJT2EIHQ4NdQA/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZd6R6K2WGxU6dpr2cOBYyYia6gvLpkiaLaKAmgTgshSgFrEtUMPPxoiajiag/640?wx_fmt=png)

对于清除邮件转发的设置，只需要将邮箱地址设置为空即可

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdgQdHdtNTTvEYAtIYB17QxEBMt3tiasPGq6dCAe775X3RtnW90dwt3ZQ/640?wx_fmt=png)0x03 查看邮件转发的配置

在我们添加邮件转发前，通常需要先获得邮箱转发的配置

通过抓包发现，在访问Web主页面时，如果存在邮件转发的设置，那么返回数据会增加以下内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdXeYR0jNgiadE6lzSAPfKG4qyMGc9z4ghSw8hxOZqjfBJDoNsJdkKfRw/640?wx_fmt=png)

如果不存在邮件转发的设置，返回数据不存在字符zimbraPrefMailForwardingAddress

在程序实现上，访问Web主页面需要添加Cookie，再通过正则表达式筛选出指定的内容即可

实现代码示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdpLgPXLHKJQIzqGQ2Itx9CjCtnibNX67eexu3leJTVnSSic6Uw7ygwSAw/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdgQdHdtNTTvEYAtIYB17QxEBMt3tiasPGq6dCAe775X3RtnW90dwt3ZQ/640?wx_fmt=png)0x04 查看文件夹共享的配置

在上篇文章《Zimbra-SOAP-API开发指南4——邮件导出和文件夹共享》缺少了查看文件夹共享配置的方法，本文作为补充

通过抓包进行分析

发送的url示例：https://

发送的内容示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdeJsrgUUDlNX4skNgF6UybdJUJCXsmTmlb9BUBFH0XXh0LKfHwianY9Q/640?wx_fmt=png)

返回的内容示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdarNesb1tAaL7aJ5AibIBxvbWdnuo6F3dRia14c9J6SU4cqXqNAREKUFA/640?wx_fmt=png)

从以上内容可以知道，相关的请求为GetFolderRequest

查看GetFolderRequest的用法：https://files.zimbra.com/docs/soap\_api/8.8.15/api-reference/zimbraMail/GetFolder.html

经过前期的积累，这里也可以通过Zimbra SOAP API实现，发送GetFolderRequest，对返回内容进行筛选即可

收件箱存在文件共享的数据内容示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdEEShGyiaFJgOXeUNHHGeABvibMwSaLoicQo0Bxpncib9C84FRBbcJELaHg/640?wx_fmt=png)

在程序实现上，如果返回结果中存在字符

实现代码示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdnOIFrxEk7gguKqdiaqEibibdQFMF3F0SJWcnYh33eI4AsECrJrVfWhVvA/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdIKdSTXH7PRvoMrhC8WLGSDv8Rt2cp8t6OMribcJ80AibD73dna1mqKVQ/640?wx_fmt=png)

在删除文件夹共享的操作时，需要填入zid和Inbox对应的数字2即可

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdgQdHdtNTTvEYAtIYB17QxEBMt3tiasPGq6dCAe775X3RtnW90dwt3ZQ/640?wx_fmt=png)0x05 开源代码

新的代码已上传至github，地址如下：

https://github.com/3gstudent/Homework-of-Python/blob/master/Zimbra\_SOAP\_API\_Manage.py

添加以下四个功能：

AddForward：添加邮件转发

GetForward：查看邮件转发

GetShare：查看文件夹共享

RemoveForward：清除邮件转发的设置

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdgQdHdtNTTvEYAtIYB17QxEBMt3tiasPGq6dCAe775X3RtnW90dwt3ZQ/640?wx_fmt=png)0x06 小结

本文扩充了Zimbra SOAP API的调用方法，添加四个实用功能，实现方法和思路也可在XSS漏洞上进行测试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdOAWYBicu7nrtiaS8iaPRiaGdBg2Sf9iaf1YIT7AmOCQNz0jgiaS7Wzicwku4g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icB5q7ZsPFUgRBqSv9AugZdfickITyoib36dT1S16hksPrBGKwA6vUClm7RkbmEoKV9ibAhExcAB5BSw/640?wx_fmt=png)

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