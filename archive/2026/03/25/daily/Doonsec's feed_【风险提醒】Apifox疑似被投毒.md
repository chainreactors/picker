---
title: 【风险提醒】Apifox疑似被投毒
url: https://mp.weixin.qq.com/s/nQuwdQwLHqq-d1Tj5nw97w
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:26:18.846035
---

# 【风险提醒】Apifox疑似被投毒

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icCLY10D8tvLPu6nO6oEF7Jk5p5SqO3RfQJgibibDzYg6v8KSPuYApXwDiaHcDIkibUfBxK7PodqFUydhP6hGGAJKibmgNVK8ZP1gGicHWBWbgpwk0/0?wx_fmt=jpeg)

# 【风险提醒】Apifox疑似被投毒

小叶Sec

![]()

在小说阅读器中沉浸阅读

以下文章来源于好靶场
，作者小王

![](http://wx.qlogo.cn/mmhead/XYrRG5UShDc8MiasaqKIRuv8ygOQeco20z91bZzqSptr4yT8nEmmLBzdFCY6BRHg3fKmcfiafia6cg/0)

**好靶场**
.

学安全要练习，练习就选好靶场。我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。

58.5

💡 好靶场

团队宗旨：我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。所以我们团队名称就叫“好靶场”。

我们承诺每天至少更新1-2个新靶场。我们要的是稳定更新，而不仅仅是堆叠数量。

* • 全球第一家以SRC报告为蓝图制作靶场的网络安全靶场平台。
* • 全球第一家引入AI靶场助教的网络安全靶场平台。
* • 14个不同方向靶场供你选择。
* • 代码审计+漏洞修复靶场全新上架。

* • 无门槛费，每次开启不扣除积分，不扣除金币，超级会员每天不限次数开启靶场。
* • 靶场独立，每个靶场环境完全隔离。

# 好靶场目前进度

797

靶场数量

210个

漏洞报告数量

# 概述

2026 年 3 月曝光的一起**严重级（Critical）软件供应链投毒攻击**，攻击者针对  API 一体化协作平台 Apifox 的桌面端实施入侵，通过篡改其 CDN 上的合法 JavaScript 文件，向  Windows、macOS、Linux  全平台客户端植入恶意代码，实现敏感信息窃取、全量远程代码执行、内网横向攻击等恶意行为。

技术文章参考：https://rce.moe/2026/03/25/apifox-supply-chain-attack-analysis/

# 核心攻击背景

1. 1. **漏洞根源**：Apifox 桌面端基于 Electron 框架开发，未严格启用`sandbox`沙箱参数，暴露了 Node.js API 接口，为攻击者通过 JS 代码实现终端完全控制提供了基础条件，三大操作系统平台均受影响，无平台豁免。
2. 2. **投毒入口**：Apifox 启动时会加载`https://cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js`，该文件正常大小 34KB，2026 年 3 月 4 日后出现被投毒的 77KB 版本，攻击者在合法代码末尾追加了约 42KB 的恶意后门代码。
3. 3. **C2 基础设施**：攻击者使用`apifox.it.com`作为恶意 C2 域名，该域名极具欺骗性 ——`.it.com`并非意大利国别域名，而是不受 ICANN 标准体系监管的商业二级域名服务，注册门槛极低，极易被误认为 Apifox 官方域名；同时域名通过 Cloudflare CDN 托管，隐藏真实源站 IP，恶意流量难以与正常 CDN 流量区分。
4. 4. **攻击活跃窗口**：2026 年 3 月 4 日至 2026 年 3 月 22 日，共计 18 天；截至 3 月 25 日，CDN 入口文件已还原为正常版本，C2 域名 DNS 解析已下线，但源站 IP 仍可响应。

# 关键事件时间线

| 日期 | 核心事件 |
| --- | --- |
| 2026-03-04 | `apifox.it.com` DNS 解析上线，CDN 上的 JS 文件开始被投毒，攻击正式启动 |
| 2026-03-05 | Wayback Machine 抓取并存档了 77KB 的投毒版本 JS 文件 |
| 2026-03-12 ~ 03-20 | 观测到至少 10 次不同的 Stage-2 攻击载荷下发，攻击者持续迭代窃取能力 |
| 2026-03-22 | `apifox.it.com` DNS 记录下线，域名停止解析，攻击活跃期结束 |
| 2026-03-25 | CDN 入口文件还原为正常 34KB 版本，DNS 失效但 C2 源站 IP 仍可响应，技术分析报告发布 |

# 影响范围

* • 2026 年 3 月 4 日之后启动过 Apifox 桌面端的所有用户；
* • Windows、macOS、Linux 全平台用户，无平台豁免；
* • 持有 SSH 密钥、Git 凭证、K8s 集群权限、npm 发布权限的开发 / 运维等高权限用户，为高风险攻击目标。

## 核心风险

| 风险项 | 核心影响 |
| --- | --- |
| SSH 私钥泄露 | 攻击者可直接登录服务器 / 跳板机，实施内网横向移动 |
| Git 凭证泄露 | 源代码仓库未授权访问，可引发更大范围供应链攻击 |
| Shell 历史泄露 | 暴露内部 URL、数据库连接串、API Key、各类 Token 等敏感信息 |
| K8s 配置泄露 | 集群管理权限泄露，可直接接管生产环境 |
| npm Token 泄露 | 可向 npm 仓库发布恶意包，扩大供应链攻击面 |
| Apifox 账户信息泄露 | 攻击者获取用户邮箱、姓名，可实施定向钓鱼与社会工程学攻击 |

# 应急处置与安全建议

1. 1. 立即停用 Apifox 桌面端应用；
2. 2. 全量轮换`~/.ssh/`目录下的所有 SSH 密钥对；
3. 3. 吊销所有 Git Personal Access Token（GitHub、GitLab 等平台）；
4. 4. 轮换 K8s 集群 OIDC Token 与 kubeconfig 凭证；
5. 5. 轮换 npm registry 认证 Token；
6. 6. 修改 Shell 命令历史中暴露的所有密码、Token、API Key；
7. 7. 全面审查服务器登录日志，排查异常 SSH 登录行为。

# 事件总结

这是一起典型的软件供应链投毒攻击，攻击者通过篡改  Apifox CDN  上的合法静态文件，实现了对海量开发者终端的广撒网式入侵。攻击设计精巧，通过多层代码混淆、加密通信、一次性   URL、随机持久化、域名视觉欺骗等多种技术手段，规避检测与溯源，同时具备极强的扩展性，C2 可随时下发任意代码实现深度入侵。

# 好靶场介绍

零基础入门不迷茫！专属网络安全从零到一体系化训练——配套完整靶场+精选学习资料，帮你快速搭建网安知识框架，迈出入门关键一步！

全场景实战全覆盖！聚焦Web渗透工程师核心能力，深度拆解TOP10逻辑漏洞，精通PHP代码审计、Java代码审计等核心技能，从基础原理到实战攻防，覆盖行业高频应用场景！

真实漏洞场景沉浸式体验！src训练专题重磅上线——1:1还原真实漏洞报告，让你亲身感受实战挖洞流程，积累符合企业需求的实战经验！

有宝子就问了，主播主播，这么好的靶场怎么用：

首先关注好靶场

然后发送bug，可以点击链接直接登录

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvve2xib0I0O5XTibibicpcNb2b3lFm6AtzAT4Zl3icT2ticC7icP7kLJahMmgPKc0ecuNcq373kXXsyibplw/640?wx_fmt=png&from=appmsg)

