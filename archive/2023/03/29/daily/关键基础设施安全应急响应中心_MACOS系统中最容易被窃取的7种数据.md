---
title: MACOS系统中最容易被窃取的7种数据
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247535633&idx=4&sn=5278568075e811c43a42b171be871243&chksm=c1e9c040f69e4956f2769b223b18cc594f6ce5fe8dc51f022ad96f756b10658b474f7d7e7a7c&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-03-29
fetch_date: 2025-10-04T11:02:12.895253
---

# MACOS系统中最容易被窃取的7种数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguCibStIQ7lF1r1FAuUglG1q4EyHiawHeiaJAnJbiaedazmGftFnamdic8ialBXUicHrGWSGUwCcM430Agtg/0?wx_fmt=jpeg)

# MACOS系统中最容易被窃取的7种数据

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguCibStIQ7lF1r1FAuUglG1q2twbUJQFMaiaEHoxFrFZSCt6jdtIzqb5GVlvibwZpaaOz6TU7wqiaHPhg/640?wx_fmt=jpeg)

一直以来，macOS系统的最大特点之一就是较少受到恶意软件的困扰。研究数据显示：在过去5年中，严重困扰Windows终端用户的勒索软件攻击并未在Mac设备上大量重现，锁定Mac设备或数据并向其所有者勒索赎金的攻击模式目前还难以实现。

然而，窃取有价值的数据并以恶意的方式将其货币化，这种攻击策略在各个操作系统上都很常见。在macOS系统上，非法攻击者也同样在窃取会话cookie、Keychain（密钥串）、SSH密钥等信息，并通过广告软件或间谍软件等恶意进程违规收集数据。这些数据可以在各种地下论坛和暗网市场中销售，或者直接应用于各种网络攻击活动。

本文梳理总结了macOS系统中最容易被窃取的7种数据资产类型，以帮助安全运营人员更好地保护企业，并识别潜在的风险迹象。

**01、会话cookie数据**

macOS恶意软件的最常见攻击目标就是存储在用户设备上的会话cookie。为了方便和提高用户的使用效率，macOS系统上的浏览器和许多企业级应用程序通常都会允许用户保持登录状态，直到他们明确退出。这是通过在设备上存储会话cookie来实现的。如果攻击者窃取了这些cookie，他们就可以在不同的MAC设备上使用这些cookie来登录，而无需身份验证。

在近期发生的CircleCI入侵事件中，Mac电脑的会话cookie就被违规窃取。根据CirlceCI的公开声明显示：“我们已经了解到，一个未经授权的第三方利用部署到CircleCI工程师笔记本电脑上的恶意软件，窃取了一个有效的SSO会话。该设备于2022年12月16日被入侵。现有的杀毒软件没有检测到恶意软件。调查表明，该恶意软件能够执行会话cookie盗窃，并在远程位置模拟目标员工，然后实现对公司业务系统的访问。”

在macOS系统中，会话cookie通常位于用户或进程可以访问的位置，尽管这些位置（例如用户库cookie文件夹）通常会受到“透明、同意和控制”（TCC）框架的限制，但是研究人员发现，TCC虽然对正常使用者来说是一种管控措施，但对攻击活动来说很难构成有效的限制。

以下是在macOS上存储会话cookie的位置的一些常见示例：

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkD88DoQCmecQvLROL1rNStyIHDPArXrEMK9tF9Tvr7bsI62wpUiaRSTCUhpaSBDQXsWd1Eyt6cb8GA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

此外，与应用系统相关的数据库也是犯罪分子的攻击目标。弱加密的数据库可以通过一些用户密码知识就能轻松解密，且通常被恶意软件安装程序在最初的攻击中获取到。例如，Zoom的加密数据库就是Pureland infostealer的目标。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD88DoQCmecQvLROL1rNSty966u5CDpJdLVGTgELhNrKGU8AgAmFp9Acf3vBGjQIaA9KxlW7oB7aQ/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

【pureland Infostealer搜索Zoom加密数据库】

**02、用户的密码管理文件**

在用户的Mac电脑上，最重要的数据可能是用户的密钥管理文件，这是一个用于存储密码、身份验证令牌和加密密钥的加密数据库。密钥管理文件使用了强大的加密技术，不能简单地通过窃取数据库甚至访问计算机来破解。然而，密钥管理文件的弱点是，如果攻击者掌握了用户的登录密码，其中存储的隐私信息就可以全部被解锁。如果该密码很弱，很容易被猜到，或者由于使用者的疏忽而错误提供给恶意进程，那么密钥管理文件的加密强度将完全起不到作用。

研究数据显示，密钥管理文件已经成为非法攻击者的目标。最近的例子包括DazzleSpy和一种被称为“KeySteal”的威胁，这种威胁最初是由趋势科技的研究人员于2022年11月份发现。苹果公司在今年3月发布的XProtect v2166和XProtectRemediator中才添加了KeySteal检测功能。

KeySteal的目标文件与.keychain和keychain-db文件扩展名存在以下位置：

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkD88DoQCmecQvLROL1rNSty0Ao33xJKRmNapficmSlQbOibBxAYL0XPfOavftdTvZ5lKJk9Vibaib4OOA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD88DoQCmecQvLROL1rNSty8V40G3qicWY29qbJTlYnvlzI1YiahYiaJqvZBibh64O0f86pqSnvia8TQTA/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

【枚举macOS密钥管理文件的恶意函数】

当密钥管理文件被查询后，就会被base64编码，并通过名为JKEncrypt的开源中文加密库进行加密，JKEncrypt是一种“自制”加密函数，使用传统的3DES算法。

**03、用户登录密码信息**

