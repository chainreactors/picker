---
title: Operation（Giỗ Tổ Hùng Vương）hurricane：浅谈新海莲花组织在内存中的技战术
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247513780&idx=1&sn=a2650f77b1b7a4b73b27ec637bef04d1&chksm=ea6641c3dd11c8d58e8cd03792f61e801bc69c868a2c7ccc64826afab019e4e19fa13ab75e3d&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2025-01-21
fetch_date: 2025-10-06T20:10:58.813424
---

# Operation（Giỗ Tổ Hùng Vương）hurricane：浅谈新海莲花组织在内存中的技战术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7XKTUEwzSoVNIOhuNCHqF5RPGxV4Wiajl3cu9fpVJQ9hVwKWmc6XibTow/0?wx_fmt=jpeg)

# Operation（Giỗ Tổ Hùng Vương）hurricane：浅谈新海莲花组织在内存中的技战术

原创

红雨滴团队

奇安信威胁情报中心

概述

新海莲花组织最早出现于2022年中，直到2023年底转入不活跃状态，2024年11月重新活跃并被我们快速制止并披露[1]，在2023年全年新海莲花组织展示出于以往完全不同的技战术，进攻水平也比之前提升很多，该组织使用多个 0day 漏洞针对我国军工、能源、航空等领域开展间谍活动，意图窃取我国能源和军工领域在中东、中亚、非洲、东亚的部署情况。

本文仅作为安全研究，我们不关注初始样本载荷，主要披露新海莲花组织内存插件和间谍目的，天擎EDR可以在内存中精准告警新海莲花组织所有内存插件，我们建议政企客户启用云查功能来发现未知威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7Ey9w4aZ0wpt52aVqdlmQeaeviaTeAQ9P0IT5y9fp3zOIaLybzib53XoQ/640?wx_fmt=png&from=appmsg)

内存技战术

新海莲花组织通过终端软件 0day 漏洞向内网特定终端下发恶意更新，实现供应链攻击。在目前国内错综复杂的安全产品生态下，这种攻击模式是所有 APT 组织的最优解，并不是海莲花组织独有的手法[2]，我们甚至观察到针对国内的勒索软件运营商也有类似的操作，区别在于勒索运营商会向全内网终端下发勒索软件，而 APT 组织则是选择特定的目标终端后下发，新海莲花组织内存技战术如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7QR4SFpV56W5rE3WGS2XibeUwydKhicAaofJTjJIXN7WNyKDicCCaoXGiaQ/640?wx_fmt=png&from=appmsg)

新海莲花组织在 2022-2023 年所使用的 Cobalt Strike 有一个非常明显的特征：

木马运行后会自动将当前的屏幕截图保存为 PNG 格式并发送到 C2 服务器上，如果恰好此时攻击者正处于 RDP 的状态，那么就能在受害者机器上得到一张攻击者双击木马程序的照片：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc78I5T9ibu9LBF4sCa69ZkOmLr10CAKmwM4miaNthUlzsDJaAn4jE5POrg/640?wx_fmt=png&from=appmsg)

Cobalt Strike 注入到系统进程后会在当前进程中内存加载 Rust 特马并回连新的 C2，Rust 特马的分析友商已经有过分析，故不再赘述。接着通过 Process Hollowing 的方式将文件目录收集插件注入到系统进程中。

**文件名收集插件（内存态）**

该插件为 20 KB大小的 Shellcode，首先会获取 Temp 路径，并生成一个 UUID 与路径拼接作为中间文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7y6aibd9716W7tl4H55PnBwk34k3j1d8lao40rlLFu1ZstcBiaLoibyhnQ/640?wx_fmt=png&from=appmsg)

接着会遍历文件，收集受害设备上的指定后缀文件，并将结果与 0xF1 异或后写入文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7enqA3gRiaLibVrr8etf7CBIhpftAZEbE4HuxVJWU7b2rXWdXcBsDJuhQ/640?wx_fmt=png&from=appmsg)

解密后的文件格式如下，会收集文件名和该文件的创建、修改、访问时间。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7Od1XryBKUmnmCC7iaM8jAn5S66f4aSabtVnm4CQNLVZg9d2XSI5xR1Q/640?wx_fmt=png&from=appmsg)

收集的指定后缀如下：pdf、png、jpg、ppt、pptx、one、ini、pfx、config、xmind、conf、ofd、7z、wpt。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7wSwR2ACICOXpozvFaJCWmugRL0oLwoIIdyySF4gfABYbibSAIEIlQVQ/640?wx_fmt=png&from=appmsg)

