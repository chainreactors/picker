---
title: 实战逻辑漏洞（短信）利用
url: https://mp.weixin.qq.com/s/E6YAFNJpgTYVj4k4bgYk_Q
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:53:08.903019
---

# 实战逻辑漏洞（短信）利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eQs5ycicWaylYNg9qHmmicduCmrkbartnewCWSe17IiaZn1beiavLiaoY3ZWPHaAU2TbtibvHU5FM63csibDjHMd7HcW5L2QBq8mqYXlWRwCnrgBqM/0?wx_fmt=jpeg)

# 实战逻辑漏洞（短信）利用

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQs5ycicWaym2IUMuDuYPkO13pglb7x9yq8GgrhhG4USS73fTQEcDKlVFhibo5hE2DFia6FJibxsl7IKhttp2iaWjygP9HHbeZD7p7Qib01mOAsNo/640?wx_fmt=png&from=appmsg)

登录框起手，先测试一波短信轰炸

yakit启动！

抓包fuzz phone参数一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQs5ycicWaynXPicxtWibdJNDDFsLsoV7dQeoD3hYVz4IyQZI8iciafaS5KF8wIBeGeVCmNJnvXYmAEmeEsIAcuZxK6zuc0DmiazCF3lGvbH1wOlw/640?wx_fmt=png&from=appmsg)

并发成功，短信轰炸

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQs5ycicWaym0liaeUj9iaE0Uv4R0drViblwDy0jogSeX7nEMjIicv2EKBiahW0gs1hwxEhzE5sZHOV2pR78pHd60fribp3dEu8Jggc0uVEb32GECM/640?wx_fmt=png&from=appmsg)

这时候收到一堆短信，四位数验证码，试试能不能打任意账户登录注册

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eQs5ycicWaykhDCJJcNg6AQ9fpUSpXnh7cziaIP4p2u885TUO5yRNW9l14yCapiaeicWlGibe1Rvcf5FOpekoPIDVuvKZUnfhtiaaBlo0UViaREEJ0/640?wx_fmt=png&from=appmsg)

ok了，实现任意账户登录注册

这时候探测下资产，找一些短信接口，重复步骤试试

![](https://mmbiz.qpic.cn/mmbiz_png/eQs5ycicWayk9qFP9gamLyZEwI5vxq7CKqJ3bibtWHvde1jm8q6EluOvt8l036iagibw30QYM3cXFcm88fVWCV2KpIuHV6dmLtxHsaFiaUmlAbvY/640?wx_fmt=png&from=appmsg)

找到一处资产，图形验证码复用，实现任意账户登录注册

之后进入系统，xss实在绕不过去了。

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