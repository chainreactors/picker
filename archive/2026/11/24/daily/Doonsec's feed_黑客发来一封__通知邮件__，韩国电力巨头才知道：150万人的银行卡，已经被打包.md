---
title: 黑客发来一封\"通知邮件\"，韩国电力巨头才知道：150万人的银行卡，已经被打包
url: https://mp.weixin.qq.com/s/xCdcSqX3yX4A9J387nfQwA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:38:34.284694
---

# 黑客发来一封\"通知邮件\"，韩国电力巨头才知道：150万人的银行卡，已经被打包

# 黑客发来一封"通知邮件"，韩国电力巨头才知道：150万人的银行卡，已经被打包

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

▍一分钟读懂本文

一家掌管全国电网的韩国国企被黑客入侵，150 万人的身份证号、银行卡号和账单被打包带走。最荒诞的是——公司是从黑客发来的一封"通知邮件"里，才知道自己被偷了。本文复盘事件经过，拆解那道"分开保存"的墙为何没挡住，以及这件事离普通人到底有多近。

📖 字数 **约 1600 字** ⏱ 阅读时长 **约 4 分钟** 🔑 关键词 **数据泄露 · 关键基础设施 · 钓鱼诈骗**

先看一封信。

2026 年 11 月 19 日，韩国电力公司一个高管收到封邮件，陌生人发的，就一句话：你们的数据在我手上。

没有勒索弹窗，没有告警，没有半夜打来的电话。一家管着全国电网的公司，是这么知道自己被黑了的——**黑客写信来告诉它的**。

我看到这条新闻愣了一下。不是因为 150 万这个数，现在泄露动辄千万，数字大了反而没感觉。让我愣的是那封信。被偷了家，事主是收到小偷的短信才知道的。

**侮辱性有点强。**

## 一、被打包带走的，是 150 万个人的什么

攻击进了两个系统，一个是缴电费的 **KEPCO ON**，一个是供应商投标用的 **SRM**。

| 谁 | 多少人 | 丢了什么 |
| --- | --- | --- |
| 缴电费的客户 | 650,487 | 姓名、居民登记号、电话、住址、银行、账号、卡号、账单 |
| 投标的公司代表 | 426,827 | 姓名、居民登记号、邮箱、公司地址 |
| 员工和供应商的人 | 442,934 | 姓名、单位、工号、手机号、邮箱 |

一百五十多万，是这三拨人加起来的数，没去重，真人可能少一些。公布时用的是大的那个。

我盯着第一行看了半天。居民登记号相当于咱们的身份证，账号、卡号、账单全在里面。**这哪是名单，这是一份能直接照着骗的画像。**你每个月交多少电费，对面都知道。

后面两类人还多了个邮箱。供应商的对接人，邮箱旁边挂着身份证号和公司地址；做采购的，邮箱旁边是工号和手机号。这不就是现成的剧本吗——冒充采购办公室发封邮件，引一个真实存在的招标项目，请你"更新一下收款账户"。钱就这么没了。

## 二、比被偷更丢人的，是事后怎么圆

时间线拉出来，挺尴尬的。

**19 号**　黑客在暗网吆喝卖货，同一天，公司收到那封邮件。

**20 号**　公司才"确认信息被暴露"。

**22 号**　发公告。

数据什么时候丢的、怎么丢的，自己不知道，是黑客和暗网替它把这事定了性。

更绝的是有记者追问：怎么进来的？

回答是，"先进技术，比如 AI"。然后就没了。入口在哪，链条怎么走，一个字不说。AI 替它把锅背了。

我看到这儿有点乐。AI 要是能开口，估计得说一句：别啥都往我身上推。

还有一件事。七周前，这公司刚漏过一次，大概两万四千个员工的信息。那会儿它专门强调，客户数据分开存的，没事。**这次漏的，恰恰是客户。**

那道"分开存"的墙，到底立没立，是个问题。

## 三、电网没停电，但 150 万个钱包被抄了

公告里有句安抚：电网的运营控制没受影响。

这话不假。但读着不是滋味。

人家没去拉闸，没碰调度系统，直接把一百五十万人的身份证和银行卡搬走了。**电网的闸门是守住了，普通人的钱包被翻了个底朝天。**

而且泄露从来不是结束，是开始。

往后你可能会收到条短信，"电费退款到账，点此确认"，对方能报出你的客户编号、你的银行、你上个月交的钱。你说你点不点。

