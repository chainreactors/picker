---
title: Rspack和Vant等热门包遭殃！加密货币挖矿软件潜入npm包
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587736&idx=3&sn=ea4b0d410e20154a57137739d7e45299&chksm=b18c22d286fbabc4d80721d0af507a22c86b0b723742eb0b3cb54e655277333cdd6d5f866fa2&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-24
fetch_date: 2025-10-06T19:40:34.004301
---

# Rspack和Vant等热门包遭殃！加密货币挖矿软件潜入npm包

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EficNsfyv6H2XuGwTPCuDQ5H9g8TxAgoAgru7EgXmjnIjMrEuicks3MMGO5rrI0IrmT5nicRsASlkBw/0?wx_fmt=jpeg)

# Rspack和Vant等热门包遭殃！加密货币挖矿软件潜入npm包

看雪学苑

看雪学苑

近日，npm包管理器遭遇了一起严重的供应链攻击，多个热门的npm包被植入了加密挖矿软件，包括Rspack和Vant等。这些包的开发团队已经确认了这一事实，并发布了新的安全版本以修复问题。

Rspack是一个高性能的JavaScript打包工具，最初由字节跳动开发，现已被多家公司采用，包括阿里巴巴、亚马逊、Discord和微软等。然而，其两个npm包@rspack/core和@rspack/cli被黑客攻击，导致这些包中包含了加密货币挖矿恶意软件。这些恶意包已经被发布到官方的npm注册表中，可能会影响到数十万名开发者。

根据安全公司Socket的分析，黑客通过未经授权的npm发布访问权限发布了恶意版本的@rspack/core和@rspack/cli包。这些包中包含了恶意脚本，会向远程服务器发送敏感的配置信息，例如云服务凭据，同时也会收集IP地址和位置信息。这些信息会被发送到"ipinfo[.]io/json"服务器。

值得注意的是，这次攻击仅限于特定国家的机器，包括中国、俄罗斯、香港、白俄罗斯和伊朗。攻击的最终目标是触发XMRig加密货币挖矿软件在受感染的Linux主机上下载和执行。这种恶意软件会通过"package.json"文件中的postinstall脚本自动执行，确保恶意负载在无需任何用户操作的情况下执行。

Rspack的开发团队已经发布了新的包版本，移除了恶意代码，并且已经使所有现有的npm令牌和GitHub令牌失效。他们还检查了仓库和npm包的权限，并对源代码进行了审计，以发现任何潜在的漏洞。目前，正在进行对令牌盗窃的根本原因进行调查。

此外，安全公司Sonatype表示，相同的供应链攻击还针对了另一个npm包Vant，后者每周的下载量超过4.1万。攻击者成功地发布了多个受损版本到npm注册表中，包括2.13.3、2.13.4、2.13.5、3.6.13、3.6.14、3.6.15、4.9.11、4.9.12、4.9.13和4.9.14版本。

Vant的开发团队表示，他们已经发现了其中一个团队成员的npm令牌被盗，并被用于发布多个版本的包，其中包含安全漏洞。他们已经采取措施修复问题，并重新发布了最新版本的包。

这次攻击凸显了包管理器需要采取更严格的安全措施来保护开发者的必要性，例如执行验证检查，以防止更新到未经验证的版本。然而，正如最近的Ultralytics供应链攻击在Python生态系统中所示，攻击者可能仍然能够通过破坏GitHub Actions来发布带有验证的版本。

因此，开发者需要保持警惕，确保他们使用的包是安全的，并且没有包含恶意代码。同时，包管理器和开发团队也需要采取措施来防止这种类型的攻击，例如实施更严格的安全措施和进行定期的安全审计。

在npm包管理器中，开发者可以通过以下方式来保护自己：

* 使用npm的验证功能，确保包的完整性和安全性。
* 定期更新包版本，确保使用最新的安全版本。
* 检查包的依赖关系，确保没有包含恶意代码。
* 使用安全的npm令牌和GitHub令牌，防止未经授权的访问。

总之，npm包管理器的供应链攻击是一个严重的问题，需要开发者、包管理器和开发团队的共同努力来防止和解决。通过采取更严格的安全措施和保持警惕，开发者可以保护自己和自己的项目，避免受到恶意代码的影响。

资讯来源：thehackernews

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

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