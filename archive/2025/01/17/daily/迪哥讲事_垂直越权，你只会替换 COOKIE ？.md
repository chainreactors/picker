---
title: 垂直越权，你只会替换 COOKIE ？
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496878&idx=1&sn=da95b7064e7bdbbf53ae06a6b9df0f66&chksm=e8a5fecddfd277db713446ce20375d8d5ba31517f0fae716a2a6b9433fe0fcf2a8a56428ca89&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-01-17
fetch_date: 2025-10-06T20:11:45.698061
---

# 垂直越权，你只会替换 COOKIE ？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4r18JzhT7QaaPhJ3cS5pyF6dhXtAyy3LJgVdbic6GtxRlIdZmib0nThBTjUT309sYfx51JQt85yicWg/0?wx_fmt=jpeg)

# 垂直越权，你只会替换 COOKIE ？

迪哥讲事

以下文章来源于轩公子谈技术
，作者阿杰谈技术

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5l1taOtPMfDOorccicaGasHAgDQu6DcYBmVHoicZs202vg/0)

**轩公子谈技术**
.

从0到1，五年翻身之路，安全笔记分享 擅长渗透测试，应急响应，内网渗透，代码审计。

在 Web 安全领域，越权访问漏洞主要分为垂直越权和水平越权两种类型。本文将着重探讨垂直越权测试的思路与方法 。

早期在学习小迪的相关视频时，我了解到一种垂直越权的测试方式：通过替换高权限账号与低权限账号的 cookie，来尝试实现越权访问。这种方法在特定场景下有一定的可行性。

然而，在实际工作环境中，这种基于 cookie 替换的测试面临诸多挑战。一方面，测试人员往往很难获取到足够的测试账号，有时甚至仅能得到一个管理员账号。

若要通过添加用户功能来配置一个低权限小号用于测试越权，整个流程不仅繁琐，而且耗费精力，使得 cookie 替换的操作变得极为不便。

另一方面，即便系统允许用户自行注册，但注册用户所能使用的功能通常极为有限，在这种情况下，传统的 cookie 替换方式难以发挥作用。

那么，面对这些实际问题，我们该如何有效地进行垂直越权测试呢？

接下来，本文将围绕垂直越权的多种实用思路展开深入分析。

### 如何挖掘垂直越权呢

个人观点有两大种，四小种。

#### **基于用户角色的测试思路**

具体来说，就是将低权限账号的 cookie 替换后，用于访问原本仅限高权限账号使用的接口。

以`/api/system/user/list`接口为例，该接口的作用是列举用户列表。在正常的权限设定下，这类接口只有管理员才有访问权限。普通用户登录系统后，由于系统权限控制，其操作界面不会出现用户管理相关功能入口，也就无法直接访问用户列表接口。

在进行越权测试时，我们把普通账号的 cookie 进行替换，然后用替换后的 cookie 去访问`/api/system/user/list`接口，并发送请求数据包。若此时能够成功查询到用户列表数据，那就表明系统存在垂直越权漏洞，即低权限用户可通过不正当手段访问到高权限用户才能访问的资源。

#### **基于功能接口测试思路**

在进行系统安全测试时，有一个重要的环节是针对接口的越权测试。具体操作流程是，在登录系统前后，分别提取相应的接口信息，并将这些接口汇总起来进行统一测试。

实际测试中，若面临没有测试账号的情况，主动向相关负责人申请账号是必要的途径，毕竟不主动申请，账号不会自动提供。

要是系统允许用户自行注册，且注册流程无需经过审核，注册完成即可直接登录，那么注册后就可以着手提取接口。

提取接口数据后，借助 Burp Suite 等专业工具对这些接口进行遍历测试。在遍历过程中，重点关注接口返回的内容，将其与登录后正常访问所获取的数据进行对比。

在遍历测试之前，建议先全面浏览后台的各个功能点，查看其中是否存在数据，以及这些数据是否涉及敏感信息。这样做的好处在于，当工具遍历跑出来数据后，能够更高效地判断，而无需对每一条数据都进行逐一细致对比，便能快速确定是否是由于越权问题导致的数据异常情况，从而大大提升测试效率和准确性。

基于 web 页面的越权

还有一种方式，也是基于接口，但是是针对 web 页面的越权，属于功能接口的分支。

比如登录后的 url 为

http://www.test.com/demo/#/home

http://www.test.com/demo/home

这两种，第一种大多数是vue框架

在进行系统安全测试时，我们首先利用熊猫头工具来获取接口信息。获取到接口信息后，有多种方式进行后续的访问遍历测试。一方面，可以通过编写 Python 脚本对获取的接口进行拼接访问；另一方面，也可以借助 Burp Suite 工具来完成接口的拼接访问操作。

