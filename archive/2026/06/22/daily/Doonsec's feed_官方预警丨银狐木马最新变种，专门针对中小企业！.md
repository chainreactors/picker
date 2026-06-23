---
title: 官方预警丨银狐木马最新变种，专门针对中小企业！
url: https://mp.weixin.qq.com/s/XrqCosxbef-fki68T3fTlw
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:03:28.686344
---

# 官方预警丨银狐木马最新变种，专门针对中小企业！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0Kn2VsOJzu6QwQ4dtsDZGRCReu2hwhxnyQvpYKbyIzalcQ00IqGzFGCE3BWxz9bdTO7dibpRniaJxjRtRGrFNgqW8GWQyjP6gyTBeAGwrDkgU/0?wx_fmt=jpeg)

# 官方预警丨银狐木马最新变种，专门针对中小企业！

原创

深海捕鱼
深海捕鱼

DeepPhish

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/0Kn2VsOJzu4pwjJrd2GDqyA8FmQ6hwDO0SGiaTZuYjE7SPqHuf1AiaiaKDBm4jtWPgSDiaq9yiaYicmaqn5jMbBMzjSewrC1aUNqiaic3AHWb5Fgzn0/640?wx_fmt=png&from=appmsg)

大家好，这里是DeepPhish。

专注反钓鱼实战训练与钓鱼溯源分析，深耕钓鱼攻击全链路拆解、恶意指标汇总与反诈实操科普，帮你精准识破各类网络钓鱼陷阱，守住个人信息与财产安全。

**重点预警！**

公安部网安部门提醒：近日，新型“银狐”木马病毒再次呈现高频活跃态势。

该木马通过批量发送伪装成“税务稽查”“补贴发放”的钓鱼邮件，定向攻击企业财务人员，植入木马后长期潜伏，伪造老板指令诱导对公转账。

据公开资料显示，目前已有1000+企业受害，遭受损失已高达20亿！

并且银狐木马受害者中中小企业占比高达73%！

原因很简单：大型企业往往有专职的安全团队以及完整的应急处理流程。而中小企业的安全防护往往只有一个免费的杀毒软件，非常容易中招！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0Kn2VsOJzu6AX0VTktO8LqAzpwOQzKZC8KkmwSRW7RIiayge9fXbCibL4IgX3icPyicnsxLuwUZb2C3Qz5iaGLws6nT67HGrs7F5zewLPibTBpl8I/640?wx_fmt=png&from=appmsg)

本文将结合近期公开案例，分析银狐木马的攻击特点，并给出防范建议，供安全管理人员与技术人员参考。

**近期案例**

![](https://mmbiz.qpic.cn/mmbiz_png/0Kn2VsOJzu5Pia5saicfdLia6wia1eqJ0KUcbT9qjUlzTcHOgJYXvr0QtdbyDfywJZ4ibxZPO6euhmcUzMYmLhtDDqVTe0sZdBzibsgpRyLlHJfZo/640?wx_fmt=png&from=appmsg)

某外贸公司财务总监收到伪装成“2026年税务稽查通知”的邮件，点击附件后电脑被植入“银狐”木马。

木马截获了银行短信验证码，攻击者通过远程控制，以财务总监的电脑为跳板，分三笔转走公司账户47万元，且银行流水显示为“本人操作”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0Kn2VsOJzu4ias0dwOpCKPCP0YcUFMQ462O6ETPpenbuYhH9Mx8PVQLZMcNAdiawaDTGUsAT6TxMaiawaCGTh6QLpH8t2iamGw8icUS5j5MHTpjQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0Kn2VsOJzu6B7uTsIp5M75lTHwhhxUFhSTicTrI37uibURQiaFdoWoEaLHoeTk2f8qvZiczuQu93noNykLp4qwgF3tul2avVuNiaISReoicO00JuM/640?wx_fmt=png&from=appmsg)

**攻击步骤解析**

