---
title: 【安全圈】基于 Mirai 的 xlabs_v1 僵尸网络利用 ADB 劫持物联网设备发动 DDoS 攻击
url: https://mp.weixin.qq.com/s/cW-yJsBFiPEcAT9FKaWHPQ
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:52:48.483204
---

# 【安全圈】基于 Mirai 的 xlabs_v1 僵尸网络利用 ADB 劫持物联网设备发动 DDoS 攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGsrHZEfwtDTrU5MR7Diap8HtOtOTdoicY9OeyR6C2iaf55Y9NlOaLS8omnQhqZ6ssEpoMoGRwtFoNVFmqpPOrjJEWRHEK9NMg8iaY/0?wx_fmt=jpeg)

# 【安全圈】基于 Mirai 的 xlabs\_v1 僵尸网络利用 ADB 劫持物联网设备发动 DDoS 攻击

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

攻击

网络安全研究人员揭露了一种新的源于 Mirai 的僵尸网络，它自称为 xlabs\_v1，**目标是暴露在互联网上且运行安卓调试桥（ADB）的设备，将这些设备纳入一个可发动分布式拒绝服务（DDoS）攻击的网络。**

详细研究该恶意软件的 Hunt.io 表示，他们在发现位于荷兰的服务器（IP 地址为 “176.65.139 [.] 44”）上有一个无需任何认证即可访问的暴露目录后，发现了这一僵尸网络。

Hunt.io 称，该恶意软件支持基于 TCP、UDP 和原始协议的 21 种洪水攻击变体，包括 RakNet 和类似 OpenVPN 的 UDP 攻击，能够绕过消费级 DDoS 防护。它还被作为一种 “出租 DDoS 攻击服务” 提供，专门针对游戏服务器和我的世界（Minecraft）主机。

xlabs\_v1 引人注目的地方在于，它会搜寻在 TCP 端口 5555 上运行暴露 ADB 服务的安卓设备，这意味着任何默认启用该工具的设备，如安卓电视盒、机顶盒、智能电视等，都可能成为潜在目标。

除了安卓 APK（“boot.apk”），该恶意软件还支持多架构构建，涵盖 ARM、MIPS、x86 - 64 和 ARC，表明它也针对家用路由器和物联网（IoT）硬件。

最终形成的是一个专门构建的僵尸网络，它会从操作员面板（“xlabslover [.] lol”）接收攻击命令，并按需产生大量垃圾流量，尤其针对游戏服务器发动 DDoS 攻击。

Hunt.io 解释说：“该僵尸程序是静态链接的 ARMv7 版本，运行在精简的安卓固件上，通过 ADB shell 粘贴到 /data/local/tmp 目录进行交付。操作员的九种变体有效载荷列表是针对安卓电视盒、机顶盒、智能电视以及出厂启用 ADB 的物联网级 ARM 硬件进行调整的。”

有证据表明，这种 “出租 DDoS 攻击服务” 采用带宽分层定价。这一判断基于一个带宽分析程序，该程序会收集受害者的带宽和地理位置信息。

该组件会向地理位置最近的 Speedtest 服务器打开 8192 个并行 TCP 套接字，持续 10 秒使其饱和，并将测量到的数据传输速率报告回面板。Hunt.io 指出，这样做的目的是为付费客户将每个被攻陷的设备分配到相应的价格层级。

这里需要注意的一个重要方面是，僵尸网络在以 Mbps（兆比特每秒）为单位发送带宽信息后就不再驻留，这意味着由于缺乏持久化机制，操作员必须通过相同的 ADB 利用通道再次感染该设备。

Hunt.io 称：“该僵尸程序不会将自身写入磁盘持久化位置，不会修改初始化脚本，不会创建 systemd 单元，也不会注册定时任务。这种设计表明，操作员将带宽探测视为一种不频繁的集群层级更新操作，而非每次攻击前的预检查，这种退出并重新感染的循环是其设计意图。”

xlabs\_v1 还具有一个 “杀手” 子系统，用于终止竞争对手，以便独占受害者设备的全部上行带宽来发动 DDoS 攻击。目前尚不清楚该恶意软件背后的主谋是谁，但从僵尸程序每个版本中嵌入的 ChaCha20 加密字符串可看出，威胁行为者的绰号是 “Tadashi”。

对共置基础设施的进一步分析发现，在主机 176.65.139 [.] 42 上有一个 VLTRig 门罗币挖矿工具包，不过目前还不清楚这两组活动是否为同一威胁行为者所为。

Hunt.io 表示：“从商业犯罪角度来看，xlabs\_v1 处于中等水平。它比典型脚本小子使用的 Mirai 衍生版本更为复杂，但不如顶级商业出租 DDoS 攻击操作那么复杂。该操作员在价格和攻击种类上竞争，而非技术复杂性。消费级物联网设备、家用路由器和小型游戏服务器运营商是其目标。

与此同时，Darktrace 透露，其蜜罐网络中一个故意配置错误的 Jenkins 实例遭到未知威胁行为者的攻击，他们从远程服务器（“103.177.110 [.] 202”）下载并部署了一个 DDoS 僵尸网络，同时采取措施躲避检测。

该公司表示：“特定于游戏的 DoS 技术的出现，进一步凸显了游戏行业持续成为网络攻击者的广泛目标。这个僵尸网络很可能已经被用于攻击游戏服务器，这提醒服务器运营商要确保采取适当的缓解措施。”

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGEHO4xOUjhtc6oVQNj8MjqykzKODib9zoxEvL9htzaDy3GCCpbcR7acibdQyM6QqkOtdpMHTIbcw6qIia9dVR5uGdsudjpicFOoiaw/640?wx_fmt=jpeg&from=appmsg)

***END***

阅读推荐

[【安全圈】安卓高危0Day漏洞可远程获取Shell访问权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076197&idx=1&sn=f04ddcae84cf9ff13b2696de01ec65eb&scene=21#wechat_redirect)

[【安全圈】上古软件DaemonTools被投毒埋下木马：直接卸载吧 已经没啥用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076197&idx=2&sn=d5866e3f0b1ae35fa7de7fc57defec1d&scene=21#wechat_redirect)

[【安全圈】PHP 结束 30 多年定制许可历史，正式采用 BSD 3-Clause 许可证](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076197&idx=3&sn=9d052ec11e89d8715f365258c5a457f8&scene=21#wechat_redirect)

[【安全圈】Apache HTTP Server 漏洞致数百万服务器面临远程代码执行攻击风险](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076183&idx=1&sn=9d34b2fc14abfd37f943b2df7423829c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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