---
title: 利用时光机所发现的 SSRF
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496642&idx=1&sn=a7dfca57a0a9de7fec1d201d14abe2ca&chksm=e8a5f9a1dfd270b785196b80a6b442587c172c00dcae6cd9cc985423e37e8e1d8f66030beae9&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-12-21
fetch_date: 2025-10-06T19:39:26.962823
---

# 利用时光机所发现的 SSRF

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4xNe7afUgMgDOe8HicyD37gu83a6t8PSDkYFGIIvltOa6pLsIW6DicSMibTSNJHTibQSvzFEjTEE8meg/0?wx_fmt=jpeg)

# 利用时光机所发现的 SSRF

迪哥讲事

编者荐语：

正常流程走一遍以后不要忘了时光机

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

# 前言

wayback machine，这是一个获取隐藏 URL 的伟大工具。通过以下URL即可轻松获取 URL：

https://web.archive.org/cdx/search/cdx?url=\*.redacted.com/\*&output=text&fl=original&collapse=urlkey&filter=statuscode:200

当选择一个网站（例如上面 URL 参数中的 redacted.com）时，我们可以 wayback url 中寻找 API 端点和有价值的参数，如 getImage、 url 、 path 等。

# 漏洞发现

在一次搜索中，白帽小哥发现了一个可以用于生成 PDF 的 API，参数作为 GET 参数进行传递，URL看起来如下；

https://redacted.com/pdf-service?path=/test/testpage

白帽小哥开始尝试读取一些本地文件，但没有发现任何重要内容：

https://redacted.com/pdf-service?path=/../../../../../../../../etc/passwd

然后白帽小哥尝试传递一个URL给这个参数：

https://redacted.com/pdf-service?path=somethinglikethis.com

同样失败，但却收到了这个请求一些内部报错，于是白帽小哥开始尝试一些字符，看能否绕过该验证：

https://redacted.com/pdf-service?path=@google.com

成功！可以在 PDF 中看到谷歌页面。

这是一个 PDF 生成器，它会将页面转换为 PDF。然后白帽小哥用collaborator URL 试了试，发现该服务器部署在 AWS ec2 上。并且可以看到AWS ec2的几个 IP 地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jkjR1FY7JJTqh9WZweqT2JRgCjdw2np9ibsibyrYxuLq8k6Eqje9F5DSpM23CwlqkbBkfib8sBeaOrbQ/640?wx_fmt=png&from=appmsg)

于是白帽小哥开始尝试获取AWS元数据，但却看到的是一个空白的 PDF 页面。

这是因为当服务器无法访问一个域名时，它会返回了一个内部服务器错误。

经过一些尝试后，白帽小哥顺利获得服务器 200 状态响应并返回了 AWS 元数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jkjR1FY7JJTqh9WZweqT2JRgTEhhJvfEQoB38LG5MiayQKm9M14AqbNdBnK4iayd25LsYtz0mCsRGiag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jkjR1FY7JJTqh9WZweqT2JRjjqUBpzibkmSVsSqBMB3NibqVOlAfIQdmow5koCoyLb901N3lzJFTH6A/640?wx_fmt=png&from=appmsg)

其实这时候已经足够报告漏洞了，但白帽小哥对内部网络心生好奇。

因为这是一个生产环境，白帽小哥发现了一些内部域名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jkjR1FY7JJTqh9WZweqT2JRcXbhgPibxZOYonOEH3o8tXYv6ZhCBZxRmcZdWgWVwPz2qZYt9lPKs9A/640?wx_fmt=png&from=appmsg)

于是小哥尝试从 localhost 获取一些端口，并成功得到了 3000 端口，这是 nodejs 端口。

但经过几番尝试后，小哥发现扫描 localhost 会导致拒绝服务，于是小哥不得不停止了扫描，只好乖乖地迅速报告漏洞，静静地等待赏金奖励。

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

以上内容由骨哥翻译并整理。

原文：https://medium.com/@gguzelkokar.mdbf15/from-wayback-machine-to-aws-metadata-uncovering-ssrf-in-a-production-system-within-5-minutes-2d592875c9ab

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