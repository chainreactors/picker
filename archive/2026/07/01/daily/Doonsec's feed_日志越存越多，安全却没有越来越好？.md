---
title: 日志越存越多，安全却没有越来越好？
url: https://mp.weixin.qq.com/s/__ufpe-VTdnqLvqBYsVhIw
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:54:28.423109
---

# 日志越存越多，安全却没有越来越好？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aKicBJwHBSq6t10JvHEhXPBAtoGfjcFEb8icvgVngLtQK2Ufhqm57LhBX3LWf9ickOc7PIJYbRTwtlJYzEE8oOibUpicTV2a3x1daq3u94L1J8rs/0?wx_fmt=jpeg)

# 日志越存越多，安全却没有越来越好？

聚铭网络

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/uaicMoGl6iaSz34icEtlMpNrZxACe3gTguJiahs3ias2D2kS6ozGicAjicWicluQ1LHzMVaFmAuGP4ibdB4nJY8Y1Dmxgcg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/ldFaBNSkvHhfReibVrfKgxN97qcFx3LVvHmfTYU065P2GNVC8FhTh123NyMjcicJiaK6Xt2AjTQIX0ps3iaUiaNVRibQ/640)

“为什么日志越存越多，安全却没有越来越好？”

这个问题，怕是许多企业的安全负责人心里都犯过嘀咕。十年前的日志系统，一天收几百万条算大项目；现在一台服务器就能产生上百万条日志。安全设备的存储容量从TB级买到PB级，日志留存从6个月扩展到12个月、18个月，预算一年比一年高。但每次复盘安全事件时，最尴尬的场景依然在重复：

“攻击进来了，日志里有记录吗？”

“有。”

“当时为什么没发现？”

“……因为太多了，没看到。”

**日志量增长了100倍，安全能力却好像并没有同步提升100倍。** 问题出在哪？答案，就藏在日志管理的底层逻辑里。