如上所述，用户的密钥管理文件对未经授权的一方用处不大，除非他们也拥有登录用户的密码，而且由于登录密码对于Mac设备上的几乎所有操作都是必要的身份验证，因此它们受到恶意攻击者的高度追捧。

用户登录密码窃取可以通过多种方式实现：通过欺骗、通过键盘记录或者一些简单的任务请求授权，然后将该授权用于非法的攻击活动。恶意软件通常会要求受害者提升权

限，这样它就可以安装一个特权可执行文件，随后以高级用户身份来运行，完成攻击者想要完成的各种任务。CloudMensis/BadRAT间谍软件就是一个很好的例子。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD88DoQCmecQvLROL1rNStyJBXRSoh6VnGuRtqbTrIHZtiahib8rFiaCjAJqzsgrictT9DmibVxUTpLrHg/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

【CloudMensis/BadRAT会向用户发出权限升级的请求】

**04、浏览器中的密码及相关数据**

许多macOS用户会利用浏览器来存储网站登录凭据和密码，以及其他有用的数据，如用户填写的登录凭证、浏览器历史、搜索历史和下载历史，这也是非法攻击者非常感兴趣的信息。

以Pureland infostealer的恶意攻击活动为例，Pureland执行以下命令作为getChromeSSPass函数的一部分：

security 2>&1 > /dev/null find-generic-password -ga 'Chrome' | awk '{print $2}' > /Users/

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD88DoQCmecQvLROL1rNStyiad8u8p9TGbqYe7na6jaLhjjf5C2CqV61tJwb9MiaIt7WAH5XqtfYNGQ/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

【Pureland Infostealer上与Chrome数据盗窃相关的字符串】

不过，该恶意进程需要具备更高的权限，并绕过通常的TCC控制才能成功，否则用户将会收到有关该尝试的安全警告。

**05、SSH密钥信息**

攻击者一旦拥有macOS用户的SSH密钥，就可以在受害者的系统上验证自己的身份。SSH文件夹还会允许攻击者访问同一系统上的其他帐户或同一网络上的其他系统配置文件。除了窃取SSH密钥之外，如果攻击者能够获得SSH文件夹的读写访问权，他们还可以通过分发自己的授权密钥以实现后门远程访问。

2022年5月，macOS Rust开发人员就沦为了CrateDepression SSH密钥窃取攻击的目标，本次攻击活动影响了在其MAC设备上设置了GITLAB\_CI环境变量的用户，这也表明攻击者对用于软件开发的持续集成（CI）管道感兴趣。一旦攻击成功入侵主机设备，就会触发Poseidon有效载荷，其中包括搜索和窃取SSH密钥。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD88DoQCmecQvLROL1rNStyLVibVia4Vrr3FqdoZkCdibgxZyG7tjkglDDWRrUFdOjtzEwllopciaVsbw/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

【Poseidon代理搜索妥协设备上的SSH和AWS密钥】

同样值得注意的是，除了硬编码SSH数据盗窃的恶意软件外，任何能够将文件上传到远程服务器的后门RAT都可以搜索SSH密钥。

**06、macOS系统环境信息**

许多macOS恶意软件的一个常见行为是从设备中查询和窃取各种环境信息数据。出于各种原因，这可以用于伪造设备的特征指纹，包括选择性地发送恶意软件和执行恶意软件。例如，C2可以自动交付特定平台、特定版本的恶意软件。类似地，威胁行为者还可能会向各种受害者分发特定的（其环境与攻击者的兴趣相匹配）攻击载荷。

如果攻击者对目标环境有深入了解，则可以创建针对该信息的散列，仅在受感染设备的信息匹配时才执行。这种有选择性的传递和执行，可以使得攻击者更高效的实施攻击活动，同时更难以被发现。DazzleSpy就是这种恶意攻击的一个真实事例，该恶意软件会轮询（poll）其环境以获取大量的环境数据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD88DoQCmecQvLROL1rNSty3qRTCcR7km3JEWf1qvSq0jYc5Mh2FibPnTOXIfxutcKibTPPiar9DgInQ/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

【DazzleSpy非常详细地监视它的主机环境】

**07、粘贴板中的内容信息**

当用户通过快捷键“Cmd-C”执行复制功能时，粘贴板或剪贴板就会在内存中存储文本、图像和其他数据。

对于恶意软件开发者来说，粘贴板很有吸引力，因为它是密码、加密货币地址和其他数据窃取的有效途径。例如，一些加密货币窃贼会监视用户将钱包地址复制到粘贴板上，然后将其替换为属于攻击者的地址。

获取并写入粘贴板相对容易，因为苹果提供了Foundation框架NSPasteboard api，以及Unix命令行实用程序pbcopy和pbpaste。

EggShell RAT就是一个很好的例子。这个自定义版本被用于XcodeSpy恶意软件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkD88DoQCmecQvLROL1rNStyDabA68HGXxQRqE6kMaJen0hX9L0pZSszbhyJYjTGs6d3yld2Wkic85Q/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

【getPasteBoard函数被用于XcodeSpy恶意软件】

**防护建议**

随着Mac电脑设备在企业生产和开发团队中越来越受欢迎，存储在Mac电脑上的数据对攻击者来说正变得越来越重要。企业要缓解各种类型的数据窃取攻击，首先需要部署一个完善的端点安全解决方案，它既可以快速识别并阻止恶意软件，也可以让安全团队看到设备上正在发生的事情。

此外，安全运营人员还应该定期监控试图访问密钥链、SSH和上面讨论的其他文件路径的进程。

最后，尽管macOS系统的TCC机制还有很多不完善的地方，但保持macOS系统的及时更新仍然至关重要，因为苹果公司会定期升级TCC框架，并修补研究人员报告的其他安全漏洞，降低MAC设备的使用风险。

原文来源：安全牛

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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