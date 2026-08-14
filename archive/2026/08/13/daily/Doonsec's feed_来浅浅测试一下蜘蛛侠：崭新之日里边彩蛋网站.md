---
title: 来浅浅测试一下蜘蛛侠：崭新之日里边彩蛋网站
url: https://mp.weixin.qq.com/s/mkoo0q1eDsaVFd5Bk1w5uQ
source: Doonsec's feed
date: 2026-08-13
fetch_date: 2026-08-14T03:58:54.249429
---

# 来浅浅测试一下蜘蛛侠：崭新之日里边彩蛋网站

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8swOkKrLpPeZeNicVZPQRRpYq90Vp37ZIbrux4OHI9t9iaP5klggSIAyR7Diccic49LAcHcwVrUuLN8VIHnOKsiaehIEOJargiboSvf5H6ca9FkyU/0?wx_fmt=jpeg)

# 来浅浅测试一下蜘蛛侠：崭新之日里边彩蛋网站

GG安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于蜉蝣安全实验室
，作者蜉蝣信安

![](https://wx.qlogo.cn/mmhead/K6CEv0Hv9DccOEOfvbIWl4eHK8LUoV7wd1OKwP8k21mVN73bSIlOWX7VkgAjX4nGEwZqhqDEQd8/0)

**蜉蝣安全实验室**
.

红蓝对抗，Web渗透测试，红队攻击，蓝队防守，内网渗透，漏洞分析，漏洞原理，开源工具，社工钓鱼，应急响应，网络安全。个人的部分知识技能，倾向于使用知识库和文章的方式进行总结回顾自己，我学多少我就分享多少

#

![](https://mmbiz.qpic.cn/mmbiz_png/8swOkKrLpPd5KgQrLd5g7GiaKT4r51NjymxQWDdWxFAiaDtdn6X7Sn9mibz2Nibq7bva8wB9ibPoanzhib6Kc2xsUicEDh9XHTb3v0vLDukLaCtY0Y/640?wx_fmt=png&from=appmsg)

---

## THE LAST TIME

看完电影等半天结果是一个网站彩蛋这你受得了？

那咱们作为一个网络安全人员（嗨壳O(∩\_∩)O）必须得上手干他一下啊呀哈哈哈哈

《蜘蛛侠：崭新之日》相关的一个彩蛋网站：https://spideytracker.net/intl/uk/

第一眼看上去就是一个像素风互动页面，点点按钮、看看地图、追一下蜘蛛侠彩蛋。

但作为一个网安人，看到这种站我脑子里第一反应一般不是“好玩”。

而是：

**这个站背后到底挂了哪些资产？**

事先声明：就是娱乐渗透，大家看一乐乎就行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8swOkKrLpPfhz6XFgoVmGPoaxTFlwbib9DnsicYmnOicyHRfObd9m9M2YwicRKtSRiacMjTPFPE1dXdNDPibHibmddwFwaia9MIvXJcBiaJCD9cskVcQ/640?wx_fmt=png&from=appmsg)

【👆：本次测试流程】

先说结论这个站整体暴露面不算复杂。

主站是一个前端资源比较重的互动页面，边缘侧熊猫头以及wappalyzer插件就能看到 **Akamai + Apache + UltraDNS** 等等页面的构成

![](https://mmbiz.qpic.cn/mmbiz_png/8swOkKrLpPe10Aibv8oCSHibXVuHuTaVMyeTKcsLyiavEvtTBBzQIfzG8Z5Ec3QvCFibaNLbWicE4wMvrricslWzue5LNzckb6bsSOINXgAxw8jGU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8swOkKrLpPckvYQD5UU7bSAR8JOs6AF84AjI9pVmN1m34Sc83sqyPGYpRQ0ZYvWpYd8o5YF5ibW0l0v4WVtgVwibWGY48mialPFWiaxODRwqtrM/640?wx_fmt=png&from=appmsg)

源码里能看到 Astro 构建痕迹、New Relic、OneTrust、GTM、Google Maps、CloudFront、Sony Pictures 相关外链。

常见敏感路径没有直接读到东西。

`.git/HEAD`、`.env`、`.DS_Store` 这类路径返回 403 或 404，`/admin/`、`/debug/`、`/backup.zip` 会跳到 404。

比较值得继续关注的是两点：

**第一，公开数据里能看到 stage 子域名。**

**第二，前端里能看到 Google Maps API key 调用，需要确认 Referer 限制。**

**这里可以说是摸到资产边界了。**

目标页面长这样

先看目标本身。

页面是一个像素风的 Spidey Tracker，看起来确实挺像电影宣发彩蛋页。

我先把 Cookie 弹窗处理掉，然后截了一张比较干净的页面图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8swOkKrLpPc6MiabCR1K1OPMAwzDMtfmiavmGgAiaMEyvI4BDx4JricT1kkI7hK5cV3icmse8nQiceOgWBtbvUKM7n9u3MlDszgDew0LGjNllVOz8/640?wx_fmt=png&from=appmsg)

【👆：Spidey Tracker 目标页面】

这个页面本身没有明显输入框，也没有很传统的登录、搜索、上传这种入口。

所以测试思路不能一上来就奔着 SQL 注入、任意文件上传那种方向去。

这种站更适合先从外围看：

域名怎么解析？

有没有子域？

是不是 CDN？

前端资源从哪里来？

有没有测试环境？

有没有明显配置疏漏？

这才是第一步。

先从空间搜索引擎看一眼

咋们先看了 URLScan。

这个地方很适合看公开历史记录，因为它能帮我们快速看到别人扫过哪些 URL、页面跳转到了哪里、服务端大概是什么。

截至本文整理时，也就是 **2026 年 8 月 3 日**，URLScan 对 `spideytracker.net` 有 14 条公开结果。

里面能看到 `/intl/uk/`、`/us/`、`/intl/us/` 这些路径，也能看到一部分请求跳到了 `spideytracker.com`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8swOkKrLpPeUAaXrwiap3yFQJ5R0Ldd5HSuECFwr8ibQEDLduYXrcmR8fxEklawauicR3iaspW1F3tHSZibLVvAnHJEMhIDv7UDFH5M0aljdgW2o/640?wx_fmt=png&from=appmsg)

