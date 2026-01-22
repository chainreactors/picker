---
title: 全球诈骗广告推送的隐秘版图
url: https://mp.weixin.qq.com/s/PlkUbbW5S2P8OgITSxdlkg
source: Doonsec's feed
date: 2026-01-21
fetch_date: 2026-01-22T03:33:55.332085
---

# 全球诈骗广告推送的隐秘版图

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk9Tnia65QiaB5XwwDYOYKKchX9kfNbOhqJ4johsvC2JhSNO3gLrLeAIroA/0?wx_fmt=jpeg)

# 全球诈骗广告推送的隐秘版图

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

# 你的手机或者浏览器是不是偶尔会弹出一些奇怪的通知？

#

# 可能是标注“账户异常”的警示，可能是号称“恭喜中奖”的诱饵，也可能是看不懂的外文弹窗，这些看似不起眼的广告推送，背后藏着一个覆盖全球的诈骗网络。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk9Lyuu93XVdmOwnGX2pibqHOSmJPKusUgiaBAdVnAbLlLNjElCYTibKf5pA/640?wx_fmt=jpeg&from=appmsg)

#

#

这些弹窗绝非随机出现，其背后是精密运作的联盟广告推送体系。

关于这套广告推送体系，可以先看这篇文章再阅读后续内容，可以更方便了解机制：[你的定位不是被偷的，而是被“合法广播”出去的](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184745&idx=1&sn=46497274e3077858804d66f5c50cf0e7&scene=21#wechat_redirect)

研究人员偶然发现其中一个广告推送系统存在DNS记录漏洞，顺着这一突破口深入追踪，15天内收集了60GB数据、5700万条日志，不仅截获了骗子的全套话术，更彻底看清了诈骗广告推送产业链的隐秘运作逻辑。

为摸清这些骚扰通知的源头，2025年1月，研究人员明知故犯地访问了一个已被入侵的网站，并在网站上弹出的提示框中点击了“允许”，订阅了来自未知攻击者的推送通知。只需轻轻一点，一个定制的Service Worker程序就被下载到研究人员的设备上，用于管理他们的“订阅”。

手机开始不停地震动，推送的通知层出不穷，一天往往超过100条。这些诱饵五花八门，从经典的恐吓软件到约会软件，再到名人的耸人听闻的故事，应有尽有。

直到几个月后，点击通知时突然出现域名无法解析的错误，这一破绽被研究人员精准捕捉。

这并非拦截所致，而是攻击者犯了一个低级错误：**DNS无效委派**。简单说，他们在注册商处配置了外部名称服务器，却未在服务器上留存域名信息，导致这个域名成了“无主之地”。而根据DNS规则，任何人都能在服务商处“认领”这类废弃域名。（域名抢注）

不到一小时，研究人员成功抢注该域名，部署的服务器瞬间被海量请求淹没，受害者设备的详细信息、广告副本、软件升级请求源源不断涌入。更意外的是，攻击者的DNS配置漏洞远不止一处，24小时内研究人员抢注的恶意域名从1个增至近120个，每秒产生30MB日志，成千上万台设备持续发起连接。

这并非孤立事件，而是一个覆盖全球的大规模推送广告网络，研究团队触碰到的，仅仅是冰山一角，攻击者控制的域名数量至少是研究人员掌握数量的10倍。

60GB压缩JSON数据，为研究人员还原了这个诈骗网络的真实面貌。褪去“广告”伪装，这些通知的恶意本质暴露无遗。

在用户点击通知广告时，这些广告会将其重定向到诈骗网站。

通知 URL 包含一个自动重定向到固定域名的链接，该域名会将流量导入由联盟广告网络运行的流量分发系统 (TDS)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk9kh4XmLnziaXdhkDPmYdotvH5TCWVnlf9zpnRJp7W5wCUSu4f2nicsgVw/640?wx_fmt=png&from=appmsg)

这些骚扰你的诈骗通知，早已实现“全球本地化”，覆盖全球60多种语言。从英语“重磅消息🔥”、法语“您的账户已被锁定”，到印地语“立即赢取500卢比奖金”、韩语“检测到病毒文件”，话术精准适配不同地区用户，就为了提高诱导点击的成功率，点击后，可以是流量为目的的广告，可以是恶意软件下载等等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk9GjlrQAdoJTa3RfRUqMxqeF62iaBGiaqiaVKe45xPvojgDibjvEU1qClTaQ/640?wx_fmt=png&from=appmsg)

流量分布却高度集中：**孟加拉国、印度、印度尼西亚、巴基斯坦四国占总流量的50%**，其中印度受害者占比20%，但单用户广告价值几乎为零，成为骗子的“低价值流量池”。

地图显示了各国向受害者推送的通知百分比

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk9TA0MZOOXJbSSSBwcicURs9DI7oh6WPBiarhMgXqPsBxlL2VXicYZ5MyZA/640?wx_fmt=png&from=appmsg)

2024 年 10 月至 2025 年 6 月每月新增受害者人数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk9uWYuibfkfFoV9STDRGyZniaPLvSM5D7FGbs4ER4ytJekU58c3yBEQlqA/640?wx_fmt=png&from=appmsg)

