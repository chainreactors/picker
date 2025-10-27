---
title: Mylobot僵尸网络团伙近期活动分析
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247507362&idx=1&sn=4743369899053b402f8e32093ef26829&chksm=ea662ad5dd11a3c35b83fbe3ccf3a979dd6927faae5b9fbda4f67d1a03d2efdcb455f6f6b5fd&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2023-08-01
fetch_date: 2025-10-06T17:01:56.806135
---

# Mylobot僵尸网络团伙近期活动分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhSgGiccumWAiaBYBgKbQy5TbYiaFH324CzNBPmRHOgC8YYxpHPCzUIzIXg/0?wx_fmt=jpeg)

# Mylobot僵尸网络团伙近期活动分析

原创

威胁情报中心

奇安信威胁情报中心

Mylobot僵尸网络是一个针对Windows操作系统的僵尸网络家族，它曾使用内嵌大量Fake-DGA域名的方式来对抗传统黑名单检测技术，我们在2020年发布了一篇文章《Mylobot僵尸网络依旧活跃，C2解密流程揭露》讨论了内嵌域名的解密方法，并提供了进行批量解密的思路。而该团伙至今仍处于活跃状态，我们对其运营的恶意软件进行了一些梳理分析。

Mylobot僵尸网络由Deepinstinct公司在2018年发现并命名，其文章里提到的主要是mylobot-proxy恶意软件，mylobot-proxy主要功能是网络代理。我们2020年的解密分析也是针对mylobot-proxy样本的，而事实上，mylobot-proxy仅仅是Mylobot团伙运营的恶意软件之一，其运营的主要恶意软件还包括mylobot-core等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhdMjVhUicRgcgLwSDU2OSriczXFiaa9yHNuMPGZiajdKeE6OTzcy4jF4ibFA/640?wx_fmt=png)

Packer-Shellcode

Mylobot使用的所有恶意软件都由Packer-Shellcode打包加载，其内置了加载Shellcode所需的WindowsAPI名称哈希值，并通过这些哈希值获取对应API地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhA7DZJOEDSib9TSf5Cc1ia7rgelrJOtFg1c0AZyB0s0UicMs4qicIaDhJ4w/640?wx_fmt=png)

其通过RC4解密全0数据，得到一串字节列表，使用字节列表作为 Key 逐字节与资源中的密文进行逻辑运算得到Shellcode与PE文件，Shellcode重新创建一个进程作为宿主进程，然后挖空进程并映射为解密出的这个PE文件。解密出的PE文件就是Packer-Shellcode的下一阶段恶意软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhSz3OSvjGdf13PsqM3SicTqTwtuIVwBqOeYwCRlSaibJqwBkL5ZGhlZdQ/640?wx_fmt=png)

恶意软件加壳无非就是为了规避直接被查杀，但是Mylobot团伙并没有对其使用的Packer进行过更新，目前我们捕获到的最新的Packer-Shellcode与2017年版本并没有什么不同之处，其在VT的检出率也是比较高的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhVHKeQUlYE20lw9icmSbArc4Vh5En96z3JEgEkhheZODW3D7nYgKicxjw/640?wx_fmt=png)

mylobot-proxy

mylobot-proxy将失陷机器变为一台网络代理机器节点，通过C2下发代理任务进行流量转发，这个恶意软件也是Mylobot团伙主要的盈利软件。它也由Packer-Shellcode工具加载，但是其本身又由一个控制器Loader控制，这种层层套娃的加载形式可以概况为如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhXiaEGQdIurZx3qckiaxMnjSe0EURRSBlARSaMiaKTeTZfMEnrMiaFeAwIQ/640?wx_fmt=png)

早期的mylobot-proxy内嵌了大量Fake-DGA名，而攻击者仅会注册部分域名作为真正的C2，此举虽然可以一定程度上防止域名被置黑名单，但也会带来另一个弊端，其他分析人员也可以选择部分域名注册，进而对僵尸网络进行规模评估，甚至是接管僵尸网络。在我们的视野中，2022年更新的mylobot-proxy就已不再使用Fake-DGA技术.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhPffL1RurgMuXlha7y2Hb0jQBcYEZItwicLjoSlcP0zTicicDXWH9bW1YA/640?wx_fmt=png)

mylobot-proxy实际连接的域名为m<0-42>.格式，其中比较特殊的是m0子域名。在mylobot-proxy的指令处理部分，有两个特权指令——7、8号指令，这两条指令分别表示从后续载荷、指定URL下载执行新一阶段的恶意软件，这两条指令主要用于更新mylobot-proxy软件。我们目前捕获到的mylobot-proxy的版本为2023年3月，通过其特殊的软件更新机制，我们对其内置的3个域名的m0子域进行分析，暂未发现这些域名绑定过IP，这表明目前mylobot-proxy最新版本为2023年3月更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhF8Vukycp8zicDMs9iaxey8vFET0BicFbPQqZnxDaUltdK4Xj8ejG1wA0Q/640?wx_fmt=png)

mylobot-proxy主要是用于提供代理功能，当僵尸网络规模足够后，攻击者可以将这些资源产品化，化身为代理服务提供商。在今年上半年BitSight指出，Mylobot与bhproxies代理服务有关，我们通过相关分析，得到了与BitSight一致的结论，其关联如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhemFNZo255Cu0h51UxWBYxB5ZC0qsFsgWbc6Bu3QcsqQAjJnnOLD9Sw/640?wx_fmt=png)

