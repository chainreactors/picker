---
title: 资产≠台账！AI驱动换个算法，厘清数据安全的隐性“负债”
url: https://mp.weixin.qq.com/s/OjtL8Q7tb5BohVk_pIvOGA
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:43:40.248409
---

# 资产≠台账！AI驱动换个算法，厘清数据安全的隐性“负债”

# 资产≠台账！AI驱动换个算法，厘清数据安全的隐性“负债”

天融信

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/nJmicCz2NYxNibMqIOfXMnZxbVBPBGKu3pficMjqFslyVdhUYhSozJ0egjyKoezIaK9qEyYy6ttzMv3T5Kiasiae7icg/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

数据泄露早已不是“大厂专属难题”，每一家数字化企业，都站在风险前沿。一起来回顾下11月上半程的重点新闻：

**第一份是数据泄露名单：某杂货品牌企业**在2726万条客户信息泄露之外，又添约109万条信用卡资料；某上市珠宝企业会员系统遭未授权存取；某集成电路制造服务企业4.6万笔员工资料在境外论坛明码标价。三起事件的共同点，是先被攻破，后才知道。

**第二份是数据安全罚单：**11月初国家网信办集中通报10起执法典型案例，10月31日公安部网安局公布3起不履行数据安全保护义务的案例。13起案件里，没有一起毁于复杂攻击手法，问题都出在日常运营：弱口令、未授权访问、未清理的测试数据、未及时下线的系统、过期的授权。

**第三份是境外论坛的一则兜售帖文：**先放样本，限时公开，开价3枚比特币。被写进名单的企业，是从别人的转发截图里才知道自己上了榜。

**问题侧**

三份材料指向同一本账

资产栏写得很满，“负债”栏一片空白

账没算错，算法旧了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTfyYs33RQOXjdzMCRsGmUicXDNyJMzebF6kHwLwqpwuicowRCdvmAX0Kt74e17RT4AHRBQnWGL7YAF03FyVCptAPUtEobPhoqM20/640?wx_fmt=png&from=appmsg)

**1**

**数据安全这张表，不能只有资产栏**

![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTfkBUT6ejMKMldnDBMDLg0TQyeZ3ibxkSeOVJz90FiciaNPduTauOeu4QMVhGPib03THTtrsO0Yya7NWuunCPzybCZXr5GZLBpdaQg/640?wx_fmt=png&from=appmsg)

长期以来，数据安全的账本只有一种算法：采购防泄漏设备记一笔资产，通过等保测评算一次验收，平台上线写进年度总结。

“负债”栏却几乎空白：该删未删的数据、该下线未下线的系统、过期的授权、不足六个月的日志、贴入AI对话框的客户名单，都未写进验收报告、资产台账与考核项。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTdMicXk1LOiadsBKOO4JzicW1iayiaDlUKBfFmib7XKB3XxItdTsvpxicGWhRAOZa967UZ9p2Y6kobtGnM5KU6LcypyrF63Iuw3CzLV2E/640?wx_fmt=png&from=appmsg)

天融信在日常调研中发现，约六成客户还在规划，三成处于建设期，进入常态化运营的只有一成。差距不在技术，而在验收那一刻：项目通过，队伍撤走，账本合上。“负债”不会因账停而消失，只会在某天由外部审计一次性计提。

![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTeLoCibOWqTKfTMqOGMH9zWpxGBk5zMfk0exgFiccLRz2mZxicL3Vcw46O1KribUyAgkvS2IxNZ04kHJSvVLwtE1gibD4ibJpmVlvvWI/640?wx_fmt=png&from=appmsg)

**2**

**藏在台账之外的数据安全“负债**”****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTcoicKiahPfLChDy5ib3hicnwxpwNAPicVhQ8gIvKxbKPWBxDvvxOptw3rHZlIB3j23iaplZHsDjOHj2meP5OFCmSPCiaUa52zzibxCdrM/640?wx_fmt=png&from=appmsg)

