---
title: 三、如何使用PPPOE拨号上网？
url: https://mp.weixin.qq.com/s/EnZw94uRrL04bF6VknxJJg
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:28:42.048975
---

# 三、如何使用PPPOE拨号上网？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/gibIKibEUpvLNgDiarPguBfoUA4GqvMSVT2iciaSHy4BJcxEvLFtrqdFPM4picVxv1fL8BlgWenzKpcYibvT3pTZvdTJg/0?wx_fmt=jpeg)

# 三、如何使用PPPOE拨号上网？

原创

老五

老五说网络

![]()

在小说阅读器中沉浸阅读

点击上方**蓝字**，关注我们

**“老五工作室”**

**PPPOE拨号上网**

“老五工作室”部署了一台路由器R1。路由器R1作为互联网接入设备，为内网用户提供上网服务。由于“老五工作室”资金有限，所以工作室只能购买家庭宽带，使用PPPOE的拨号方式访问互联网，部署在互联网接入设备的上行接口。老五希望在路由器上配置NAT功能，使内网用户192.168.10.0/24可以通过公网口的IP地址访问Internet。

地址规划：

pppoe-server网关地址：110.110.110.1/24

R1与CORE互联地址：192.168.255.0/24

内网用户地址网段：192.168.10.0/24

PPPOE地址池部署在pppoe-server路由器，PPPOE地址池网段：110.110.110.0/24 网关地址是：110.110.110.1/24

pppoe客户端账号：laowu，密码：laowu888。

**“老五工作室”网络拓扑**

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLNgDiarPguBfoUA4GqvMSVT2mzcVMXG0RjrxHiahBYlianbVOqYsZjay7C7reoDKEnpq18IdHNCyPkLg/640?wx_fmt=png)

一、实验配置

（1）CORE设备配置：

```
sysname CORE#vlan batch 10 255#interface Vlanif10ip address 192.168.10.254 255.255.255.0#interface Vlanif255ip address 192.168.255.1 255.255.255.0#interface GigabitEthernet0/0/1port link-type accessport default vlan 255#interface GigabitEthernet0/0/2port link-type accessport default vlan 10#ip route-static 0.0.0.0 0.0.0.0 192.168.255.2#
```

（2）R1路由器设备配置：

```
sysname R1#acl number 3000  rule 5 permit ip source 192.168.10.0 0.0.0.255 #interface Dialer1link-protocol pppppp chap user laowuppp chap password cipher %$%$#g%(UT*+G3J>uRQK4_0C,.z{%$%$ip address ppp-negotiatedialer user laowudialer bundle 1nat outbound 3000#interface GigabitEthernet0/0/0ip address 192.168.255.2 255.255.255.0 #interface GigabitEthernet0/0/1pppoe-client dial-bundle-number 1 #ip route-static 0.0.0.0 0.0.0.0 Dialer1ip route-static 192.168.10.0 255.255.255.0 192.168.255.1#
```

（3）pppoe-server设备配置：

```
sysname PPPOE-Server#dhcp enable#ip pool pppoe-servergateway-list 110.110.110.1 network 110.110.110.0 mask 255.255.255.0 #aaa local-user laowu password cipher %$%$~j&>R5X/3@.2{00`=+\Oj$KZ%$%$local-user laowu service-type ppp#interface Virtual-Template1ppp authentication-mode chap remote address pool pppoe-serverip address 110.110.110.1 255.255.255.0 #interface GigabitEthernet0/0/0pppoe-server bind Virtual-Template 1#
```

（4）内网用户PC1主机：

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLNgDiarPguBfoUA4GqvMSVT2wBZmxdzeaJwbaicx6SYxFxs4Jhic1ib0DJagzLlhwNribxibqJtwaJaEqOA/640?wx_fmt=png)

二、结果验证

（1）内网PC1与110.110.110.1测试连通性：

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLNgDiarPguBfoUA4GqvMSVT2UKCOpjKMnnmNC1B0TBEHyqTkqr2lB5uLFh4qp5aWa8VlW5ZsG0icXlw/640?wx_fmt=png)

（2）查看路由器R1的PPPOE拨号获取地址以及获取数过程：

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLNgDiarPguBfoUA4GqvMSVT2sXWy2qZsARrodhwqsDooxszy2znL2aw8jOI65pcxvEsfca42E7Fspg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLNgDiarPguBfoUA4GqvMSVT2FNOjyqBB7j5btAibFuiaicPIEAOsAsMwkf6A6EpE5sGTSaGIYXU5Ohc6A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/v4vz52CcB13ZXRV9zmAO2vtA0yMotwM0j6fFjXmJUov1USlrtbvSdDhsXbTTeGia6rk9zap1rcdqQVZLibyVf6CQ/640?wx_fmt=gif)

长按二维码

关注更多精彩

![](https://mmbiz.qpic.cn/mmbiz_jpg/gibIKibEUpvLNgDiarPguBfoUA4GqvMSVT2icOp3wPVpxFXCpicqeJPUicxrNPo1UJpgB5BfEzBRlUxuonpYvOEcn6CA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12T0IfQ2ySyETI7FIw0ehV0nZXOYHPnvSCGAwt452BKQmsRsTps54pbyYuHXxHr7Yp89Ms9NqvGYw/640?wx_fmt=png)

**转载请附上原文出处链接，原文链接：【老五说网络公众号】**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLOJzH1ibvfvuFCD14XFsicawiaoknTMvxaEdUvgrDMyGO31nS6B2As3IjHzIr2xeMA4dtrXg4SpwYW6Q/0?wx_fmt=png)

老五说网络

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLOJzH1ibvfvuFCD14XFsicawiaoknTMvxaEdUvgrDMyGO31nS6B2As3IjHzIr2xeMA4dtrXg4SpwYW6Q/0?wx_fmt=png)

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