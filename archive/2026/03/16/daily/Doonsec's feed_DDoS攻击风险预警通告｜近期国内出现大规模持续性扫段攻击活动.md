---
title: DDoS攻击风险预警通告｜近期国内出现大规模持续性扫段攻击活动
url: https://mp.weixin.qq.com/s/xrvU9a4L0BfHwXhVpBE6qw
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:12:50.923092
---

# DDoS攻击风险预警通告｜近期国内出现大规模持续性扫段攻击活动

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/RiaMmbYzV5MiaSStibVQhLpXJXqpC4VF0maoNeua7wHl62F1cFicRdAqk45ny3ucvErxBDvgDq51b5oZqibJZh5iaNGcvz3pXsSU91flWSfn0cyMQ/0?wx_fmt=jpeg)

# DDoS攻击风险预警通告｜近期国内出现大规模持续性扫段攻击活动

抗D产品线
抗D产品线

电信云堤

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Dh3fqSPAOWekCSIf3ffuFuiaBPl4BSArBsDhFEMSOTbeIfb7mdz4D0mDExZesv4PPicUdsOTxfRUx8QntAMTmTBA/640?wx_fmt=gif&#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Dh3fqSPAOWePMu18J3qdm7D4DgerZrtmzfZ2ThoQZZl4WAHJScyL4c59NPZcjXgnP2YL4HnUicxRibjtBZmqJW8A/640?wx_fmt=png&#imgIndex=1)

近期，中国电信天翼安全监测发现一起具有组织化特征的DDoS攻击，攻击模式呈现出高频化、短时化、多轮次化，已对部分客户业务稳定性造成一定影响。现发布本次安全风险预警，旨在帮助各行业客户提前做好防护准备，有效应对潜在风险。

**⚠****攻击特点速览**

本轮攻击疑似由Fastcat黑客攻击组织发起，以TCP反射扫段为主要攻击手法，主要特点如下：

* 单次攻击峰值多低于50Gbps，攻击频次极高，形成持续性骚扰

* 攻击流量以TCP 80端口应答包为主，源IP多为国内地址，极具欺骗性

* 快速轮询目标IP段，单次仅持续数十秒至数分钟，极易绕过传统阈值检测

* 引发客户网络链路抖动、访问延迟升高、短时业务不稳定等风险

**一、攻击态势概述**

根据近期网络监测数据分析显示，国内互联网环境中出现针对大量IP地址段的轮询式DDoS攻击行为。攻击虽整体峰值不高，但频次较高，呈现持续性骚扰特征，已导致部分对业务实时性要求较高的客户网络出现明显抖动。

结合近期攻击特征与历史威胁情报，初步研判此类攻击的幕后组织高度疑似为FastCat黑产组织。该组织长期从事DDoS攻击资源租赁及攻击服务活动，曾多次在全球范围内发起大规模网络攻击事件。结合当前攻击模式和行为特征分析，本轮攻击可能存在一定商业化攻击动机。

***二、攻击技术特征***

**攻击流量构成**

以TCP协议80端口应答数据包为主，大量来自国内IP地址的 TCP响应流量集中指向目标网段，由于反射流量来源于大量真实网站服务器，在网络层呈现正常HTTP响应特征，具有较强的隐蔽性。

**扫段手法**

攻击者首先伪造目标IP地址作为源IP，向互联网上大量Web服务器的TCP 80端口发起HTTP请求。由于Web服务器会对请求进行正常应答，大量HTTP响应数据包会被发送至被伪造的源IP地址，从而形成反射攻击流量。为了扩大攻击影响范围，攻击者会不断改变伪造的源IP地址，对目标网段中的IP进行依次快速轮询伪造请求。因此，大量正常网站服务器的HTTP响应流量会持续被反射至目标网段的不同IP地址，从整体上形成扫段攻击效果。

**流量规模**

单次攻击峰值通常低于50Gbps，因分散到大量目标IP，攻击检测易造成漏检或短时大量异常告警。

**影响范围**

覆盖金融、互联网、云计算、游戏、政企等多个行业，对实时交易、在线业务、延迟敏感系统造成明显干扰。

**三、攻击风险分析**

**单次攻击时间短但频率高**

单次攻击持续时间通常为数十秒至数分钟，但攻击轮次密集，容易造成持续性业务干扰，频繁触发防护设备清洗策略，影响正常用户访问。

**TCP 80端口响应流量为主**

攻击流量主要表现为HTTP服务的响应数据包，攻击检测识别难度提升。

**单IP流量不高但整体影响明显**

单个IP地址承受的攻击流量较小，但整个网段聚合流量持续高压。

**反射源分布广泛**

攻击流量来自大量正常网站服务器，源地址高度分散，攻击者通过不断变化伪造的源IP，造成对目标地址段的轮询攻击。

***四、重点行业风险提⽰***

**金融行业：**交易系统对网络抖动极度敏感，可能引发交易失败或延迟。

**互联网平台企业：**用户访问体验下降，导致业务流失。

云计算及IDC服务提供商：多租户环境下，一处受攻击可能波及邻居。

