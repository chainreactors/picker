---
title: 基于运维/安全角度下的资产治理，以及探讨开发终端装agent做解密和监控进程，影响编译效率时有无更好解决方案...｜总第264周
url: https://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491519&idx=1&sn=df1460756caa4a32b179674c2392b7e0&chksm=ea4bb5f8dd3c3cee2ba636f1f2594a13bcc0d063239ac947a12701ba11271917b20412d0c53f&scene=58&subscene=0#rd
source: 君哥的体历
date: 2024-10-10
fetch_date: 2025-10-06T18:53:56.969378
---

# 基于运维/安全角度下的资产治理，以及探讨开发终端装agent做解密和监控进程，影响编译效率时有无更好解决方案...｜总第264周

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwZSeZo0a7Whsqnlu9xDF9M7QWZO2GQB72etse4F8raQjibdRB91BD6KhTn0lweLp4ZE67rkLpcoYyA/0?wx_fmt=jpeg)

# 基于运维/安全角度下的资产治理，以及探讨开发终端装agent做解密和监控进程，影响编译效率时有无更好解决方案...｜总第264周

原创

群秘

君哥的体历

![](https://mmbiz.qpic.cn/mmbiz_gif/yXsxtS2cfwYLicju4TyAeQhibftSnibn1R9dnxB7tCR0JyCicooUTh4rDmWsBv1wBniaFHVGdaNmMeJOl1hVIicPKkzg/640?wx_fmt=gif)

**0x1本周话题**

*话题一**：请教一下，有代码库(git、svn)加密的相关产品吗？或者有什么好的解决方案？*

A1：问了几个，有两种形式：

* 使用网关形式，上传加密，下载解密那种。
* 二开对接svn git 原理和一类似，都是流量劫持。

‍

A2：GPG技术。git可以配置gpg，github和gitlab都支持gpg。

**Q：**这个是可以直接对库里的代码做加密是吗（密文）？比如开发终端我理解可以拿到本地做解密然后再打开，比如Jenkins来拉取代码的时候怎么做解密呢？

了解了几个解决方案，基本都是代码库加密，但是开发终端要装agent做解密和监控进程，而且会对编译效率产生影响，所以想问问各位都是怎么做的？

A3：代码防泄露。我前司就是这么干的，确实影响效率，但是还是这么干，整个vsstudio进程算放到agent清单里，用的亿某某。

A4：jenkins可以随便写流水线和脚本，可以做任何事，包括gpg解密。百度搜索： gitlab gpg jenkins gpg github gpg。

**Q：**你们是在库里密文存放，拿下来到安装agent的终端解密，还是库里明文存，过网关拿到本地才做加密？密文存会不会影响对比和预览功能？

A5：做这个的出发点只是防泄漏的话，如果是内网管理，感觉性价比不高啊。

A6：全链路加密。只有装了终端的才可以执行代码，没装终端的执行不了代码。

A7：这个很编译效率，但是就这么干啊。CIO觉得影响的那一点效率相比泄露的风险，他可以接受效率低一点。

A8：如果是自上而下的那理解了。总感觉没啥实际意义，高端的都是偷设计，偷代码本身得是一个特别熟悉这个项目的人才能用起来啊。

A9：3d图纸那些也是加密的，pdf啥的都是加密的。发出去的图纸走外发申请，可以做限制，比如打开三次以后自动销毁，比如截止到某月某日自动销毁。

A10：重要图纸是必须加密的，看看现在淘宝上，各种ppt和图纸。传统文档加密方案都行。

A11：我们也上了这个，所以觉得内部存储库加密的性价比更低咯。这个用起来还不错。就是外发流程需要审批。正常内部使用基本无感知。

A12：亿有时候各种爆0day，但是他们基本上纯内网，外网只有邮件，所以问题不大，杜绝了99%的入口，防着邮件不要有恶意文件或者病毒蠕虫进来即可，以及防勒索。

而且他家的产品有很多方式可以绕过那个加密，我当时也测试了很多出来，但是那时候负责的经理让闭嘴，我也没说话，干了一年我就跑路了。

A13：还能绕过审批外发。我也是18年19年的时候用过，那时候可以绕过。现在新版本就不知道了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwZSeZo0a7Whsqnlu9xDF9M7ViaSqZLJ2Dz0TGpH9BA6fsdwnUIzEcIHKLay3Sibiac5aLeFgKeWw0ksw/640?wx_fmt=jpeg&from=appmsg)

