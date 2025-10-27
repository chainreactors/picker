---
title: 绕过加密防线！微软已修补的 BitLocker 漏洞仍存在被攻击风险
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787711&idx=1&sn=3cd2b76ec096d4383afb18e3ce399839&chksm=8893bd50bfe43446e466c1bc09af7994b9d789df57debae634a246675be581d5c16a8d9e84b7&scene=58&subscene=0#rd
source: 安全客
date: 2025-01-09
fetch_date: 2025-10-06T20:10:44.566177
---

# 绕过加密防线！微软已修补的 BitLocker 漏洞仍存在被攻击风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5hcsNbsL3pE5zKnSNGDtrQjHAMdTCUO03vMF8yonh6MQdu6GsnWpicPSo3rPqt9YRR1MPxPWLImSw/0?wx_fmt=jpeg)

# 绕过加密防线！微软已修补的 BitLocker 漏洞仍存在被攻击风险

安全客

近日，**一项新的研究发现，Windows BitLocker 磁盘加密功能中一个先前已修补的漏洞仍然存在安全隐患，黑客可以利用该漏洞解密信息。**BitLocker 是微软 Windows 操作系统中的一项磁盘加密功能，主要用于保护存储在硬盘上的数据不被未授权访问。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5hcsNbsL3pE5zKnSNGDtrQhicF4ab5iawkxdoQibcfRF15pyFM2gFnVXYw3YMtgeBGJ7cPQ1we3PXxQ/640?wx_fmt=jpeg&from=appmsg)

在德国最近举行的混沌通信大会上，安全研究人员 Thomas Lambertz 表示，微软针对一个中等严重性漏洞（CVE-2023-21563）的补丁并未完全阻止攻击。Lambertz 还指出，与微软的分析相反，该漏洞可以通过网络被利用。

“这种攻击完全是通过网络进行的，”Lambertz 说。“我们只需要插入一个 USB 设备并使用 PXE 启动来利用该漏洞。” PXE（Preboot Execution Environment）启动是一种网络启动技术，允许计算机从网络上的服务器启动操作系统。

Lambertz 在一台完全更新的 Windows 11 设备上展示了名为“bitpixie”的攻击方法，该方法利用了 Windows 设备在启动和恢复过程中处理内存或加密时存在的弱点。通过将设备重启到恢复模式并使用 Windows 启动加载器运行降级版本，研究人员促使设备忘记加密密钥。由于缺乏足够的机制来撤销旧启动加载器版本的认证，Lambertz 表示他获得了对系统内存的访问权限，并从中提取了数据，包括用于解密数据的主密钥。

研究人员还指出，攻击者可能会利用复杂的硬件调试工具来获取受保护的内存内容，进一步绕过 BitLocker 的加密。安全专家表示，这一漏洞并非仅限于特定版本的 Windows 操作系统，部分较老的硬件平台也未能完全符合现代加密标准，导致漏洞的攻击面更为广泛。

Lambertz 强调，漏洞的实际利用也取决于设备的具体配置。例如，某些系统如果未启用受信平台模块（TPM），则即使应用了补丁，BitLocker 的保护也可能变得更加脆弱。TPM 芯片被认为是硬件级的安全防护，可为加密密钥提供额外的物理隔离，因此在没有 TPM 的情况下，攻击者可以更容易地通过启动介质获取敏感数据。

虽然 BitLocker 加密系统被认为是 Windows 平台上一种强有力的数据保护工具，但研究人员指出，任何安全技术都有其局限性，尤其是在面对有经验的攻击者时。随着攻击技术的不断演进，组织和个人必须保持警觉，及时更新系统，防止潜在的安全漏洞被恶意利用。

“BitLocker 的加密本身没有错，但它依赖于操作系统的安全性，”安全专家 Lambertz 表示。“如果操作系统中的其他漏洞得不到及时修复，攻击者仍然可以通过绕过加密保护来访问数据。”

虽然 BitLocker 提供了强大的加密保护，但专家提醒，任何加密技术都无法单纯依赖于一项措施，必须结合其他多层防护手段。除了启用硬件加密，建议企业和个人用户采取以下安全措施：启用多因素身份验证，结合硬件安全模块（如 TPM）和生物识别技术，增强系统的物理和认证安全；定期审计和更新，及时安装安全补丁，并对系统进行定期安全检查，确保没有被攻击者利用的潜在漏洞；强化供应链安全，确保所有硬件设备和软件供应链的安全性，避免被第三方供应商植入后门。

尽管 BitLocker 已被修复的漏洞不再具备直接攻击路径，但它提醒我们，硬件安全和加密保护之间存在的薄弱环节仍然需要关注。对于全球范围内的企业和政府机构而言，保持对供应链和硬件安全的持续关注，并实施全面的加密和身份验证措施，才能更有效地应对日益复杂的网络威胁。

文章参考：

https://www.govinfosecurity.com/patched-bitlocker-flaw-still-susceptible-to-hack-a-27195

**推荐阅读**

|  |
| --- |
| **01**  ｜[新型越狱技术“Bad Likert Judge”突破安全防护](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787704&idx=1&sn=81b143351b8c0cad6145ca6a756fc798&scene=21#wechat_redirect) |
| **02**  ｜[Siri窃听引发集体诉讼](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787696&idx=1&sn=ea2f9e10e14547933467edfa7fb9767e&scene=21#wechat_redirect) |
| **03**  ｜[大众汽车集团发生严重数据泄漏](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787686&idx=1&sn=a51f4aaa0be3120d09f2b25f796c7fa2&scene=21#wechat_redirect) |

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5hcsNbsL3pE5zKnSNGDtrQV9tiaOsD3G7A4Kl5uicammU85Ov7M7LgicUM6nYk8icwGHHQdWxicSu7Spg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5hcsNbsL3pE5zKnSNGDtrQz3CT31IQgbHxqoM61PmSs1dh6rV2S0qVibVQnnD6o84ClhpfksCtSwQ/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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