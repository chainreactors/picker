---
title: 0day 挖到手软，403 到 getshell
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496966&idx=1&sn=c49dbe1213cb5a1afa836901e2c13038&chksm=e8a5ff65dfd27673a9c0d7fdd99094847b291a7b8434f16f408af60943322f7ba539d1f82082&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-01-29
fetch_date: 2025-10-06T20:09:19.677673
---

# 0day 挖到手软，403 到 getshell

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj5aqVYXkhyGibkibQsv9O8cwaad53P6NicfpfXvFqfmBlfuApbSUxPYBoYOdsl7o4KdbTn8zr5IM0L1Q/0?wx_fmt=jpeg)

# 0day 挖到手软，403 到 getshell

迪哥讲事

以下文章来源于轩公子谈技术
，作者private null

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5l1taOtPMfDOorccicaGasHAgDQu6DcYBmVHoicZs202vg/0)

**轩公子谈技术**
.

从0到1，五年翻身之路，安全笔记分享 擅长渗透测试，应急响应，内网渗透，代码审计。

开局 403

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2msvOC4yctXm8iccVlCSHUiaKCAkavWejPOcl5DNDSe1F3FXjxlN2NyYA/640?wx_fmt=png)

于是，开启目录扫描工作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt24OebmicXG2m2YLS7WCiaqAsDEHGiajiae01aeBeymWhcTnZYacMNpNyb5w/640?wx_fmt=png)

log.txt 文件泄露了日志内容，其中皆是报错信息，并且能够看到绝对路径。

test.html 疑似为前台静态页面，登录时无反应。

而 business 打开后会出现一个网站，在该网站上既可以登录，也能够进行注册。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt25icAFPyqiaKf3ermfmTTzxQfudUyDGe1IAoQmkNE5LSZaJyhobT3bjwg/640?wx_fmt=png)

首先，查看登录页面，进行抓包操作，以检测是否存在注入漏洞。然而，很明显该页面不存在注入漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2owKTw3LOiab3HpWqb1brHXGVBswYsSB7m8nSsxmBdmyS3dXKElCaWkA/640?wx_fmt=png)

登录绕过

随意输入账号和密码后，修改返回包，将原本的 “f” 改为 “t”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2vb3pY0AUXZicJppibnAmr2azDYfVvJz6EymM2R3E2vEoCV2dgFLWk6Nw/640?wx_fmt=png)

抱着试一试的心态进行上述操作后，没想到竟然进入了后台。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt271nAoQ4ryWULRBjLvZ2sgk37oDsyVib7ASFPOxVFJQXEaynsic4NJhSQ/640?wx_fmt=png)

短信并发

使用并发插件进行测试，原本想着会发出一堆验证码，结果却发现同一个验证码发送了两次，算是捡到了一个小漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2x69BuG7cSVtf97yxeAAaYQ5E4MibIcoTO6P7UZyXdeGJLnpzGkwe7pg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2Aic4wiaTibr1xzWjsyqnsa15zjvUAwgRU3X2UYTJpAfFwZwialeOJeqibFQ/640?wx_fmt=png)

接着查看源代码，发现了 ueditor 的特征。通过拼接路径，成功打开了默认页面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2nql0nhPG0LSsEU7PKrq3vwl59vYh2RCia9MIFOEvKpmrReiaaCniaSd1w/640?wx_fmt=png)

进行上传图片操作时，反应十分缓慢。抓包查看后发现后端接口访问失败，导致图片无法上传。于是尝试进行 XSS测试，权当是碰运气。

短信篡改

在发送短信的时候，发现有一个 “msg” 参数，其内容虽然经过加密，但总让人感觉有些奇怪，疑似是验证码。于是选中该参数，让 Burp Suite 进行识别。果不其然，这妥妥的就是验证码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2F7F3v3JFMVQoYKat9NL6rLDcib7x6RWkPZ9QC4oP3QPYYgKibBVwzRWA/640?wx_fmt=png)

那么，是否能够改变其内容呢

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2SFXdrdGGYWFrj0Eoibd43AJODuYFHl5Dz6eCOsUsibFY9ibe5Gp8IfiaiaQ/640?wx_fmt=png)

6666666

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt294xcBsiazc8mGYcR9J6JEZkCG5VtUS1iagVz0RhXyS56ibWJvo5flsDeA/640?wx_fmt=png)

SQL 注入

使用熊猫头，看到有很多接口地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2q2MakofZdXoue1hSTicNlXN4Yld6Ld8eicelQibjRLUtsU0Cr5j8EuQZg/640?wx_fmt=png)

接着进行拼接测试，大致查看一遍后发现都是查询接口，不存在删除接口。

于是使用 Burp Suite 对这些接口进行测试。

大部分接口都可以访问数据，但参数是空白的，要么返回 0，要么返回 1。

随机选中一个，进行单引号输入测试时，出现了报错。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2sGvfoaq2ghUZ7HZ7JIUYVf99MkciasDWDX3qELy1osbuH6LtoqFMlrQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2X4XeYkIHhBrgXRNE8yAYOuhe9nEq34xbDcVWZGFMBOT3kwsPLo2XEw/640?wx_fmt=png)

直接使用 sqlmap，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2mhrtdROI4iaT69gic3Q5Q57wC0DgLPEeZHafKImH2ueSsq2H0AVVZXtw/640?wx_fmt=png)

多个接口，x 多个漏洞。

未授权访问

然后再次扫描 api 目录，发现了 swagger

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2QWjV2VpGH0t7cKicVdPa4cP7SdnVuvPopMV8wMU7VruGmSKiabr61knQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2j0tp7rltoSEV0wu3ibDcFHTWb8JJialGibMj77zgprjAdofFicDwREvibpg/640?wx_fmt=png)

其中有一个上传接口，访问 405，吆，有戏

文件上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2icYpFHDCGiasOcr3NcgvLIibLlhQTDDPoT8oEtAahl5d6PTfLky6iccIdw/640?wx_fmt=png)

aspx 后缀未拦截

一句话木马直接 getshell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2z4lOAgDHfRG4gImNXL3pFSBVAclQw7O5PL8GBcHvRbyYDibow6TZNAg/640?wx_fmt=png)

最终获得以下漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt2NQiasRhrsGhg4wW1ibyXDceY7CzZlibDNS7BIdPiaEGOcUKXoDF15ic1oYA/640?wx_fmt=png)

然后看了一下供应链，才 3kw 的注册资金，没得证书，G了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQZHGd0IqGcCrDK1OKCq1Nt256gfyVxH4xF315jgAu9QdBF8UEiaQ3upEfqx5sY9ibS6EVr1icGOkkOVA/640?wx_fmt=png)

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