---
title: 网络安全知识小讲堂 | 四万台设备的指挥部，没有固定门牌
url: https://mp.weixin.qq.com/s/_Spxr-NgrFCKSccEqGsrUw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:59:10.249278
---

# 网络安全知识小讲堂 | 四万台设备的指挥部，没有固定门牌

# 网络安全知识小讲堂 | 四万台设备的指挥部，没有固定门牌

原创

武汉网络安全
武汉网络安全

武汉网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn6xia9ep49RicrT5OEnGGic4KZ4TaJucHxwTyU8G2DFHrKz3vgE69yKzy7kZy1HpGdzWns5ZibqCrbYFg/640?wx_fmt=png#imgIndex=0)

**点击上方蓝字 关注武汉网络安全**

![](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn6xia9ep49RicrT5OEnGGic4KZWo09t2MA3L4rPHia34pbYeJ0f4Otp9qIMC9ghF6kj9we0orNMmibEiadQ/640?wx_fmt=png#imgIndex=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/qM42Jic4O617vGSn34UygcLqQgNUkDS7FjD0tsPMUjjqKxVNHGnIaXYrh9rsmicEULco9RqBeIfaNib02nxPWY1qDoWibkNyqLsTBVspC7Gice44/640?wx_fmt=gif&from=appmsg#imgIndex=2)

它的新意不在攻击，在藏身。

据国家互联网应急中心 10 月 30 日发布的风险提示，一种名为 VeilDHT 的新型僵尸网络正在大范围传播，十天内在境内感染约四万台设备，以 Linux 服务器和 IoT 设备为主。这个家族的特别之处不在攻击能力，而在藏身：指挥地址不写在任何固定名单上，按域名封、按 IP 封，都可能扑空。

本文事实与数据引自国家互联网应急中心《关于新型僵尸网络VeilDHT大范围传播的风险提示》（2026-10-30），出处见文末。

![第12期_图1_封面.png](https://mmbiz.qpic.cn/mmbiz_png/qM42Jic4O617ZM7e2EjwXKCewjozcxXF7WUOFLdzpFmKib79fPhwXnIG9FwV7V8B4awu5ZK3BXeRoGlJ9kXDR31XDk32xTI6gnJrYlaYOGRr4/640?wx_fmt=png&from=appmsg)

01

进门这一步，没有任何新技术

传播以漏洞利用为主。提示里点名的两个漏洞都有年头：一个是华硕路由器的命令注入漏洞（CVE-2024-3912），另一个藏在 Realtek SDK 组件里（CVE-2021-35394）——不少厂商的设备共用这套底层组件，一个组件出事，用到它的产品跟着出事。

目标集中在 Linux 服务器和各类 IoT 设备。这类设备最常见的状态，是通电就连网、连上就没人再管：固件出厂是什么版本就一直是什么版本，口令能用就不换。感染量还在爬坡，单日同时上线最多的一天超过 1.5 万台。

值得留意的不是这两个漏洞本身，而是这种组合的普遍性——旧漏洞配旧口令，门一直是开着的，只是这次进来的客人换了住法。

这一步不新，新的是后面每一步。

02

两条通道，都不把真地址写在脸上

过去收拾一个僵尸网络，思路是顺藤摸瓜：找到控制端的域名或 IP，封掉，队伍就散了。这个思路有一个前提——地址是固定的。VeilDHT 偏不给你固定。

它获取真实控制端地址走两条通道，互为备份。一条经过域名解析：解析应答返回的都是伪装的假地址，按域名去查，查到的是空门。另一条藏在公共 P2P 网络里：真实地址混在海量正常流量中传递，没有独立的域名或 IP 可指认。

对防守方来说，这意味着名单式封禁基本落空：解析结果是假的，真实连接又埋在公共流量里。报告也把「检测、封禁与追踪难度较高」写进了总结。

封禁清单对付的是固定目标，它把目标做成了流动的。

03

每一处都拒绝了「找规律」

就算流量到了眼前，认出它也不容易。通信全程加密：握手、认证、指令传输一路密文，中途截获也难以还原。这套加密的完整程度在僵尸网络里并不常见，靠认特征串、认流量形状的老办法，基本够不着。

心跳是随机的：木马定期向控制端报到，但周期和内容都不按固定节奏来，想靠「找规律」发现它，行不通。配置信息以密文存放、顺序被打乱，静态分析难以按序还原。版本支持滚动更新，会自动升级——防护刚学会认这一版，它已经换上新的一版。

单点特征认不出它，异常得凑在一起看。

04

被借走的机器，不会喊疼

感染之后，设备本身一切照旧：上网照常、亮灯照常，主人多半毫无察觉。变的在别处——这台机器同时成了三样东西：发起流量攻击的炮台，藏住真实来源的跳板，长期在线的资源。

这也是这类僵尸网络最难缠的地方：损害由别人承受，痕迹留在设备主这里。等到流量溯源找到自家设备时，问题往往已经存在很久。

自查的手感也只有三样：异常进程、异常外连、异常端口监听——报告防范建议里的排查重点就是这三个方向。

它不偷你的东西，它借你的机器替它干活。

![第12期_图2_原理示意图.png](https://mmbiz.qpic.cn/mmbiz_png/qM42Jic4O615dqoBHZHEGnBWcvQ95uT4VFHUtVtdScSic0rCDj923xorbiaFRO0zaIvVzibzSS00oC8MVpomuyCqgLBUOfp75qjUZWTm9OSkOTI/640?wx_fmt=png&from=appmsg)

05

防护建议

报告给了六组建议。把一台设备从上架到出事摊成三段，六组建议正好各归其位。

上架时：把门修结实

1. 资产清单先理一遍，历史漏洞和最新漏洞一起修，IoT 设备同步升级固件

2. 口令十六位起步，大小写字母、数字、符号混排，不同设备不同口令并定期更换

3. 软件只从官方等可信渠道获取，下载后校验文件哈希，不装来路不明的程序

运行中：让异常露头

4. 终端防护软件保持开启，定期全盘查杀

5. 重点排查异常进程、异常外连与异常端口监听，留意设备在非使用时段的在线动静

6. 网络运营者按通报的处置建议，在出口侧监测相关域名解析请求与连接，发现异常及时阻断并留存证据

出事后：先隔离，再清点

7. 发现感染立即核实受控情况与入侵途径，先把主机隔离出网络，再动手清理

8. 处置情况按属地主管部门要求报告，同步留存日志与证据

上架时的两件事成本最低，运行中的告警最先响，出事后先隔离这一步最容易被跳过。

![第12期_图3_防护清单卡片.png](https://mmbiz.qpic.cn/sz_mmbiz_png/qM42Jic4O6167UmstGiaaUvHr6NCPEmTKhfCbl70FicNgWJY1uMbrsDBaJJzbtrJK52OYF1EBC8D4pg5F0ibtGfePzqjbqIbZIpWN2xfkFrOIVM/640?wx_fmt=png&from=appmsg)

封不完的地址可以慢慢找，没打上的补丁一天都别等。

你家路由器的固件，上次更新是哪一年？

本文事实依据：
1. 国家互联网应急中心：《关于新型僵尸网络VeilDHT大范围传播的风险提示》，2026-10-30，https://www.cert.org.cn/portal/yjtb/eydmtb/2026/11/9c93808159904601829af4e7330cd06a.htm

## ***往期回顾*** [首批18家网络产品安全漏洞收集平台签署自律公约](https://mp.weixin.qq.com/s?__biz=MzA3OTEyODAxMw==&mid=2247514061&idx=1&sn=3b1faf85897e9e7c8b1dda7e313c28f1&scene=21#wechat_redirect) ![](https://mmbiz.qpic.cn/mmbiz_png/qM42Jic4O617vCviaP7SiaRdPzHiaf9hsGCcLr7vuX2y3yHjvG1BeS4FaB3TqTlklqIrbiaLibT287J6b0BVc7jZ3DqwM5IoM7mJauLqAibhb1hWeU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6) [关于征求《湖北省推动“人工智能+制造”若干措施（征求意见稿）》意见的通知](https://mp.weixin.qq.com/s?__biz=MzA3OTEyODAxMw==&mid=2247514061&idx=2&sn=483781b8865bfe0face765061c9e6c30&scene=21#wechat_redirect) ![](https://mmbiz.qpic.cn/mmbiz_png/qM42Jic4O617vCviaP7SiaRdPzHiaf9hsGCcLr7vuX2y3yHjvG1BeS4FaB3TqTlklqIrbiaLibT287J6b0BVc7jZ3DqwM5IoM7mJauLqAibhb1hWeU/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4) [副会长动态 | 天融信参加2026年网络和数据安全产业论坛并获多项认可](https://mp.weixin.qq.com/s?__biz=MzA3OTEyODAxMw==&mid=2247514061&idx=3&sn=c5b15ec8080cafd923fc7fd0ae07cd7c&scene=21#wechat_redirect) ![](https://mmbiz.qpic.cn/sz_mmbiz_png/qM42Jic4O614JBweRYZYsKXp1Dtsxcnl01KuibYEMot0bvKEoRbFwuSI6gF4xq09KTtSvEuXzJhEssy5DKeRkShsz0AyRdicb0gECZwXsrtK30/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=9)

##

![图片](https://mmbiz.qpic.cn/mmbiz_png/qM42Jic4O617yedic9FDiaXYtAh6GvpyC5sJIpvMVCHhXUSJickW4DOOph3EVQnz5TGONI76s1scQjCme9icsjZ0k5TSNYHHaoupjUYUGB1Os7Bc/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lJWhyqdP0Inib7gFln8HMiaedowUpdURAEPu6gLq67vIbDna2ZBCCxYG7MZoyfpUJMWJ0p5yCJic8Asxu4XdeicXcw/0?wx_fmt=png)

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