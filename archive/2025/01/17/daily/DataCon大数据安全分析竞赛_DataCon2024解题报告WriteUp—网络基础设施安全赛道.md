---
title: DataCon2024解题报告WriteUp—网络基础设施安全赛道
url: https://mp.weixin.qq.com/s?__biz=MzU5Njg1NzMyNw==&mid=2247489113&idx=1&sn=f50d636aa1d51351143f9cdf801aedeb&chksm=fe5d0ed9c92a87cf2d0cb0ac85dcfb860d8e5684ae9d60f6eaad2c43357757367e274d6cacf0&scene=58&subscene=0#rd
source: DataCon大数据安全分析竞赛
date: 2025-01-17
fetch_date: 2025-10-06T20:11:03.636606
---

# DataCon2024解题报告WriteUp—网络基础设施安全赛道

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RicNZQMn3FU5bK1JDcdwqMBhaS9JtA4t2v7VvmkkKQE8fNaXucCNhLIeC2sUkeJcQIZ1rYw1zXabaVfNHvj77cQ/0?wx_fmt=jpeg)

# DataCon2024解题报告WriteUp—网络基础设施安全赛道

“ddddns”战队

DataCon大数据安全分析竞赛

2024年11月28日，DataCon2024大数据安全分析竞赛落下帷幕。来自中国科学院信息工程研究所的“ddddns”战队荣获**网络基础设施安全赛道冠军**，本期一起来看看“ddddns”战队的解题报告。

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU5bK1JDcdwqMBhaS9JtA4t27J5Q6z2vRImDjvKA3DIQwpQWbSOHeg1icVLeBlSAwcicicjtbZQJ09R2w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU5bK1JDcdwqMBhaS9JtA4t2JzficYTBFzcPQLzBEqkPke9tMuicww4iaIND5M8xUsz4oVMEArg0ic47Ww/640?wx_fmt=png&from=appmsg)

**1 DNS开放解析器识别与攻击利用**

**1.1 Q1：开放解析器发现（100分）**

题目要求利用网络扫描和探测技术发现给定网段（172.19.0.0/16）内，作为开放DNS解析器的主机。开放DNS解析器是指能够接受来自外部IP地址的DNS查询请求并返回响应的DNS服务器。考虑向给定网段全部IP发送DNS查询，如果能够返回合法的DNS响应，则认为该服务器为开放解析器，并记录其IP地址。

使用Python的dnspython库向172.19.0.0/16网段内全部IP发送关于google.com的A记录的DNS查询，总计获取72个能够解析成功并返回合法响应的IP，记为开放解析器。

**1.2 Q2：开放解析器版本识别（96.33分）**

题目要求识别Q1中扫描得到的开放解析器的软件及版本，DNS解析器的版本识别可以通过两种主要方法：一是直接查询其提供的版本信息（如version.bind）；二是根据其特定行为或特性来推断版本。通过结合这两种方法，可以有效提高版本识别的准确性和覆盖范围。

首先通过version.bind命令获取解析器的版本信息。使用Dig工具对目标解析器执行查询，指定version.bind和CHAOS类，检查解析器返回的版本信息。如果返回明确的版本号，则记录下来，得到65个返回明确版本信息的结果，另外9个系统提示关注版本特性。

因此，对于未直接提供版本信息的解析器，基于其行为特性进一步分析。首先通过向全部解析器发送空报文，观察不同软件返回的错误响应，分析不同软件返回结果的差异可确认余下9个解析器为Bind9。随后关注Bind 9不同软件特性差异，收集不同版本的官方文档，综合大模型和手工分析得到Bind9版本差异表。

|  |  |  |
| --- | --- | --- |
| 特征 | 9.16 | 9.18 |
| 胶水缓存 | 存在 | 弃用 |
| 陈旧缓存 | 开启 | 弃用 |
| --disable-silent-rules | 可选 | 不可选 |
| --enable-backtrace | 可选 | 不可选 |
| --enable-shared | 可选 | 不可选 |
| --enable-native-pkcs11 | 可选 | 不可选 |
| --with-geoip2 | 功能失效但可选 | 不可选 |
| --with-libjson | 功能失效但可选 | 不可选 |
| --with-libnghttp2 | 功能失效但可选 | 不可选 |
| --with-libtool | 功能失效但可选 | 不可选 |
| edns中的最大udp长度 | 4096 | 1232 |

表1 Bind9 软件版本差异表（部分）

最终选择以EDNS支持的UDP数据包大小限制值作为判断依据对Bind9软件版本进行区分：

* BIND 9.16及之前的版本默认的UDP数据包大小限制为4096字节。
* BIND 9.18默认的UDP数据包大小限制为1232字节。

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU5bK1JDcdwqMBhaS9JtA4t2Cud2tvIhdxZUGkhY8ILxdlxvjS7yYEv5w7icibUpHU5UmibiaYjHDZGyMA/640?wx_fmt=png&from=appmsg)图1.2.1 不同Bind版本之间的特性差异

根据该特征，可以将未知解析器与已知版本特性对应，完成全部DNS解析器版本识别。

