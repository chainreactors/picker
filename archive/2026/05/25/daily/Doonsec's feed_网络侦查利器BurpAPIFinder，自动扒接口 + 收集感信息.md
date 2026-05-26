---
title: 网络侦查利器BurpAPIFinder，自动扒接口 + 收集感信息
url: https://mp.weixin.qq.com/s/XHo8JQXi5ihY8cpWyCMTIQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:05:33.833053
---

# 网络侦查利器BurpAPIFinder，自动扒接口 + 收集感信息

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mQFl6fQOc0rqMjmgjJTFuwqmZJpRGCyjvGc0apR6BJuu0KM2cac8rvfggoXiblELg0CMgnCk3MSIgjfusQ1PA9iaSO9RxhWTlMnxqhugIEs2Q/0?wx_fmt=jpeg)

# 网络侦查利器BurpAPIFinder，自动扒接口 + 收集敏感信息

子午猫
子午猫

网络侦查研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2bujwd3M0M1ICStsbhAHWtth8dQwoBBFoNDafDAzGbm1sCA8bqVWIjs40A8lu9rtuD4yeOOwDNadg/640?wx_fmt=png)

开展网络侦查过程中，手动从JS文件里艰难翻找接口，同时排查敏感信息，那过程犹如大海捞针，折磨着每一位从业者。页面背后隐藏在JS路由中的接口，配置文件里深藏的后台路径，以及可能在响应中“裸奔”的账号密码、云密钥、Token等敏感数据，都让这项工作既耗时又极易遗漏。不过，今天要给大家介绍一款专为网络侦查量身打造的强大Burp插件——BurpAPIFinder，它将为你开启高效便捷的网络侦查新体验。

## BurpAPIFinder核心功能大放异彩

BurpAPIFinder是基于Burp Suite开发的一款接口发现与敏感信息识别插件，它就像一位不知疲倦的智能助手，全程监听代理流量，默默工作且不会干扰你的正常流程。其核心功能实用且强大：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mQFl6fQOc0rR0bWG81lp76nkPxFHtOkhswDRn6q9QMk0WEeicHkkWAtXLYTSt3MPImZt1bQuiaY6ufOot9slTyGBia0hqdgmooYtqLq6fe1AGM/640?wx_fmt=png&from=appmsg)

1. **接口路径全自动提取**：它不局限于简单的正则匹配，而是支持多种模式，能从HTML、JS文件中精准扒出绝对URL、相对路径以及接口后缀。哪怕是隐藏得很深的API和管理端路径，也能被它“揪”出来。
2. **敏感信息一站式排查**：内置106条源自攻防实战的指纹规则，还整合了HaE、APIKit、sweetPotato三大主流规则，无论是账号密码、手机号、身份证，还是云KEY、JWT、Shiro特征等敏感信息，统统都逃不过它的“法眼”。
3. **智能路径补全探测**：支持自定义父路径，能够自动将发现的接口拼接到诸如/api/v1、/admin等前缀下再次尝试访问，对于前后端分离以及版本化接口的探测有着极佳的效果。
4. **可视化结果一键筛选**：主界面实时展示请求数据，提供“只看重点”“只看敏感内容”“只看200状态”等筛选选项，面对海量接口也能快速聚焦重点，优先排查关键漏洞。
5. **带凭证自动复测**：可自定义Cookie、Authorization请求头，对于匿名访问无法通过的接口，能带着凭证自动重新测试，确保不会放过任何未授权访问漏洞。

## 轻量高效的技术原理，为测试保驾护航

这款插件在运行过程中，仅监听Burp Proxy的响应包，不会对原始请求进行任何修改，充分保障测试的安全性。其核心流程清晰明了：

1. 监听Burp代理流量，全面读取URL、请求方法、状态码以及响应内容。
2. 自动过滤静态文件、白名单路径以及3xx/404等无效响应，有效减少干扰信息。
3. 从HTML/JS中提取接口路径，并将其存入本地SQLite数据库。
4. 调用指纹规则匹配敏感信息，并在界面上标记结果，方便人工进一步复核。

整个插件模块分工明确，Proxy监听、路径提取、任务调度、指纹识别、结果存储各个环节各司其职，运行稳定流畅，不会出现卡顿现象。

## 5分钟快速上手，零门槛轻松使用

1. **下载插件**：前往项目的GitHub Releases页面，直接下载编译好的jar包。需要注意的是，使用该插件要求JDK 9 +的环境，而新版Burp可直接兼容。项目地址为：https://github.com/shuanx/BurpAPIFinder 。
2. **Burp加载插件**：打开Burp Suite，依次点击Extensions → Installed → Add → Java ，然后选择下载好的BurpAPIFinder jar包。加载成功后，会出现专属的标签页。
3. **开始自动扫描**：在浏览器中配置好Burp代理，正常访问目标站点，插件便会自动监听流量、提取接口并识别敏感信息，全程无需手动干预。
4. **查看与筛选结果**：主界面会展示请求总数、JS解析成功数等数据，通过筛选按钮能够快速定位重点接口与敏感内容，大幅提升人工验证效率。
5. **自定义配置（可选）**：在配置页可以灵活调整敏感关键词、开启主动探测功能以及设置自定义父路径。如果是旧版本升级，需要删除同目录下的BurpAPIFinder.db和finger - tmp.json，以避免出现冲突。
6. **手动编译（可选）**：对于喜欢探索的朋友，可以拉取源码，使用Maven一键打包：

```
git clone https://github.com/shuanx/BurpAPIFinder.gitcd BurpAPIFindermvn package
```

## 四大实战场景，尽显网络侦查必备实力

1. **前端接口资产梳理**：只需访问首页、登录页、管理页等页面，插件就能自动整理JS文件中所有的接口路径，快速且全面地完成资产面的摸底工作，从此告别手动复制粘贴的繁琐。
2. **敏感信息泄漏排查**：一键扫描响应包，就能精准定位账号、密码、云密钥、凭证、身份证等各类敏感数据，排查泄漏漏洞又快又准。
3. **JS路径智能补全**：针对/api、/api/v1等网关前缀，插件会自动拼接路径并进行重试，轻松发现常规扫描容易遗漏的版本化接口。
4. **授权接口未授权检测**：配置好凭证后自动进行复测，能够快速发现匿名访问受限，但携带凭证却可获取数据的未授权或越权漏洞。

## 总结与提醒

Burp原生流量视图通常只记录请求，而BurpAPIFinder完美地弥补了这一短板，将前端零散的接口和敏感线索全部整合起来，转化为可筛选、可复测的清晰结果。如果你还在手动艰难地翻找JS文件、尝试各种接口，那么这款插件绝对值得一试，无论是攻防演练、内网自查还是靶场练习，它都能让你的网络侦查效率提升一倍。

最后郑重提醒：本工具仅可用于授权测试与安全自查，严禁用于任何非法攻击行为，合规使用，是我们每个人应尽的责任。

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2bujwd3M0M1ICStsbhAHWtt0VVqCfFLOVnpmeNJ3R59doWtI0AmqLn4Qkic8aAS06l0pATjcYx10zw/640?wx_fmt=png)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2b9Dn5TZppcYVNqtewpGLM6TUkWg29ayK9yWAJbqViaE15Ltf8AprRumW3Lmw3ibHOAsMYMnhNqcfiaA/0?wx_fmt=png)

网络侦查研究院

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2b9Dn5TZppcYVNqtewpGLM6TUkWg29ayK9yWAJbqViaE15Ltf8AprRumW3Lmw3ibHOAsMYMnhNqcfiaA/0?wx_fmt=png)

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