***话题二：******各位有在公司、从运维或者安全的角度，做过资产方面的治理么？***

A1：资产、资产的业务挂载关联、业务责任人、资产的风险数据。这四个方面能关联起来，就可以了。

A2：现在就是想做这个。想先把资产整理全了，至少是相对全，然后基于其上打标，最后再基于资产数据关联安全分析。有什么好的思路和建议么？

A3：其实我觉得这个方向是比较容易失败，因为资产整理全是最难的一环。我觉得**比较好落地的路线是：先聚焦关键资产，例如边界，打出样，都要哪些信息，在哪承载，系统如何对接，如何使用，拿出成果，然后再扩大治理范围。**

A4：比较难，得需要运维或基础平台的大力配合。探查技术，资产多方持续校准，资产探查是关键。想要先摸全后再开展，工作永远无法开始。

A5：资产全，是最难的，变化多，数据鲜度，质量，获取来源，正面采集负面检验，投入也大。

A6：如果第一步就试图资产全，往往资源没有投入到最高危风险。一开始可以先缩小到重要资产全。或者进行内部CMDB+外部探测。

A7：资产全是对的，是目标，但不要“先”资产全了“再”做什么，以免死在第一步都没出成果。cmdb往往一经使用就发现问题。

A8：肯定啊，只要相对全就行了。那接下来第二步怎么做呢？

A9：系统化，数据由系统获取，关联由系统使用。比如责任人不要录入的，而是获取变更发起人，业务不要录入的，获取发布应用，保持数据的鲜度，产出提升成果数据，例如攻击资产关联、处置时效、情报研判等，倒逼数据质量提升。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwZSeZo0a7Whsqnlu9xDF9M7JzK7JibGShpbiaXQXNcYTfYClUJ14ibKJGHv54povnyYQeOSRHsxBuZfg/640?wx_fmt=jpeg&from=appmsg)

A10：这个最主要要确定清楚，做什么资产的梳理。备件也算吗？

A11：这事怎么做都行，正向就是IT有cmdb，服务主动接入，统一管控。反向就是安全扫描，发现未知提醒进行正规流程归属。

问题只在这事特别长周期，只要有人耐心做，一定出很多新资产，然后就可以提升安全评估的覆盖面。但这个事属于那种对组织价值很大，对个人受益不多。这个一直是行业内做得不太好的部分原因。

A12：所以要让组织觉得受益很大，不仅安全受益，科技领域方方面面逗受益，这是基础数据。做资产治理关键是你坐在哪个位置，服务于谁，目标不明确边界不明确，治理会很难。

A13：这种搭基建的工作，过程中，别人都可以直接拿来用这份数据，直接产出价值。而搭基建的那个人要花很多时间在沟通协调测试上，基本就没时间做有直接产出的部分。

而大部分老板认为这是没有技术含量，谁都能做的事，而不会考虑衍生给别人价值，最后做的那个人很尴尬。所以资产管理这事，只有大领导懂，他自上而下想做，才可能做好。自下而上讲价值基本无法成功。

A14：我们之前做过一段时间的资产梳理，也想做我们自己的CMDB，结果就如同这位老哥说的，半路夭折。

A15：赞同，但尴尬的是安全工作很多还要基于这类基础工作来开展，否则安全要从零开始收集信息。而且最后可能还得落一个办事不力，没有产出的“罪名”。

