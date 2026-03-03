---
title: EVE-NG中CSR1000v设备配置SSH协议，基于DHCP
url: https://mp.weixin.qq.com/s/d1rk_jTUww2hUK1bjwunJw
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:09:09.876036
---

# EVE-NG中CSR1000v设备配置SSH协议，基于DHCP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Dibzmm9niba04iaRk4ajjmA5gwaDvNSprKlOmrMic8QOBicEYncP4EguicNraiaHBf7F5scD0cAP6gib6S4cXTXQnfX18XwFAmqVWfVzPF9vW9E9Syo/0?wx_fmt=jpeg)

# EVE-NG中CSR1000v设备配置SSH协议，基于DHCP

原创

Lino
Lino

网络技术联盟站

![]()

在小说阅读器中沉浸阅读

各位同学，大家好！我是你们的 Python 讲师 Lino。

先确认:

* 设备：Cisco CSR1000v
* 接口：GigabitEthernet1
* 连接：EVE-NG 的 Cloud0（NAT）
* DHCP Server：EVE-NG 宿主机 NAT（自动提供）

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba07ia1vU0W3AgPZcCV8dslNxClRYjqlIibxSf57teWn2qyYR3otKtf2ibofvalRvwWsp0kb7vDWdxpjHdrMvPBtoQXzCw4XNDrB4oQ/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba04SvZVialwW4yib8kUacRCGq2B6e1J3SicQoWSHzgPuyO3n3p13D4lMOl8F1c352rkibVS6QJCo0HGV0PwfILJVVM0RvK3g4aGGzNo/640?wx_fmt=png&from=appmsg) |

## 进入特权模式

```
```
enable
```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba04yUZlWaSyctj926Tpq3KB8EcBGlUqwywvFIrtxaO3zsk21d5iavPIIEwZBfy8u1c4hypsiaZWnlXOGz5bYNcnSn2wic59BEErVlc/640?wx_fmt=png&from=appmsg)

## 全局基础配置

```
```
configure terminal
hostname CSR-SSH
ip domain-name lab.local
```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba05ib1f0upJ4qDiaKX6DgOjXCKrOPKIbKYqJBK6NDr6CLpYarTQhx8sBteiaGvicLp5pLS2CoCl7qDBibRnCmGNkmjIdE0j3zKMlFdGI/640?wx_fmt=png&from=appmsg)

> `hostname` + `ip domain-name`是后面生成 RSA 的**硬性条件**

## 管理接口使用 DHCP

```
```
interface GigabitEthernet1
 description *** MGMT via EVE-NG NAT ***
 ip address dhcp
 no shutdown
exit
```
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06735EuMX97ocTukhZ6qter72dvTMeVqhnZSCWtqwfIzwj1N1NNqe6P7k07oYzZPydIaicpic2WnUjekpSbf1a0RLQGgOP86VCDQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

网络技术联盟站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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