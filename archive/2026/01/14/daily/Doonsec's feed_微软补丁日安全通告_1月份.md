---
title: 微软补丁日安全通告|1月份
url: https://mp.weixin.qq.com/s/YtlwJnxSBjjRBJIvmeYzqw
source: Doonsec's feed
date: 2026-01-14
fetch_date: 2026-01-15T03:29:50.453034
---

# 微软补丁日安全通告|1月份

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6AXx2DwE6E7JlMoMslDIBcIHhufepX2c6TnZ2EC1SZVTospz8W0Q37icA/0?wx_fmt=jpeg)

# 微软补丁日安全通告|1月份

深益研究实验室

深信服千里目安全技术中心

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6AWHiau64gVQzuuOuE83FU6rpY55yibVX36AX0A60wSaaD1GIy5m02zs4Q/640?wx_fmt=gif&from=appmsg)

2026年1月14日（北京时间），微软发布了2026年 1月安全更新，共发布了115个CVE的补丁程序，比上月增多了45个。

在漏洞安全等级方面，存在8个标记等级为“Critical”的漏洞，57个漏洞被标记为“Important/High”等级的漏洞； 在漏洞类型方面，主要有21个远程代码执行漏洞，58个权限提升漏洞以及22个信息泄露漏洞。

**漏洞分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6ATn4ABX5ctHFKBCaQc5skDXtTPYd6atpTERPovPPNsOQTTuBzv3iaOMw/640?wx_fmt=gif&from=appmsg)

**2026年漏洞数量趋势**

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6Ax6USzunwpyhILan0SRoZAdnqbBQLoWzOPVX6cTY7MNtL6z1CAtF1Mg/640?wx_fmt=png&from=appmsg)

图 1 近一年微软补丁漏洞修复情况

总体上来看，微软本月发布的补丁数量为115个，有8个 Critical 漏洞补丁。

千里目安全技术中心在综合考虑往年微软公布漏洞数量的数据统计和今年的特殊情况，初步估计微软在今年二月份公布的漏洞数将比今年一月份少。漏洞数量将会维持在80个左右。

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6ATn4ABX5ctHFKBCaQc5skDXtTPYd6atpTERPovPPNsOQTTuBzv3iaOMw/640?wx_fmt=gif&from=appmsg)

**历史微软补丁日12月漏洞对比**

2023-2026年，1月份的漏洞数趋势如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6A9vmzs8rib0OyLlXS6srbPowUm4Xn0gY0ndu6CKibXpkYVibribSUJ4vOfQ/640?wx_fmt=png&from=appmsg)

图 2 微软近年1月Windows补丁漏洞数量对比

2023-2026年，1月份的漏洞危险等级趋势和数量如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6AeHCUCia0Xicc7kro3xQUm5a0r7a5uG0Mg1toVzvBePIKsvuRY4WUr6DA/640?wx_fmt=png&from=appmsg)

图 3 微软近年1月漏洞危险等级对比

2023-2026年，1月份的漏洞各个类型数量对比如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6Av4kSHnUzwB4XY56CyCEjp1ghGVvVpu1ibqicUIGk92WiburcNVPLr3Unw/640?wx_fmt=png&from=appmsg)

图 4 微软近年1月漏洞类型对比

数据来源：根据微软官方安全更新通告中的数据统计

* **从漏洞数量来看，今年相较去年减少。**微软在2026年1月份爆发的漏洞相较于去年减少。本月出现了115个漏洞补丁，并且有8个 Critical 类型的漏洞补丁。

* **从漏洞的危险等级来看，相较去年“Critical”等级的漏洞数量减少，“Important/High”等级的漏洞数量减少。**本月出现了8个“Critical”等级的漏洞，相较去年减少了约27%；本月出现了107个“Important/High”等级的漏洞，相较去年减少了约29%。

**从漏洞类型来看，RCE类型的漏洞数量减少，DoS类型的漏洞数量减少，EoP类型的漏洞数量增多****，**需要引起高度重视，尤其是RCE漏洞在配合社工手段的前提下，甚至可以直接接管整个局域网并进行进一步扩展攻击。

**重要漏洞分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6ATn4ABX5ctHFKBCaQc5skDXtTPYd6atpTERPovPPNsOQTTuBzv3iaOMw/640?wx_fmt=gif&from=appmsg)

**漏洞分析**

**桌面窗口管理器信息泄露漏洞 CVE-2026-20805**

DWM桌面窗口管理器是自Windows Vista以来Microsoft Windows中的合成窗口管理器，它允许使用硬件加速来呈现 Windows 的图形用户界面。它最初是为了启用部分新的“ Windows Aero ”用户体验而创建的，它允许诸如透明度、3D 窗口切换等效果。

其中存在信息泄露漏洞，攻击者可以利用该漏洞在目标系统获取未授权的信息。该漏洞存在在野利用，经过评估，危害比较大，我们建议用户及时更新微软安全补丁。

**安全引导证书过期安全功能绕过漏洞 CVE-2026-21265**

