---
title: 105 国星链用户遭追踪，藏在广告体系里的跨国监视情报行动
url: https://mp.weixin.qq.com/s/pfMaZcGYEUHl45kOo8fUHQ
source: Doonsec's feed
date: 2026-10-28
fetch_date: 2026-10-29T07:49:41.583165
---

# 105 国星链用户遭追踪，藏在广告体系里的跨国监视情报行动

# 105 国星链用户遭追踪，藏在广告体系里的跨国监视情报行动

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年10月15日，TrendAI发布了一份报告，报告没有点名任何公司，只用了一个代号：SHADOW-EARTH-79。

十二天后，路透社援引六名知情人士的话捅破了这层窗户纸。SHADOW-EARTH-79的真身是一家叫Discover-Tech的以色列广告技术公司。它在105个国家的Starlink流量中是排名第一的广告竞价赢家，占了所有星链用户广告中标事件的约13%。

之前黑鸟已经对该公司干的事情进行了详细介绍，相关阅读：[你刷到的一条广告，可能正在给手机装间谍软件](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451189327&idx=1&sn=ae1924e6941ca799ebe70724677bd0f1&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrTL5e5KJlEMiclOaMnkuAZ9yyBGqWtn44Bia3pEdSun9axeiaJwTnJP92eDEf114wfUYNa6jac6YpfbqKx5GU7fGU2mSrqvOMB3I/640?wx_fmt=png&from=appmsg)

这不是一个卖广告的故事，这是一个关于监控基础设施如何藏身于数字广告供应链的故事。

# 先搞懂RTB是怎么回事

每次打开一个网页或App，屏幕上那块广告位背后都在发生一场毫秒级的拍卖。这个过程叫Real-Time Bidding（实时竞价，简称RTB）。用户设备向广告交易平台发出请求，平台把用户信息打包发给所有参与竞价的需求方平台（DSP），各DSP在几十毫秒内出价，价高者赢得这次广告展示。

相关阅读：[广告相关文章阅读](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451188475&idx=1&sn=ecc1f631a174bd55b82e6d66938bf958&scene=21#wechat_redirect)

问题在于，为了让出价更精准，请求里携带的信息远不止有人打开了页面。设备的IP地址、地理位置、自治系统号（ASN）、设备型号、屏幕尺寸、操作系统、运营商，甚至用户在页面上的行为标签，全都被塞进bid request里发给每一个出价方。

这意味着，一个从来没有被用户直接接触过的第三方，只要参与了竞价，就能拿到这些碎片信息。单次看这些数据似乎没什么，但如果一个出价方在全球范围持续、高频地收集这些请求，积累下来的数据量足以拼出一张完整的行为画像。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrFox5lmoON9t9EzczbHCSnUK6w6Qc0FNYnIlAO0VcZaI2x5RWWEA1IjWq1TBsK0pQpXLmd8xmhVBZgqkk7fiatT3L2Y80rhK5g/640?wx_fmt=png&from=appmsg)

TrendAI的研究团队监测了一个DSP从2025年12月31日到2026年8月15日共228天的数据，截获了8471万次广告请求，其中844万次归因到具体买家。在这些数据里，SHADOW-EARTH-79的行为模式异常得几乎不需要专业训练就能看出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpOhCe2lwTYibndQn61ibOTuuPUm03QKjwPnQCMuufMuISHnXthWeLypheDOf9hgHpfpHM6MF7iaB0tG4J4aJNrKpuQGYTo2YLp4k/640?wx_fmt=png&from=appmsg)

# 数字不会撒谎

先说总量。SHADOW-EARTH-79在49个国家是排名第一的中标买家。在匈牙利，它占了全国广告竞价事件的91.1%；在以色列是90.1%，埃及77.2%，阿塞拜疆75.2%，委内瑞拉72.2%。

