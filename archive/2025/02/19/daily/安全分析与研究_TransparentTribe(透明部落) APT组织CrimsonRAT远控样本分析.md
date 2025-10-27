---
title: TransparentTribe(透明部落) APT组织CrimsonRAT远控样本分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247490574&idx=1&sn=01ffe4798637dd2465d3d3b7171b4aaa&chksm=902fb326a7583a30c4e61dde6527c7b77143024a1e40892601805568b72d1d1f9e9bb791b8f8&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2025-02-19
fetch_date: 2025-10-06T20:40:11.102831
---

# TransparentTribe(透明部落) APT组织CrimsonRAT远控样本分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSydZLzgT0ZwB82z3hb8Y8qhbBI1gavaZgDdanjJzXXBN2YzEJw6Z1Bw/0?wx_fmt=jpeg)

# TransparentTribe(透明部落) APT组织CrimsonRAT远控样本分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

TransparentTribe(透明部落) APT组织在2016年2月被Proofpoint披露并命名，也被称为ProjectM、C-Major、APT36，该APT组织被广泛认为来自南亚地区某国，并且与另一个由Paloalto Unit42团队披露的Gogron Group存在一定的关系，曾针对印度国防、政府和教育部门开展网络间谍活动。

TransparentTribe(透明部落) APT组织长期针对周边国家和地区的政府、军队进行定向攻击活动，擅于利用社会工程学进行鱼叉攻击，向目标投递带有VBA的doc、xls等钓鱼文档，执行诱饵文档中的宏代码释放执行CrimsonRAT、PeppyRAT等，窃取目标的相关资料信息。

最近几年TransparentTribe(透明部落) APT组织攻击活动非常频繁，努力研发新的攻击武器，不断的更改其初始进入机制并使用新的定制恶意软件，这表明其正在积极多样化的组合攻击方式以危害更多受害者。

样本分析

1.远控样本采用C#语言编写，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSicssZxlGY6sVoxLvbHAurVytyJPq7s0Xpa8eZTkIUk0ZaKDVBVnbJyQ/640?wx_fmt=png)

2.逆向分析主程序代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSic5JcHJN7M0NJD468CD1jN0aIPf6dpq9uib2lW3akdlMunwmrz0VmxaA/640?wx_fmt=png)

3.远程服务器IP地址为209.127.18.107，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSw7Z29X9icLFacicWDVlymbibh3Xt6PLfW9HLEFS39vetZHKo2ZCLiaqbSg/640?wx_fmt=png)

4.相关的端口号，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSwt93UibtEcuEoVFDHuGXHGCPlZZ7icPicrr0GUPnKcn6KKpXfPiaDJ9v8A/640?wx_fmt=png)

5.C2通信相关指令，与此前发现的攻击样本基本一致，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OScLiaTmic6vM2d3TbulS5cY7WrwC5Hq3yOPz91rKPLZO8XWZwtZ94CrOw/640?wx_fmt=png)

6.获取主机相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSjxrzVOUt9dBwp2Y6VjTowKQrBlZ3ialYsLqWmAFHHicNyRe1lmX3jWhQ/640?wx_fmt=png)

7.设置自启动注册表项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSuYekxJHd15evQexu4xHDLorryW8LOAn6kfN9ticedP7kj0t7CRw1BcA/640?wx_fmt=png)

8.获取主机进程列表信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSq80sw4gfPJ5hQYX4BgXKIuULmU58PJgIYTZOxyDVERcZTKm2jPcvGQ/640?wx_fmt=png)

9.获取主机磁盘目录文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSOOcu4p0icvqmHAr7ibJJhfrOUuBzL1G4QqX0pM2Cx4oqoWiblicPu7aPRw/640?wx_fmt=png)

10.获取主机屏幕截图信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSTibwyFvT6vdtmEhVbKibnKQy23yzk7WUoCCoFvowr04AYqIe0QsodWZQ/640?wx_fmt=png)

11.其他功能点有兴趣的可以自行分析,利用威胁情报平台查询C2地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSt1zsKibbklYOv4E8Q25zicgoO4RLtS5Hib0NUlxbLo1u0vP1cnPBoM3VQ/640?wx_fmt=png)

12.关联到多个CrimsonRAT远控类样本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVuptkmPEhhfbnWlOicKN5OSs3hCDeG7VLp72E7SYx4rVoPH8ZsVm2nt5ibS3cHJOgiaYp8QFwZWDqNg/640?wx_fmt=png)

总结结尾

APT是全球企业面临的最大的安全威胁之一，需要安全厂商密切关注，未来APT组织还会持续不断的发起网络攻击活动，同时也会持续更新自己的攻击武器，开发新的恶意软件变种，研究各种新的攻击技术，使用新的攻击手法，进行更复杂的攻击活动，这将会不断增加安全威胁分析和情报人员分析溯源与应急响应的难度，安全研究人员需要不断提升自己的安全分析能力，更好的应对未来各种威胁挑战，安全对抗会持续升级，这是一个长期的过程。

对高级恶意软件分析和研究感兴趣的，可以加入笔者的全球安全分析与研究专业群，一起共同分析和研究全球流行恶意软件家族，笔者今年打算深度跟踪分析一些全球最顶级的TOP恶意软件家族，这些恶意软件家族都是全球最流行的，也是黑客攻击活动中最常见的恶意软件家族，被广泛应用到各种勒索攻击、黑灰产攻击、APT窃密攻击活动当中以达到攻击目的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXDIda3D6VvFWhqojST24E2rTRBJMYDfYowK8WcvBScfWlJiaYZ5elMdlrREG1LDVODxFQ0Eoy0YLQ/640?wx_fmt=jpeg)

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmW8qYF2seSKglWFKoJdassltn5V5IPUn3OGXsdD4v2nRPg8ZzFAicpXlmlwVmd9KTm4XPkRcXtBEKw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

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