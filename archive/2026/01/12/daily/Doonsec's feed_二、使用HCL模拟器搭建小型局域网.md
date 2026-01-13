---
title: 二、使用HCL模拟器搭建小型局域网
url: https://mp.weixin.qq.com/s/CLJPGF8UdT6p_v6xdi-9PA
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:28:38.928660
---

# 二、使用HCL模拟器搭建小型局域网

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gibIKibEUpvLObd2H3F7EYRYIibsyyQsOKnzRzibJkL4xZEUHOJf7YyUsiawSN7W3ocDL0afcn2FfOU0ibSNULnWPm6g/0?wx_fmt=jpeg)

# 二、使用HCL模拟器搭建小型局域网

原创

老五

老五说网络

![]()

在小说阅读器中沉浸阅读

点击上方**蓝字**，关注我们

**使用新华三的HCL模拟器**

**小型局域网****配置实验**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gibIKibEUpvLObd2H3F7EYRYIibsyyQsOKnAgDpkmUObxibiac41ZbOVYia2Bqap7kRzqa1r4GuicLAj0f8zvzLZqyVKQ/640?wx_fmt=png)

一、实验配置

（1）H3C-CORE设备配置：

```
sysname H3C-CORE#telnet server enable#vlan 10#vlan 20#vlan 100#vlan 255#interface Vlan-interface10ip address 192.168.10.1 255.255.255.0#interface Vlan-interface20ip address 192.168.20.1 255.255.255.0#interface Vlan-interface100ip address 192.168.100.1 255.255.255.0#interface Vlan-interface255ip address 192.168.255.1 255.255.255.0#interface GigabitEthernet1/0/1port link-mode bridgeport access vlan 255combo enable fiber#interface GigabitEthernet1/0/2port link-mode bridgeport access vlan 10combo enable fiber#interface GigabitEthernet1/0/3port link-mode bridgeport link-type trunkport trunk permit vlan allcombo enable fiber#ip route-static 0.0.0.0 0 192.168.255.2#local-user laowu class managepassword hash $h$6$ZlPzeBg9E4HDIU9A$7VjNtSkH7G5kFW+3lYn1dDzrf8xkqe0dHDzVjNNP59BimKuvgdqpYYLcC2ca3P4QlnFjNWr7WxxkdW+63i4CqQ==service-type telnetauthorization-attribute user-role network-operator#return
```

（2）H3C-route路由器设备配置：

```
sysname H3C-route# telnet server enable#nat address-group 1 address 110.110.110.1 110.110.110.1#interface GigabitEthernet0/0 port link-mode route combo enable copper ip address 110.110.110.1 255.255.255.0 nat outbound 2001 address-group 1#interface GigabitEthernet0/1 port link-mode route combo enable copper ip address 192.168.255.2 255.255.255.0# ip route-static 0.0.0.0 0 110.110.110.2 ip route-static 192.168.10.0 24 192.168.255.1 ip route-static 192.168.20.0 24 192.168.255.1#acl basic 2001 rule 5 permit source 192.168.10.0 0.0.0.255 rule 10 permit source 192.168.20.0 0.0.0.255#local-user laowu class manage password hash $h$6$qGyhPQLNJdrrviQR$NHVGfDVDbuj+xbxJeeOB6TAGI8stnstxX1IaBtHJbOkHmdSTzG63z4n/5emHIah/yvN9j2qYNHC/F20g/Iq4jw== service-type telnet authorization-attribute user-role network-operator#return
```

（3）H3C-jieru设备配置：

```
sysname H3C-jieru#telnet server enable#vlan 1#vlan 20#vlan 100#interface Vlan-interface100ip address 192.168.100.2 255.255.255.0#interface GigabitEthernet1/0/1port link-mode bridgeport link-type trunkport trunk permit vlan allcombo enable fiber#interface GigabitEthernet1/0/2port link-mode bridgeport access vlan 20combo enable fiber#ip route-static 0.0.0.0 0 192.168.100.1#local-user laowu class managepassword hash $h$6$rkDd9dG7OYebUAtU$Mcnd/G4hs+AWoKEf70YRq441WW+JH7VeZDAgo6vaqRS4Y1SxfUEZtVty+IsAZW7FBboZx9U9bmgjb2YGuAGu4Q==service-type telnetauthorization-attribute user-role network-operator#return
```

（4）WAI-wang模拟路由器配置：

```
sysname WAI-wang#interface LoopBack0ip address 12.1.1.1 255.255.255.255#interface GigabitEthernet0/0port link-mode routecombo enable copperip address 110.110.110.2 255.255.255.0#return
```

二、结果验证

（1）内网PC1内网，外网测试连通性：

（2）内网PC1通过telnet方式登录管理设备：

![](https://mmbiz.qpic.cn/mmbiz_gif/v4vz52CcB13ZXRV9zmAO2vtA0yMotwM0j6fFjXmJUov1USlrtbvSdDhsXbTTeGia6rk9zap1rcdqQVZLibyVf6CQ/640?wx_fmt=gif)

长按二维码

关注更多精彩

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gibIKibEUpvLObd2H3F7EYRYIibsyyQsOKnz4qrMpfPB29Kw7sb7skic9NkgEUqLoCLMnqicuk4pic2qBCLRnF2EVefw/640?wx_fmt=jpeg)

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