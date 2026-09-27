---
title: 【安全圈】Roundcube 旧漏洞出现实际利用报告，邮件系统需核对版本
url: https://mp.weixin.qq.com/s/1T4B--nSUlb2GhM26Zx9fg
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:20:48.554133
---

# 【安全圈】Roundcube 旧漏洞出现实际利用报告，邮件系统需核对版本

# 【安全圈】Roundcube 旧漏洞出现实际利用报告，邮件系统需核对版本

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyG3JTVDvibAos2SZaNM2seibqOkzTwnfpticfvwVAt9nuniaxwhJOyoibD4l0zGkibn9H4I6pQc1twLaj5ZvwwGhDosg9SaWIianu0wUc/640?wx_fmt=png&from=appmsg)

加拿大网络安全中心在 2026 年 9 月 21 日更新通报称，公开报告显示 Roundcube Webmail 漏洞 CVE-2026-48842 已在真实环境中遭到利用。这个漏洞并非最近才有补丁：Roundcube 项目早在 5 月 24 日发布的 1.6.16 和 1.7.1 中就已修复。

Roundcube 是通过浏览器使用的邮件客户端。CVE-2026-48842 位于其 virtuser\_query 插件，属于登录前可触发的 SQL 注入。简单说，攻击者可能借特制请求让原本只应查询用户信息的数据库操作执行额外语句。前提是目标部署使用了相关插件，且运行的是仍有漏洞的版本；不能把所有部署 Roundcube 的邮件系统都视为同样暴露。

这次需要区分“漏洞已被利用”和“攻击详情已公开”。加拿大网络安全中心引用公开报告指出存在实际利用，但通报没有披露攻击者身份、受害者数量或具体攻击链。也不能把 Roundcube 其他漏洞的入侵案例，直接算到这个编号头上。

对管理邮件系统的团队，第一步是确认实际运行的 Roundcube 分支和版本，以及是否启用了 virtuser\_query 插件。低于 1.6.16 的 1.6 分支和低于 1.7.1 的 1.7 分支包含该问题。由于项目之后又发布了其他安全更新，应结合所用分支升级到当前可用的安全版本，而不是把 5 月的最低修复版本误认为最新版本。Roundcube 的公告列表显示，9 月 6 日还发布了 1.6.19 和 1.7.4 安全更新。

如果实例长期暴露在公网且仍运行受影响版本，完成更新后还应结合 Web、应用和数据库日志查看异常请求与账户活动。更新修复的是漏洞入口，无法单凭版本变化判断历史上是否曾遭利用。没有发现异常也不代表绝对安全，但排查应围绕实际部署与日志证据开展。

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