---
title: 加密货币 APT 情报：揭秘 Lazarus Group 入侵手法
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501259&idx=1&sn=0b2183929367aa5845f0a9e1d1a42e74&chksm=fddebb4ccaa9325a643092adbf32e184c96a1c95717f5f587e160eb60729319775c5ea708de0&scene=58&subscene=0#rd
source: 慢雾科技
date: 2025-02-24
fetch_date: 2025-10-06T20:36:34.008643
---

# 加密货币 APT 情报：揭秘 Lazarus Group 入侵手法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZ37iaPF8PIlB9zofacGibnwsmfPAQra8oJlW0w6nUbltbbj3OfsibNlOfIbfdRCCEKfOSjQxm0iblCVA/0?wx_fmt=jpeg)

# 加密货币 APT 情报：揭秘 Lazarus Group 入侵手法

原创

慢雾安全团队

慢雾科技

作者：23pds & Thinking

编辑：Liz

**背景**

自 2024 年 6 月以来，慢雾安全团队陆续收到多家团队的邀请，对多起黑客攻击事件展开取证调查。经过前期的积累以及对过去 30 天的深入分析调查，我们完成了对黑客攻击手法和入侵路径的复盘。结果表明，这是一场针对加密货币交易所的国家级 APT 攻击。通过取证分析与关联追踪，我们确认攻击者正是 Lazarus Group。

在获取相关 IOC（入侵指标）和 TTP（战术、技术与程序）后，我们第一时间将该情报同步给合作伙伴。同时，我们还发现其他合作伙伴也遭遇了相同的攻击方式和入侵手法。不过，相较之下他们较为幸运 —— 黑客在入侵过程中触发了部分安全告警，在安全团队的及时响应下，攻击被成功阻断。

鉴于近期针对加密货币交易所的 APT 攻击持续发生，形势愈发严峻，我们在与相关方沟通后，决定对攻击的 IOC 和 TTP 进行脱敏处理并公开发布，以便社区伙伴能够及时防御和自查。同时，受保密协议限制，我们无法披露过多合作伙伴的具体信息。接下来，我们将重点分享攻击的 IOC 和 TTP。

### **攻击者信息**

攻击者域名：

* gossipsnare[.]com, 51.38.145.49:443
* showmanroast[.]com, 213.252.232.171:443
* getstockprice[.]info, 131.226.2.120:443
* eclairdomain[.]com, 37.120.247.180:443
* replaydreary[.]com, 88.119.175.208:443
* coreladao[.]com
* cdn.clubinfo[.]io

涉及事件的 IP：

* 193.233.171[.]58
* 193.233.85[.]234
* 208.95.112[.]1
* 204.79.197[.]203
* 23.195.153[.]175

攻击者的 GitHub 用户名：

* https://github.com/mariaauijj
* https://github.com/patriciauiokv
* https://github.com/lauraengmp

攻击者的社交账号：

* Telegram: @tanzimahmed88

后门程序名称：

* StockInvestSimulator-main.zip
* MonteCarloStockInvestSimulator-main.zip
* 类似 …StockInvestSimulator-main.zip 等

真实的项目代码：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZ37iaPF8PIlB9zofacGibnws9s1lwR7p2PUB7qLDtmQzLOnqfEKX1iadBFQJzSduwYMyqEH2APZ1c8w/640?wx_fmt=png&from=appmsg)

 (https://github.com/cristianleoo/montecarlo-portfolio-management)

攻击者更改后的虚假项目代码：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZ37iaPF8PIlB9zofacGibnwsWQj9DM9F4mqeP2FMkS4nTKAYwuS8GMKE1gxKazv2dsibQPsH2N2A2Aw/640?wx_fmt=png&from=appmsg)

对比后会发现，data 目录多了一个 data\_fetcher.py 文件，其中包含一个奇怪的 Loader：

```
...elif content_type.startswith("application/yaml"):    data = yaml.load(response.text, Loader=yaml.Loader)                    #response.raise_for_status()self.prices = data...
```

### **攻击者使用的后门技术**

攻击者利用 pyyaml 进行 RCE（远程代码执行），实现恶意代码下发，从而控制目标电脑和服务器。这种方式绕过了绝大多数杀毒软件的查杀。在与合作伙伴同步情报后，我们又获取了多个类似的恶意样本。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZ37iaPF8PIlB9zofacGibnwsZM5rVCYtoUOYLH1D2SqPEyYtnmdHiaPZm8huicvxkc4Dg9TLT0IYa83w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZ37iaPF8PIlB9zofacGibnwsSAsNq88Tb2LuMpb5OCibep6mbBLkPicdqyFQJ7v09uUqJx1009iaTDibNg/640?wx_fmt=png&from=appmsg)

