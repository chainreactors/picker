---
title: 记一次狗运逻辑漏洞接管前台账号
url: https://mp.weixin.qq.com/s/G0gY7NxkyEydZmpWVQhlQA
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:05:13.760356
---

# 记一次狗运逻辑漏洞接管前台账号

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eQs5ycicWaynwYJj4LH1oqVNgIAspJUJv5k3Pwp8hZK9egc9QyiagkutAKQ0UtfyWDaWZfcy5HKibMkG4NehE3edJsEyphicTYNULFIWicIic41vs/0?wx_fmt=jpeg)

# 记一次狗运逻辑漏洞接管前台账号

原创

L×K@y
L×K@y

Quest安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用

注：漏洞已提交平台

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eQs5ycicWaymzkuwSWDTbQic8t6RA7clEx8T4kWj8MItVWuUUWYhUATxktxv6JYxgzG8V4FfB0O0n8GkolpRgAibgVkcWaLeXibf4etSQicLobKA/640?wx_fmt=jpeg)

登录框起手，这里有个其他师傅发的思路总结

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eQs5ycicWaym8fHIGOPX9wrYDYo7BozkVvAXyZ4SJsdrt4FmURLvdshezAZ3X1JvKQ1wVGMF4CdXQIewIEZG4kLwjyoc1HtXSib66WyLS5wD0/640?wx_fmt=jpeg)

无短信验证功能，其他漏洞并没有得到结果，尝试点击注册功能

![](https://mmbiz.qpic.cn/mmbiz_jpg/eQs5ycicWaylZHiaHbOY74ibMclfjCmz9KUawJvt9HQ8bFjPaiausyQ3kKTNbqZvvIDaN9KeYxBhJNoJfAibwynkN8RAa6Jhfwlhu9Hyog0thptQ/640?wx_fmt=jpeg)

注册功能竟然有默认密码，这下就好办了

看看账号是不是按照顺序来的

![](https://mmbiz.qpic.cn/mmbiz_png/eQs5ycicWayn25kwIM3gXULPHiaF0kHrIaydxFib7Eibptnib1co4x0kp8iceRMicbmEVpOZSPyJBALk2SQLlHAIgMqAF3TiaN0WmC2LrNyR5rLTp10/640?wx_fmt=png&from=appmsg)

fuzz之后发现基本上是使用了默认密码，完成账号接管

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/HhKWtOygby9AOqkgGmBJufyXQuKHkic54gAWia2jNlgr42TmMSfMiakvMH5ia910kQ8PicMAc2H6jtqe0Xd3zp45T4g/0?wx_fmt=png)

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