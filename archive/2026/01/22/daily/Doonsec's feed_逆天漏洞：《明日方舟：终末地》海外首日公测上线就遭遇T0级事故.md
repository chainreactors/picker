---
title: 逆天漏洞：《明日方舟：终末地》海外首日公测上线就遭遇T0级事故
url: https://mp.weixin.qq.com/s/soxHxzHlonxqtAoJjXiAkg
source: Doonsec's feed
date: 2026-01-22
fetch_date: 2026-01-23T03:29:54.581140
---

# 逆天漏洞：《明日方舟：终末地》海外首日公测上线就遭遇T0级事故

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sY7YiaX0Dh2ianDeFqI4Ql8VWiao5H1egnCm1lOEW39hbA9My3xVxVSXZy67CMLNOrHicDyGrzg1bgrAyo7iaiaGFfkw/0?wx_fmt=jpeg)

# 逆天漏洞：《明日方舟：终末地》海外首日公测上线就遭遇T0级事故

原创

二道
二道

二道情报贩子

![]()

在小说阅读器中沉浸阅读

# 1月22日，《明日方舟：终末地》海外服上线首日即爆发严重支付安全事故。玩家绑定PayPal账户后，其他用户的游戏内消费可能被随机从该账户代扣，部分玩家损失金额达数千至上万美元，事件引发全球玩家集中声讨。

海外服玩家绑定PayPal账户后，其他玩家的游戏内消费可能被随机从该账户扣款，而非从实际消费玩家账户扣除。受影响交易记录显示，扣款金额差异极大，例如10美元的月卡服务被扣除1200美元，且涉及美元、日元、欧元等多币种交易，部分玩家累计损失达数千至上万美元。

从技术层面分析，漏洞根源可能源于两方面。其一为API接口逻辑重大错误，开发者未严格遵循PayPal官方支付接口规范，导致所有绑定PayPal的用户支付凭证被存入同一公共存储池，系统扣款时随机抽取池内账户完成支付。其二为免密支付机制误用，游戏支付接口错误调用PayPal免密授权功能，未对用户账户信息进行有效隔离，使得第三方消费可跨账户随意扣款。

开发商鹰角网络海外品牌Gryphline于1月22日21:15发布公告，立即暂停PayPal支付渠道服务，承诺4小时内完成所有异常交易的退款工作，并建议玩家暂时改用其他支付方式完成游戏消费。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sY7YiaX0Dh2ianDeFqI4Ql8VWiao5H1egnCkmdfmgibD539ibO4icdwutzbga1aSGgjMeuteV8pOebj9aWNY8WIBeHWQ/640?wx_fmt=jpeg)

已绑定PayPal账户的玩家需立即解绑该支付方式，同时核查PayPal账户交易流水，发现不明扣款后及时联系游戏官方报备。在官方彻底修复漏洞并公示安全说明前，避免重新绑定PayPal，优先选择信用卡等替代支付渠道。

部分欧美玩家因突发大额扣款陷入财务危机，有玩家透露损失600美元后无力支付房租，相关案例在社交平台广泛传播。中文社区有声音调侃该事件将美国玩家推向经济崩溃临界点。

技术从业者指出，此次漏洞属于低级安全问题，未按官方API规范开发支付接口，暴露游戏研发团队在支付安全领域的严重疏漏。玩家群体则质疑鹰角网络海外运营能力，呼吁官方重新委托专业代理商负责支付系统搭建与运维。

截至1月22日，《明日方舟：终末地》海外服本体服务运行稳定，但PayPal支付渠道恢复时间尚未明确。后续需重点关注三方面进展：一是官方承诺的4小时退款时限是否足额兑现，退款到账效率如何；二是针对遭受大额损失的玩家，官方是否推出额外补偿方案；三是鹰角网络是否会公开漏洞技术复盘报告，明确责任主体与整改措施，以挽回玩家信任。

