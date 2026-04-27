---
title: 赏金猎人笔记：SSRF 受限怎么办？搭上开放重定向接着打
url: https://mp.weixin.qq.com/s/ofc6cYQB3oaqwi5Wwu-MWw
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:06:14.332035
---

# 赏金猎人笔记：SSRF 受限怎么办？搭上开放重定向接着打

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qg1MKHx3jGHd9pgWIibjOeVtoAnjVKU8KzoiazXhuFsQBTD9zvY1BZ7sQ52uu7DIz1mdh8GysLI0HSK4KeZY399lC0EiaDyzOCa8NVbFke4yK0/0?wx_fmt=jpeg)

# 赏金猎人笔记：SSRF 受限怎么办？搭上开放重定向接着打

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

有个挺有意思的漏洞组合，今天拿出来跟你聊聊。

事情是这样的：某个网站有个“检查库存”的功能，看着再普通不过。但你如果仔细抠一抠它的逻辑，能摸出不少门道。

第一步：测一下 SSRF 行不行

点“检查库存”，Burp 抓包，把请求扔进 Repeater。

请求里有个参数叫 stockApi，一看就是后端去查库存的地址。

试着把它改成一个外部地址，看看服务器会不会傻乎乎去请求——结果不行，人家做了限制，只认对应的参数，无法通过构造内部请求进行访问。

到这里，直接打 SSRF 好像没戏。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGHZqCaDf7o0fzt53jdPLP2RGxLDdzXmdlcadbkRSsaeJNOxDbtVlglgAE7buvOiadiaGLAMf7evSSBicfQRvIae0Bbdus4zcggPJg/640?wx_fmt=png&from=appmsg)

第二步：意外发现一个开放重定向

继续逛网站，点“下一个产品”，URL 里出现一个 path 参数。

看响应包，这个 path 的值被原样塞进了 Location 头，用来做页面跳转。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGGcCFjcpuKy1mPProx1v5KHPT93ejgwuJaBLx6J1ApRhHlBO8CicKhwnfEiavMP6Box02PUkkA5h1T5HwNMC5XuEKIuDS2tuPsVU/640?wx_fmt=png&from=appmsg)

这不就是个开放重定向吗？你想让它跳哪，它就跳哪。

第三步：让这两个漏洞“联手”

单独看，一个被限制的 SSRF（无法直接访问内网），一个开放重定向，好像都掀不起什么浪。

但组合起来就有意思了：stockApi 不是只认自家地址吗？那我让它去访问“下一个产品”的链接，再通过 path 参数把最终目的地指向管理后台。

这样一来，服务器检查的是自家域名，放心放行；跳到“下一个产品”之后，又被重定向带到我们真正想去的地方。（这里需要注意的是，需要直接在请求查询的时候进行拼接访问下一个商品的请求，目的就是为了欺骗它，让他认为请求合法。）

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGFzxsGBLibVGg712Q5maMVxiaAy1a03QRCPJRrTHsJRkJLHsedTZG3wRQp6ibRbEwoiaweh5yicR3MjDazHAvMnHoCaTYYx1uoWbC3I/640?wx_fmt=png&from=appmsg)

构造一条这样的链接：

/product/nextProduct?path=http://192.168.0.12:8080/admin

把整条链接喂给 stockApi，发请求。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGHRZ8H4fhP5RDquTrIWNAYh1TnbXmQbLiceGMbOiavtGth9sTFgGKpzeyn6XEIQSnAiaSoVsVWxXY2qm74UB7FtOibMnOy8uMfb65M/640?wx_fmt=png&from=appmsg)

返回结果让人兴奋——库存检查器顺着重定向一路跑过去，管理后台的页面赫然出现在响应里。

第四步：再进一步，动手删用户

既然能碰到管理后台，那就能搞事情了。

把 path 改成删除用户的接口地址：

/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos

再次用 stockApi 发起请求。

服务器照做不误，顺着跳转链摸过去，把 carlos 这个用户给删了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGHW5yicVPxlVRvx37WX40wW91WUI5EBLvQecibxyFhibmOUPq8CzsUEicdkEXWgWrcQsKW4GvuSBGAd6zaFwA5frBIvDBhHFyfyLmA/640?wx_fmt=png&from=appmsg)

整个攻击链其实就四步，核心思路只有一个：当一个漏洞单独用不了的时候，看看能不能给它搭个桥。

实战里这种情况比你想象的多。很多开发者在修 SSRF 的时候，只做了简单的白名单，完全没意识到自己网站里还藏着个能被人当跳板用的重定向功能。

下次挖洞遇到类似的场景，不妨把这个套路翻出来试试。

觉得有用的话，点个关注，后面还会继续分享这种实战小技巧。在挖洞路上碰到什么有意思的案例，评论区随时聊。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

升斗安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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