你或许只偶尔收到几条弹窗，但受害者的遭遇远比想象中恶劣：

平均每天被推送140条通知，订阅期内累计可达7600条，部分用户甚至被持续骚扰超一年。更隐蔽的是，骗子会通过延迟参数分批推送，每次20条，让受害者全天都被弹窗纠缠，防不胜防。

广告通知中使用的不同类型诱饵的百分比

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk9C3ZSbhmGKLX2htZFuMf8Ot4CoDsFTsgGpAibvfksc1SA49bItzZZ12Q/640?wx_fmt=jpeg&from=appmsg)

这种狂轰滥炸并非盲目操作，核心目的是诱导误触，数据显示，其真实点击率低至1/80000，5700万次通知仅产生630次点击，骗子靠“量变求质变”，赌用户在厌烦中不慎点击。

更可怕的是，这些弹窗背后还藏着隐私泄露风险，所有通知日志均以明文传输，无需复杂解密，仅需解码Base64字符串就能获取全部信息。

骗子会给每个受害者分配SID订阅者ID，精准追踪设备型号、网络运营商、订阅时间，甚至用“成人”“约会”“VR”等关键词给用户画像，针对性推送诱饵。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk9t6DG75AboUmFY5iciaAdfQ42PkATsYX16YCCgibu2I4hgHpm9IrDkPvPQ/640?wx_fmt=png&from=appmsg)

点击通知后，用户会被导向不同模板页面：既有“安全扫描”“验证码”等恐吓类模板，也有“约会模板”“想约炮模板”等成人内容模板，最终要么诱导订阅新通知，要么引流至诈骗网站。

尽管点击率惨淡，这个诈骗网络仍能盈利，其商业模式藏着多重猫腻。

该网络采用CPM（每千次展示付费）和CPC（每次点击付费）两种模式，其中CPC收益微乎其微，15天仅赚1.8美元，核心收入来自CPM，日均约350美元，按攻击者控制的域名规模估算，全球日收入或达3500美元。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk9J7JuLpgxjNR0BpjakQOlO0pgMETGXVbDDj7gR4RI660hC15uGOVXwg/640?wx_fmt=png&from=appmsg)

为榨取更多收益，骗子玩起了“重复计费”套路：同一广告每天向同一受害者推送20次，通过调整延迟参数规避重复检测，靠虚假展示量向广告商收费。而广告定价普遍极低，90%以上广告单条成本低于5美分，成人内容、安全警报类模板CPM仅0.02美元，完全靠规模取胜。

每个目标国家/地区每日广告通知价格

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk9ickImSyKTe4JYmF9swUN2gKsFbJBFaeB7t4AgmicmboNjVdica00F8FtQ/640?wx_fmt=jpeg&from=appmsg)

更讽刺的是，这类广告通知平台号称有“合规审核”和“防欺诈功能”，却对“检测到5种病毒”“账户被封锁”等欺骗性通知视而不见；所谓的IP不匹配检测、用户代理验证等功能要么失效，要么需额外付费启用，本质是靠灰色规则收割广告商和受害者。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk9tg4Eic3S6yUc0an6ia81kHHtcFRMhw2Gxv4zUqIyHtgz9ZKYCo8roI7g/640?wx_fmt=jpeg&from=appmsg)

尤其是你在浏览网页的时候，有时候弹出一些病毒通知类广告，一些无防范的用户很容易点进去。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqnbzgPqnNnzl8y6mYiaPlk99vq9SXWktD3Dq6cjJXoYicUjKbLQTicLicvnaVnbialxfJ61kDlKa5jEGg/640?wx_fmt=png&from=appmsg)

总之，这类因配置错误或被遗忘的广告域名，在互联网上数量庞大，几天内如果没被续费，就会被不法分子劫持利用。

类似技术已被多个威胁组织滥用。例如DNS威胁行为者Vacant Viper，会劫持域名用于TDS流量分发系统，传播恶意软件。

若被弃用域名仍在被积极使用，攻击者可轻松获取海量敏感信息，形成更大范围的攻击链条。

值得深思的是，业内对这类漏洞的界定存在争议，不少人认为这只是“捡漏”而非攻击，但正是这种模糊性，让域名劫持成为网络犯罪的低成本工具。

技术报告：

https://www.infoblox.com/blog/threat-intelligence/inside-a-malicious-push-network-what-57m-logs-taught-us/

此前与广告威胁相关文章:

[规避的艺术：朝鲜黑客如何将恶意链接伪装成合法广告点击](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184868&idx=1&sn=0c459224066a594d097be5bc1a2da391&scene=21#wechat_redirect)

[你的定位不是被偷的，而是被“合法广播”出去的](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184745&idx=1&sn=46497274e3077858804d66f5c50cf0e7&scene=21#wechat_redirect)

[Intellexa联盟0day漏洞攻击不止：泄露分析揭全球监视黑幕](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451183972&idx=1&sn=d2a4411d2ea14dbfb3f7f7af6ef02a28&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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