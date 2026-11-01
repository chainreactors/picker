---
title: 不用答题也拿高分！虚拟仿真平台分数可任意篡改
url: https://mp.weixin.qq.com/s/c0ipxT8qRPC6klkIYMMFJw
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:17:56.597276
---

# 不用答题也拿高分！虚拟仿真平台分数可任意篡改

# 不用答题也拿高分！虚拟仿真平台分数可任意篡改

三垣网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明：本文仅用于安全技术研究学习，所有测试均在授权环境完成，严禁对未授权教育系统进行任何渗透、抓包、篡改操作。

00

[ 前言] .

在教育类 Web 系统当中，成绩计算、分数提交是非常核心敏感的业务逻辑。很多开发会把分数交由前端页面计算，提交的时候直接把分数参数传给后端。如果后端没有对分数做校验与重新核算，直接信任前端提交过来的score、chengji这类可控参数，攻击者只需要抓包修改请求参数，就能随意篡改考试、实验得分。

本次测试对象为某科技大学虚拟仿真实验教学平台，平台对外开放注册。普通注册账号无需任何特殊权限，抓包修改请求内的分数参数，即可随意修改考试成绩与虚拟实验分数，分数还会同步计入课程排行榜，直接扰乱教学考核。

01

[ 漏洞复现过程 ] .

1. 注册普通账号访问平台

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGLHicYDrONRe7zbuwav41K5iaiciahiaRK51DOLic09HQsgwEH2skdiaeia0HfTm7gMadCHcBVibn0K3QzlgaomLIw0gBIjX5nkMBmdMaGA/640?wx_fmt=jpeg&from=appmsg)

2.找到考试功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGJ5arX5mjKYicXTH2eYVxVLHZVqjYJ1Wia91XluVwfSq0F0HCfzO1hq5xh2zMjicQ1k9zhp8NBcWglxxXCh7ZnHprG5ZJiaK5cGl1I/640?wx_fmt=png&from=appmsg)

3.点击提交试卷，请求数据包中存在可控参数 chengji，该参数由前端页面进行计算之后传给后端。

    1>原始数据包：chengji=1&shiyan=0

    2>将chengji参数值修改为500，重放发包。

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGKb28NyMeP8FicLc844KbYvbicc8nunnicByAbD21iaxzvZQM1pynKOufZ9mPorSH2fneGibsibBYNSCxLvPlBiaQvkMpnNqVseicCft4M/640?wx_fmt=png&from=appmsg)

4.可以看到直接修改成功

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGJKOv3Jhfs7FiaiaLfQfgjt410wc1dnsibftQQjSlUlWS9Z17UrbUL7YBnszSg28tic4heiaiawsiaibjJVGbI7vIztZlEOGfACHmpLmuo/640?wx_fmt=png&from=appmsg)

5.业务影响

篡改后的考试成绩、虚拟实验成绩会真实存入系统，并且参与课程排行统计。恶意用户可以刷高分占据排行榜前列，破坏教学考核公平性。

03

[ 原理分析 ] .

这个漏洞属于典型的业务逻辑缺陷：

1. 分数的计算逻辑放在前端浏览器完成，后端不重新核算；
2. 后端没有对传入的分数做合法性校验，没有限制分数的最大、最小取值范围；
3. 直接把用户可控的参数写入数据库，攻击者通过抓包即可随意篡改。

很多开发者误以为前端页面的限制可以保障业务安全，但是前端所有参数都可以被抓包篡改，关键业务数据必须由服务端进行计算与校验。

欢迎关注我们

#业务逻辑漏洞#edusrc

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGJaWOwicn7raXm5k4xXDlBia0Okyg0R9d4niakArWeAcFZe0mbIWPKXdgcJHv0mIY6picqR7UB0GmPPeMC70E9VFWMXDEdYOj8GS3o/0?wx_fmt=png)

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