---
title: 国内首个AI智能体安全标准出台：从\"裸奔\"到\"系安全带\"
url: https://mp.weixin.qq.com/s/zHItlBAmxpej4jfOz2J2LA
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:24:28.261859
---

# 国内首个AI智能体安全标准出台：从\"裸奔\"到\"系安全带\"

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88VHpJAMA3Ixr2KsTMqSIiaJwdebgncx6wsHydaChprFK16zhhBvEfSszDnLJ6oyhsZKia71ER9JUiciaP7nX4JUpQBc4gbZxic2kSl4/0?wx_fmt=jpeg)

# 国内首个AI智能体安全标准出台：从"裸奔"到"系安全带"

安小圈
安小圈

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2ZmL5d0ic88UjChjy2ZqA9kf43fQgpDjjZ5hryO3Y1iaXRX1qEI2m8DkBxrfkN6Z8O7c5CbCiaKQCrYZU8wlzOpxYHXIIjI1eDBrYic23SibeECQ/640?wx_fmt=gif&from=appmsg)

7月1日，全国网络安全标准化技术委员会（网安标委）秘书处印发网安秘字〔2026〕80号文件，发布《网络安全标准实践指南——智能体部署使用安全指引》（TC260-PG-20266A）。这是国内首个专门针对AI智能体部署使用的安全标准文件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hlXiae3yiayvf9yUPycXk736MibL51ySFZxqIvPFkPB7ic6F1BUY6o3YkZbicrAGYibwruK7YkflBHqTS1nA7I0y5TwexMQMMh8QBiavRdNrKK8cFQ/640?wx_fmt=jpeg&from=appmsg)

过去一年，AI智能体（Agent）爆发式增长——自动写代码、自动操作电脑、自动调用API，能力边界飞速扩展。但一个问题始终悬在空中：一个拥有你电脑文件读写权限、Shell执行权限、网络访问权限的AI，到底该怎么管？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hlXiae3yiayvcN1uCnHqicRA5KiakS9Awo1uNniaCZ6P0kFfuCtGmPvJzTkr1DzDibgv9305JqwPmSDJ9cLoF6gmDMZmgAIHrZFoJN4t9Qd7BoJ34/640?wx_fmt=png&from=appmsg)

这份文件给出了第一份官方回答。

五大阶段，全生命周期拉起红线

指引的核心框架是"五大阶段"——评估、准备、部署、使用、停用，覆盖智能体从选型到退役的全生命周期。每个阶段都有具体的安全操作要求，不是泛泛而谈的原则，而是可执行的实操清单。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hlXiae3yiayvcY2RMNxceiae6nu1SCibIE4h1vShwO1zmP41iaRAQZaOHickQO7DdDTY0FBt4LWLhRngys9IejdXT2gKibbibIqUJbF3Jaic2EGzx6WU/640?wx_fmt=png&from=appmsg)

评估阶段先问"该不该用"。要求使用者明确使用目的和业务场景，评估采用智能体的必要性，谨慎选择拟部署的智能体。文件明确列出四类"不应选择"的情形：超一个月无维护且有未解决问题、安全问题长期未响应、存在未修复高危漏洞、已停止维护。同时要求优先选择集成安全沙箱、高风险操作管控、急停控制的智能体——换句话说，没有安全机制的"裸奔"智能体，官方态度是别碰。

准备阶段管的是"装之前"。安装物料必须从官网或应用商店获取，不用网盘、论坛、群组里的修改版和破解版；安装前要验证数字签名和完整性，防范投毒篡改。对大模型的选择，文件提出了一个关键要求：应选择已通过生成式人工智能服务备案的大模型，且优先采用本地化部署；调用外部模型应使用官方接口，"不应通过来源不明的中转站、未授权代理等方式调用"。