#### 福利1：

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvXVIibapFtib6OxTy5TW0HJdlhE9EIicfBe4AsJUQIJ7IRUs9SB0503rHe4ia5P80habCuCPlUQjEGjA/640?wx_fmt=png&from=appmsg)

找到个人中心，邀请码输入0482d6d28539424c，白嫖14天高级会员。

#### 福利2：

关注好靶场bilibili。拿着关注截图找到客服，领取5积分或者7天高级会员。

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBtNhnwsibMqDG31CpA7qQKa81Ym01iamwlkmxPzLsI73ptEwJ3D0S7ZKTFRDlIrM3iaIiaYcyVtGbMnLw/640?wx_fmt=png&from=appmsg "null")

# ~ 每日限免 ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wWnCm40UQo3upJtdZDSSpMQoxM02icLjFT7FzZzkVMVelrlEDibev1EDaPbiaSTHojEJxOvlvu3Qa6w/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

    为了能让更多的宝子可以免费的开启会员靶场，我们会在工作日随机开放一些靶场的限免，还请加群关注。我们会以如下的方式在群里通知。

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvDtuNKem9kEYXZPnR8icGAXbdy4ibHbWM9Oa1zWDaFBYIribtRB8KQdrAYuYjMxiae2UFx7W8yFsUuGA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvDtuNKem9kEYXZPnR8icGAXDCGrKBD8iaCpACtAn87ncaxPJjhukOmrbQ8F6S7rnLKRsAbMdBgjp7g/640?wx_fmt=png&from=appmsg)

