---
title: 从Okta源代码泄露看GitHub的安全威胁与防护
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247533599&idx=2&sn=88827aae15208408dac59121b34b6747&chksm=fa93f2decde47bc86515dc2bb3d6c93cf26738bec0153a70b9577777e80766a3745e0c5b01e8&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-12-31
fetch_date: 2025-10-04T02:48:17.713022
---

# 从Okta源代码泄露看GitHub的安全威胁与防护

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176leA3nQVDPicooKkhqH9soEMlKJTG1FCMWLvcBmDwu8cO4ib5youXU8cL68pIKicIziagWful5qFhibC8g/0?wx_fmt=jpeg)

# 从Okta源代码泄露看GitHub的安全威胁与防护

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176leA3nQVDPicooKkhqH9soEMv17uMa3bibh1La6vf1vAjRaPfVtr0j1kfaCR8NpKabiaQJNibGQmXyRgA/640?wx_fmt=jpeg)

日前，知名云身份安全服务商Okta正式披露其私有GitHub存储库遭到黑客攻击，部分源代码遭泄露。尽管Okta公司表示，本次泄露事件不会造成其客户的隐私数据安全，Okta有充分的技术手段来保护用户服务安全。但安全研究人员认为，源代码泄露造成隐形危害在短时间内尚难以准确评估。

GitHub拥有9000万活跃用户，是目前全球最受欢迎的源代码管理工具。由于它是信息系统底层基础设施的重要部分，因此长期以来受到非法攻击团伙的重点关注。本次Okta源代码泄漏事件，只是近年针对GitHub代码库非法访问攻击中的最新案例。Dropbox、Gentoo Linux和微软的GitHub账户之前也都遭受过类似的攻击。

攻击者不仅企图获取源代码，同时也觊觎代码中的敏感信息，以便在后续攻击活动中使用。通过访问应用系统的源代码，攻击者可以查找其中的漏洞，然后在后续攻击中利用这些漏洞。同时，攻击者还可以获取存储在GitHub中的硬编码密钥、密码及其他凭据，从而访问托管在AWS、Azure或GCP中的云服务和数据库。

Okta的GitHub代码库被入侵是一个教训深刻的例子，表明了保护企业内部的访问安全到底有多难，但这并不是独特的案例。虽然GitHub提供了一些保护代码管理库应用安全的防护工具，但很多企业组织并不充分知道如何使用工具。而且遗憾的是，一些最重要的安全功能需要额外付费才能够使用。

不过，以下七个实践经验被证明可以提高GitHub的安全性，对于目前正在应用GitHub的企业组织可以尽快关注并尝试应用。

**1.不要将私人账户用于工作**

对于开发人员，私人GitHub账户是其个人品牌履历的一部分，可帮助其职业生涯的晋升和成长。遗憾的是，这也是如今使用GitHub的组织面临的最大漏洞之一：它们对私人账户用于工作往往没有严格管理。从代码安全的角度，私人GitHub账户不应该用于工作，尽管这么做会带来一些便利性，但企业根本没有办法有效控制谁可以访问创建私人GitHub账户的私人Gmail地址。

**2.通过单点登录进行身份验证**

在GitHub现有的业务模式中，用户需要为集成单点登录（SSO）服务支付额外的费用。但是从代码访问安全的角度，企业应该将GitHub连接到组织的SSO系统中，比如Okta、Azure AD或Google Workspace。开发人员的身份信息应该和企业进行锁定，只允许通过统一的SSO进行身份验证。

**3.所有账户都采用2FA**

在很多企业的SSO提供程序中，会设有豁免组和策略异常处置，这可以使SSO MFA被攻击者轻松绕过。因此，当企业通过SSO执行统一的身份验证时，最安全的选择是对组织中的所有GitHub用户都要强制执行多因素身份验证2FA，防止绕过行为的发生。

**4.使用SSH密钥用于git操作**

虽然GitHub通过个人访问令牌（PAT）引入了细粒度权限控制，但它们仍然容易遭到网络钓鱼的攻击，因为这些令牌常常以明文形式存储。如果使用SSH密钥对git操作进行身份验证，企业需要使用完善的PKI来管理如何配置和提供SSH密钥，还可以将其与企业的设备管理和CA证书有效联系起来。

**5.使用角色限制特权访问**

GitHub目前提供了几种不同的代码库角色，可以基于最小权限原则进行分配。基本权限可以在组织层面加以控制。在实际使用中，管理者需要合理分配保障成员高效工作所需的最小权限角色，尽量避免让开发人员拥有高等级的管理员权限。

**6.严格限制外部合作者使用**

与第三方供应商合作是管理大型软件项目的一个常态。然而，目前GitHub所能提供的外部合作者管理能力存在较大不足，难以确保企业的开发活动安全。因此，需要强制要求外部合作者通过公司的SSO进行身份验证，杜绝代码库管理员直接邀请他们访问代码库的情况发生。

**7.审核，分析，再审核**

没有一家企业的安全控制策略和措施是完美的，即使制定了再好的GitHub应用安全策略，账户也会出现安全疏漏，错误也会在所难免。因此，企业在应用GitHub过程中，要花时间实施定期审计流程，以寻找不安全的休眠账户，并限制代码库中特权角色的数量。一旦企业的GitHub环境被严格保护后，应注意及时发现那些违反策略的情况，比如用户仍然在SSO之外进行身份验证，或者没有使用2FA。

**参考链接：**

https://www.darkreading.com/edge-articles/why-attackers-target-github-and-how-you-can-secure-it

原文来源：安全牛

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

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