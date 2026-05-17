---
title: 【域攻防】noPac域内提权
url: https://mp.weixin.qq.com/s/gBS86kfrhbzwlpyC9s8LsA
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:43:27.721060
---

# 【域攻防】noPac域内提权

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kibYIhwqxpuibmE5TDUCGvkh7DvMDyUY6SGGKIzMsLOCX1agrR6dwAqbUmM8AfjJqLYhhQw9CBEawjhgyEWDYVd8EoEYFkjMObDgl6U880KkE/0?wx_fmt=jpeg)

# 【域攻防】noPac域内提权

原创

平凡在修行
平凡在修行

平凡在修行

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**「时光会把你雕刻成，你应有的样子」**

## **「免责声明」**

本公众号分享的所有文章仅用于信息防御技术研究，切勿用于其他用途。由于传播或利用此文所提供的信息、技术或方法而造成的任何直接或间接的后果及损失，均由使用者本人负责， 文章作者不为此承担任何责任。

## **「一、漏洞原理」**

* CVE-2021-42278，机器账户的名字一般来说应该以`$`结尾，但AD没有对域内机器账户名做验证。
* CVE-2021-42287，与上述漏洞配合使用，创建与DC机器账户名字相同的机器账户（不以$结尾），账户请求一个TGT后，更名账户，然后通过S4U2self申请TGS Ticket，接着DC在`TGS_REP`阶段，这个账户不存在的时候，DC会使用自己的密钥加密`TGS Ticket`，提供一个属于该账户的`PAC`，然后我们就得到了一个高权限ST。
* 假如域内有一台域控名为 DC（域控对应的机器用户为 `DC$`），此时攻击者利用漏洞 CVE-2021-42287 创建一个机器用户 `SAMTHEADMIN-48$`，再把机器用户 `SAMTHEADMIN-48$` 的 sAMAccountName 改成 DC。然后利用 DC 去申请一个TGT票据。再把 DC 的sAMAccountName 改为 `SAMTHEADMIN-48$`。这个时候 KDC 就会判断域内没有 DC 这个用户，自动去搜索 `DC$`（DC$是域内已经的域控DC 的 sAMAccountName），攻击者利用刚刚申请的 TGT 进行 S4U2self，模拟域内的域管去请求域控 DC 的 ST 票据，最终获得域控制器DC的权限。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kibYIhwqxpuibzo4gpeoAheasNMaTujDndmic8zpHUOoMz9t6C27aKO52E7zLVgvhKJn3vibqMxTibjZtbvDO7dliao6ickhY0hn0MnaayZckWTe98/0?wx_fmt=png)

平凡在修行

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kibYIhwqxpuibzo4gpeoAheasNMaTujDndmic8zpHUOoMz9t6C27aKO52E7zLVgvhKJn3vibqMxTibjZtbvDO7dliao6ickhY0hn0MnaayZckWTe98/0?wx_fmt=png)

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