台账只记录已采购、已上线的安全能力，却忽略了“没做到”的隐性亏空。这些亏空极易被低估，共同构成数据安全“负债”，导致泄露发生往往早于企业的感知。

**第一笔，该删未删。**安徽某数据公司的“数字档案管理系统”用了含漏洞的ES开源版本，测试后未清数据，2400余份审计报告与合同被窃；开篇提到的**某杂货品牌企业**那批资料，本该在2021年系统升级时删掉，却拖了几年。

**第二笔，该管未管。**某医院体检系统设弱口令，取数几乎没有门槛；某软件公司的“盒子”无需登录就能打开4000端口控制台，个人信息全部以明文存放；部分单位权限混乱，数据被导出到无防护的联网电脑。

**第三笔，该续未续。**某医院整改复核时发现，防火墙、数据库审计、堡垒机因授权过期同时失效，终端留有700个漏洞、73个高危。设备还在机架上，授权却已到期，在检查结论中与未采购几无区别，甚至更糟，它制造了“防护已到位”的错觉。

**第四笔，该留未留。**《数据安全法》要求建立全流程管理制度、开展教育培训、采取技术措施；《网络安全法》要求日志留存不少于六个月，按场景分级留存一至三年。不少案件恰好卡在日志被覆盖、无法追溯。

![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTcWUNa1nmhq4VEEdxZRp5Na7bEkGbKNtmZX6kcjTWyJWRANNRc5ZwVfkxS6UBUOS52g8aVXnsxVfZOicO87DKr5VwDxLoh0984g/640?wx_fmt=png&from=appmsg)

***注意啦！***

**四笔账都记在院墙之内，但还有一页长期记在墙外：**数据沿着云账号、供应商接口、招聘与背调平台、离职交接U盘、员工随手打开的AI工具流出。“自家系统未被入侵”，只能证明正门还锁着。

更值得注意的是时序：数据先挂上论坛，截图先在社交平台流传，之后才轮到核实与应对。多数企业是在别人的转发截图里，第一次知道自己上了榜。

![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTc9U2lx8Vl1fm3CmlXibqbXOfJnPCqtVSREe5DmmVbTWuXLk1icwp3mWGojutGQibqUXDck8bhGEFPO6Gkiaav8DSu2dXOwBzaZYuA/640?wx_fmt=png&from=appmsg)

**解法侧**

隐性“负债”厘清，建设思路自然明了

企业缺的往往不是安全设备

而是一套能落地、可持续的新算法

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTdbQziaDibC6yvAAlicCtYns8zbmDtbeJjeciaiaibkqn3DX2YKCqSYicaCapVRfQY8ZCuHgx2iaHQsCcPhfxaJp3BRxLQIIhfR9IsB23I/640?wx_fmt=png&from=appmsg)

**1**

**更换算法：六个环节+六步走**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTeAxcjhcwaCVPnAGRR1ibYsubNyafkOH10bAxRFS90JDDYdhXypzqqlVwEY5vgUJV0dz0QjsKrGAIkWibs4MmIr6B2aF4KsP0MGk/640?wx_fmt=png&from=appmsg)

数据安全建设需围绕六个环节：**采集、传输、存储、处理、交换、销毁**，每一步都有动作，也都可能失效——不做分类分级，敏感数据“不知道自己敏感”；不加密，链路就是明文；不备份，一次勒索即归零；不脱敏，生产数据成了测试数据；不管交换，共享变成外流；不擦除，该消失的数据仍保留在盘上。

![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTdMyYIYW18pyvGNqW0V4qvXzkCfX2Or5vZqyce9gInhic8EAMg1GTLwmokAnAicvqHLibEiajOY7ibyiaqDUficBIscUgdeGSsZe6mZBI/640?wx_fmt=png&from=appmsg)

天融信把数据安全建设拆分为六步：**治理评估、组织建设、管理体系、防护能力、运营管控、监管协同。**最常被跳过的是第五步，因为它不产出验收单。

