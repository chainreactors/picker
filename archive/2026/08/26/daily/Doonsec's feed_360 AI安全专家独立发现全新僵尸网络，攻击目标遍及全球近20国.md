---
title: 360 AI安全专家独立发现全新僵尸网络，攻击目标遍及全球近20国
url: https://mp.weixin.qq.com/s/E8IyOyoAqdcLhfCuG5gWmQ
source: Doonsec's feed
date: 2026-08-26
fetch_date: 2026-08-27T12:10:40.652839
---

# 360 AI安全专家独立发现全新僵尸网络，攻击目标遍及全球近20国

# 360 AI安全专家独立发现全新僵尸网络，攻击目标遍及全球近20国

360数字安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU362NhLdPIDibrhibC5gfZR980tl5kIv8p6m64VHJU1n0pa7WajQ3lticuSKic1icw7xGRNGibTiaibdI7g7Q/640?wx_fmt=gif)**

news

AI安全专家在日常巡检中，发现了一个奇怪的现象：

一组陌生程序，正在主动攻击“银狐”木马的C2服务器。

谁在“黑吃黑”？

沿着这条异常线索，360 AI安全分析专家持续追踪，最终独立发现一个此前从未被曝光的全新僵尸网络。

该僵尸网络由AI驱动编写，支持Windows、Linux双平台，可以针对13种常见网络协议发动攻击。自今年7月出现以来，已对全球至少1311台服务器发起凭据喷射攻击，攻击目标遍及近20个国家和地区。

根据其用于伪装的样本名称，360暂将其命名为“端点僵尸网络”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxMlFsSeFcm15kU32HXJn5lTK9IkibEPXo27WgaBkU6g6VsxnaXbbCFbibba23TaznAMaiczsZRiawUv0pkqHVXmPfhOUFeCdkXOu7g/640?wx_fmt=png&from=appmsg)

**‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍AI巡检“银狐”，意外发现另一伙攻击者‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍**

## 事情起源于一次针对“银狐”木马的日常巡检。

##

360 AI安全分析专家在分析“银狐”C2服务器连接数据时，发现了一组不同寻常的程序：它们并非前来接收控制指令，而是在主动攻击多个“银狐”C2服务器。

AI安全分析专家随即采集相关信息，并从样本库中找出对应样本展开逆向分析。

在反编译过程中，AI先后识别出反调试、日志获取、权限提升、数据加密、证书操作和网络连接等敏感行为。综合研判显示，该样本属于恶意下载器，具备隐蔽运行、持续保活和远程接收指令等能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxMNuHEZh4f0zywnicuUYjx6hgxe0Rtaia4xQYs9RLFK5wSOYa3xW1ZEWm1rvwPthIos32YspG4ibCQuxkOPFHwMAzZPW7ia7cSBUJ0/640?wx_fmt=png&from=appmsg)

更值得警惕的是，“端点僵尸网络”会伪装成curl工具或EDR客户端，并使用AES算法对内部数据进行加密，具有很强的隐蔽性。

其Windows初始投递样本在VirusTotal的检测结果为“0/63”，没有被任何安全厂商标记为恶意；Linux样本此前甚至没有被平台收录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxOknOAgdWEymIcH1MCrEmWMTWXVn0hhX0NfUPllgibRK2GtpgXSQ2cpfYWbo8ic6A2QV5I7R61RuRD2rO4pw8lg1dTSCAW5bWgOk/640?wx_fmt=png&from=appmsg)

**‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍顺藤摸瓜，AI还原完整僵尸网络‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍**

传统检测没有发出警报，但AI安全分析专家没有停下来。

它继续主动挖掘，成功获取控制端下发的指令，并破解其通信加密算法。随后，AI结合安全大数据，对样本、网络连接和攻击行为展开多级关联分析：

> 向上，追出了僵尸网络使用的部署工具和脚本；
>
> 向下，还原了其释放的攻击载荷；
>
> 沿着旁支数据，又发现了支持Linux系统的跨平台部署样本。

