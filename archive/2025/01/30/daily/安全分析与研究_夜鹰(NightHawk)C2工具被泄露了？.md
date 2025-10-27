---
title: 夜鹰(NightHawk)C2工具被泄露了？
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490232&idx=1&sn=71a4e338358972fe51261cbc15ddcc02&chksm=902fb590a7583c8670bf284d9d8eb2fb2c3d7608c5cccf3c64a743f4b24808388990b8b5fde4&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-01-30
fetch_date: 2025-10-06T20:11:09.357747
---

# 夜鹰(NightHawk)C2工具被泄露了？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qMBh1U9U33vvXibq0auvy7JX1wv1hYKnkIJtuz3GoNCqFehCKiao1Yujiaw/0?wx_fmt=jpeg)

# 夜鹰(NightHawk)C2工具被泄露了？

原创

pandazhengzheng

安全分析与研究

‍

**‍安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

夜鹰(NightHawk)是一款专门供红队使用的C2工具包，具有高度的免杀特性，由号称世界一流的研发团队MDSec提供技术支持，相关的功能特征，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qM2lTJ2010Vo3srUpCK1KneTS5uXL8xdlI64gs9bXfTbfFBIGKgZvibUw/640?wx_fmt=png)

具有高度可塑性和可配置的代理，具有自定义出口和点对点通信，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qMn3gXJH8EcILva3o3whaZqGGicia3xx9PNncqNkia9dVygf2MZvibEQmgHw/640?wx_fmt=png)

点击式OpSec工件的有效负载生成器，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qMOjKjDyY3S8NXB2K1XtiaJvsr862lP7KBV4xmyWFjDRmrVL0Ta60tSoQ/640?wx_fmt=png)

用于隐秘阶段的隐写术shellcode生成工具，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qMmqhcV7E5CYB28gbxpdjmYh0U1fgkibzfoBnX20lvkicCvdKE5ibWWnU3g/640?wx_fmt=png)

该C2工具每年的订阅费用高达1万美元(真他娘的赚钱，Brute Ratel C2一年才3000美元)，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qMM47eibjDmBQel7EwIZ82kldzXfjrbnDjzLVMwn42JkNy5KT9gNzz6Ew/640?wx_fmt=png)

该C2工具目前只对欧洲、澳大利亚、加拿大、日本、新西兰、挪威、瑞士（包括列支敦士登）和美国等地区进行出售。

白俄罗斯、俄罗斯、乌克兰、中非、中国、朝鲜、伊朗、伊拉克、黎巴嫩、刚果共和国或利比亚的用户无法购买夜鹰(NightHawk)。

笔者此前分析和研究过该C2工具的在野真实攻击样本，近日在逛某社交网站时发现夜鹰(NightHawk)工具被上传到了一些恶意软件分析平台，从平台上下载到该C2工具，分享出来供大家参考学习一下，每年订阅费高达一万美元的C2工具到底长啥样，哈哈哈哈。

NightHawk工具

1.从相关的平台下载该C2工具，解压缩之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qMZf1cldUq8AwmicdvSrDaTcjmoXV3SmoHVNVLaxquRFbB3cZ92peFibpg/640?wx_fmt=png)

2.APIServer目录下的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qMT65UjgyPQiaWib3j5AoLXVAydtYLXjnaygibyH4d9SsxsXD06FoDJIkBQ/640?wx_fmt=png)

3.C2\_Client目录下的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qMHpLcJSmnHxQMptg3tNiaiafG0wjHPMFibKyWz9JurkxVQIib05zSgqMRmw/640?wx_fmt=png)

4.C2Server目录下的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qMxR6y2VmNZTnqMyOiafNaSsFtXThvt1v8lTWRD5ApwvjRQiaAaoJztwdg/640?wx_fmt=png)

5.该C2工具客户端，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qMA2URXGl3eaibiaJ7ukf2PVnKe0SeeXre9SqXC61V7pKLShN7alCCmBeQ/640?wx_fmt=png)

其他内容就不分享了，有兴趣的可以自行去深入研究了，搭建好环境，跑起来生成payload，然后进行相关的c2操作，以及针对工具和payload等进行深度的逆向分析等。

**友情提示：****不要私下问笔者工具的下载链接和下载地址，笔者不分享该工具，也不保证该工具是否包含后门，仅笔者自己做分析和研究使用，提取相关的特征，用于攻防对抗研究，也不会使用该工具进行任何非法操作！如果该工具己经被泄露了，未来可能有人使用该工具进行相关的网络攻击行动，注意防范！**

总结结尾

如果对恶意软件分析感兴趣的，可以加入笔者的全球安全分析与研究专业群，一起共同分析和研究全球流行恶意软件家族。（新年优惠于今天晚上22点过期，每年一次)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmUMvXdiayjkiarLibAQqINU6qMNBH5jB7uicRiau5NziatGMndnhxwlwna95PRpuUrBiagRzcYYYkLYQ3QicQ/640?wx_fmt=jpeg)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXu7cXIY417QzQwV6Ttpc5ZIbicVuNWKM5WVvXtiaN6AYiaDicWUwgCiaFYIQ0BV0aRHicib0xpXGWjEmoyA/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

‍

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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