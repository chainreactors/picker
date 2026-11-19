---
title: 搞安全的必收藏！10个免费网络安全搜索引擎
url: https://mp.weixin.qq.com/s/32d3vIdSsRPGP9FbnJ_8_A
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:41:20.251587
---

# 搞安全的必收藏！10个免费网络安全搜索引擎

# 搞安全的必收藏！10个免费网络安全搜索引擎

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

安全干货预计阅读 6 分钟 · 共 2091 字

搞安全的必收藏！10个免费网络安全搜索引擎

收藏这一篇就够了

#OSINT#网络安全#资产测绘#白嫖神器

READING PATH

阅读路线

5 个章节

01

为什么这些工具值得收藏

-

02

核心 10 个搜索引擎

-

03

额外强力互补工具

-

04

使用建议与合规提醒

-

05

写在最后

做安全、做渗透、做威胁情报、做企业资产测绘的人，手里都得有几把「白嫖神器」。今天整理了目前最实用的 10 个网络安全 / OSINT 搜索引擎，外加几个强力互补工具。会用的人等于捏着免费情报库。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfz9BxFFHfd9rpiaD7MA0C0hnaR4uszwr1v8XrXobwBC9oGH0Kocsx8If3x6m6Sx6jXzvYZSoZuheHxkTylOcjs2ceWlstUSNibYw/640?wx_fmt=png&from=appmsg)

CHAPTER 01

**01****为什么这些工具值得收藏**WHY IT MATTERS

在真实工作中，我们经常需要快速回答这些问题：

●某台服务器到底暴露了哪些端口和服务？

●某个域名背后关联了多少 IP、证书、历史记录？

●某个 IP 是普通扫描噪音，还是真正的攻击源？

●开源组件有没有已知高危漏洞？

靠传统搜索引擎很难直接拿到答案。而下面这些工具，专门为「网络空间测绘」和「威胁情报」而生，很多都提供免费额度，用好了能大幅提升效率。

CHAPTER 02

**02****核心 10 个搜索引擎**THE CORE 10

01

Shodan

**官网**：https://www.shodan.io

全球联网设备与服务器搜索的鼻祖。端口、Banner、地理位置、组织信息都很全。适合找暴露的摄像头、数据库、工控设备等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxbgEJJ38b6ibkGTy4YC4LbweS9HOS6f6Dfib2ibj1T6Aic44Ckp3yic0qKHW3dm2SDJ0ePSpo3pnk8UN23UwBY3HUn36Hs2ak54O40/640?wx_fmt=png&from=appmsg)

常用查询示例：

●`port:22 country:"CN"`

●`product:"Apache" version:"2.4.49"`

提示：免费额度很低，建议考虑一次性 Membership。

02

Censys

**官网**：https://search.censys.io

公网主机、证书、服务指纹查询。结构化程度高，证书透视能力极强，特别适合做关联分析和攻击面发现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfyIXx2Qbia3AImYbicTCnTFhR1GiaAOGDjGwUfBk5m2C3F1Dbn4PRI2pDqOqMxCS3VJj8dFubJ7KvyNug0JibAQ5Zz2wiaKLWs6F2qE/640?wx_fmt=png&from=appmsg)

03

ONYPHE

**官网**：https://www.onyphe.io

网络威胁与资产情报结合的平台。既能看暴露服务，也能看到威胁标签，欧洲视角数据不错。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfwyhRylqFA1pbytW5wr7t4B0oKsIaZ94cx0CPqIat6RsW0hw6WP1ge9xN0mgicqNE93qOIiarTch5AyXiaFy6aU5HwCr7ZPV6DvTw/640?wx_fmt=png&from=appmsg)

04

ZoomEye

**官网**：https://www.zoomeye.org（或 zoomeye.ai）

国内常用的网络空间资产搜索引擎，中文友好，亚太地区覆盖较强。指纹规则丰富，支持应用、标题、端口组合查询。

常用示例：

●`app="Nginx" && country="CN"`

●`title="管理后台" && port="8080"`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfzGlHcc22xDJPV7jbyQqGMq05g2meUkrw1k9icH98yTD1fo5atiab9j8C4uCj7KQfwfDbyktLVibAyIwarSEVZxNCq8HPKnwqdtcw/640?wx_fmt=png&from=appmsg)

05

GreyNoise

**官网**：https://viz.greynoise.io

专注「互联网噪音」识别。当一个 IP 打到你防火墙时，能快速判断它是普通扫描器，还是真正针对性攻击。SOC 降噪利器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfzTmUEcRQCj2nmJXemzicmPVHAy8q3JjWpLuictfYOyfrLqJbt20y27SSLTZIjrRicILZzUfLibTkVVh9N9Wmmw7fNno3EMq24R8Bs/640?wx_fmt=png&from=appmsg)

06

Hunter.how

**官网**：https://hunter.how

网络空间资产搜索引擎，支持 IP、域名、端口、产品指纹等查询。覆盖广，有免费额度，语法接近 FOFA / ZoomEye，适合做资产发现和指纹检索。

常用示例：

●`product.name="Nginx"`

●`protocol="mysql"`

