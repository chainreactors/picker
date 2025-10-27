---
title: 【安全圈】I-O Data路由器0Day漏洞被利用，无修复补丁
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066435&idx=3&sn=bbca90f744a9f08fd2d2e9d95bb190e2&chksm=f36e7ec3c419f7d5cf01456a6710a86aa0232fb64cceceecabeed12a0e2bcb562d4935577983&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-07
fetch_date: 2025-10-06T19:40:14.757268
---

# 【安全圈】I-O Data路由器0Day漏洞被利用，无修复补丁

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgdme7EAeBhHP74oFZvnicp3rr1puwBA5zZbKAsuLmDgePyABZZRwtM2BhXkaUrTkyw4ibdUH4KV9rw/0?wx_fmt=jpeg)

# 【安全圈】I-O Data路由器0Day漏洞被利用，无修复补丁

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

日本计算机紧急响应小组（CERT）警告称 ，黑客正在利用I-O Data路由器设备中的零日漏洞来修改设备设置、执行命令，甚至关闭防火墙。

I-O Data在其网站上发布的安全公告中承认确实存在三个零日漏洞，但目前暂无完整的修复补丁，预计将在2024年12月18日发布，因此在此之前用户将面临比较严重的风险。![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgdme7EAeBhHP74oFZvnicp32VNdIAIibbenMO2AWTvFpCibwc08FDphg2wU3wUXQvuciazB14OedeiblA/640?wx_fmt=jpeg&from=appmsg)

上述三个零日漏洞在2024年11月13日被发现，包括信息泄露、远程任意操作系统命令执行和导致防火墙禁用的漏洞。

具体如下：

* CVE-2024-45841：敏感资源上的不当权限配置，导致低权限用户可以访问关键文件。
* CVE-2024-47133：认证的管理员用户可以在设备上注入并执行任意操作系统命令，利用配置管理中的输入验证不充分漏洞。
* CVE-2024-52464：固件中的未记录特性或后门可导致远程攻击者在无需认证的情况下，关闭设备防火墙并修改设置。

受影响的设备：这些漏洞影响UD-LT1和UD-LT1/EX设备，前者是为多功能连接解决方案设计的混合LTE路由器，而后者是工业级版本。

最新可用的固件版本v2.1.9仅解决了CVE-2024-52564漏洞，I-O Data表示其他两个漏洞的修复将在计划于2024年12月18日发布的v2.2.0版本中提供。比较糟糕的消息是，已经有客户因为这些漏洞而遭到黑客攻击。

I-O Data安全公告指出，“已收到使用混合LTE路由器UD-LT1和UD-LT1/EX的客户的咨询，这些客户报告了来自外部来源的潜在未经授权访问。”

在安全更新发布之前，I-O Data 建议用户实施以下缓解措施：

* 禁用所有互联网连接方式的远程管理功能，包括WAN端口、调制解调器和VPN设置。
* 仅限VPN连接的网络访问，以防止未经授权的外部访问。
* 将默认的“访客”用户的密码更改为超过10个字符的更复杂的密码。
* 定期监控和验证设备设置，以尽早检测未经授权的更改，并在检测到泄露时将设备重置为出厂默认设置并重新配置。

不过国内的企业用户不需要太过担心，因为I-O DATA UD-LT1和UD-LT1/EX LTE路由器主要在日本市场销售，旨在支持NTT Docomo和KDDI等多个运营商，并兼容该国的主要MVNO SIM卡。

参考来源：https://www.bleepingcomputer.com/news/security/japan-warns-of-io-data-zero-day-router-flaws-exploited-in-attacks/

***END***

阅读推荐

[【安全圈】Crypto.com 与 HackerOne 一起推出 200 万美元的漏洞赏金计划](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=1&sn=8b5178681a68125be7487364041e0e92&scene=21#wechat_redirect)

[【安全圈】立即修复，微软驱动程序关键漏洞已被APT组织利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=2&sn=c856137ec845bc74a8a86abc23c1eb69&scene=21#wechat_redirect)

[【安全圈】谷歌浏览器类型混淆漏洞让攻击者能够执行远程代码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=3&sn=28c802936604146904c583d74c14846f&scene=21#wechat_redirect)

[【安全圈】知名伏特加品牌因勒索攻击而倒闭](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066421&idx=4&sn=7bf50178818225897c7e681c7ddab487&scene=21#wechat_redirect)

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

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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