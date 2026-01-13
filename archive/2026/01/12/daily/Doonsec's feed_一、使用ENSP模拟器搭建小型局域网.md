---
title: 一、使用ENSP模拟器搭建小型局域网
url: https://mp.weixin.qq.com/s/DjGxoBOBHUaU_V53fMY9jA
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:28:36.278351
---

# 一、使用ENSP模拟器搭建小型局域网

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/gibIKibEUpvLMUa4585JpkF5ibs1moPm5fIUia7YNonVyrtH1fWDeLrYWfa43ic3cAJDESbARZt17Gz1WibiaicddBZWDA/0?wx_fmt=jpeg)

# 一、使用ENSP模拟器搭建小型局域网

原创

老五

老五说网络

![]()

在小说阅读器中沉浸阅读

点击上方**蓝字**，关注我们

**小型企业网络实验配置**

小型企业如何配置无线有线一体网络？现有“老五工作室”需要设计网络规划以及配置，需要满足几点是，有线无线网络划分，地址自动获取，无线名称：laowu，无线有线可以互访。

地址规划：

互联网server:220.220.220.220/24 网关：220.220.220.1/24

互联网地址：110.110.110.0/24 网关：110.110.110.1/24

内网设备互联地址段：192.168.255.0/24

有线用户网段：192.168.10.0/24

无线用户网段：192.168.20.0/24

无线AP管理地址段：192.168.21.0/24

VLAN规划：

有线用户VLAN: VLAN 10

无线用户VLAN：VLAN 20

无线设备管理VLAN: VLAN 21

设备互联VLAN: VLAN 255

**“老五工作室”网络拓扑**

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLMUa4585JpkF5ibs1moPm5fIBZKzGGm7qHWmpH17HfAWa7ibg4u0IR6Rhy5oiclIpxd44Z43Ab0pXj4Q/640?wx_fmt=png)

一、设备配置：

（1）互联网Server1配置：

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLMUa4585JpkF5ibs1moPm5fIKBK6DiaMSMskCcrOLiaIKKNosDoYdQF4TJAD3geCYtWdIeZ3krd0cWuQ/640?wx_fmt=png)

（2）INTERNET-R2配置：

```
sysname INTERNET-R2#interface GigabitEthernet0/0/0 ip address 110.110.110.1 255.255.255.0#interface GigabitEthernet0/0/1 ip address 220.220.220.1 255.255.255.0#
```

（3）出口路由R1配置：

```
sysname R1#acl number 2002 rule 5 permit source 192.168.10.0 0.0.0.255 rule 10 permit source 192.168.20.0 0.0.0.255#interface GigabitEthernet0/0/0 description to-CORE ip address 192.168.255.2 255.255.255.0#interface GigabitEthernet0/0/1 description to-hulianwang ip address 110.110.110.2 255.255.255.0 nat outbound 2002#ip route-static 0.0.0.0 0.0.0.0 110.110.110.1ip route-static 192.168.10.0 255.255.255.0 192.168.255.1 description youxian-userip route-static 192.168.20.0 255.255.255.0 192.168.255.1 description wuxain-user#
```

（4）核心CORE配置：

```
sysname CORE#vlan batch 10 20 to 21 255#vlan 10description youxian-uservlan 20description wuxian-uservlan 21description wuxian-managevlan 255description hulian-R1#ip pool vlan10gateway-list 192.168.10.1network 192.168.10.0 mask 255.255.255.0dns-list 114.114.114.114#ip pool vlan20gateway-list 192.168.20.1network 192.168.20.0 mask 255.255.255.0dns-list 114.114.114.114#interface Vlanif10ip address 192.168.10.1 255.255.255.0dhcp select global#interface Vlanif20ip address 192.168.20.1 255.255.255.0dhcp select global#interface Vlanif255ip address 192.168.255.1 255.255.255.0#interface GigabitEthernet0/0/1description to-R1port link-type accessport default vlan 255#interface GigabitEthernet0/0/2port link-type accessport default vlan 10#interface GigabitEthernet0/0/3port link-type accessport default vlan 10#interface GigabitEthernet0/0/23port link-type trunkport trunk pvid vlan 21port trunk allow-pass vlan 20 to 21#interface GigabitEthernet0/0/24description to-AC6005port link-type trunkport trunk allow-pass vlan 20 to 21#ip route-static 0.0.0.0 0.0.0.0 192.168.255.2#
```

（5）无线AC6005配置：

```
vlan batch 21#dhcp enable#vlan 21 description -wuxain-manage#interface Vlanif21 ip address 192.168.21.1 255.255.255.0 dhcp select interface#interface GigabitEthernet0/0/1 port link-type trunk port trunk allow-pass vlan 21#capwap source interface vlanif21#wlansecurity-profile name laowu-securitysecurity wpa2 psk pass-phrase %^%#b-W~R6YI\IQ+6u7d(9oF3q'&BqRiq+YuTfQV4L7E%^%# aes ssid-profile name laowu-ssid  ssid laowu vap-profile name laowu-vap  service-vlan vlan-id 20  ssid-profile laowu-ssidsecurity-profile laowu-security regulatory-domain-profile name laowu ap-group name laowu  regulatory-domain-profile laowu  radio 0   vap-profile laowu-vap wlan 1  radio 1   vap-profile laowu-vap wlan 1 ap-id 0 type-id 56 ap-mac 00e0-fc5e-18c0 ap-sn 210235448310057CF004  ap-name laowu01  ap-group laowu#
```

二、结果验证：

（1）无线主机STA1的信息：

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLMUa4585JpkF5ibs1moPm5fICt5icPibibOWVEAsJQkEeBhYt4NkTbHaSduHkr4ArtTvYtHV6yJCqrHGg/640?wx_fmt=png)

（2）有线主机PC1的信息：

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLMUa4585JpkF5ibs1moPm5fIKIjicibKla7BfMJkFky2Ij1u71YxjPiaXX1xYOOXwaCmU0oMwGL7IKdBg/640?wx_fmt=other)

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLMUa4585JpkF5ibs1moPm5fI7M3iaG4TNB7ZtsIhGxMKGMhGeEYvb27ibsfGGFyAlr9KWnUMaTYdOfhA/640?wx_fmt=png)

（3）查看PC1访问外网Server1地址：

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLMUa4585JpkF5ibs1moPm5fIXkaACiag99P1r1Cl3JyQdEdjicyHVqJXhjPjeiciceh5S6OcSfPIzbeObA/640?wx_fmt=png)

（4）查看AP上线信息：

![](https://mmbiz.qpic.cn/mmbiz_png/gibIKibEUpvLMUa4585JpkF5ibs1moPm5fIam8s9U8fsiaGgdnokxqrWoOEwYOnf0u1189QvGxf5oe17MiaR9f4sPPA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/v4vz52CcB13ZXRV9zmAO2vtA0yMotwM0j6fFjXmJUov1USlrtbvSdDhsXbTTeGia6rk9zap1rcdqQVZLibyVf6CQ/640?wx_fmt=gif)

长按二维码

关注更多精彩

![](https://mmbiz.qpic.cn/mmbiz_jpg/gibIKibEUpvLMUa4585JpkF5ibs1moPm5fIcRJYyW6tL3XbsnbnERP8XIibXcEChvqPsibJkGlMfUjZHQEMxGooQFJw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12T0IfQ2ySyETI7FIw0ehV0nZXOYHPnvSCGAwt452BKQmsRsTps54pbyYuHXxHr7Yp89Ms9NqvGYw/640?wx_fmt=png)

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