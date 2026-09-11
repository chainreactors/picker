---
title: 惊！“0交互”被入侵现实案例：语音没接微信就被接管&amp;打印机还没工作就被控制
url: https://mp.weixin.qq.com/s/_AUDe9ijGEDYJjo4zOWgOQ
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:48:35.938875
---

# 惊！“0交互”被入侵现实案例：语音没接微信就被接管&amp;打印机还没工作就被控制

# 惊！“0交互”被入侵现实案例：语音没接微信就被接管&打印机还没工作就被控制

原创

打印机安全
打印机安全

打印机安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

先说明一下：你看到这篇文章时，腾讯官方已经在服务器端更新了服务，所有用户都可免遭其害。

复原一下这个漏洞案例：

你的微信语音响了，几秒后，微信就被另一端拨打语音的好友控制了，他可以读你微信的消息、代你发消息，再用你的微信向你通讯录里的另一位好友拨打语音，再控制你这位好友的微信。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6liaItc9B4ZicJk62vC8lIVxictz6OXBaJicNoJ3ryhMMy4gVBCe34a9fXsoFpQxVcYsts4Il7x0v5ibJJucC8OKOPQwahWiaiago4Cy9E3W012Jgo/640?wx_fmt=jpeg&from=appmsg)

这不是什么科幻场景，这是实实在在发生的案例，不分系统，Android和IOS都可以。

但这里有个前提：拨打语音的这个人必须是在你的通讯录里好友。

美国加州网络安全公司Calif于2026年7月验证了这个概念场景并向腾讯报告了该漏洞，腾讯8月份在服务器端进行了修复。

类似的情况也会在打印机上发生

2026年5月，某国外品牌\*\*生 L14150型号打印机，固件为FL27PB，可以被精心构造的打印任务破解。

现实的场景就是：打印机在那里好好的，打印一堆乱码后，就不能打印了，局域网的其他设备还在被这台打印机攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6liaItc9B4ZicpdU2MGBsMeZ8oR73xUJWib37XEBYpzfqnLhfiaDs5aZrUJKdHFOPcxAmAkLFydFHNSVWA0gX7Dqz4amibNpCxDWI0pN1LuvaV4E/640?wx_fmt=jpeg&from=appmsg)

基本原理是这样：

打印机有一个开放的端口，叫9100，打印机上对应运行的服务叫RAW。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6liaItc9B4Z8hukuS9aiaR3bspPcibVMglxNsScXnoZBz6WwGFXuXCqlyuFibTgAnqvCA2us4sXnoPzjJr6jx4Dk2icfdPceYEYERI5U7gdt4p0M/640?wx_fmt=jpeg&from=appmsg)

RAW服务的任务是：只接受电脑或者其他设备发过来的打印任务，不反馈，接受任务的窗口就是9100。

用收快递类比一下这个过程：

快递员直接把快递从窗户（9100）扔进你的房间，你在房间里收快递（RAW服务），你也不拆，你把快递就交给下一个房间的人去拆（解析打印数据）。

问题出在收快递的空间，正常的快递，你的房间够堆放这些快递，规则而有序。

漏洞发生的原理是：

快递员给你的快递是精心设计的，这个快递超出了你的房间尺寸，你就得借用其他的房间的空间来堆放这个快递，而被借用的那个房间，恰好是整个房间的控制室，这个快递导致整个房间系统罢工了 or  快递放在了房间系统的控制器上（远程控制）。

这个漏洞已经被编号为：CVE-2026-39047,严重程度被评为高，评分7.6。直接导致的后果是打印机拒绝服务和打印机无限重启，同时也可能导致执行任意代码，取决于固件的内存保护机制以及攻击者绕过这些机制的能力。

![](https://mmbiz.qpic.cn/mmbiz_png/6liaItc9B4Z96gInUtthgqC2GIcB1HUtg27f2fE4yeQXQvYpuul3atnYPqjSp8ic04eJKgp1q4Xics8ZzYZa4Ul4AFWJq1EVR6GwZsbRaUibViag/640?wx_fmt=png&from=appmsg)

你的打印机9100端口安全吗？

9100端口的特点，使得打印机一直是一个沉默而被动的接受者。所以如果有一天你的打印机拒绝打印了，有一种可能就是9100端口拒绝服务了。

来测测你的打印机9100端口？

附赠9100端口测试代码，python环境，需要pip安装几个moudle，代码自取，不谢！

-->测试代码，点击链接获取代码：CVE-2026-39047-main.zip

参考链接：

https://www.esecurityplanet.com/artificial-intelligence/news-ai-wechat-worm-billion-accounts-apac-china/

https://www.nytimes.com/2026/09/08/us/politics/calif-ai-worm-wechat-hack.html

https://www.sentinelone.com/vulnerability-database/cve-2026-39047/

https://www.linkedin.com/posts/azhari-ramadhan-610030136\_cybersecurity-redteam-iotsecurity-activity-7461210985123483648-ebih

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TeIldibXx0Qk3WFficqIB2ksTRbFiawe9toURBGn2QoN0trWKdeBKbWMpFzYA7pbia57KLibKRPuOK7YHH0e3ykcxVw/0?wx_fmt=png)

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