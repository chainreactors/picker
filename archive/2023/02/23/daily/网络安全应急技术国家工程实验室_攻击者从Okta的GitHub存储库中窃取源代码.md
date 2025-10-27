---
title: 攻击者从Okta的GitHub存储库中窃取源代码
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247534764&idx=5&sn=8f388da8b347be30a273a58c16fcd3d5&chksm=fa93fe6dcde4777b0d6a595e7e21602b00670c4351a2866c75c1e3b17ff0b84915eb20c414bf&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2023-02-23
fetch_date: 2025-10-04T07:52:01.952734
---

# 攻击者从Okta的GitHub存储库中窃取源代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kR03VqkY7LXQfSSde6NTVu3GhBGRlXibAicCZESgTltML7T4SacAJQzLcibZZ15hVCsSX5Go8B1ffkQ/0?wx_fmt=jpeg)

# 攻击者从Okta的GitHub存储库中窃取源代码

网络安全应急技术国家工程中心

本月初，微软旗下的GitHub向Okta发出警告，称其代码库存在 "可疑的访问"，并确定不法分子复制了与该公司的Workforce Identity Cloud（WIC）相关的代码，WIC是一个面向企业的访问和身份管理工具，该工具可以使员工和合作伙伴能够在任何地方工作。

该公司在本周的一份声明中说，其调查发现WIC服务本身并没有被破坏，也没有发生客户数据被未授权访问，这些数据包括HIPAA、FedRAMP或国防部客户的数据。

此外，Okta表示，它并不需要源代码的保密性来保证其服务的安全性，所以它仍然可以安全的运行。

官员们还说，该漏洞并没有影响到Auth0或Okta的消费者和软件即服务（SaaS）应用的客户身份云信息。Okta去年以65亿美元的价格收购了Auth0，这笔交易将两家备受瞩目的身份和访问管理（AIM）供应商结合在了一起。

在得知发现了可疑的访问后，该供应商暂时限制了对Okta的GitHub存储库的访问权限，并暂停GitHub与第三方应用程序的集成。

Okta说，此后，我们审查了最近对GitHub托管的Okta软件库的所有访问记录，调查信息泄露的范围，而且审查了最近对GitHub托管的Okta软件库的所有提交，验证我们代码的完整性，并轮换了GitHub凭证，而且也通知了执法机构。

网络安全公司Cybrary的高级安全研究员Matt Mullins在一封电子邮件中告诉媒体，Okta的GitHub漏洞也只是网络犯罪分子在供应链攻击中向上游移动寻找潜在受害者时针对开发人员和代码进行攻击的最新例子。

Mullins说，进入这些系统给APT[高级持续性威胁]集团带来的好处是可以提前发现他们的目标并研究漏洞（如代码中明显的漏洞）、秘钥（如脚本中的硬编码信条）或其他错误的配置（如配置中的明文模式）。

他补充说，由于像Okta这样的服务对企业是如此的重要，攻击者将继续以'安全'供应商为目标进行攻击，这很令人震惊。那么企业的安全谁来负责？

今年以来，Okta已经成为不法分子的攻击目标。今年1月，该公司遭到了高调的Lapsus$勒索集团的攻击，该集团在通过内部员工的工作站获得访问权后，得以进入Okta的内部系统。官员们在今年晚些时候猜想说，如果没有实施零信任政策，这次攻击造成的后果可能会更糟糕。

8月，网络安全公司Group-IB发现了一场始于3月份的大规模网络钓鱼活动，被称为Oktapus。该攻击活动旨在窃取130多个目标组织（包括Twilio和Cloudflare）用户的Okta身份凭证和双因素认证（2FA）代码，然后攻击其组织内的客户。

9月，Auth0作为一家独立的运营公司，对外称最近发生了一个 "安全事件"，该案件涉及到2020年10月Okta收购前的代码相关的存储库。然而，该公司也表示，目前没有证据表明其环境或客户的环境被恶意访问，数据被盗，或其系统中存在内鬼。

**参考及来源：**

https://www.theregister.com/2022/12/23/okta\_code\_copy\_hack/?td=rt-3a

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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