---
title: 反制取证典范with思路
url: https://mp.weixin.qq.com/s?__biz=MzI2MzA3OTgxOA==&mid=2657165556&idx=1&sn=ed8d86668a3a9e692a8f23f09af14be5&chksm=f1d4d211c6a35b07f6bf2a6a41b3f7c1834a1ba7c8687729dfd752bda8534e342d6b030eca09&scene=58&subscene=0#rd
source: 暗影安全
date: 2024-07-05
fetch_date: 2025-10-06T17:43:34.836960
---

# 反制取证典范with思路

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PrTu58FA79aW6vwg8n4nuAh8T4TvJgOksUuugf9sic5q0snOC8gapKhh9wkU1lbjSAdLB8xTJ5TkR3OHEJjLNtw/0?wx_fmt=jpeg)

# 反制取证典范with思路

暗影安全

以下文章来源于安全光圈
，作者z00000

![](http://wx.qlogo.cn/mmhead/McYMgia19V0WnpOxxgRcviaB3UlfOO3IB4Z0AAv1xPU9mA8hkH3L6CIenaTd6oHIicLSReKGpWS4cA/0)

**安全光圈**
.

分享攻防实战用到的技术；摄影的基础教学；搞机踩坑过程；找回自己丢失的表达欲和有趣的灵魂。

# 有趣的溯源/反制案例&&思路

### 有意思的反制案例

漫漫长夜，身为一只值守的小牛马，突然看见蜜罐上上线了一个奇怪的告警~

oh~有攻击者被反制上鱼了

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAia0KzPghB2HLBlJpQEFIyibHBxse326CZkCGCZLB0jRd7rGUxx9ffZuA/640?wx_fmt=png&from=appmsg "null")

看看上线的机器都有什么信息呢？

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAFN4iaPSAOfvX4BicTHl4C60s5uKTBEicjW4pFTLgWXL9VW6amMZyLmNow/640?wx_fmt=png&from=appmsg "null")

嗯，手机号有了，报告稳了！

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAYrNajUm8Em1ax776xPmTzcicZiciaLLqPY26UR9YkEz33fRhqO3jxe1zg/640?wx_fmt=png&from=appmsg "null")

wifi信息确认了大概的单位名，结合ip定位可以大致印证一下是否有溯偏，我这里用埃文免费查了一次发现两个信息是对得上的

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAu9qP9G4A8NJuXA6GP810TibicpianbzQqWcCwlibADvZ1dJSERm0oerT9A/640?wx_fmt=png&from=appmsg "null")

趁着机器还在线，去找找攻击者MacOS上的宝藏

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D2rnMshwwwrEYelia3uSLmcD0OxcicicK58kibF7fhz8YsnhXuRQXc4hKP8egxaCy5az5amC8qINd5rjA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D2rnMshwwwrEYelia3uSLmcDs8HP4pTSvUbOJC5b8znhDsYHp6AheecMmVicm3HV3h37KP8D56cOmBg/640?wx_fmt=png&from=appmsg)

路径东西倒是不少呢，录用通知书都出来了，这里可以写完整报告了

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAbiceLSjFIxCY35ibMKH4uZ1jIMCwsIZNia0SXKYZ7gXD0ibCBANdwpRURQ/640?wx_fmt=png&from=appmsg "null")

折腾完毕，在访问其他路径的时候估计是触发了MacOS的弹窗，被攻击者发现，清理离线了

那么根据当前的情况，过滤一下攻击者的ip，还原一下攻击者的上线经过，完善整体的反制路径

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAQLdhhXjzYTNRLqesSs3K7J4QiaI6FJYs2R4wwlq9uYywaB4PmiayicF8A/640?wx_fmt=png&from=appmsg "null")

根据日志得知攻击者在通过git扫描的钓鱼页面的时候被反制了，之后没看见对我们单位有什么动作，估计是因为git反制的原理导致的，他日后估计还会多次上线。

既然上线了那就只好把你写进我的报告啦~

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D2rnMshwwwrEYelia3uSLmcDRLbTRmMkNOV2D3DB9L0ue2aIYY04lajg9rskHibicDPBuwurY8WBgCHA/640?wx_fmt=png&from=appmsg)

### 常见的几种溯源/反制手法

现代化蜜罐都做了哪些溯源/反制的操作呢？

1. 1. 可克隆相关系统页面，伪装“漏洞”系统，以此进行反制。常见的有git反制、svn反制、goby反制、cs反制、还有一些应用的 0 day和 n day等。
2. 2. 可克隆相关系统页面，伪装内部应用下载，以此诱导攻击者运行网站的木马程序进行反制。
3. 3. 互联网端投饵，一般会在Github、Gitee、Coding上投放蜜标（有可能是个单独的网站地址、也有可能是个密码本引诱中招）。
4. 4. 利用JSONP、XSS、CSRF等前端类漏洞获取访问蜜标的攻击者网络身份（网络画像）。

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAM0XukdF1WVcTqQeiamyBPdUP9oe4R4e22fpIiaKtLQelcUgF6BZjibg4w/640?wx_fmt=png&from=appmsg)

### 溯源社交平台到验证身份

所有的社交id都是为了得到 攻击者手机号/网络ID 以便于进一步得到攻击者详细信息

例如网络id可以拿到Google、Github、各大src等平台中访问搜索。

百度、微博、qq号都是可以尝试查看发布的公开信息的。

例如百度可以通过 baidu贴吧 --> qq号 --> 手机号 --> 支付宝查询真实姓名

良好的案例：

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAmWP6EFIW4gGXddodjLIyCmn8mwhgH6B4J9ib547O198h8WbNSITibWow/640?wx_fmt=png&from=appmsg "null")

百度贴吧的回帖中发现红队老哥泄露了自己的联系方式

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAeiczDdP4b1E3qO89MPUqIFtQ4NKkPnha0KYtXC5xwnwspqtc96Ow2KA/640?wx_fmt=png&from=appmsg "null")

搜索QQ查看一些基本信息

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAJQbFIdE7eic6GdECezXHlbhB6myxE1X09UiaZzKmTSpvI8F2kE61ia6ZA/640?wx_fmt=png&from=appmsg "null")

SG库检索QQ号获取到了手机号

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAKpGsZaz7UUQD796XgcmAkBNvV1MlWsVGmekFGXpfdlXe1CwiaHSibcTw/640?wx_fmt=png&from=appmsg "null")

手机号检索到了微信号、脉脉等信息

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAXR7xc8obyt6ricujzh7rLjlFkV6DQthUxsXbdP6O5IsHsWkEicoVxBsA/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicALFs39hkicqtF7BjR0TdspXlzxRE8AffMibyD0rT6w9RExVtBsroQFdiaw/640?wx_fmt=png&from=appmsg "null")

支付宝转账验证，得到真实姓名

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicALlITiaSTyGUUOnEVWEnlTXOQPpIxvh1icDyw97rl6RKkT2k1OxUojkyQ/640?wx_fmt=png&from=appmsg "null")

如果是打马中间四位数的手机号，可以去找找在线去空号的接口，或者付费去空号。

得到可用手机号之后，再给安卓手机批量导入剩余非空号的号码，去脉脉、百度贴吧等地方查看攻击者的详细信息，筛选定位出具体的攻击者。

手机号可以通过支付宝转账获得攻击者的真实姓名(可配合银行卡转账信息)，得到完整手机号。

通过在线的各种信息检测接口来得到更多的信息。例如:https://privacy.aiuys.com/

![](https://mmbiz.qpic.cn/mmbiz_png/g1X9cMsc6D12oDlL3EWticXW5ftUKQmicAwbbs0R5tGhAeFQfjPicppJty8mxlGYGwcJQ8CrezX3LW9SibDzDRWsAw/640?wx_fmt=png&from=appmsg "null")

得到进一步的更多信息，坐实攻击者身份

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PrTu58FA79arIQGU74rJvbDtBoicQlQ8rMIzfax1Ol2RY5YnbsN82PLkvicB9FLHxFibrF5k7x2N7VXicectIVucibg/0?wx_fmt=png)

暗影安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PrTu58FA79arIQGU74rJvbDtBoicQlQ8rMIzfax1Ol2RY5YnbsN82PLkvicB9FLHxFibrF5k7x2N7VXicectIVucibg/0?wx_fmt=png)

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