A16：我同样建议安全要聚焦在输出价值上，比如，发现资产不全，也算一种价值，快速响应时带上得益于全面的资产数据，夸夸cmdb，给他们成就，包括运维监控，资产盘点，都依赖于基础数据质量，千万不要因为自己有基础数据就去抢基础的活。

例如，你有hids，有堡垒机，可以和cmdb互相补充，他可以查你的数据补充，全公司最全的数据资产还是他，因为你不会去对接发布平台、维修工单，你可以查他的数据叠加，不要替代。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwZSeZo0a7Whsqnlu9xDF9M72NJjRg0Qn1xTLODBVyn28ykoQALKIenarSMPGLOFkCW4CvMT3RJBYA/640?wx_fmt=jpeg&from=appmsg)

---

**0x2 群友分享**

**【安全资讯】**

[**国务院：审议通过《网络数据安全管理条例（草案）》 讨论《中华人民共和国海商法（修订草案）》等**](https://mp.weixin.qq.com/s?__biz=MzUyMzA0NzkzNA==&mid=2247709734&idx=1&sn=683ffd8ef93d7608a225affcccef1305&scene=21#wechat_redirect)

[**新规速递-《国家网络身份认证公共服务管理办法（征求意见稿）》**](https://mp.weixin.qq.com/s?__biz=MzkzMDY2MDA2Ng==&mid=2247485461&idx=1&sn=f92709db94dd85d8847488d93876c7ae&scene=21#wechat_redirect)

---

由于微信修改了推送规则，需读者经常留言或点“在看”“点赞”，否则会逐渐收不到推送！如果你还想看到我们的推送，**请点赞收藏周报，将****【****君哥的体历】****加为星标或每次看完后点击一下页面下端的“在看”“点赞”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwYaBZeQPdr2gbHqon58JxAIpZTicPdU1I8I0lBV82ur0C278ycyU7FKAvOEibactZPNC8L1mu7zMZAQ/640?wx_fmt=jpeg)

【金融业企业安全建设实践群】和【企业安全建设实践群】每周讨论的精华话题会同步在本公众号推送（每周）。**根据话题整理的群周报完整版——每个话题甲方朋友们的****展开讨论内容——每周会上传知识星球**，方便大家查阅。

---

**往期群周报：**

**[关于soc建设，系统完整性受到破坏时的防御机制，以及AV+EDR异构实践的探讨｜总第263周](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491504&idx=1&sn=0ab81b085e1ed20d35fd1539c78e14aa&chksm=ea4bb5f7dd3c3ce15bb64c2e1970642a41b860d2c1d91990ef95b2ddcd64008485a79084953d&scene=21#wechat_redirect)**

**[内部如何防止终端中毒？各家强密码具体要求是什么？法律角度下，不同方式加密传输手机号的区别是什么？【 总第262周】](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491493&idx=1&sn=af4c325c08c6fe124c5906c7476c7490&chksm=ea4bb5e2dd3c3cf43d366a29983e74e392663fb8625942baef6447c7d3f3d6d0917384de97a5&scene=21#wechat_redirect)**

**[探讨防止终端信息泄漏的主流方式以及基础架构部存在的必要性| 总第261周](http://mp.weixin.qq.com/s?__biz=MzI2MjQ1NTA4MA==&mid=2247491441&idx=1&sn=1cefa7764ae6c0153ca308335f0eecc9&chksm=ea4bb536dd3c3c202017790cce21a63feccd308ced3e973aa640561c9a1fd3a523d51fc60e08&scene=21#wechat_redirect)**

---

## **如何进群？**

**如何下载群周报完整版？**

**请见下图：**

![](https://mmbiz.qpic.cn/mmbiz_jpg/yXsxtS2cfwbppZu5PBSictiaObD2Bnru4z5nSyfMrsqjPO0micwA8CsIDUxRb73kIPomrYtYpWuWqPwMU17LHAIpg/640?wx_fmt=jpeg)

‍

‍

‍

‍

‍

‍

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