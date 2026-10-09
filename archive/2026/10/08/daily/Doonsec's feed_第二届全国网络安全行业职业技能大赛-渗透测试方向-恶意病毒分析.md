---
title: 第二届全国网络安全行业职业技能大赛-渗透测试方向-恶意病毒分析
url: https://mp.weixin.qq.com/s/k5HNNiW-m0E0oQjEk95GYQ
source: Doonsec's feed
date: 2026-10-08
fetch_date: 2026-10-09T08:10:16.025968
---

# 第二届全国网络安全行业职业技能大赛-渗透测试方向-恶意病毒分析

# 第二届全国网络安全行业职业技能大赛-渗透测试方向-恶意病毒分析

内存余响
内存余响

内存余响

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

题目描述:

某单位在内外网互传数据的光盘中捕获一窃密木马，现提供包含该木马的样本文件。 提交要求： 通过逆向分析，找出该木马上传数据时的回连IP与端口。 附件地址：

# 分析过程

存在upx

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib8u4hZGQgUTzlJ0JicDicKfRnCXmWNYYbLVZoH8E9becPbxlrp4D1yHGGyJWHK5LaJgLzYHXNUicxLpC4BP24ibKzqxkJGVLrGLpIc/640?wx_fmt=png&from=appmsg)

脱壳之后，根据导入表wininet.dll的相关函数开始分析

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib8t27Z6ohQeWic6g8lPgR94ibDhoMoYzib4GNKwAFhlYvMv9lxNROxYYXPml1GyX56lKicTzhk0NlK50WZ60y1Zh477pfWrZVOiaHnU/640?wx_fmt=png&from=appmsg)

定位到这个函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibibK7ukgicAEHkPibj4rl8uSIYQG3RWG5w33EAnapaCmNibypvD86T1flmnJfgrfSficibPJwnjOiao4xevLZEe5yy3obYEYs7W75U7d4/640?wx_fmt=png&from=appmsg)

再次ctrl+x定位到引用它的位置发现存在C2ip明显特征

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibicZmdeyoUXEicWaIFE5ouGXHLrMol4ve4jOmwVVhZicYnlVeEficib3JvogdfYYUbwutnicJGs1mT0ZktmicctTbMnSoaOoFibsDLK9CQ/640?wx_fmt=png&from=appmsg)

动态调试一下将eax改为5

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibicVXKz3VNZ0hfKBtnibZA5gX1B62pm2khm8qoNypWlLic7Rkqwq89jjsQhGGfXNN1NH5FPLfibRcq5SicicAwYhDvxPktJLUfDFZtks/640?wx_fmt=png&from=appmsg)

执行到以下函数

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibicX2PswJyUkRH8t6z95wTfrfia397tCXQkT0qVynDx8043pvAWuXBjGxxlXGQxUjlwjfwiacFCQj03kIQMGS9a0H9uNfzYpvNHNM/640?wx_fmt=png&from=appmsg)

发现可能是个解密函数，且返回了c2 ip 172.255.63.100

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib8VwRdTOJkbNGu5qCqorv8v6Poz4nV6nYvI9QFXsuRN2WZV2dDKgvC9WFLnctbsJcnwoEf7wdNytQMKKGxZWZ16TdEMSicMCRJg/640?wx_fmt=png&from=appmsg)

2DScq 经过sub\_1400014D5函数解密之后刚是2556

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib87wibNDl8ia739CzsxVMgFaibew4y4nR0plvwjzbJMHy5bcO2pmQ8ib533MO6X0pjrVSg8FmYiatQzxPceLZ8y7tlAMUFf9j65yyd0/640?wx_fmt=png&from=appmsg)

答案就是172.255.63.100:2556

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic4YfldibtqMVhOo0ez7bhNzzvcKGfFIlhFKFvlSN3VmFvNUVyibvMYJP3SR60w6t9GFkzGY4yrGNrvk2DZYQ5lbJQppuHpG1VfI/0?wx_fmt=png)

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