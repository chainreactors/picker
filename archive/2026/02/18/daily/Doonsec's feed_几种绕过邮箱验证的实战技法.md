---
title: 几种绕过邮箱验证的实战技法
url: https://mp.weixin.qq.com/s/8hrsgJAygnsF14K04XkI2w
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:16:11.972344
---

# 几种绕过邮箱验证的实战技法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7xtecWUgCRzw57KXoeeYOMLFs9oCRzyynFKoGgHjhvWmqTFPse10ibs1j2qKDgGDf9vP6iau0zesEAZvrA0Uk3gdfZwRzOIKYsdE82ia8mZSAE/0?wx_fmt=jpeg)

# 几种绕过邮箱验证的实战技法

迪哥讲事

![]()

在小说阅读器中沉浸阅读

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

#

在本文中，作者分享了一些在真实世界中，完全**无需工具**即可绕过邮箱验证的独特方法——无需 Burp Suite，无需扫描器，没有任何花哨的技术。 仅需一个浏览器、逻辑思维以及好奇心。

*该文章适合那些喜欢靠思考而不是工具来发现漏洞的研究者。*

### **1️⃣ 通过“禁用注册按钮”绕过 OTP 验证**

所述网站的注册流程如下： 用户输入邮箱地址后，系统会在下一步要求输入 OTP（一次性密码）。 只有在 OTP 验证成功后，**注册按钮**才会变得可点击。

**漏洞发现过程**

1. 作者填写了所有必填的详细信息，如姓名和密码。
2. 输入一个邮箱地址后，应用程序要求进行 OTP 验证。
3. 在此阶段，注册按钮存在，但处于禁用状态。
4. 检查注册按钮后，作者发现其属性为 `disabled=true`。
5. 随后移除了按钮上的 `disabled` 属性。
6. 注册按钮立即变为可点击状态。
7. 点击后，账户在**未验证 OTP 的情况下**被成功创建。

![file](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhn57MM24Bx8FXG4jMib8ENjgv5a2PaOQMEv2cSnrXvhfSkGPmGWxPFrhMdl9ibb9hS8hqQYwPg9Pxxp2lDZ0o0cVOfh7dDsY0eE/640?wx_fmt=png&from=appmsg)

由于作者已无法访问其账户，因此无法确认该漏洞是否已被修复。

### **2️⃣ 通过“招聘方注册流程”绕过邮箱验证**

作者最初将此问题提交为**低危**，但经过评估影响范围后，目标方将其升级为**高危**。***该应用具有两种不同的注册流程：***

* **学生注册** – 工作流程正常，在账户创建前强制执行邮箱验证。
* **招聘方注册** – 首先要求提供邮箱和密码，然后将用户重定向到订阅/支付页面。

**漏洞原理**

1. 使用招聘方注册页面，通过输入邮箱和密码创建了一个账户。
2. 提交详细信息后，应用程序将用户重定向到付款/订阅页面。
3. **没有完成支付**，直接离开了该页面。
4. 接着，访问了**学生登录页面**（而非注册页面）。
5. 使用在招聘方页面创建的同一组凭据进行登录。
6. **登录成功**，没有任何邮箱验证。

![file](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgT4223icRh2ibEt9WEkjYSqGQbiaIiaoaXncb8rpWKJPOWI0k0ibPVAbpSThZzOCkiaIvX3HUwkLRG7frXcPuY5wMBxQhEfGtFLAmGI/640?wx_fmt=png&from=appmsg)

该漏洞已被成功修复，作者也获得了相应的赏金。

### **3️⃣ 通过“编辑个人资料”来绕过邮箱变更验证**

此问题涉及**修改账户邮箱**时的漏洞，与注册无关。 应用程序在“编辑个人资料”页面内提供了“更改邮箱”功能。

**预期行为**

* 用户点击“更改邮箱”。
* OTP 被发送到当前邮箱地址。
* OTP 验证成功后，邮箱地址被更新。*此邮箱变更功能是整个“编辑个人资料”页面中的一个模块。*

（点击回车或点击查看完整尺寸图片）

![file](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZial6tUEbvjiatwtz18Zl71pONApKTu4s6w9joibRzgyKOGps8nQpbddJDDDhenDSGIVZThENVQztsGeRGec9HSfoFWyVcIibpbAos/640?wx_fmt=png&from=appmsg)

作者没有保存赏金截图，但确认漏洞已修复，并收到了赏金。

**漏洞原理**

1. 导航到“编辑个人资料”页面中的“更改邮箱”部分。
2. 邮箱输入字段显示为只读。
3. 检查该邮箱输入字段后，移除了 `readonly` 属性。
4. 直接修改了邮箱地址（**没有点击“更改邮箱”按钮**）。
5. 没有使用专门用于邮箱的按钮，而是点击了**保存个人资料**按钮（用于保存整个个人资料）。
6. 个人资料成功保存，邮箱地址在**没有任何 OTP 验证**的情况下被更新。

### **4️⃣ 通过“次要邮箱升级”来绕过邮箱验证**

该方法思路较为独特。 该网站允许用户创建账户并立即登录，但除非邮箱地址通过验证，否则个人资料会标记为**未验证**。

**漏洞原理**

1. 使用他人的邮箱地址创建了一个账户，**没有进行验证**。
2. 登录该账户，并导航至“账户设置”。
3. 发现其中有一个“添加次要邮箱地址”的选项。
4. 添加了一个可控并能验证的邮箱地址作为次要邮箱，并完成了验证。
5. 验证之后，应用程序允许将**次要邮箱标记为主要邮箱**。
6. 执行此操作后，出现了意外情况：***最初用于注册的那个邮箱地址（即他人的邮箱），现在自动被标记为已验证。***

![file](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhEQRtGG7ploZNUeKNzJKpncbn4kvxOib80cAG0SKH28icAUicZg2vvqSD3Bffll6iaOb9mEpmlvL8R0c1EicTYoV2nZLUWqx6NKGl8/640?wx_fmt=png&from=appmsg)

如果你是一个长期主义者，欢迎加入我的知识星球，本星球日日更新,包含号主大量一线实战,全网独一无二，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

往期回顾

#

# [如何利用ai辅助挖漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497813&idx=1&sn=c778ad6a4bffd7a0a72a900144ea90ca&scene=21#wechat_redirect)

#

# [如何在移动端抓包-下](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497880&idx=1&sn=b9b980464333074216b55ea94c8a743a&scene=21#wechat_redirect)

#

# [如何绕过签名校验](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497491&idx=1&sn=a1b00b9a8a54eb96aa3ba8bf23cb7e28&scene=21#wechat_redirect)

#

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)[‍](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

作者未收到目标方的回复。

原文：https://infosecwriteups.com/5-ways-to-bypass-email-verification-without-using-any-tool-87bfbe7fc156

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