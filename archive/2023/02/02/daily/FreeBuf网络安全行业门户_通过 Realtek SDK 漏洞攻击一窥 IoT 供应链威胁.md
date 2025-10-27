---
title: 通过 Realtek SDK 漏洞攻击一窥 IoT 供应链威胁
url: https://www.freebuf.com/articles/network/356260.html
source: FreeBuf网络安全行业门户
date: 2023-02-02
fetch_date: 2025-10-04T05:29:20.078389
---

# 通过 Realtek SDK 漏洞攻击一窥 IoT 供应链威胁

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

通过 Realtek SDK 漏洞攻击一窥 IoT 供应链威胁

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

通过 Realtek SDK 漏洞攻击一窥 IoT 供应链威胁

2023-02-01 15:49:31

所属地 北京

根据 Unit 42 的监测，大多数月份利用单个漏洞的攻击不会超过攻击总量的 10%。但研究人员发现，2022 年 8 月至 2022 年 10 月间利用 Realtek Jungle SDK 远程代码执行漏洞（CVE-2021-35394）的攻击却占到了攻击总量的 40%。

截至 2022 年 12 月，研究人员一共监测到 1.34 亿次利用该漏洞的攻击，其中大约 97% 都是发生在 2022 年 8 月之后。

由于 CVE-2021-35394 漏洞影响来自 66 个不同厂商的近 190 种型号的设备，攻击者就利用该漏洞在全球范围内对智能设备进行大规模攻击。

## 漏洞概述

CVE-2021-35394 漏洞于 2021 年 8 月 16 日被公开披露，由于许多 IoT 设备厂商都使用 Realtek 芯片组，该远程命令执行漏洞是一个典型的供应链安全问题。

在野存活量较大的易受攻击设备与厂商如下所示：