这些数字意味着什么？一个正常的商业广告主不可能在一个国家拿下九成以上的竞价份额，就像一家快餐店不可能吃下整个城市的餐饮业。这不是市场竞争，这是垄断式采集。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqic4VX3tqk6ngZhzPKOhq5mI6up1vxFSepked4BZOO6fE6ptPFSKKJS4R0suvAVjrQWgZWdYC0uQ8m0J7vOu6ww6XibDOYwfmBQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpicdBWM00g46nLfg9mVMGDv48Nsxwa9ygyV5o4gmtSwlTO7q2ca1KHWdFN92CTJodlWjWfrvGdhGpqDMOkoQdXcQJibR8iaEhL8s/640?wx_fmt=png&from=appmsg)

再看星链。在Starlink的IP地址段（AS14593，SPACEX-STARLINK）上，SHADOW-EARTH-79的lift（增幅指数）达到了4.9倍。这个指标的意思是：该买家在星链流量中的中标份额，除以它在整体流量中的份额，得出的倍数。1倍以上就说明它在刻意倾斜资源瞄准这部分用户，4.9倍意味着它几乎是专门为星链用户建的这条管道。

作为对比，其他高量级买家的lift通常在2倍左右，整体平均水平约3%。SHADOW-EARTH-79一个人吃掉了星链广告中标量的12.9%，共66208次广告展示。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoZVFShl0gUZNIgHzsVoZFGXsALwBWDr5m8MgRvIk2uwRUXrfEaCSQrJYbYZYN0huVdReuNSTKolWEhGlQ0vJ7cbFeod0nBNBc/640?wx_fmt=png&from=appmsg)

更值得注意的是它活跃的区域。叙利亚、利比亚、南苏丹、也门，这些地方合法西方商业广告需求几乎为零的地方，SHADOW-EARTH-79全部是排名第一的买家。阿富汗排第二。TrendAI的报告原话是在受制裁或活跃冲突国家，合法广告需求实际上为零，但这家公司在这些地方持续出价，而且是最大的买家。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpxgiaFUFnuOCTnTAyeyYGeLFuZ4t9YdYrRnTkib4ic3nX2N8Ltic8KFoicbTkkU6LU5HdyvtrKwTianB8Nd5owrJTw2iaEdIXpsXr8WY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp01BysYUKtCsgfMPl77XSQn5aUcib3DCwiawpqXPArnmXvLncGaetWrHcfgZnGsVjn8MhTafAG7xxeOVkfq98XXhjEaKcovXk00/640?wx_fmt=png&from=appmsg)

有些国家甚至是星链本身被禁止或限制的地方：喀麦隆、叙利亚、苏丹、缅甸、利比亚。但只要有人用星链终端连上网络，广告请求就会发出去，SHADOW-EARTH-79的出价就会跟上去。研究团队用星链官方geo-feed数据库交叉验证了IP归属，仅在缅甸和苏丹两个地址段上出现定位差异，其余全部吻合。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoXWeG5Syia0ayliaxJaiaKvZYHmpu3rIVjRZC9N083ZMbHXhqSX7RP08ynTsjwPAoe4xM4bWsS3u6XibfxAfyl5GJs97bX7uvcF50/640?wx_fmt=png&from=appmsg)

# 为什么是星链

星链的特殊性在于它绕过了地面电信运营商。传统手机和宽带流量要经过各国监管的ISP，而星链终端直接通过SpaceX的卫星通信，地面网络在战区被摧毁或封锁时，星链成了唯一的网络通道。

乌克兰军方靠星链做前线通信和无人机指挥。记者、维和人员、异见人士在审查严格的地区用星链绕过防火墙。这些人的共同特点是：他们的位置信息本身就是高价值情报。

今年5月，以色列国土报Haaretz和情报网站Intelligence Online分别报道，以色列资本持有的企业正在向客户推销识别和追踪星链用户的方法，而广告数据在其中扮演了关键角色。

当一个星链用户打开网页，他的IP地址属于AS14593这个段，这个信息本身就在标示位置。RTB系统把这个标签发给所有出价方，而SHADOW-EARTH-79要做的只是持续出价、持续收集、持续比对。研究团队还发现，部分国家的广告请求明显偏向政府网络所属的ASN，这意味着目标筛选可能精确到了机构级别。

# 被还原的后端系统

光看出价数据还不够。TrendAI的研究人员做了一件更狠的事：他们从SHADOW-EARTH-79公开的assets文件夹里恢复了整个Web应用的前端代码结构。