写入完毕后会重新读取该文件到内存中，并删除该文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7GVr72ATslF7ibkPIViapCaYNq5tXUQSdWJnThibD0a2jfLOgQfrmNpJng/640?wx_fmt=png&from=appmsg)

将读取到的内容重新与 0xF1 解密后，重新进行加密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7ic9bRJsW0HfOzpDbiaibOEcKmbXxtrQcqwhOS1LrQamyTgGwl0y1U6bSQ/640?wx_fmt=png&from=appmsg)

加密算法为 128 位 AES 算法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7t3jNl4ibrbYHcUyQjH2f5HTruh2m555UuEC2HmUZw92RD5TacT4c1Hg/640?wx_fmt=png&from=appmsg)

最后将加密的内容再与 0xF2 异或后写入文件 C:\Programdata\SogouInput.xml中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc71cA7eJoowVCV74xC2CTUTIrXSE2LO7lDQvyzysN5ZICSb20PMQDVEQ/640?wx_fmt=png&from=appmsg)

攻击者会在后端对 xml 文件进行分析，最终挑选出窃取的目标文件，窃取完文档后攻击者如果选择进一步横向移动，一般会通过 Process Hollowing 的方式将管道特马注入到系统进程中。

**管道特马（内存态）**

该管道特马所在的内存块固定大小 0x35000，创建名为 \\.\pipe\InitStarts 的管道循环监听。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7DePf20K6Q9fEJiaQUb8SGkNvB1pMfEZQAJmicpHABl1woibEjicmL0x4MQ/640?wx_fmt=png&from=appmsg)

读取管道中的数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7KnWANbEbHCdXppLfTA2fldARCjzyALSE6jxmHXVYujhrvxN2icKM0Rg/640?wx_fmt=png&from=appmsg)

通信过程中定义了一个结构体，创建线程并将结构体当作参数传入。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc704ic5NWewFW2LWZicM9AmG06s3bV2iafI7Ine35hyXCYfoiad3mibYtkygg/640?wx_fmt=png&from=appmsg)

该线程会持续读取管道中的数据，并将数据解密后传递给工作线程，同时获取工作线程执行后的数据再解密传输到管道中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7tCHqjQJrB1U5VzyQHgJiaGd6B6Azic5l9cXOBgxTDESaLefQFgWPiaFxQ/640?wx_fmt=png&from=appmsg)

加密算法如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7T8gZTzCAbUJbypumKkziaa3hwDXPoUcYTQq7wLuZtDW73msesjOu0Kg/640?wx_fmt=png&from=appmsg)

工作线程中有大量的功能性函数，例如：文件管理、shellcode加载、命令执行等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7k6nX6icpq3DRgEVOL0kjRao2AaQ9HPKMD29HvwucjcGkH3yG94cZ5Vw/640?wx_fmt=png&from=appmsg)

我们观察到新海莲花组织通过管道内存加载了 ssh 登录插件。

**ssh登录插件（内存态）**

该插件功能就是通过内置的账密登录内网 linux 服务器：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7nGricn3D2wyITTLpyqsLiaZLINegkbGXQRrXnoWzISwgq4rKEoSIYfIQ/640?wx_fmt=png&from=appmsg)

密码为弱口令，可以推测攻击者是通过爆破的方式获取到服务器密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7U2Zy755PBsWP6AQHv16q0ZiceWOe7QnGkBE0Me0mciaibE62616P5ENTw/640?wx_fmt=png&from=appmsg)

通过 history 日志可以确认攻击者在浏览服务器上的目录并打包数据。

**双平台特马（内存态）**

新海莲花组织在入侵边界服务器时如：web服务器、防火墙等设备会使用一款 Win | linux 双平台的特马，该特马最早在防火墙上被发现，很长一段时间内我们认为该特马只在边界服务器上部署，但是在一次对抗的过程中发现该特马被注入到 Windows的系统进程中，并且注入时间离 Cobalt Strike 的植入时间晚一周。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7CMXNagPLx4lNWTzQNVqo9LVibYMvzl5w2dB1eSBm6Roo43qlwC1sYuw/640?wx_fmt=png&from=appmsg)

新海莲花组织通过该特马执行 CMD 命令，添加根证书 “certutil -addstore "ROOT" client.cer”，添加完成后选择在磁盘落地 DLL，此时的 DLL 带有数字签名，用于免杀 EDR。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7UibcsdBBOE3jj5j1bicmIItEPUn0rpUjGNiacBuZonzJS8icnN84h2ubmQ/640?wx_fmt=png&from=appmsg)

**杀软对抗**

