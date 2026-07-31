---
title: 如何用 20 年前的漏洞在几分钟内黑掉数千个数据中心
url: https://mp.weixin.qq.com/s/QBN7A8B8BohcTbVbjtHV-g
source: Doonsec's feed
date: 2026-07-30
fetch_date: 2026-07-31T05:28:58.506956
---

# 如何用 20 年前的漏洞在几分钟内黑掉数千个数据中心

![cover_image](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibcl6VUdqecZszNexwria1snLdwI7FS91UrKFicGicELxVZsuupYztrtxM1VGbWVlaNic3QrCXNEiaWNck2V4d3mtYu7ZupL13icn05nQ/0?wx_fmt=png&from=appmsg)

# 如何用 20 年前的漏洞在几分钟内黑掉数千个数据中心

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 通过扫描全网 3.6 万个暴露在公网的 IPMI 服务，我们发现其中三分之二因一个 20 年前的漏洞（CVE-2013-4786）在登录前就泄露了密码哈希。借助现代 GPU 算力，即便是“唯一”的出厂密码也能在几十秒内被破解。更糟的是，攻击者已经在利用这些接口植入勒索信息了。

## BMC 是什么？为什么它这么要命？

基板管理控制器（BMC）是插在大多数现代服务器主板上的一个独立处理器。你可以把它理解成服务器的大脑之外，还有一个“小脑”。不管主机操作系统是死机、蓝屏还是根本还没装，这个小脑都能正常工作。

它能干什么？远程开关机、挂载虚拟光驱重装系统、刷固件、看传感器温度、改底层配置，这些它全能干。说它是数据中心里权限最高的控制点之一，没毛病。

BMC 通常对外暴露好几个管理入口：老派的 IPMI 协议、新一点的 Redfish API、一个网页管理界面，还有远程控制台和虚拟媒体功能。很多厂商的实现里，这些入口背后用的是同一套用户数据库。也就是说，你在 IPMI 上用的那套账号密码，大概率也能登进网页后台或者 Redfish API。

而问题就出在这里。IPMI 的认证过程，在登录完成之前就可能把密码相关的信息泄露出去，给离线破解留下了口子。

不同厂商管自己那套 BMC 叫不同的名字：惠普的叫 iLO，戴尔的叫 iDRAC，联想的叫 XClarity Controller，超微（Supermicro）有自己的方案，还有一个开源的 OpenBMC 项目在云厂商和超大规模数据中心里用得不少。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibcl6VUdqecZszNexwria1snLdwI7FS91UrKFicGicELxVZsuupYztrtxM1VGbWVlaNic3QrCXNEiaWNck2V4d3mtYu7ZupL13icn05nQ/640?wx_fmt=png&from=appmsg)

▲ 一个典型的 BMC 网页管理界面。BMC 常常同时对外暴露网页、API、控制台和 IPMI 等多个管理入口，背后是同一套高权限管理体系。

BMC 一旦被拿下，防守方就非常被动了。你部署的那些安全工具，绝大多数跑在操作系统层面，盯着内核、容器、业务进程。BMC 完全不在这层信任边界里——攻击者踩着 BMC 在主机底下活动，而上边那些安全软件根本看不到他。

更麻烦的是，BMC 通常不是孤立的。它们坐在一套独立的带外管理网络里，这套网络里的管理员密码经常是重复使用的，流量监控也比生产网弱得多。攻击者完全可以用一台服务器的 BMC 作为跳板，横向移动到其他服务器的管理控制器，把整个数据中心的管理平面变成自己的后花园。

持久化也是个头疼问题。攻击者在 BMC 或固件里种下恶意代码之后，重装系统、换硬盘、甚至常规的应急响应流程都清不掉它。想把机器的信任根恢复回来，得做固件验证、重新刷写，甚至直接换硬件。

## 为什么 AI 基础设施更怕这个？

AI 数据中心把成千上万台高价值的 GPU 服务器集中在一起，背后共用一套管理网络。这里还有共享存储、高速互联、多租户运维工具搅在一起。一台 BMC 失守，就可能摸到更多服务器、更多关键基础设施和客户的工作负载。

