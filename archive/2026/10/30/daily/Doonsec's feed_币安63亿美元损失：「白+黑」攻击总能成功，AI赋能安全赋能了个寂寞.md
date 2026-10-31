---
title: 币安63亿美元损失：「白+黑」攻击总能成功，AI赋能安全赋能了个寂寞
url: https://mp.weixin.qq.com/s/9FexptfQ5YtLEmuC_KaDhA
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:45:19.574259
---

# 币安63亿美元损失：「白+黑」攻击总能成功，AI赋能安全赋能了个寂寞

# 币安63亿美元损失：「白+黑」攻击总能成功，AI赋能安全赋能了个寂寞

原创

AI安全迪哥
AI安全迪哥

AI安全迪哥

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

今天币圈巨震，币安遭受了黑客攻击，预计损失已达63亿美元。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczOlP4mylhzMsYibHRJh8z7WHR84Ts83Lgpktm5AUMm3HZicaAK1uDDqibBOXHoTNLwFibTPrONibjLU1W7Uq3eiaY8pYVqUJNNKSToZo/640?wx_fmt=png&from=appmsg)

起因是一台DevOps工程师的笔记本被入侵，攻击者获得一个服务容器的访问权，通过它提交未授权的提现交易。这条链上没有一个环节需要"破解"。笔记本是内网里合法的终端，容器是有权限的服务，签名是受控密钥签的。三层各自校验的东西，全部通过，都是白的。

![](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczOWyT76S7ekTtyFys2BbpNTv7nhfyzknicgRpc2G4icjnVxXJWQecgDaRZYp7ia8K9kvtD5fc2LAXfbPmZss2fApjwPdWpoSOazTw/640?wx_fmt=png&from=appmsg)

而前段时间，Bitget遭受黑客攻击，损失3.88亿美元，也是一样的手法，所有的纵深防御都认为是一个正常的管理员指令，而AI也检测出了异常，但是被淹没了。[64分钟攻破Bitget造成3.88亿损失，纵深防御+零信任集体失效，企业安全建设何去何从](https://mp.weixin.qq.com/s?__biz=Mzk4ODQ0NDMyNg==&mid=2247484831&idx=1&sn=ff3475b387ed378d14bc82ff2e6c0816&scene=21#wechat_redirect)

同时，马斯克也发了一个推文："Everyday is Zeroday"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczNxibWxVnlQ1FoQIlTfmeC0qcx9ZKANWficlzP4jiaX6nPyTLVBGITV2QibKb73uP00NR662TiafWb1AuZqxvXneONMK5rqVVHGtOCo/640?wx_fmt=png&from=appmsg)

币安跟bitget一样，采用了**AI赋能安全（AI for Security）的防护技术。技术提供方**Blockaid 的AI模型在首笔转出后两分钟内就标记出了异常。

先看近期所有网络攻击事件，背后共同的规律：白加黑

![](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczN6px3XT8u3YGo6CibqautNENSDmPT3tVNAOX2dKx7RcFhicBTz2Bv3I9N3udJ4eWTsVzQQz1NOxJ7QX8PQn1DSib6qhUPnZaAbCg/640?wx_fmt=png&from=appmsg)

白的是受信任的“加白”内容：例如签名、身份、会话凭证、逻辑0day,这些明确已经是“白”的内容，根本不会匹配特征库，不会匹配情报，不会匹配规则，但很遗憾的是，很多企业的安全运营，却一直围绕着情报、IOA/IOC/SIEM规则、特征库更新来。上个月迪哥去北京一家知名企业，发现主界面用的某TOP厂商的安全运营中心，是各种规则编织出的告警过滤器。而有些企业，用AI挂在这些告警之后，当一个更快的告警降噪器。当这类攻击都是白利用攻击，压根不产生告警，那你降噪运营了半天，到底在运营什么？

黑的是攻击者操作白的对象的上下文意图：例如对白利用对象，产生了不太符合身份或者业务场景的上下文操作。但这部分，有的企业忽视了，有的企业可能用AI赋能了，但是跟Binance以及众多被攻击者一样，产生了攻击信号，但被大量噪音淹没了，这也是迪哥之前文章里提了多次的，白的是对象，黑的是上下文，以及纵深防御一定要围绕不同的维度，从「异构」到「异构」+「异信号」

回到了两个非常关键的安全建设问题：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczPKoHEzkhziaicbfGm5fxdzBCJh01UT6AAczibQzcgfmHgfwvcoDHsib3EjJlQibq4Zf0vLpRlBUDibv8uMB12pcLdhtLVLA2cOAvAk0/640?wx_fmt=png&from=appmsg)