关键技术分析参考：https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation#how-to-disable-the-warning

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZ37iaPF8PIlB9zofacGibnwsicgLGlWkqicqWxK07nMMIRcNsx5FicoD9lyvX3vbDSwhQrarDldmlaYYw/640?wx_fmt=png&from=appmsg)

慢雾安全团队通过对样本的深入分析，成功复现了攻击者利用 pyyaml 进行 RCE（远程代码执行）的攻击手法。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZ37iaPF8PIlB9zofacGibnws9XoMLLvZg5K8dyPWvQCpNJUIqk10vOKAId2qlJKZjIhCg9FstUNW9w/640?wx_fmt=png&from=appmsg)

###

### **攻击关键分析**

**目标和动机**

目标：攻击者的主要目标是通过入侵加密货币交易所的基础设施，获取对钱包的控制权，进而非法转移钱包中的大量加密资产。

动机：试图窃取高价值的加密货币资产。

**技术手段**

1. 初始入侵

* 攻击者利用社会工程学手段，诱骗员工在本地设备或 Docker 内执行看似正常的代码。
* 在本次调查中，我们发现攻击者使用的恶意软件包括 `StockInvestSimulator-main.zip` 和 `MonteCarloStockInvestSimulator-main.zip`。这些文件伪装成合法的 Python 项目，但实则是远程控制木马，并且攻击者利用 pyyaml 进行 RCE，作为恶意代码的下发和执行手段，绕过了大多数杀毒软件的检测。

2. 权限提升

* 攻击者通过恶意软件成功获取员工设备的本地控制权限，并且诱骗员工将 docker-compose.yaml 中的 privileged 设置为 true。
* 攻击者利用 privileged 设置为 true 的条件进一步提升了权限，从而完全控制了目标设备。

3. 内部侦察和横向移动

* 攻击者利用被入侵的员工电脑对内网进行扫描。
* 随后，攻击者利用内网的服务和应用漏洞，进一步入侵企业内部服务器。
* 攻击者窃取了关键服务器的 SSH 密钥，并利用服务器之间的白名单信任关系，实现横向移动至钱包服务器。

4. 加密资产转移

* 攻击者成功获得钱包控制权后，将大量加密资产非法转移至其控制的钱包地址。

5. 隐藏痕迹

* 攻击者利用合法的企业工具、应用服务和基础设施作为跳板，掩盖其非法活动的真实来源，并删除或破坏日志数据和样本数据。

**过程**

攻击者通过社会工程学手段诱骗目标，常见方式包括：

1. 伪装成项目方，寻找关键目标开发人员，请求帮助调试代码，并表示愿意提前支付报酬以获取信任。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZ37iaPF8PIlB9zofacGibnwsr3Hic8dcG5GiagdnxJdpicrGM40NX46AYtPIqUEng9yibk4gaQWmYB6XBA/640?wx_fmt=png&from=appmsg)

我们追踪相关 IP 和 ua 信息后发现，这笔交易属于第三方代付，没有太多价值。

2. 攻击者伪装成自动化交易或投资人员，提供交易分析或量化代码，诱骗关键目标执行恶意程序。一旦恶意程序在设备上运行，它会建立持久化后门，并向攻击者提供远程访问权限。

* 攻击者利用被入侵设备扫描内网，识别关键服务器，并利用企业应用的漏洞进一步渗透企业网络。所有攻击行为均通过被入侵设备的 VPN 流量进行，从而绕过大部分安全设备的检测。
* 一旦成功获取相关应用服务器权限，攻击者便会窃取关键服务器的 SSH 密钥，利用这些服务器的权限进行横向移动，最终控制钱包服务器，将加密资产转移到外部地址。整个过程中，攻击者巧妙利用企业内部工具和基础设施，使攻击行为难以被快速察觉。
* 攻击者会诱骗员工删除调试运行的程序，并且提供调试报酬，以掩盖攻击痕迹。

此外，由于部分受骗员工担心责任追究等问题，可能会主动删除相关信息，导致攻击发生后不会及时上报相关情况，使得排查和取证变得更加困难。

### **应对建议**

APT（高级持续性威胁）攻击因其隐蔽性强、目标明确且长期潜伏的特点，防御难度极高。传统安全措施往往难以检测其复杂的入侵行为，因此需要结合多层次网络安全解决方案，如实时监控、异常流量分析、端点防护与集中日志管理等，才能尽早发现和感知攻击者的入侵痕迹，从而有效应对威胁。慢雾安全团队提出 8 大防御方向和建议，希望可以为社区伙伴提供防御部署的参考：

**1. 网络代理安全配置**

**目标：**在网络代理上配置安全策略，以实现基于零信任模型的安全决策和服务管理。

