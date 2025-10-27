---
title: 【技术原创】Zimbra-SOAP-API开发指南3——操作邮件
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247552840&idx=1&sn=baa32921e2ee5926a6c3cf13746533d2&chksm=e915df72de625664b82b3371e630f3ba18b5281b874bd83ec81a80410043e3ad4695b726045b&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-10-27
fetch_date: 2025-10-03T21:01:54.312473
---

# 【技术原创】Zimbra-SOAP-API开发指南3——操作邮件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcPeGVOr1MXxAO2r6CGSicD0WCXHAeKNeicHoZU4jMuu8TickayfialpLJkw/0?wx_fmt=jpeg)

# 【技术原创】Zimbra-SOAP-API开发指南3——操作邮件

原创

3gstudent

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcI8XWCia7Es9POIoDpDCic3bO1R55vupB9V6slHia5CMmMuvrJZvbR4VYQ/640?wx_fmt=png)0x00 前言

在之前的文章《Zimbra SOAP API开发指南》和《Zimbra-SOAP-API开发指南2》介绍了Zimbra SOAP API的调用方法，开源代码Zimbra\_SOAP\_API\_Manage。本文将要在此基础上扩充功能，添加邮件操作的相关功能。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcI8XWCia7Es9POIoDpDCic3bO1R55vupB9V6slHia5CMmMuvrJZvbR4VYQ/640?wx_fmt=png)0x01 简介

本文将要介绍以下内容：

查看邮件

发送邮件

删除邮件

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcI8XWCia7Es9POIoDpDCic3bO1R55vupB9V6slHia5CMmMuvrJZvbR4VYQ/640?wx_fmt=png)0x02 查看邮件

Zimbra SOAP API说明文档：https://files.zimbra.com/docs/soap\_api/9.0.0/api-reference/index.html

结合Zimbra SOAP API说明文档和调试结果得出以下实现流程：

调用Search命令获得邮件对应的Item id，通过Item id作为邮件的识别标志。

获得Item id后可以对邮件做进一步操作，如查看邮件细节、移动邮件、删除邮件等。

**1.获得邮件对应的Item id**

需要使用Search命令。

说明文档：https://files.zimbra.com/docs/soap\_api/8.8.15/api-reference/zimbraMail/Search.html

需要用到以下参数：

(1)query

表示查看的位置，示例如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcYDIYmc0lNU5bviahibdPbN88hmz4WMAYk1kSLK6hzNLib3L1sNwtOiakFQ/640?wx_fmt=png)

(2)limit

表示返回的查询结果数量，示例如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcyL4yaY9Mz855pHtCZIReBqkkwX2sic3cSFHA4Yvlmh5nJ8kAzoMxr0A/640?wx_fmt=png)

如果不指定该属性，默认为10

测试代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcxFeoicmibXPeHy9iafKbtU4mOQicJVicW5OflwR2ey3Bk5Tib8THMGfBZ0rg/640?wx_fmt=png)

返回内容示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcxkxM52loZuwQlkiaYf8CJtCN7hBCvkcIdkChlfqOLibqB0vONpx6QECg/640?wx_fmt=png)

对以上格式分析，发现标签<c\*\*\*对应每个邮件的信息，提取数据如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jchyaslk6nnPKadjtzwpTcFDlWqmFe2US0QK6nku1I0VSfqojO6lia0eg/640?wx_fmt=png)

格式分析如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jctDcJM3n0llnwRCAEhMDXAnN8CvPh51Zne2ia9E1VgQyjZS8DwHtoZUQ/640?wx_fmt=png)

时间格式转换的示例代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcIlnazIwHvrmo5u86tuNIJiat8OlclowV1g4T1d67jiajCvqlaQtUlkKQ/640?wx_fmt=png)

综合以上内容，得出提取Item id、发件人、标题、正文内容和发送时间的实现代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcomlGyIQfnDR1jY4PMbj7p5xM4aicw5iaQ73OMTkibFpoB3QEto1db7TuA/640?wx_fmt=png)

**2.查看邮件内容**

测试发现，查看邮件细节可以不依赖Zimbra SOAP API，访问固定url即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcoEJW4GBHaRicQLOk5JVEfc3j6ERnibyGKgibIVrFxL53wVzwsZh8u9oSg/640?wx_fmt=png)

通过这种方式可以获得完整的邮件内容，包括Base64编码的附件内容。

实现代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcBPV6Ch0I9VmsQ2WBwJibu3abwhsXEicnKNPicPrPsfGw2XibplibXjNNgqg/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcI8XWCia7Es9POIoDpDCic3bO1R55vupB9V6slHia5CMmMuvrJZvbR4VYQ/640?wx_fmt=png)0x03 发送邮件

在发送带有附件的邮件时，需要先上传附件，再发送。

**1.上传附件**

上传功能通过FileUploadServlet实现，对应代码位置：/opt/zimbra/lib/jars/zimbrastore.jar中/com.zimbra/cs/service/FileUploadServlet.class

