---
title: 记某次渗透中order by排序注入
url: https://mp.weixin.qq.com/s/DR_0sQYIhNakD780YNPPHQ
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:36:37.432635
---

# 记某次渗透中order by排序注入

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/G7wcJ5iacQnX4aqkTkKSXtuCK2Gl1tgajr2YWJfVX9lUXLxl6RIVKOBGRibTOfh2ibKxcKmhfQkTjCTtiabV5JibD4g/0?wx_fmt=jpeg)

# 记某次渗透中order by排序注入

赤弋安全团队

![]()

在小说阅读器中沉浸阅读

以下文章来源于小梵安全
，作者小梵安全

![](http://wx.qlogo.cn/mmhead/ibLButGMnqJODY0cbiakO9YqtrfP5Axte2HzUvSBJxTenxV26Hup0FPANvs4xLdZicRniaPHSp5N1XM/0)

**小梵安全**
.

大学生勇闯网络安全，分享真实漏洞案例、实战思路与工具技巧。谢谢你的关注！

前言：菜鸡勿喷，主要给新手师傅说一个不同的sql注入思路，大佬划走即可。大家可以多点点关注，后续会继续更新，谢谢！

在最近的某次渗透中发现一个order by排序注入 故写下这篇文章给新手师傅看一些不同的sql注入

依旧登录框起手  有注册功能 那就先注册进去看看

![](https://mmbiz.qpic.cn/mmbiz_png/G7wcJ5iacQnX4aqkTkKSXtuCK2Gl1tgajvQib3bFEpKK0pBS6gpAnYG41ZmOC17ODAicqrfbKogLfcbSDfSmpaic9w/640?wx_fmt=png&from=appmsg)

翻到在用户管理处 有这种小箭头表示排序的 这种就可能存在排序注入

![](https://mmbiz.qpic.cn/mmbiz_png/G7wcJ5iacQnX4aqkTkKSXtuCK2Gl1tgajVno9CTLIqoRJ0hBF4DQJEZKxl6iaNf6g0KQof4gU33R7mgGcDpXEcGw/640?wx_fmt=png&from=appmsg)

那么他的后端sql语句大概就是这样的

```
select * from table where id=1 order by xxx desc;
```

这种地方在java-mybatis环境中很容易引发注入问题，

原因很简单，在mybatis中order by ${sort}传的是列名不能用#{}，因此需要额外用白名单处理，但是有的开发懒得去处理就会导致存在注入。

在基础设置中可以新增用户，可以给用户上传头像，但是这里好像上传什么都只会下载下来，不知道能不能利用，有没有大佬评论区说一下。在这里点击查询 然后抓包看看

![](https://mmbiz.qpic.cn/mmbiz_png/G7wcJ5iacQnX4aqkTkKSXtuCK2Gl1tgajNx4iaooYAbrQEkcNkySyy8zsibyaVVcUZPrmmGVADXpNzsehafTR0W2g/640?wx_fmt=png&from=appmsg)

抓包发现存在order参数 order=asc

![](https://mmbiz.qpic.cn/mmbiz_png/G7wcJ5iacQnX4aqkTkKSXtuCK2Gl1tgajlCIiczhfQNgdHNZas9mfrOVpe3R7dSzibAYPEAOEaWkctCS654icjQibnQ/640?wx_fmt=png&from=appmsg)

简单判断一下是否存在注入

发现order=asc,37页面显示正常

发现order=asc,38页面显示报错  说明存在37列

![](https://mmbiz.qpic.cn/mmbiz_png/G7wcJ5iacQnX4aqkTkKSXtuCK2Gl1tgaj7RF9VpYEMib4OlibLvJbRxiaw0vZp9jRS4UOjoJibLhbA4aA3GHHYoBILw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/G7wcJ5iacQnX4aqkTkKSXtuCK2Gl1tgajf0rmHfibVHwa2ftGgcSVSyq2AoxNcFwbbX4EU24Lv8HricibYW2IQx6FQ/640?wx_fmt=png&from=appmsg)

既然出现报错信息 那这里直接使用报错注入即可获得数据库名

![](https://mmbiz.qpic.cn/mmbiz_png/G7wcJ5iacQnX4aqkTkKSXtuCK2Gl1tgajiaufHMKyMqSKjba60qlAjVLefBiaOayUby66lqdvrVJ8GTXSETe1u72w/640?wx_fmt=png&from=appmsg)

最后，也衷心祝愿各位新手师傅们，能通过这篇文章有所收获，顺利挖到属于自己的第一个漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/G7wcJ5iacQnX4aqkTkKSXtuCK2Gl1tgajKK2HHWGFHmGHNibrjDLLErdztnfTLRB1ILvJOXxCZ9SYsBbwpRjQ3Vw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Tb6OwBlojEicRyZT8n81n70HIFAaVPfaGp7SicSOyTQXAYUCfiaQvR8kqEo2x5KNo9dINkCR9W2ibibKSnbRchwItyg/0?wx_fmt=png)

赤弋安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Tb6OwBlojEicRyZT8n81n70HIFAaVPfaGp7SicSOyTQXAYUCfiaQvR8kqEo2x5KNo9dINkCR9W2ibibKSnbRchwItyg/0?wx_fmt=png)

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