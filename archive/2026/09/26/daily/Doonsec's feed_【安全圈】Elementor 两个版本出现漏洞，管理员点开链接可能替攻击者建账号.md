---
title: 【安全圈】Elementor 两个版本出现漏洞，管理员点开链接可能替攻击者建账号
url: https://mp.weixin.qq.com/s/kj60IIrZj23HUUicPxmBtw
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:20:45.450797
---

# 【安全圈】Elementor 两个版本出现漏洞，管理员点开链接可能替攻击者建账号

# 【安全圈】Elementor 两个版本出现漏洞，管理员点开链接可能替攻击者建账号

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyGc99M6s0r7c2AIwm0Imgrb6DWITEm0rWsdh3lUZjzKibyAvTy4dXcJwc8Vn1G8OLqpjVexIib65YDeZoR6PNCDEicm1SV31z6ds4/640?wx_fmt=png&from=appmsg)

漏洞研究平台 Patchstack 于 2026 年 9 月 25 日披露，WordPress 页面构建插件 Elementor Website Builder 的 4.3.0 和 4.3.1 版本存在跨站请求伪造漏洞，编号为 CVE-2026-62062。官方漏洞记录显示，4.3.2 已修复该问题。

攻击场景有一个关键前提：网站中已登录的用户需要打开攻击者构造的链接。若点击者是管理员，在默认安装的站点上，浏览器可能借用其登录状态执行创建用户的请求，给攻击者新增一个管理员账号。攻击者自己无需先登录，但也不能仅凭远程访问就自动取得管理员权限。

跨站请求伪造可以理解为让浏览器在用户不知情的情况下，带着现有登录状态完成操作。Patchstack 分析发现，受影响版本的 Elementor 在处理特定请求时，用过于宽松的地址字符串判断绕过了 WordPress 原本用于防范这类操作的校验。攻击者可以把相关字符串放进链接参数，使其他接口也受到影响。

这不是所有 Elementor 版本都存在的问题。研究报告明确将影响范围限定为 4.3.0 和 4.3.1；插件总安装量超过千万，也不能据此认定这些站点全部受影响。Patchstack 的漏洞说明指出这种问题可能被利用，但截至这份公开材料，并未给出已经发生大规模入侵的证据。

管理 WordPress 站点的团队应核对 Elementor 版本，将上述两个受影响版本更新到 4.3.2 或之后的修复版本，同时查看近期是否出现陌生管理员账户。站点如果有多名管理人员，应把版本核对和账户检查覆盖到实际使用的站点，而非只看插件总安装量。管理员在保持登录状态时，也应谨慎打开来源不明的站点链接。更新可以阻断这条漏洞利用路径；如果已有陌生账户，还需要另行核查其活动。

***END***

阅读推荐

[【安全圈】MikroTik 路由器曝高危攻击链：无需密码即可取得管理权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079107&idx=1&sn=5712944c4f810ffca0d15071dc160407&scene=21#wechat_redirect)

[【安全圈】恶意软件混入 Terraform 插件，基础设施部署依赖成攻击入口](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079107&idx=2&sn=ea4ee6438b9b45eeb555d7995bd16de6&scene=21#wechat_redirect)

[【安全圈】开发文档里的示例域名被用于攻击，假人机验证诱导执行命令](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079107&idx=3&sn=27c8b75a75e32d9b0ea12450dc4c2a94&scene=21#wechat_redirect)

[【安全圈】微软确认9月更新致Win11断网：Always On VPN遭端口占用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079096&idx=1&sn=c04a8ea82c6ab3cff736ca5a7c0769ff&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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