---
title: Patch白文件绕过360免杀fscan扫描工具
url: https://mp.weixin.qq.com/s/R6_19BqBXUVQMJr1DgOnmg
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:42:47.447232
---

# Patch白文件绕过360免杀fscan扫描工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQXH33O9HCvsz95JLibwq1ZPFQJ4VdSlYP00a0ZgA4QwDPwa0RUq6gaI1EsrtM7CHlrhkTj0D1ueyctmaxjs27qaTDDiaTq9xlwxc/0?wx_fmt=jpeg)

# Patch白文件绕过360免杀fscan扫描工具

原创

Hello888
Hello888

安全天书

![]()

在小说阅读器中沉浸阅读

本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担！！！

工具介绍

自动化扫描白文件，自动Patch白文件进行免杀。支持bypass 360核晶、火绒、Windows Defender、微步沙箱等，免杀上线CS！

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQXFJqxP7PumDdCAjGGNicg8Ys5oCHB9iamB1BaGKurwfw6hZMNaZRTnegp0QB6wMZeQicB5nefLX8IibfeXiaPHthEtKyyXTRlnNDibU/640?wx_fmt=png&from=appmsg)

免杀效果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQUdodiaWdlHIiczic4OSbpgGmV7PSicjDztWX4Z03qHGTbPva4pKdys1gBEn5sMC0icco7KcWaFibrq9OWvs4M480icIWTcKzvGaz2Dhc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQXFiciboLwMTTY8UU1sdRo8Ryb5qKwYunqCAosTfdMeTeoFyIUf7PBN3ZLmACfbibH02OqdEghqadBkJL3hvmajL19RhLY0pRBgFA/640?wx_fmt=png&from=appmsg)

直播回放

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQUCCpHyTqCPrtmTwiaMybQo9x76F3m7ZfyNHB86ia0ZgVicXlZLM8xOjnoticqr4QU0WDFGUNDHSOTLWFT6Dns3FO0htX0syPdSGHc/640?wx_fmt=png&from=appmsg)

```
https://www.bilibili.com/video/BV1xvQUB5ExC/?spm_id_from=333.1387.homepage.video_card.click&vd_source=eaefe32d6f7dd5d14ddeeed834902ddb
```

免杀钓鱼培训课程新上线

课程目录/核心

* **0基础也能冲：全程直播教学，小白也能上手做免杀**
* **武器化免杀教学：打包工具+源码+教程，学完直接用于实战**
* **拒绝过时技术：紧跟杀软更新，教的都是当下能用的硬技巧**
* **包过免杀：详细见课表，给你免杀安排明明白白**
* 不止免杀：讲师亲授一线钓鱼思路技巧，教你上鱼
* **一次报名：直播+录播权限+后续技术更新，终身免费学习**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQW9kibz2hXYuDhAicZS2Y4OiaFyucdxU2q9FOADUgfZSVuicy1bJZdOjC381DqclPtXYsf1ezWVicmbjGiazePkYnT7nzFRcH5IZoxfU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQVUajpXGJicZRaII2IssQRCtYsf0y6aibeM4TbWRb7iaNQpq1To8ofDU1AtW8qZibjSgyZ66RhYMuhics4OICuficiaj4nyTgbo7VqncI/640?wx_fmt=png&from=appmsg)

**课程实战效果**

**公众号以往的文章里面也有绕过视频，下面是一些截图：**

**360安全卫士**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQWZGhc6ibcaDicI6OjTUvagydJhlw7qAtv6t1Dcg6keibYribb8uy4n7dpdGATMictjrwMEviaJfrBQewKLbmRmc0NvqA1TXrHgYgxGs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQWgsH8gXd62ib23oVzmPGLoFYdyrFNdyEIQSlIMPaMR088iaw7DXEtLM9gjVicibLwH90YYRHa828t7OqSsP4TqgWy2VXWhL7H9b4o/640?wx_fmt=png&from=appmsg)

过360云传查杀

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQWKkNlsGpEcMhPTROT4ocyo6wUBMelkZvS5j9N3BeVM3X2x83MzNCYZNIp97ZCpibLGBoY75hcwo7RyK5bvK0lDYMO0mMToHOick/640?wx_fmt=png&from=appmsg)

自启动维权

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQVFYjicq6FG2IcjtwVz34ejzq5Lj8FVgUCe6350FHh3NC1lDJ7bX4qicYGwsnITZlf24CiaEjcQVtmXAic9ICiaaQjyj1no1FkDR9OY/640?wx_fmt=png&from=appmsg)

