---
title: 择文看图器1.0 – 类似微信看图，让你直接从图片上OCR识别文本并复制[Windows]
url: https://buaq.net/go-170988.html
source: unSafe.sh - 不安全
date: 2023-07-03
fetch_date: 2025-10-04T11:52:22.860985
---

# 择文看图器1.0 – 类似微信看图，让你直接从图片上OCR识别文本并复制[Windows]

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/3188ca246ed9677d8f0f628817ef832e.jpg)

择文看图器1.0 – 类似微信看图，让你直接从图片上OCR识别文本并复制[Windows]

HomeWindows择文看图器1.0 – 类似微信看图，让你直接从图片上OCR识别文本并复制[Windows]
*2023-7-2 16:5:21
Author: [www.appinn.com(查看原文)](/jump-170988.htm)
阅读量:24
收藏*

---

[Home](https://www.appinn.com)

[Windows](https://www.appinn.com/category/windows/)

择文看图器1.0 – 类似微信看图，让你直接从图片上OCR识别文本并复制[Windows]

**择文看图器1.0** 是一款论坛大佬 @dog 同学发布的 Windows 小工具，模拟了微信看图功能，让你直接从图片上 OCR 识别文本并复制。@[Appinn](https://www.appinn.com/zewenkantuqi/)

![择文看图器1.0 - 类似微信看图，让你直接从图片上OCR识别文本并复制[Windows]](https://static1.appinn.com/images/202307/appinn-feature-images-2023-07-02t155725-786.jpg!o "择文看图器1.0 - 类似微信看图，让你直接从图片上OCR识别文本并复制[Windows] 1")

## 缘起

经常有人在论坛寻找类似微信看图的windows应用：

* [提取PC端微信看图功能](https://meta.appinn.net/t/topic/41435)
* [有没有什么Windows看图软件可以像iOS相册，微信pc版那样，直接在图片上复制文本？](https://meta.appinn.net/t/topic/42521)
* [微信的图片浏览功能，直接选择图片中的文字并进行复制](https://meta.appinn.net/t/topic/44408)

虽然我给出了一个直接调用微信（但不进行发送）来看图的代码，不过一直得保持微信在运行状态有点不舒服（[点击该方法详情](https://meta.appinn.net/t/topic/44693)）。

所以我动手写了一个 “择（zhái）文看图器”，就像择菜一样，把文字从图片里手动择出来。

## 效果

1. 首先会全屏显示图片，当OCR识别完毕（时间视字数多少而定），窗口会闪一下，此时便可以选择复制文字了。
2. 可以设置文字显示的透明度，透明度为0就和微信看图差不多啦。
   （打开文件夹下setting.ini修改，默认为1，即完全不透明）
   ![image](https://meta-cdn1.appinn.com/uploads/default/original/3X/7/c/7cb9fbea5faaffd833efc63e978574e55f307618.png "择文看图器1.0 - 类似微信看图，让你直接从图片上OCR识别文本并复制[Windows] 3")

![说明2](https://meta-cdn1.appinn.com/uploads/default/original/3X/a/8/a8dfbbe6bac9ba5dbe23191db7b054a914d4e3de.gif "择文看图器1.0 - 类似微信看图，让你直接从图片上OCR识别文本并复制[Windows] 4")

不透明度的效果

3. 可以通过 ctrl + 鼠标滚轮 来缩放图片，快捷键esc来关闭图片。
4. 如果嫌每次都要在打开方式里面选半天麻烦，可以将“常驻.exe”放到开机项。
   这样的话，只需要在文件管理器选中想要打开的图片，然后按下按键 ` ，也就是键盘上esc下面那个按键，即可通过择文看图器来打开该图片。

## 下载地址（只支持 win10、X64 及以上的系统）

链接: [百度盘](https://pan.baidu.com/s/1w0d3W10a2_NnWK3mIRyLWQ?pwd=xwg9) 提取码: xwg9

## 局限性

仅仅适用于横排、竖排的文字，错位不严重。
复制的文本是一句一句的，没有处理换行的重新黏合，后续版本会增加这个功能。
斜着排的文字显示会错位严重，需要懂html的autohotkey大神继续开发（我不会）。

## 鸣谢

使用了 autohotkey 的 Neutron库、PaddleOCR库。
鸣谢大佬 [@18CM](https://meta.appinn.net/u/18cm) 对于html知识的帮助。

## 版权声明以及广告

开源共享，欢迎大家再次开发完善。

![测试图片](https://meta-cdn1.appinn.com/uploads/default/original/3X/7/d/7db15a279842cb2c5d83efac6670a88823dd8660.png "择文看图器1.0 - 类似微信看图，让你直接从图片上OCR识别文本并复制[Windows] 5")
bug以及意见反馈也可闲鱼联系

## 发布页面

* <https://meta.appinn.net/t/topic/44693>

文章来源: https://www.appinn.com/zewenkantuqi/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)