---
title: [工具教程]Burp 光标瞎飘？这篇教你彻底搞定
url: https://mp.weixin.qq.com/s/vV0aUsx0eGnpAYq69Q8oMQ
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:34:53.358120
---

# [工具教程]Burp 光标瞎飘？这篇教你彻底搞定

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icCLY10D8tvLicOgMS4ZCibWVyoHSQgMY0KbENxxc23AQL9xFxZR3EAOBTjvSm4SlYao6YyDPWma477RAFVMAjttAkZK3PPPV6GFRibNr2pezJQ/0?wx_fmt=jpeg)

# [工具教程]Burp 光标瞎飘？这篇教你彻底搞定

原创

Elon
Elon

好靶场

![]()

在小说阅读器中沉浸阅读

> 💡 好靶场
>
>  团队宗旨：我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。所以我们团队名称就叫“好靶场”。

---

我们承诺每天至少更新1-2个新靶场，好靶场追求的是稳定日常更新而不仅仅是数量。

---

## 1.好靶场介绍

**官网链接http://www.loveli.com.cn/**

> 零基础入门不迷茫！ 专属网络安全从零到一体系化训练——配套完整靶场+精选学习资料，帮你快速搭建网安知识框架，迈出入门关键一步！ 全场景实战全覆盖！ 聚焦Web渗透工程师核心能力，深度拆解TOP10逻辑漏洞，精通PHP代码审计、Java代码审计等核心技能，从基础原理到实战攻防，覆盖行业高频应用场景！ 真实漏洞场景沉浸式体验！src训练专题重磅上线——1:1还原真实漏洞报告，让你亲身感受实战挖洞流程，积累符合企业需求的实战经验！

🚀哈喽～各位宝子们周一早上好~~👋！做渗透测试的小伙伴大概率都遇过这个糟心问题：BurpSuite 里光标和鼠标点击位置对不上，偏移错位严重影响操作效率，敲代码、点功能全靠 “盲猜”。其实这个问题根源很明确，解决方法也超简单，今天就把 3 个亲测有效的解决办法整理好，小白也能一键搞定！以下的详细内容👇

## 2. 详细教程

光标错位移位问题是因为系统高 DPI 缩放（125%/150%）和 Java 界面不兼容，导致鼠标点击位置、光标位置和实际显示位置对不上，出现偏移错位。

## 解决方法1

打开burpsuite的 **“Settings”**

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvKF5GdQ7QiaVOyLVjQ7GkvcXBf7C7SebjRExSwAMia2DmCAl3iaia79EZRicZ3gPKPznj3KYeV2d2yz4yianF6A0oPGGicKAgmT6xhq0M/640?wx_fmt=png&from=appmsg)

来到 **“User interface”** （用户界面）点击 **“Display”** 来到 **“Scaling”** （缩放）的 **“Configure scaling settings”** （配置缩放设置）选择缩放比例“1.0”，然后重启burpsuite即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvJ01l7AERzfdfkqibLoP1JxfcgChQVtXrA7zfwzlE7WicjUZNp8EOz0gSHNw2d6oIyPEBp0wjDhiadLd2icyU7FxibCf1oibwbmJticJY/640?wx_fmt=png&from=appmsg)

## 解决方法二

在启动脚本中 :后面加上参数 **-Dsun.java2d.uiScale=1**即可需要记住 **（启动burp之前的位置添加）**

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJg9icYVQequtQHf1olyicgX3ShWzzdbtQIMiam5lm4R2r3nBibfibic54VgSXbicR7wtiaAC4At57IFDKNrr02Eu2W1bkeFylGjiceOfE0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvL7C3ic5z52DwzMZm3As9WJOnSEMQXnR3Ztn8JkN34IrFeiaUoKzfaic8eRn0J8ib16omdhztZoAOIrlH6I7tSzs64pKgWSG7OUsXg/640?wx_fmt=png&from=appmsg)

## 解决方式三

在 **“Settings”** (设置) 点击 **“User interface”** （用户界面）选择 **“HTTP message display”** 在设置里修改字体的大小，修改到内容不在出现burpsuite不在出现光标错位。

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvKqx1Bl5Jhxe9nATB990I4wH2icroAwnOGqjKqbUftGhBy4IYQKCaROrvv3OnEbP12mKPiaFSvGZye50OrQsicAcR9tUC7ib5PEQ94/640?wx_fmt=png&from=appmsg)

## 3. 如何使用好靶场

首先关注“好靶场微信公众号”然后发送bug，可以点击链接直接登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvJn80Sicpic7OmticxNKsrrgJFTNUhAftHBnCibiaicLFUCB8ehvyT0PrXEG4lDcsnvDLAqJSBQlHz0V4F8SIF5gpO9iaNiaH97PBFjQRw/640?wx_fmt=png&from=appmsg)

## 4. 福利

