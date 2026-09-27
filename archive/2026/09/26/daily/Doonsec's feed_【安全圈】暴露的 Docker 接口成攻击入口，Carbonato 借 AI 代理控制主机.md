---
title: 【安全圈】暴露的 Docker 接口成攻击入口，Carbonato 借 AI 代理控制主机
url: https://mp.weixin.qq.com/s/oMGCudK7VKh40DEKFZu66Q
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:20:42.402895
---

# 【安全圈】暴露的 Docker 接口成攻击入口，Carbonato 借 AI 代理控制主机

# 【安全圈】暴露的 Docker 接口成攻击入口，Carbonato 借 AI 代理控制主机

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

docker漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyFVYV5daibbZULf7UW8CZXEGTuiat8pBuecibywAzUa3bQtVqJKC8gvvuh5fD9cwlHmbQIn4yXvwDUIBiaAO4ofFRy0GIyOiczVepb0/640?wx_fmt=png&from=appmsg)

安全公司 ThreatDown 于 2026 年 9 月 22 日公布了对 Carbonato 的调查。这是一个针对 Docker 主机的僵尸网络：攻击者寻找对网络开放、又没有认证保护的 Docker API，借此让目标主机自行启动特权容器，取得进一步控制能力。

研究人员是在一个无需登录即可访问的 Docker 镜像仓库中发现相关材料的。他们读取到近 60 个仓库、数百个镜像标签和约 4.3 GB 数据。材料涉及两个有关联的犯罪项目，其中之一就是 Carbonato。仓库暴露的规模说明调查证据丰富，并不等于已有同样数量的主机被入侵。

这次攻击的特别之处在于后续控制方式。Carbonato 会安装开源的 Hermes Agent 框架，并替换其指令文件，让它通过 Telegram 接收操作者的任务，维持访问并搜集凭据。Hermes Agent 本身是合法软件；风险来自攻击者在失陷主机上的配置和使用方式，不能因为环境中出现这个包就直接判定中招。

研究报告称，恶意指令把 AI 服务的 API 密钥列为优先收集目标，随后还包括 SSH 凭据、访问令牌和数据库相关秘密。Carbonato 还会扫描邻近网络，寻找更多开放的 Docker 接口。对于把容器平台与生产凭据放在同一台机器上的团队，这意味着一次错误暴露可能延伸到其他系统。

运维人员可先确认 Docker 守护进程是否向不可信网络开放，特别是未加认证的 2375 端口；镜像仓库也应检查访问控制。由于 Docker API 可直接管理容器，开放接口本身就需要优先处理，不能只靠容器内部的应用认证。若发现异常特权容器、无法解释的 Telegram 外联，或 Hermes Agent 的指令文件出现与 Carbonato 相关的内容，应按主机入侵排查，并核查可能泄露的凭据。只关闭暴露端口，不能清除攻击者已经留下的持久化组件。

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