---
title: Palo Alto Networks Expedition 工具曝关键漏洞，明文密码或泄露
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588707&idx=2&sn=d8b388917808b4ab77f7526a37a8f228&chksm=b18c26a986fbafbfafefb07442a2524806b1f3c1598ea59eff936f42c6f1d5c9c7346e8eb91e&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-17
fetch_date: 2025-10-06T20:10:52.036510
---

# Palo Alto Networks Expedition 工具曝关键漏洞，明文密码或泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibEk705UlQxicQwbKDfcEuVmfUoubL3p8bHEIyYqB3KQ8gOlfN3thj2J4Q/0?wx_fmt=jpeg)

# Palo Alto Networks Expedition 工具曝关键漏洞，明文密码或泄露

看雪学苑

看雪学苑

Palo Alto Networks 近日披露了其 Expedition 迁移工具中的多个关键安全漏洞，这些漏洞可能使攻击者能够执行任意命令并访问敏感的防火墙凭证。这些漏洞包括一个操作系统命令注入漏洞（CVE-2025-0107），该漏洞允许经过身份验证的攻击者以 www-data 用户身份运行任意 OS 命令，从而可能暴露运行 PAN-OS 软件防火墙的用户名、明文密码、设备配置和 API 密钥。

Expedition 工具已于 2024 年12月31日达到生命周期终点（EoL），因此暴露出大量漏洞。已披露的其他漏洞还包括 SQL 注入（CVE-2025-0103、CVSS 7.8）、反射型跨站点脚本（CVE-2025-0104、CVSS 4.7）、任意文件删除（CVE-2025-0105、CVSS 2.7）和通配符扩展枚举（CVE-2025-0106、CVSS 2.7）。

Palo Alto Networks 已在1.2.100版本（针对 CVE-2025-0103、CVE-2025-0104 和 CVE-2025-0107）和版本1.2.101（针对 CVE-2025-0105 和 CVE-2025-0106）中解决了这些安全问题。然而，由于该工具已达到 EoL 状态，公司不打算发布任何其他更新或安全修复程序。

安全研究人员指出，虽然目前没有证据表明这些新漏洞被积极利用，但针对类似漏洞的概念验证漏洞的可用性引发了对未来潜在攻击的担忧。

为了降低这些风险，Palo Alto Networks 强烈建议企业组织采取以下应对措施：

* 升级到 Expedition 1.2.101 或更高版本
* 将网络访问限制为仅授权用户、主机和网络
* 在不频繁使用 Expedition 时完全禁用 Expedition
* 由于已进入 EoL 状态，建议考虑不再使用该工具

Expedition 是一款免费实用程序，旨在帮助企业组织从其他供应商过渡到 Palo Alto Networks 的下一代防火墙（NGFW）平台。虽然这些漏洞不会直接影响 Palo Alto Networks 防火墙、Panorama 设备、Prisma Access 部署或云 NGFW，但它们会严重危害运行 Expedition 易受攻击版本的系统的安全性。使用 Expedition 的组织被敦促立即采取行动，以保护其系统和敏感数据免受这些漏洞的潜在利用。

资讯来源：cybersecuritynews

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibExiboJzOiafqGLvlOkrmU6NIr3qSr7ibpkIo2N5mhCTNXoMl37s2oRSIDw/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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