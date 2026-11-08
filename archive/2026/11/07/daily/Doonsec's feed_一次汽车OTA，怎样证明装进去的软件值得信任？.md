---
title: 一次汽车OTA，怎样证明装进去的软件值得信任？
url: https://mp.weixin.qq.com/s/yzaY1w6RhS67zzEM0vt0ng
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:09:45.959249
---

# 一次汽车OTA，怎样证明装进去的软件值得信任？

# 一次汽车OTA，怎样证明装进去的软件值得信任？

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**01**

**下载完成以后，验证才刚刚开始**

车主在屏幕上按下“立即更新”，看到的通常是一段进度条。车辆背后却要完成另一套更复杂的判断：这份软件由谁批准，是否适用于当前硬件，能否与其他控制器协同，安装中断后车辆还能否安全使用。下载速度和更新成功率只是其中一部分；一份来源合法的文件，也可能因为版本过旧、配置不符或组合错误而带来风险。

美国国家公路交通安全管理局在2022年汽车网络安全最佳实践中，专门提出限制固件降级攻击，并要求设计OTA安全措施时考虑服务器失陷、内部人员、中间人攻击及协议漏洞。这个威胁模型把问题从无线链路扩大到了发布后台和整条更新流程。为车辆建立可恢复的信任，需要把这些位置分别看清。

历史案例能说明这项工作的层次。腾讯科恩实验室在Black Hat 2017论文中记载，其2016年特斯拉研究披露后，车企通过OTA回应并引入代码签名保护；实验室随后在2017年研究公告中，又报告绕过该签名机制的问题，并说明相关补丁已通过FOTA下发。这段经历同时展示了远程更新的修复价值与验证实现的重要性，不能据此推断今天车型仍受当年漏洞影响。

本文采用Uptane 2.1.0等公开技术资料展开机制分析，工程示例均为说明性场景。Uptane是一套面向车辆更新的安全框架，覆盖可信交付和终端验证；它明确没有包办构建系统遭入侵、可信软件包本身含有恶意代码等供应链问题。因此，签名验证通过只能回答特定的授权和完整性问题，不能替代代码审查与功能验证。

**02**

**让车辆分别确认“软件合法”和“确实该装”**

哈希值能够发现文件发生变化，但如果攻击者可以同时替换文件和哈希值，校验仍然可能通过。数字签名把校验信息与受信任的发布身份联系起来；加密则主要解决内容保密。工程上应把软件哈希、长度、适配信息与发布授权纳入受保护的校验过程，不能因为下载经过加密连接，就省掉车辆本地的验证。

Uptane进一步把发布职责分成两个仓库。Image仓库保存软件及其可信描述，Director仓库根据车辆上报的版本清单决定各控制器下一步应装什么。车内Primary承担主要通信和验证工作，再向Secondary控制器分发所需内容。这样的分工，使软件发布资格和具体车辆的安装安排能够分别受到约束。

其底层借鉴的TUF把元数据分为Root、Targets、Snapshot和Timestamp等角色：Root分配可信密钥与签名门限，Targets描述目标文件，Snapshot约束元数据集合的一致性，Timestamp帮助判断内容是否仍然新鲜。文件签名只是这组检查中的一环；攻击者即便拿到旧的合法文件，也不能因此绕过版本、有效期及元数据关联检查。

车内资源差异还会改变保护能力。Uptane要求Primary执行完整验证；资源有限的Secondary可以采用部分验证，其元数据信任主要依赖Director的Targets签名，而不独立核验Image仓库元数据。目标软件仍需按相应元数据检查。后者能减轻计算和存储负担，却失去了一部分独立校验能力，因此选择这种方式需要记录剩余风险，不能只把它当成一次性能优化。

对实施团队而言，重要的是把验证放到安装决策之前，并保护验证结果不被后续步骤绕过。下载代理报告“成功”不能直接变成刷写许可；接收端还要核对目标身份、文件内容和已保存的可信状态。更换控制器或恢复出厂设置时，也应避免把受保护的版本记录一并清空，否则先前建立的限制可能在维修操作中失效。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCnmn5qIiccfCibSUMdenUuKyiaDOkn41e5ibD7fzGqZRJxAiabI4icbIWNCnic4cvsQN3z8ml6XbIW68xlibJYu4M0HVn6rZPlJj9MULw/640?wx_fmt=png&from=appmsg)

**03**

**密钥管理要准备好失陷后的下一步**

一把全局密钥用起来很方便，却会把不同车型、供应商与产品年代的风险绑在一起。实际设计应区分签发信任关系的高权限密钥、日常发布密钥和设备身份密钥，明确各自能批准什么。硬件安全模块可以减少私钥被直接导出的风险，但如果发布账户已经失陷，攻击者仍可能通过合法接口发起签名请求。权限控制和审批记录因而同样重要。

Uptane最佳实践建议把Image仓库的Root、Targets及委派角色密钥离线保管，并让密钥彼此隔离；对高影响角色采用门限，可以降低单把密钥失陷的后果。这里的门限要求来自不同密钥，不能把同一把密钥签两次当作两人批准。设备使用对称身份密钥时，文档还给出了将密钥服务器与面向互联网的Director隔离的安排。

