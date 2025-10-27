---
title: 论文分享 Measuring the Practical Effect of DNS Root Server Instances
url: https://mp.weixin.qq.com/s?__biz=MzA4ODYzMjU0NQ==&mid=2652311631&idx=1&sn=fbdc3c3c699ef39b7f5d4331994ad1ce&chksm=8bc48dc1bcb304d77bdf93274e00330c1a59916a455ef00d95873eae6e6d45bb18eacaa9d633&scene=58&subscene=0#rd
source: 网安国际
date: 2022-10-14
fetch_date: 2025-10-03T19:50:47.320485
---

# 论文分享 Measuring the Practical Effect of DNS Root Server Instances

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icelxY6ibIXSXeUicnToz7pY4rp8jxhdEhTwaiajXTQVNHWLD0FuhpQ30kJgaWsjvalOo4QGgflPMMLbzgVPKyo8AQ/0?wx_fmt=jpeg)

# 论文分享 Measuring the Practical Effect of DNS Root Server Instances

网安国际

以下文章来源于NISL实验室
，作者张丰露，刘保君

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM766Bv1SQgibFlalH9bqtncibzFunlpyJGeVJiaKNlDOeyfQ/0)

**NISL实验室**
.

网络与信息安全实验室(NISL@THU)，专注于网络、系统、应用、人工智能安全教学与研究，在国际四大安全会议发表三十余篇论文，成果在业界产生了广泛影响力。孕育了蓝莲花、紫荆花等知名战队，发起了网安国际学术论坛InForSec。

今天分享的论文主题为：域名根服务器节点实际效用测量研究。论文作者来自于清华大学网络研究院。

近年来，我国政府机构加快引进部署域名系统根服务器节点。为量化评估我国互联网用户域名解析环节对境外根服务器节点的不合理依赖，论文提出了一种区分根服务器域名查询请求是否出境的方法。研究结果表明，我国境内部分根服务器节点实际作用范围有限，部分根域名查询请求仍然大量出境。针对上述发现，作者提出了针对性的改进建议。研究论文发表于网络测量领域重要会议 PAM 2022。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych9qyvaLBtiaUiaMTtITFu5uxROkBicMHAWfUKJClDaHGJqTq1MBA4iabnWq7TdwHkBKQ4PdFF7iawVmOLw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

全文约2200字，阅读时间约6分钟。

**01**

**【研究背景】**

域名系统是互联网关键基础设施之一。作为互联网的中枢神经，域名系统在网络安全体系中起着至关重要的作用。域名根服务器系统（DNS Root Server System），作为域名空间层次化结构的顶点、以及几乎所有域名解析查询请求的起点，对于互联网的安全稳定尤为关键。

由于早期域名协议报文的长度限制，根服务器标识符的数量为 13 个（使用英文字母 A 至 M 表示），其运营管理由 12 家相互独立的组织机构负责。2002 年后，为优化域名解析效率，根服务器运营机构采用任播技术在全球范围广泛地部署根服务器节点（Root Server Instance）（有时也被译为根服务器镜像）。**然而，长期以来，位于欧美国家的根服务器节点数量远远高于亚洲国家 [1]。**

近年来，关于域名根服务器可靠性的质疑之声不绝于耳。为使互联网用户域名查询解析摆脱对境外根服务器节点的不合理依赖，我国政府部门积极部署根服务器节点的引进工作。截至2020年12月，中国境内已陆续引入了 5 个根服务器（F、I、J、K、L）的 16 个镜像节点。

然而，上述我国内地引进部署的根服务器节点，究竟能在何种程度缓解国内互联网服务对境外域名根服务器系统的依赖，以及又该如何针对性地制定后续根服务器节点的引进策略，已成为安全社群密切关注的话题。

**02**

**【研究方法】**

为了判断互联网用户域名解析过程是否依赖于境外的根服务器节点，一种直观的实验方法是：在国内主流运营商中选取地理位置分布均匀的实验观测点，并主动向域名根服务器（A 至 M）发起查询请求。依据域名解析交互时对端通信实体的地理位置属性（境内/境外），判断当前互联网用户是否需要依赖于境外的根服务器节点。

然而，由于当前根服务器运营管理机构普遍采用任播技术（Anycast），利用IP地址完全相同的主机在全球范围内广泛部署服务节点 [2]，上述实验将面临一个主要挑战：**如何区分根服务器节点的地理位置属性。**

为解决上述问题，在实验设计过程中，研究人员巧妙地利用我国国际网关所引入的侧信道信息（Side Channel）[3]。具体而言，研究人员选择实验观测点，模拟境内用户向13个根域名服务器（A至M）发起包含特定域名的查询请求，并分析域名应答响应报文中的资源记录。若资源记录源自于国际网关设备，则推测其出境；反之，则推测该查询请求未出境。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych9qyvaLBtiaUiaMTtITFu5uxRhj9c3UJnDp0uk8oLUyr9mf39yT4kRnChxiasdbamUsaAUXPmXoAvTicg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图表一：利用国际网关侧信道信息区分根域名查询请求是否出境

