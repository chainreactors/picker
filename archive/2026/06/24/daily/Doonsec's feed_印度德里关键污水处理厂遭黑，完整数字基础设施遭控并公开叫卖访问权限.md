---
title: 印度德里关键污水处理厂遭黑，完整数字基础设施遭控并公开叫卖访问权限
url: https://mp.weixin.qq.com/s/vPWkwAxFIshI42oQtsleFQ
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:07:46.381347
---

# 印度德里关键污水处理厂遭黑，完整数字基础设施遭控并公开叫卖访问权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lQ1jXOMq3d2KXmkJyMp7SsMjgic3DH7SdG115t61ias9XKic6EiaKXkF6lbxL5MoBEuPZSz5DLACcgKQgz2lzNvv8NU8Mm9eVBPn6icv0OeUEicUE/0?wx_fmt=jpeg)

# 印度德里关键污水处理厂遭黑，完整数字基础设施遭控并公开叫卖访问权限

原创

网空闲话
网空闲话

网空闲话plus

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年6月23日，自称“基础设施破坏小队”（Infrastructure Destruction Squad）的黑客组织在其Telegram频道上发布售卖帖，公开兜售对印度德里水务局（Delhi Jal Board）旗下**Coronation Pillar污水处理厂（STP）**的完整访问权限。该帖详细披露了渗透深度、已窃取数据体量及取得的远程控制能力，并以同样的口吻展示了对印度尼西亚大型水务公司的工控系统攻陷成果，同时夹杂出售加密货币平台漏洞的信息，构成了一场针对关键基础设施的系统性威胁展演。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lQ1jXOMq3d1lfGeiaMJLRAZU5F2856zGUZkdrSpsXhT9PzUcJfQHHEQtabuibFXiatPUvQFcZqc3ucD9pibD4rKaPqQ5Val9XbJgTZJibWnPoXx4/640?wx_fmt=png&from=appmsg)

根据攻击者的描述，遭渗透的污水处理厂位于**北德里穆昆德普尔·布拉里（Mukundpur Burari）地区**，被认为是德里市最重要的污水处理设施之一，其服务范围涵盖**沙克提纳加尔、卡姆拉纳加尔、鲁普纳加尔、GTB纳加尔、德里大学北校区**等广大人口稠密区域。该厂的处理能力约为每日**2000万至7000万加仑**（约7.6万至26.5万立方米，视运行阶段而定），采用**活性污泥法**等现代工艺去除有机污染物、固体和各种有害物质，对维持北德里地区水环境安全具有不可替代的作用。

![](https://mmbiz.qpic.cn/mmbiz_png/lQ1jXOMq3d1qnfg5J95ibpordiaibjURZrBAChlbEUodgtkMuSG0I1WU75z3VvbOGJwwYh3LSicMdcibMjXR9wICLa2PwKEpUx5ZnacM3uIYW9PA/640?wx_fmt=png&from=appmsg)

攻击者宣称，该厂内部系统已被“完全攻破”。其团队成功获取了**Portainer**和**Cloud Commander**等管理控制面板的权限，从而具备了远程管理容器、文件及服务器的完整能力，并宣告对“整个公司的数字基础设施”拥有完全控制权。Portainer是广泛使用的容器管理平台，Cloud Commander则为基于Web的文件管理器，拿下这两套系统，几乎等同于掌握了IT环境的“命门”，为横向移动至底层工控网络埋下巨大隐患。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lQ1jXOMq3d1MFtbT6MlLTvoPILJcHvWfC95KvK9lGIvzM0pArmyjoSyIINpA9iahZwUPbX6esOLKsSXPGLrvC6EcJPm88HWhmpBK7iaSNOQvI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/lQ1jXOMq3d0Kws7rjibFgwW7lqGceh8E2XQRUVsgwqpuxbRA0cdTojea0WnwEHmAnjmIffadvFicpXJjjAOCZOwUkH9h4YxWIqAwjtpL38ILU/640?wx_fmt=png&from=appmsg)