在 Neocloud 和 GPU 云环境里，这个问题更尖锐。就算你租的是独享裸金属服务器，那台机器往往还是接在服务商统一管理的带外网络上。BMC、装机系统、调度服务、凭据仓库、运维工具，这些很可能横跨多个客户的机器。服务商的管理平面成了所有租户信任的核心支点，一旦被突破，租户隔离就是一纸空文。

所以影响范围可以远超一台机器、一个客户。拿下服务器的 BMC 或者管理它的那套系统，就能碰到更多主机和共享资源，既炸了半径也抬高了修复成本。

## 那个 20 年老洞

这次研究的核心是 CVE-2013-4786，IPMI 2.0 协议里一个在 2004 年就埋下的问题。过程不复杂：在认证阶段，BMC 会用你的账号密码和当前会话参数计算一个 HMAC-SHA1 值，然后把它返回给请求方。

关键就在这里。任何一个没登录的攻击者，只要能在 UDP 623 端口上跟 BMC 说上话，就能请求拿到这串哈希，然后离线猜密码。跟在线暴力破解不一样，每试一个密码候选不用再跑去问 BMC，自己本地跑就行了。

这意味着什么？弱密码、重复使用的密码、出厂默认密码、甚至格式可预测的“唯一密码”，都可能被离线跑出来，而且不会在 BMC 上留下反复登录失败的可疑日志。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfAwFTCT9xNBBQj186aWY7Mmp7peliaRUic24tcRxicFmBfa9NF0QwOYtIYNeHxWGb2FbaYQeiaUNkVT8DJJQRYyeyqjxgr1vuoDNs/640?wx_fmt=png&from=appmsg)

▲ 简化版 IPMI 2.0 RAKP 交互过程。BMC 在客户端认证完成之前就会返回一个基于密码计算的 HMAC-SHA1 值。

## 扫一遍全网看看

我们一开始就问了一个简单问题：有多少 BMC 直接挂在公网上？

在 2026 年 5 月 6 日，我们用 UDP 623 端口扫了一遍，找到 36872 个暴露在公网的 IPMI 主机。接下来的两三个月里反复测了几次，每天平均还有大约 60 个之前没见过的 IP 新冒出来。

这个数字本身不新鲜，公网上的 IPMI 早就被人念叨很多年了。真正值得追问的是：这些服务里，到底有多少在认证之前就主动把安全漏洞送上门？

我们写了一个轻量级扫描器，逐一检查这些公网 IPMI 服务的已知问题和危险配置：

* 是否开启了 Cipher Suite 0，这个东西配置不当会严重削弱 IPMI 认证
* 是否接受空用户名或空密码
* 是否声明了 NONE 认证模式，等于直接跳过密码验证
* 是否对常见的厂商默认用户名返回了 RAKP 响应
* 以及最关键的，CVE-2013-4786，也就是登录前就能拿到密码哈希的问题

结果可以分成两类：一是认证交互前就暴露的危险配置，二是 IPMI 2.0 认证流程本身那个更底层的漏洞——直接泄露哈希让人离线猜密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdU86oY2XD6Im1cDevB98flPPNjYZfN4GKVM18t5cYQbkO0GgYIEdLAOtC3y2hKOgDXcADLAup4v8sgakeHKzsy1tNut4eaoN4/640?wx_fmt=png&from=appmsg)

▲ Shodan 上查询 IPMI port:623 的结果，可以看到大量 IPMI 服务直接暴露在公网 UDP 623 端口上。

## 把数据摊开来看

为了让大家直观感受到规模，我们做了一个交互式地图 BMCRadar24[1]，把这次研究里找到的公网 BMC 都标了上去。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibc3ouic6qCkskyk5Jh27DInd2AdXFzuD2ocYe65WNrL1A9eibrDhjep7BMiamrHy8kb7EO8hcn4zISEdYqldEHtyaGQicmuxiaibvHds/640?wx_fmt=png&from=appmsg)

▲ 这个地图可以让你直观地看到公网暴露的服务器管理接口在全球的分布情况。

测试完这堆端点后，数据很清楚：

36872 个公网暴露的 IPMI 主机里，有 24650 个（66.9%）在客户端认证完成前就返回了至少一次 RAKP 响应。6240 个（16.9%）接受空用户名加弱密码。2340 个（6.3%）用的具名账号（比如 ADMIN 或 root），其对应密码在常见字典里能直接找到。