最终，AI从最初的一条异常连接出发，拼出了“端点僵尸网络”的完整组件、攻击配置和运行方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxMS8f46kicW9eTedVOqWG9vVGnvk57k79fzBiaCaC4PJR9tqsDNaw0CF5xkxXattEhFbbEUUYIoA5KSYM8nlMvLeGfSSnc6JGldk/640?wx_fmt=png&from=appmsg)

经全面分析确认，“端点僵尸网络”是一个由AI驱动编写的跨平台凭据喷射网络。它采用三层架构展开分布式入侵，支持包括wsman、SSH、RDP、HTTP、FTP、Telnet在内的13种常见网络协议，同时具备信息采集和攻击指令下发能力。

根据AI解密出的攻击数据，当前其主要攻击目标是微软WinRM/GSSAPI普遍采用的Web服务管理协议wsman。360已经发现全球至少1311台服务器正在遭受该僵尸网络的凭据喷射攻击，相关服务器分布在多家主流云服务商，攻击目标覆盖近20个国家和地区。

**‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍当攻防进入“机器速度”，安全也需要一支AI专家队伍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍**

完成分析后，360 AI安全分析专家形成了完整事件报告和处置建议，提交人类安全专家审核，并配合建立控制指令监测机制、开展协同处置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxM4qJJBkF6nibc5cS3shr2zyIfBgLAdUd9kODyrq1wl6Q81bnkh36uGxnb1oRcZpPMXjfLcM94AibbX3WDRQpTFHhvr4EexGzicaE/640?wx_fmt=png&from=appmsg)

从一条异常连接出发，自主分析样本、破解加密通信、展开关联溯源，最终还原一个完整的攻击网络——这次实战说明，AI在安全领域已经不只是帮助人类查看告警、整理信息，而是开始像真正的安全专家一样，围绕目标持续分析、主动探索并完成复杂任务。

面对AI驱动、自动化和规模化的新型攻击，360正将二十余年积累的安全数据、威胁情报、专家知识和实战经验转化为AI能力，打造覆盖安全巡检、威胁研判、样本分析、攻击溯源等不同任务的安全智能体蜂群，并通过多智能体协同，让原本需要多名专家接力完成的复杂工作进入“机器速度”。

未来的网络攻防，不再只是人与人的较量，也将是AI与AI的对抗。安全能力的竞争，也将从单一工具、单点能力的比拼，走向安全大模型、安全智能体与人类专家协同作战的全新阶段。

**当攻击者开始用AI发动攻击，防守者也必须拥有自己的AI安全专家。**

**以AI对抗AI，这场新的攻防已经开始。**

往期推荐

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  | | --- | --- | | **01** | ● [“AI安全报告”首位推荐！360构建智能体全域防护体系](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247586499&idx=1&sn=9f0f70f075ec089ad3aa4c08aae9e67f&scene=21#wechat_redirect) | | ► 点击阅读 | |
| |  |  | | --- | --- | | **02** | ● [ISC.AI 2026 周鸿祎演讲全文：打造中国版“Mythos”，应对网络安全新挑战](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247586322&idx=1&sn=c68961f482c2dc603287457d88414ec8&scene=21#wechat_redirect) | | ► 点击阅读 | |
| |  |  | | --- | --- | | **03** | ● [三项荣誉！360漏洞挖掘智能体登顶华为终端安全贡献榜](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247586269&idx=1&sn=69bbe8ecf24060ed8b241b827f1ed95f&scene=21#wechat_redirect) | | ► 点击阅读 | |
| |  |  | | --- | --- | | **04** | ● [360获国内首个人工智能安全能力认证 智能体安全进入“持证时代”](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247586248&idx=1&sn=08eae8d96a27a1c6e3b6b358160b9db1&scene=21#wechat_redirect) | | ► 点击阅读 | |

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

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