**1.3 Q3：拒绝服务攻击模拟（96.98分）**

攻击目标为172.19.0.5（之后修改为172.18.0.5），观察附件中提供的域名解析记录（check\_fqdn.pcap）发现目标解析器为权威服务器，负责解析的域名有：victim.com，jtfgzlm.com，jthmfgz.com，通过在攻击环境中查询pcap中出现的所有域名的二级域名的NS记录，得到的查询结果也可以验证该结论。

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU5bK1JDcdwqMBhaS9JtA4t2Xc7sib7anhDmkicDgSBfEjibiaxG9hyfJdo6PksNfBaKDkr4iaUunTBZsew/640?wx_fmt=png&from=appmsg)图1.3.1 NS记录查询结果

总体而言，发现如下五种攻击方式，同时为了提升攻击效率，针对不同的攻击方式选择了具有特定特征的解析器以最大化到攻击目标的流量，进而进行攻击实现。

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU5bK1JDcdwqMBhaS9JtA4t2aHicIR0qRgZAjwOqWAeeIMO5W2gWrT3Bg35gawwBzx10CyPPNZTvw4Q/640?wx_fmt=png&from=appmsg)图1.3.2 攻击方法概览

**首先关注目标服务器负责解析的域名，对check\_fqdn.pcap文件进行分析，判断有以下四类攻击方式。**

**1.错误配置的NS循环解析链**

分析check\_fqdn.pcap文件中的域名解析记录发现，从域名a.qwe.com的查询开始，解析器不断返回NS记录，形成NS解析链，其中包括需要向目标解析器查询的ins.victim.com（i指a、b、c等）。

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU5bK1JDcdwqMBhaS9JtA4t2OgnrQbd0MiaL5lVlJo6ADvG4bWeCAH6Fib6LFTYT97lWWxrPfiast3xkQ/640?wx_fmt=png&from=appmsg)图1.3.3 查询域名触发a.qwe.com触发的NS解析记录

编写Python代码提取相关记录，得到如下NS解析链：

```
a.qwe.com.-> ans.victim.com. -> b.qwe.com. -> b.asd.com. -> bns.victim.com. -> c.qwe.com. -> c.asd.com. -> cns.victim.com. -> d.qwe.com. -> d.asd.com. -> dns.victim.com. -> e.qwe.com. -> e.asd.com. -> ens.victim.com. -> f.qwe.com. -> f.asd.com. -> fns.victim.com. -> g.qwe.com. -> g.asd.com. -> gns.victim.com. -> h.qwe.com. -> h.asd.com. -> hns.victim.com. -> i.qwe.com. -> i.asd.com. -> ins.victim.com. -> i1.qwe.com. -> i1.asd.com. -> i1ns.victim.com. -> i2.qwe.com. -> ...i10.asd.com. -> i10.qwe.com. -> i9ns.victim.com. -> i9.asd.com. -> i9.qwe.com. -> i8ns.victim.com. -> i8.asd.com. -> i8.qwe.com. -> i7ns.victim.com. -> i7.asd.com. -> i7.qwe.com. -> i6ns.victim.com. -> i6.asd.com. -> i6.qwe.com. -> i5ns.victim.com. -> i5.asd.com. -> i5.qwe.com. -> i4ns.victim.com. -> i4.asd.com. -> i4.qwe.com. -> i3ns.victim.com. -> i3.asd.com. -> i3.qwe.com. -> i2ns.victim.com. -> i2.asd.com. -> i2.qwe.com. -> i1ns.victim.com. -> i1.asd.com. -> i1.qwe.com. -> ins.victim.com. -> i.asd.com. -> i.qwe.com. -> hns.victim.com. -> h.asd.com. -> h.qwe.com. -> gns.victim.com. -> g.asd.com. -> g.qwe.com. -> fns.victim.com. -> f.asd.com. -> f.qwe.com. -> ens.victim.com. -> e.asd.com. -> e.qwe.com. -> dns.victim.com. -> d.asd.com. -> d.qwe.com. -> cns.victim.com. -> c.asd.com. -> c.qwe.com. -> bns.victim.com. -> b.asd.com. -> b.qwe.com. -> ans.victim.com.
```

可以看到NS解析链最终回到ans.victim.com，形成循环。

因此，向开放解析器查询NS解析链中的任意域名A、AAAA、TXT、MX、CNAME即可触发NS循环解析，并产生大量发往目标服务器的查询，实现对目标服务器的拒绝服务攻击。

对于该类攻击，利用符合以下条件的解析器可以实现更好的攻击效果：①无缓存或缓存时间短，增加解析器的外部依赖，使其多次向权威服务器（目标服务器）发起查询；②超时重试次数高，多次重复尝试对NS记录中域名地查询，使得解析器可以更多次地向目标服务器发起查询。

**2.NS记录→no such name**

分析check\_fqdn.pcap文件中的域名解析记录发现，存在一条长度为2444的NS记录，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU5bK1JDcdwqMBhaS9JtA4t2fEed4hibWMOvH1FMszyeUGLS0Ekhaicibticx5uj37G3O30HcY2KWNqNxQ/640?wx_fmt=png&from=appmsg)图1.3.4 长度为2444的NS解析记录

