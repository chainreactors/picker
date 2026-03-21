---
title: 间谍活动闯入现实：当基础设施成为情报收集通道
url: https://mp.weixin.qq.com/s/ie8yo1eoqf_x70wiVGwb5A
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:01:30.218326
---

# 间谍活动闯入现实：当基础设施成为情报收集通道

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0OV0B0HWnfwNIXGMggGiaKm0aFoZup2QvBrPo6XlNcbjhz4mnxicRZKMGP4rPRr3SxtvNW5C7HJntmmqFKDic8GhDibK8I5xWqaLw/0?wx_fmt=jpeg)

# 间谍活动闯入现实：当基础设施成为情报收集通道

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1XZxEEGudxsiaYZzlXGD4ddIy6IomIEuuDvjWkMahRHlm4fW23ITMmo8enk2ouPFOOYia3b63k8RkVAOWaxpaBmEeicBiajWSpFGc/640?wx_fmt=png&from=appmsg)

##

**Part01**

## ****共享服务带来的安全困境****

现代企业依赖的共享服务、统一身份认证层和互联服务提供商，正成为犯罪团伙和国家背景黑客组织的渗透路径。这种依赖关系的重叠已成为CISO（首席信息安全官）必须应对的核心安全特征。

威胁行为体始终在寻找攻击优势。近期，研究人员发现两种旨在长期获取情报的攻击活动，其攻击路径直指企业内部关键节点。企业已处于攻击者的情报收集路径上——它们不必是直接目标，但由于使用与攻击者已控制的相同基础设施，自然成为攻击版图的一部分。CISO的挑战在于确保企业不会仅因网络连接方式就成为他人的情报通道。

**Part02**

## ****攻击路径的聚合效应****

两起独立攻击活动正通过相同的运营依赖项产生交集。这种重叠并非协同攻击，而是现代基础设施集中化访问的必然副产品。当所有流量都经由少数共享服务、统一身份层和互联供应商时，攻击者无需协调即可通过相同入口入侵。

典型攻击面包括：

* 电信路由系统
* 云服务相邻资源
* 托管服务通道
* 身份联邦体系

这些企业赖以运转的"连接组织"，同样被攻击者用于监控认证、窃取数据及维持长期访问——全程无需直接接触目标企业。当不同任务的黑客通过相同依赖项入侵时，暴露出的是结构性安全缺陷。由于这些依赖项具有共享性和不可避免性，问题不在于单个攻击活动，而在于允许攻击者在企业上游长期潜伏的基础架构设计。

**Part03**

## ****商业间谍软件的通道化威胁****

使用Predator间谍软件（受制裁的Intellexa联盟产品）的犯罪组织已在十余个国家活动，美国制裁未能阻止其蔓延。其攻击目标高度精准：记者、活动人士、政界人士、人权捍卫者、政府雇员及承包商等高价值人群。这些目标持有的信息价值远超其设备本身。

Predator的攻击手法呈现专业化演进：

* 单点击链接攻击
* 零点击漏洞利用链
* 网络流量劫持
* 持久性设备控制

作为政府级商业间谍平台，Predator这类设备级入侵会演变为企业级风险。一旦部署，即可在上游截获企业数据流、认证系统和服务商网络，形成持续性监控能力。其危害不仅在于入侵个体设备，更会危及受害者登录的系统、经过的网络及服务提供商——这些正是企业依赖的共享基础设施。

**Part04**

## ****国家背景的电信网络渗透****

2026年2月，新加坡披露高级网络间谍组织UNC3886入侵了该国四大电信运营商（Singtel、StarHub、M1和Simba）。攻击者使用0Day漏洞、Rootkit和高级持久化技术，长期控制骨干基础设施及网络数据。

这意味着：当电信网络成为实时信号情报收集点，攻击者无需直接入侵目标环境，即可从其依赖的通信链路获取信息。尽管新加坡未指明幕后支持者，但行业分析普遍将UNC3886与中国关联。关键不在于归因，而在于这种访问具有上游性、持久性和结构性嵌入特征。

**Part05**

## ****CISO的应对策略****

当前威胁已超出理论范畴，需立即采取可量化措施：

**1. 依赖项风险评估**

* 从共享依赖项视角重新评估风险，内部资产仅是攻击面的一部分
* 将电信、云服务、MSP/MSSP和身份认证通道纳入可见性管理
* 视上下游合作伙伴为威胁面的活跃组成部分

**2. 供应链安全强化**

* 要求电信和云服务商提供安全合规证明
* 降低对非可控基础设施的默认信任级别
* 采用"已失陷"假设设计认证流程

**3. 检测体系升级**

* 转向检测低噪声、长期驻留的情报收集特征
* 将情报驱动的风险评估纳入常规治理架构
* 会话层加固：预设令牌窃取和身份冒充场景

**4. 保险策略调整**

* 新加坡电信事件成为转折点，网络保险将明确涵盖骨干网APT驻留风险
* 保费显著上涨，未审核供应商可能导致续保被拒

**Part06**

## ****战略现实****

商业犯罪组织与国家背景黑客正利用相同的现代基础设施依赖关系展开活动，这种重叠已成为运营环境的决定性特征。对CISO而言，核心问题不再是"是否会遭直接攻击"，而是"所依赖的基础设施是否已成为他人的情报平台"——且可能浑然不觉。

**参考来源：**

The espionage reality: Your infrastructure is already in the collection path

https://www.csoonline.com/article/4143390/the-espionage-reality-your-infrastructure-is-already-in-the-collection-path.html

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3hCYIDd7a8icmhzic2aMTw0bics6BfDdhRCQCsKTwXSAB6wXtEwI4OK9jdlFfFFNQJa4JUiapxxu56BjXl4gx3LEXYU1GMRkpiawgA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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