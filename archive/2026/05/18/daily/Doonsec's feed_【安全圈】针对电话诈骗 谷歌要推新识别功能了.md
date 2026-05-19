---
title: 【安全圈】针对电话诈骗 谷歌要推新识别功能了
url: https://mp.weixin.qq.com/s/rO_5jm5QmJo8GzeDuJaU8g
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:01:14.990723
---

# 【安全圈】针对电话诈骗 谷歌要推新识别功能了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHEZl1OJKdvDmvHYHk4CIQQntRCqzJH49Vyfj00PEtXNt4EjxqRh0HtC22xEqxLjvgbjIw3Av1DAbhb033Z5DZJUrq96Z2aoss/0?wx_fmt=jpeg)

# 【安全圈】针对电话诈骗 谷歌要推新识别功能了

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

谷歌

据科技媒体 Android Authority 今日报道，谷歌正在为 Android 系统电话应用开发伪造电话号码识别功能，在诈骗袭来时提供预警。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyHBojBFcBxukh1CzZt3k4vibLhSNYdy2Aicuz8MtpfsItnVu7gwocqudohBB2vcFfMysLHiazkgRfWL7xYic95blbibicfDWhR8ZLib6I/640?wx_fmt=png&from=appmsg)

据报道，谷歌的电话应用已经拥有垃圾电话防护、号码识别和来电筛查等功能，可对抗营销骚扰电话或诈骗电话。

该媒体首先拆解了 Pixel 手机最新版谷歌电话应用（v222.0.913376317）的 APK 安装包，发现伪造电话号码检测功能相关痕迹，安全圈附代码如下：

```
<code>&lt;string name="incall_contact_checker_alert_title"&gt;This may not be %1$s&lt;/string&gt;&lt;string name="incall_contact_checker_alert_default_title"&gt;This may not be a real caller&lt;/string&gt;&lt;string name="incall_contact_checker_alert_description"&gt;"Someone may be pretending to call from your contact's number"&lt;/string&gt;&lt;string name="incall_contact_checker_alert_end_call_action"&gt;Hang up&lt;/string&gt;</code>
```

从上述代码来看，谷歌电话应用未来可在检测到伪造电话号码时提醒用户：“有人可能正在伪装成 XXX（安全圈注：联系人姓名）拨打电话”，**并提供挂断选项**。

事实上，伪造电话号码实施诈骗并不罕见，骗徒会通过技术手段，**让来电显示一个真实存在、甚至已经保存在用户通讯录里的号码**，但实际上，真正拨打这个电话的号码并不是屏幕显示的号码，而是另有其人。骗子正是利用了熟人的信任心理，攻破用户防线。

此前曾有传闻称，谷歌正在开发一套电话号码验证机制，自动验证电话号码的真实性并识别虚假号码，必要时直接挂断通话。但无论如何，Pixel 手机在处理可疑电话方面已经拥有不错口碑。

***END***

阅读推荐

[【安全圈】苹果最强安全防线，5天被AI攻破：网络安全进入新纪元？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076557&idx=1&sn=70a591aae8a5b83007bbeb32779f881d&scene=21#wechat_redirect)

[【安全圈】黑客利用 Burst Statistics WordPress 插件认证绕过漏洞发动攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076557&idx=2&sn=0e78da0c84763775c4cc537dd3b7ea92&scene=21#wechat_redirect)

[【安全圈】黑客利用 Burst Statistics WordPress 插件认证绕过漏洞发动攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076557&idx=3&sn=c636faff278cae3d93f0d1ff35483775&scene=21#wechat_redirect)

[【安全圈】Linux内核漏洞"ssh-keysign-pwn"允许攻击者窃取SSH密钥与影子密码文件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076524&idx=1&sn=85724f6aa9c493a3823cc2988e73c7ec&scene=21#wechat_redirect)

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