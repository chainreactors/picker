---
title: 攻防、SRC必备插件 | 前端资产采集、嗅探、指纹扫描、泄露扫描、漏洞审计与 Vue Router 分析
url: https://mp.weixin.qq.com/s/qVYvfo0WHJ6RS3QUgX9mlQ
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:35:14.310140
---

# 攻防、SRC必备插件 | 前端资产采集、嗅探、指纹扫描、泄露扫描、漏洞审计与 Vue Router 分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLibk43AmbibStdiblKB6ZZ4GlciaDvEOD08SDVFZp38PJrKWXBibePqJKRtyvF8gtTy1UQdhibN2fb4yxicDiaAjChuMvSQqLV1APXQ9Q/0?wx_fmt=jpeg)

# 攻防、SRC必备插件 | 前端资产采集、嗅探、指纹扫描、泄露扫描、漏洞审计与 Vue Router 分析

flagqaz
flagqaz

夜组安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！**所有工具安全性自测！！！VX：****NightCTI**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把**夜组安全**“**设为星标**”，否则可能就看不到了啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg)

## 工具介绍

玄镜 AegisScope 是一款浏览器扩展工具，用于在当前页面上下文中采集前端代码资产，并对页面 HTML、JavaScript、SourceMap、打包器产物和运行时接口线索进行分析。

它的目标不是替代人工安全审计，而是把前端侧最容易遗漏的代码资产、敏感信息、接口线索、路由鉴权依赖和逻辑风险集中呈现出来，让测试人员可以更快定位值得复核的位置。

## 核心能力

### 代码资产采集

* 自动采集当前页面的外链脚本和内联脚本。
* 支持页面 HTML 一并纳入采集与扫描。
* 保存模块分为 JS 和 HTML：JS 会将代码类资源统一打包为 ZIP，HTML 会将当前页面尽量内联为单个 HTML 文件。
* 支持继续发现运行时 chunk、SourceMap、框架资源、内联 SourceMap 中的源码文件。
* 对同源资源使用当前页面上下文读取，提高登录态页面的代码资源获取成功率。

![](https://mmbiz.qpic.cn/mmbiz_png/WibL3bOeESMJQMDGPtXqOzMibrVlJ5EL021lTJ2G9ySiaj8icU0tyiaZ6ia8RItC7ibobGHric23Jr4shXDYMCc8lNt1aCB85VOcBFckwZuLeENEK0s/640?wx_fmt=png&from=appmsg)

### 泄露扫描

泄露扫描用于发现前端代码中可能暴露的敏感数据、密钥、令牌和不安全加密用法。

支持识别的常见类型包括：

* 云厂商凭证：AWS、阿里云、腾讯云、Google Cloud、Azure、华为 OBS/OSS 等。
* 平台 Token：GitHub、GitLab、Slack、Discord、npm、Docker、Shopify、Cloudflare、Vercel、Netlify、Mailgun、Firebase 等。
* API Key 与请求头凭证：Bearer Token、Basic Auth、Authorization Token、X-API-Key、Session/Cookie Token 等。
* 个人敏感信息：邮箱、手机号、国际手机号、身份证号、银行卡号、公网 IP、内网 IP 等。
* Webhook：Slack、Discord、企业微信、钉钉、飞书等。
* 加密风险：硬编码 AES/IV/HMAC/JWT 密钥、AES ECB、DES/3DES、RC4、MD5/SHA1 安全上下文、RSA PKCS1/NoPadding、eval 解码执行等。
* 打包/混淆识别：Webpack、Vite/Rollup、Parcel、Browserify、Next.js、Nuxt、Angular、Umi/Dva，以及常见混淆和压缩特征。

扫描结果会按漏洞严重性排序，危害最高的结果优先展示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMKQHUk8F40TTiaqIGBYUicH8JXiczTEo5xzbHHHCmicD797rXQII9sAQRknOWf0RozZyIiak2KszBfLBU0D3SZ8VQlqUcR4vOThTass/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMLBiazuDe36JiaBg39m2hBbVlpzKgYibfzlAWKW9NqjFnyREKZmxe71mmEviaKdogpgLezZzY1oQIXkq1bTm49lb65ps4Qel88xME0/640?wx_fmt=png&from=appmsg)

### 网站嗅探

网站嗅探模块采用玄镜自研的多来源识别思路，用于对当前站点进行被动技术识别。点击主弹窗中的“网站嗅探”后，结果会直接在当前插件页面内展开，不会跳转到新的页面。模块会结合页面 HTML、响应头、Cookie、Meta、脚本资源、运行时全局变量和资源路径等多类证据，快速识别 Web Server、运行时、前后端框架、CMS、JavaScript 库、UI 框架、字体脚本、数据库线索、分析工具、CDN 和安全响应头等信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMLJMhIQg2NXG0iaOLiaq5HAoabtURDnzAoCRJO5bXFabFdryqlpibQyYqgZSruJJuGmm8qR86BszkeuC26Zge2y8JREnWicRojkdzk/640?wx_fmt=png&from=appmsg)

### 指纹扫描

