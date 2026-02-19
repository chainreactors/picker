---
title: 企业路由器配置IPv6家用宽带的PPPoE拨号示例
url: https://mp.weixin.qq.com/s/58sikA2l0OKzDwfXcMg7KQ
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:19:57.956011
---

# 企业路由器配置IPv6家用宽带的PPPoE拨号示例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricPHibgtQzZvNPpd59GrfyppLqvsCtj095uJKOo0GL2RibfKr9C8hRZzSA/0?wx_fmt=jpeg)

# 企业路由器配置IPv6家用宽带的PPPoE拨号示例

原创

衡水铁头哥
衡水铁头哥

铁军哥

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/f5u8u3lDeLchGaIcFTOuEzUYJyA2UibBrCNnQdjVEpYaZthELRW8oaiaUPXweZu61lAcOx0bWAPzhgJMibtaLaHVA/640?wx_fmt=gif)

正文共：2730字 16图，预估阅读时间：7 分钟

我们前面介绍了如何配置PPPoE Server，并通过DHCPv6协议为终端分配IPv6地址**（****[配置PPPoEv6服务器为终端分配IPv6地址](http://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458856433&idx=1&sn=31455767b3091a463b85b1e106924e9a&chksm=fc98a2fccbef2beaff0707f0ea6786214f654fc7c17a9b8d559a0e4104592ab9fe79b77bcb5a&scene=21#wechat_redirect)****）**。但是这个操作有点偏向于运营商侧，对于普通企业用户而言，可能没学到什么东西。

那对于普通企业用户而言，IPv6应该怎么玩呢？或者换个说法，你跟我一样，家里的上网设备是一台企业级路由器**（****[网络之路4：快速上手企业路由器MSR810-W](http://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458850264&idx=1&sn=70b864ad557397a25346ee1ecbdcfc39&chksm=fc989ad5cbef13c33b83ca0f0a61f0a3dec0f295c46a43fbbd7467033522335f124d2cab6358&scene=21#wechat_redirect)****）**，那应该怎么配置才能使终端可以通过IPv6上网呢？

相比IPv4 PPPoE的家喻户晓，IPv6 over PPPoE（PPPoEv6）的配置略显神秘。它不仅是运营商接入网的基石，更是企业通过DHCPv6-PD获取IPv6前缀，为内网成百上千设备分配全球身份证的关键一环！

首先，我本地的MSR路由器已经拨号成功了，电脑终端通过DHCPv6可以正常获取到IPv6地址**（[有状态DHCPv6快速模式配置及EUI-64介绍](http://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458854852&idx=1&sn=dc86c28c9ad422cbe92feacfbc228aae&chksm=fc98acc9cbef25dff6df228ebc49fafdab38e7864b694c0403478c51607e9f2eda8bd8a6c550&scene=21#wechat_redirect)****）**。在此基础上，我们将PPPoE Server设备桥接到主机的物理网卡，使HCL中的虚拟网络可以联网；然后配置PPPoE Client设备，其实就等效于我的MSR设备；再将Client设备连接到主机的VirtualBox Host-Only Ethernet Adapter网卡，模拟内网的上网主机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricOpNvCmibEiaiaibsI9BpPDp6Uk8MMUiaajwJLyN2qaX3MvcNBRV4pfrSfLQ/640?wx_fmt=png&from=appmsg)

在这个网络里面，Client通过PPPoE接入Server，Server作为PPPoE Server通过DHCPv6协议给Client分配代理前缀，Client再通过代理前缀给下面的主机分配IPv6地址。

首先配置Server可以上网，参考DHCPv6的无状态配置**（****[无状态DHCPv6配置](http://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458854597&idx=1&sn=fd44512dca7f14233cdd8e624745b455&chksm=fc98adc8cbef24de0caa56d0c9b7e2f5a7c3d9c0785eb01fc1e4cf7f69613ba330d9277c128b&scene=21#wechat_redirect)****）**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujrickJibhibEs1P9ZjWg76UszicRFVv5r9vqvokLLhPItgHU5JSSjnAo8JyFQ/640?wx_fmt=png&from=appmsg)

我记得之前还吐槽无状态配置方式太简单，没什么卵用，我现在收回这句话，太简单了。

跟配置IPv4的PPPoE一样**（****[脚本案例来了！一台初始化配置的MSR810-W快速满足业务上线的4个要求](http://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458843684&idx=1&sn=1f393d12d4dabbf5ecaed7f9ba6ab0a6&chksm=fc997329cbeefa3fd76bba9bd20af397c38c721f69fbb9301b4608c3bf6621456f0ef13a7824&scene=21#wechat_redirect)****）**，我们先在Server上创建一个PPPoE用户。

```
#local-user pppoe classnetwork password simple pppoe service-type ppp
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricb2WC1kmGWFKoXebKGbDsNcicCialr8kDmctia6LxgJibCL2iblrKWfiay6GQ/640?wx_fmt=png&from=appmsg)

然后，我们配置虚拟模板接口1来和客户端交互报文，配置VT1接口采用PAP认证对端，配置本端IPv6地址，关闭对RA消息发布的抑制；开启DHCPv6 Server功能，配置Host主机通过DHCPv6协议获取IPv6地址。

```
#interfacevirtual-template 1pppauthentication-mode pap domain systemipv6address 2024::1 64undoipv6 nd ra haltipv6nd autoconfig managed-address-flagipv6dhcp select server
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricL10xx7csmsibjgvBseSmKfKCWWH4ZqWic0YJYGr9oNIMaFrlA5QDG5Aw/640?wx_fmt=png&from=appmsg)

接下来，在GigabitEthernet1/0接口上启用PPPoE Server协议，将该虚拟模板接口1绑定至该以太网接口。

```
#interface gigabitethernet 1/0 pppoe-server bind virtual-template1
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricvcjJsTsOA7n156AXfyxkW21vF1VdTYXOwwys9bqw6KmDotuuUVHgBA/640?wx_fmt=png&from=appmsg)

本次，我们使用DHCPv6前缀池的方式来分配IPv6地址，配置DHCPv6前缀池1，包含的前缀为2024::/64，分配的前缀长度为80；并创建名称为pppoe的DHCPv6地址池，在地址池下引用前缀池1。

```
#ipv6dhcp prefix-pool 1 prefix 2024::/64 assign-len 80#ipv6dhcp pool pppoeprefix-pool1dns-server240E:40:8000::10domain-nameguotiejun.comgateway-list2024::1
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricO0UvK9YibXbQEHvHvuN1Sdn3BEkicC5zRqFufI2xAChTbIM4Y1ZPIu0w/640?wx_fmt=png&from=appmsg)

在ISP域下为用户配置授权地址池属性。

```
#domain system authorization-attribute ipv6-pool pppoe
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricOia3m4Xn9ysUJlJIaZLx4rDfrzAy0V85ItGNVfOuqWI3EAhmDoKo1FA/640?wx_fmt=png&from=appmsg)

接下来，我们配置Client设备，对应各位手里的企业级路由器**（****[网络之路9：MSR810-W配置命令解读](http://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458850397&idx=1&sn=8ce25673270d1f3631c3b88c81c6d42f&chksm=fc989d50cbef14467fd5c9408b2382b1c289776e6c2e1cc78bcbc38a3bfcaa7c1a57b65b640c&scene=21#wechat_redirect)****）**。

首先，PPPoE的基础部分与IPv4基本一致。创建一个Dialer接口，开启共享DDR；配置Client被Server认证的方式为PAP，当Server认证时，并配置Client发送的PAP用户名和密码；配置PPPoE Client工作在永久在线模式；配置DDR自动拨号的间隔时间为60秒。

```
#interfacedialer 1dialerbundle enableppppap local-user pppoe password simple pppoedialertimer idle 0dialertimer autodial 60
```

还有IPv6的差异部分，配置Dialer1接口作为DHCPv6客户端，通过DHCPv6方式获取IPv6地址、IPv6前缀和其他网络配置参数；指定获取到IPv6前缀后，创建编号为1的IPv6前缀，该前缀编号1对应的IPv6前缀为DHCPv6客户端获取到的前缀。

```
#interfacedialer 1ipv6address dhcp-allocipv6dhcp client pd 1
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricGTkzItUFh70T0QcsYbLgoPhkndabVeWRKYHlyflxib4QFMUZRFaINEw/640?wx_fmt=png&from=appmsg)

接下来，配置一个PPPoE会话，该会话对应Dialer bundle 1，Dialer bundle 1对应Dialer1接口。

```
#interface gigabitethernet 1/0 pppoe-client dial-bundle-number 1
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricmUlf8ZOahyyKCp18Ah4Rib67BI5TSmUxxv62gArfZBwpZVUWL3Voh5g/640?wx_fmt=png&from=appmsg)

添加缺省路由的配置，大家看自己的需求来定要不要加，因为通过DHCPv6可以获取默认路由，手工配置只不过是改变了路由类型，并且将优先级从80提升到了60而已**（****[IPv6静态路由配置](http://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458854710&idx=1&sn=419c5aeb85c0fe6ee73f377e42d883ec&chksm=fc98ac3bcbef252d4f6edc62c0f659702e6c425888b427f3aef7cccda476c2f7061ba4fab765&scene=21#wechat_redirect)****）**。

```
#ipv6 route-static :: 0 dialer 1
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricJADRRuXANrEuHAibshh6GW1iceuwuPXk8uQXtNAFpvRIQUCbFzPcw5sA/640?wx_fmt=png&from=appmsg)

接下来，我们在接口GigabitEthernet2/0上取消对RA消息发布的抑制，并开启无效授权前缀通告功能。

```
#interfacegigabitethernet 2/0undoipv6 nd ra haltipv6nd ra invalid-delegated-prefix advertise enable
```

最后是尤为重要的一步，需要在接口GigabitEthernet2/0上配置动态获取IPv6前缀的编号为1，即该接口将使用编号为1的前缀生成IPv6地址，并将编号为1的IPv6前缀通过RA报文分配给终端设备。

```
#interfacegigabitethernet 2/0ipv6address 1 2024:7:29:18:18:18::1/80
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricSeYEfVm3rZMI4hG3icBicWh9874A795Fx4sIG1p6IzeQ3p2LRC81OP0w/640?wx_fmt=png&from=appmsg)

我们看一下Client设备通过DHCPv6获取的配置信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricQp5u8mjrFb9rjVKtWNsYicQIEz2UC2UjrRZThKAYorgkExxDERPiaRtA/640?wx_fmt=png&from=appmsg)

自动获取并创建的IPv6前缀信息，以及接口的IPv6地址信息。

```
display ipv6 prefix
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricvroyxI8LFW3OJafCwa9kyKTiaafeNdJAcYcfJsZo3HbGNxgILpR4Y1g/640?wx_fmt=png&from=appmsg)

