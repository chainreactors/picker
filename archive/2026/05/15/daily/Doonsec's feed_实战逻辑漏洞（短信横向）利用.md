---
title: 实战逻辑漏洞（短信横向）利用
url: https://mp.weixin.qq.com/s/jI4hCcuQWPqcm8IDslVQ0g
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:13:23.752883
---

# 实战逻辑漏洞（短信横向）利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eQs5ycicWaymdukyTUPZcZzq2Mo2aoUlFqXepdUJoWCgVHMl57QBp6icibR5lXtmclswcj7icy6ZSaNV1u6ibodkiceNTcvYPYThVlic6qxhF5e5X0/0?wx_fmt=jpeg)

# 实战逻辑漏洞（短信横向）利用

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

注：漏洞已提交平台，并且已修复

点一手忘记密码

![](https://mmbiz.qpic.cn/mmbiz_png/eQs5ycicWaylIuhl2WsTUC8mI7hdUpoqKgMibRgEbjcacmo3VC1Q5vX3t25YFkYSU4N83WvBvGfz2ehl82j5XocKQUt6kAYojuPqSErVXkf38/640?wx_fmt=png&from=appmsg)

yakit抓包，试了一下短信轰炸，显示操作成功但是发短信速率没达到要求。

于是想到之前看的文章，逗号拼接一个手机号，拼接的手机号会遭到短信轰炸

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQs5ycicWayndnOX6iblL2nfqveHtzl1kAL88mnpJicOa9ibqFxBeSBnicqYzpwiaMuNiaibtKujlJdlvpl21Ub8ScnxshX8ic9ylibnVDAicyMR81u9wA/640?wx_fmt=png&from=appmsg)

拼接了之后并没有受到短信轰炸，而是......

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQs5ycicWaylZibGYpLydttb0gPIDojvSUTC6QR3swYKObu6geSickS9gPBgpDYZyqRnaeRsYUGLEklqzZC5jOeeibnWG7AZ6PftQ6Nsv2PG7ibM/640?wx_fmt=png&from=appmsg)

好家伙，危害直接加重了，验证码横向，造成任意用户登录和重置密码

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/HhKWtOygby9AOqkgGmBJufyXQuKHkic54gAWia2jNlgr42TmMSfMiakvMH5ia910kQ8PicMAc2H6jtqe0Xd3zp45T4g/0?wx_fmt=png)

Quest安全团队

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