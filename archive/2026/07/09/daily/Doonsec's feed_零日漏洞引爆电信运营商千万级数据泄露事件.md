---
title: 零日漏洞引爆电信运营商千万级数据泄露事件
url: https://mp.weixin.qq.com/s/7qFQN--jUsZzd8vQswXS0g
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:54:33.091152
---

# 零日漏洞引爆电信运营商千万级数据泄露事件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hfjKPyxBDjqTZL1ku62ZYypVoSFyc5130mvHcCicUEDhcibECH0MgU3LIfWDwX6ekcN9lmpiaicENFvzVorwfd91eyYiajTrxMfbfnsT2PXicibBiaY/0?wx_fmt=jpeg)

# 零日漏洞引爆电信运营商千万级数据泄露事件

原创

何威风
何威风

河南等级保护测评

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**KDDI确认超1223万邮箱地址泄露，第三方软件零日漏洞引发日本近年最大邮件系统安全事件**

日本第二大电信运营商KDDI近日公布针对ISP邮件系统遭受网络攻击事件的最终调查结果。经过进一步取证分析，此次事件共确认造成**12,233,087个电子邮件地址**以及**7,616,173个邮件账户密码**遭到泄露，成为近年来日本通信行业影响范围最大的邮件系统数据泄露事件之一。

与此前公布的"最高可能影响1422万账户"相比，此次公布的数据意味着KDDI已经完成事件取证，确认了实际泄露范围。目前公司表示尚未发现因本次事件导致的二次攻击或进一步数据滥用情况，但仍要求所有受影响用户尽快完成密码修改。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hfjKPyxBDjqpIwWzJ3mvA9xl4smOmia3d1RCGiaxPHy71nOyoeNrk2Su94gdWlt07OjBGRZlvD7Yv4TssOIUVRgs8U6ibzVLd0vLsfTbPe6ROU/640?wx_fmt=png&from=appmsg)

此次事件影响的并非KDDI移动通信网络，而是KDDI为多家互联网服务提供商（ISP）建设和运营的一套统一邮件平台。受影响的包括BIGLOBE、@nifty、J:COM、Commufa、STNet等多家ISP邮件服务，而**au Mail、UQ mobile Mail以及au one net Mail由于运行于独立基础设施，并未受到此次攻击影响。**

## 攻击过程：零日漏洞导致攻击者长期潜伏

KDDI调查显示，本次攻击利用的是部署于邮件系统中的**第三方软件未知漏洞（Zero-day）**。攻击活动最早可追溯至**2026年5月16日**，攻击者利用尚未公开、软件供应商当时亦未知的漏洞进入邮件平台，并持续实施未授权访问。直到**6月17日**，KDDI监测到异常行为后才确认遭遇网络攻击，并立即完成系统修复、封堵漏洞及技术防护措施部署。调查还发现，在KDDI发现漏洞时，软件供应商尚未意识到该漏洞存在，目前已启动向相关公共机构报送漏洞信息并推进公开披露工作。

这一过程体现出典型的供应链攻击特征：攻击者并非直接攻破运营商自身业务系统，而是通过第三方组件中的未知漏洞，进入由运营商统一提供的邮件基础设施，最终波及多个ISP客户。

## 泄露数据已由"可能泄露"升级为"确认泄露"

经过近三周的取证分析，KDDI确认此次事件造成以下数据泄露：

* **电子邮件地址：12,233,087个；**
* **邮件系统密码：7,616,173个**

  （属于上述邮箱地址的子集）。

泄露密码均为邮件系统账户密码，并不意味着运营商会员账号或其他业务认证信息一定泄露，但如果用户存在密码复用行为，则攻击者可能利用泄露凭据对其他互联网服务发起撞库攻击，因此风险仍然较高。

## 应急响应：快速修复、强制改密、EDR全面部署

事件发现当天，KDDI即完成漏洞修复并阻断攻击路径，同时启动全网应急响应。为降低账户被盗风险，公司联合各ISP推动受影响用户修改密码，并计划通过运营商实施**强制密码重置**，确保所有受影响账户完成密码更新。

技术层面，KDDI于**6月21日**完成所有对外通信服务器的EDR部署，以强化恶意行为检测能力；随后委托第三方专业机构开展取证分析，确认除本次漏洞外，未发现其他异常攻击痕迹。与此同时，公司还向日本总务省提交了正式调查报告，以履行《电气通信事业法》规定的监管报告义务。

## 后续整改：引入AI分析代码，推动邮件协议升级

值得关注的是，KDDI提出了一系列具有前瞻性的整改措施。

一方面，公司计划利用**人工智能（AI）技术**对第三方软件设计文档及源代码开展系统性分析，对潜在缺陷进行全面排查，希望在传统漏洞扫描之外发现深层次设计缺陷。另一方面，KDDI还计划与各ISP共同推进更高安全等级的邮件通信协议和基础设施升级，在兼顾传统邮件客户端兼容性的前提下，逐步提升整个行业邮件系统的安全水平。

## 安全观察：事件暴露共享基础设施的系统性风险

此次事件具有较强的行业代表性，其影响远超单一运营商数据泄露。

首先，攻击目标并非某一家ISP，而是**共享邮件基础设施**。当多个运营商依赖同一邮件平台时，一旦核心平台出现漏洞，将形成"一点突破、多方受影响"的放大效应。这也是近年来供应链攻击持续增长的重要原因。