【👆：URLScan 搜索结果】

把 URLScan 的 API 结果整理了一下。

这里比较关键的几个点：

`/intl/uk/` 是 200；

`/us/`、`/intl/us/` 这类路径是 404；

历史记录里服务端都显示为 Apache；

IP 和 ASN 指向 Akamai。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8swOkKrLpPd9mkKWLUgpT2wpS7LHz14ppAloibsPHsM9BCMeTg2qkRHIEjeeIohWbzWiah10cV0zTLvjbH7sTl1libVcunBZL6piaGfbVRKibFJM/640?wx_fmt=png&from=appmsg)

【👆：URLScan 历史记录摘要】

这个阶段一般不会急着判断漏洞。

因为空间搜索引擎看到的是“别人某个时间点扫到的状态”，它适合当线索，不适合直接当最终结论。

真正要跑一遍的的，还得自己再测一遍。

子域名这里有个 stage

然后看子域。

可以用公开 hostsearch 数据看了一眼，结果不多：

`spideytracker.net`

`stage.spideytracker.net`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8swOkKrLpPdKJuZibqFziaZFicPdgjn5TF3C6ZPkbp7lLS1pR3iceVt1X5UibDTlRn9k4HoJUUcHNlt3Rh2YFWRBvZNTib0btqsF8OVXDgu4Mjf7Y/640?wx_fmt=png&from=appmsg)

【👆：hostsearch 子域名结果】

这里的 `stage` 就比较有意思了。

因为很多真实项目里，stage、staging、test、dev 这类子域，往往比正式站更容易出问题。

说做就做，对 `stage.spideytracker.net` 做了一个很轻量的确认。

DNS 显示它 CNAME 到 AWS ELB：

`alb-microsites-stg-368882556.us-west-2.elb.amazonaws.com`

访问 HTTPS 返回：

`403 Forbidden`

`Server: awselb/2.0`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8swOkKrLpPdDJbS1WPq6fnHkLtGLawVLyELW1A3Snvsx2PqvlyxLuuNL7ZZWhVxfg542TeYpC4HUqnLibXcYGbI5KWosQGJ7QeFGD3vNEOn0/640?wx_fmt=png&from=appmsg)

