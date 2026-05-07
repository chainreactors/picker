---
title: 台湾23岁学生用SDR和手持电台瘫痪四列高铁：TETRA无线电漏洞让19年安全体系形同虚设
url: https://mp.weixin.qq.com/s/2FbP_KviNwol4rMc4Kil-g
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:30:36.055009
---

# 台湾23岁学生用SDR和手持电台瘫痪四列高铁：TETRA无线电漏洞让19年安全体系形同虚设

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Re7J21uQeAJws8cD1KSicFiaCkP1ptHhPJWCxvddpf16cSCtfXtcBMT9IZNSwc1rUBwczNZYyh2IPZcm0X8Kl4e5B16b2cv4IhgclMor7s0DI/0?wx_fmt=jpeg)

# 台湾23岁学生用SDR和手持电台瘫痪四列高铁：TETRA无线电漏洞让19年安全体系形同虚设

网空闲话plus

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

不进入驾驶室，不接触操作台就逼停多列高速列车，这听起来像是天方夜谭。然而，这种事情真的发生了。一名23岁台湾学生，利用简单的设备做到了。他现在可能面临最高十年的刑期。

以下文章来源于安全365
，作者H

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6icAqHPcru8JqFe5E50Lqxhia3zpBXczVx6rRHicqZtd6dg/0)

**安全365**
.

安全365 互联网安全门户网站,提供专业的互联网安全资讯、普及安全知识。居安思危、思而有备、备而无患！

> **导语**：一个23岁的台湾大学生，买了个SDR设备，攒了11部手持电台——就这么点装备，把台湾高铁的调度系统搅了个底朝天。四列高铁被迫紧急停车，累计延误48分钟。你以为这系统有多少层防护？七层。但问题是，参数19年没换过。这不是技术多么高超，这叫"漏洞送到嘴边"。

---

## 一、事件经过

根据台北时报的报道，2026年4月5日23:23，台湾高铁公司（THSRC）调度中心突然收到一部属于维修部门的手持电台发出的警报信号。这个"General Alarm"（GA，通用警报）是TETRA系统中优先级最高的警报类型，会自动触发区域内所有列车切换到手动紧急制动模式。

四列运营中的高铁列车瞬间停在了轨道上。