福利1： 找到个人中心，邀请码输入0482d6d28539424c，白嫖14天高级会员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLCicFgYymsZVpugibO1C8AVsib8XicsA53jA7a050c434b35AhxXQHcdCOzjtRl9N3GpUzIsFdNXY0rh56Mll8dmpKNJIib98uZvibQ/640?wx_fmt=png&from=appmsg)

福利2： 关注好靶场bilibili。拿着关注截图找到客服，领取5积分或者7天高级会员。

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvIicU6vDElyplQWIXkDdgNCmMkL9xCMOx9EsUKtNN4OhyBrAGbMo3QkpzFS5OP8ETAdLenHsJAjz3XCVrfnBSu186zyaqERbsLk/640?wx_fmt=png&from=appmsg)

## 5. 每日限免

每日限免 为了能让更多的宝子可以免费的开启会员靶场，我们会在工作日随机开放一些靶场的限免，还请加群关注。

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJguqkEichc2zwjCTwfQsl8FW56dZAlNmdDAbLVarx22icu0Y6sJibk94vBBoibkNU3htXEknvAVQQCObYtlB51hatQab1ibRp13a98/640?wx_fmt=png&from=appmsg)

我们会在微信群、QQ群每天更新限免靶场，以及免费学习资料；任选一个群添加即可，所有的通知都会到位在交流群通知，请添加好友，我将邀请你加入“好靶场内部交流群”

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvKvSCywPlC90S8mWg9fr8xxhWShHvJ3z1njibcmLCFHchA6Xl70fByLuek75ZgF8uUR5r8wqQJT730tcQvzD7ATHIdIibj1Yq3Io/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvL62Jib8LO4pnzu27PofUnice4tk9fv57UjsK6dySBood4KOYYIyqcyzG8xdksv5hWMltXV27rSiaQBoXbQd4scwms3D2oXp5PX3A/640?wx_fmt=png&from=appmsg)

## 6. 好靶场AI客服机器人

为方便学习还有提问，我们设计了好靶场Ai客服机器人，可以完成简单的客服能力，以及好靶场日常靶场提醒更新、根据你的询问推荐靶场

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJWgicVJZCqicFqHryHf2oekbyLAic3fkgiaibJeZF3sofXCBPJj1EokyFA6CWGqoah7K5wGP9fGgRbXrof4QwkGm8sFV8PLUZlBdicA/640?wx_fmt=png&from=appmsg)

> “噜噜大王”正式上线

大家点击左边的快捷工具，有一个AI助教功能，然后点开就可以和噜噜大王对话啦，由于是内测期间，仅限于年会员才可以进行使用。还需要进行微调，会随着大家的使用而进行优化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvIvott8QpOguxQruTFVFO5sgS6tk4TA66xq9LdzicO8micwPRGWPKgzse4ibp2z0xp7bSJ32aoZDCRbaUfHenFeQglcR1PnAW70zs/640?wx_fmt=png&from=appmsg)

你可以尝试问一下关于打靶场的问题

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJHOE1iahc0JD1gdSF2P2UwOuYOwia2WcGcZI3qXc2r1pSNbCuLlQxiaCzy89nwdpicOGI7lbkkGWgd8GXPAtAwO2K5icVaFnMOaeeY/640?wx_fmt=png&from=appmsg)

## 🚀好靶场会员订阅

好靶场会员订阅 首先点击会员订阅 ，然后选择对应的套餐 ，选择对应的会员去支付 ，支付完成后即可会员到账

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvLicRSPx4NXENbaPVxeF2rLIuyHArtS8HOoIM8TfID3wFxo8icSQDQasMxnqU9QbjfXskbHibKgHbeVBw3nBZ21L65YekWYnt4xUA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJcatqLTdbqI1MI6wP5uKCiagTMKqQOvHlrRI5nIGzOg4nzIKIwfOBruOVe7cSNK7T29SwAyUY7f0tMTuqicl4aKUBAGJKPKa3A0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJkQZQagkapGxPmA54TpyG9ic1NiaMQlhCdpKSVPMGuDZiaiaAZBHrD35MqBAb3DaOxiaDe4FZgUhFwOrDpUxrcKH6AzzS1KK3xnibVc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLqz0Ib7Km2ibLlJRMh5P4mxCyIticKBGMYVQdzCESabI8o64l24pyhHgOdoupK1EuykUMJdgNJAwJFYsnQjmNibuXVvQPp182M6o/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvK2C7klp7wKKhoR7iamhAw3AVsjpcIvpHzC5YZWjhMSQ6s5sWRLqawfkh3SXcMGw99vGgwRBMkGeA/0?wx_fmt=png)

好靶场

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvK2C7klp7wKKhoR7iamhAw3AVsjpcIvpHzC5YZWjhMSQ6s5sWRLqawfkh3SXcMGw99vGgwRBMkGeA/0?wx_fmt=png)

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