![image.png-16.8kB](https://image.3001.net/images/20230201/1675237771_63da198b722fa1cfc0600.png!small)易受攻击的设备数量

根据在野攻击情况，一共有以下三种类型的 Payload：

① 执行 Shell 命令，连接恶意 IP 地址并自动下载执行恶意软件，主要是 Mirai 恶意软件：

![image.png-32.5kB](https://image.3001.net/images/20230201/1675237771_63da198bf0b577e6520c8.png!small)Payload

② 直接将二进制 Payload 写入文件并执行：

![image.png-700kB](https://image.3001.net/images/20230201/1675237772_63da198ccff37d2ff56cb.png!small)Payload

③ 直接重启服务器以实现拒绝服务：

![image.png-10.8kB](https://image.3001.net/images/20230201/1675237774_63da198e2ff9e4d9acd62.png!small)Payload

## 恶意软件

在野利用该漏洞的大多数都是 Mirai、Gafgyt 与 Mozi 等知名的恶意软件家族，也有使用 Golang 开发的新兴僵尸网络 RedGoBot 牵扯其中。

RedGoBot 在 2022 年 9 月首次被发现，攻击者使用 wget 下载恶意软件：

> hxxp://185.216.71[.]157/Bins\_Bot\_hicore\_amd64
> hxxp://185.216.71[.]157/Bins\_Bot\_hicore\_arm64
> hxxp://185.216.71[.]157/Bins\_Bot\_hicore\_arm
> hxxp://185.216.71[.]157/Bins\_Bot\_hicore\_mips
> hxxp://185.216.71[.]157/Bins\_Bot\_hicore\_mips64
> hxxp://185.216.71[.]157/Bins\_Bot\_hicore\_ppc64
> hxxp://185.216.71[.]157/Bins\_Bot\_hicore\_ppc64le
> hxxp://185.216.71[.]157/Bins\_Bot\_hicore\_s390x
> hxxp://185.216.71[.]157/Bins\_Bot\_hicore\_mipsle
> hxxp://185.216.71[.]157/Bins\_Bot\_hicore\_mips64le

2022 年 11 月发现的 RedGoBot 第二波攻击，攻击基础设施切换到 185.246.221[.]220。

> hxxp://185.246.221[.]220/Bins\_Bot\_hicore\_s390x
> hxxp://185.246.221[.]220/Bins\_Bot\_hicore\_ppc64le
> hxxp://185.246.221[.]220/Bins\_Bot\_hicore\_ppc64
> hxxp://185.246.221[.]220/Bins\_Bot\_hicore\_mipsle
> hxxp://185.246.221[.]220/Bins\_Bot\_hicore\_mips
> hxxp://185.246.221[.]220/Bins\_Bot\_hicore\_arm64
> hxxp://185.246.221[.]220/Bins\_Bot\_hicore\_arm
> hxxp://185.246.221[.]220/Bins\_Bot\_hicore\_amd64

该僵尸网络支持的 C&C 命令：

| 命令 | 描述 |
| --- | --- |
| exec | 远程命令执行 |
| attack | 发起 DDoS 攻击 |
| kill-bot | 终止执行 |
| update-bot | 进行更新（暂不支持） |

收到攻击指令后，可以通过 HTTP、ICMP、TCP、UDP、VSE 与 OpenVPN 等协议进行 DDoS 攻击：

![image.png-41.7kB](https://image.3001.net/images/20230201/1675237774_63da198ea6e6a98b22cef.png!small)支持的攻击类型

## 攻击源分析

从 2021 年 8 月到 2022 年 12 月，共监测到 1.34 亿次 CVE-2021-35394 漏洞利用攻击，其中 97% 发生在 2022 年 8 月后。攻击源涉及 30 多个国家和地区，美国是最大的攻击来源，占到总量的 48.3%。越南、俄罗斯、荷兰、法国、卢森堡和德国也名列前茅：

![image.png-48.1kB](https://image.3001.net/images/20230201/1675237775_63da198f54c62925eb706.png!small)攻击来源分布

随时间变化的攻击趋势如下所示：

![image.png-189.5kB](https://image.3001.net/images/20230201/1675237776_63da19907e293efeb2fd7.png!small)攻击趋势变化

2022 年 9 月与 10 月，攻击达到顶峰。值得注意的是，来自俄罗斯的攻击 95% 都针对澳大利亚。

从 2022 年 8 月到 2022 年 12 月，针对 CVE-2021-35394 的攻击占总攻击的百分比如下所示：

![image.png-33.8kB](https://image.3001.net/images/20230201/1675237777_63da199185b553b7dcea7.png!small)各国该漏洞的攻击占比

以下 IP 地址是攻击最频繁的攻击者：

![image.png-53.6kB](https://image.3001.net/images/20230201/1675237778_63da1992266f6b9580478.png!small)攻击频度排名

分析了所有的 Payload，出现频率最高的 URL 及其攻击源如下所示：

![image.png-95.7kB](https://image.3001.net/images/20230201/1675237778_63da1992eddb4bf625d11.png!small)URL 频度排名

## 结论

通过 CVE-2021-35394 的在野攻击情况可以看出，攻击者对供应链漏洞非常感兴趣。由于普通用户非常难以识别和修复这些漏洞，造成影响面非常广。

## IOC

> 199[.]195[.]251[.]190
> 172[.]81[.]41[.]196
> 103[.]149[.]137[.]124
> 103[.]149[.]137[.]138
> 46[.]249[.]32[.]181
> 69[.]67[.]150[.]36
> 103[.]149[.]137[.]192
> 45[.]125[.]236[.]14
> 173[.]247[.]227[.]66
> 173[.]247[.]227[.]70
> 185[.]122[.]204[.]30
> 45[.]95[.]55[.]188
> 2[.]58[.]113[.]79
> 45[.]95[.]55[.]24
> 45[.]95[.]55[.]218
> 45[.]95[.]55[.]189
> 193[.]142[.]146[.]35
> 37[.]139[.]129[.]11
> 78[.]135[.]85[.]70
> 45[.]137[.]21[.]166
> 195[.]178[.]120[.]183
> 195[.]133[.]81[.]29
> 5[.]253[.]246[.]67
> 45[.]61[.]184[.]133
> 45[.]61[.]184[.]118
> 149[.]5[.]173[.]33
> 163[.]123[.]143[.]226
> 45[.]61[.]188[.]148
> 103[.]207[.]38[.]165
> 45[.]13[.]227[.]115
> 176[.]97[.]210[.]147
> 163[.]123[.]143[.]200
> 185[.]44[.]81[.]62
> 38[.]22[.]109[.]7
> 147[.]182[.]132[.]144
> 205[.]185[.]126[.]88
> 209[.]141[.]51[.]43
> 198[.]98[.]52[.]213
> 45[.]95[.]55[.]185
> 20[.]249[.]89[.]181
> 3[.]235[.]28[.]168
> hxxp://185.205.12[.]157/trc/TRC[.]mpsl
> hxxp://172.81.41[.]196/trc/TRC[.]mpsl
> hxxp://135.148.104[.]21/mipsel
> hxxp://199.195.251[.]190/trc/TRC[.]mpsl
> hxxp://37.44.238[.]178/d/xd[.]mpsl
> hxxp://176.97.210[.]135/assailant[.]mpsl
> hxxp://198.98.56[.]129/trc/TRC[.]mpsl
> hxxp://141.98.6[.]249/billy[.]sh
> hxxp://185.216.71[.]157/Bins\_Bot\_hicore\_mipsle
> 26e96945ee32199536d4c85124a24c28e853b557eb31f3907d19f08b9798dff4
> 1967370203138b9324f11c5cb3fd15ac8d2f0c585373486614600b676a4e2641
> 78953c71318fb93fa90607039bceb48f2746a8abfa3a9a8914c8fdc48ebf55df
> 57d39a6a88093c9e1fbc1626105d714be92680bdf666279b7663bcaaf7fa7e6e
> 78b55d3f1b34f1154a28ce4fc855252bc3104a07944053facf6acce9195b2e77
> 81e581ed06515af959c8477442243f20baa77c0e54a1054542900936c6e81ff5
> ab3de77616b4d85f032a226da6c3629de4a8f1c1b4d32674c1bed30afb9419e1
> a877b4e71c8f2f4ab6915cbe8c57c82ac12331e183f7cbda2de4dc3780a50379
> 26e96945ee32199536d4c85124a24c28e853b557eb31f3907d19f08b9798dff4
> 5e647d4991f9d339e6e83cee6168915e1e2c9fac0cddc53d3083cbc96a278035
> 6bca8cf5e48e819179f8473e4e600da2c1ef00802bf1744885dcb5ad56618943
> bc03af5c06a7ff6774688e8d71f6d06e0d402f4f86d5b23969bc53d5eab3e522
> 67f73e1efa3c3a05e896567dfb2cef56e9b5eb33283a13e5934900030357e7e6
> ebfedbcf428215d34d8f876fb9c5658048dbb4c5607f328ae155bf26a292b38d
> e0fd14114737e4a599f0769683de4faf54cefae1cc106d9f475aa23bdbf5a753
> 5967a4889b54b97adbb6b949ffd590fa416599326eb3432f40fa142aab1df795
> ff8a1abcd4fa94ffc0f1f43a92f816e6bd08272ec54d748cf004c3ef1323d5d9
> 080a64d595ff246d01b920d5010cffcb4ac56f224acdec32ee3eab08099c6a7b
> e1d3adcb85298a08973b7ae6702cc4830d20ebde98e2eac85179c1bbba3ef7ac
> edec8e8d4c2ec0c489e4c5dbb89994c223f29e8d4470825bd488bf1a44e42751
> 28d6dce95ffb8186ac8c611dee0681cca028bbf93365e4f0c7c67c235d3034a3
> 97878c28d915e2b56e7c06436d209a9198eb0c50bdfb1fd4602e9e95b5eb4321
> 637dc2a8baf2a46ffe872aedc823ab766b4a9fbab129b2c7dc9513ba8ee712bc
> 0d2c3120464184610ac939c34e5309968bd7b81255708307d545d742f3468930
> f3a3e90ea713215a4d30f0f142d6ef0f1ed72b246ee297b8bba64921dbf4300c
> 3f8b5887ae0ef8b51845bf0f2996c4f9891cdc0724b7d0ccc3dbc1b4cdae11a2
> 1a70ceb57768d3e027e307abd09548f151a8d6da72532f1b88e9813eaf0bdad2
> 2ef3040947c9d51317e103457a6613ac9297cb610b3691ef6d440f15cb36a9ed
> 9b7eb2cf51d806076e1662ca4ad800c1de421234c19fbea44b56eb47cc616fd8

## 参考来源

> [Unit 42](https://unit42.paloaltonetworks.com/realtek-sdk-vulnerability/)

# 漏洞分析 # 物联网 # 供应链安全

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

漏洞概述

恶意软件

攻击源分析

结论

IOC

参考来源

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏...