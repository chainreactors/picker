---
title: 【安全圈】微软确认：Windows更新出现新Bug！直接没法关机
url: https://mp.weixin.qq.com/s/hGLfA0Mv7toaE3AUVBw_fw
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:34:35.452088
---

# 【安全圈】微软确认：Windows更新出现新Bug！直接没法关机

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgxsg8sFQ3uicr3g7sUibeibzGQ2lNicOSJjrcKcibcZ9wxJ6KLQibvVJibLZrxQJxEpzokhWBBTtpiaYjEXw/0?wx_fmt=jpeg)

# 【安全圈】微软确认：Windows更新出现新Bug！直接没法关机

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

bug

微软在其官方网站中确认，部分设备安装了2026 年1月累积更新（KB5073455）后出现了一个Bug：部分设备在尝试关机或休眠时，会自动触发重新启动，导致用户无法正常关机。

根据微软的说明，受影响系统版本主要是Windows 11 23H2的企业版（Enterprise）或物联网版（IoT），并且开启了System Guard Secure Launch（系统保护安全启动）功能。

这一功能本意是利用基于虚拟化的安全技术，保护系统在启动过程中免受固件级攻击，但在最新的安全更新后，该功能却意外干扰了电源管理指令。

目前，微软尚未发布正式修复补丁，为受困扰的用户提供了一个临时解决方案，受影响用户可以通过命令提示符执行以下指令强制关机：

shutdown /s /t 0

需要注意的是，目前休眠功能尚无临时补救措施。

微软特别提醒用户，在离开电脑前务必手动保存所有工作，并采用上述命令关机，以防设备因无法进入休眠导致电量耗尽或非预期重启。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgxsg8sFQ3uicr3g7sUibeibzGlVYVcdGfUtkiamGoAKQiaC1X0DaB7mZv02wr2ASSancT7TbtJPiaZtfzw/640?wx_fmt=jpeg&from=appmsg)

***END***

阅读推荐

[【安全圈】腾讯FPS大作突发崩溃引热议！玩家抱怨:网费谁补偿？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073743&idx=1&sn=d569c1593013a127f457b74734010c74&scene=21#wechat_redirect)

[【安全圈】数据泄露蝴蝶效应！外卖平台惨遭黑手](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073743&idx=2&sn=2608532ec97f40796a2f1f6f05a4ad87&scene=21#wechat_redirect)

[【安全圈】美国最大运营商 Verizon 服务一度中断十小时、波及数十万人，官方承诺补偿](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073743&idx=3&sn=68404eced1fbed01846f09613e81f0e2&scene=21#wechat_redirect)

[【安全圈】俄语黑客伪装以色列组织，Sicarii勒索软件实为假旗行动](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073743&idx=4&sn=f07e381df80a18c3eb1b66f071e961b2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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