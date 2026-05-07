---
title: 机器学习--基础入门--00什么是机器学习？
url: https://mp.weixin.qq.com/s/8BMcuk6SFAe-U8Q63iKPUg
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:32:28.552341
---

# 机器学习--基础入门--00什么是机器学习？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eicD4kPkImPz2RA0zKFD3wkAuuNddZVyk9q2UArdSRpAD917ibZHzeSMtz1zJP2maZXkPeDfQxHHBmvUXWaEzRZXQe1BB5mibGQS6icTGeWXeibc/0?wx_fmt=jpeg)

# 机器学习--基础入门--00什么是机器学习？

小叶Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于青鸾sec
，作者Zero

![](http://wx.qlogo.cn/mmhead/USH8Nb3Hz5SUklDje4ibRemJZ9TVDeWOCThdyTBIgk3JDC2lv3ibUjhwzwtdDmpaA5icKSOGxjJmUc/0)

**青鸾sec**
.

广东某大专大一在读新生，在网络空间安全领域当黑奴中
领域：AI For Security、Web安全
团队：SecureNexusLab-AI组成员
项目：LLMAttackGuide、SNL&朱雀AI安全科普、大模型提示词注入手扎

***声明***

本文作者：Zero

本文字数：1107字

阅读时长：约10分钟

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，青鸾sec以及文章作者不为此承担任何责任。

青鸾sec有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经青鸾sec允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。

# 什么是机器学习？

## 好靶场课程链接

> **本期内容**
>
> http://www.loveli.com.cn/chapter\_course\_list?course\_id=102§ion\_id=65">http://www.loveli.com.cn/chapter\_course\_list?course\_id=102&section\_id=65[1]
>
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/eicD4kPkImPxEgZQPkDa1ZocqEwc4Dt1xzHwiaKxShvxaMgMMLzx6ibh8Vsibue7rsDHWHmNicryQWL9NtFhA1KsCqfSqrXFCA9Rp39jJmucdg6k/640?wx_fmt=png&from=appmsg)
>
> **后期内容板块**
>
> ![](https://mmbiz.qpic.cn/mmbiz_jpg/eicD4kPkImPwYIzQGbA41xdQPYBG5jSW2cfBfoIHrNqoVF2qDxjOKhG4FJWw4icwDwsyMfEd6rywpcTWTic6BJ53kj9A4PcfWQj1ibKuOkgFeqg/640?wx_fmt=jpeg&from=appmsg)

## 好靶场介绍

> 我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。所以我们团队名称就叫“好靶场”。

## 概念：

机器学习是让计算机从数据中“自动找规律”，而不是由人逐条写死规则，从而能在没见过的新数据上做出判断或预测的一种技术。它属于人工智能的子领域。

## 对比：

最基本的 AI 模型是一系列 if-then-else 语句，其规则和逻辑由数据科学家明确编程。在最简单的层面上，即使是基本的恒温器也是一个基于规则的 AI 系统：当使用简单的规则进行编程时，例如

`IF room_temperature < 67, THEN turn_on_heater`

以及

`IF room_temperature > 72, THEN turn_on_air_conditioner`

恒温器能够自主决策，无需人工干预。在更复杂的层面上，由医学专家编程的庞大而复杂且基于规则的决策树可以分析症状、情况和合并症，以辅助诊断或预后。

而相比于上面传统的编程规则，简单的说就是：传统AI靠“人写规则”，机器学习靠“自己悟”。

拿垃圾邮件来说：你不需要人工总结垃圾邮件长什么样，直接扔给它大量邮件样本。模型会自己猜、算错在哪、然后调整自己，这样反复练习，它自然就“暗中”学会分辨了。

| **传统编程** | **机器学习** |
| --- | --- |
| **程序员编写明确的规则** | **计算机从数据中学习规则** |
| **适用于问题明确、规则清晰的情况** | **适用于复杂、规则难以明确的情况** |
| **例子：编写计算器程序** | **例子：编写识别垃圾邮件的程序** |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eicD4kPkImPyxr73aFXfbbZdM293EZrEgt7v15wtAtic6rZOOvk70ZeicWO4xgwibPfqwIHxibcPmhvPUM37qLD3r9VzJkAEnthgM0iaPu71yJqu0/640?wx_fmt=png&from=appmsg)

---

## 类比：

想象一下，你正在教一个小孩认识各种动物，你不需要告诉他"所有猫都有两只耳朵、四条腿、胡须…"这样复杂的规则，而是给他看很多猫的照片，告诉他"这是猫"，慢慢地，这个小孩就能自己认出以前没见过的猫了。

![](https://mmbiz.qpic.cn/mmbiz_gif/eicD4kPkImPwuAGBYl47eibbib38pxtqokrYmYuQpxUTcaxo7bxhgsoIVLBPNoYdFKwaor24UZG3cibibqtGStHojSiaIZeofz8RA3aUgoWqZJxb8/640?wx_fmt=gif&from=appmsg)

机器学习就是这样一种让计算机学习的方法：我们不直接编写复杂的规则，而是让计算机从大量数据中自动找出规律和模式。

> 参考链接：https://www.runoob.com/ml/ml-intro.html

## 展望：

随着 AI 系统要执行的任务变得越来越复杂，基于规则的模型也变得越来越脆弱：通常，无法明确定义模型必须考虑的每一个模式和变量。而机器学习是一个不断发展的领域，它正在改变我们与技术的互动方式，并为解决复杂问题提供了新的工具和方法。

#### 引用链接

`[1]`http://www.loveli.com.cn/chapter\_course\_list?course\_id=102§ion\_id=65: *http://www.loveli.com.cn/chapter\_course\_list?course\_id=102§ion\_id=65*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7cwYsJwE4IyPczNesOwRdnluVLvWzdawcOwwibmTlUeEhIhM8kTYj8XgMe87atk9icaFOGu6icVZ09msmzgL2X7ww/0?wx_fmt=png)

小叶Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7cwYsJwE4IyPczNesOwRdnluVLvWzdawcOwwibmTlUeEhIhM8kTYj8XgMe87atk9icaFOGu6icVZ09msmzgL2X7ww/0?wx_fmt=png)

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