简单说，约三分之二的暴露 BMC 在登录前就主动交出了密码相关的哈希。这里面有两个问题特别突出。

第一是空用户名。6240 台 BMC 对空用户名返回了认证材料，离线分析后发现匹配的密码弱得可怜。

第二是常见密码直接能用。2340 台 BMC 对 ADMIN 或 root 这类账号返回的认证材料，跟公开字典里的密码对上了。在返回 RAKP 响应的端点中，大约 9.5% 几分钟内就能跑出密码。

这里要说明：我们只做了离线分析，没有把跑出来的密码拿去登录，也没碰任何管理界面或改变系统状态。

不过弱密码只是问题的一半。另一半是：有些密码在标准字典里找不到，但它们遵循了可预测的出厂格式。

## Supermicro 的出厂密码格式

在我们数据集里，超过一半返回 RAKP 响应的 BMC 是 Supermicro 的机器。这个牌子在数据中心、托管环境和 GPU 基础设施里到处都是。

老旧的 ADMIN:ADMIN 默认凭据只命中了几百台。大多数 Supermicro 端点跟我们的初始字典对不上。这很正常。从 2019 年 11 月起，Supermicro 为了符合加州 SB-327 法案要求，把共享的 ADMIN 密码换成了每台唯一的预置密码。用户名还是 ADMIN，密码变成了印在机箱标签上的十个大写字母。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfKzldtuNmYMat1qEjPOaruZicDUxy9jHy5H9icSdjhtPvE3N8nTIicxgmlJAQOo26PB7ibUZRicPvA9bENr3nibNx3QZ9Ukg09OAhqE/640?wx_fmt=png&from=appmsg)

▲ Supermicro 关于为受影响产品引入唯一预置 BMC 密码的说明。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeQpsIibEgRNuFfkxx0b6gjv7c9eGwtM2uOErCmxdSdZsuCPl37rqN01OXicibEXPfqjPaw010Micuk6m41GoWpVj1eZ2DqhGoNoss/640?wx_fmt=png&from=appmsg)

▲ Supermicro 文档里写的密码格式：正好十个大写字母。

十个大写字母，26 的 10 次方，约 141 万亿种可能。直接跑字典跑不出来，但它的格式太受限了。对于一个有八块 GPU 的现代服务器跑 Hashcat 来说，穷举完整个候选空间大约只需要一小时。

遍历全部公网暴露的 BMC 这么搞成本太高，因为每一次抓到的 RAKP 响应里的会话值都不一样，每个都得单独算。但对一个有明确目标的黑客来说，挑几台系统下手，这个破解成本完全可以接受。

为了验证这个攻击路径是否真的走得通，我们拿一个美国裸金属 GPU 服务商的两台相邻 IP 做了测试。这个服务商的安全政策允许对其公网系统做测试，我们严格限制只分析 IPMI 认证流中泄露的密码材料。

两台机器都是 2023 年产的 X13DEM 主板，最新的 Supermicro 系统。两边跑出来的密码都严格符合十个大写字母的机箱标签格式。我们没有拿这些凭据去登录、去访问管理接口、或者更改任何系统状态。

当天我们就报告了这个问题，附上了受影响的 IP 和修复建议，然后停止了测试。服务商后来修掉了这个暴露。

## 拿我们自己的 HPE iLO 试试

Superrmicro 的测试说明了一件事：就算是每台唯一的出厂密码，只要格式被框死了，IPMI 在登录前又主动交哈希，那它就是离线破解的靶子。

我们想看看其他厂商是不是也有类似问题，就从实验室机架上搬出一台服务器，用它的 HPE iLO 出厂密码试了一遍。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibd7c0g0E7VeqIxIgLP91PYSO8klMTTiaqM9L4SciaOicqmW81DJwOlQ2ziaPTU1xz5NLKFRIJ4dv3cHyjEG9QOxKVia6foFx1xxEFcc/640?wx_fmt=png&from=appmsg)

▲ 我们实验室一台服务器上的 HPE iLO 出厂凭据标签。

HPE iLO 的出厂密码格式是：八个字符，大写字母加数字。36 的 8 次方，约 2.8 万亿种组合。听起来很多，但实际上比 Supermicro 那个 141 万亿的密钥空间小了大约 50 倍。