在数据窃取方面，发帖者提供了一份堪称“精确测绘”的成果清单，用以证明攻击的彻底性和渗透深度。据称，已外泄总量高达**764.12 GB**的数据，其中包括经过完整分析的请求日志：共计涉及**706,906条请求**，其中**706,893条**被归类为有效请求，**13条**失败，另有**1,007条**“未找到”。攻击者强调，所有这些请求已被用于识别网络中的漏洞与薄弱点。此外，还收集了详细的访问者统计信息，记录有**2,127名独立访客**，时间跨度为**2025年10月13日至2025年11月27日**，并精确掌握了流量高峰（**每分钟多达45名访客**）和短时间内**11.47 GB**的数据传输量。更深入的是，攻击者识别出了“**sales**”“**basic sales**”等内部API端点，按照**2xx成功、3xx重定向、4xx客户端错误、5xx服务器错误**等状态码进行分类，并对访客的地理位置、操作系统和浏览器类型进行了全面分析。这些精细测绘结果不仅表明攻击者已在内网进行了长时间、无死角的潜伏侦察，更意味着水厂的应用逻辑、数据流向和潜在突破口已被悉数掌握。

作为同一条售卖信息的一部分，该小队还宣称利用其自研的“**VoltRuptor ICS**”工具攻破了印度尼西亚一家主要水务公司**PT. Sauh Bahtera Samudera**的配水网络，涉及一个价值约**14.7亿印尼盾**的项目。攻击者声称已掌握从**Cilia站**到**Cibeber、Ramanuju、Gerem站**的完整配水网络控制权，可实时读取压力、流量和水库水位，远程操作水泵，并扬言“可随时更改运行设置、增加压力、减少流量甚至关闭所有水泵，从而切断印尼广泛地区的供水，对民众、工业和农业造成巨大破坏”，以此作为施压和勒索的筹码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lQ1jXOMq3d3hzxG6KwZ4BKhW7yWunU2qE69nsaS3qajrgBeH770mtQUyCzL7brnabnmYhrFC4dNX9sXJYTXYgDl0SOrRoBg5TbdMwQSatOo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/lQ1jXOMq3d1uY4wr0icx3jzJFK9MBCGhMktEF8G05Lwk78YZCYlfpC1GZ6X43z5HMpP72gI0JFjI5SD6IRcleRia1zWow4S6RsuRqPyuMsicV4/640?wx_fmt=png&from=appmsg)

此事件的时间线进一步显示了该组织的活跃度与协作网络：同日中午12:20，其频道以**500美元**的价格出售据称可“窃取1000份金融文件、护照及数据”的大型加密货币平台漏洞；晚间10:36，则发布感谢消息，向**“xX313XxTeam”**在推广工具和持续支持方面致谢，暗示背后存在协作化的网络犯罪生态。

尽管截至发稿前，印度德里水务局及印尼相关公司尚未发布官方声明，但发帖中提供的具体站点名称、面板类型、精确到个位数的日志统计和长达数月的观测期，使这一系列宣称具备较高的技术可信度。若入侵属实，Coronation Pillar污水处理厂将面临运行参数被恶意篡改、未处理污水溢流乃至工艺完全瘫痪的灾难性风险。这一事件再次证明，关键基础设施的IT与OT边界一旦失守，其所承载的物理破坏与社会危害将远超传统数据泄露。

### 【闲话简评】

此次事件的最危险之处，在于攻击者通过Portainer、Cloud Commander等IT运维管理工具便取得了对核心基础设施的“完全控制”，这暴露出工业组织普遍存在的一个致命误区：将高权限管理面板直接暴露于公网，且未部署严格的多因素认证与网络隔离。攻击者一旦拿下这些跳板，便能借由内部API和弱隔离的边界，逐渐蚕食工控层，将数字入侵演变为对物理世界的破坏。此事警示水务、电力等关键信息基础设施运营者必须引以为戒，即刻收敛不必要的互联网暴露面，强制落实运维入口的零信任访问，构筑IT-OT单向隔离与行为审计，并对异常控制指令建立实时阻断能力，绝不能让管理容器的一行配置，变成打开污水闸门的那把钥匙。

参考来源：Infrastructure Destruction Squad组织TG频道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

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