其次，本次事件再次证明**零日漏洞防御能力**已成为大型运营商的重要安全能力。攻击者利用供应商尚未知晓的漏洞完成长期潜伏，传统依赖漏洞补丁和签名检测的安全措施难以及时发现异常，更需要通过EDR、行为分析、威胁狩猎以及持续监测机制提升未知威胁发现能力。

此外，本次事件也反映出**第三方软件安全治理**的重要性。对于运营关键基础设施的企业而言，仅关注自身代码安全已远远不够，还应建立覆盖供应商软件、开源组件及外部服务的全生命周期安全管理体系，包括软件物料清单（SBOM）、供应链风险评估、第三方漏洞响应机制以及持续安全验证等措施。

## KDDI事件再次说明，在数字基础设施高度共享、供应链深度耦合的今天，网络攻击已经从单点系统渗透演变为针对整个生态链的系统性攻击。对于电信运营商、互联网平台以及关键信息基础设施运营者而言，未来网络安全建设重点不仅在于"修补漏洞"，更应建立**持续监测、供应链安全治理、零信任访问控制、EDR/XDR联动检测、AI辅助漏洞分析以及快速应急响应**等综合防御能力，从而提升面对未知漏洞和高级持续性攻击（APT）的整体安全韧性。

---

[等保、关保、数保、个保，网络安全与数据治理“四位一体”的体系化制度框架](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505812&idx=1&sn=018455069df3d9894104953c6e14a91f&scene=21#wechat_redirect)

**[网络安全等级保护制度统一框架辨析](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505812&idx=1&sn=018455069df3d9894104953c6e14a91f&scene=21#wechat_redirect)**

---

**>>>等级保护<<<**

**[从资质驱动到能力驱动——新标准下测评机构的生与死](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[测评机构迎大考，安全厂商的机会来了！](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[测评机构的回旋镖来了！测评机构不仅要会“测别人”，更要先“管好自己”](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[新标准背景下等级测评机构应培养什么样的人才](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[供应链企业应该如何适应等级保护发展](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[网络安全等级保护制度演进，安全治理思维的演变](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

[网络安全等级保护之安全物理环境](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全区域边界](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全通信网络](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全计算环境](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全管理中心](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全管理制度](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全管理机构](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全管理人员](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全建设管理](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

[网络安全等级保护之安全运维管理](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)

**[网络安全等级保护制度演进，回看2003年27号文](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505801&idx=1&sn=958f82ebcc5a21a127373e93aa1ab825&scene=21#wechat_redirect)**

**[网络安全等级保护制度演进，回看2004年66号文](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505809&idx=1&sn=2403c84d9c92c697d9083bc79e7469a0&scene=21#wechat_redirect)**

**[网络安全等级保护制度演进，回看2006年7号文（过渡性文件）](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505809&idx=1&sn=2403c84d9c92c697d9083bc79e7469a0&scene=21#wechat_redirect)**

[《等级保护条例》迎来最新进展](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505649&idx=1&sn=342bf65417e243d0771ca56d852e76a4&scene=21#wechat_redirect)

[网络安全等级保护制度统一框架辨析](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505789&idx=1&sn=239bac6ed28aa1bbf7c7d36cbf0b7f57&scene=21#wechat_redirect)

[网络安全等级保护安全物理环境之防盗窃和防破坏实现](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121519&idx=1&sn=631a7fe01f6172254409e26272c68ffe&scene=21#wechat_redirect)

[网络安全等级保护物理访问控制实现](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121492&idx=2&sn=2dc3e4c889b8b33464176a871dd2fac5&scene=21#wechat_redirect)

[信息安全技术 网络安全等级保护测评过程指南](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121469&idx=1&sn=745b1a5bbb2c0bac74d0cbcdf03bf2e0&scene=21#wechat_redirect)

[夜读：GB 17859-1999安全保护等级划分准则](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121433&idx=1&sn=0074031432dd648b7d41627c11b520d2&scene=21#wechat_redirect)

[等级保护基本要求标准系列](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121261&idx=1&sn=83eaa31a45d33b441a84a1ffafac583d&scene=21#wechat_redirect)

[等级保护的数据摸底调查](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652120232&idx=1&sn=4e95783ee5fd62e9e9cc8b74103fc310&scene=21#wechat_redirect)

[网络安全等级保护自查清单（对照法条）](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652121146&idx=1&sn=07cef95c28356b7f740a00f94ab7f170&scene=21#wechat_redirect)

[由新《网安法》罚则看等级保护、应急安全责任](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652120509&idx=1&sn=db3380982915487b4689a312349f984f&scene=21#wechat_redirect)

[等级保护的数据摸底调查](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652120232&idx=1&sn=4e95783ee5fd62e9e9cc8b74103fc310&scene=21#wechat_redirect)

[以等级保护为中轴线/基础的网络安全监管体系发展](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505443&idx=1&sn=b55926a407e187fd62563c8cae51199a&scene=21#wechat_redirect)

[网络运营者等级保护合规自查表](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247505260&idx=1&sn=ed42da685a9950029b024dd9bbc89247&scene=21#wechat_redirect)

[信息安全技术 网...