360杀毒

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQWPd0Or0LbDXpm0iablSLTR1EeIcpqb8ibBpGZ95fN0gj2KyJ20mzsu5PTCOj873ys0PScTLhYA2n3UiakX4j3jEyVnNGTYicsdtia8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQXpNB8uEs5IG700yQlD4iaqo4KliaicDLT9RA9OLu2iaicGiczbR1PlXCD4xLyk9Fuqf9WlrNibmzY1GpYTUZiaTLwwHqVx0oCibdHsoB7Y/640?wx_fmt=png&from=appmsg)

**360企业版安全云**

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQW3rHrD4P65bUuTBTYdWKNJiaTXGI3K2cfzIeib2G0Fydw1e9v2iavGrZtx9ka52U6QzD1kuChCWX5iaYsAoGziacrwFsbwDc7DSvtk/640?wx_fmt=png&from=appmsg)

**火绒6**

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQUWCWxEuZTqqnXteqbACMm9QtuK6iaP57ibXsUhKe7Sw9ZC4KiblM734bgxhjs3vXSOuUYfAareAOVokl6HGMWSGX9IopNs3hFBT8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQVduL5uKPCABPDOB6EsVlpt42f8LqNSq5Wdq92dWh0CTvhtC3ibYWevRbibibnRur2VjHwHswdj9GFGtyRv5n0gjIk3NtcFM8dTJg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQUKhWTXuNdBQqttzSAfc4Q1UvDal99d36OZuQln56vDaLhlchsRA7aa7EgicWCHt0CCwpref6VLoulWvehewmmEvg2amfGFWEF4/640?wx_fmt=png&from=appmsg)

**Defender**

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQXK0r03Bib1L6b7Mynvb8fBLorn0ZWsQ8cFhzJNp741AMKtue1vic4UjOveFxUTp3k9QDmjGBBSYS7dPPNCreSQibhH2Gpume0Hmc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQVnHBdD1DcBqSnLzrlGLqrbavy9LzDgo1uVXJFI045ZHmju8CK6EpiclClntsSKMgSk5TfStPEP3NTXHo8ocnazoVk9Xib8TDk28/640?wx_fmt=png&from=appmsg)

**微步在线云沙箱**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQW0c7q6icIgyeMjfiavNyKNvPzoCOqX6hS6eyu3PicS5iaPMdCoAuYT26Y3TIIvYbroXQAKb79El0jeiaOBklQeGwh3pn17dkx2xd0k/640?wx_fmt=png&from=appmsg)

**sxf终端防护中心**

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQXc6gnBNEfhqmkZojlLibGPdm8OGLCdTHo3IqCW2qVlwVBGwHKCCynwxykMZDVXCRDhiaRAFanx6efZbs1ZWYGibWmJL1W6W9D4Qo/640?wx_fmt=png&from=appmsg)

**天晴**

![](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQXx9zCyTPMogRUj0AL2deM9xLNMm3PsX5cTsBCyodiahMMVJRZ7CGpkrDnzJa4H9rhvedbM8CUibBKzLP1lLNjtbqAFQ52OVtOkA/640?wx_fmt=png&from=appmsg)

**还有其他就不一一截图！**

**适合人群**

*** ✔️ 免杀兴趣爱好者
* ****✔️安服/WEB手补充免杀钓鱼技术点****

* **✔️ 红队进阶师傅，想补齐免杀钓鱼短板**

* ✔️ 0基础入门，想学免杀钓鱼，没人带、无门路

* ✔️ 厌倦野路子，想要系统、能落地、不踩坑的实战教学

课程价格及优惠

费用：3699

* 前5名立减300
* 学生立减200元
* 三人成团，每人立减100元
* 以上优惠活动可以叠加，共26节课。一次报名，后续更新课程免费听！

还有活动！！！现在报名送价值100元的圈子优惠券（圈子成员已达300人，也会一直更新）扫码见圈子详情：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQVuGtur0224etg2BWZwYGapzdfhpwcs0SVtspo3WkHibER9ZwgYz18dNQVDvXsVIozQky0jeG95F3XMHhH8HpqJicDic5WnkjAfts/640?wx_fmt=jpeg)

**报名联系**

**VX：TLA206011**

![](https://mmbiz.qpic.cn/mmbiz_jpg/EYGYnyEdzQWibrIVs3gOkzaBH55arXX66hG4icDoD1kJuMzk9vR4Ml5HVZQiaVAic187icPsibafW4M8ycb5bCWpVrUtLbE7PiaFMNBRNczcNGBBWo/640?wx_fmt=jpeg&from=appmsg)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

安全天书

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

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