client.bhproxies.com是bhproies提供服务的域名之一，其两条解析IP指向大量所属Mylobot团伙资产的域名。而89.39.107.82是bhproxies服务商的代理服务提供节点之一，其更是与Mylobot团伙最新的C2域名m20.onthestage[.]ru的解析一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhY2Y1wQOmXqRBTWTnZwKHJ2d3femra39ibIlSTvdGv01MyCibCicLkSROA/640?wx_fmt=png)

Mylobot团伙在2023年2月底对mylobot-proxy进行了一次C2的更新，统计最新的C2域名连接情况，每个独立IP视为一个失陷机器，我们发现其规模呈现扩张趋势，数据如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMh8LibJ8npG4I1CXR7DTa4e2swzjDjBGy8hozT5aDAM7mCKnBoydl1CWQ/640?wx_fmt=png)

mylobot-core

Core由Packer-Shellcode模块加载，在Mylobot团伙的攻击链中主要充当下载器的作用，mylobot-proxy是Core主要分发的恶意软件。Core同样使用fake-dga域名，且目前最新版本中并未被移除。内嵌的域名使用AES加密，加密使用的Key在mylobot-proxy也出现过。其解密出大量域名端口对，与早期mylobot-proxy域名具有很高的相似性，随后选择这些域名的buy1、v1、up1子域进行连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhxg0RL8DibqJTodtWDP2bQkxe66YYD1DumCuv9LR0RNZNibXRicXyz3BsQ/640?wx_fmt=png)

成功连接上C2域名后，Core首先发送机器的基础信息进行Bot上线。其中一个字段为name\_id，是样本硬编码的一个字符串。称其为mylobot-core的原因就是该团伙曾把这个字段设置为core。我们在2023年7月份捕获的样本中，其id被设置为了feb23，也就是2月23号，这与样本编译时间一致，与mylobot-proxy的更新时间也比较接近。其上线信息结构如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhgSibIIXLRm8X8BMGia49qtMHBJrYrAounWOJfq13bwibBGEDRL87dCdeQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhRQaE8NENCpwhmVDCHaAIia8t7K6J6S8OsefEyQ0zlbKk3HW7Jlf9FicQ/640?wx_fmt=png)

在发送完上线信息后，服务器需同样回复一次上线标识符 \x45\x36\x27\x18，并且需要发送下一阶段的恶意软件的下载信息。下载信息同样采用AES加密，其域名的加密采用同一个Key。后续的恶意软件主要为mylobot-proxy，以下是我们收到的下一阶段的载荷信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhQrrJRDgWtwONTibkxYYIgFKJ1licXe1gtE1KuylWibXmmkYG7T7eTmFbg/640?wx_fmt=png)

mylobot-core主要充当其他恶意软件的下载器角色，除了mylobot-proxy，该团伙还下发过其他恶意软件。minerva-labs曾经在core的指令中检测到Mylobot团伙下发了一个勒索邮件发送器，勒索信内容描述攻击团伙在色情网站投放了木马，记录了失陷者的摄像头与邮件通讯录信息，如果不打钱就发送摄像头录像给失陷者的联系人，让失陷者社死。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhB5VIva625Vul6oGzaLoJFDDxD1H6nnOKYSwLKdicTQLzupoZuHknnqQ/640?wx_fmt=png)

不过我们暂时并未在mylobot-core检测到下发除mylobot-proxy的其他恶意软件，由此可以判断mylobot-proxy仍是该团伙主要运营的重心。

总结

Mylobot团伙虽然被披露了5年之久，但其仍旧处于较活跃的状态，不过从其“主打产品”mylobot-proxy与mylobot-core来看，恶意软件的代码功能并没有什么较大改动，这导致其查杀率相当高。我们猜测这可能是因为Mylobot团伙的运营中心在代理服务的售卖与运营上，从mylobot-proxy频频收到的指令也能印证这一点。从mylobot-core收到的勒索邮件发送器也说明了该团伙还从事有其他黑色产业，不过我们目前尚未发现其他相关联事件，对于Mylobot团伙之后的动向我们将持续跟踪。

IOC

**Download Server**

wipmania[.]net

wipmsc[.]ru

stcus[.]ru

162.244.80.231:80

212.8.242.104:80

51.15.12.156:80

**mylobot-core（部分）**

bcbxfme[.]ru

bmazlky[.]ru

bthmzsp[.]ru

byosnwr[.]ru

cxxhtmb[.]ru

dkqhmbi[.]ru

dldzeoo[.]ru

dlihgic[.]ru

dnfojik[.]ru

**mylobot-proxy（202303-至今）**

onthestage[.]ru

krebson[.]ru

stanislasarnoud[.]ru

参考链接

https://mp.weixin.qq.com/s/5YBvsb\_pZGq\_vxDlTNatEA

https://minerva-labs.com/blog/mylobot-2022-so-many-evasive-techniques-just-to-send-extortion-emails/

https://www.bitsight.com/blog/mylobot-investigating-proxy-botnet

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2AqAgxkehic9AbRLiboBt1ex1wV75t0SMhu06AKiadp2Aon62BM3nfG9axY6PM9OJ6JcbkbxdfvR7GDxGSBqh3HKw/640?wx_fmt=gif)

点击阅读原文至**ALPHA 6.0**

即刻助力威胁研判

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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