Secure Boot（安全启动） 是 Windows 依托 UEFI 固件 提供的一项启动完整性保护机制，用于在系统启动早期阻止未签名或被篡改的启动组件执行，从而防御引导级恶意软件（如 bootkit、rootkit）。

其中存在安全功能绕过漏洞，攻击者可以利用该漏洞在绕过目标系统上的安全功能，做出规定之外的行为。漏洞经过评估，危害比较大，我们建议用户及时更新微软安全补丁。

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6ATn4ABX5ctHFKBCaQc5skDXtTPYd6atpTERPovPPNsOQTTuBzv3iaOMw/640?wx_fmt=gif&from=appmsg)

**影响范围**

|  |  |
| --- | --- |
| **漏洞名称、CVE编号** | **受影响版本** |
| 桌面窗口管理器信息泄露漏洞  CVE-2026-20805 | Windows Server 2025 (Server Core installation)  Windows Server 2025  Windows Server 2022, 23H2 Edition (Server Core installation)  Windows Server 2022 (Server Core installation)  Windows Server 2022  Windows Server 2019 (Server Core installation)  Windows Server 2019  Windows Server 2016 (Server Core installation)  Windows Server 2016  Windows Server 2012 R2 (Server Core installation)  Windows Server 2012 R2  Windows Server 2012 (Server Core installation)  Windows Server 2012  Windows 11 Version 25H2 for x64-based Systems  Windows 11 Version 25H2 for ARM64-based Systems  Windows 11 Version 24H2 for x64-based Systems  Windows 11 Version 24H2 for ARM64-based Systems  Windows 11 Version 23H2 for x64-based Systems  Windows 11 Version 23H2 for ARM64-based Systems  Windows 10 Version 22H2 for x64-based Systems  Windows 10 Version 22H2 for ARM64-based Systems  Windows 10 Version 22H2 for 32-bit Systems  Windows 10 Version 21H2 for x64-based Systems  Windows 10 Version 21H2 for ARM64-based Systems  Windows 10 Version 21H2 for 32-bit Systems  Windows 10 Version 1809 for x64-based Systems  Windows 10 Version 1809 for 32-bit Systems  Windows 10 Version 1607 for x64-based Systems  Windows 10 Version 1607 for 32-bit Systems |
| 安全引导证书过期安全功能绕过漏洞  CVE-2026-21265 | Windows Server 2025 (Server Core installation)  Windows Server 2025  Windows Server 2022, 23H2 Edition (Server Core installation)  Windows Server 2022 (Server Core installation)  Windows Server 2022  Windows Server 2019 (Server Core installation)  Windows Server 2019  Windows Server 2016 (Server Core installation)  Windows Server 2016  Windows Server 2012 R2 (Server Core installation)  Windows Server 2012 R2  Windows Server 2012 (Server Core installation)  Windows Server 2012  Windows 11 Version 25H2 for x64-based Systems  Windows 11 Version 25H2 for ARM64-based Systems  Windows 11 Version 24H2 for x64-based Systems  Windows 11 Version 24H2 for ARM64-based Systems  Windows 11 Version 23H2 for x64-based Systems  Windows 11 Version 23H2 for ARM64-based Systems  Windows 10 Version 22H2 for x64-based Systems  Windows 10 Version 22H2 for ARM64-based Systems  Windows 10 Version 22H2 for 32-bit Systems  Windows 10 Version 21H2 for x64-based Systems  Windows 10 Version 21H2 for ARM64-based Systems  Windows 10 Version 21H2 for 32-bit Systems  Windows 10 Version 1809 for x64-based Systems  Windows 10 Version 1809 for 32-bit Systems  Windows 10 Version 1607 for x64-based Systems  Windows 10 Version 1607 for 32-bit Systems |

**解决方案**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6ATn4ABX5ctHFKBCaQc5skDXtTPYd6atpTERPovPPNsOQTTuBzv3iaOMw/640?wx_fmt=gif&from=appmsg)

**官方修复建议**

微软官方已更新受影响软件的安全补丁，用户可根据不同系统版本下载安装对应的安全补丁，安全更新链接如下：

1.https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-20805

2.https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21265

**参考链接**

https://msrc.microsoft.com/update-guide/releaseNote/2026-Jan

**时间轴**

**2026/1/14**

微软例行补丁日，微软官网发布漏洞安全公告。

**2026/1/14**

深信服千里目安全技术中心发布安全通告。

点击**阅读原文**，及时关注并登录深信服**智安全平台**，可轻松查询漏洞相关解决方案。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xrMsyoaicqlKfcjiaVXBVK6ATNwo6PG9ULbUmJJuwBOuPTibDmyF4HbDnIhiaUh0TVkGiaPM6KHw1Fe5w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5zvcIHbwGGYKbqDVYsVKzNNia1jYtHf49C7133AlDXAgex2W4lFvpia56tjQQDkiauNBrl08YbxqG01A/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

深信服千里目安全技术中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

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