例如，我们可能会将基础网址`http://www.test.com/demo/#/`与不同的功能路径，如`main`、`system`、`list`等进行拼接，形成类似`http://www.test.com/demo/#/main` 、`http://www.test.com/demo/#/system` 、`http://www.test.com/demo/#/list`这样的访问链接。通过这种拼接访问的方式，运气好的话，有可能直接访问到原本受限的其他功能页面。

不过需要注意的是，并非所有基于 Vue 框架开发的系统都会存在此类越权访问漏洞。

系统是否存在漏洞，关键取决于业务系统权限的设置方式。

在实际情况中，可能出现多种结果：整个系统可能一个越权漏洞都不存在；也有可能在众多接口中，仅有一两个存在越权情况；甚至存在所有接口都存在越权漏洞的可能性。

另外，在访问过程中，还可能会遇到这样的现象：访问后虽然能打开新的页面，但在点击页面功能进行抓包时，发现返回的是错误信息（如 error 提示）或者 403 禁止访问状态码等。

这些情况在测试过程中都是较为常见的。所以，最终能否发现越权漏洞，在一定程度上存在不确定性 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQYru6KMWMHt0Ol9hib4ZaWoNWJSjp9F6Kfn85kRQ9YFBrC7n0GEnwlvZ1J6deQvy9kYB0S06IWFuzw/640?wx_fmt=png&from=appmsg)

另一种情况是针对非 Vue 框架的系统。在这种情况下，可采用直接拼接路径的方法，如`http://www.test.com/demo/home`、`http://www.test.com/demo/list`、`http://www.test.com/demo/system`等。这些路径的收集工作同样借助熊猫头工具来完成，收集之后再按照前面提到的利用 Python 脚本或 Burp Suite 等方式进行后续的测试操作，以检测是否存在潜在的安全漏洞或越权访问等问题。

下面就看一下实际案例：

这是我注册的账号，发现就这几个点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQYru6KMWMHt0Ol9hib4ZaWoNy2mvRhAshPicFxjO2EIomtztyp33YFI3QDTaFoWLnW3Bib8gx4oYEu8A/640?wx_fmt=png&from=appmsg)

然后就获取接口，然后发现我自己可以获取到人员机构，并且能够添加成员，赋予登录权限后，就直接登录进来了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQYru6KMWMHt0Ol9hib4ZaWoNuBJjqwBVJNy37gyubw0Ty1uNmyplH0N9sJOmVbazsTr6iabTIrBQCNQ/640?wx_fmt=png&from=appmsg)

下面这个也是注册用户进来的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQYru6KMWMHt0Ol9hib4ZaWoNEF8G7JHjcgQCVXJygWn2R7IvoGjIhic4YwRicF8K3ZfGySBK9CcPnmSQ/640?wx_fmt=png&from=appmsg)

基本上就五个功能点，然后通过熊猫头提取接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQYru6KMWMHt0Ol9hib4ZaWoNCoc3jwnd0OCO4Slgm4UZgcd8AqZ5URSxrGMia8I1MyYpK6Biav6M77bA/640?wx_fmt=png&from=appmsg)

直接拼接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQYru6KMWMHt0Ol9hib4ZaWoNdIRFH95jmSMFPcMdGtliauq8kxIKRYY8dbJhnDJf81sUvcxxVGbf65w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BAby4Fk1HQYru6KMWMHt0Ol9hib4ZaWoNCEgv9qbUzXovSMbaAZ3Y3gcDETxeuZ7O2XadV3p2k21mIVvNPeMejA/640?wx_fmt=png&from=appmsg)

就发现了很多敏感信息。

基于目录扫描的越权

在安全测试中，还有一种测试思路值得关注。最后一种是在登录系统之后，通过配置 cookie 的方式，对网站进行全面的目录扫描。在此过程中，可使用预先准备好的字典进行匹配，以发现一些潜在的安全隐患。

例如，在进行目录扫描时，可能会发现一些敏感页面，如`passwd.html`页面。当打开该页面后，可能会出现严重的安全问题，比如无需额外验证就能修改管理员账号密码，这种情况会给系统带来极大的安全风险。

另外，还有一种相对较少见的情况。

有些网站在访问登录地址时，会先跳转到后台页面，然后再跳转至登录页面。

针对这种情况，我们可以持续进行抓包操作，等待浏览器完全到达后台页面。在该页面上点击不同的功能点，并适时放包，直到 Burp 工具中出现相关的接口信息。然后，利用这些接口信息开展测试工作。

在实际测试过程中，我仅遇到过一次这样的情况，在这个案例中，该网站可以进行文件上传、信息查询等操作。

不过，从严格意义上讲，这种情况更倾向于属于未授权访问的范畴，其涉及的安全问题需要我们引起足够的重视，因为它会使未登录用户获取到本不应有的权限，可能导致信息泄露、数据篡改等一系列严重后果。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

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