韩国那边已经放话，查实了从严罚，公共部门反复出事的罚款上限，从 20 亿提到了 50 亿韩元。

## 四、说三句实在的

一两句就够，我说三句。

**给企业的：**KEPCO 道歉里自己漏了底，"部分为便利而提供的功能，成了攻击目标"。简化认证、开放接口，用起来是真方便。方便的那扇门，别人也能进。身份证号、银行卡这种东西，干嘛非要放在一个面向所有人的缴费页面上？

**给做安全的：**别光盯着自己的仪表盘。最早发现出事的，有时候是客服的投诉、黑客的邮件、暗网上挂出来的样本。收件箱也是告警源。

**给普通人的：**验证码不外借，陌生链接和来路不明的 App 不点，凡是让你改收款账户的，拿自己存的号码打回去问。就这几条，真到那份上能救命。

电网的闸门守住了。

那一百五十万人的钱包闸门，谁守？

泄露的终点不是通报发出那天。是很多天后，一个陌生人打电话过来，准确叫出你的名字、报出你的卡号，然后说：需要核实一下您的信息。

到那一下你才知道，那一百五十万人里，有没有你。

end

![](https://mmbiz.qpic.cn/mmbiz_png/zj5ibzxuvcrWv3RVy2Hd2kRCbExIoc2KiaKhy9wibOMxXx7JOSlCKbhvCiaJfO7xrtjRCIPWmH3RlO9Og5QxTOlLjg/640)

[网络安全行业变天了：大厂难熬，小厂突围](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494243&idx=1&sn=3c0f0b23c09f6e4174d40db3b6cc52ea&scene=21#wechat_redirect)

2026-11-21

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibT0thjyleA2OjGRZnzvsrNJ53jwMac2ibrelycbF6Sicrks6kSSrbHfR0ibibRbTuT6DTdicuPpIDQPpOG1GdxbNFRhW2QqM3JMUgAE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494243&idx=1&sn=3c0f0b23c09f6e4174d40db3b6cc52ea&scene=21#wechat_redirect)

[Java底层漏洞引爆风险：Jira、Jenkins、Keycloak等应用面临无认证远程代码执行威胁](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494237&idx=1&sn=976f0a2e083a681febd4cd778bbcf010&scene=21#wechat_redirect)

2026-11-19

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibQBpl6X6PErFfjpSE2l3rKfjYtmiaawEJ79QgnwUOvL3JvEjuvF5CxBdrluJHLWXiatyNictJkZEcok4OHvYqV86I8roEyfHe0NFA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494237&idx=1&sn=976f0a2e083a681febd4cd778bbcf010&scene=21#wechat_redirect)

[德国军用无人机遭网络攻击：一次软件更新，差点让战场装备停摆](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494232&idx=1&sn=c2bd8caf118aa725c1ff0cb86f6f24d1&scene=21#wechat_redirect)

2026-11-17

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibTiaZpaVSBfbybamzviaNX9ZPOIQvibLhdfEpNYZibCtqmWTJhOIVYCfYUnUcibicQzHFsfib4ZF4icTTiaaPYGb9FTM8GW3N0icWs0W2qJs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494232&idx=1&sn=c2bd8caf118aa725c1ff0cb86f6f24d1&scene=21#wechat_redirect)

[朝鲜黑客用AI冒充熟人，4亿美元加密货币被盗：视频会议也不可信了](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494226&idx=1&sn=8b4314e23efe39b65f798a479146196c&scene=21#wechat_redirect)

2026-11-16

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibRlzT5X6HufQicrtxtNDoanhjpicZR59cvRnUFuBmN7ZXBLkv5lWJdHRK8PBxQgWPw6jLhgknrTdC864K6IHooRufHXTvmvTBOp0/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494226&idx=1&sn=8b4314e23efe39b65f798a479146196c&scene=21#wechat_redirect)

[OpenAI放出安全大招：AI自己找漏洞、写补丁，但最后一步依然交给人](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494221&idx=1&sn=897f6cb684141b3e2f4249d816d62b3e&scene=21#wechat_redirect)

2026-11-15

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibTPKZDaNicNGib7xb7ZBvjDMhVCByT0kOSlGPq141JmQpNjLngXibSVDX98dK17ctG9yVk5NH3dPib6yDBvEKe5wFNDEMN2dL8RgBc/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494221&idx=1&sn=897f6cb684141b3e2f4249d816d62b3e&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过