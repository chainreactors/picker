---
title: 攻防必备，DLL侧载（白加黑）自动化生成
url: https://mp.weixin.qq.com/s/gpHl11zbzXqHUNv4tuA-Hw
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:08:27.887287
---

# 攻防必备，DLL侧载（白加黑）自动化生成

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibXL9MCj2GqNanpC239DYKs5hxQicM5OUsuTCukCJ58MDwvW7czXxRJINovfW9j6ib7Ae0XibKsibs40msKZ42HAUvICp3v7WAE1RBxvMKIfQ8gY/0?wx_fmt=jpeg)

# 攻防必备，DLL侧载（白加黑）自动化生成

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

还在用传统方法制作DLL测载，操作繁琐费劲？现在不需要了。

## 一、背景

### 1.1 什么是"DLL侧载"（白加黑）？

DLL侧载（`DLL Side-Loading`），常被称为"`白加黑`"技术，是一种利用Windows动态链接库加载机制的攻防技术。

> Note
>
> 应用程序在运行时，会加载所需的DLL文件，DLL容易被篡改而EXE无法验证其合法性。DLL侧载本质上是DLL未做防篡改导致的`安全漏洞`。但是很遗憾，目前这个漏洞SRC不收，但却在攻防中广泛被使用。

### 1.2 传统手工编译存在缺陷

一是环境配置复杂，测试可能需要一堆工具及命令，过程繁琐。需要理解PE文件结构、导出函数等知识，同时手工编译的DLL特征明显,尤其是Visual Studio。

## 二、解决方案

高级白加黑技术操作简单，初级人员也可轻松掌握该技术，工具全自动化编译处理，DLL低特征带[[自研高级反沙箱]](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484622&idx=1&sn=dc9f87df89fc3e2a58b955162700d3d0&scene=21#wechat_redirect)，同时轻松支持OLLVM混淆。

![1.0工具界面](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqPML9N6G8LZ3I1sIrE6vW6y8nEuibqhxiab7S8klPzhz21fgdTmCoKQpQ7WHW5flnh2KayUCTgBev5kpXzzOdtTlMicneouh8GYxs/640?wx_fmt=png&from=appmsg "null")

1.0工具界面

![1.1工具界面](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqNNkMS6JzAFWenPvSyV1f3uwmQ2smnaxZEgX7icOLRuzotNxOC6NicyOT91micVH2XTmmqJZmdcxnkTBUbDapWvylicQdfq9e857do/640?wx_fmt=png&from=appmsg "null")

1.1工具界面

而现在，`DLL侧载`和`DLL代理`被合并为一个项目为`高级DLL劫持测试技术`，便于新人学习并彻底掌握该类技术。

![1.2工具界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibXL9MCj2GqO8iaPeqoxh25RooaStOy6V6pWdibDFDXNPttWXwj3P69X3ghPfkEcQzoqlmMjDfmc3sWhicvxkvWasAvgEuDGBTxoIDTKfHGhzzA/640?wx_fmt=jpeg&from=appmsg "null")

1.2工具界面

> Warning
>
> 红队工具普遍具有进攻性，该工具具有序列号机制防止扩散滥用。

该技术是《2026年红队战术攻防武器库个人产品手册.xlsx[1]》主要技术之一。

> Note
>
> DLL侧载只是DLL劫持技术之一，另一种是DLL代理。

**视频演示：**

## 三、使用场景

1.攻防学习，合法授权的红队行动。
2.~~挖掘DLL侧载漏洞提交SRC获取酬金。~~
3.理解其原理，排查并设计防御方案。

## 四、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

1.仅可用于已获得书面授权的目标系统测试；
2.遵守法律法规，不得用于侵犯他人隐私或数据窃取；

本人不承担因用户滥用本软件导致的任何后果。使用即视为同意并接受上述条款。

---

#### 引用链接

`[1]` 2026年红队战术攻防武器库个人产品手册.xlsx: *https://www.kdocs.cn/l/coR1BuQkseWz*

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

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