**游戏及在线应用平台：**实时性要求高，攻击易造成卡顿、掉线。

**政企信息化系统：**对外服务抖动可能影响公众服务和形象。

上述行业普遍对网络稳定性和业务连续性要求较高，在面对高频扫段攻击时更容易受到影响，建议加强重点防护。

**五、防护建议**

**1**

**加强网络流量监测能力**

持续监测网络出口流量，重点关注：

• TCP 80端口响应流量异常增长

• 来自大量不同源地址的TCP响应流量集中访问同一目标网段

• 地址段范围内多个IP访问流量短时反复异常升高

**2**

**建立本地风险识别与处置能力**

建立检测与处置机制：

• 边界防火墙启用TCP状态验证，丢弃所有未关联会话的应答包

• 异常流量聚合分析，快速识别攻击

• 限制系统半开连接总数，保证应用可用

**3**

**部署专业DDoS防护服务**

对业务连续性要求高的客户，建议启用专业抗DDoS防护，与本地部署防护能力形成立体组合防护能力：

• 网络侧流量清洗，实时过滤恶意报文

• 自动化识别攻击与防护，无需人工干预

• 高并发攻击流量处理能力，应对高频脉冲

***六、持续监测与服务支持***

当前该类扫段攻击活动仍处于活跃状态，且持续演进。我们将持续跟踪分析相关攻击行为，并根据态势变化及时发布新的安全预警。云堤·抗D基于中国电信云网资源优势，采用BGP Anycast、SRv6、FlowSpec等路由技术，结合见微安全大模型辅助智能研判分析，通过骨干、城域、端侧防护能力实现高、中、低全方位DDoS攻击的监测与防护，打造针对DDoS攻击的近源与近目的相结合、云网端多级联动的分布式“导弹防御体系”，对DDoS攻击精准识别、全面防护。

![image.png](https://mmecoa.qpic.cn/mmecoa_png/RiaMmbYzV5MgBk1yaibSAddOaJFViaa9eahDjDicj3JufaIo7Lp7GWWCPB6c94tiaAJtnZicBZzA4lib18CQMibfbxiaC9icUqQ41T1HJPdvkLFJEibJU8/640?wx_fmt=png&from=appmsg)

云堤DDoS防护产品架构

展⽰⾻干网、城域网、IDC多级联动防护体系

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/RiaMmbYzV5MjYZtrTA8AsYLjA1nj3uicibVMxQKf9hjODKZiaRtpGLwB57AdLUXTOPt7rrkAqwzXeLpv8HdbVZ6fXicAia7Jsxs7oCbNEQdoKNJRg/640?wx_fmt=gif&from=appmsg)

如需紧急协助，请联系

4009259120

7×24小时应急响应团队

随时为您提供安全防护服务

供稿：抗D产品线

排版：武云龙

编辑：陈师慧

校对：李雪

执行主编：田金英

主编：冯晓冬

**推荐阅读**

[![](https://mmecoa.qpic.cn/mmecoa_png/K3Wt1qVwribzkmB1qufciacviaMv3Mkzf7xXUQAarrb5nibEuJauvGxD5fIBWkYXZDRXR72kW2fFIBibjDjnCiaT8ryQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk2NDIzNTYwOA==&mid=2247490425&idx=1&sn=6d77d3c587bc3b2154ef40ce2600c45f&scene=21#wechat_redirect)

[境外DDoS洪流来袭 我国多地多行业遭冲击](https://mp.weixin.qq.com/s?__biz=Mzk2NDIzNTYwOA==&mid=2247490425&idx=1&sn=6d77d3c587bc3b2154ef40ce2600c45f&scene=21#wechat_redirect)

[![](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5Mj3t0ociavgUfqVXp4IZUTCbfqI69gRmiaBMwWaPaDXbic6qy5s84WOoD0gkoLveG1815636vE0k3nxibibFQibPQbyuzyVOibxibdMice0/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk2NDIzNTYwOA==&mid=2247490318&idx=1&sn=7e7a09f44e109f5b2a7ca0346fe21400&scene=21#wechat_redirect)

**[“22.2Tbps洪峰”突袭基础设施——超大规模DDoS攻击已具备“战术级”打击特征](https://mp.weixin.qq.com/s?__biz=Mzk2NDIzNTYwOA==&mid=2247490318&idx=1&sn=7e7a09f44e109f5b2a7ca0346fe21400&scene=21#wechat_redirect)**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/z7xPqlc0GbBZdrnibkon0HxogO9iazwQy5cqsw6fRdkPujrZZCuVnk7ywgyYA7yTfRIIkEXpdpDfQlkFMENO9P0Q/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/K3Wt1qVwribxuTYm5vRkaKsUs4HJHScD5DBp39NrL0IdrjN1ZlZajrPZYzCYYw5ksSHz9iaOpOOC7q5bS5s9V54g/0?wx_fmt=png)

电信云堤

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/K3Wt1qVwribxuTYm5vRkaKsUs4HJHScD5DBp39NrL0IdrjN1ZlZajrPZYzCYYw5ksSHz9iaOpOOC7q5bS5s9V54g/0?wx_fmt=png)

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