于是对域名health.health.com的相关解析记录进行分析，结果如下表所示。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **序号** | **报文类型** | **记录类型** | **记录值** | **源→目的** | **备注** |
| 1 | query | A | health.health.com | 3→112 |  |
| 2 | query | NS | health.com | 112→2 |  |
| 3 | response | NS | ns1.health.com | 2→112 |  |
| A | 172.19.0.11 |  |
| 4 | query | AAAA | ns1.health.com | 112→254 |  |
| 5 | response | NS | ns1.com | 254→112 |  |
| A | 172.19.0.2 |  |
| 6 | query | A | health.health.com | 112→11 |  |
| 7 | response |  |  | 11→112 | 未返回结果 |
| 8 | query | AAAA | ns1.health.com | 112→2 |  |
| 9 | response | NS | ns1.health.com | 2→112 |  |
| A | 172.19.0.11 |
| 10 | query | A | health.health.com | 112→11 |  |
| 11 | response | NS | health1-100.victim.com | 11→112 |  |
| 12 | query | A/AAAA | health1.victim.com | 112→5 |  |
| 13 | response |  | no such name | 5→112 | 未查询到结果，继续查询其它NS记录 |

因此，向开放解析器查询域名***health.health.com***和***healthi.health.com***（i为1-100）的随机子域名的因此，向开放解析器查询NS解析链中的任意域名A、AAAA、TXT、MX、CNAME即可触发NS循环解析，并产生大量发往目标服务器的查询，实现对目标服务器的拒绝服务攻击。

对于该类攻击，利用符合以下条件的解析器可以实现更好的攻击效果：①无缓存或缓存时间短，增加解析器的外部依赖，使其多次向权威服务器（目标服务器）发起查询；②超时重试次数高，多次重复尝试对NS记录中域名地查询，使得解析器可以更多次地向目标服务器发起查询。

**3.错误配置的CNAME循环解析链**

分析check\_fqdn.pcap文件中的域名解析记录发现，从对域名a.ieka.com的查询开始，解析器不断返回CNAME记录，形成CNAME解析链，其中包括需要向目标解析器查询的x.victim.com（x指a、b、c等）。

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU5bK1JDcdwqMBhaS9JtA4t2pWym3jXnoVyOhVPSNehGNZjKyPF3YbBrGEd42CsVibg6X2V2ibt6MGyw/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU5bK1JDcdwqMBhaS9JtA4t2nDCo42NL6BvOVBlicfgJghKcFeM0VzNVwjj7Z23FnQ7DTXLPWgXkdWA/640?wx_fmt=png&from=appmsg)图1.3.5 CNAME解析链

编写Python代码提取相关记录，得到如下CNAME解析链：

```
a.ieka.com. -> a.yumlly.com. -> a.losers.com. -> a.victim.com. -> b.yumlly.com. -> b.losers.com. -> b.victim.com. -> c.yumlly.com. -> c.losers.com. -> c.victim.com. -> d.yumlly.com. -> d.losers.com. -> d.victim.com. -> d1.yumlly.com. -> d1.losers.com. -> d1.victim.com. -> d2.yumlly.com. -> d2.losers.com. -> d2.victim.com. -> d3.yumlly.com. -> d3.yumlly.com. -> d2.victim.com. -> d2.losers.com. -> d2.yumlly.com. -> d1.victim.com. -> d1.losers.com. -> d1.yumlly.com. -> d.victim.com. -> d.losers.com. -> d.yumlly.com. -> c.victim.com. -> c.losers.com. -> c.yumlly.com. -> b.victim.com. -> b.losers.com. -> b.yumlly.com. -> a.victim.com. -> a.victim.com. -> a.losers.com. -> a.yumlly.com.
```

可以看到，CNAME解析链最终回到a.yumlly.com，形成循环。

因此，向开放解析器查询CNAME解析链中的任意域名的随机子域名的A、AAAA、TXT、MX、CNAME、NS记录即可触发CNAME循环解析，并产生大量发往目标解析器的查询，实现对目标解析器的拒绝服务攻击。

对于该类攻击，利用符合以下条件的解析器可以实现更好的攻击效果：①无缓存或缓存时间短，增加解析器的外部依赖，使其多次向权威服务器（目标服务器）发起查询；② 允许较长CNAME链，部分解析器对递归深度有所限制，在达到一定次数时会停止查询，当解析器允许较长地CNAME链时，则可以使其更多次地向目标服务器发起查询。

**4.jtfgzlm.com & jthmfgz.com（类似五叉树攻击）**

分析check\_fqdn.pcap文件中的域名解析记录发现，存在大量与jtfgzlm.com及jthmfgz.com的子域名相关的解析记录，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU5bK1JDcdwqMBhaS9JtA4t2CjUIo6nCkuoeo4zRsTq2icM8T4icMhnSv9lxclglwicRL6ASxZ9I0sE4Q/640?wx_fmt=png&from=appmsg)图1.3.6与jtfgzlm.com及jthmfg...