●`domain.suffix="example.com"`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfyNnqzSTLKEBvE4iajM4R7ehGGxib61tkO7Vo38INSia8HLNox7qaQTbrayM0ibrmXqoVwQtkXLlsCUJ6qTsccY3VRDicClI1e8F8es/640?wx_fmt=png&from=appmsg)

07

Netlas

**官网**：https://netlas.io

IP、域名、端口、证书、WHOIS 一站式检索。查询语法类似 Elasticsearch，免费额度相对友好。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfy4ow4CicUl4UAPjiaeCEh5gWAGhIq0teGU6ZnYbyOJlbicw8Pnf9HUZ0wQu0D7ag2kqKbAgFveHCzicFPficafV9BL9kmYG2OAXY3A/640?wx_fmt=png&from=appmsg)

常用示例：

●`port:443 AND geo.country:CN`

●`http.title:"index of"`

08

FOFA

**官网**：https://fofa.info

国内非常主流的网络空间资产搜索引擎。语法强大，指纹 + 图标哈希能力突出，企业资产测绘几乎必用。

常用示例：

●`app="ThinkPHP" && country="CN"`

●`title="登录" && body="password"`

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfz0fUDavYlyqTLWibchicRcBnPjEKic3dZ7I17MVTdTTxPvQpBuPDSmOCUQTPjv5sIia0HXtzmicVMRdYMgOF1S5TYQSEXQtf5cSqaU/640?wx_fmt=png&from=appmsg)

09

NVD

**官网**：https://nvd.nist.gov

NIST 官方 CVE 漏洞数据库。权威性最高，做漏洞管理、补丁优先级排序时的核心参考。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfwK3lG6g7cpU7IypcAt8GiazvGTU8z1Nt6j3bVPQwxb63YCSxpCmibfUe072g43gyUAp0ew4ic45XrG1B67Rqpl1zIiclMiaPMfN1Qo/640?wx_fmt=png&from=appmsg)

10

OSV

**官网**：https://osv.dev

开源软件漏洞查询平台（Google 主导）。对依赖库、包管理器漏洞查询非常方便，可配合 osv-scanner 等工具使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfwuz6gltKOFpRB2lbgrISVoSAGAKdU2k3pflqWeZukR9rLhzWf4jREd79QoAIo51KAibpXjmPicicnHa5rs2dmOn6nciaRIfSqg1JY/640?wx_fmt=png&from=appmsg)

工具上新

10个网络安全搜索引擎已收录

一键直达，方便好用

#OSINT#资产测绘#白嫖神器

已经把这 10 个网络安全 / OSINT 搜索引擎全部收录进我的工具箱了

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfx9WjUXaNObRERNHDbfBRFdApoNUINu2uGIHOTGpLyyiciazer1dqHNOd3SJCNYnm4IXOKdwv6p05fUNpUoIdAuCtN5Apmq2RMHs/640?wx_fmt=png&from=appmsg)

工具箱[1]

CHAPTER 03

**03****额外强力互补工具**BONUS TOOLS

除了上面 10 个，下面这些也强烈建议加入书签：

●**LeakIX**（https://leakix.net）：暴露服务 + 数据泄漏索引

●**Criminal IP**（https://www.criminalip.io）：带风险评分的资产与威胁情报

●**BinaryEdge**（https://www.binaryedge.io）：扫描数据 + 风险评分

●**Quake**（https://quake.360.net）：360 网络空间测绘

●**urlscan.io**：URL 行为分析与截图

●**VirusTotal**：多引擎文件 / URL / 域名 / IP 检测

●**crt.sh**：证书透明度日志，挖子域名神器

●**SecurityTrails**：历史 DNS、WHOIS、子域名

CHAPTER 04

**04****使用建议与合规提醒**IMPORTANT NOTES

重要

合规红线

#授权#合法使用

这些工具只应用于**授权范围内的资产发现、防御研究和合规情报工作**。未经授权对他人资产进行大规模扫描，属于违法行为，请务必遵守法律法规和平台使用条款。

实操建议：

1.**多引擎交叉验证**：同一个目标尽量用 Shodan + Censys + FOFA/ZoomEye 同时查，结果经常互补。

2.**合理使用免费额度**：日常探索用 FOFA、ZoomEye、Netlas；深度查询用 Shodan 会员；证书关联优先 Censys。

3.**自动化**：多数工具提供 API，可配合 theHarvester、Amass 或自写脚本批量使用。

4.**持续更新书签**：网络空间搜索引擎更新较快，建议定期检查官方状态和额度变化。

CHAPTER 05

**05****写在最后**

工具再多，关键还是「会用」和「用对场景」。建议先从 Shodan、Censys、FOFA、ZoomEye 这四个开始熟悉语法，再逐步扩展到 GreyNoise、Netlas 和漏洞库。

把这篇收藏起来，下次做资产测绘或威胁情报时直接打开就行。

收藏了吗？有用就点个赞转发给同事吧

安全圈一起进步

· 点赞 ·

喜欢就点个赞吧

· 转发 ·

分享给更多朋友

· 推荐 ·

推荐给身边的人

## 参考资料

[1]工具箱：https://didiplus.kwpmp.cn/?preview-theme=theme-heolink

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过