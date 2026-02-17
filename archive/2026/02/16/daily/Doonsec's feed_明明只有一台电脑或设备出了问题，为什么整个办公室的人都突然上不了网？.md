---
title: 明明只有一台电脑或设备出了问题，为什么整个办公室的人都突然上不了网？
url: https://mp.weixin.qq.com/s/AZVeNoH98i1v06Z8zAOolA
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:12:51.286533
---

# 明明只有一台电脑或设备出了问题，为什么整个办公室的人都突然上不了网？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vf29dJy0S5icBbCm6wicUub6RL3DWsZ6GibglBWjmWYs175Kw6xTFt0wVo0GgwKldh0OQgoFBhfiaPBUKrqVwU50EJOZJRZgJju8qZfzorG7bibo/0?wx_fmt=jpeg)

# 明明只有一台电脑或设备出了问题，为什么整个办公室的人都突然上不了网？

原创

圈圈
圈圈

网络技术干货圈

![]()

在小说阅读器中沉浸阅读

点击上方 网络技术干货圈，选择 设为星标

优质文章，及时送达

![](https://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT9z1qCg1V9MbsCSdmUBkOicVRmk5T6j0m8Z8L9YdmdU0crxLkBG4994IkXaZTrSnJAZksCicKaqO43g/640?wx_fmt=png)

> 转载请注明以下内容：
>
> **来源**：公众号【网络技术干货圈】
>
> **作者**：圈圈
>
> **ID**：wljsghq

局域网里每台电脑、手机、打印机、摄像头都需要一个“门牌号”，这个门牌号就是IP地址。

最常见的是192.168.x.x这种格式。

公司一般用两种方式给设备发门牌号：

* 手动设置（静态IP）：比如服务器、NAS、打印机，我们自己填好IP、子网掩码、网关、DNS。
* 自动获取（DHCP）：大多数员工电脑、手机都是这种方式，路由器或专门的DHCP服务器会自动分配一个还没被用的地址。

同一个网络里，同一个IP地址只能被一台设备使用。如果两台设备同时用了192.168.1.100，就会产生冲突。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S58Oz8frfd87ztYVvg4IDPJTYSZmqibh1NpZV21iaaLl5k9JSKGKybzps52xAMIclcz8CibVNstmhK0pOuf4Z0RlcjZCkHXdvIA4BY/640?wx_fmt=png&from=appmsg)

正常情况下，Windows、macOS遇到冲突都会弹出提示框：“IP地址冲突”，然后其中一台网卡会被禁用。但现实中，很多时候提示框没来得及弹出，或者压根没显示，整个网络就已经乱了。

## 为什么一台设备冲突，就能让大家都掉线？

核心原因跟两个机制有关：**ARP协议** 和 **广播域**。

局域网里，电脑之间真正通信靠的是MAC地址（网卡的物理地址），而不是IP地址。IP只是高层用的逻辑地址。

当你的电脑想访问公司服务器（比如192.168.1.10）时，会先问：“谁是192.168.1.10？请告诉我你的MAC地址。” 这就是ARP请求，而且是**广播**发出去的，全网所有设备都能听到。

正常情况下，只有真正的192.168.1.10会回答：“是我，我的MAC是xx:xx:xx:xx:xx:xx。”

但如果现在有两台设备都认为自己是192.168.1.10，它们都会抢着回答！

结果：

* 你的电脑收到两个不同的MAC地址回答，缓存表不停翻转（一会儿这个MAC，一会儿那个MAC）。
* 数据包发出去后，到底到达哪台设备变成了随机事件。
* 连接时好时坏，Ping丢包严重，网页加载一半卡住。

公司路由器的IP通常是192.168.1.1（或类似），它是所有设备访问外网和跨网段的唯一出口。

假如一台新笔记本（或恶意设备）错误地把自己的IP设成了192.168.1.1：

* 全网电脑要上网时，都会先发ARP广播问：“谁是192.168.1.1？”
* 路由器和那台笔记本都会回答。
* 大家电脑的ARP表开始混乱，相当一部分流量被错误送到笔记本上。
* 笔记本根本处理不了这些路由流量，于是大量丢包。
* 表现出来的就是：大家同时掉线，内网文件共享也变慢或失败。

我遇到过最典型的一次：新来的实习生把自己的电脑静态IP设成了路由器地址，结果不到五分钟，整个楼层四十多人都报“网络中断”。

冲突设备不停发送ARP应答（尤其是某些恶意工具或配置异常的设备），广播包数量激增。

