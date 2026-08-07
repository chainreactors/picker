---
title: EDU低危漏洞也可以通杀
url: https://mp.weixin.qq.com/s/mgkcM_csmIcAG7U62vJ0mQ
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:24:09.174803
---

# EDU低危漏洞也可以通杀

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icCLY10D8tvLIMPnXs1mmyq0neLe0qy0NCEnzGdQOfksSbfpjsJVSaJ0t0iagzcO5CjAZg29rdxtdOE5ogSsrV55h2UnaogRvicfMLUljy3p3A/0?wx_fmt=jpeg)

# EDU低危漏洞也可以通杀

信安笔录

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

某次测试中通过对js中接口遍历发现漏洞，虽然是低危，但也通杀了30+站。

以下文章来源于好靶场
，作者Elon

![](https://wx.qlogo.cn/mmhead/XYrRG5UShDc8MiasaqKIRuv8ygOQeco20z91bZzqSptr4yT8nEmmLBzdFCY6BRHg3fKmcfiafia6cg/0)

**好靶场**
.

学安全要练习，练习就选好靶场。我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。

> 💡 好靶场 团队宗旨：我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。所以我们团队名称就叫“好靶场”。

## 1. 好靶场介绍

官网链接http://hbc.haobachang.com/

[好靶场新手入门教程指南2.0](https://mp.weixin.qq.com/s?__biz=Mzg4MDg5NzAxMQ==&mid=2247489042&idx=1&sn=5f5ce07562ffb21caf3e51daa59cdf96&scene=21#wechat_redirect)

## 2. 通杀思路

### EDU截图

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJcwvvDkCxmW90DiaicfUELR8BI9jsNYepPx2x6PACke36iatSSEDUkSbtvslZNgT2u9rgSm7TmUSvibmCCzxgcKeX0DKuIDqWtLrk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvLk4qa3nJZpQgQyaapXXtG36uYS41n3Q3IlIR2curxJaSiakJA7Tm09qRFCa0nsY2T1Hm3VQUaR8SxhbicrOQyHWwkDh3Mf8poso/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvKAT8Tem6dVgPWEoXVbqGmcSayKGOIrb5gxhfTJPS3ZF6YmLIVgYza4ic3LuxPX44aWRm1AtRU9GJTWME7Tj2MxluU2UuMyyzXs/640?wx_fmt=png&from=appmsg)

Hello，宝子们，今天给大家分享的是一位师傅通过好靶场练习之后积累思路拿到一个小通杀的案列。

### 思路分享：某云的Token接口

#### 起因

目标是某智慧校园平台，先是\*\*\*\*.edu.cn，就是个 Vue 的 SPA。 SPA 的好处就是前端里啥都打包在 js 文件里。所以第一步永远是把所有东西全拉下来。

### 寻找接口

JS 文件下下来之后，用正则把里面所有 `/xxx` 这种路径全提出来。这里有个坑，直接搜字符串匹配 `"/xxx"` 会漏掉很多用拼接的方式拼出来的路径，所以我当时是直接把所有带斜杠的字符串先导出来过一遍，再筛出像接口的。

筛出来的接口一堆：`/a**et/*`、`/d**m/*`、`/os/*`、`/m*s/d***ce/info/v***Url/*`，还有 `/c***er/a*r/v1/load***`。当时看到 `load***` 这个名字就觉得有戏——"加载某token"这种接口。

#### 判断免鉴权

光有接口清单不够，还得知道哪些接口不用带 token 就能调。这个平台前端有 axios 拦截器，会判断请求有没有 `**Token` / `**Token` / `***ist` 这几个标志。

所以我用了个正则，去匹配 js 里 `"/接口路径"` 后面一小段内容里带 `****Token:!0` 的。这种匹配方式有个好处：能把接口和它的鉴权配置一起捞出来，不用一个个去翻调用点。

结果 `load***` 就在这个列表里，和 `/**/rdspwd`、`/***/token` 这些登录接口排一起——也就是说它被标记成免鉴权的。当时心里已经有个八九成把握了。

#### 如何验证

直接 GET `/****/****/****/v1/load***`，不带任何 cookie 和 token，返回了 `d***.******Token`，格式是 `24.xxx.2592000.过期时间.282335-15812841`。

这里有个细节，某家的 AIP 的 token 格式是 `2********.<appid>`，最后那段就是 appid。所以光从返回的 token 就能看出用的是哪家的。

### 好靶场（相关练习靶场）

```
http://hbc.haobachang.com/findbug?keyword=vue
```

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvKqGYib7UL9TRkd67IU5ByRwuZQFqCMHL0V6MYjfiaCoeBDbwZyocUZZ0CXHgsNvzt3h78Y2DGhN2VrfvpViarWHJfwkWc88tLR6Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvI6NLh62VIUCGfCQ1oiaEcjGKd9vPVSYiayic65BIaV7e0ic6YO7UFBsFjlrSEIuiauAn4053hWTx5ESu6iaJ8lQNHbzuwiaYQH13Zf4w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvLPoNs5t12dAReu1YlMWkpfqLqoMPiaasb9tx4lFJYRTzl3d9YhibV6jibLf9NNpK0po09icSDDDKSYUTp4CAZW8fic7ajm18jicDvfc/640?wx_fmt=png&from=appmsg)

