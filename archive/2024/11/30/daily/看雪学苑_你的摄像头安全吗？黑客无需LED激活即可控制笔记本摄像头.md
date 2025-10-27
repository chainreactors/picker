---
title: 你的摄像头安全吗？黑客无需LED激活即可控制笔记本摄像头
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458584586&idx=3&sn=ade97df00fb3e264d2a7d77b3a81ff67&chksm=b18c368086fbbf963462d38ae5a9dc99bac905571106ee896ecfcddad18ebcb5a60ab657bef2&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-30
fetch_date: 2025-10-06T19:16:16.999086
---

# 你的摄像头安全吗？黑客无需LED激活即可控制笔记本摄像头

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EEoP87icqNvOd9jAibJHwnO4Ekj9rCNpJS59wQxW34DTA8ETiaEJE3HJ4pAMsicJU3KYgDTzBvFzANvQ/0?wx_fmt=jpeg)

# 你的摄像头安全吗？黑客无需LED激活即可控制笔记本摄像头

看雪学苑

看雪学苑

随着技术的发展，个人隐私保护变得越来越重要。最近，一项新的安全研究发现，黑客可在用户不知情的情况下激活笔记本电脑的网络摄像头，这一发现引发了公众对个人隐私安全的广泛关注。

安全工程师Andrey Konovalov，以xairy为名在GitHub上活跃的Linux内核安全工程师揭露：**他发现通过刷新Lenovo ThinkPad X230笔记本电脑上的网络摄像头固件，可以在摄像头本身激活的情况下独立控制其LED。**这意味着，即使摄像头的LED指示灯没有亮起，黑客也能悄悄激活摄像头，从而监视用户。

Konovalov开发的这一工具，使得对ThinkPad X230上的摄像头LED进行软件控制成为可能。尽管这款笔记本已经有十多年的历史，但这一发现在技术社区引起了热烈讨论，人们开始质疑为什么摄像头和LED指示器不是硬连接的。

通过对几台笔记本电脑的改造，Konovalov能够开发并刷新自定义固件。这一过程中，他不得不以十六进制转储和分析控制器的SROM（只读存储器），并在没有任何文档的情况下反汇编代码，以找到负责流式传输视频和启用LED引脚的位置。

联想对这一发现发表评论称，X230等较旧的EOL系统不包括固件更新验证。然而，自2019年以来，联想的图像处理器已经包括对相机固件的数字签名检查，并支持具有写保护的安全胶囊更新。

Cybernews的研究人员指出，类似的绕过摄像头LED指示灯的攻击过去已经发生过多次。他们强调，攻击者可以通过在受影响的笔记本电脑型号上安装恶意软件，在不被发现的情况下监视受害者。

这一发现在GitHub上引起了广泛关注，人们担心，所演示的方法可能会影响许多其他通过USB连接摄像头并允许刷新固件的笔记本电脑。用户强烈表示，LED指示器应该连接到摄像头的电源，或者是摄像头的“启用”信号，而不应该通过任何固件操作。

在现代计算机中，尽管存在更强大的基于硬件的解决方案以确保LED在摄像头使用时始终亮起，但**许多人更倾向于设置摄像头物理硬件开关（直接把摄像头贴上何尝不是个好法子），**以绕过任何基于软件的指示器。

资讯来源：cybernews

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

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