上传细节可参考：https://github.com/Zimbra/zm-mailbox/blob/develop/store/docs/file-upload.txt

上传的url: https://

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcCQ1ebgNJN3zCVjr0maSOuj5Az5y6RTeWf6NcXoC2auPD1mopprxMcg/640?wx_fmt=png)

如果添加参数fmt=raw,extended，返回结果示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcAYKgQENZ28Cfd2bIXNMskhxtC8sNKz3VUsCnrW0PGOOZdzWAJmE7MA/640?wx_fmt=png)

经过比较，发现添加参数fmt=raw,extended能够额外获得文件类型，示例:"ct":"image/jpeg"

所以在上传时，使用url: https://<  url >/service/upload?fmt=raw,extended

综合以上内容，得出以下实现代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcX4YreaPdQ5ysDuhujiamRYiawXrmFrWbasv3LZavqNmAwguzNQ0s3EoQ/640?wx_fmt=png)

**2.发送带有附件的邮件**

需要使用SendMsg命令。

说明文档：https://files.zimbra.com/docs/soap\_api/8.8.15/api-reference/zimbraMail/SendMsg.html

需要用到以下参数：

(1)e

表示发件人和收件人等相关信息，示例如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jct8aTstIR7H3MWoSAM4icunhuVuX9BGCpSvME2JRu0vlKDjbPNRqvKww/640?wx_fmt=png)

(2)su

表示邮件标题，示例如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcxibS9icick7L1iasxI8wGpkl6Q0qBA9Z3h3DpvJwhWOXxDZk6CHc7mYgZw/640?wx_fmt=png)

(3)mp

表示正文内容，示例如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jc6BJoTVR6u7Xz74abwViaibfNzrEvUicBg4KvfMhXCJxHGWgGvTaibglcfA/640?wx_fmt=png)

(4)noSave

如果设置为1，表示邮件发送后，不在发件箱保存副本，示例代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jc3JSZmBxvuCxOWBXhgWQcQA1txoGJoF7sdBJ0Rg1DWo8E1icszibl4dDA/640?wx_fmt=png)

(5)attach

指定发送附件的aid，示例代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jc7zUqr47DR8azPFRcloibLrp0gUIk3LcXmQ1gKaBTMWdmAfrgv9pDJfw/640?wx_fmt=png)

综合以上内容，得出发送带有附件邮件的实现代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcLqJicrYwC46jO15ad51VbIZ0wctALic0USC8JoJUSaib560yHTtMLCjVw/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcI8XWCia7Es9POIoDpDCic3bO1R55vupB9V6slHia5CMmMuvrJZvbR4VYQ/640?wx_fmt=png)0x04 删除邮件

需要使用ConvAction命令。

说明文档：https://files.zimbra.com/docs/soap\_api/8.8.15/api-reference/zimbraMail/ConvAction.html

需要用到以下参数：

(1)tcon

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcemEZ5Y3oFoJqNib1HEUGaTaOV4A3H9Wgb91aOqG4ux9adPsQYFAwTMg/640?wx_fmt=png)

通过浏览器删除邮件的流程是先点击删除邮件，将邮件移动至垃圾箱，再从垃圾箱中点击删除邮件，完成邮件的彻底删除。

通过Zimbra-SOAP-API可以简化以上流程，直接删除邮件。

实现代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcMxgkKmmvxTVHj0nX00ty9CJMuHtg4ZAmeVMBKg3avKl61WmIV88CVA/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcI8XWCia7Es9POIoDpDCic3bO1R55vupB9V6slHia5CMmMuvrJZvbR4VYQ/640?wx_fmt=png)0x05 开源代码

新的代码已上传至github，地址如下：

https://github.com/3gstudent/Homework-of-Python/blob/master/Zimbra\_SOAP\_API\_Manage.py

优化了代码结构，增加了以下功能：

DeleteMail，删除指定邮件

SearchMail，获得邮箱信息，包括Item id、发件人、标题、正文内容和发送时间

SendTestMailToSelf，向当前邮箱发送一封带有附件的邮件

uploadattachment，上传附件

uploadattachmentraw，上传附件的另一种实现，用于特定条件

viewmail，查看邮件完整细节

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcI8XWCia7Es9POIoDpDCic3bO1R55vupB9V6slHia5CMmMuvrJZvbR4VYQ/640?wx_fmt=png)0x06 小结

本文扩充了Zimbra SOAP API的调用方法，添加三个实用功能：查看邮件、发送邮件和删除邮件，记录实现细节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcMibfTCgeBewib73uIc48HFMMk6picVRGj2pluKaPrgZr3SQH32Zicbkliaw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcWBWSnYJOWuD4j22ol7Ko5CXulm1ibZYNSSlebbUPgUiaPL0tcY0W24rg/640?wx_fmt=png)

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