![SDR设备与高铁：TETRA无线电入侵示意图](https://mmbiz.qpic.cn/sz_mmbiz_png/Re7J21uQeALaUYP6qfVtbc16FnVVH0icxbeib7OMwC192rqcZJwgoNjRsWZSrVjdtibTYKTf88UuvEHM44EwRkutdH6kQjib7fPUxSwmMLO0VtA/640?wx_fmt=png "SDR设备与高铁：TETRA无线电入侵示意图")

调度中心试图回拨确认——电话那头的人回答得漏洞百出，随后直接关机。THSRC立即对手持电台进行全面清点，结果发现每一台配发的电台都好好地锁在仓库里，没人动过。结论只有一个：**有人克隆了参数。**

4月6日，THSRC向警方报案。

---

## 二、攻击手法：SDR + 手持电台 = 低端武器

警方还原了嫌疑人林某的攻击路径，说出来其实一点都不复杂：

**第一步：买设备。** 在网上买了一台SDR设备（软件定义无线电），接上天线和笔记本电脑。

**第二步：监听。** 打开软件，捕获THSRC的TETRA通信流量。

**第三步：解码。** 在软件里把相关参数解出来——TETRA的空口参数、加密配置，全部暴露。

**第四步：烧录。** 把这些参数写入自己的手持电台。一共11部，想用哪部用哪部。

**第五步：触发。** 找个信号覆盖范围内的位置，按下发射键——四列高铁应声停车。

此外，一名21岁的"朋友"据说还提供了一些关键的THSRC参数。

整个过程中，最难的一步是第一步——**买个SDR设备**。剩下的工作，开源工具全包了。

---

## 三、TETRA：一个被忽视的定时炸弹

### 什么是TETRA

TETRA（Terrestrial Trunked Radio，地面集群无线电）是一种专门给公共安全、铁路、机场、港口等关键基础设施设计的数字集群通信标准。它的设计目标是**可靠、优先、容灾**——所以它有最高优先级的警报机制，GA信号一旦发出，接收范围内的设备必须执行。

问题就在这里：**TETRA的早期加密方案有后门。**

2022年，安全研究机构就公开披露了TETRA的TEA1加密算法后门（CVE-2022-24402），该后门允许攻击者完全破译通信内容，甚至可以**注入伪造的控制指令**。一个SDR加一台普通笔记本电脑，用开源的Osmocom TETRA解码器，就能完成拦截和注入。

![TETRA Radio System](https://mmbiz.qpic.cn/mmbiz_png/Re7J21uQeAKCiaPwnibPbmmw5tnREhBQKDrliajzfx9yw6FQyqIAzAiclJmWPv2lic6NjNpOSW2cJWVKKy1pLia2WCYQmhO276abGsy3bPeMRn3hY/640?wx_fmt=png "TETRA Radio System")

### 19年没换的参数

THSRC这套无线电系统据称有七层验证机制，听起来固若金汤。但有七层不等于安全——如果这七层都是基于同一套从未轮换的密钥参数，那和一层有什么区别？

这就是关键基础设施最常见的毛病：**安全设计躺在纸面上，实际运行多年不更新、不轮换、不检测。**

---

## 四、追踪溯源：基站日志 + CCTV = 天网

你以为发完信号就没事了？太天真。

TETRA基站会记录每个上行信号的接入点，通过多点信号强度比对，可以把发射源锁定在某个区域——这叫**三角定位**。然后调出该区域内所有路口的CCTV，一个个排查。

林某被追踪到他的出租屋。4月28日执行搜查令，查获：11部手持电台、1台笔记本电脑、1台SDR设备。

目前他以10万元新台币交保候审，面临**十年以下有期徒刑**，适用台湾《铁路法》和《刑法》中危害公共交通安全相关条款。

他的辩护理由是："不小心按到开关，设备放口袋里误触的。"

你觉得呢？

---

## 五、类似案例：实验研究的代价

这类事情不是第一次发生。

**2016年，斯洛文尼亚。** 一个叫Dejan Ornig的大学生，用RTL-SDR和Osmocom TETRA解码器发现本国警察的TETRA终端根本没有启用身份认证——官方文档说是有认证的，实际没有。他把发现报告给相关部门，结果被起诉。历时七年诉讼，最终被判七个月缓刑。

**2026年初，美国。** 安全研究人员演示了用SDR复制货运列车"车尾装置"（EoT）的未授权制动指令，证明美国货运铁路系统同样存在RF攻击面。

这些案例的共同点是：**研究人员的发现没有被当作安全改进的机会，而是被当作犯罪来处理。**

---

## 六、关键基础设施的致命盲区

复盘整个事件，有几个点值得所有关键基础设施运营者警醒：

**1. 无线电参数必须定期轮换** TETRA系统的密钥、ID、频率参数必须按固定周期更换，不能一套用十九年。这不是可选项，是基本操作。

**2. 物理安全 + 逻辑安全缺一不可** THSRC的电台都在仓库里，但参数被人克隆了——说明问题不在终端，在系统层面。基站侧必须具备异常接入检测能力。

**3. SDR降低了攻击门槛** 十年前，搞清楚铁路系统的无线电参数需要昂贵的专用设备。今天，一台几百块的SDR加开源软件，足够。关键基础设施运营者必须认识到：**攻守门槛已经严重不对等。**

**4. 重视安全研究者的价值** 如果林某不是用于恶作剧，而是把发现提交给THSRC，换来的是什么呢？七年前斯洛文尼亚的案例告诉我们：可能是起诉、可能是牢饭。这套激励机制不改变，运营者将永远不知道自己的漏洞被谁发现了。![Translated news graphic from https://udn.com/news/story/7315/9475450](https://mmbiz.qpic.cn/mmbiz_png/Re7J21uQeAK3keEvW5LiavfzMhbL32iaJezxpCsf1FUsjYic9acp3SN1I6NarkfSfEhghtpsKvEjE3z1vFicngaCkEZic3N6xLmcNsq6eTMzoZwI/640?wx_fmt=png&from=appmsg)

---

## 七、相关链接

* 台北时报原文：https://www.taipeitimes.com/News/taiwan/archives/2026/05/05/2003856781[1]
* RTL-SDR原文：https://www.rtl-sdr.com/student-arrested-in-taiwan-for-using-sdr-and-handheld-radios-to-halt-four-high-speed-trains-with-tetra-hack/[2]
* TETRA加密后门（CVE-2022-24402）披露：https://www.rtl-sdr.com/encryption-on-the-tetra-protocol-has-been-broken/[3]
* Dejan Ornig案例：https://www.rtl-sdr.com/security-researcher-jailed-for-researching-tetra/[4]

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

### 引用链接

[1]*https://www.taipeitimes.com/News/taiwan/archives/2026/05/05/2003856781*

[2]*https://www.rtl-sdr.com/student-arrested-in-taiwan-for-using-sdr-and-handheld-radios-to-halt-four-high-speed-trains-with-tetra-hack/*

[3]*https://www.rtl-sdr.com/encryption-on-the-tetra-protocol-has-been-broken/*

[4]*https://www.rtl-sdr.com/security-researcher-jailed-for-researching-tetra/*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

网空闲话plus

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

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