![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTe8UbYT5ibzWg5DEHawW7btfUkweiciahvQ5N3wNHtVlLsnkhf7PSsC15ibD1ficVmeibG73pQAvhvwbINpTA8YQOJbVR3tdsrcKdaUc/640?wx_fmt=png&from=appmsg)

**前四步摸清“账上记了什么”。数据**分类分级系统可快速厘清数据资产底数，实现数据类型精准定级、数据风险态势监控等；数据安全检查工具箱系统预置七大类、800余项指标，支持迎检前的预演；数据库审计系统支持50余种协议，可还原访问主体、时间、来源主机及操作行为；数据防泄漏系统覆盖网络、终端与云端，依托全链路防护架构应对各类风险。

**方案层面各有分工：天韧-数据勒索保障方案，集“网络防护、流量检测、终端防御、保险兜底”于一体；**天剑-数据泄露防治方案，在网络、终端、数据三层设防；天权-数据特权管控方案，实现一体化、智能化数据特权管控；天盈-数据开发利用安全方案，为数据的开发利用提供全过程防护；天享-数据交换共享安全方案，严格控制跨网数据交换中“共享即外流”风险；天界-数据跨境安全合规方案，帮助企业全面评估数据跨境安全状况，明确合规路径，确保合规操作；云数据安全保障方案，帮助客户建设云管端分区、数据分级的安全等级云；可信数据空间解决方案，通过机制设计落实“可用不可见、可控可追溯”的流通要求。

**第五步解决“账能不能对上”。**数据安全管理平台将资产、策略、告警、工单汇入同一底座，实现告警一键处置；数据安全风险分析系统内置80余个攻击模型，配合授权到期预警与托管运营，形成常态化运营闭环。如果这一环缺位，安全能力即便搭建完成，也难以保持长期有效。

AI时代浪潮下，算法要同步更新：资产栏记设备与系统，“负债”栏记流向与智能；体系随之向“以数智为中心”升级，升级为全场景、全智能的数据安全能力体系：从资产测绘到运营闭环六层贯通，院墙内外接成一条链，智能嵌入分类分级、研判、编排与7×24小时运营。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTeJGGxT48JX8icNGeaSJGWzrXwhLhk2Iic6c7HricmV6DFF4m3SdNoCFTll9mD2e3w8uU7IENnaPAHicu5Y3yBpXU7xzssiaKeomCY0/640?wx_fmt=png&from=appmsg)

**2**

**数智入场：AI在这张表上占两栏**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTfpkEABmWo0row13SkE6AhJ5PbespD1Gl68ssG5HZtq4lCnvKsg7PFwM6E2oS2AMeUibgphicuv64Co8CZz6K8ZCuapjdicIYJyibw/640?wx_fmt=png&from=appmsg)

“负债”一栏，变化在出口。过去的出口可数：数据库、邮件、U盘、系统对接；如今是大模型对话、智能体调用、MCP与A2A协议、API接口和各类“AI中转站”。出口变了，审计视野却还停留在原处。

监管也已将AI列入表内。修订后的《网络安全法》于2026年1月1日施行，首次在法律层面为人工智能立规；9月已有企业以“API中转站”调用大模型接口、未做安全评估被处罚。

资产一栏，AI第一次让“把账记清”成为可能。传统分类分级靠人力堆叠，中型企业盘三个月也未必准确；借助大模型理解语义、抽取特征，识别准确率可达95%以上。

天融信把两栏接在同一张表上：**大模型安全网关为大模型应用系统提供覆盖其生命周期全过程的安全防护，可有效应对智能体自主调用工具与数据带来的新型风险；大模型****数据安全监测系统内置各类安全知识库，可**实现数据输入、训练部署、交互输出的全链路闭环监测；**AI安全评估系统基于**双模型对抗，帮助企业在上线前先做一轮风险验证；**API安全审计系统**把账铺到接口一级，紧盯接口攻击、数据暴露与越权调用，让每次调用可留痕、可阻断。