【上：stage 子域名检查】

这里要注意。

**403 不等于安全，也不等于漏洞。**

它只能说明当前访问方式下没有直接打开。

后续如果是正式项目测试，我会继续确认几件事：

stage 是否有白名单；

是否存在 Host 头差异；

是否还有其他路径；

是否和正式站共用配置；

是否能通过历史快照或 JS 资源反推出接口。

但这篇文章就不继续往攻击性方向扩了。

因为我们现在的目的，是写一个浅浅的测试过程。

DNS 和 CDN 痕迹很明显

接着看 DNS。

主域名 `spideytracker.net` 解析出来多个 A 记录，TTL 很短。

这基本就是 CDN 边缘节点的味道。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8swOkKrLpPet2KZqwM1K6hVtTR3xYOTiaJyWYicunDzSxsoW4oGBBOmfJjT5f5JjxcIJydR9Mxm25H5fLIx3sQnFKbfqkYfbcJWSibM3Uvd5Os/640?wx_fmt=png&from=appmsg)

【配图：DNS A 记录】

NS 记录这边可以看到 UltraDNS。

![](https://mmbiz.qpic.cn/mmbiz_png/8swOkKrLpPcgQyXYGV4zY8ZNbNOfnyIXkKibJILzfbC2FlCY1QfQN57ZKF2fDgSmNYcn6P5asyE5dbotn7a6U4B9u1Cmt9OajyqwEwlKlHvg/640?wx_fmt=png&from=appmsg)

【👆：NS 记录】

然后我拿其中两个 IP 做了 RDAP。

结果都指向 Akamai 的网段。

![](https://mmbiz.qpic.cn/mmbiz_png/8swOkKrLpPfuGlia5lUZenxGzkTQ8NBazxosSnTnXWZXuvFibk1cfVZt9XEBjNtJKOgppAc8kY40SzfuLL62W603ibCxqZa25uTVszklBzYhec/640?wx_fmt=png&from=appmsg)

【配图：IP RDAP 归属】

这里有一个很容易踩的坑。

**看到 IP 不等于看到源站。**

尤其是这种电影宣发站、活动页、营销页，大概率前面会套 CDN。

所以你看到的 Akamai IP，更多代表的是边缘节点，而不是后端真实服务器。

这个判断很重要。

如果把 CDN IP 当源站去写风险，报告就容易跑偏。

响应头能看到什么

再看 HTTP 响应头。

主页面返回 200。

能看到：

`Server: Apache`

`X-Request-ID`

`X-Frame-Options: SAMEORIGIN`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8swOkKrLpPdcRVwf5vf3CXDica2dYbd64N4MjUzLHCwUmiaQ5tTK7ZYaiaTDGZFC09viaTknJ0pPwhsfoXEABeXoSqQasRQCtPvC3B8OgWNj3fg/640?wx_fmt=png&from=appmsg)

【配图：HTTP 响应头】

这里我比较关注两个点。

第一个是 `Server: Apache`。

它只给了一个大类，没有具体版本号，所以暂时不能直接靠版本判断漏洞。

第二个是 `X-Frame-Options: SAMEORIGIN`。

这说明站点对点击劫持有基础防护。

至少从这一次响应来看，它不是那种完全裸奔的活动页。

不过我在这次响应头里没有看到明显的 CSP 和 HSTS。

这个不能直接写高危。

但如果是正式安全加固建议，我会把它放到“安全响应头补齐”里。

源码比页面更有东西

页面本身看着像一个互动地图。

但源码里能看到更多信息。

我简单做了一下关键词统计。

Astro 构建痕迹非常明显，`data-astro-cid` 和 `_astro/` 资源很多。

同时还能看到：

New Relic；

OneTrust Cookie；

Google Tag Manager；

Google Maps；

CloudFront 静态资源；

Sony Pictures 相关链接；

X 账号链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8swOkKrLpPeaE5H3xZ2ApkO4GNshmnsdYF1v0HTRQ6oFWSWvj6yE6iczFLvOLa5w0EibEK5WtR4s3PLtv47XoicuiaUKwJgT95Ua98rgibYQQicfs/640?wx_fmt=png&from=appmsg)

