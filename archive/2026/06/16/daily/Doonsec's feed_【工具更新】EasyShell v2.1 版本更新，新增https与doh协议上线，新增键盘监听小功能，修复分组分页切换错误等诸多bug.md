---
title: 【工具更新】EasyShell v2.1 版本更新，新增https与doh协议上线，新增键盘监听小功能，修复分组分页切换错误等诸多bug
url: https://mp.weixin.qq.com/s/RpFkRKBgJ9LlKUIiI4FiCw
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:00:57.545675
---

# 【工具更新】EasyShell v2.1 版本更新，新增https与doh协议上线，新增键盘监听小功能，修复分组分页切换错误等诸多bug

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XfO0XCNPrNruicVhcZjOpiawDNpVVcmiaawM8C8CS01ibHH04kq9OlL6IlUDg835JpkIRduuCLYicnJ8BqiazFpuNibJvH3vX4m69qgqrWRolqv2Ik/0?wx_fmt=jpeg)

# 【工具更新】EasyShell v2.1 版本更新，新增https与doh协议上线，新增键盘监听小功能，修复分组分页切换错误等诸多bug

原创

沐寒
沐寒

渗透云记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责声明**

由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJZJ4pVQHOicqtkQntqLduTfPaVvVnZ4iaGc0DaBeQqNoicYUrzzyOpIsJWbSgNUqV3SodRwKFOIq3Lw/640?wx_fmt=png&from=appmsg)

欢迎关注本公众号，长期推送技术文章

## 前言

感谢各位师傅们的热心测试，发现了诸多bug，目前已经修复的有：

1. 新增https、doh协议用于上线使用
2. 新增windows的键盘记录学习小功能
3. 新增mysql作为数据库数据源，默认还是sqlite
4. 修复主机列表分组切换分页错误的bug
5. 优化客户端流量特征

## 展示

1. 新增https、doh协议

目前已实现协议8个，分别是tcp、kcp、ws、http、https、doh、dns、oss

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNrZGESetubXiccc5HUmj7OWicHpHejlXY0Df0VPToWj55hFYOibiaicX6ZloibG0MicEwzwr61iaxLeYZia9lhpEqaK2g9tPNld7CtFY39o/640?wx_fmt=png&from=appmsg)

2. 应各位师傅的需求，键盘采集学习小工具已集成，可以简单娱乐使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNqz1jZc9yV914qiaU4iaVgSJ2b7m6DHC9ujYa2ViaPgwODfNJicBTArfAjpxnibJeMMoiazQfPia84j6ToCcgrbpMC2eAdmYia0XOU2Qhk/640?wx_fmt=png&from=appmsg)

支持注入键盘内容到对方屏幕

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNq7M3voorgRYs9tcG0sf7E0oLZvS7fnyZZ9K6FxpJOOTDolHXBuMtVVXPj9rnKLRb5E3CBoqh3UxDzP9sqlRWoQQlcGo99WR88/640?wx_fmt=png&from=appmsg)

## 展示

往期版本测试效果，一镜到底

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLbE8HiaQapVkBwypwXhsmWWEwZyOx2Frhw9bDjyRnVSMtubJkZJY9NX2Hw8Igx7fDmuZnYXzPUvDA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azK0JBUq0N1g9hpXvZiaWm32V2kibRficfdehadlNxb8ibickibcgHFOr9FXF5qibRy3pDw984iaZP8InvejUQ/640?wx_fmt=png&from=appmsg)

往期精彩：

[EasyShell Extensions 脚本菜单 — 用户使用手册](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484902&idx=1&sn=4f9096c77e3e2417eded3a064529a4b9&scene=21#wechat_redirect)

[【工具更新】EasyShell v2.0 版本更新，新增网络拓扑探索，优化内网多级网络上线，修复shellcode无法加载等诸多bug](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484898&idx=1&sn=5a39f358de3b7e7be791cc76a6c95fa8&scene=21#wechat_redirect)

[【工具更新】EasyShell v1.9版本更新，修复存在的bug，提高程序稳定性与免杀能力](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484879&idx=1&sn=6176e276171325ea1ab307f427745a28&scene=21#wechat_redirect)

[【工具更新】EasyShell v1.8版本更新，重构客户端，减小体积的同时增强免杀效果](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484870&idx=1&sn=3c0b1706d8e0ca389b8e56c33a16103b&scene=21#wechat_redirect)

[【工具更新】EasyShell v1.7版本更新，修复诸多bug，同时新增诸多新功能](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484859&idx=1&sn=55dfff811f27f24c3d35ae3b6f3e6ace&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLapsPaDZpneu1VjNTprA9zO5DTQcutB6EHJnCOFoeFYnrHcHqxxeIfHYQJSzMNibZOu85xuRAYVOQ/0?wx_fmt=png)

渗透云记

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLapsPaDZpneu1VjNTprA9zO5DTQcutB6EHJnCOFoeFYnrHcHqxxeIfHYQJSzMNibZOu85xuRAYVOQ/0?wx_fmt=png)

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