在一台苹果 M3 芯片的电脑上，穷举完整个空间大约要一天。在我们实验室那台装了八张 RTX 6000 PRO 的服务器上，每跑一个响应只需要约 32 秒。

## 公网 BMC 上的勒索留言

在研究过程中，我们撞到了一个暴露在公网的 HPE iLO 4 登录页面。它的安全公告栏里被人改了，挂着一条勒索留言。内容说服务器数据已被加密，索要 0.3 个比特币。

我们没法确认服务器本身是不是真被加密了，但这条被篡改的页面说明一件事：已经有人拿到了这台机器的管理接口权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdOgjXdrE7roafCP2V3FQLdKEYye8l0ttYMmh2CelNT6zKETeQyQjD0Jjyfd1JYzxve7me9GibVWDZJrIZRtbv9QTNL7Zk1l1Ug/640?wx_fmt=png&from=appmsg)

▲ 一台公网暴露的 iLO 4 登录页面，安全公告栏被人改成了 RSA-2048 勒索信息、0.3 BTC 要价和一个一次性邮箱地址。

这不是第一次发现攻击者盯上 iLO。早前就有研究记录过针对 iLO 的恶意活动，比如 iLOBleed，一个持久化的 iLO 4 Rootkit，跟针对服务器的破坏性攻击有关联。

我们撞到的这个页面把风险变成了肉眼可见的东西：一个暴露的 BMC 不只是一块被遗忘的管理页面。它是一条通往服务器底层的高权限密道，比操作系统还深。虽然我们没法确认这台机器的具体情况，但已知的攻击案例已经证明，这一层在真实对抗中被实实在在地利用过。

## 怎么修？

核心规则就一条：IPMI 绝对不该对公网开放。

具体动作包括：

* 在网络边界上直接封掉 UDP 623 端口
* 机器上架部署的时候把出厂密码换掉
* 关掉那些旧版和弱鸡选项：IPMI 1.5、Cipher Suite 0、匿名账号、NONE 认证模式
* 把 BMC 访问限制在独立的专用管理网络里，走 VPN、跳板机或者别的受控管理通道
* 上网络访问控制，只允许可信的运维机器连 BMC
* 把管理网监控从生产网监控里独立出来，分开看

在条件允许的环境里，用走 TLS 的 Redfish 替代 IPMI，放在隔离的管理网内。但无论如何，Redfish 和 IPMI 都不该直接曝在公网上。

## 漏洞通报

作为研究的一部分，我们把发现的问题报给了能确认身份的相关厂商和服务商。

2026 年 6 月，我们通知了 Supermicro：当 IPMI 对公网开放且能被远程拿到密码相关哈希时，受影响现代系统上的出厂 BMC 密码格式能够在可接受的时间内被恢复出来。

Supermicro 认可了在配备多 GPU 的现代破解能力下这个攻击场景是可行的。他们强调用户应该在初始设置时更换默认 BMC 密码，并建议始终把管理网络放在管理 VLAN 和 ACL 后面，不接公网。他们还说，会考虑为未来硬件版本改进默认密码策略，比如加长密码或扩大字符集。

我们也通知了其他能定位到具体归属的服务商，内容包括使用弱密码或 IPMI 配置有风险的系统。

## 结语

这个漏洞暴露的是数据中心管理平面一个普遍存在的安全缺口。BMC 管着最核心的基础设施，但得到的监控和保护往往远不如它们手底下管着的那些业务系统。

搭配上现代 GPU 的破解能力和可预测的出厂密码，这个漏洞能把一台暴露的 BMC 变成横跨管理网络的高权限据点，还很难被发现。

厂商和组织必须把管理层当成真正的安全边界来对待：隔离它、断掉公网暴露、轮换出厂凭据、持续监控。别等出了事再补。

这项研究是 Lava 在 AI 基础设施安全领域工作的一部分。FORGE 框架[2]对数据中心和 AI 基础设施面临的风险有更全面的梳理。如果你的机构运营数据中心或者 AI、GPU、裸金属基础设施，我们很愿意聊聊更广泛的基础设施管理和安全挑战[3]。

---

### 参考资料

[1] https://lavahq.io/bmc

[2] https://forge-framework.io

[3] https://lavahq.io/research?contact\_us=true

[4] https://lavahq.io/research/bmc-exposure-alert

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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