交换机把这些广播包转发到所有端口，CPU占用率飙升，正常业务包被挤压，网络整体变慢甚至瘫痪。

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5ibCoD5VCvSazaRvKzq2sq3MGl1xyxCbjt4HMQppRyQPy7l65ics2n8xOiaSuGs3LsHAbVibgRsMAZD1RAIIJQx2f0ib0PT9nnZfdmQ/640?wx_fmt=png&from=appmsg)

## 常见的几种触发场景

1. 员工自己手动改IP（最常见）

想临时测试、连投影仪、远程协助，结果忘了改回来。

2. 克隆虚拟机/ghost还原没改IP

两台一模一样的虚拟机同时在线，IP完全相同。

3. DHCP服务器出问题

地址池用完了还在分配 → 重复发同一个IP。

路由器重启后把内置DHCP开了，而公司还有一台Windows DHCP服务器，两个同时发地址。

4. 打印机/摄像头等物联网设备

出厂默认IP是192.168.1.100，忘记改就接入公司网络。

5. 极少数恶意情况

有人用工具伪造ARP，冒充网关（做中间人攻击）。

## 怎么快速判断是不是IP冲突？

简单几步就能基本确认：

1. 打开命令提示符（Windows键+R → cmd），输入：

```
arp -a
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5ibBhZAsqJz64pQBIAvzHozuH9h9oqEE9SF1SiaMDNqXVonedlkibDPribsat2d12NdlMXGcWrjTqkyWGqdv83ibiaAo3qgaibQBNk6IE/640?wx_fmt=png&from=appmsg)

看同一个IP下面是否出现多个不同MAC地址。

2. Ping网关（通常是192.168.1.1或你知道的那个），看是否大量丢包、时延忽高忽低。
3. 用手机或另一台电脑连同一个WiFi/网线，试试能不能正常上网。如果部分设备正常，部分不行，通常是广播域内冲突。
4. 如果有条件，上交换机或路由器后台，看广播包数量是否异常高（每秒几千上万）。
5. 最直接的方法：把怀疑的设备网线拔掉或WiFi关闭，看网络是否立刻恢复。

## 平时怎么预防这种事？

不需要太复杂的方案，日常做这几件事就能大幅降低概率：

* **关键设备用静态IP，并做好记录**

服务器、NAS、打印机、摄像头统一登记IP和MAC，存在表格里。

* **DHCP范围设置合理**

公司有100台设备，地址池就给150-200个，别卡得太死。重要设备做DHCP保留（Reservation），固定分配。

* **新设备接入前检查**

让员工用自动获取IP，别随便手动改。

* **交换机开启简单防护**

如果用的是管理型交换机，打开“DHCP Snooping”和“ARP Inspection”，成本不高但效果很好，能挡掉大部分伪造和重复IP。

* **定期巡检**

用手机App（比如Fing）或电脑软件偶尔扫一下局域网，看看有没有IP、MAC异常重复。

IP冲突这个故障，看起来小，实际影响大，主要因为它破坏了“地址唯一性”这个网络最基础的假设。

大多数时候不是什么高大上的安全攻击，就是人为失误或配置疏忽。但一旦发生，全公司停摆半小时到几小时很常见。所以保持一点点警惕，把基础工作做扎实，就能避免90%以上的类似事件。

有遇到过更离谱的IP冲突故事，欢迎留言交流～

# **---END---** **重磅！网络技术干货圈-技术交流群已成立** 扫码可添加小编微信，**申请进****群。** **一定要备注：****工种+地点+学校/公司+昵称****（如网络工程师+南京+苏宁+猪八戒）**，根据格式备注，可更快被通过且邀请进群 ![](https://mmbiz.qpic.cn/mmbiz_jpg/p8No8ScJKT94LpPQZiap0D6hj7eQmHdDUQEvWdRGMD2ic4JQ2Gq8cibgVt0TgPeRfG7OoP3doq9023GkcecKBCW2A/640?wx_fmt=jpeg) ▲长按加群

![](https://mmbiz.qpic.cn/mmbiz_gif/p8No8ScJKT91zHQia5QWRMJhVxUyF4g3ZAuv0YbUEoiaVCzgE2gQT6eQC0Hx6icUE9HQbqFfVP3sSqbIUksF1Ojrg/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT8cAnqjp2AZ90pLWoO7Ysr6JzXPMqP8qibB5ggPz4amnZicChP8vQExwbEJ1O0BtqiaYuYHicm74DQnbA/0?wx_fmt=png)

网络技术干货圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT8cAnqjp2AZ90pLWoO7Ysr6JzXPMqP8qibB5ggPz4amnZicChP8vQExwbEJ1O0BtqiaYuYHicm74DQnbA/0?wx_fmt=png)

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