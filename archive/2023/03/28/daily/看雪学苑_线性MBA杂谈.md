---
title: 线性MBA杂谈
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458499980&idx=2&sn=4fbcea70f67def142a581450ada06925&chksm=b18e8b0686f90210708fe862cec36dd253b5f1fa90251bb0170a0d51cddbf1575259b33c205e&scene=58&subscene=0#rd
source: 看雪学苑
date: 2023-03-28
fetch_date: 2025-10-04T10:53:56.041898
---

# 线性MBA杂谈

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8tmtpFWDwpoM9vgt478ZWwzF1ia9b0aVOPB4WmNNQUTVxHPf94Yy3vbQ/0?wx_fmt=jpeg)

# 线性MBA杂谈

R1mao

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HSBAkx44BvNgDiacX7ia4Eg8aAW0E20fH9zX5Xt2rGkso4QcAibbNN52XoVb9WLwIT8QZI8icv2sjic3Q/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：R1mao

# **线性MBA反混淆**

##

## **背景：线性MBA混淆**

###

### **1. 定义**

* 什么是BA(Boolean-Arithmetic)
  n 为一个正整数，且B={0，1}，那么下面这个代数系统可以成为BA
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEKc9RufsZ6wI7aDUia8pXmvLYniafLIibtHCtoDtqdfX0oQXjOm3vxIzYg/640?wx_fmt=png)
  其中<<,>>代表着左右移位，·代表着乘法，s代表着有符号数的运算。

* 什么是线性MBA Expression
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEQOV9ab94w3uJlHlruIUBtRUNCeVYXhQZTulDB8VFtQTxyuqiaPFs29g/640?wx_fmt=png)
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEUWLWa9ia24kwNX5IUPEIiacQblQ9VfrZHncx00rjn4H9EhGh4wS7j0UA/640?wx_fmt=png)

###

### **2. 应用方式举例**

例子：

如果存在
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEZqPehEE5ibCHmtw27x0ltYtmibw1kicwPqf8YveiaznO7tMAzwgBribIaWQ/640?wx_fmt=png)
那么可以移项
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrE710XuD93iaAJp7anvYm7n9qmdJG69iaucqO3jySic0FYicvcnIicNGP7Aiag/640?wx_fmt=png)
则运算x-y即可由右边的运算混淆代替。

更多的例子:
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrE8ZUOu2AJSZUQesWibw5R6Bohrec6aw8nP1Pgku7zDdTdqPNQLJMg45g/640?wx_fmt=png)

### **3. 线性MBA的生成方式**

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEGpvsE7Fb6Lzsibap3ruJ4HtPgibiaibCPEJ9Ll3ic2H0fnEnbPSpiaZibTCWA/640?wx_fmt=png)

### **4. 给出混淆过程定义**

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEliaza3Q8a6D5G4GQuEdYEt9TpGpX1OPjfkpNXHiajORia6aZuheSQDBvw/640?wx_fmt=png)

### **5. 关键定理的证明**

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEf1IXEyQYJzpZLkMY4zDjrpH1Wib2NB30VkicQT9Xf9KmHW8uWV4He8icQ/640?wx_fmt=png)

##

##

## **现有工作：mba-blast or 化简引擎**

###

### **1. 化简思路：**

* 1.使用z3等约束求解器进行化简，时间非常长且效果不尽人意
* 2.mba-blast工具(最新论文 MBA-Blast: Unveiling and Simplifying Mixed
  Boolean-Arithmetic Obfuscation)

###

### **2. mba-blast数学原理**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEpFjQ9sEf1dz3tWs2ib05vRHXBJKIibOibLibaX9znOly403gYI9QvwItwA/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEPxAmB3lgh407r0rDxNRVhXVVNJWBAYk0BDQVyZVwicAMJJpAq7eLVWg/640?wx_fmt=png)

### **3. 进一步的**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrE64IVx3L5M7CKp8IpMlg2wd1AlXx1R7QGJAyZyXSJBMKb83mC5eb4Dw/640?wx_fmt=png)

### **4. 总结**

###

### 在MBA-Blast工具中化简线性mba混淆采用的是迭代化简的过程，它证明了任何mba都可以不断迭代化简，最后化简为简单的形式，因此其算法需要迭代公式库，且变量数目越多需要的化简公式也越多。

###

### 而进一步的可以发现，本质上是一个线性代数问题，通过构造几个真值向量能够作为极大线性无关组的位运算组合，就能够通过矩阵求逆的方式将任何MBA化简至该位运算组合的表示下。因此只要选取简单的位运算组合，例如x,y,x^y,-1等，即可实现化简。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEOAd222zxReZgfE7asRIblhbIcbCKrOxWmsdicFxIULrqMEXwxSXZpYQ/640?wx_fmt=png)

**看雪ID：R1mao**

https://bbs.kanxue.com/user-home-948449.htm

\*本文由看雪论坛 R1mao 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FJjl92zYviaHbyrEZEZzyZFOjibI9RsDgTicPv5dSuE7FmbcRjV9sn7Y7qDnx1icFuO45cIj22DLEZDQ/640?wx_fmt=png)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458499288&idx=1&sn=b2b9cd6ff7388a8658d254e13c72f9ad&chksm=b18e885286f9014436a590f2531fda167be67e1e227ea395812968e828932bd44eade34b0dbf&scene=21#wechat_redirect)

**#****往期推荐**

1、[CVE-2014-1767 分析报告](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458499500&idx=1&sn=551de43832e2ea2afdcc9a48e6c76838&chksm=b18e892686f90030e52de062b889807fb76ae0c0aa510896e686eb1b48672f6a331cf35f1d8f&scene=21#wechat_redirect)

2、[Realworld CTF 2023 ChatUWU 详解](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458499288&idx=2&sn=cb04969bed75f826d5b9effd3ef47d93&chksm=b18e885286f901445c4bf1c868b51ccb423c8c9b7027e9908f11f8153ce3068a965e04fb808e&scene=21#wechat_redirect)

3、[安卓协议逆向 cxdx 分析与实现](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458499198&idx=1&sn=a16261bef71086a0eee931d5709f294f&chksm=b18e88f486f901e22359f08e9668b7e9348d8c8e15caf535774bc4ac637c0dec6e384005bb55&scene=21#wechat_redirect)

4、[Kernel PWN从入门到提升](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458499012&idx=1&sn=cc2bec22b8100661d3be4914e2cac64a&chksm=b18e874e86f90e58b02344269b99dc2f451d5f855c3288b328da9c9747640b3ccbfb7ba8d45b&scene=21#wechat_redirect)

5、[Kernel PWN-开启smap保护的babydrive](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458498982&idx=2&sn=bc108408437309cdee3a654dff730d44&chksm=b18e872c86f90e3adfdc7ea68c8ee2a5bf68a759c123ac037047b32138eb153b5b9a8593c74d&scene=21#wechat_redirect)

6、[【详解】CTFHUB-FastBin Attack](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458498963&idx=1&sn=993867aa6c42f4c5b0b28fd3a323b9ad&chksm=b18e871986f90e0f45ae967dc65c086d027eae52c31b4af07bda217aa98c4a0084ffdcab73d3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicdP7bNEwt8Ew5l2fRJxWETW07MNo7TW5xnw60R9WSwicicxtkCEFicpAlQg/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8EbEJaHl4j4oA4ejnuzPAicd7icG69uHMQX9DaOnSPpTgamYf9cLw1XbJLEGr5Eic62BdV6TRKCjWVSQ/640?wx_fmt=gif)

点击“阅读原文”，了解更多！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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