新海莲花组织似乎是为数不多能够分清楚360安全卫士和天擎EDR两款杀软的APT组织，在此之前很多APT组织都认为只要能够免杀360安全卫士就能够绕过天擎EDR。新海莲花刚开始活动时使用了两种新方法分别针对360安全卫士和天擎EDR，但是很快被我们和友商发现并及时进行对抗。释放名为 propsys.dll，判断加载该 DLL 的进程是否为 360baobiao.exe

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc76q3eP2VSKUiceCSzYILFLcnK6yLfkefbSPTOotoMvKH1R6erPaMuibEA/640?wx_fmt=png&from=appmsg)

DLL 的主要功能通过 DeviceIOCtontol 关闭自保。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc75DnU9kQCVMnu6nj2OUrbsjutvq0yich1gYL2WKtfDspusqzibgDaBUuw/640?wx_fmt=png&from=appmsg)

之后休眠 zhudongfangyu.exe 和 360rps.exe 进程，实现致盲的效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc71cA6VIougfhXTQw2g4B9D464smUWm3ZKbHXewq5yw4ibDzjib28VDSPA/640?wx_fmt=png&from=appmsg)

目前该手法已经无效。

UTC+7

上述复杂的内存 TTP 似乎只是“昙花一现”，从2023年12月份新海莲花转入不活跃状态之后，我们就再也没有观察到类似的技战术，在此之后2024年3月老海莲花继承了其攻击资源又发起了两波 0day 供应链事件，并让我们最终确认攻击者位于 UTC +7 时区，海莲花通过一些渠道购买国内 VPS 服务器将其当作代理一直在请求目标单位的终端管理服务器并挑选要入侵的目标人员。（不止海莲花，在2024年我们观察到几乎所有方向的APT组织都在通过代理公司或者黑产四件套来购买国内 VPS 厂商的资源，将其当作代理和C2，甚至还有找国内人员给木马后门代签数字签名的行为，APT已经深度融入国内黑灰产上下游中，我们建议对国内下游人员进行打击，将这些通道彻底遏制）。

在 UTC+8 的时区下，基于天眼设备可以观察到攻击者每天从早上10点一直工作到晚上19-20点，标准的八小时工作制，到点下班有双休，与国内红队的工作强度相比不太饱和，攻击者唯独在4月18号这一天缺勤，并且第二天“上班”时间较晚。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7bD2XQtrlAlJH1ek33nKeskbuXiaL77evicPibPIjDnmwoZeblJAk0QO3g/640?wx_fmt=png&from=appmsg)

经过搜索发现4月18号为东南亚某国的法定节假日，称之为“雄王节”（Hung Kings/ Giỗ Tổ Hùng Vương）。

目的

目前已经确认攻击者位于东南亚国家，假设其为所在国提供情报服务。在研究其目的时，我们仅挑选终端服务器定向下发的案例来研究，因为攻击者在终端服务器上可以看到目标单位所有的组织架构和人员信息，其挑选的目标终端必然具有定向性，而其他的间谍活动比如批量入侵防火墙、web 服务等都是非定向性的，无法作为研究的数据源。

我们整理了2021-2024年间数起终端下发事件，大部分情况下其目标都聚焦在西南省份的环境和交通数据，以及我国在东亚的能源部署，这些都符合东南亚国家的利益，转折点在新海莲花出现之后，2023-2024年大规模刺探我国能源、军工领域在中亚、中东、北亚、非洲的项目和部署情况，受害终端上甚至包含向境外派遣的人员名单，这些数据并不是东南亚小国能够消化完的，更像是域外大国关注的领域，而新海莲花组织出现的时间又恰好和东南亚某国与域外大国达成网络安全合作的时间点相吻合。

以上只是我们作为网络安全厂商所观察到的事实的陈述，不针对任何国家和个人。

总结

目前，基于奇安信威胁情报中心的威胁情报数据的全线产品，包括奇安信威胁情报平台（TIP）、天擎、天眼高级威胁检测系统、奇安信NGSOC、奇安信态势感知等，都已经支持对此类攻击的精确检测。

参考链接

[1].https://ti.qianxin.com/blog/articles/new%20-trend-in-msi-file-abuse-new-oceanlotus-group-first-to-use-mst-files-to-deliver-special-trojan-cn/

[2].https://mp.weixin.qq.com/s/3bmehaRuvaL5TnvdZXwYWA

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2AqAgxkehic8C3Giamg6Ks60U0OgM1MNc7iaSafcZx0IwnxMSvmf0ic6vndsYbEznsyPniap0vHeByyF6Yae3ulDjnA/640?wx_fmt=gif&from=appmsg)

点击阅读原文至**ALPHA 7.0**

即刻助力威胁研判

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=pn...