部署阶段是安全防护最密集的环节。几条红线格外值得注意：不用管理员权限运行智能体，遵循最小权限原则；限制可访问目录，不授予主目录和系统目录默认访问权限；配置为仅本机可访问，不开放至外部网络；开启全量日志记录。文件还要求提前建立高风险操作清单，对清单内操作实行二次确认或直接阻断——列出的高风险操作包括停止系统服务、格式化磁盘、批量删除、权限修改、密钥更改、开放端口，以及"涉及转账、支付等影响个人财产安全的操作"。

使用阶段聚焦日常运行中的持续安全。除了安全复查和技能安全测试，文件对敏感信息保护着墨颇多：向智能体提供个人信息应坚持"最小必要原则"，涉及生物特征、家庭隐私等敏感信息应审慎提供；未获第三方授权不应提供第三方个人信息；不应提供未获许可的业务数据。此外，要求定期手动查看长期记忆文件内容，及时清理不宜存储的隐私数据——这是针对智能体"记忆"功能的专项防护，在其他安全标准中很少见。

停用阶段不等于"关掉就行"。文件要求停止主程序及所有关联服务和后台进程，备份必要数据，执行环境清理（本地卸载或重置系统、云环境删除数据和撤销凭证、虚拟化环境直接停用）。还特别提醒：确认终止相关服务、取消订阅及自动续费，关注大模型接口是否产生异常费用。

起草阵容透露了什么

这份指引的起草单位名单值得细看：中国电子技术标准化研究院、国家计算机网络应急技术处理协调中心（CNCERT）、清华大学、浦江国家实验室、中央网信办数据与技术保障中心，加上阿里云、华为云、火山引擎（字节跳动）、腾讯云、360——国内主流云厂商和安全大厂几乎全部在列。

这个阵容说明两件事：第一，大厂们已经意识到智能体安全是刚需，不是锦上添花；第二，这份指引不是闭门造车，起草过程中吸收了实际部署智能体的厂商经验。文件中对"中转站调用""一键部署脚本""长期记忆泄露"等具体风险点的精准描述，不是坐办公室里能写出来的。

"实践指南"意味着什么

需要注意这份文件的效力级别。它属于《网络安全标准实践指南》系列，是网安标委秘书处组织制定的标准相关技术文件，性质是指导性文件，不是强制性标准。

换句话说，目前这份指引是"建议你这么做"，不是"你必须这么做"。但这不意味着可以忽视它。中国的监管路径通常遵循"实践指南→行业标准→强制标准"的演进逻辑。今天的实践指南，很可能就是明天强制标准的前奏。在标准正式落地之前先按指引执行的企业，未来合规成本最低；等到强制标准出台再仓促应对的，付出的代价会大得多。

更关键的是，指引附录B专门面向组织提供了安全管理建议——建立内部智能体使用管理制度、资产登记表、活动监控、未审批智能体发现能力。这些要求指向一个明确的趋势：企业内部对智能体的使用管理，正在从"个人行为"上升为"组织责任"。

AI治理从"管模型"进入"管应用"

过去两年，国内AI治理的重心主要在模型层——生成式AI服务备案、算法推荐规定、深度合成管理规定。这份智能体安全指引的出台，标志着治理重心开始向应用层延伸。

模型层管的是"AI能说什么"，应用层管的是"AI能做什么"。智能体与聊天机器人最大的区别在于，它不仅仅是生成文本，而是能感知环境、调用工具、执行操作——它有"手"。管住一个有手的AI，比管住一个只会说话的AI复杂得多。

这份指引的价值在于，它没有回避这个复杂性。从"不用管理员权限运行"到"定期清理长期记忆中的隐私数据"，从"不安装来源不明的插件"到"停用后撤销API密钥和自动续费"——每一条都是实操层面的具体要求，而不是"注意安全"的空话。

智能体的"裸奔时代"结束了。虽然目前只是系上了"建议性"的安全带，但方向已经很明确：要么现在主动系上，要么等法规强制你系上。

本文事实来源：《网络安全标准实践指南——智能体部署使用安全指引》（TC260-PG-20266A，v1.0-202607），全国网络安全标准化技术委员会秘书处2026年7月1日发布，网安秘字〔2026〕80号。原文下载自TC260官网（www.tc260.org.cn）。