![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTfVAsKOst5jFat8a31LgF9exuX5oZGhPoQPy9IBPHAXu0MlTy2iaMrxOd8LxXdmGoT2JcsWc5tXVfB6NA5N8Tia0McNPaaAZuvUM/640?wx_fmt=png&from=appmsg)

**致数据安全负责人**

* 数据泄露的形态正在变化：从“被攻破”转向“被滥用”，从“院内”转向“墙外”。攻击者未必需要攻破防线，只要拿到可用的数据就够了。
* 安全合规要求同样在收紧：从“事后处罚”转向“事前评估与持续审计”。授权过期、数据未删、日志不足，都已列入处罚依据。
* 数据安全建设思路在调整：从“产品堆叠”转向“平台、运营与AI”。单点能力堵不住系统性渗漏，账要有人记、有工具记、长期记。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTcNPIfoiaznaduYHcvtGM4MeAOibGCTqqLTJ5c9YS0bz6nEmeKDX6H4GR6RcicAsGZjNMjvK07XLNPk4rnQ5E9jOyCRs79lAaHJAU/640?wx_fmt=png&from=appmsg)

数据是资产，也是“负债”。算法换了，账还需要逐年记下去。天融信愿把根扎到客户离不开的地方，依托“以数智为中心”的数据安全能力体系、从治理咨询到应急响应的完整服务，帮助企业从容应对技术迭代与监管变化，让每一笔数据资产都算得清、控得住、护得牢。

近期热点

[首批！天融信入选国家人工智能安全漏洞库（AIVD）技术支撑单位](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650999946&idx=1&sn=75f8a5d4801ec0185a6723dc123429c7&scene=21#wechat_redirect)

[从规则定义到AI驱动，天融信新一代自动化渗透测试系统正式发布！](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650997685&idx=1&sn=5ccf0972aba3dd70716c923d4b584b95&scene=21#wechat_redirect)

[世界互联网大会｜天融信发布“三域一平面”智能体全域安全框架](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650997772&idx=1&sn=fdfa39eb9343eb4724214d558ca7d7ac&scene=21#wechat_redirect)

[天融信：当应急响应遇上AI，以人机协同打赢网络攻防遭遇战](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650997756&idx=1&sn=b5b65c32761dc66d42589fce17cf439e&scene=21#wechat_redirect)

[天融信超融合：已位列市场第二](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650996861&idx=1&sn=b6f5ba8fb7f4a3516cd3a9b33a9f5757&scene=21#wechat_redirect)

**关注天融信了解更多信息**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/dSWSuPicfjTfMTWicc8vjaOqbhhrKehADyT8bNDMKcj3HRo43hWskicsVDx0v5AIybW780yVwklGZIgsI8d7rU2QveGyUnE08BFQ6YHTiaI2DEs/640?wx_fmt=gif&from=appmsg#imgIndex=2)

![](https://mmbiz.qpic.cn/mmbiz_gif/dSWSuPicfjTch4xDfDkudNeE2ejFmFFlP2aXic9unoe8RnpINgNzfOoczYWndia6D5nLW8jAFAXsXYs9jVVqNozeYE4JshxcpyjlVk1jY6GE84/640?wx_fmt=gif&from=appmsg#imgIndex=3)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/dSWSuPicfjTd2lEcLMGdLD9jnKfdcKH98RiaxZhnQHEHVn3ES0B7975o0vlNOV7iaicXMIq8AsBV8QW6zUnBhtEOJdIhmgPicnISd9yHTPjN504o/640?wx_fmt=gif&from=appmsg#imgIndex=4)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/nJmicCz2NYxPiazyASKVba57ReFHFEqicHGum3FRLQza0a8624LIibogluysp3HQgcztqd1HUchOdIDwak46dKT1IQ/0?wx_fmt=png)

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