此次事件被业内定义为T0级支付安全事故，核心问题在于支付接口缺乏用户数据隔离机制。这一案例提醒玩家，绑定免密支付服务时需谨慎评估风险，尤其涉及跨国游戏交易时，应优先选择安全系数更高的支付方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sY7YiaX0Dh2ianDeFqI4Ql8VWiao5H1egnCneziawMSxoAbL9tr8BGfI35qo4PbSnffxMWO2ibwMx1kK84JW0so2iaLg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sY7YiaX0Dh2ianDeFqI4Ql8VWiao5H1egnCTJrlyUTO6tNgfxs6B8cxAAnVOIhcMTW5uG7RjGpjaF1nDtUTBMZ32Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sY7YiaX0Dh2ianDeFqI4Ql8VWiao5H1egnCcDAGap5OmrkDp4NQ4ZzoYnRDhcMCHGgCLJdsbL7pdpLSvW6icBRJGMg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sY7YiaX0Dh2ianDeFqI4Ql8VWiao5H1egnCOgsQpVSPianOWZDa3piaicSkfibQVGh9UukzViaiajOO6d2T38tsUxmaDvfg/640?wx_fmt=jpeg&from=appmsg)

有关小麦地，大佬的事故报告通俗版来了:

开门见山，这次事故算是鹰角和PayPal91分锅，确实是26年IT领域开年第一狠活。

原理其实各路分析也都说的差不多了，哥们也就再用非专业术语概述一下。

首先需要科普的是，鹰角用的微服务、多线程之类的技术，严格来说都是不安全的。安全性必须由开发者充足完善的思考来保证，但很显然，鹰角并没有保证这一点。于是，就发生了以下事项海外玩家小A，开开心心打开了终末地氪金，理想状况下的流程是这样的:游戏客户端识别到了他的游戏内uid，然后开始走支付流程->小A使用了PayPal进行支付->付款成功->PayPal标记了小A本次授权的凭证为已核销->PayPal通知鹰角->充值到账。

但是笨笨鹰角开始发力，业内大伙都会把客户端UID和支付凭证强关联，绑定在一起避免出错，但是鹰角偏不。整个流程里，这一环是完全缺失的。这就导致了不管是哪个号发起的支付请求，只要池子里有支付凭证，鹰角拿起来就用。并且其他的分析报告也提到了，凭证可能被放到了全局作用域中，这就类似以下场景:有十个人排队拿着钱买瓜，排第一的小A把钱包递给摊主鹰角，然后十个人开口说自己要几个瓜，鹰角一边说好，一边把10个人的账单都用小A的钱包付款，鹰角无视了小A不断提醒的“我已经付过钱啦”然后狠狠的收费。为什么说PayPal有1分锅呢，因为这个管钱包的，他是等着店家拿票给他看，他看到票付钱，但是他反应确实会慢半拍，他把钱付出去之后，会稍晚那么一小会儿，才能留下“这个钱我付过了，之后再拿这个票要钱的不能给通过”的记录，那就是这么一小会儿，就有天选倒霉蛋遭扣了5000美刀。

总而言之，移动支付这个国内已经做了太多太久，非常成熟的技术。微服务也火了这么多年，所以我只能认为这并非是设计失误，而是执行坏了)目前有资历能力做架构设计的，他就是神志不清了也整不出这种烂活。所以更大的可能是:因为要考虑成本，所以能省则省。又因为过度乐观的预估了热度，觉得充值订单系统压力会很大，所以把线程池留够了但是没成本考虑线程安全了。测试纯混日子，最终促成了这一惊天大狠活。

另外还有个点，我没看到人说。众所周知，这么重要的发版时刻还是公测首日，一般来说肯定是要全程盯着的。特别是支付系统的日志，鹰角在普遍概念里已经算是大厂了，我不信他们会没人盯着，那为什么开服三四个小时才有第一波急救措施，熔断PayPal支付呢?我有个无责任脑洞:这部分降本增效过度，导致日志根本没考虑到要核验并打印出付款uid和支付凭证是否匹配的提示，只有个数字流水在滚动了..

本来想的是公测首日超抖登顶登基T0级霸权手游结果成了联合斩杀顷刻炼化老外的P0级事故案例(编者注:大佬本人是这么说他写这段文字的时候的心态的写的我浑身是劲真的从业八年没见过这么夸张的烂活...

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sY7YiaX0Dh2iaS8mtrK1dUrIzGbM7UYdiajsuibtSMXj2aYsQnZ5mwhTupx5rDHVU4n7XlXghkUcecCfeuCX0icJMoA/0?wx_fmt=png)

二道情报贩子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sY7YiaX0Dh2iaS8mtrK1dUrIzGbM7UYdiajsuibtSMXj2aYsQnZ5mwhTupx5rDHVU4n7XlXghkUcecCfeuCX0icJMoA/0?wx_fmt=png)

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