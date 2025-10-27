---
title: 某航空WIFI破解，无限制空中上网
url: https://zgao.top/%e6%9f%90%e8%88%aa%e7%a9%bawifi%e7%a0%b4%e8%a7%a3%ef%bc%8c%e6%97%a0%e9%99%90%e5%88%b6%e7%a9%ba%e4%b8%ad%e4%b8%8a%e7%bd%91/
source: Zgao's blog
date: 2024-05-07
fetch_date: 2025-10-06T17:15:48.888511
---

# 某航空WIFI破解，无限制空中上网

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 某航空WIFI破解，无限制空中上网

* [首页](https://zgao.top)
* [某航空WIFI破解，无限制空中上网](https://zgao.top:443/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/)

[5月 6, 2024](https://zgao.top/2024/05/)

### 某航空WIFI破解，无限制空中上网

作者 [Zgao](https://zgao.top/author/zgao/)
在[[渗透测试](https://zgao.top/category/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/)](https://zgao.top/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/)

![](https://zgao.top/wp-content/uploads/2024/05/IMG_0268.jpg)

坐过国际航班都知道全程十几个小时，飞机上的wifi又特别贵，动则几百块。只有头等舱和公务舱才能免费使用。但没网肯定是不行的，坐飞机的过程中就研究了一下如何免费上网的小技巧。

文章目录

[ ]

* [使用10分钟免费包](#%E4%BD%BF%E7%94%A810%E5%88%86%E9%92%9F%E5%85%8D%E8%B4%B9%E5%8C%85 "使用10分钟免费包")
* [使用公务舱的座位号登录](#%E4%BD%BF%E7%94%A8%E5%85%AC%E5%8A%A1%E8%88%B1%E7%9A%84%E5%BA%A7%E4%BD%8D%E5%8F%B7%E7%99%BB%E5%BD%95 "使用公务舱的座位号登录")
* [如果有验证码怎么办？](#%E5%A6%82%E6%9E%9C%E6%9C%89%E9%AA%8C%E8%AF%81%E7%A0%81%E6%80%8E%E4%B9%88%E5%8A%9E%EF%BC%9F "如果有验证码怎么办？")
* [总结](#%E6%80%BB%E7%BB%93 "总结")

## 使用10分钟免费包

这个航空还算良心，可以免费体验10分钟的WiFi。

![](https://zgao.top/wp-content/uploads/2024/05/image-1024x684.png)

burp抓包看一下认证的接口。

![](https://zgao.top/wp-content/uploads/2024/05/image-1-1024x521.png)

如果认证成功，当前设备的ip就可以接入互联网。

![](https://zgao.top/wp-content/uploads/2024/05/IMG_0267.jpg)

但是体验时间到期，就会提示付费购买上网包。

## 使用公务舱的座位号登录

![](https://zgao.top/wp-content/uploads/2024/05/image-2.png)

既然充钱才能变强，那么直接用别人充了钱的号就行了。

![](https://zgao.top/wp-content/uploads/2024/05/IMG_0261.jpg)

打开航旅纵横，看看公务舱的座位号，随便用一个人的座位号。

![](https://zgao.top/wp-content/uploads/2024/05/iShot_2024-04-27_19.15.09-1024x797.png)

由于是用的护照号的后4位，和爆破验证码是一个逻辑。直接用intruder爆破就行了，但是吐槽一下burp中使用random随机某个区间范围的数字是会重复的，就导致有些重复的发包。

![](https://zgao.top/wp-content/uploads/2024/05/iShot_2024-04-27_19.16.56-1024x732.png)

使用爆破成功的4位数登录。大概10分钟的就能爆破成功。

![](https://zgao.top/wp-content/uploads/2024/05/image-3-1024x723.png)

发现这个座位的人已经登录了一台设备，不过问题不大。

![](https://zgao.top/wp-content/uploads/2024/05/iShot_2024-04-27_19.19.36-1024x742.png)

这样就能无限制上网了。

## 如果有验证码怎么办？

![](https://zgao.top/wp-content/uploads/2024/05/IMG_0467.jpg)

回程的时候是另一家航空，加上了验证码要麻烦一些。可以用burp一些验证码识别的插件，或者使用python的ddddocr这种验证码识别的库就行了。

![](https://zgao.top/wp-content/uploads/2024/05/IMG_0468.jpg)

这时才发现给10分钟体验已经很良心了，有些航空连体验的机会都不给。

## 总结

这种思路很简单。用其他方式理论上也是可行的，比如mac地址欺骗，不过有些航空做了ap隔离。

当然还是多搞钱最直接，几万块的公务舱随便买，就没这些破事儿了。

Post Views: 2,938

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 10条评论

###### 匿名 发布于4:03 下午 - 2月 15, 2025

会留痕被航空公司发现吗

[回复](https://zgao.top/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/?replytocom=9330#respond)

###### 匿名 发布于5:33 下午 - 6月 30, 2024

请问无限制上网是怎么搞得？是踢了人家吗？

[回复](https://zgao.top/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/?replytocom=8360#respond)

###### 匿名 发布于2:29 下午 - 6月 17, 2024

已经加了防爆破功能，尝试失败后直接封掉当前设备

[回复](https://zgao.top/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/?replytocom=8252#respond)

###### haixingzhe 发布于2:48 下午 - 6月 10, 2024

哈哈，思路很简单，难的是动手尝试的能力

[回复](https://zgao.top/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/?replytocom=8202#respond)

###### zgaolove666 发布于3:59 下午 - 5月 27, 2024

看懂了，不给体验，就能相对安全。 被日的成本提高了

[回复](https://zgao.top/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/?replytocom=8117#respond)

###### phhhh 发布于10:55 上午 - 5月 20, 2024

你把那个人踢了他重新登录不是又把你踢了吗？

[回复](https://zgao.top/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/?replytocom=8069#respond)

###### 匿名 发布于11:00 上午 - 5月 20, 2024

写个心跳，自动登录就行。而且飞机上也不是所有人全时段都在用

[回复](https://zgao.top/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/?replytocom=8070#respond)

###### cdxiaodong 发布于12:47 下午 - 5月 9, 2024

请问您再飞机上是如何使用笔记本电脑的呢 待起飞阶段吗

[回复](https://zgao.top/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/?replytocom=7940#respond)

###### Zgao 发布于4:44 下午 - 5月 9, 2024

飞机上现在不是全程都可以用电子设备吗？

[回复](https://zgao.top/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/?replytocom=7949#respond)

###### 秩序熊 发布于11:22 上午 - 8月 30, 2024

飞机在起飞和降落阶段不允许使用pad、笔记本等大型电子设备，手机可以全程使用

[回复](https://zgao.top/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/?replytocom=8778#respond)

### 发表评论 [取消回复](/%E6%9F%90%E8%88%AA%E7%A9%BAwifi%E7%A0%B4%E8%A7%A3%EF%BC%8C%E6%97%A0%E9%99%90%E5%88%B6%E7%A9%BA%E4%B8%AD%E4%B8%8A%E7%BD%91/#respond)

Δ

版权©2020 Author By : Zgao