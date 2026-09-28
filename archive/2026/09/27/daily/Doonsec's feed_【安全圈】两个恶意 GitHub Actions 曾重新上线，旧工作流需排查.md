---
title: 【安全圈】两个恶意 GitHub Actions 曾重新上线，旧工作流需排查
url: https://mp.weixin.qq.com/s/qOmKGxp8i6icDe8scfPZaw
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:53:37.368759
---

# 【安全圈】两个恶意 GitHub Actions 曾重新上线，旧工作流需排查

# 【安全圈】两个恶意 GitHub Actions 曾重新上线，旧工作流需排查

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意代码

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyFoy4bFM3IJtl1OEDGeicsDzLCzLsGAOeO0lhPRRPlMhicBB37Nyfj9ra1Vvu5orlyic4hq5je9ZIyPIJEibzMae4NW3L2EoXeR2t4/640?wx_fmt=png&from=appmsg)

安全公司 Socket 在 9 月 24 日披露，两个曾卷入 Mini Shai-Hulud 供应链攻击的第三方 GitHub Actions，在被停用数月后重新开放访问，却仍保留指向恶意代码的版本标签。它们分别是 actions-cool/issues-helper 和 actions-cool/maintain-one-comment，常被项目用于自动处理问题和评论。

这次风险并非攻击者又发布了新版本。恶意内容在 5 月已进入这两个仓库，随后仓库被停用，依赖它们的工作流因此无法下载代码。Socket 观察到，仓库于 9 月 16 日再次可用，而标签并未清理。引用这些标签的工作流只要再次运行，就可能把原有恶意代码下载到构建环境执行。Socket 于 9 月 25 日更新称，两个仓库已再次被禁用。

需要区分“依赖”与“实际受害”。Socket 统计，仅 issues-helper 就有约 1.5 万个下游仓库，但尚未确认其中多少仓库使用了受污染标签、在重新开放期间运行过工作流，更没有据此给出已泄露密钥的总数。风险集中在 9 月 16 日至再次禁用之间，且取决于具体引用方式和工作流拥有的权限。

GitHub Actions 是自动构建和发布过程中运行的外部代码。版本标签可以移动，因此工作流文件看起来没有变化，实际下载的代码却可能变化。如果工作流向第三方 Action 提供了仓库令牌、发布密钥或云平台凭据，这些信息就可能暴露在受污染的运行环境中。

维护者可检查工作流是否引用上述两个 Action，回看相关时间段的运行记录和可访问的密钥。对确实运行了受污染标签的工作流，应按其实际权限更换可能暴露的凭据，并移除该依赖或改用已核实干净的固定提交。仅看到“约 1.5 万个依赖仓库”，不足以断言自己的项目已经被入侵。

***END***

阅读推荐

[【安全圈】暴露的 Docker 接口成攻击入口，Carbonato 借 AI 代理控制主机](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079118&idx=1&sn=c15dc9fe4166f047f1ddffafc639e2e0&scene=21#wechat_redirect)

[【安全圈】Elementor 两个版本出现漏洞，管理员点开链接可能替攻击者建账号](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079118&idx=2&sn=07a85f3f5a44eccdf34f8f69a44142ec&scene=21#wechat_redirect)

[【安全圈】Roundcube 旧漏洞出现实际利用报告，邮件系统需核对版本](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079118&idx=3&sn=34002ec3d4c40f3f8b2224c5576bbfa3&scene=21#wechat_redirect)

[【安全圈】MikroTik 路由器曝高危攻击链：无需密码即可取得管理权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079107&idx=1&sn=5712944c4f810ffca0d15071dc160407&scene=21#wechat_redirect)

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