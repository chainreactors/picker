---
title: Palo Alto Networks PAN-OS身份认证绕过+远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507450&idx=1&sn=baba096592ba4c2ce7f2849d12b10277&chksm=cfcabeeef8bd37f89467ead114de2ac0cf01ef8fcabc14a2993ad364fd7dbb510b9ab01a82b5&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-11-22
fetch_date: 2025-10-06T19:16:31.378561
---

# Palo Alto Networks PAN-OS身份认证绕过+远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMI9AicGNHltEFNliaEU67CwgSibfONW0ib18vsxvniae0dvDGyNH4YzdjmskGMeKXoCGr0Cr6FzbVsxu5w/0?wx_fmt=jpeg)

# Palo Alto Networks PAN-OS身份认证绕过+远程代码执行漏洞

原创

微步情报局

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMKNkm4Pg1Ed6nv0proxQLEKJ2CUCIficfAwKfClJ84puialc9eER0oaibMn1FDUpibeK1t1YvgZcLYl3A/640?wx_fmt=png)

**漏洞概况**

PAN-OS 是 Palo Alto Networks 公司开发的下一代防火墙操作系统，为 Palo Alto Networks 防火墙提供安全功能和集中管理能力。

微步情报局近日捕获到Palo Alto Networks PanOS身份认证绕过漏洞情报(CVE-2024-0012，https://x.threatbook.com/v5/vul/XVE-2024-0659)和Palo Alto Networks PanOS 远程代码执行漏洞情报(CVE-2024-9474，https://x.threatbook.com/v5/vul/XVE-2024-33390)。

CVE-2024-0012 漏洞可绕过身份认证，访问后台接口。

CVE-2024-9474 漏洞可在身份认证后，实现命令注入。

二者形成结合利用链，即可实现未授权条件下的前台远程命令执行漏洞，利用难度较低。CISA（https://www.cisa.gov/known-exploited-vulnerabilities-catalog） 和 Palo Alto官方（https://unit42.paloaltonetworks.com/cve-2024-0012-cve-2024-9474/）称已观察到上述漏洞的利用行为，建议受影响的用户尽快修复。

**漏洞处置优先级(VPT)**

**综合处置优先级：高**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2024-0659 XVE-2024-33390 |
| 漏洞类型 | 身份认证绕过  远程命令执行 |
| **利用条件评估** | 利用漏洞的网络条件 | 远程 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 默认配置 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | POC是否公开 | 是 |
| 已知利用行为 | 是 |

#

**漏洞影响范围**

|  |  |
| --- | --- |
| **产品名称** | Palo Alto Networks - PAN-OS |
| **受影响版本** | CVE-2024-0012漏洞影响范围：  10.2.0 ≤ version < 10.2.12  11.0.0 ≤ version < 11.0.6  11.1.0 ≤ version < 11.1.5  11.2.0 ≤ version < 11.2.4  CVE-2024-9474漏洞影响范围：  10.1.0 ≤ version < 10.1.14  10.2.0 ≤ version < 10.2.12  11.0.0 ≤ version < 11.0.6  11.1.0 ≤ version < 11.1.5  11.2.0 ≤ version < 11.2.4    注意：两个漏洞的影响范围并不完全一致，10.1.x版本存在认证后命令注入漏洞，但不存在认证绕过，无法实现前台rce |
| **有无修复补丁** | 有 |

前往X情报社区资产测绘查看影响资产详情：

https://x.threatbook.com/v5/survey?q=app%3D%22Palo%20Alto%20Networks%20PAN-OS%20Firewall%22

**漏洞复现**

绕过身份认证并实现远程命令执行：

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMI9AicGNHltEFNliaEU67CwgSzq16ohMRc6ib9YZpL7a4yeyxn1yXQoibaMLshr9P5Yu858p0YQgmdygQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMI9AicGNHltEFNliaEU67CwgSz0qmWzS8haOt0AVZ1woqNy1ayIusyCwXBP6ro8ZpsfWyHccWjvcKmw/640?wx_fmt=png)

**修复方案**

**官方修复方案：**

官方已发布漏洞公告，请尽快更新至PAN-OS 10.1.14-h6、PAN-OS 10.2.12-h2、PAN-OS 11.0.6-h1、PAN-OS 11.1.5-h1、PAN-OS 11.2.4-h1 及所有更高版本的 PAN-OS。

漏洞公告地址：

1. https://security.paloaltonetworks.com/CVE-2024-0012
2. https://security.paloaltonetworks.com/CVE-2024-9474

## **临时修复方案：**

* 将对管理接口的访问限制为仅受信任的内部 IP 地址，以防止来自互联网的外部访问。
* 使用防护类设备进行防护，重点关注和监控Header中带有“X-PAN-AUTHCHECK: off”的请求。

**相关攻击IP**

91.208.197[.]167

104.28.208[.]123

136.144.17[.]146

136.144.17[.]149

136.144.17[.]154

136.144.17[.]158

136.144.17[.]161

136.144.17[.]164

136.144.17[.]166

136.144.17[.]167

136.144.17[.]170

136.144.17[.]176

136.144.17[.]177

136.144.17[.]178

136.144.17[.]180

173.239.218[.]248

173.239.218[.]251

209.200.246[.]173

209.200.246[.]184

216.73.162[.]69

216.73.162[.]71

216.73.162[.]73

216.73.162[.]74

来源：https://unit42.paloaltonetworks.com/cve-2024-0012-cve-2024-9474/

**微步产品侧支持情况**

微步威胁感知平台TDP已于2024年11月20日支持检测，检测ID为S3100157358、S3100157359，模型/规则高于 20241120000000 可检出。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMI9AicGNHltEFNliaEU67CwgSYLX50UibWn0iaOkStP3FLFv1qyz5r9znAxdpPPMHan2plJad6S0Ac2lg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMI9AicGNHltEFNliaEU67CwgSgvYDmBmANuSSDiaHfNXgGiaiasfqbQzScUM8swiaTvHe2eiaKfLNYvPibNlA/640?wx_fmt=png)

- END -

//

**微步漏洞情报订阅服务**

微步提供漏洞情报订阅服务，精准、高效助力企业漏洞运营：

* 提供高价值漏洞情报，具备及时、准确、全面和可操作性，帮助企业高效应对漏洞应急与日常运营难题；
* 可实现对高威胁漏洞提前掌握，以最快的效率解决信息差问题，缩短漏洞运营MTTR；
* 提供漏洞完整的技术细节，更贴近用户漏洞处置的落地；
* 将漏洞与威胁事件库、APT组织和黑产团伙攻击大数据、网络空间测绘等结合，对漏洞的实际风险进行持续动态更新。

扫码在线沟通

↓↓↓

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQl5bZ5Mx6PTAQg6tGLiciarvXajTdDnQiacxmwJFZ0D3ictBOmuYyRk99bibwZV49wbap77LibGQHdQPtA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTIdM9koHZFkrtYe5WU5rHxSDicbiaNFjEBAs1rojKGviaJGjOGd9KwKzN4aSpnNZDA5UWpY2E0JAnNg/640?wx_fmt=png)

点此电话咨询

**X漏洞奖励计划**

“X漏洞奖励计划”是微步X情报社区推出的一款针对未公开漏洞的奖励计划，我们鼓励白帽子提交挖掘到的0day漏洞，并给予白帽子可观的奖励。我们期望通过该计划与白帽子共同努力，提升0day防御能力，守护数字世界安全。

活动详情：https://x.threatbook.com/v5/vulReward

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

微步在线研究响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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