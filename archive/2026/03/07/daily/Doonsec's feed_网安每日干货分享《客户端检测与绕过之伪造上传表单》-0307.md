---
title: 网安每日干货分享《客户端检测与绕过之伪造上传表单》-0307
url: https://mp.weixin.qq.com/s/SmFM_nEu_wv7hhD1HfYnKA
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:06:33.379004
---

# 网安每日干货分享《客户端检测与绕过之伪造上传表单》-0307

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QJTLZsy5trHicVFwWm8TOMq0oyDP3LibePfBBau9w0tx72ibJWP8qVIOKNmxKD3l4B3fz5RtqH5wZ2EKvWgYeMNic9qKnPTaGwWcssPHmDSkRDI/0?wx_fmt=jpeg)

# 网安每日干货分享《客户端检测与绕过之伪造上传表单》-0307

原创

建哥聊安全
建哥聊安全

建哥聊安全

![]()

在小说阅读器中沉浸阅读

# **客户端检测与绕过之伪造上传表单**

## **实验目的**

通过本实验，掌握文件上传客户端的检测原理以及绕过方法。

## **实验环境**

·操作机：Kali

·靶机：Apache + PHP

·实验地址：http://ip/upfile/1/upload.html

## **实验原理**

文件上传的客户端检测主要通过前端的JS代码获取文件后缀名进行验证，后端PHP代码没有对文件做任何检测，因此只需要绕过客户端检测。
客户端检测的绕过方法有三种：

1. 删除浏览器事件

2. 通过BurpSuite抓包修改后缀名

3. 伪造上传表单

## **实验步骤**

1、登录操作机，打开浏览器，输入实验地址：http://ip/upfile/1/upload.html

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEJp922ez2nic0K13IiaQ8fvd9t5GAByrq3A4icfHa9xcvFVLWkiazax3icJoicvGXiaUtoqtyNhaibKucuY0K1yDEtjCWK5Tu3s7evIMo/640?wx_fmt=png&from=appmsg)

2、在操作机上准备要上传的文件（脚本文件），比如新建info.php文件

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFasicId20CsyjgDHeXY6sJ8eoibq9jrfntcqnqjZ8KOjfmI6N951W3F2ia7icsolhAqgAa0Vj0AFyWY1RYO8TQIHVbWfLWaicuHe90/640?wx_fmt=png&from=appmsg)

3、点击“选择文件”按钮，选中要上传的文件

4、点击“submit”按钮，文件上传失败

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGDiclTakP23ibNT5icKRwHQxhuJSYd1WTNNEiaSzCDicsNic01OfYcBkmpsMLDhictgicaGvhh7ewKwkHoXIR59IWWibQlrSfvibHwh6FuY/640?wx_fmt=png&from=appmsg)

5、根据提示，需要上传“jpg”的图片文件，点击“确定”返回上传页面，鼠标右击，点击“查看元素”

6、可以看到表单调用了JS代码的selectFile()函数做过滤限制，并且表单提交到upload.php页面，所以伪造一个没有做任何过滤限制的表单同样提交到http://ip/upfile/1/upload.php即可，新建1.html文件，action字段根据靶机IP和端口自行调整

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGh2JutPQbVlj57zVPRljv5xefS4lVkFQDz4IkGmlNGR9DQrF9iaH9hl60dwnxryQcQUdMBa8zHaI3RabmGtdOXx9YdLsg289Yc/640?wx_fmt=png&from=appmsg)

7、双击1.html文件

8、点击“浏览”，选择要上传的脚本文件1.php

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHq5byasXGWicq6pRich3QDpKRHs6KvicdVCYPzyu6g6oLIBgrJSjyvCal5iakW8VnjmMEvQ2JDkvibuCEsSIEibqwDuUj997BROXf48/640?wx_fmt=png&from=appmsg)

9、点击“submit”按钮，再次上传文件，脚本文件成功上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trG6E5Ns2AzjhxiaAxT0ic8SDibXm73b8nRHQxTs6PDAUj1PBdePD2TK4XlXA1l9p0TA8RgmCEbjyDlfwQOrMl7WlcuLRu5y6TbLyA/640?wx_fmt=png&from=appmsg)

10、访问http://ip/upfile/1/upload/info.php，上传的脚本文件成功解析

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHxXtfNLXh1GibZOrCfdq4gw7FnAKOPKYgZ406UpDsqFsm5Kp7re1GtFVQ2fRVCzc5jt7QxFr0rDvDDLnSJnbeqqNw0rl7FJGicE/640?wx_fmt=png&from=appmsg)

## **实验总结**

掌握文件上传的客户端检测原理以及通过伪造一个没有做任何限制的表单，数据依然提交到http://ip/upfile/1/upload.php，绕过原来的JS代码的限制。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Yxh0GAibwTaORa9r0ajicyoicMtnziaKFLwhxuibUhsBa2Wup0Frtic9OI56H3Psr3tYtxVTDQcPAUk8Oze23XAeFQoQ/0?wx_fmt=png)

建哥聊安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Yxh0GAibwTaORa9r0ajicyoicMtnziaKFLwhxuibUhsBa2Wup0Frtic9OI56H3Psr3tYtxVTDQcPAUk8Oze23XAeFQoQ/0?wx_fmt=png)

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