可以看到，Client拨号成功后，Server通过DHCPv6协议为Client分配一个代理前缀2024::/80；再结合接口配置的80位前缀，匹配之后接口的IPv6地址的后48位即为18:0:1，和PD前缀合起来就是2024::18:0:1/80。

查看服务端的拨号信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujricAMYY9NgSum4FibbMEibfwvy9lZgOthfxUU7jTKibnHZibib7Gor0tu8fh9A/640?wx_fmt=png&from=appmsg)

测试一下Client到是否可以访问互联网。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujrict8zDVWic1cT7BibaNswRLIibzj9CbaIb3Kfo4ousI39YcRwL6n05SnciaQ/640?wx_fmt=png&from=appmsg)

再测试一下IPv6的DNS是否可用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6TLkQEqM6ETWicsItJaujrictgYzliaGjef9F4icH00T3CxX91BtRdagx1AIFEDXmzVG6lmq6nXquibTw/640?wx_fmt=png&from=appmsg)

该说不说，这长长的一串，让谁背也背不下来啊！

通过本次步步为营的配置，我们不仅成功打通了PPPoEv6链路，更深入理解了DHCPv6前缀委派这一强大功能。它使得企业只需一个PPPoE会话，就能为整个内部网络获取充足的IPv6公网地址空间，是迈向IPv6时代的必备技能。

你的网络环境是否也已部署IPv6？欢迎在评论区交流配置心得！

\*\*\*推荐阅读\*\*\*

[我们的WireGuard管理系统支持手机电脑了！全平台终端配置，支持扫码连接，一键搞定](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864213&idx=1&sn=ec85efce2a3b76ba244c71ccbd...