【👆：源码关键特征统计】

再看资源列表。

这里我把前端可见的 Google Maps key 做了脱敏，文章里没必要把完整 key 放出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8swOkKrLpPdDA6JibGls93TzrsmQU1SC1QZcXgfYdFzGcHjHtxKpAC88kJibRo9u0jEonFpkCdwSUhhjZO6IuibPZibtHAxonQ4pm0xftpe35Mk/640?wx_fmt=png&from=appmsg)

【👆：页面资源与第三方依赖】

这一步其实挺有价值。

因为如果我们能把一个“电影彩蛋页”，拆成一张更真实的资产关系图：

主站在 Akamai 后面；

票务/预告相关资源走 CloudFront；

Cookie 合规走 OneTrust；

监控埋点走 New Relic；

分析统计走 GTM；

地图交互走 Google Maps；

品牌和隐私条款回到 Sony Pictures。

这就是为什么我一直觉得，信息收集不是“扫一遍就完事”。

真正有用的是你要知道：

**这些东西之间是怎么连起来的。**

目录扫描我没有大字典硬怼

然后做一点目录探测。

这里我没有拿大字典去硬扫。

因为这种公网活动站，如果你只是为了写文章和做轻量验证，没必要上来就高并发 fuzz。

我只测了几个最常见、最容易暴露问题的路径：

`/robots.txt`

`/sitemap.xml`

`/.well-known/security.txt`

`/.git/HEAD`

`/.env`

`/.DS_Store`

`/config.json`

`/api/`

`/admin/`

`/debug/`

`/backup.zip`

结果如下。

![](https://mmbiz.qpic.cn/mmbiz_png/8swOkKrLpPfBCa8v29Q0e5NAvicMSibtRKvrhiax4lxC33E0EduTFC4rnzQR1IFibFHHsgSPwZgL7yg51RYWO6pogpEs9ibAamwvFcldo7pPkAq0/640?wx_fmt=png&from=appmsg)

【👆：低风险路径检查】

这组结果看下来，没发现直接可读的敏感文件。

`.git/HEAD`、`.env`、`.DS_Store` 是 403。

`robots.txt`、`sitemap.xml`、`config.json`、`api/` 是 404。

`admin/`、`debug/`、`backup.zip` 这类路径会 302 到 `404.html`。

说得直接一点：

**这一步没有捡到低级洞。**

但这个结果本身也有价值。

因为它告诉我们，至少从这组常见路径看，站点没有把源码、环境变量、备份包这种东西直接挂出来。

所以总结！手动跑TOP10 基础项怎么测

这个站没有传统表单，也没有登录入口。

所以我没有硬写什么 SQL 注入、弱口令、越权。

没有入口就硬编漏洞，那就太假了。

我这里主要做了几个适合当前站点的基础项：

CORS；

Clickjacking；

敏感信息暴露；

安全配置；

第三方依赖暴露面。

先看 CORS。

我带了一个外部 Origin：

`Origin: https://example.com`

GET 和 OPTIONS 都没有看到 `Access-Control-Allow-Origin: https://example.com` 这种放开结果。

![](https://mmbiz.qpic.cn/mmbiz_png/8swOkKrLpPfFrD3jkVloB1c6tPMiaYNIB3ia5Tyl0DXPtVBthFblIib1Z5RLiazuRPfK8JpcicMIeCzL9k17evl2315YAy3wiaDDvEcgrjP8QribibY/640?wx_fmt=png&from=appmsg)

【👆：CORS / OPTIONS 检查】

所以这一步的结论是：

**未发现明显 CORS 放开问题。**

Clickjacking 前面也说了，响应头里有：

`X-Frame-Options: SAMEORIGIN`

这至少说明有基础防护。

敏感信息这块，前端确实能看到一些第三方配置和调用痕迹。

比如 Google Maps API key。

但这类 key 通常就是前端调用用的，不一定等于泄露。

真正要判断风险，关键看：

有没有 Referer 限制；

有没有 API 限额；

有没有绑定具体服务；

有没有异常...