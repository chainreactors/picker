---
title: 网络安全最大的敌人，可能不是黑客，而是形式主义
url: https://mp.weixin.qq.com/s/G454ieNqxeJOqw5weB_a0A
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:07:56.630437
---

# 网络安全最大的敌人，可能不是黑客，而是形式主义

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XpPOHs6ZLMHAeSU0FLhFaj7KzAvLGcqjFLkPCQ8LVgQ0aMFwJicATjianwlfm7bsuhnwNlj8BzicJI7tTiadv94fLicibgXI4UMdQMpzJIq8J5l4E/0?wx_fmt=jpeg)

# 网络安全最大的敌人，可能不是黑客，而是形式主义

原创

Caigensec
Caigensec

菜根网络安全杂谈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GagrLP56FibVwx4hfFezZXyhDATCQtibMyLqTzMlb8DXuhXPvQ2pwyG7UsYv9As6Ujffp9g7wiaDVBNo4ncIghIkA/640?wx_fmt=png)

点击上方蓝字关注我们

![](https://mmbiz.qpic.cn/mmbiz_png/Rw1GYXElC3fsz3fQsXSqeO7MgiamgBtBjFwpXTXJkafnVYDcxTe2VibnQPWsmZnoiaLeOzRqf8pgRsA8d7gsEMDhQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ick6R1E3YokGa1ibCe5rpdRyAoBRvrYqueA3wY9CwYuRkqG2lE5MctQus6KVY2uic2Kj03Cf6xiaQHzOjibL8QJTomw/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

![](https://mmbiz.qpic.cn/mmbiz_gif/Sg02xflJ62rdxefX9thdaL8hxJWicY1vPlEmzNIWcBy2ypXTggHXX9e0kFDEVicficwTDdlLHLNrh6ica1SEvMqKeQ/640?wx_fmt=gif)

免责声明：本公众号尊重知识产权，如有侵权请联系我们删除。

作者寄语：

我是菜根（Caigensec），也是本公众号的运营人。说起来有点惭愧，我不是什么安全大牛，也没有显赫的履历。写这个专栏的初衷很简单，把自己在网络安全这条路上摸爬滚打的经历和思考记录下来。

水平有限，难免有疏漏之处，欢迎大家指正交流。毕竟在网安这个领域，我们都是一边学习一边成长。

提到网络安全，人们首先想到的往往是APT攻击、勒索软件、供应链投毒、0day漏洞，仿佛最大的威胁永远来自外部黑客。

但在很多企业里，真正长期削弱安全能力的，未必是攻击者，而是一种更隐蔽、更顽固的问题，形式主义。

它不像勒索病毒那样让系统瞬间瘫痪，也不像数据泄露那样迅速引发舆论风暴。它更像一种慢性疾病，缓慢侵蚀组织的判断力、执行力和风险感知能力。

最危险的是，它让企业看起来很安全，并且真心相信自己已经安全。而这，比真正的不安全更可怕。

01

安全最大的幻觉，做了很多，就等于很安全

![](https://mmbiz.qpic.cn/mmbiz_png/1BiahkUNKiclteCuCXiaCW4UMxvnLW4rTb6NTKnUoGsLbztIoJUj2t9ttkcdhm6ryDTH9k9b8uyl7Tj9Rf3PaWMYA/640?wx_fmt=png)

很多企业判断安全水平的方式很简单，买了防火墙、WAF、态势感知平台，通过了等级保护测评，做了年度攻防演练，建立了制度和流程，上线了SOC、SIEM、威胁情报系统。

于是得出结论，我们已经具备了成熟的安全能力。

但现实往往是，高危漏洞长期无人修复，弱口令依旧存在；权限体系混乱，攻击面大量暴露；日志采集了，却没人真正分析；告警产生了，却没人及时响应；制度写得完整，却没人持续执行。

问题不在于没做，而在于用完成动作，代替解决问题，这正是形式主义的本质。

02

最常见的网络安全形式主义

![](https://mmbiz.qpic.cn/mmbiz_png/1BiahkUNKiclteCuCXiaCW4UMxvnLW4rTb6NTKnUoGsLbztIoJUj2t9ttkcdhm6ryDTH9k9b8uyl7Tj9Rf3PaWMYA/640?wx_fmt=png)

## **0x01、合规替代安全**

这是最普遍的问题。很多企业把等级保护、审计检查、监管要求，当作网络安全工作的终点。安全团队的核心任务，变成准备材料、完善文档、迎接检查。

于是出现一种荒诞现象，文档比系统更安全。制度里写着禁止弱口令，现实中admin/admin仍在使用；制度里要求定期修复漏洞，现实中高危漏洞半年无人处理；制度里有完整应急预案，真正出事时却没人知道先找谁。

通过测评，并不等于具备防御能力。攻击者不会因为你合规就停止攻击，如果安全工作的目标只是顺利通过检查，那本质上做的不是安全，而是应试。

## **0x02、买系统，不等于有能力**

许多企业遇到安全问题的第一反应是买设备。

漏洞多，买扫描器；告警多，买SIEM；响应慢，买SOAR；云上风险多，买云安全平台。

最后系统越来越多，架构越来越复杂，预算越来越高，但真正的结果却是告警爆炸，运维负担加重，一线人员疲于应付，真正风险依旧存在。

安全建设逐渐变成采购行为，而不是能力建设。本质上，这是用复杂性掩盖无效性。安全不是缺一套系统，而是缺真正能持续运转的治理机制。

## **0x03、攻防演练异化，安全版的临时突击**

每年护网期间，很多企业都会进入高度重视状态，临时封端口、临时改密码、临时值守、临时拉群、临时加班。

护网结束后，一切恢复原样。这不是安全建设，而是一次年度表演。

真正的安全能力，应该体现在平时无人关注的时候，而不是检查来临之前。如果一个组织只有在被盯着时才开始重视安全，那它建设的不是防御能力，而是应试能力。

03

为什么形式主义如此顽固

![](https://mmbiz.qpic.cn/mmbiz_png/1BiahkUNKiclteCuCXiaCW4UMxvnLW4rTb6NTKnUoGsLbztIoJUj2t9ttkcdhm6ryDTH9k9b8uyl7Tj9Rf3PaWMYA/640?wx_fmt=png)

因为它符合组织管理的现实逻辑。老板更容易看到买了什么设备，花了多少预算，完成了多少整改项，却很难量化少发生了一次攻击，少损失了一次数据泄露。

安全最大的价值，恰恰在于什么都没有发生。而没有发生，最难被证明。再加上安全部门天然是成本中心，无法像销售一样直接证明收益，于是越来越多的安全工作开始追求可展示性，大屏比闭环重要，PPT比能力重要，采购比治理重要。

形式主义因此变得合理，甚至高效。

04

安全的本质

![](https://mmbiz.qpic.cn/mmbiz_png/1BiahkUNKiclteCuCXiaCW4UMxvnLW4rTb6NTKnUoGsLbztIoJUj2t9ttkcdhm6ryDTH9k9b8uyl7Tj9Rf3PaWMYA/640?wx_fmt=png)

成熟的安全体系关注的，不是能不能完全挡住攻击，而是攻击面是否持续减少，权限是否不断收敛，漏洞修复是否形成闭环，异常行为是否能更早发现，响应和恢复时间是否持续缩短。

也就是说，安全的核心，不是拥有多少工具，而是组织是否具备面对失败后的恢复能力。这才是真正的安全韧性。

网络安全最危险的状态，不是被攻击，而是组织失去了对风险的敬畏。形式主义最可怕的地方，不是浪费预算，而是让所有人相信我们已经足够安全了。于是没人再追问，为什么漏洞一直存在，为什么告警没人处理，为什么制度没人执行，为什么同样的问题年年重复。

真正成熟的安全团队，不是最会写报告的团队，也不是设备最多的团队，而是那个始终敢于面对真实问题、持续解决真实风险的团队。因为安全从来不是一次性完成的项目，而是一种持续对抗失控的能力。

END

![](https://mmbiz.qpic.cn/mmbiz_png/ick6R1E3YokFvoM6PLd2g5R9ZyvTVYQhyosDWxvJP5DSfU2zuS01w7sRwGM8y8FPkADsZgW9OzB1fkoEcrsDxmA/640?&wx_fmt=png)![]()![]()![]()![]()![]()![]()![]()![]()![]()

亲爱的朋友，若你觉得文章不错，请点击关注。你的关注是笔者创作的最大动力，感谢有你！

![](https://mmbiz.qpic.cn/mmbiz_png/hTteHHe3QhbWfdLFIQTf8aRCpicxOVskIFGHvib9wFrSvpOkG1prHhy47bGaqjcRHWeZuR0A4TuBLZulsHBp2jYQ/640?wx_fmt=png)

往期推荐

![](https://mmbiz.qpic.cn/mmbiz_png/ib2rOTTXbaRCpkiapP7gr7ic5WibDjVQhnv7lA7iaDlWwYAFKeCmzovW1vyh58JV9hhCKmwnLSW9zzPBMvkuwaEU1xg/640?wx_fmt=png)

Recommended in the past

[网络安全厂商群侠传，江湖儿女的硬核与幽默](https://mp.weixin.qq.com/s?__biz=MzI5MTIwOTQ5MA==&mid=2247490639&idx=1&sn=377a1f04a404c6ef59ebfea88cf87649&scene=21#wechat_redirect)

[网络安全是伪需求吗](https://mp.weixin.qq.com/s?__biz=MzI5MTIwOTQ5MA==&mid=2247490747&idx=1&sn=6f8e63898ae04612bb0923fb1409d845&scene=21#wechat_redirect)

[网络安全行业还值得入吗](https://mp.weixin.qq.com/s?__biz=MzI5MTIwOTQ5MA==&mid=2247490720&idx=1&sn=2a4c63e8801b7801b7ca7e225e2a8f0d&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/XpPOHs6ZLMHobubyUcS4oCTbia813OeNh1vlbOibGCePUF8EfW1mfQLPK4y7wOGuy8e0ib7WqlyKglnXDiaGZ3HFMPjdD007ibJRxwXIsxOVw11w/0?wx_fmt=png)

菜根网络安全杂谈

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/XpPOHs6ZLMHobubyUcS4oCTbia813OeNh1vlbOibGCePUF8EfW1mfQLPK4y7wOGuy8e0ib7WqlyKglnXDiaGZ3HFMPjdD007ibJRxwXIsxOVw11w/0?wx_fmt=png)

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