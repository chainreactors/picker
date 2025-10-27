---
title: api漏洞测试-GraphQL自省问题
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496184&idx=1&sn=7014f42d58aee7478234c29528d5208c&chksm=e8a5fb9bdfd2728d04ec4b21fd8e06a8354615684c8ab6ae00d618ea35f3b4eedfffaa5ba930&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-21
fetch_date: 2025-10-06T18:49:15.123832
---

# api漏洞测试-GraphQL自省问题

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6UmqoqZ9GUguvT9uGrIeuFMicTa9L49Rx4y5SFM3VEos0f8eomFKfRECDnADHZUkL0bKnOLvrZYTA/0?wx_fmt=jpeg)

# api漏洞测试-GraphQL自省问题

原创

zuriel

迪哥讲事

api漏洞测试-GraphQL自省问题

## 正文

正常情况下的请求：在生产环境中，开发者通常会禁用自省查询功能，只允许有限的、明确授权的查询。例如，用户只被允许查询他们自己账户的信息，无法访问其他用户的信息。

示例（正常请求）：

```
{
  user(handle: "john_doe") {
    id
    name
    email
  }
}
```

这个请求只会返回授权用户的信息，开发者可以通过权限控制和验证来确保用户不能访问其他用户的数据。

受到攻击后的请求：如果自省查询未被禁用，攻击者可以使用自省查询来获得整个 schema，然后构建出未授权的查询，从而访问敏感数据。

攻击示例：首先，攻击者使用自省查询获取整个 schema 信息

使用下面链接中的payLoad进行查询

https://gist.github.com/craigbeck/b90915d49fda19d5b2b17ead14dcd6da

获得 schema 信息后，攻击者知道了有一个 "team" 节点，即使这个节点已被标记为弃用，攻击者仍然可以通过构建如下的查询来访问：

```
{
  team(handle: "security") {
    id
    about
    base_bounty
    bug_count
    sla_failed_count
    sla_missed_count
  }
}
```

通过这种方式，攻击者可以访问本应禁止访问的团队信息，甚至获得未公开的字段，如 "sla\_failed\_count"。

更多请看星球

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj6UmqoqZ9GUguvT9uGrIeuFZ7rfczKajb4XRKwIA48pjEI8pzXhVuXO78ic0RHpLjlWJmrdvzibGOZw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj6UmqoqZ9GUguvT9uGrIeuFTbrR2u9wKS2h6peQicDHG6QLr73gsmmWibU1jbfQLsLuxLFgjSO2UdFA/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

## 参考

https://hackerone.com/reports/291531

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