**03**

**【主要发现】**

研究人员收集了来自国内主流运营商的百余个测量观测节点，分别对13个根服务器域名发起多轮次查询，并基于上述研究方法进一步判断查询请求是否出境。

下表展示了对于不同根服务器域名，查询请求流量在境内解析的比例。主要结论包括：

1. 中国教育和科研计算机网（CERNET）内包含一例自建根服务器节点，致使所有根服务器域名查询请求流量均可在境内被解析。

2. 部分根服务器节点的实际作用范围可能受限。譬如，中国电信的观测点向F根发起的查询请求，有99.34%在内地被解析；然而中国联通和中国移动的观测点向F根发起的查询请求，仅有3.24%和1.53%可被内地节点解析。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych9qyvaLBtiaUiaMTtITFu5uxRQKd9XrhZTlKLtsJYj9Ho9u5KfZ2QtLfvrAZywYZR1YhEB6ojm7Dsiag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图表二：根服务器域名查询请求于境内解析的比例

（白色背景表示境内存在相应的根服务器节点）

研究人员还分析了各实验观测点的结果，进一步证实了我国境内引进部署的部分根服务器节点可能仅向特定网络用户提供服务。例如：

1. 内地F根服务器节点对所有位于电信的观测点提供服务，但不对位于联通、移动的观测点提供服务。

2. 内地J根服务器节点对所有位于联通的观测点提供服务，但不对位于电信、移动的观测点提供服务。

3. 内地K根服务器节点对所有位于电信、联通的观测点提供服务，但不对位于移动的观测点提供服务。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDychibKcIBcIQgf4s6TkBMcKweKgnDmcrMoPSomEJlvcPO2mDA7bawSr4M0knbdCYIrweJW3L75v5K1WA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图表三：每个观测节点发起的根域名查询流量于内地解析的比例 （颜色越深，代表比例越高）

随后，研究人员同大型运营商及DNS根服务器的运营者进行了深入交流。最终确认了上述现象的背后原因：

1. 内地根节点通常部署于运营商网络内部，而不是位于网络交换节点；

2. 运营商网络之间的BGP路由策略受到限制。

因此，尽管内地已经引进部署了大量根节点，部分互联网用户的根域名查询请求流量仍会出境，请求可能会被路由至更远的海外根节点进行解析。

**04**

**【结论】**

这项工作围绕中国境内域名根服务器节点的实际效用问题开展了测量研究，提出了一种分辨根域名查询请求是否出境的方法，发现了由于根服务器节点部署策略以及运营商BGP网络路由策略的限制，互联网用户发起的部分根域名查询请求流量仍然将出境解析。

基于上述研究方法，研究团队开发了“域名系统根服务器节点运行监测系统”，有助于网络运营商及时发现根服务器节点的运行异常。系统效果图如下。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych9qyvaLBtiaUiaMTtITFu5uxRPQ2XtWv9Mb12uJhUiaCkMiaexicZt4e3LOv5SMS6u66O6AkGWwGnonhMA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图表四：域名系统根服务器节点运行监测系统展示界面

原文链接：

https://doi.org/10.1007/978-3-030-98785-5\_11

参考文献：

[1] Root Server Technical Operations Association. https://root-servers.org/

[2] Hardie, T.: Distributing authoritative name servers via shared unicast addresses. RFC 3258, April 2002. https://doi.org/10.17487/RFC3258, https://rfc-editor.org/rfc/rfc3258.txt

[3] Lowe, G., Winters, P., Marcus, M.L.: The great DNS wall of China. MS New York Univ. 21, 1 (2007)

编辑&审校 | 张一铭、刘保君

![](https://mmbiz.qpic.cn/mmbiz_jpg/icelxY6ibIXSVuicsK4D2icVJTX0AVHaibtHNLgwu7j0nojdkAFx3CAvGsCyKXZ7JJ2eaI18Zzia1A8Hw7ibdTPKJAweQ/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVlNf68NLWmpfibn7F9KsZzNAIDY1JCxHTWxVibDXwxJ6Pb5voAqiaweFCkQUPb6SJ51jPQ3iaAk8dGJw/0?wx_fmt=png)

网安国际

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icelxY6ibIXSVlNf68NLWmpfibn7F9KsZzNAIDY1JCxHTWxVibDXwxJ6Pb5voAqiaweFCkQUPb6SJ51jPQ3iaAk8dGJw/0?wx_fmt=png)

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