这是一个基于React框架开发的管理后台。前端代码打包成bundle后通常放在公开目录里，不管用户有没有登录都能访问到。通过分析这些JavaScript bundle，研究团队用AI辅助还原了整个应用的目录结构和功能模块。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqNA6P1RwdKG6ZsOp9iazk69KicoVGUTBXlf1qY59eVI4iatpzRxpkicexI2k4K9e97N27v9n7icdQkIuxx63SaydicAqPj4Bk9hFcDs/640?wx_fmt=jpeg)

从公开assets目录还原的React应用源码树（TrendAI）

这张源码树暴露的信息相当直白。Views目录下有AuthManagement，带TOTP/2FA多因素认证管理；有ChangePassword、CreativeUpload，还有一个叫S3BrowserScreen的组件，标注了S3 file browser，说明这个后台还直连了亚马逊S3存储桶。

Components目录下是一整套表单和数据表格组件，包括FormCsvFileUpload、FormCsvTable、FormMultiSelectDropdown。Redux Actions里有OPERATIONALEventLoggerActions，一个广告公司的后台需要运营事件日志做什么。

但真正让人后背发凉的是后面两张图。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrwzVCzpCSc62Oaocy83zVpvGOuS54Em4kiaCc24lDDc8Pw9QD0JsHiaoKcDqOcIzW6ptV724p1sRU78ULMW6icgtkJxVbicKGnvPo/640?wx_fmt=jpeg)

ADDITIONAL IP/NETWORK OPTIONS配置面板，含panda（De-anon模式）与cjsc\_script（手动脚本注入）（TrendAI）

这是一个叫ADDITIONAL IP/NETWORK OPTIONS的配置面板。里面的选项列表读起来像一份监控工具的功能清单：truncated\_ips（截断IP）、ignore\_user\_proxy（忽略用户代理）、prefilter\_ip（预过滤IP）、dest\_port（目标端口）、cjsc\_logConn（记录连接）、show\_hash（向操作员显示哈希值）、freq\_cap（频率上限）。

最关键的两个选项：panda，注释写的是De-anon mode，即去匿名化模式；cjsc\_script，注释是Manual script injection，即手动脚本注入。

一个广告管理后台需要去匿名化和手动脚本注入做什么。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqxaCyiaicJveicmGd6mWfWyt4yuvUHzvrsg3woj1iaOEbT5hbjXR38SicxpUa7Uvv2cYvtnXOntL5goURbMO6b1IjfBdH2mB0uNYus/640?wx_fmt=jpeg)

IP COLLECTION MODES采集模式、CONCAT IP与DISRUPT OPSEC V2面板（TrendAI）

第三张图更完整。顶部是IP COLLECTION MODES，提供六种采集模式：仅采集IP、采集IP加设备ID、不带ID的IP、多IP加ID、多IP不带ID、无限FIFO队列。中间是CONCAT IP的radio选项，选v2模式会要求填写一个叫opsec\_key的字段。底部是DISRUPT OPSEC V2，分为IP层面干扰、时间层面干扰和User-Agent层面干扰三个子项。

opsec这个词本身就说明了一切。OpSec是Operational Security（行动安全）的缩写，这是情报和军事领域的术语，不是广告行业会用的词。一个正经的广告管理后台不会需要行动安全密钥，也不会需要IP层面干扰和时间层面干扰功能。

把这三张图放在一起看：一个带2FA登录、有S3文件浏览、能手动注入脚本、能去匿名化目标、还配了行动安全反检测功能的系统，它的用户界面长这样，但它的实际用途显然不是管理广告投放。

TrendAI的结论写得很克制：该系统的设计更像一个监控和情报收集平台，而非广告管理平台。异常的出价行为、在受制裁和冲突国家的压倒性份额、对星链地址段的过度竞价，三者合在一起，指向的是一个瞄准敏感地理区域特定人群的追踪基础设施。

# Candiru的影子

如果说TrendAI的报告还停留在广告基础设施疑似被用于监控的层面，同一天发布的另两份报告就直接把名字点出来了。

