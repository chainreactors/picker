---
title: （附公开PPT下载链接）KCon 2026圆满举办：“弈智”破局，推动AI安全从“示险”走向“解法”
url: https://mp.weixin.qq.com/s/k-5v87B50J5b16exwiqyeA
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:58:00.506141
---

# （附公开PPT下载链接）KCon 2026圆满举办：“弈智”破局，推动AI安全从“示险”走向“解法”

# （附公开PPT下载链接）KCon 2026圆满举办：“弈智”破局，推动AI安全从“示险”走向“解法”

安在

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于KCon 黑客大会
，作者KCon 组委会

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM6m3iagLsKGm4I4QHz3AwupwX9A6WDFqc2ickDJlCcn8rCQ/0)

**KCon 黑客大会**
.

KCon 黑客大会，汇聚黑客的智慧。知道创宇出品，追求干货有趣的黑客大会。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

第十四届KCon黑客大会11月1日在北京中关村国家自主创新示范区展示中心圆满举办。作为2026人工智能+大会（GAI+C）官方安全论坛，本届大会以“弈智”为主题，围绕“弈智破局·善用智能”。大会汇聚独立研究者、开源社区成员、高校实验室，以及政企、金融、汽车等行业的安全负责人和 AI 落地实践者，以14+前沿议题和丰富的现场体验，集中讨论AI时代不断扩大的安全边界，以及可信AI如何真正进入研发、数据、业务与治理流程。

接下来，让我们共同回顾KCon 2026的精彩瞬间，重温那些凝聚技术创新与实践热情的高光时刻，感受安全研究者和AI落地实践者对技术探索的执着与坚持。

PS：点击文末“阅读原文”，获取部分演讲嘉宾PPT~

KCon走过十四载，AI从未远离

KCon由知道创宇发起，十四年间，已经从安全研究者交流技术的年度聚会，逐步成长为观察攻防趋势、连接前沿研究与产业实践的重要平台。

大会开场，知道创宇CSO黑哥回顾了KCon十四年发展历程。他表示，AI正在改变网络安全规则，既带来巨大冲击，也创造行业的重大机遇。AI作为新生产力，正催生新的生产关系，网络安全需要主动打破既有规则、拥抱变化。KCon也在变化，今年首次作为2026人工智能+大会（GAI+C）官方安全论坛亮相，走向更大、更广的舞台；与TGO 鲲鹏 AI 工坊等伙伴展开深度合作，共同连接更多技术力量与产业力量。但“无干货，不KCon”的主旨始终不变，未来将继续为技术研究与产业实践提供开放、务实的交流平台。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6WxC64IddGqDUhyricPicUYXiaZfBZPoHluBMSp4tibVuxmfw8epXESv7sT84srcTu7s4ibUrsVtvpgrwicKFtibG2wX68mMKJWcvcC9xEpdsf8ic5o/640?wx_fmt=jpeg&from=appmsg#imgIndex=0)

知道创宇CSO黑哥开场致辞

从终端到运行时：风险沿着AI技术栈加速传导

上午的讨论沿着AI技术栈逐层展开。移动端安全研究关注如何让漏洞发现更快、更接近真实应用；进入PC与智能体场景，重点则变成如何隔离具备自主执行能力的Agent，避免图形操作、输入控制和跨环境交互成为越权入口。AI不仅改变研究方法，也让终端从静态应用扩展到能够持续行动的Agent。

当Agent进入推理与多租户环境，风险进一步向系统内部传导。共享缓存与状态可能成为新的侧信道，智能体行为变化也让风险识别和规模化检测更具挑战。底层资源如何被利用、上层行为如何被识别，正在成为推理安全需要同时回答的问题。

到了协议、模型服务与执行层，攻击也不再只表现为报文是否合法。协议状态转换、第三方AI服务的真实能力、模型调用过程中的隐藏行为，以及Harness、沙箱和Hook之间的信任传递，都进入了安全研究视野。

这些讨论回答的是同一层问题：AI安全正从内容输出扩展到终端、推理、协议、模型服务与运行时。风险不再是孤立漏洞，而会沿着AI技术栈跨层传导。理解了这条风险链，下一步自然要回答：如何把安全做成可部署、可审计、可持续迭代的工程能力？