来源：安小圈

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88V6AwR3ZXXkoGhIvxCo8jtJV5K0yckJf6KSMbddibV4kcUBtoBOa7O70xjicricrZv1oWMuiafkLd9blATloZAPUotnyOIhguTqvJo/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538732&idx=1&sn=467a34e79656ebbd199335dcc77d7584&scene=21#wechat_redirect)

[重磅申报开启：2026年南京市数字经济（网络安全）工程中级专业技术资格评审申报开始了！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538732&idx=1&sn=467a34e79656ebbd199335dcc77d7584&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88VEzjic1f7B8a9prz3icdEgQpXH1gOGyCYoZHyUAicqvDfdkVCKTCYm9qicEVTGF7fAosbaxdibXgxBT9na3DsrMjxBOyiadNzFvx5Po/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539413&idx=1&sn=477a535cc1c5dd21ac667eff0f60c271&scene=21#wechat_redirect)

[【征稿启事】2026 IEEE网络韧性与内生安全国际会议（IEEE CRESS 2026）相约南京，诚邀投稿！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539413&idx=1&sn=477a535cc1c5dd21ac667eff0f60c271&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88Xr95JLPMCj3IEsZGAL0znMgDYy7QcmFibtBvxLR6nTbq4W4vTMnUhAdaobhKG9mibWfVugG7kFoImZBUEf8MqpF5H8AibmLbk1eI/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[欢迎报名！“联盟货架” 征集工作正式启动](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[聚力协同发展 | 中国质量认证中心有限公司南京分公司正式加入联盟，成为副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

2026-06-17

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88XRibsIKXF2TFo31YtyfTpzRKp3lqA3JpyMFdGWKGGVtONQDgr2Hfm8pibrCwAiaQn5RWPJxTgelQxwFln0ZDrAwK8YuDWUgNaxFE/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

[携手共建产业生态 | 紫光恒越正式升级联盟副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

2026-06-18

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88Ug4pM2QBleSEh81Xt2icXIibBY5o6icibpSFMbFcu4TN9eNvibibict0BCDx8nCYrYViclCu2KGMdx7RnIAdrEvuSGtxKa20mBqH9IPhI/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

****| 往期回顾****

**[AI4E如何重构数字生态系统网络发展范式？](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247532455&idx=1&sn=ee5102d94087e9440ede67b18386c621&scene=21#wechat_redirect)**

**[资料下载 | 十五五规划建议全文及说明](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534593&idx=2&sn=7f9516f40cbafbcb1012d5999612157a&scene=21#wechat_redirect)**

**[《科技日报》整版访谈邬江兴院士：将“安全基因”植入人工智能系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537206&idx=1&sn=2ce618202d759560ecee6aeca93b8c24&scene=21#wechat_redirect)**

[里程碑时刻：智己LS9 Hyper搭载原创内生安全技术](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538132&idx=1&sn=77e4efcb6eea205e082f79b82336cc65&scene=21#wechat_redirect)

[邬江兴院士：构建内生安全质量检测体系，筑牢人类可控可信 AI 根基](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539044&idx=1&sn=1791fd1aad5f130fe5d87c46cc4b8687&scene=21#wechat_redirect)

[《智能网联汽车 自动驾驶系统安全要求》：强制性国家标准发布](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539447&idx=2&sn=049dcc3aecb0b2d69a014e1e640389d6&scene=21#wechat_redirect)

[广西日报 特稿《王的猜想》](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539447&idx=1&sn=80f50cb87655bb61a2375885edf5d0ac&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/jRRfTC292pXGqHBACsK1cVtpyTB5F8VFsEY3paWnfS3dichupP4OknoSrNN3c6YviaDsLwKnfHwj1OibB7lWFvbibQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jRRfTC292pX7QK5QfSb6k3uQJ3EsDmeCnsG6veyEXTXsbCcuuTJ7LWzo0tPv2ezibrAF07JXGxYs8zSXgXibLX2Q/0?wx_fmt=png)

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