# **~** 内部群 ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wWnCm40UQo3upJtdZDSSpMQoxM02icLjFT7FzZzkVMVelrlEDibev1EDaPbiaSTHojEJxOvlvu3Qa6w/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

加群不收费哈！！！交流群里会每天更新限免靶场，以及免费学习资料。

进一个群就可以，所有的通知都会通知到位

进交流群，请加我好友

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBs73DYicxITQPQsBVqHAu48icqickaJDCvv6zqQdibzakNgCA7NyKdfvJjETfibNQqX9vuPGUUuklGoRQQ/640?wx_fmt=png&from=appmsg)

喜欢玩QQ的宝子们可以加这个QQ群

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvP29u5t2iaAicTeGA9f2DicBU9Fxt45RyGTdjibCHCNIIvwsRrTTL7gLrO9iamaZBtgVibYSFpHsz7uwZQ/640?wx_fmt=png&from=appmsg)

**~**

AI客服内测ing

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wWnCm40UQo3upJtdZDSSpMQoxM02icLjFT7FzZzkVMVelrlEDibev1EDaPbiaSTHojEJxOvlvu3Qa6w/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

可以完成简单的客服能力，以及靶场推荐

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBsOqIxrNhIgec8tYziaickpVF3bHRTPAyaBaMgRPngTVJRmCpApOeNiaiaagJXZXmqRR5WNBbdJTrDtfA/640?wx_fmt=png&from=appmsg)

# 会员订阅

首先点击会员订阅

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvL0lia2u1nNacRPsGManicYyYENDcXMK8JvRKxnLMQ5fRF89GuvgyxnFIcuZBS0SKEFsI0cTo1j9YERW9qad7SjVW1QXqU9o21wQ/640?wx_fmt=png&from=appmsg)

##

## 然后选择对应的套餐

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLZDZP0Aibbr9vaJNcWYkLrhjG6mx2nIlnIVFU4rdQrIZgUx3FjQXMqnCTMRhg5CQmuaAJgSD5X6FkFU5sgj7eNI9wG0tEdSIws/640?wx_fmt=png&from=appmsg)

##

## 选择去支付

##

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvL9MiabG0hFP2WApianrv99EPjziabzLlTt85cW3LTW22jo6HgZibksG59ibwO1F2t2n4Dn5pJO4UbskHnQVjmhCQib7vicCcvsrmjSKA/640?wx_fmt=png&from=appmsg)

##

## 支付完成后即可会员到账

##

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvLiazKvfyEZOMyk1YxDbLU2ZUgLA3vU4W6KOqUiashYibBhzzAt39Z4Or66R7kjUhibXApNUbGaKV60dniaUuCA7edzn1b8Zd2c6duk/640?wx_fmt=png&from=appmsg)

有什么好的建议可以在留言区评论哦

##

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7cwYsJwE4IyPczNesOwRdnluVLvWzdawcOwwibmTlUeEhIhM8kTYj8XgMe87atk9icaFOGu6icVZ09msmzgL2X7ww/0?wx_fmt=png)

小叶Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7cwYsJwE4IyPczNesOwRdnluVLvWzdawcOwwibmTlUeEhIhM8kTYj8XgMe87atk9icaFOGu6icVZ09msmzgL2X7ww/0?wx_fmt=png)

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