01你的安全运营，是围绕不产生告警的白对象运营，还是围绕完整的白加黑运营？

02即便围绕白+黑进行运营，你能不能在早期把真实攻击信号从海量噪音中提取出来并快速遏制？

白+黑的攻击怎么防：把判定依据从匹配库换成不变量

先给 AI 划一条边界。构建白+黑能力的产品采购方向，微软自己的产品文档已经写了：它的分诊智能体判定意图，且不依赖静态规则和预定义输入，而是做上下文的意图推理：普通大模型做上下文梳理识别+决策JEV/Laya模型快速决策。

如果追求极致速度、效果、性能，通用大模型外，还需要一个垂域安全模型。

![](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczNmFUTRK0vjyia9C50pFELwVA9oLzu75iaDw6MDdjAUXZ9oAzuQhIFYYMQ6phatyB62Nks23Hz0bI0C735jyiczDQ6OsPHYAXhdGI/640?wx_fmt=png&from=appmsg)

目前看，最接近的架构，以海外的产品为例，Crowdstrike以及PaloAlto的架构比较接近，可阅读之前迪哥文章：[安全圈都在谈Agentic SOC：CrowdStrike 凭什么敢让 AI 做判断？](https://mp.weixin.qq.com/s?__biz=Mzk4ODQ0NDMyNg==&mid=2247484847&idx=1&sn=20ee9c4978a16c0879edccc76e154a80&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/E3UNgemkczPxfFffs7Qh4cVyQE3qQsSyOjuNtBIaC3ic9dkwqkAcrFoWaSX7I3Dp7pnrnsrVA81QIFmuxb13EQ3DCBjnPooO4N8bxbbBQeyc/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**L0 事实层：记状态变更，不记告警。** 字段清单：账户／身份标识、代码或权限字段的前后值、nonce、授权列表原文（chain\_id／目标地址／nonce）、调用方、被调用方、calldata 选择器、余额变化、时间戳。这一层不要"检测"，只要变更流。币安案里最关键的那条事件，就是"某 EOA 的代码字段从空变成指向一个未开源合约"。

**L1 语义归因层：让模型读规则的上下文，产出二层证据链。** 对每一条命中的规则、名单、阈值、权限项，让模型去读它的原文、适用范围、变更记录，输出三个结构化字段：这条规则保护的**不变量**是什么、它的**作用域边界**在哪、当前事件**是否落在它的作用域内**。

于是判定不再是一层证据，而是两层：一层是规则命中记录，二层是该规则声称要保护的那个不变量此刻有没有被破坏。这两层给出的结论可以完全相反，而四种组合里最危险的是"未命中 + 不变量被破坏"——币安案最要命的那 3 分 24 秒，就落在这一格里。

**L2 意图判定层：决策模型。** 输入不是原始告警，是 L1 的断言加上行为序列——演练痕迹、注资路径、时间结构、批量与排序这类"读过规范"的痕迹。输出三态：意图为黑、为白、**证据不足**。第三态必须存在，否则模型会被迫给噪声编故事。

**L3 执行层：三条路，不是一条。** 签名前拒绝（策略层，人不可绕过）、签名后即时撤销（预制好的撤销交易，演练过才算有）、库存隔离（不再向状态未知的账户入账）。把策略写成代码、决策与执行解耦，这类开源实现已经成熟（OPA 是常见的一种），不需要为此买新平台。

![](https://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczPksBxyRI6m0a2geyQqIVa7JhUiaEcUUPQd3plnfcX7mhm6vXlW1xPVvxl17ibTnicAh1Pt9mHhNNa9Qx6exxMplY36gfyia8MM6ibk/640?wx_fmt=png&from=appmsg)

最后，构建什么能力，决定未来你会不会遭受攻击

你买的每一层防护，校验的都是它见过什么；攻击者用的，是你没见过的意图。

**白名单管的是谁能进哪扇门。这次是有人拿着合法钥匙，把锁芯换成了自己的。**

留一个动作给今天：把你们签名类和权限类的规则清单拉出来，逐条写一句"它保护哪个不变量"，写不出来的那一行，标上"作用域未知"。这一遍不需要采购，一个下午能做完两类规则。

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/E3UNgemkczMFkIZFVysicQLgtKK5XzzLA5ZKFpKH3DVr5xYezuQr0bODOmhTKLR6vO27yRBf8rIJ625r4TqusibRY9Y9fdLiaEeVv9CXTbIGbg/0?wx_fmt=png)

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