**解决方案：**Fortinet (https://www.fortinet.com/), Akamai (https://www.akamai.com/glossary/where-to-start-with-zero-trust), Cloudflare (https://www.cloudflare.com/zero-trust/products/access/) 等。

**2. DNS 流量安全防护**

**目标：**在 DNS 层实施安全控制，检测并阻止解析已知恶意域名的请求，防止 DNS 欺骗或数据泄露。

**解决方案：**Cisco Umbrella (https://umbrella.cisco.com/) 等。

**3. 网络流量/主机监控与威胁检测**

**目标：**分析网络请求的数据流，实时监测异常行为，识别潜在攻击（如 IDS/IPS），服务器安装 HIDS，以便尽早发现攻击者的漏洞利用等攻击行为。

**解决方案：**SolarWinds Network Performance Monitor (https://www.solarwinds.com/), Palo Alto (https://www.paloaltonetworks.com/), Fortinet (https://www.fortinet.com/), 阿里云安全中心 (https://www.alibabacloud.com/zh/product/security\_center), GlassWire (https://www.glasswire.com/) 等。

**4. 网络分段与隔离**

**目标：**将网络划分为较小的、相互隔离的区域，限制威胁传播范围，增强安全控制能力。

**解决方案：**Cisco Identity Services Engine (https://www.cisco.com/site/us/en/products/security/identity-services-engine/index.html)，云平台安全组策略等。

**5. 系统加固措施**

**目标：**实施安全强化策略（如配置管理、漏洞扫描和补丁更新），降低系统脆弱性，提升防御能力。

**解决方案：**Tenable.com (https://www.tenable.com/), public.cyber.mil (https://public.cyber.mil) 等。

**6. 端点可见性与威胁检测**

**目标：**提供对终端设备活动的实时监控，识别潜在威胁，支持快速响应（如 EDR），设置应用程序白名单机制，发现异常程序并及时告警。

**解决方案：**CrowdStrike Falcon (https://www.crowdstrike.com/), Microsoft Defender for Endpoint (https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint), Jamf (https://www.jamf.com/) 或 WDAC (https://learn.microsoft.com/en-us/hololens/windows-defender-application-control-wdac) 等。

**7. 集中日志管理与分析**

**目标：**将来自不同系统的日志数据整合到统一平台，便于安全事件的追踪、分析和响应。

**解决方案：**Splunk Enterprise Security (https://www.splunk.com/), Graylog (https://graylog.org/), ELK (Elasticsearch, Logstash, Kibana) 等。

**8. 培养团队安全意识**

**目标：**提高组织成员安全意识，能够识别大部分社会工程学攻击，并在出事后主动上报异常，以便更及时进行排查。

**解决方案：**区块链黑暗森林自救手册 (https://darkhandbook.io/), Web3 钓鱼手法分析 (https://github.com/slowmist/Knowledge-Base/blob/master/security-research/Web3%20%E9%92%93%E9%B1%BC%E6%89%8B%E6%B3%95%E8%A7%A3%E6%9E%90.pdf) 等。

此外，我们建议周期性开展红蓝对抗的演练，以便识别出安全流程管理和安全防御部署上的薄弱点。

### **写在最后**

攻击事件常常发生在周末及传统节假日期间，给事件响应和资源协调带来了不小的挑战。在这一过程中，慢雾安全团队的 23pds（山哥）, Thinking, Reborn 等相关成员始终保持警觉，在假期期间轮班应急响应，持续推进调查分析。最终，我们成功还原了攻击者的手法和入侵路径。

回顾本次调查，我们不仅揭示了 Lazarus Group 的攻击方式，还分析了其利用社会工程学、漏洞利用、权限提升、内网渗透及资金转移等一系列战术。同时，我们基于实际案例总结了针对 APT 攻击的防御建议，希望能为行业提供参考，帮助更多机构提升安全防护能力，减少潜在威胁的影响。网络安全对抗是一场持久战，我们也将持续关注类似攻击，助力社区共同抵御威胁。

**往期回顾**

[慢雾：Bybit 近 15 亿美元被盗背后的黑客手法与疑问](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501246&idx=1&sn=eafc7080cc28d1f8bf16c362f3ac2230&scene=21#wechat_redirect)

[顺藤摸瓜｜披露假冒慢雾员工行骗事件](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501212&idx=1&sn=996e238a420e98e240db4cddefff0343&scene=21#wechat_redirect)

[风险提醒｜从 LIBRA 看“政治化”的加密货币骗局](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501191&idx=1&sn=26c082e5b96c433a9292785b1089f88c&scene=21#wechat_redirect)

[连环作案｜zkLend 被黑深度分析，关联 EraLend 事件](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501146&idx=1&sn=90497fe1fb951860c7927052f13be74d&scene=21#wechat_redirect)

[慢雾：AAVE V2 安全审计手册](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247501098&idx=1&sn=341bf68002be703b2f92d3c822dcf587&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaa3Th7YiamUUBwq1Iiby9N9lWh3tKP2MVjM6L3UxtTnuUy6iaegsOP2IrqZYsIBM2v3XgC5O2JTbY5g/640?wx_fmt=png&from=appmsg)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**T...