加拿大网络监督机构Citizen Lab和纽约广告安全公司Confiant在10月15日同一天发布报告，直接点名Discover-Tech。两家机构都指出，这家公司滥用广告竞价流程，将泄露的用户数据回传给自己。

Citizen Lab的另一项调查更进一步：Discover-Tech曾协助将以色列间谍软件公司Candiru的零点击（zero-click）间谍软件植入到半岛电视台等媒体机构员工的设备中。

Candiru这个名字在间谍软件圈子里不算陌生。它是一家以色列商业间谍软件厂商，和NSO Group的Pegasus属于同一类产品：针对智能手机的国家级监控工具。零点击意味着目标不需要点击任何链接，只要广告在浏览器里加载完成，恶意代码就会自动执行，设备被完全接管。

整个链条是这样的：RTB竞价收集到目标的IP和设备信息，判断目标是否有价值，向目标设备投放携带恶意JavaScript的广告创意，广告加载即完成zero-click感染，Candiru间谍软件落地执行。

这不是理论推演。Citizen Lab已经在多个敏感网络组织的流量中发现了这些广告，涉及媒体机构、政府部门和科技公司。

# 不敢点名的行业

一个有意思的细节：TrendAI的研究人员其实确信Discover-Tech就是幕后主体，但他们在报告里没有点名。

路透社的六名消息人士中有五个人透露，TrendAI高管在内部讨论中提出了法律顾虑，最终决定不公开归因。TrendAI在声明中给出的理由是，不点名是为了降低出错风险，避免使用由炒作带动的标签，以及可能误导防御者、扭曲风险优先级并引发不当响应行动的不稳定行为者名称。

这种自我审查在网络安全行业并不罕见。今年早些时候，Palo Alto Networks在一份关于全球网络间谍活动的报告中删除了所有指向中国的明确表述，尽管研究团队确信攻击源自北京。路透社当时报道说，删除内容的原因是担心点名中国会导致Palo Alto在北京的业务受到审查。Palo Alto后来否认报告与采购法规有关联，称任何关联都是推测性的、虚假的。

暴露监控行动可能招致报复，这是行业心照不宣的潜规则。研究公司要做生意，客户遍布全球，得罪任何一个有权势的角色都可能付出商业代价。于是报告里用代号代替真名，用疑似代替确认，让读者自己去猜。

事件曝光后，Google、Comcast等广告平台已经切断了Discover-Tech的竞价访问权限。至少一家美国大型科技公司和一家国际组织已经启动了内部调查，审查Discover-Tech的广告是否针对过自己的员工。

SpaceX和Discover-Tech在报道发出前两周都没有回应置评请求。

# 高风险人群该怎么办

这件事听上去离日常使用很远，但RTB广告系统是每个上网的人都会经过的管道。对于普通用户，TrendAI给出的建议包括：重置广告ID、关闭广告个性化、减少在携带设备上使用广告支持的App。

对于高风险人群，比如在冲突地区工作的记者、维和人员、人道主义工作者，建议打开iPhone的Lockdown Mode（锁定模式）。这款功能会大幅收窄攻击面，让第三方更难投递和运行恶意载荷。授予App权限时遵循最小权限原则，很多免费App靠广告SDK赚钱，而SDK本身就是广告网络接触设备的入口。

广告拦截器可以装，但不要百分之百依赖。如果拦截器只是让广告不显示，追踪事件很可能仍然在后台发生。真正有用的拦截器需要能拦截Web流量中的广告标签、阻止广告支持的App连接广告后端、并阻止敏感追踪信息发往广告网络。

已知SHADOW-EARTH-79的后端基础设施地址后，最直接的做法是在网络层面阻断通往这些服务器和云厂商端点的流量。风险降低的核心思路不是识别每一个可能滥用系统的出价方，而是从接触面上减少暴露。

数字广告供应链的复杂程度远超大多数人的想象。一次广告展示背后是十几个系统的接力，信息在这个链条上被转手、聚合、分析。

黑鸟认为，当这条管道被情报机构盯上的时候，普通用户能做的其实不多，但至少可以知道：

每次屏幕上弹出一条广告，背后都有一场看不见的拍卖，而在那场拍卖里，位置、设备、行为，全都在被标价。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BM...