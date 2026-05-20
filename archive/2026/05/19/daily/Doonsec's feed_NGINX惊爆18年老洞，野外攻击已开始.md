---
title: NGINX惊爆18年老洞，野外攻击已开始
url: https://mp.weixin.qq.com/s/f1Nny-9ii9pS3RKpmsoStA
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:00:43.254240
---

# NGINX惊爆18年老洞，野外攻击已开始

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH2rSL7SADibtHQ5HKSE9ytf3IIRPhYcz5CwzzE2KgX0iaPdkY5ZwG1icyyU90CwibVzSXdEzSxATCQPK2PicWAiacOGnxD43Byn0Qu0o/0?wx_fmt=jpeg)

# NGINX惊爆18年老洞，野外攻击已开始

原创

安全客
安全客

安全客

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日，威胁情报公司VulnCheck披露，NGINX的一个高危漏洞（CVE-2026-42945）已被野外攻击者武器化利用。这个堆缓冲区溢出漏洞潜伏在NGINX代码库中长达18年之久，CVSS 4.0评分高达9.2，影响NGINX 0.6.27至1.30.0的全版本范围。

事件概述

CVE-2026-42945隐藏在NGINX Plus和NGINX开源版本的ngx\_http\_rewrite\_module模块中。据安全公司Depthfirst分析，该漏洞最早引入于2008年——也就是说，它在NGINX代码库里存在了整整18年，从未被发现。

VulnCheck的蜜罐网络已检测到针对该漏洞的真实攻击尝试。攻击者通过构造恶意HTTP请求触发漏洞，探测到目标后直接投递Webshell。

从漏洞公开披露到野外武器化，仅过去数天时间。

漏洞技术细节

1.影响范围

NGINX Plus及NGINX Open Source 0.6.27 ~ 1.30.0全版本。

2.攻击条件

* 无需认证，远程即可触发
* 通过构造恶意HTTP请求实现
* 需要特定NGINX配置可被利用
* 攻击者需知晓或探测到目标配置

3.潜在影响

* Worker进程崩溃：可直接导致服务拒绝（DoS）
* 远程代码执行：在ASLR被关闭的系统上可执行任意代码

安全研究员Kevin Beaumont指出，触发RCE需要同时满足两个条件：默认NGINX配置+系统关闭ASLR。AlmaLinux维护团队也表示，在默认配置下，将堆溢出转化为可靠的代码执行"并非易事"。

但维护团队同时强调："并非易事"不等于"不可能"。仅DoS层面的利用已经足够构成紧急威胁。

安全观点

1.基础设施的"暗债"比想象中大

一个18年前的漏洞，影响全球数以百万计的NGINX实例。即使是经过最严格审查的开源基础设施组件，也可能存在长期未被发现的深层缺陷。"成熟稳定"不等于"没有问题"。

2.武器化窗口期正在急剧缩短

从漏洞披露到野外攻击，这次只用了几天。攻击者对高危漏洞的响应速度和防御者一样快——甚至更快。补丁发布后的"黄金修复窗口"不再是几周，而是几小时。

3.纵深防御不能依赖单一机制

ASLR确实提高了RCE的利用门槛，但DoS攻击在ASLR开启的情况下依然有效。把某个安全特性当成唯一防线，本身就是风险。安全设计应假设每一层都可能被绕过。

4.版本更新需要制度保障

很多组织的NGINX版本可能几年没动过。建立基础设施组件的版本追踪和定期更新机制，远比等到9.2分的漏洞出现在野外时紧急响应要有效得多。

修复建议

版本升级：升级NGINX最新版本

检查配置：审查ngx\_http\_rewrite\_module相关配置

开启ASLR：确保系统地址空间布局随机化已启用

部署WAF：配置规则拦截已知exploit特征

临时缓解：对无法立即更新的系统，考虑临时禁用rewrite模块相关功能

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/o0buL62hK7M8RnVz7mqRVDRkqm2sJeT2icM4WyR7kMkHpLVaicR3tJ4gr5kIb4zje9lXgd5PuOw42Z5KtathltcQ/640?from=appmsg)

**END**

推荐阅读

[深度分析Sorry勒索软件的加密实现与行为特征](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649789890&idx=1&sn=7105facbd94397f0277f8dda2ce10396&scene=21#wechat_redirect)

2026-04-29

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH1VZR2mRpXQJ6nyj7FkNQv1iaZicMn7JcZzmRAVkBmxfgoamTtxZBV9gVKoeENbTj4v7AlID1SnU1ZObabAlbHC6F8JJ9icKWpuDo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649789890&idx=1&sn=7105facbd94397f0277f8dda2ce10396&scene=21#wechat_redirect)

[全国50城巡装过半！无锡龙虾x漫剧大会落幕，AI普惠深耕长三角](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649789851&idx=1&sn=084dff75c5ce41928430748742042dcf&scene=21#wechat_redirect)

2026-04-11

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH28wNSULcxtdjzvWCeFMuDvdVBfd1yib1emJXvoqFmfk16Y2ibJ45CaFEAOlkBLF4QHz80GJMrEYgNwA6IGrvY8lpq7XibH3aRCTs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649789851&idx=1&sn=084dff75c5ce41928430748742042dcf&scene=21#wechat_redirect)

[关于防范OpenClaw（“龙虾”）开源智能体安全风险的“六要六不要”建议](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649789738&idx=1&sn=4e3ed29738d838c58b06deb23e7d23fa&scene=21#wechat_redirect)

2026-03-12

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH3xzBWUz2TNg9lHeCX5rTHLFAF9jmfPRrphtAiaBT9NT6EibvfAfWynyC3iaAeH6oBR3HibRfxrCDfn07pnZpgMUylNmtENdJqBicPg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649789738&idx=1&sn=4e3ed29738d838c58b06deb23e7d23fa&scene=21#wechat_redirect)

[258 个漏洞，你的 OpenClaw 真的安全吗？](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649789738&idx=2&sn=122e85b5b8a505c14a1dbeb853ab860e&scene=21#wechat_redirect)

2026-03-12

[![](https://mmbiz.qpic.cn/mmbiz_jpg/dZ7ia5iaWFzzicSAskoVZicR7qqRUIf0gRZHhsr5CC5Ciam9NNr1VH8B85xw3zpBF5MicZFsq9Z3lOrnbzbAKQ1UwK95XGQsCQSLKtMQGlNtGUC2o/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649789738&idx=2&sn=122e85b5b8a505c14a1dbeb853ab860e&scene=21#wechat_redirect)

[OpenAI发布应用安全智能体：可自主发现、验证并修复漏洞](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649789723&idx=1&sn=864d06bec8122f6ed8a2dd34d43c29f7&scene=21#wechat_redirect)

2026-03-09

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH3xtqTdvMIGhtFdHEl7jL1Js4xQIfRmy3jFMgV1oyUWpApuVyjb0iaTIjibhDYYNkXFOa1icrf0WKkVB3wI38JiacdgLFwXb2xlDT0/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649789723&idx=1&sn=864d06bec8122f6ed8a2dd34d43c29f7&scene=21#wechat_redirect)

预览时标签不可点

内容含AI生成图片

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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