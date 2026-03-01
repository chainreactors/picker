---
title: 5天，100+ CVE，0误报：我们用自研AI挖掘引擎重新定义了白盒漏洞挖掘
url: https://mp.weixin.qq.com/s/bJnwgw2e7YN6gr9fbWFgDQ
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:22:50.070526
---

# 5天，100+ CVE，0误报：我们用自研AI挖掘引擎重新定义了白盒漏洞挖掘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kMicrkibFtl0JUaG3mJFYTpEdsSNatpicfa9jEMdXrLWV819HPn0yXeSibSu4z4sN6EDyk7faeKEzwDcM0r9MRuicXQBHGfZwTdS2qPURBCWcDm8/0?wx_fmt=jpeg)

# 5天，100+ CVE，0误报：我们用自研AI挖掘引擎重新定义了白盒漏洞挖掘

原创

秋风
秋风

北京秋风代码科技有限公司

![]()

在小说阅读器中沉浸阅读

过去这一周，我们做了一件有意思的事——

**用自研的AI漏洞挖掘引擎，在5天时间内，对80个GitHub 10K+ Star的顶级开源项目进行了安全审计，成功挖掘出80+高危/严重级别漏洞。**

## 已获分配CVE编号的项目

截至发文，以下项目的漏洞报告已通过审核并获得CVE编号：

| 项目 | CVE编号 | 严重程度 |
| --- | --- | --- |
| **SillyTavern** | CVE-2026-26286 | HIGH |
| **Plane** | CVE-2026-27705 | MEDIUM |
| **Mautic** | CVE-2026-3105 | HIGH |
| **Pimcore** | CVE-2026-27461 | HIGH |
| **Actual Budget** | CVE-2026-27638 | HIGH |
| **BentoML** | CVE-2026-27905 | HIGH |
| **NocoDB** | CVE-2026-28399 | MEDIUM |
| **Coolify** | CVE-2026-27883 | HIGH |
| **Gotenberg** | CVE-2026-27018 | HIGH |
| **Unkey** | CVE-2026-28339 | MEDIUM |
| **Piwigo** | CVE-2026-27634 | CRITICAL |
| **Pixelfed** | CVE-2026-27011 | HIGH |
| **Follow (Folo)** | CVE-2026-27499 | HIGH |

###

其余漏洞仍在项目方审核流程中，将陆续公开。部分已关闭的报告属于项目不再维护或正在修复中的重复提交，**没有一例是因为误报被拒。**

并且还出现了报告质量较高获得开发者称赞的情况：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMicrkibFtl0LfnIGiah19uEy2miaxNEZTj0oc9kmW3pgZqQaMRzibEkE4flIsW25Z7z3TicNTw9hVB1MibTgezmRWMVFXDDqxU1KQ9xicXJb8HB0rY/640?wx_fmt=png&from=appmsg)

从已公开详情的漏洞可以看出，引擎的能力覆盖了多种高危漏洞类型：

**SQL注入** — Mautic、Pimcore中的SQL注入漏洞，分别涉及ORDER BY方向参数和未过滤的筛选值，这类漏洞隐藏在业务逻辑深处，传统扫描器极难发现。

**SSRF（服务端请求伪造）** — SillyTavern的资源下载功能存在SSRF，攻击者可借此访问内部服务和敏感资源。

**IDOR（越权访问）** — Plane的资产修改接口和Paperless-ngx均存在越权问题，后者还叠加了Jinja2沙箱逃逸，可能导致远程代码执行。

**授权缺失** — Actual Budget的同步接口完全缺少鉴权，任何人都可以直接访问用户财务数据。

**协议绕过** — OpenClaw的浏览器导航守卫存在协议绕过，可被用于恶意跳转。

大家可以持续关注我们把面板公开在了:https://tracker.dmsec.cn/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMicrkibFtl0I0wusjDUicG4HzTScsAWUWv4FPLn19FZxyLa2UDuOhY7vfyTTug9IVUDO4mYCnfjicAknIic67aCYxm7eFDlSFlHZOkrHDjWdKT0/640?wx_fmt=png&from=appmsg)

当然了 这个项目在当前时代的背景下已经OUT了 我们目前在做另外两个研究并会逐步公开，敬请期待~

# 联系我们

https://www.dmsec.cn

地址：国家网络安全产业园区（通州园） 北京市通州区西集镇网安园创新中心1号-334

联系电话:17896065108

技术支持邮箱:glna9n@163.com

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wnj1L9iaEjqZelFFhicpicQ1rj761wCprU6lnVknDVepp4PAHAQmPeJYk2axIMdT27gpQHXL5ohfhM3SAIIiaKU2VA/0?wx_fmt=png)

北京秋风代码科技有限公司

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wnj1L9iaEjqZelFFhicpicQ1rj761wCprU6lnVknDVepp4PAHAQmPeJYk2axIMdT27gpQHXL5ohfhM3SAIIiaKU2VA/0?wx_fmt=png)

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