![](https://mmbiz.qpic.cn/mmbiz_jpg/6WxC64IddGoJpTFW98zDgVwJj09SOzkx0fqdEUtqWYjqcqQibeJjRvZrZicW67m8EKPBhR0R43AvSzJbJibnMdiccuhBQyQPia5SEYwhHYysO6JE/640?wx_fmt=jpeg&from=appmsg#imgIndex=1)

上午场演讲嘉宾

从可控到可用：安全从风险警示进入工程闭环

下午的讨论将视角从“问题从哪里来”转向“能力如何落地”。移动端研发开始把工程效率、质量与安全纳入同一套度量闭环；AI Native组织则进一步讨论人与智能体如何协同，安全边界也从代码层延伸至组织流程和角色权限。

从组织再进入系统，可信Harness成为企业使用AI的重要前提：只有明确执行环境、工具权限和关键动作边界，模型能力才能安全进入业务流程。与此同时，本地模型与企业决策中枢的实践，进一步讨论如何把可控执行转化为实际业务价值。

安全最终还要进入数据和行业现场。从代码生成走向可信数据工程，意味着数据来源、处理过程与结果使用都需要可验证、可追溯；金融等行业的规模化AI研发实践，则尝试在提升开发效率的同时，把权限管理和安全审查纳入日常工作流。随后展开的圆桌对话进一步连接不同角色的真实经验，让技术方案回到组织和产业的共同语境。

![](https://mmbiz.qpic.cn/mmbiz_png/6WxC64IddGrtYfG2uiaCcSDKxlrDRWjdiaLDuAZ29BEaIegds1NtlrRW8P5GmhloZP19b1ZicIpmQLHMvpicNxNgXic83hPgDTwx6JMhyoicqnZLk/640?wx_fmt=png&from=appmsg#imgIndex=2)

下午场演讲嘉宾

从移动工程到AI Native组织，从Harness和本地模型到数据工程、金融实践，下午的议题组成了一条完整落地链：安全不再是产品上线前的单点检查，而是贯穿架构设计、权限控制、数据治理、业务运行和人工接管的基础能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6WxC64IddGoiaUyf8LreH2clVcJmbAscoaJNIUtSDu3FFiaTUZuvLMx1ibXNcEuJUVcdFjmEO8LcWT2MiaPKnLr4jH4kswpuCM7gqC1vGaCKr5w/640?wx_fmt=jpeg&from=appmsg#imgIndex=3)

下午场圆桌对话

从会场到展区：硬核技术与轻松互动同频

会场之外，本届KCon同样呈现出技术大会少见的丰富层次。机器人表演一亮相便吸引参会者驻足，为高密度的安全议题增添了更具未来感的一幕。爱派AiPy展位的Coser则是整个展区一道亮丽的风景线，仙气飘飘的形象吸引了不少参会者主动上前合影。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6WxC64IddGojskDxk8WJb6zWv48zqW2FnNZhlhld5lU5NMYiaoSWl5zePdKiciar7UBh6w6Lb5Mr4aoulLicnCerb1ib7tYulH1CGslmtXcv445k/640?wx_fmt=jpeg&from=appmsg#imgIndex=4)

两轮抽奖则贯穿现场，从极客装备到压轴大奖，为紧张充实的技术日程带来一阵阵惊喜。除此之外，精致的茶歇区成为议题之外的“第二会场”。研究者、开发者和企业安全负责人在这里继续刚才的话题，交流漏洞细节、产品实践和合作可能。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6WxC64IddGrRTlSTsb14bQP7eZibDGlicbjxAPPKClR6WicvTUxPcpbI22kDeyxEYIcyCiakzzI02UpgyJtdWTficrBj2QPBTicUrKBjA0O2DDv8A/640?wx_fmt=jpeg&from=appmsg#imgIndex=5)

机器人、展位、茶歇、抽奖与Coser互动共同构成了一条轻松的参与动线，让KCon不只“听得进”，也“逛得住、玩得开、聊得深”。硬核内容与开放氛围在这里相互补充，技术社区的人情味也因此更加鲜明。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6WxC64IddGrS6ap6WkmPibCv6Q9PSIaiaIZBiaAHQB5PTj6cvNFBpZVpT7WVicCNWRnJ42bhmV6nzNowlsbh5hiajWJcCeVtVgUiaZ8nQpqK3h1S0/640?wx_fmt=jpeg&from=appmsg#imgIndex=6)

![](https://mmbiz.qpic.cn/mmbiz_jpg/6WxC64IddGrOz3ReNddzs7iaNtfnwarrnF7GcTk0EbYA2nuULJ9rwQprnjlbPtrL0Kj8seUlicNpMjCPdEk72Ackm5QvxAOeghNWjDNbbu4rU/640?wx_fmt=jpeg&from=appmsg#imgIndex=7)

一张棋盘：从技术社区走向产业现场

本届大会的讨论不再局限于单一的安全团队。独立研究者、开源社区成员和高校实验室，与政企、金融、汽车等行业的安全负责人和 AI 落地实践者同场交流。研究者带来攻击面发现与漏洞验证，开发者关注Agent和工具链的安全构建，企业安全负责人更关心权限、审计与风险边界，行业实践者则需要可信AI能够真正落地。

不同角色在同一张“安全棋盘”上交汇，让前沿研究获得真实业务参照，也让产业实践更早识别风险。从会场内的连续提问，到茶歇区的深入讨论，再到展位前的动手体验，本届KCon把知识分享、技术展示与行业连接放进了同一个现场，为后续研究、产品验证和生态合作创造更多可能。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6WxC64IddGq8G01sYicv3azBDyJTKz8tJkK7sTPXotiaaMSCk5MAGTGTUjUd7eF0DMy92y8fkJv5VV08uo05K6TpicscdD7zuUeA0ibXyKJictD4/640?wx_fmt=jpeg&from=appmsg#imgIndex=8)

在攻守之间，锚定可信AI的下一步

当AI从内容生成走向任务执行，安全问题也从“模型会不会说错话”，转向“系统会不会做错事”。KCon 2026所呈现的，不只是一次关于前沿攻防的集中展示，更是一条逐渐清晰的实践路径：先理解风险，再寻找解法，最终让安全进入架构设计、执行控制与组织治理。

十四届积累，新的产业坐标。KCon将继续连接安全研究与AI应用现场，以真实问题牵引技术验证，以可信执行支撑产业落地，与更多研究者、开发者和行业伙伴共同守住智能时代的行动边界。

KCon 2026 圆满举办

弈智破局 · 善用智能 —— 感谢每一位同行者

****END**

[![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpft3Q38fRygqB6JoiaNnuCd9iciapibWtWwO8ibpib9wPiclHb5UET2E1vSXsmC8vic1h844SFa01Iic2Yq4keCAA4hRibAN8cQc8NqHejBc/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247657060&idx=1&sn=9fdcb0cd7084523a3ea7fb24ce6e2c31&scene=21#wechat_redirect)

点击这里阅读原文**

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

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