指纹扫描模块位于网站嗅探页面中，用于对当前站点进行主动指纹识别。点击网站嗅探结果上方的“指纹扫描”后，会跳转到独立扫描页面并自动开始扫描，无需再次手动点击开始。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMLo2gCsbPck1GU0YzvVBnpia2sOvHQrZbKsukzR1sRWH09APibC8YzuzSibBkVa90CTM1brYYF0oc8x9d1y0RfpE61UxibkN5cAPes/640?wx_fmt=png&from=appmsg)

### 漏洞审计

漏洞审计模块用于从前端源码和接口线索中提取潜在业务风险，并辅助进行授权验证。

主要审计方向：

* 未授权 API、敏感 API、鉴权状态异常。
* 接口文档、OpenAPI、Swagger、Knife4j、GraphQL、GraphiQL 暴露。
* 前端路由鉴权依赖客户端状态。
* IDOR、租户/角色/归属字段可控。
* 支付、订单、金额、优惠、余额等逻辑参数风险。
* DOM XSS 数据流。
* 重定向、外部 URL、SSRF 参数风险。
* 上传校验依赖前端。
* CSRF、跨站凭证、CORS 配置风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMKibXOicibjWnNQTicl017JItZgNwgwcbEWdyUJPBJtJ5wUZslUFezkAsBQfOsOy0ChglhIUXmQ8pibatHk8OnDRZB93MQs7OicHL9Jw/640?wx_fmt=jpeg&from=appmsg)

### API 批量测试

漏洞审计模块内置 API 批量测试能力：

* 支持 GET、POST、HEAD、OPTIONS、PUT、PATCH、DELETE。
* 支持自定义请求体。
* 同时测试带登录态请求和匿名请求。
* 支持响应状态码、响应类型、响应预览。
* 自动将高风险 API 放在前面。
* 每条 API 支持单独手动测试并选择 HTTP 方法。

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMKjOvARxsVxFee1noKCUjBKBW4KDJnWMwEhDpFrrgUG9HBA7VoMSgF9SJUEwBibLRbD4Bwt4bGiaxtsOaJUSUNK7tLK9czibl2B4I/640?wx_fmt=jpeg&from=appmsg)

### Vue Router 运行时分析

Vue 工具模块用于分析当前页面中的 Vue / Vue Router 运行时实例。

主要能力：

* 识别 Vue 运行时、Router 实例、路由列表和守卫信息。
* 展示路由 path、name、meta、敏感路由标记。
* 支持点击路由直接跳转。
* 对前端路由鉴权类发现，可在验证时尝试清除路由守卫、修改鉴权 meta，并进入目标路由页面。
* 支持恢复已修改的路由守卫和 meta 状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMI7wkAw0D6k8fTlsq47jJvLlqbNtzibwdhfxhtjDSSHjzIcibiaSrjnPcguVGPog7cLOADsEDh77rawnYxoz5HNibA84szGb4Atc6Q/640?wx_fmt=jpeg&from=appmsg)

## 工具获取

点击关注下方名片进入公众号

回复关键字【260509】获取下载链接

## 往期精彩

[AI 驱动的 Web 加密流量渗透测试自动化代理框架 | 专为解决前端加密 Web 应用的流量加解密问题

2026-05-08

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMJW1apR1D7dTnQpgLPneabqbDm7D3m6pNsicvfsIDpP5pQbcV1V2hiaJibOuFOibzwDw2ia4YwqXYhC0hf7W9TMwiclXcOdNLwIAxib2w/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496751&idx=1&sn=37cdb1c9332b0d6171f02836b05d8b31&scene=21#wechat_redirect)[BurpSuite Payload 笔记管理插件，支持自定义二级分类、实时搜索、一键复制

2026-05-07

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMIsZK4u2rCDxbwrxYk6ib5yo7LWIfeMY6bTcXLhKtxhqcwD6jBAkGKvRkHPHzgP8bAXrHBiagZYmTvPygJIZ32YaIGeazIQH5O8Q/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496737&idx=1&sn=1dd956b31bd36ccf856120a5fd2da81f&scene=21#wechat_redirect)[40x 状态码绕过工具，集成多种绕过策略，快速检测和绕过 Web 应用访问限制

2026-05-05

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMLD2kewVseyApAmcSAic5XQzqhB1c5ibzAmOhKQmQ4atiaHZHkR0OuPuax2c31FiavAEFHQsSM6picuaZqeiap4rYiakHYLx5Tia9zyd98/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496731&idx=1&sn=58ce141f4225cb04a0c6608dc12d7a80&scene=21#wechat_redirect)[聚合多源 0day/1day RCE 情报 | 20+ 源 → RCE 过滤 → SQLite 去重 → Telegram 推送

2026-04-29

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLfIGqicl2IsicQR94ibViayxNicWp0yQgCscg6twbLGK44ZmbEmiaPhczCwoPfnjxWgicKwk4rzjEWgicbEqf7iaibExWzdErWkO7euL9vw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496719&idx=1&sn=130193d95498fc287b72babc400045ef&scene=21#wechat_redirect)[AI驱动的渗透攻防武器库

2026-04-28

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMIOW98dqfI9ia5ayDAxoR0cPc22oegpq5gw6qp9HpTo5K7AIuUdmxicoAV159s0HiaXRFYLvR35CWnZLh7eUIHBauYECJeQ5G2UfQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247496714&idx=1&sn=89453f97bf6df0e6e6967af9d4446873&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

夜组安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

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