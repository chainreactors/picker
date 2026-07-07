---
title: 【工具更新】EasyShell v2.3 版本更新，1. 新增win进程注入、2. 优化页面布局、3. 修复kcp协议偶尔离线的bug
url: https://mp.weixin.qq.com/s/_en_gHzSt27fwLrw4G5Bew
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:01:11.424763
---

# 【工具更新】EasyShell v2.3 版本更新，1. 新增win进程注入、2. 优化页面布局、3. 修复kcp协议偶尔离线的bug

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XfO0XCNPrNqBNLmvlwkuzCIDKw15K7rftAmjEGIGVFGmBz3jm3X3aPGHy04o88NoqRLHI9yPsyNQSeic015JWBibF10QsVxOOXk5keL4EbnRE/0?wx_fmt=jpeg)

# 【工具更新】EasyShell v2.3 版本更新，1. 新增win进程注入、2. 优化页面布局、3. 修复kcp协议偶尔离线的bug

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

## 更新说明

感谢各位师傅们的热心测试，发现了诸多bug，目前已经修复的有：

1. 新增离线主机心跳包重新校验
2. 新增win的进程注入与迁移功能
3. 优化前端布局，合并日志中心与系统管理标签，合并备忘录与下载管理标签，支持标签页拖拽，拆分主机管理为单独标签页
4. 优化默认win生成图标逻辑，避免每次生成图标一致被标记
5. 修复了一些额外的小bug~~~

## 展示

更新之后的操作相较于之前稍微丝滑一点，以前点击交互式shell之后，在想查看主机列表需要新建浏览器标签，在热心师傅反馈之后，现已更新为独立标签页进行主机管理，感谢ZZH师傅的反馈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNrjvDM0pv1iaosN2dtJlSVc5cqlwicw3UbQ8uOE6o2GvpDGsxrUwft8F0icGHahkgGgBVfwUia7IhILnicvEUPRNIibtFHo8PUcJd71Y/640?wx_fmt=png&from=appmsg)

优化了一下顶部菜单的布局，避免顶部菜单展示冗余，具体修改如下：

1. 将下载管理与备忘录进行合并展示，放在了辅助功能内；
2. 将系统管理与日志中心标签进行合并，放在了系统管理中；

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNoD7CHgvuic0ZsbdH2WMeOic40EYibv9w1mMYLebwbu9XQna653GSkibLuqUF1t7OMgAyA1qnorUmp2k0u61cj4kVHFkjv4TkQwbXQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNqQIEGsyiaCRYQ4JhqSJgDSTODv8CyXVOJvoZSgJ1asMicuWyuealiac1KZ8bqVd9KTrvjrSicV6flMzJibUltotUqUVicl6jXpYUzL8/640?wx_fmt=png&from=appmsg)

至于之前有师傅反馈的图标被标记，存在qvm告警的情况，现在在生成的过程中会随机变化，保证每次生成的图标均不一样，不过肉眼直接看的话，区别不是很大，不过程序进行计算的时候，值肯定是不一样的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNpMQKyF18THH1sm0wOWk6fz8K8DMTpKUkicLdL56tPhXN8yae8q5WnyswVVw62qmiaERcBASqUAPTXLSn6dassm7jxUzuxeI7yA8/640?wx_fmt=png&from=appmsg)

进程注入的可以直接看以下视频进行了解

## 更新后的部分效果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNrDicsKkUJLhUlj7IseoLNLicYEXpAfvNL2FUYiazOd0U7oTKDuBXxlS2mDmeN0TVdxCD91AVom9m2EJck5hzbC7GVIARTMcw8qrA/640?wx_fmt=png&from=appmsg)

屏幕截屏展示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNpJmZxlKXITofVaBdDMBeK3ic3kEWLnoOIwCk24yry6znudIagNjqUhpDM0CIq1KG65nibcOFnOloNVN6HqJspDKY0lllsWGuqFc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNrAoxoxY2voAfV4uC36ZrCyXs1XXNwLdjicRrW9uQKgA4IiaibTXyNIUo7qWxPjjFsVaI2g8hBWC2ibJbLTPcH76OIL7rsxUxhLPXk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNqqcv39ZVbf7jrYKgnayvWkZtZFbbkicgLWNO1djQBhGME3zsALpAXU5yDaBSwzuSFFAVicoNC99NzX88jiaCBibtiajmtnJiaPtGDaY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLbE8HiaQapVkBwypwXhsmWWEwZyOx2Frhw9bDjyRnVSMtubJkZJY9NX2Hw8Igx7fDmuZnYXzPUvDA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azK0JBUq0N1g9hpXvZiaWm32V2kibRficfdehadlNxb8ibickibcgHFOr9FXF5qibRy3pDw984iaZP8InvejUQ/640?wx_fmt=png&from=appmsg)

往期精彩：

[【思路学习】EasyShell实现进程注入](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484938&idx=1&sn=2c04313f3ed4013527274a510ae62da8&scene=21#wechat_redirect)

[【工具更新】EasyShell v2.2 版本更新，修复企业微信上线提示失败、文件下载队列调度与全链路静态编译](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484928&idx=1&sn=312a618945448f7944f81adf7bc63852&scene=21#wechat_redirect)

[【工具更新】EasyShell v2.1 版本更新，新增https与doh协议上线，新增键盘监听小功能，修复分组分页切换错误等诸多bug](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484909&idx=1&sn=dd2a1603aa327f2dc70e0af2d55ad4df&scene=21#wechat_redirect)

[【工具更新】EasyShell v2.0 版本更新，新增网络拓扑探索，优化内网多级网络上线，修复shellcode无法加载等诸多bug](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484898&idx=1&sn=5a39f358de3b7e7be791cc76a6c95fa8&scene=21#wechat_redirect)

[【工具更新】EasyShell v1.9版本更新，修复存在的bug，提高程序稳定性与免杀能力](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484879&idx=1&sn=6176e276171325ea1ab307f427745a28&scene=21#wechat_redirect)

[默连(morelian) 简简单单的webshell管理工具(支持常规的代码执行，文件管理等，默认支持http与socks代理，支持gui与浏览器两种运行方式)](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484811&idx=1&sn=cb2d380da6d800639e7a1227c2473a40&scene=21#wechat_redirect)

[EasyTools渗透测试工具箱V2.2.2更新(1.新增云上安全，支持oss存储桶扫描、云存储管理与云服务管理;2. 修复数据库连接bug )](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484786&idx=1&sn=f5e7954a9de25cf2439d2a88de364383&scene=21#wechat_redirect)

---

鄙人的一个小博客 渗透云记，

官网地址：www.encenc.com

博客地址：b.encenc.com

目前已集成EasyTools渗透测试工具箱的登录，Webshell\_Agent AI自动生成平台的登录等，一个账号，多平台联动使用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfO0XCNPrNp9BQdQktUDmvnN1f7cxx13Dq6eYK9t8K9GVpMoAbjaSKZhgWoTNOW3L2f834uCbMrC0IYEZGlNExQ6l64KWibyq3gW4q7Dic0tA/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

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