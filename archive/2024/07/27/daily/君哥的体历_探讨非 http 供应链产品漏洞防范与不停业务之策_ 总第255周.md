---
title: 探讨非 http 供应链产品漏洞防范与不停业务之策| 总第255周
url: https://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491342&idx=1&sn=e4bb64f117526b3289e7f63fa1cb8952&chksm=ea4bb549dd3c3c5f34fb2e64216c8ef15578c1ca1dfe79f2c776c52add9151c98d042a30670d&scene=58&subscene=0#rd
source: 君哥的体历
date: 2024-07-27
fetch_date: 2025-10-06T17:43:10.173596
---

# 探讨非 http 供应链产品漏洞防范与不停业务之策| 总第255周

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwYicfVyKsheQZKva0Dnt9L2WgU53D4t3F5XASR7djkBmX12DRAIicOw2GvzwSXyPTYyukXHP3MsfScQ/0?wx_fmt=jpeg)

# 探讨非 http 供应链产品漏洞防范与不停业务之策| 总第255周

原创

群秘

君哥的体历

‍‍

‍‍

![](https://mmbiz.qpic.cn/mmbiz_gif/yXsxtS2cfwYLicju4TyAeQhibftSnibn1R9dnxB7tCR0JyCicooUTh4rDmWsBv1wBniaFHVGdaNmMeJOl1hVIicPKkzg/640?wx_fmt=gif)

**0x1本周话题**

话题：已知某非http的供应链产品存在漏洞，自己在用，并面向互联网提供服务，漏洞利用条件未知。已知这个资产一旦被入侵，必须停业务。大家觉得做到怎样了，才可以不把这个业务停了。

A1：对供应链提安全要求，修复漏洞呗。安全owner业务，要业务推进。

***Q：供应链自己不知道有漏洞，0day。***

A2：做好应急，及时监测，出现安全问题切到业务备机跑先，主机及时修复了切回来。上报国家，由国家同步供应链，然后自己提前修复。纵深做容忍，应急做预案，重保监测异常。如果有切面，就自己进去补洞。

***Q：必须停业务的原因是什么？***

A3：重要且核心业务，多活冗余设计，按服务区域或客户等特定条件分类多活部署，接受部分服务能力缺少，同时互为对照组分析备用，攻坚源代码，根据供应链服务商意愿和能力，针对开源协议、源代码知识产权或者第三方托管情况等情况，内部组织源代码走读... 技术增加入口封装，对延迟不敏感的业务，考虑牺牲用户体验换取变相加强纵深防御能力。

A4：网络侧被绕过正常，但是服务器日志、操作记录、进程、用户、网络连接都完全无问题，感觉八成说没被利用吧。

***Q：你是怀疑有漏洞，但没证据还是说确认有漏洞？***

A5：考虑漏洞产品增加支持异构平台部署+资源多活，保持应用层业务观察。

A6：你就理解是没有具体细节的情报好了，但领导要求自证，安全了吗，够不够。这个背景可以忽略，课题我觉得是通用的，到了演习期间，一样会有这种事。网络连接这一块有麻烦的点，就是这个业务既需要被any访问特定端口，也需要请求any的dns解析，不需要建立tcp。

A7：可不可以把暴露面收一收，入向访问放在VPN里面。

A8：不同供应商与同一供应商不同技术栈都能有利于对照观察。场景如：一个组织内不同的邮件系统，一个产品部署于信创和传统系统都可以考虑。

A9：就以邮件系统为例好了，信创有漏洞，传统暂时没漏洞，部署两套？那岂不是任何一套有漏洞都会被入侵。

A10：是的，客观上肯定增加了风险面和维护量。好的方面是，可改善了关键业务局部连续性服务能力的可能性、可靠性，接受局部服务能力缺失，压降全局服务中断风险，关键业务可以考虑以冗余和复杂性对抗未知风险。大部分产品对技术栈底座会有差异化依赖，这种差异可以考虑。

A11：这个从业务连续性层面没有问题，换个形式，比如被攻击了就一键切换到异构的另一套，也能满足。但假设说coremail或exchange有个漏洞，可以通过精心构造一个smtp协议数据包实现窃取邮件服务器上的数据，这个时候把两套都部署上反而是增加风险了。

A12：我理解你这需求是防范核心供应链未知漏洞。那只能依靠事中，事后了。建立纵深防护，上安全切面，全面安全监控。按照att&ck一个个落实监控，然后验证策略是否有效。

A13：所以主要想考虑，有0day也好，有nday没修也罢，用切面也好，用拟态也罢，那些监测的点，比如函数，比如进程，比如网络，才是关键，哪些点没异常，才能认为这漏洞没利用成功，没有失陷，不需要切换，怎么算全面？这个东西应用好了，是可以对抗网络战的，一开始可能不全面，逐步演进。

A14：你这是要对抗国家级别的黑客攻击，说真心话，有时候还是躺的好，因为攻击都在你的未知区域。先把我们已知的 那类攻击做实，可以发现。

A15：att&ck是攻击技战术，首先防御视角做不到覆盖，其次覆盖的TTP也不代表这个点没问题了，感觉不是好的方法论。

A16：att&ck 不用都全部覆盖，攻击的时候，有时候暴露一点，就可以发现异常。真要防护高水平。像xz后门那样的攻击，太难了。只能等他利用的时候，发现其他痕迹，再追溯。

A17：可以说能发现其他痕迹就是目标。那还是做数基本功。先做到自己紫军，蓝军的攻击都能发现。

A18：这块也每次都能发现问题并改进，蓝军是越来越难了。但蓝军从来不用0day，像此类场景，能显而易见地知道程序内部的调用逻辑监控不到。和自研有很大区别。

A19：精心构造的话，有一定可能性是对特定平台、产品定制化，具体到提及的两个产品，以前学习了阿里有个帖子提到过smtp除了自身安全性低些，在协议组件实现也是有差异的，这种差异可能被利用，反过来也会保持局部有限的服务不受其影响。

A20：异构我理解主要还是解决可用性，保障业务连续性，并不是解决对抗。以前分析Google Beyondcorp构建背后动机时，他们有一个假设是0day是不可能被发现完，然后架构的考虑就变成了，如何在明知可能存在漏洞情况下去进行防护。基于这个假设，Google从http应用层上去构建了统一应用代理网关收敛入口，然后通过实时引擎做基于访问的持续验证。 核心对抗逻辑特征检测作为辅助，核心放在通过可信方式做信任链验证，攻击者构造绕过检测和找0day是相对容易的，但要攻破信任体系成本是很高的。所以对抗就变成信任对抗了，信任体系如果无法攻破，数据包就传递不到真实业务系统上，后来出来创业做持安产品后，这套机制在实战过程中效果是很好的。

A21：http我觉得也比较深入了，就是非http盲区多。我理解异构也能做对抗。

***Q：怎么异构？如果是两套同时提供服务，其实是增加了暴露面，漏洞范围变广了。***

A22：算是类似拟态的逻辑。比如一类阻断设备部署多个品牌厂商，分别判断一次，如果都通过才算。暴露面不能同时，但内部可以。

A23：这感觉是负载均衡和容灾切换。

A24：其实这也有点问题，类似长尾效应，应用侧0day一类的总是没法完全避免，属于大力飞砖

A25：其实本源上就两件事情 NbSP与OVTP，一个是访问控制边界不被绕过，一个是鉴权链路完备，能做到这两点，后门和0day大部分都是一样防范。拟态能防止一部分的非预期nbsp绕过链路，但对ovtp突破型的攻击防御帮助不大。

***Q：我理解nbsp是被动防御，我的设计是良好的，基线是符合的，放着不管，攻击不进来 ovtp更强调主动防御，不相信第一范式一定有效，有没有在尝试，有偏离的迹象，要能发现响应 理念可以融会贯通，我的问题其实是postfix这类没法插桩没法切面怎么可溯， ovtp也漏了咋办？***

A26：postfix有源码的，要插桩也没问题。核心问题还是ovtp可塑链路保障难吧，这个以前我们遇到，更麻烦的是exchange。

A27：exchange后来是外面包了一层来做安全增强，不直接对用户。

A28：那我理解所有的都通用了。能插桩的插桩，不能插桩的，让它自己不对外、不出访，外面包能插桩的提供服务，即便这个不插桩的被利用了，也无法回连。

**0x2 群友分享**

**【安全资讯】**

[因数据治理问题，三家银行合计被罚715万元](http://mp.weixin.qq.com/s?__biz=MzkyMTUwMjIwNA==&mid=2247494483&idx=1&sn=3d02ddb91aa8033a7cf2ba2989afee57&chksm=c18003c0f6f78ad6d961d1615f24783c32d015914a552d5dc36e466cf53f7851e5b250f853ce&mpshare=1&scene=21&srcid=0619UC5OEWIkdcYZSy0kwODp&sharer_shareinfo=e7f956fd53723397f3b8fdda218d579f&sharer_shareinfo_first=a3c76bd941c52d36cb6fc36a8af4193c#wechat_redirect)

[ADR - 运行时安全的未来](http://mp.weixin.qq.com/s?__biz=MzkzNjE5NjQ4Mw==&mid=2247538875&idx=1&sn=b4788e804121a15034a695a49251761e&chksm=c2a07857f5d7f14129b4adec6562239b3022c1daa540600f044142a931732bc3eaed4fa191b7&mpshare=1&scene=21&srcid=06212wzx51Ra9k1d0BV1DprI&sharer_shareinfo=eb14392e565274d8ae24b31543e6fa18&sharer_shareinfo_first=c455686ff6dc696d015028ed40a433de#wechat_redirect)

[如何构建反入侵产品（Linux平台）](http://mp.weixin.qq.com/s?__biz=MzI1NTc1NTcwNg==&mid=2247484388&idx=1&sn=3673bea3696f50cd0a0e25d7d0481eee&chksm=ea305731dd47de27cdb41fd7dbafc62fa801859f389f5d1ae06581e7407dc2cf9fdf587acbb3&mpshare=1&scene=21&srcid=0619kBeiGo5wNB2KbXO9KMv7&sharer_shareinfo=c027c196dbdadddd6d163308c9c5fa30&sharer_shareinfo_first=c027c196dbdadddd6d163308c9c5fa30#wechat_redirect)

[Windows核弹级漏洞，Win7-Win11全部沦陷，最新情况来了！](http://mp.weixin.qq.com/s?__biz=MzIyNjMxOTY0NA==&mid=2247500869&idx=1&sn=99a2222c36ee923c1110b5787b342bfb&chksm=e870c836df074120634b519079cef1011ea2fdf7dbeb246084f2f23c75ff11eded3c0ba5e85b&mpshare=1&scene=21&srcid=0620Q8xuHG23vAqYDGAWKYde&sharer_shareinfo=beb81a74aa0d116236d8c6f146ba1941&sharer_shareinfo_first=eebca98475a0413517f5f204aa8e7bb6#wechat_redirect)

--------------------------------------------------------------------------

由于微信修改了推送规则，需读者经常留言或点“在看”“点赞”，否则会逐渐收不到推送！如果你还想看到我们的推送，**请点赞收藏周报，将****君哥的体历****加为星标或每次看完后点击一下页面下端的“在看”“点赞”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwYaBZeQPdr2gbHqon58JxAIpZTicPdU1I8I0lBV82ur0C278ycyU7FKAvOEibactZPNC8L1mu7zMZAQ/640?wx_fmt=jpeg)

【金融业企业安全建设实践群】和【企业安全建设实践群】每周讨论的精华话题会同步在本公众号推送（每周）。**根据话题整理的群周报完整版——每个话题甲方朋友们的****展开讨论内容——每周会上传知识星球**，方便大家查阅。

**往期群周报：**

[**关于外审中数据安全管控的探讨与实践| 总第254周**](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491337&idx=1&sn=d9852e8ff66228e478f2efb41105eb8c&chksm=ea4bb54edd3c3c586b94f6d290c509c9eaa2ee6fb0f6efc9454bc76ca8298026f82451dfc58b&scene=21#wechat_redirect)

[**关于员工上网行为管理与防范恶意域名的策略探讨| 总第253周**](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491332&idx=1&sn=b7f30e930cdc98331f59b2a0c5a078eb&chksm=ea4bb543dd3c3c5510e837625919a356ccc4aafa3a05c1470b0c0a6926d4669175e4df818674&scene=21#wechat_redirect)

[**关于日志脱敏及修改的相关讨论与法规探究| 总第252周**](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491327&idx=1&sn=ff785d64c773063797962c54611fcf2a&chksm=ea4bb4b8dd3c3daed7d4917d92b373f2bf7309be20ae0d594933af2b2ff36730ec4d263fa9bf&scene=21#wechat_redirect)

## **如何进群？**

**如何下载群周报完整版？**

**请见下图：**

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwbppZu5PBSictiaObD2Bnru4z5nSyfMrsqjPO0micwA8CsIDUxRb73kIPomrYtYpWuWqPwMU17LHAIpg/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/yXsxtS2cfwbbrvrPJc9bTvZFr7n5ZgdWsRKc2GvxcQNogPzLOcveKPP2vpaicqWsRiaASYeEsbAYNsDUWPQ6pyeg/0?wx_fmt=png)

君哥的体历

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yXsxtS2cfwbbrvrPJc9bTvZFr7n5ZgdWsRKc2GvxcQNogPzLOcveKPP2vpaicqWsRiaASYeEsbAYNsDUWPQ6pyeg/0?wx_fmt=png)

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