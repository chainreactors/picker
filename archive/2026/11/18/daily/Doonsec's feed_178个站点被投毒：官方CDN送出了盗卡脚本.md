---
title: 178个站点被投毒：官方CDN送出了盗卡脚本
url: https://mp.weixin.qq.com/s/ZtEChbf5ms-E_C_pYfremA
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:41:30.066945
---

# 178个站点被投毒：官方CDN送出了盗卡脚本

# 178个站点被投毒：官方CDN送出了盗卡脚本

华盟信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**核心事实**：11 月 16 日 04:21 UTC，BBC 的 Optimizely 项目里第一次出现不属于它的代码。到次日 21:52 UTC，Report URI 检查了 1611 段 snippet，在其中 188 段里找到同一批注入，归属 178 家机构。Optimizely 确认，攻击者利用 Experimentation 的一个漏洞，往客户项目的 Project JavaScript 里写进了恶意 JS。

这段代码由 cdn.optimizely.com 正常分发，带着厂商自己的证书。站点方没有失守，防火墙没有告警，用户浏览器拿到的就是「官方脚本」。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFursAo0XjSCoSZHCfpVMNRAV6DicVYC7SUhlyyzebvSNCW7NNgITQMktsRZ1hcJM3oHxz2hIO0D4IlEvSiacu6jWe8iaR6f4IUqw/640?wx_fmt=other&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1)

## 🎯 投毒位置：Project JavaScript

用 Optimizely Web Experimentation 做 A/B 测试的站点，页面上要加载一段厂商下发的 snippet。snippet 每次客户改配置都会自更新，加载时执行一段叫 Project JavaScript 的自定义代码。

攻击者只改了 Project JavaScript，snippet 的其余部分原样保留。改了配置就把 loader 带下去，一步到位。部分站点把 snippet 放在自己域名下托管，照样中招——内容来自同一个项目。

loader 有三个版本：多数直接加载 `1688360[.]cc/track.js`，一版把这个域名做了 base64，让文本检索搜不到，还有一版内嵌了完整载荷，域名被墙也能跑。

## 🔍 载荷干三件事：换钱包、偷卡、投 iOS 漏洞链

* **加密地址替换**

  ：`track.js` 扫描页面文本、表单、链接、剪贴板和发出的请求，把合法钱包地址换成攻击者的。只替换通过链上校验和、且附近有 wallet / deposit / send 之类付款词的地址。用户从页面复制出去的那一刻，地址已经是别人的了。
* **盗卡模块**

  ：13:43 UTC 加入，抓取站点自有表单提交的卡号、有效期、CVV。它对跨域支付 iframe（Stripe hosted fields、Adyen）里的输入无能为力，只能拿站内表单的明文。
* **凭证外带**

  ：剪贴板或地址替换成功之后，额外上报 cookie 和页面截图。HttpOnly 的 cookie 读不到，其余照拿。
* **iOS 二阶段**

  ：iPhone / iPad 会加载两个 `.icu` 域名上的 `boot.js`，读系统版本后在隐藏 iframe 里开漏洞链：Coruna 打 iOS 13.0–17.2.1，DarkSword 打 iOS 18.4–18.7，iOS 26 只做到采集设备信息。

17:13 到 17:57 UTC 之间，攻击者给所有 iOS 18.6 及以下的访问加了 Coruna iframe，页面每 60 秒自动重载一次去重试利用。这个刷新动作用户能察觉。截至 19:25 UTC，攻击者钱包入账约 7040 美元，全部集中在九个小时内；StepSecurity 对同一批地址的统计是约 6600 美元。两个地址在注入开始前就已经在用，链上看不出哪笔来自受害者。

## 📦 178 家名单：从 CNN 到 Optimizely 自己的登录页

已知受影响的站点包括 CNN、BBC、Zoom、Salesforce、GitLab、IKEA、HSBC、Equifax、Air France-KLM、Ledger、Peacock。Optimizely 自己的官网主页和登录页同样带毒。研究者把这一轮命名为 **OPTIMJACK**。

同源的注入器 `webshell[.]lol` 不是第一次出现。此前它已经借 Kissmetrics、StorifyMe、Minute Media 的脚本落地，最早可追到 9 月 17 日的土耳其站点。也就是说，同一个人或同一个团伙在第三方脚本这条线上已经摸了一个多月，这次撞上了覆盖面更大的 Optimizely。

20:40 UTC 开始批量清理。Smartsheet 的 snippet 清过一次又被重新注入，只是换成了隐藏版本——攻击者在那时仍有写入权限。攻击者是怎么拿到这么多互不相关项目的写权限，Report URI 的说法是「这得 Optimizely 来解释」，厂商公告没提漏洞细节，也没说改了多少个项目、何时修复、是否还留着访问权。

## 🛡️ 用 Optimizely 的站点，逐条核对

* 打开每个项目的 Project JavaScript、每个实验的自定义代码，搜 `1688360`、`atob(`，以及任何不是你写的脚本。`atob(` 这条专门找 base64 版 loader。
* 盘一遍谁能写你的账号：用户、API token、第三方集成，全部轮换凭据。
* 站内表单收卡的，把周一录入的卡号按已泄露处理。
* 没打 HttpOnly 的 cookie 里的 session token 和其他密钥，一并轮换。
* 上 CSP，`script-src` 和 `connect-src` 收紧。放行 cdn.optimizely.com 没有意义——毒就是从那儿来的。`strict-dynamic` 和 `unsafe-eval` 会让载荷在部分站点照样执行。

## 💡 周一点过这些页面的普通用户

* iPhone / iPad 升到 iOS 18.7.3 或更高，或者 26.3 以上。18.6 及以下访问过受影响站点的设备，值得做一次失陷排查。
* 当天付过的加密转账，拿收款地址和你原本要付的地址比一遍。不一致就是被换了。
* 在这些站点刷过卡的，盯着账单。卡号、有效期、CVV 三项齐全的，直接换卡比观察更省事。
* 核钱包地址看硬件钱包屏幕，别对着复制的文本核——剪贴板早就不可信了。

现在干净的 snippet 不代表周一没送过毒。StepSecurity 建议把日志回溯到周一 08:00 UTC，抓取自己下发的每一段 snippet，搜 `1688360`、`.icu`、`track.js`，把 Last-Modified 记下来，再去问 Optimizely 哪些 project ID 被改过、什么时候改的。

文章来源：安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kZ8oAGNeUuj6mOI5YlyeqpmfFDmlWrhDUPtdowLH0Fe1bbFYw5foqQqLA333icDSHCp2490tNgrcOArofX5wjWw/0?wx_fmt=png)

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