![日志价值与安全运营 (2).png](https://mmbiz.qpic.cn/mmbiz_png/aKicBJwHBSq5gM1icSJdpuw4fAgU9gxafzKgNxNEQG2UeicNU1oWSl4eOkkDb8Nn7UiaCdNWU7vm5jgRXLpIcR8f5icrOibknOR2tAB6RicYRknRAo/640?wx_fmt=png&from=appmsg)

**PART 1**

**不是没有日志，而是不会用日志**

《中华人民共和国网络安全法》第二十一条明确规定，网络运营者应当采取技术措施和其他必要措施，留存相关网络日志不少于六个月，以保障网络安全事件的追溯和调查。此外，《网络安全等级保护基本要求》（GB/T 22239）等标准，也对安全审计、日志记录、集中管理和分析提出了明确要求。这些法律法规和标准解决的是一个基础问题——企业是否具备完整、可追溯的日志记录能力。

![日志价值与安全运营 (3).png](https://mmbiz.qpic.cn/mmbiz_png/aKicBJwHBSq5CLbejYR5mx78oJ9JlWlbjcWrlBUAkib6Du0DCgWD2ITJuYtAYCmUYWX6FvqmicUrNhjTa8nKuXejiaqKF2kXr01zajc0T8seZJc/640?wx_fmt=png&from=appmsg)

在合规要求的推动下，“有没有日志”已不再是大多数企业的主要矛盾。**真正值得追问的是另一个更棘手的问题：日志留住了，但价值发挥出来了吗？**

现实中，不少企业每天产生数亿条日志，却依然面临告警过载、攻击难发现、事件难溯源、安全运营效率低等问题。可见，日志真正的价值，不在于留得住，而在于用得好。

**PART 2**

**日志最大的价值，在于还原攻击原貌**

一次网络攻击，很少只留下一个痕迹。攻击者从初始入侵、权限提升、横向移动到数据窃取，每一步都会在不同设备、不同系统中留下日志。

想象这样一个画面：

* 凌晨，一名员工账号通过VPN登录；
* 十分钟后，一台核心服务器出现异常远程登录；
* 随后数据库执行大量敏感数据查询；
* 紧接着，出口防火墙检测到持续的数据外传行为。

如果分别查看这些日志，它们只是几个孤立事件。但当它们**按照时间、身份、资产、行为进行关联后，一条完整的攻击路径便浮现出来**。

真正帮助安全团队发现风险的，从来不是某一条日志，而是日志之间建立起来的关联关系。因此，日志分析的重点已经从记录发生了什么，逐渐转向理解为什么发生、如何发生，以及接下来可能发生什么。

![日志价值与安全运营 (4).png](https://mmbiz.qpic.cn/sz_mmbiz_png/aKicBJwHBSq4icdHcZQbjMc7YJ2iawyVuQ8SHPgpbNblOXJyOx9NvD8844VyGFS0ic9XyxfePJP8H6PvmXwYjdTEjWRqukUvefyypfDRjOCQsow/640?wx_fmt=png&from=appmsg)

**PART 3**

**海量日志时代，人工分析已难以为继**

随着云计算、大数据、物联网以及移动办公不断普及，企业IT环境日益复杂。与此同时，日志规模也呈指数级增长。网络设备、安全设备、服务器、数据库、终端、云平台、业务系统……每天都会持续产生海量数据。对于中大型企业而言，单日新增日志达到数十亿条甚至更高，已成为常态。面对如此庞大的数据规模，**传统依赖人工查看、人工关联、人工研判的方式，越来越难以满足安全运营需求**。

真正的挑战，已经从有没有日志转变为：

* 如何快速筛选真正值得关注的日志？
* 如何自动关联分散在不同系统中的攻击痕迹？
* 如何从海量数据中发现隐藏的异常行为？
* 如何降低告警噪声，提高研判效率？

这些问题，仅靠人工几乎无法解决。

![日志价值与安全运营 (5).png](https://mmbiz.qpic.cn/sz_mmbiz_png/aKicBJwHBSq78iaI6PQI3uZLAKjiaYnz44L5WWbTqnT772kqGygKibk93aZqPLU5sUUVvcZwU4ayia1NaYS34ibIEBAJrzu5FoSwVyNvn1icIFCdaU/640?wx_fmt=png&from=appmsg)

**PART 4**

**AI时代，日志正成为安全智能的燃料**

近年来，大模型、智能体（AI Agent）等技术不断进入网络安全领域。AI能够自动研判攻击、分析风险、辅助决策，已经成为行业发展的重要方向。但AI并不会凭空理解企业网络环境，它需要持续获取真实、完整、高质量的数据，而日志，正是AI最重要的数据来源。登录行为、访问轨迹、命令执行、权限变化、流量特征、设备状态……**这些散布在不同日志中的信息，为AI提供了理解企业安全状态的重要依据**。

通过持续学习海量日志数据，AI能够：

* 建立正常业务行为基线；
* 自动识别异常访问和异常操作；
* 关联多源安全事件，识别攻击链；
* 辅助安全人员完成智能研判；
* 提供风险处置建议，推动自动化响应。

可以说，日志已经从记录历史的数据，升级为驱动AI安全运营的重要基础。没有高质量日志，就难以支撑高质量智能分析。

![日志价值与安全运营 (6).png](https://mmbiz.qpic.cn/mmbiz_png/aKicBJwHBSq40kSCgl02C1cl7xsQwMjlgwvUOQiaFytNax7yqG3yML50haoL0bWxVZqmjhtJkDQe6one8azAiaJ2HslmfzGLn9yniafm8TBXjoo/640?wx_fmt=png&from=appmsg)

**PART 5**

**安全运营，比拼的是日志价值释放能力**

未来，企业之间的差距，不再体现在谁采集了更多日志，而是谁能够更快、更准确地释放日志价值。真正成熟的安全运营体系，应当围绕日志构建完整的数据闭环：

* **统一汇聚**——打通网络、安全、主机、终端、数据库、云平台等多源日志，实现集中接入；
* **数据治理**——完成日志解析、标准化、标签化，为后续分析奠定基础；
* **智能关联**——打破设备边界，自动识别攻击路径和风险关系；
* **AI研判**——借助智能分析能力提升威胁识别准确率和处置效率；
* **运营闭环**——联动响应、持续优化，实现安全运营能力不断提升。

当日志真正融入安全运营体系，它便不再只是数据，而是支撑风险发现、攻击分析、智能决策的重要生产力。

![](https://mmbiz.qpic.cn/mmbiz_png/aKicBJwHBSq4xCB13vnWVefPicqqicMppz7HJrlJOZlvZKMdn7qaYM6AoBRNwq9jIZJlpaIwTTBfFOWm12giatAjwh3y7YUtp0OzFSymhEWh6Xs/640?wx_fmt=png&from=appmsg)

**PART 6**

**聚铭：让日志从合规工具走向安全运营引擎**

日志的价值，不在于存得多，而在于用得好。聚铭网络以释放日志数据价值为核心，**将聚铭综合日志分析系统（SAS）深度接入旗下****智慧安全运营中心（AISOC）****平台**，构建覆盖日志采集、存储、治理、分析、研判、响应的全流程能力，让日志从满足合规要求的数据留存，升级为驱动安全运营的核心引擎。

平台支持网络设备、安全设备、服务器、终端、数据库、应用系统及云平台等**1600+种**多源异构日志统一接入，实现海量日志的标准化治理、统一存储与集中分析，支持**6至18个月**日志留存，满足《网络安全法》及等级保护相关要求，为安全运营提供统一、可靠的数据底座。

依托多源关联分析、攻击链还原、威胁情报融合、ATT&CK战术映射及AI智能研判能力，平台能够自动关联分散日志、识别攻击上下文、精准定位真实威胁，并对海量日志进行语义理解、风险分析和智能告警归并，实现每天**10亿**条原始日志仅输出约**10条**高价值告警，有效降低告警噪声，大幅提升安全事件研判与运营效率。

![](https://mmbiz.qpic.cn/mmbiz_png/aKicBJwHBSq47TsghApFw3cettcmpx32qLOUUJDVegQ56Z5XiaIgqktPia5gatcu4jViaM8gRRkibYwz6K9XCRUCh5icEtSjbZHaqF239Tp5qbaibs/640?wx_fmt=png&from=appmsg)

日志记录的是过去，而真正决定企业安全高度的，是如何用这些数据守护未来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aKicBJwHBSq4tCbFCYl96VEWr8YcbfSrAIBTicxRwyyjkxsVvHBs1GbkxqTCHBRK3UPTyricyzr6cccGEIOXfqvexlyTN4F0SOAib4JVjXvEQZ0/640?wx_fmt=png&from=appmsg)

更多日志能力，欢迎了解👇👇👇

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aKicBJwHBSq6MeKgQVquXaDRl797pzoaeibc6ygC2iayqiavFOyibSvv3zwbdam0qIWFZAYaRiahhzTiaPb5pKkWne2ocUEmy8FtrJcQtibyhltgiatI/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aKicBJwHBSq4jVGe5Rr6Won3wTQIQ1Hk66LPQyCk8kXaPGBLS2jhgDpu4Zs01I4j2qRmAIsFRXlia6KcKAC0lUfU34m1WOg9owWU7XzJJrGV8/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aKicBJwHBSq7yT8WSDYtVMB5eib87ViaSoRj0iaaIMH2TmbFCdCx5WnQJ9syswNT5YG6D0z7M5fJVt4icIfaIHusTXOyRUmrG3ZXqib7kgcJjR27I/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aKicBJwHBSq4ibc83KJEaVnTQFukdQfoOzRW8Dvl52NkkRpD62IfsFMRBoeCRshgJlynAt6lwJYSeFaCZ2E0w453nUa4tSGxic7zqIbXgG98n0/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aKicBJwHBSq7Y2NPL5ia7TrSx2ZIdtWGMmxzADgic0uURwSFSbicbwqnXLcM2F6cn1het5fdIBpGcRE51D0jEqXeE2Za11bHbsBL5tGVPUgonwc/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aKicBJwHBSq41SQmkYheH1UBLUhrdRapWuu6bPQ9lER2F41xZD6dI07HuTISDVJgJCoQLIOC0eSJ8UpvYQPWRxXx2ENMFtWgElcr74X2GHV4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aKicBJwHBSq6V2VHrNhictrIkvWHy1GxWGa7Js78iaNBymicTT3RgquM2Gxn37sGvYuuyZpOiaGn8kwicuOLLYamySztsvrOibwIBbR8lUEtxUI5Cs/640?wx_fmt=gif&from=appmsg)

**★**

**往期回顾**

**★**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/uaicMoGl6iaSz34icEtlMpNrZxACe3gTguJqY0HcNib1zv87Z739xVEEU1icjSeHEzdqL1HRfcPMXBXYu2lCCIErRww/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzIzMDQwMjg5NA==&mid=2247492709&idx=1&sn=d13d438443bd9246e1020f605120d860&chksm=e8b15a44dfc6d3525bd1ff3c187ac55be18b1f9ab41c00916b75d128ae158dc2502d7956e794&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/aKicBJwHBSq7zIvxxHibIa2GTJ1dcHHWN4oXoXLd7w8j4GLH7UqfeVcythKf4ic6KicePIg6j1W48wwq8ciaJh6K429O0xvozP5hcbP5diczibDegg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzMDQwMjg5NA==&mid=2247508361&idx=1&sn=4ac35feac3090b51dbee15d6bf30f9a0&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/aKicBJwHBSq7Oa199yDiarRVicNyLvrmLKpYSEdAiaYuCmJNGwcJHknLB8FzvU2D4jia7AoBMIYE99nuNQqjEsfYT8RkTp8dEg1MjsQTLD5V4Oag/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzMDQwMjg5NA==&mid=2247508847&idx=1&sn=d9b1d6392e2c912e34546929e0ed905c&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uaicMoGl6iaSxmibldhop4EZ2Hc7MURb2Sp4OeH36iaZicMIZSKX6QdmRmA3SKeftXYJicu0tbQtgogAbLIQZrHub3jg/0?wx_fmt=png)

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