## 3. 如何使用好靶场

### 首先关注“好靶场微信公众号”然后发送bug，可以点击链接直接登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvJn80Sicpic7OmticxNKsrrgJFTNUhAftHBnCibiaicLFUCB8ehvyT0PrXEG4lDcsnvDLAqJSBQlHz0V4F8SIF5gpO9iaNiaH97PBFjQRw/640?wx_fmt=png&from=appmsg)

微信群、QQ群每日更新限免靶场与免费学习资料，加好友即可拉你进好靶场内部交流群，群内同步全部通知

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvKvSCywPlC90S8mWg9fr8xxhWShHvJ3z1njibcmLCFHchA6Xl70fByLuek75ZgF8uUR5r8wqQJT730tcQvzD7ATHIdIibj1Yq3Io/640?wx_fmt=png&from=appmsg)

## 4. 福利

### 福利1：个人中心输入：[官方邀请码]：0482d6d28539424c，白嫖14天高级会员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLCicFgYymsZVpugibO1C8AVsib8XicsA53jA7a050c434b35AhxXQHcdCOzjtRl9N3GpUzIsFdNXY0rh56Mll8dmpKNJIib98uZvibQ/640?wx_fmt=png&from=appmsg)

### 福利2：关注好靶场bilibili，抖音。拿着关注截图找到客服，领取5积分。

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvIicU6vDElyplQWIXkDdgNCmMkL9xCMOx9EsUKtNN4OhyBrAGbMo3QkpzFS5OP8ETAdLenHsJAjz3XCVrfnBSu186zyaqERbsLk/640?wx_fmt=png&from=appmsg)

### 福利3：每日限免：我们会在工作日随机开放一些靶场的限免，还请加群关注。

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJguqkEichc2zwjCTwfQsl8FW56dZAlNmdDAbLVarx22icu0Y6sJibk94vBBoibkNU3htXEknvAVQQCObYtlB51hatQab1ibRp13a98/640?wx_fmt=png&from=appmsg)

## 6. 好靶场AI资讯

为方便方便大家及时获取每日的AI资讯内容，我们选取了每日的AI资讯内容在群聊中更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvJsIWuj3TaQpcdVftR1sIg01JShbic8R3G6r1NCaialupyF5UE3yuOsBiamQdEWic3SIDz20AOicsAPeD3jdZiaY5uaa2TH6EkEU3NwU/640?wx_fmt=png&from=appmsg)

### “噜噜大王”正式上线

大家点击左边的快捷工具，有一个AI助教功能，然后点开就可以和噜噜大王对话啦，由于是内测期间，仅限于年会员才可以进行使用。还需要进行微调，会随着大家的使用而进行优化；你可以尝试问一下关于打靶场的问题

## 🚀好靶场会员订阅

> http://hbc.haobachang.com/user/vip

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvLicRSPx4NXENbaPVxeF2rLIuyHArtS8HOoIM8TfID3wFxo8icSQDQasMxnqU9QbjfXskbHibKgHbeVBw3nBZ21L65YekWYnt4xUA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJcatqLTdbqI1MI6wP5uKCiagTMKqQOvHlrRI5nIGzOg4nzIKIwfOBruOVe7cSNK7T29SwAyUY7f0tMTuqicl4aKUBAGJKPKa3A0/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/gPlD5PHq3tLtzsoFHMPUqbtVvAEZFrnibBzSPohtfWarQlRzHGftBNlkGc5mZKIIEqJWRlNxgjuthwVlibmZBG9A/0?wx_fmt=png)

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