![](https://mmbiz.qpic.cn/mmbiz_png/0Kn2VsOJzu5j7kIRfiaO2DCYEfGicP9ZuT9kVWyEZcHZcIG8ibNicajJRXxtl5hJdhCu4UrsVbNonaKk1RPnXgVJN5dTeicEjgHLAbMpqLWQr7WY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0Kn2VsOJzu6e0BXPUJa397w2THylDHa6IUFEvVCoo4g6F80rCnTBKdvr48ibFqiaPkQJNic3I41ic7S1P7pfBZv4abpbSC8l4QpFzFbhXqtEw18/640?wx_fmt=png&from=appmsg)

1、攻击者通过钓鱼邮件、即时通讯平台（如QQ群、微信群）、伪造官网链接等方式进行传播，钓鱼邮件的信息主要为通知、补贴、年末福利、罚单等，诱导潜在受害者点击附件中携带的钓鱼链接。

![](https://mmbiz.qpic.cn/mmbiz_png/0Kn2VsOJzu7tEgmMtkvDwYojkLyoQgnSbuUUj2v4hJBa8rmcAsgZCWwwzfDtxQfnicD4ibAhC0OLHgPQbFS4lK3kaBxcCXyBApaKpsDkCicSGY/640?wx_fmt=png&from=appmsg)

2、用户双击运行恶意文件后，木马会先进行环境检测——判断自己是不是运行在虚拟机或沙箱等安全分析环境中。

如果检测到安全环境，木马会立即终止运行，避免被安全研究人员捕获。只有确认是真实用户环境，才会释放核心恶意代码。

3、木马利用系统漏洞或白名单程序获取管理员权限，然后修改系统安全配置，降低防护等级。

为了保证重启后仍能运行，木马会采用多种持久化技术：修改注册表Run键值、创建伪造的系统服务、添加计划任务，甚至利用WMI事件订阅实现无文件执行。

4、木马通过加密通道连接攻击者的C2（命令与控制）服务器，完成"上线"。此后攻击者可以实时监控屏幕、记录键盘输入、截取屏幕、上传下载文件、远程操作鼠标键盘。

更隐蔽的是，木马还会拦截短信验证码——当你的网银发来验证码时，木马会先一步截获，攻击者可以直接用验证码完成转账。

5、攻击者不仅能窃取用户敏感数据和盗取财务信息，甚至可能将受害者的电脑作为“跳板”，进一步实施精准的网络诈骗。

![](https://mmbiz.qpic.cn/mmbiz_png/0Kn2VsOJzu7jPMxRIzvBuXakOvibssUrWibUgNdpb97A2oHH6cyMQGUktkKGGMm2XFxbT9kNWB00gp7hpskr7aDgtWicRvA79QmTP2bibb4ETdE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0Kn2VsOJzu7ia7qfRG8FZFakqKkY0ficqwNdOXLLvy91sf4rv9wNm8wLJR9qE8CWkKBlgoNFxIbXvz3icFeozPKv5CgIMOYoCQ4sMiaWHp4UbFA/640?wx_fmt=png&from=appmsg)

攻击活动过程示意图

**如何防范？**

**1**

在使用即时通信工具或电子邮件处理工作事务期间，警惕新增临时工作群组和电子邮件中传播的“违纪”“裁员”等相关主题文件，拒绝点击陌生人发送的邮件

**2**

收到可疑邮件时，可将可疑的邮件下载上传至EML邮件安全分析平台（https://deepphish.cn/eml）进行安全检测

![](https://mmbiz.qpic.cn/mmbiz_png/0Kn2VsOJzu57TWTUqMxWOb3RkALMhRQHgeuPau21Nv6wic8qicNXAGc7p3Q3yjibsw5jnGbWS8Iyia4CaW5hG3Ka2Qqmrt9nNMkcNQZQFqcPQEE/640?wx_fmt=png&from=appmsg)

**3**

一旦发现即时通讯工具或者邮箱发生被盗用现象，应立即断网隔离感染的终端，对重要数据进行迁移和备份之后，停用该终端直到进行系统重装或系统还原，通过安全检查后再投入使用。

**4**

定期开展安全意识培训和钓鱼演练，提升全员防范能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0Kn2VsOJzu4CMlhpnzT3IanokzgXJIh5ml6NPI7icOY1g3XeEEsjzYIMo2UjRhdL7uiaDplicVLNbM9kMVQY5nTEwbiaBLtqbcqtiarIDaEJ5C2A/640?wx_fmt=png&from=appmsg)

**DeepPhish反钓鱼训练平台**

以AI赋能实战演练，帮助企业提前发现风险，强化员工安全意识。

* 支持发件人地址任意模拟，钓鱼域名任意模拟；同时包含凭证/数据泄露钓鱼、二维码钓鱼、IM钓鱼等主流网络钓鱼形式。
* 多维度分析报告，量化训练结果，风险状况一目了然。
* 无捆绑，无隐藏费用，无需部署，即开即用。按需订阅，轻量灵活，人均最低仅需¥10/年！

如需试用，请联系官微👇

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0Kn2VsOJzu622hrz2q9eWToFic9mzCGwaVcp3tGltwLQIHzlFqZ9TNYPcCfo2HtfQg7S6RZL24wofUuicIQXrym4WH9OmfM2UX17NvPibibibR98/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/zsIOptmcnRDqJLJxa8tV10QXefJiaS9ebvvlTZ0FgI58kue6VNtRF1OibkZhAYriawOz70J1KIvEvhlkmDpvepJRw/0?wx_fmt=png)

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