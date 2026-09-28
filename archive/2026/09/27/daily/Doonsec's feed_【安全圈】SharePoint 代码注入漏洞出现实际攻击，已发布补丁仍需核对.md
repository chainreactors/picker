---
title: 【安全圈】SharePoint 代码注入漏洞出现实际攻击，已发布补丁仍需核对
url: https://mp.weixin.qq.com/s/SixW81R0v-Pxh255F2cmSQ
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:53:40.007585
---

# 【安全圈】SharePoint 代码注入漏洞出现实际攻击，已发布补丁仍需核对

# 【安全圈】SharePoint 代码注入漏洞出现实际攻击，已发布补丁仍需核对

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyGxXiaaLbCPgQRWS9X46zFWNZWUticApIuPSmYO1RoowVjniad4qcVle5u8OQeqSEjvkE4ExfNCNBPBJmnFLK3qKyZlCJfeY9vKQc/640?wx_fmt=png&from=appmsg)

美国网络安全与基础设施安全局（CISA）在 9 月 25 日将 SharePoint 漏洞 CVE-2026-65660 加入“已知被利用漏洞”目录。微软同日更新安全说明，表示已有可靠证据显示攻击者正在利用这一漏洞。漏洞本身早在 8 月披露并提供修复；本周的新进展是实际攻击得到确认。

该漏洞属于代码注入，影响本地部署的 SharePoint Server。微软当前的描述是：已经取得一定权限的攻击者，可以通过网络利用它执行代码。这里有一个重要前提——它不是任何陌生访问者都能直接远程执行代码的无认证漏洞。攻击者可能需要先获得可用账号或其他初始访问权限，才能进入这条利用路径。

微软最初把这个编号描述为欺骗问题，后来将影响说明调整为可导致远程代码执行。这种修订会改变管理员对补丁优先级的判断。CISA 将漏洞列入目录，也意味着“已有实际利用证据”，但目录本身不代表所有暴露的 SharePoint 都已被攻破。

截至目前，公开材料没有说明攻击从何时开始、涉及多少组织、哪些攻击成功，也没有给出统一的入侵后行为。管理 SharePoint Server 2016、2019 或订阅版的团队，应以微软对应产品的安全更新说明核对安装情况，不要仅凭服务器能正常打开就判断已修复。若服务器尚未更新，先按现有维护流程部署已发布补丁；同时结合账号登录、应用日志和异常进程记录检查是否出现与本次漏洞相关的可疑活动。

没有使用本地 SharePoint Server 的读者，无须把这条消息等同于自己的 Microsoft 365 租户出现同一漏洞。对实际受影响的环境，补丁能阻断已知利用路径；若此前已有入侵迹象，还需按现场证据处理，不能只以安装补丁作为结束条件。

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