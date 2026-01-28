---
title: 大道至简-AI赋能FindSomething实现高可用性前端敏感信息与未授权路径快速分析-渗透测试必备
url: https://mp.weixin.qq.com/s/9841JG7DgJeGKPfVaje6fA
source: Doonsec's feed
date: 2026-01-27
fetch_date: 2026-01-28T03:32:21.173245
---

# 大道至简-AI赋能FindSomething实现高可用性前端敏感信息与未授权路径快速分析-渗透测试必备

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XLoEenAE7AQzyqCorJYUonJiaicydF0oA6lBgGn8AnKnaMzSVcicqjXNoOgCWjvHiah9MBf2jOqdcnrfvxdXyMFFCg/0?wx_fmt=jpeg)

# 大道至简-AI赋能FindSomething新方案实现高可用性前端敏感信息与未授权路径快速分析-渗透测试必备

原创

Zacarx
Zacarx

Zacarx随笔

![]()

在小说阅读器中沉浸阅读

### 前言

    每次点开FindSomething我都晕的不行，一般网页我觉得还算OK，但是只要涉及到功能复杂的网站或者长的比较花哨的网站FindSomething肯定能给你干一大坨，挨个找真的是要了老命了，像我这个老同志老眼昏花要是碰上什么演练啥的更是喘不来气。

    于是我闲着没事就研究如何AI赋能FindSomething，最开始我想的是MCP，于是我做了一款，我自己也在测试ing，能用是能用，但总觉得杀鸡用牛刀，而且很麻烦，我每次都得给agent打一段话。

    这样做效率我只能给个3分。

    后面我又优化了下，我整了记事本，把固定模板放这，然后改一下模板就行。

    这样做效率我只能给个5分。

### 解决思路

    于是我想着，我得正视自己的需求，其实我的要求就是让ai分析一下FindSomething的内容而已，最最最简单的办法就是增加一个复制按钮、就这当浏览器聚焦一个网页的时候点一下复制，把提示词、插件扫出的信息啥的都融入进去，就不用mcp了。

    当然你可能会说你干嘛不直接给插件融进个AI，配置个api啥的，我想这样有几点问题：

    1.成本高，api虽然有免费的，但你要用好用的显然免费的难以应付，而且很难自由选择任何 AI，各种ai接口收发消息也是有些差异，各种配置也比较麻烦。

    2.插件显示的看着费眼一些，复制啥的也不太方便。

    当然你可能会说你干嘛不做个软件，把FindSomething的设计配合AI分析，做个高并发扫描器，但是这有个问题就是这样看着效率高，但是有几个问题，比如如何让扫描器模仿浏览器获取前端文件、如何防止AI的api key滥用、返回的东西你有心思看吗、如何解决并发限制等等问题

    虽然FindSomething+AI+批量扫描是一个很牛的想法，但我还没想到如何让其很好的实现，各位大牛有好的思路可以与我共同商议。

### 成品使用

直接输入chrome://extensions/ 打开开发者模式

![image-20260127221106566](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7AQzyqCorJYUonJiaicydF0oA6r7c8NQGUcVCkibxbEI9icvia9micqEwCGt35mRBwRcxtZicZicYiaFSu7ln8g/640?wx_fmt=png&from=appmsg "image-20260127221106566")

然后把工具目录拖过来即可安装

![image-20260127221154847](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7AQzyqCorJYUonJiaicydF0oA6ehaJ87CnKMx7IWERBibs6936tAgcrqpLXP57X4eibQjPJySdsL4xuxgA/640?wx_fmt=png&from=appmsg "image-20260127221154847")

随后随便找个网站

![image-20260127221253037](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7AQzyqCorJYUonJiaicydF0oA6VgicibwTqopribBFmvhB73NqnAH0JJI6OLMQlsRwaOqut9icxwjoAv0myQ/640?wx_fmt=png&from=appmsg "image-20260127221253037")

点击AI分析，就会复制整套提示词，然后你发给任意AI或者agent即可

提示词是我优化过的，返回的很简洁，就两点：

1. 可能存在的未授权url， 可以配合Open Multiple URLs批量点开测试

    当然，如果咱们用ai agent更简单，ai会自动分析

2. 相关敏感信息分析

![image-20260127222645557](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7AQzyqCorJYUonJiaicydF0oA6J8Aa7ic8yqvSUrEr1FL6EvNuvS6FUfUZNUs9gS5K4Y26ibPhGn2j7iaNQ/640?wx_fmt=png&from=appmsg "image-20260127222645557")

### 获取

公众号回复"20260127"获取插件

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ASIz4RAJ9pnvqWIDRXiaT978JAnY7UCQIc9RLgib4WyMKAvN5sJQJq9MlibUyPBJNR5wjvCCrPvcOWQQ/0?wx_fmt=png)

Zacarx随笔

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ASIz4RAJ9pnvqWIDRXiaT978JAnY7UCQIc9RLgib4WyMKAvN5sJQJq9MlibUyPBJNR5wjvCCrPvcOWQQ/0?wx_fmt=png)

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