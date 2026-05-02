---
title: 伊朗MuddyWater APT组织利用CastleRAT MaaS及区块链木马实施混合攻击的深度分析
url: https://mp.weixin.qq.com/s/KAyhIC0WDxZ2bV4bhzrlFA
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:55:45.116106
---

# 伊朗MuddyWater APT组织利用CastleRAT MaaS及区块链木马实施混合攻击的深度分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9bric97vH3E0DbG7P25noFIapv7xKTK1BNGO08SBG2O3Wu6N70c2xbrNFw4S7Ljmv3DuejSKJkvqOq1Nh63EkaGDydD5w21JMUVmAxHguibHs/0?wx_fmt=jpeg)

# 伊朗MuddyWater APT组织利用CastleRAT MaaS及区块链木马实施混合攻击的深度分析

Hackyc
Hackyc

疆来攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**概述**

网络安全研究人员近日确认，具有伊朗国家背景的APT组织MuddyWater正在利用俄语系网络犯罪团伙TAG-150运营的CastleRAT恶意软件即服务（MaaS）平台，开展高强度的网络间谍活动。此次攻击活动中，该组织不仅部署了基于以太坊区块链进行命令与控制（C2）的新型Node.js木马“ChainShell”，还结合了隐写术等高级规避手段。这标志着国家级黑客组织与地下商业犯罪工具的融合已进入实战化阶段。

#### **一、 事件背景：从自研工具到“军火采购”**

MuddyWater组织（隶属于伊朗情报与安全部）自2017年以来一直活跃，传统上依赖定制的PowerShell后门和合法的远程管理工具。然而，最新的攻击活动表明，该组织正转向采购成熟的商业MaaS平台（如CastleRAT），以快速获取高级入侵能力。

此次活动的直接线索源于一台暴露的MuddyWater C2服务器。研究人员在该服务器上发现了波斯语代码注释、针对以色列的IP地址列表，以及一个名为`reset.ps1`的PowerShell部署脚本，该脚本用于解密并释放ChainShell组件。此外，攻击者还利用隐写术将名为“Build  120”和“Build  13”的恶意载荷隐藏在JPEG图片中。值得注意的是，这些载荷均在今年2月28日美以联合打击伊朗之前编译完成，显示出明显的“预先部署”特征。

#### **二、 归因分析：构建“人-码-平台”闭环证据链**

研究人员通过多维度的数字取证，构建了严密的归因证据链：

1. **证书指纹关联**：攻击者使用了SSL.com签发的代码签名证书（注册名为“Amy Cherne”和“Donald Gay”）。其中，“Amy Cherne”证书不仅签署了已知归属于MuddyWater的StageComp木马，还签署了一个名为DinDoor的MSI安装包。
2. **基础设施重叠**：对DinDoor MSI的分析显示，其向多租户C2平台`serialmonet.com`发送包含JWT令牌的请求，令牌中硬编码了活动ID“Smokest”及用户ID。完全相同的活动标识被发现硬编码在CastleRAT的持久化计划任务名称（`VirtualSmokestGuy`）中。
3. **操作者与平台绑定**：暴露的服务器操作日志显示，攻击者曾手动测试Build 13的C2端口。该服务器上的`reset.ps1`脚本哈希值与公开恶意软件库样本完全一致，直接将伊朗操作员、TAG-150平台组件和CastleRAT C2绑定在一起。
4. **客户身份确认**：尽管`serialmonet.com`平台也被LeakNet勒索软件团伙使用，但通过分析Deno代码库和JWT凭证，确认MuddyWater是该平台的**客户**而非开发者。代码中的俄语字符串及针对独联体国家的规避逻辑，进一步印证了该平台源自俄罗斯背景。

#### **三、 技术分析：能力跃升与多维度规避**

此次攻击在技术层面展现了显著的能力升级：

* **ChainShell区块链木马**：这是一款基于Node.js的“thin shell”执行器。它摒弃了传统的HTTP直连，转而通过**以太坊智能合约**解析C2地址，通信过程采用AES-256-CBC加密。其核心机制是利用`new Function()`动态执行服务器端推送的JavaScript代码。
* **CastleRAT MaaS平台**：该平台提供了强大的隐藏虚拟网络计算（HVNC）功能，允许攻击者在受害者无感知的情况下，通过隐藏桌面静默访问内部系统、云控制台和Web邮箱，并能复用受害者的会话Cookie绕过MFA认证。此外，它还集成了针对Chrome  v127+应用绑定加密的Cookie窃取模块。
* **持续对抗与规避**：尽管自3月起多家厂商曝光了相关基础设施，攻击者仍保持高频更新（如3月11日、13日编译新安装器，3月16日更新JS样本）。攻击链涵盖了滥用CMSTPLUA绕过UAC、DLL侧加载、WMI添加杀软排除项以及隐写术等多种反检测手段。

#### **四、 事件影响与防御建议**

此次事件对现有的威胁情报与防御体系提出了严峻挑战：

1. **归因迷雾**：当网络中检测到带有俄语字符串、基于主流犯罪平台构建的恶意软件时，防御者极易将其误判为普通的俄罗斯网络犯罪活动，从而忽略了背后伊朗国家级间谍活动的真实意图。
2. **工作流失效风险**：严格区分“网络犯罪”与“APT”的传统情报工作流，很可能在此类混合型攻击面前失效。
3. **防御侧重点**：建议防御方不再单纯依赖静态IoC（失陷指标），而应关注**行为链条**。重点监测包括：异常的Outlook Web访问、CMSTP父进程调用、与区块链节点的非业务通信，以及JWT凭证的异常关联。同时，应加强对证书透明度日志的监控，力求在攻击者实现横向移动前切断入侵链。

此次事件不仅是伊朗在网络行动中追求“作战敏捷性”而非“武器自研”的战略缩影，也为观察独特的地缘政治合作提供了网络侧面的实证。

---

**图 1 MuddyWater组织攻击示意图**

*![伊朗APT组织MuddyWater升级其攻击战术策略，利用第三方MaaS平台展开攻击活动](https://mmbiz.qpic.cn/mmbiz_jpg/9bric97vH3E1FeF0AVJWDdZNZdvdFzyx87I9N7WiaBKULMqkicf9mQPtctJ8q0ukCzmJeKJibrlASmKcricDRmnHhNGT7OiaTlKAGWiaqqWF8ibpScY/640?wx_fmt=jpeg "伊朗APT组织MuddyWater升级其攻击战术策略，利用第三方MaaS平台展开攻击活动")*

**图 2 攻击活动时间节点**

![伊朗APT组织MuddyWater升级其攻击战术策略，利用第三方MaaS平台展开攻击活动](https://mmbiz.qpic.cn/mmbiz_png/9bric97vH3E1ia4ENFiaZ8BialfPpTQx4nZ9jJhcicNyTCH9iblIYY30kicKqznmXpe23IC3TKIUbl8Tc5siceicsISZOXcHosyuSL0vIYAJUVRZJ37o/640?wx_fmt=png&from=appmsg "伊朗APT组织MuddyWater升级其攻击战术策略，利用第三方MaaS平台展开攻击活动")

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/tOs8TbI2yPvic8UicV7NibHf4f20YtJW6U7X7opeH8eichog64tXbBP6ibz5ia8hXribWr2VibKFPbT8l3uAGuJliaEHL8Q/0?wx_fmt=png)

疆来攻防

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/tOs8TbI2yPvic8UicV7NibHf4f20YtJW6U7X7opeH8eichog64tXbBP6ibz5ia8hXribWr2VibKFPbT8l3uAGuJliaEHL8Q/0?wx_fmt=png)

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