门限也不是数量越多就自动越安全。如果所有签名密钥都被同一个在线进程调用，一次后台入侵仍可能取得全部签名能力。工程评审应追问签名人、设备和访问路径是否真正独立，并检查正常发布能否在合理时间内完成。需要紧急补丁时长期绕过审批，会让纸面上的保护失去实际作用。

另一个需要明确的边界是安装授权与启动授权。升级程序完成验证后，启动链仍应依照受保护的策略检查即将执行的软件，避免离线篡改绕过更新入口。恢复镜像、诊断刷写和量产烧录也要纳入同一套责任划分；如果维修接口能够无条件覆盖安全版本记录，OTA入口设置再多校验，也可能被其他写入路径削弱。

密钥轮换还必须照顾长期离线的车辆。可执行的方案需要保留可验证的信任迁移路径，测试跨越多个版本后重新联网的情形，并为无法安全远程恢复的控制器准备售后处置方式。把密钥撤销通知发到云端，并不意味着每一辆车已经接收；覆盖情况和未完成车辆清单应进入持续跟踪。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAic6Q7MLnXPS8JReYOTeFibLRRlVeLEqRk07icAkUCEEcGY3rsM7oria6II8525zbYDc8mlZjpdDicoIbRk5tIs4cT3LEyNOiclAT50/640?wx_fmt=png&from=appmsg)

**04**

**旧版本仍有合法签名，回退却需要重新授权**

降级攻击利用的往往不是伪造软件，而是曾经获批、后来暴露漏洞的旧软件。另一个容易混淆的问题是冻结攻击：车辆持续接收过时内容，被阻止看到后续更新。两者都可能使用真实签名，因此接收端需要保存可信的版本状态，并借助可信时间检查元数据有效期；仅比较文件是否完整，无法发现这些问题。

Uptane最佳实践分别讨论元数据版本号与镜像release counter。前者阻止重放较旧的元数据，后者通过拒绝计数器更低的镜像，阻止回到已被排除的易受攻击版本。文档明确不建议让所有镜像的计数器始终不变，因为在Director失陷时，这会留下选择过时镜像的空间。

不过，安全防降级与故障恢复确实会发生冲突。假设一个新版本引发兼容性故障，工程团队希望恢复旧功能，可以重新审查旧代码、形成新的受授权发布，并维持安全版本约束；如果旧代码存在已知漏洞，就不能仅为恢复便利而撤掉限制。A/B分区能保留可启动的另一份系统，但备用分区是否符合当前安全策略，仍须单独判断。

UN R156的2021年公布文本要求，OTA失败或中断后，车辆能够恢复先前版本，或者进入安全状态，并要求执行更新时有足够电力。它没有把A/B分区规定为唯一实现。对没有双分区空间的控制器，恢复加载器、救援镜像或维修流程需要与整车安全状态共同设计，不能在写入失败后才临时决定怎么办。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCOFned2mqMGPkjrFkXpxmTGmPibiaVTKBMtFsgwln7kEoJrN4dUETGyBrfNRsQop4NMLVbS8vGea5l12HXKZktD6PQ7j9ATzpSY/640?wx_fmt=png&from=appmsg)

**05**

**把一次更新当作整车状态变化来验收**

多控制器更新尤其考验系统协同。一个说明性场景是：网关已经切换到新通信协议，动力控制器却因低电压刷写失败。即使两份软件都获得了合法签名，混合状态也未必可用。发布前必须描述依赖关系、安装顺序与允许存在的中间状态，并规定哪些步骤失败就停止、哪些可以重试，以及什么时候需要限制相关功能。

Uptane标准把不相容的合法镜像混装列为威胁，也要求利用车辆版本清单和仓库信息进行更新决策。但密码学验证不会自动证明整车行为正确。一个可落地的补充，是在安装前检查版本组合，在激活后执行必要的健康检查，再确认更新完成；不能把“文件已写入”直接作为全车任务结束的唯一依据。

验证工作也应覆盖失败路径。建议在台架或受控试验车辆上重放过期元数据、错误目标包和已撤销密钥，分别在下载、校验、擦写、切换及首次启动时中断供电，再检查车辆能否恢复到预定状态。灰度发布应按硬件与软件配置分组，预先确定停止条件。单纯以在线车辆数计算成功率，容易忽略长时间离线或持续重试的车辆。

采用差分更新时，还需增加一项容易遗漏的核验：差分包必须应用在预期的基线镜像上，并检查重建结果。相同目标版本号下，区域配置或维修经历可能让车辆的实际基线不同。工程上应把基线识别、重建空间和完整包救援路径一起测试，避免为了节省下载流量，把不可恢复的风险推到安装阶段。

更新后的证据同样需要留存：哪辆车、哪个控制器、在什么可信状态下接受了哪次发布，失败发生在哪一步，谁批准了后续恢复。NIST的固件韧性指南把保护、检测与恢复作为相互衔接的能力，这个思路可用于审视OTA设计，但它本身不是汽车型式认证标准。[S7]当发布者能够凭这些记录解释一次更新的结果，并对未完成车辆持续负责，进度条背后的安全工作才形成了闭环。

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、...