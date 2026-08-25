---
title: 【深度研判】俄罗斯军方黑客（Sandworm）伪装招聘人员以乌克兰IT从业人员为目标，其社会工程招聘手法对我IT人才与供应链安全风险研判
url: https://mp.weixin.qq.com/s/9CKOJyF05reBPSHpciOXjA
source: Doonsec's feed
date: 2026-08-24
fetch_date: 2026-08-25T02:57:30.621084
---

# 【深度研判】俄罗斯军方黑客（Sandworm）伪装招聘人员以乌克兰IT从业人员为目标，其社会工程招聘手法对我IT人才与供应链安全风险研判

# 【深度研判】俄罗斯军方黑客（Sandworm）伪装招聘人员以乌克兰IT从业人员为目标，其社会工程招聘手法对我IT人才与供应链安全风险研判

FF
FF

情报分析师

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7dSju1WlLI8nic8rPUBDIfXCOic8sibGP6o19sE47hz5WNUw9854wy2xmwFfdcEjiapica0Aamr8379vl69NQ4bvmPQwlF42vMRd26Y/640?wx_fmt=png&from=appmsg)

一场伪装成猎头面试的攻击，把WireGuard这款全球运维人员高度信任的开源VPN工具，变成了穿透乌克兰关键系统的钥匙。

俄罗斯军事情报总局第74455部队关联的Sandworm集群，通过子集群UAC-0145，自2026年5月起用虚假招聘流程锁定系统管理员，最终诱导其安装篡改版VPN客户端SopraVPN，获得任意命令执行权限。

这起案件的关键不在战术新颖，而在于它把IT招聘中无法绕开的"技术测评"环节，改造成了整条攻击链里最难被察觉的一步——这种模式完全可能被复制到我的招聘渠道、供应链和涉外协作体系中。

![](https://mmbiz.qpic.cn/mmbiz_gif/tS0rfJ9Q2UJ7F1fsQNcbmUJpyfHBsib1Ru3Taw2iatLWJAxv9dpIYic6ib7d8dpYjoY5f8aiaE6JIibQfY2yQDIzvIrQ/640)

从简历筛选到定制木马，攻击者用真实Zoom面试制造心理防线的连续消耗

![](https://mmbiz.qpic.cn/mmbiz_png/2tUx7ja8EiaaGPje1UaibXH6QHVLmT7UpReGPzHePFBGcC1k7l65brOCToWJPbSb4KhgQuyakFLIH8xL8BRKxCzA/640)

###

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7evibjQ2L4mxPamRPM6WQZ1C0NWjDiazMovqPALJPVYlKDHLwfKwqrff8pJleqczcHicrItuYKd2IsZicDibrY7w4fd3Mt43j38Teyg/640?wx_fmt=png&from=appmsg)

攻击者在合法招聘平台锁定系统管理员的公开简历，冒用虚构公司名义接触候选人，把沟通从平台迁移到Telegram，再引入一场真实的视频面试，部分分析怀疑其中掺入了AI生成的虚拟形象增强可信度。

面试后攻击者以"技术测评需连接企业VPN"为由发送WireGuard配置文件，该文件被设计为必然连接失败，随后"贴心"建议下载托管在SourceForge、配以仿冒域名的定制客户端SopraVPN。

这套流程精妙之处在于，每一步动作都是IT招聘中天然存在的正常环节，受害者的警惕性被系统性瓦解。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7de4OW5Mu1ahV814AiaAkw3hvvVwdrQn8x5WHNbkeLKMcPYicJQRYJz4DJACfhq2UrcS6EEHaTI2YEys3DV6RV2rEgE58MI9ywAg/640?wx_fmt=png&from=appmsg)

SopraVPN的核心是在配置文件里塞进一个非标准字段"SymmetricKey"，用AES-256-GCM加密恶意载荷，解密密钥取自"PrivateKey"字段，最终把PowerShell代码嫁接进WireGuard原生的运维扩展接口执行——攻击者没有触碰VPN主体功能的可信度，只是精确利用了一个本该用于合法运维的接口。

Windows端建计划任务拉取二阶段载荷，Linux端借VPN隧道用curl下载可执行文件，跨平台持久化能力齐备。

![](https://mmbiz.qpic.cn/mmbiz_gif/tS0rfJ9Q2UJ7F1fsQNcbmUJpyfHBsib1Ru3Taw2iatLWJAxv9dpIYic6ib7d8dpYjoY5f8aiaE6JIibQfY2yQDIzvIrQ/640)

合法工具的信任声誉本身就是可被利用的资产，我远程接入体系存在同源暴露面

![](https://mmbiz.qpic.cn/mmbiz_png/2tUx7ja8EiaaGPje1UaibXH6QHVLmT7UpReGPzHePFBGcC1k7l65brOCToWJPbSb4KhgQuyakFLIH8xL8BRKxCzA/640)

###

WireGuard被选中并非偶然，它是全球运维、跨境办公乃至涉密网络访问的标准工具，开源、可审计的声誉恰恰构成攻击者可资利用的信任资产。

我政务网、军工配套企业、关键信息基础设施同样大量依赖各类VPN与零信任网关，一旦攻击者掌握某类工具的源码结构，完全可以复刻"合法外壳、恶意内核"的套路。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7d0Lpmpx0qNHqF83DlicIO9F0jfP25OHvfgTcLDTNjtcne2cQgQQ4w1TGMnZbljTCoJulP4xzQDooJkdoJxWUibPn9bH994QsBGU/640?wx_fmt=png&from=appmsg)

更现实的是，2026年我披露的一起案例显示，某科研单位外包运维人员因权限管控松软被境外情报机关利诱拉拢，远程下载核心科研数据跨境提供——"招聘渠道被渗透"不是假设，是已经发生的路径。

系统管理员之所以成为最优攻击杠杆，是因为他们掌握跨系统特权账户与网络架构知识，攻陷成本远低于正面突破边界防御。

我电信运营商、云服务商、能源金融行业存在数量庞大的系统管理员群体，其公开简历与跳槽信息构成情报暴露面，而外包和劳务派遣模式又进一步放大了身份核验的薄弱环节，这类人员的安全意识与终端管控水平普遍低于正式员工。

一旦某个运维终端被植入具备命令执行能力的恶意客户端，风险会沿服务关系链条扩散至该服务商的全部客户——这正是NotPetya当年借道乌克兰会计软件M.E.Doc实现全球性扩散的历史教训。

![](https://mmbiz.qpic.cn/mmbiz_gif/tS0rfJ9Q2UJ7F1fsQNcbmUJpyfHBsib1Ru3Taw2iatLWJAxv9dpIYic6ib7d8dpYjoY5f8aiaE6JIibQfY2yQDIzvIrQ/640)

朝鲜IT人员已在我境内设立空壳公司作为渗透跳板，跨境用工审查体系面临同类考验

![](https://mmbiz.qpic.cn/mmbiz_png/2tUx7ja8EiaaGPje1UaibXH6QHVLmT7UpReGPzHePFBGcC1k7l65brOCToWJPbSb4KhgQuyakFLIH8xL8BRKxCzA/640)

###

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7fPFRCF51CA9Xjyiad8ks5eppz9wcQQEQXs2ZIO2ZOiaUibvlfHhDnEPQ7KgaE3Waoib4Bm1VS2EzpZm1rs4rRywn4sq7XPbCIIOIA/640?wx_fmt=png&from=appmsg)

除Sandworm外，朝鲜IT工作者伪造身份渗透全球远程岗位早已形成规模化产业链，联合国估计该计划每年为平壤创汇2.5亿至6亿美元，而已有报道披露朝鲜IT人员正利用在我境内设立的空壳公司作为渗透西方企业的中转平台。

这意味着我的企业注册体系、跨境用工中介渠道客观上已被卷入这张全球身份欺诈网络，无论是作为受害目标还是被利用的中转节点，都对涉外经济安全构成现实压力。

我企业在跨境软件外包、离岸研发合作中同样缺乏专业的技术背景核验能力，难以甄别伪造身份、AI生成的面试形象以及测评环节植入的恶意软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7emn9JWSolBm0RaeEUZl5876zG3yXyJOc43CNArEgMXeHvTb72yAialgb8JZicicz0RvKicQrfEZEYWwug8hbEgvaMxl0qXM41k0ao/640?wx_fmt=png&from=appmsg)

不过社会工程与恶意软件技术本身具有跨阵营扩散的客观规律，一旦公开披露形成技术文档，任何具备能力的行为体都可能复制，这种扩散风险实际上更广泛地指向包括我自身防御体系在内的所有潜在目标国。

这起案件真正值得警惕的地方，不是提供了某种可以照搬的防御模板,而是提示招聘渠道、外包生态、跨境远程协作已经变成国家级网络威胁行为体竞相争夺的初始访问入口。

任何把这类风险简单归类为"境外个案"而不纳入本土供应链安全审查体系的做法，都会在下一次同类攻击到来之前留下真实的可乘之机。

完整版含攻击链技术细节图解、供应链风险模型与政策建议清单，欢迎加入"情报读书会"知识星球下载完整报告，获取更多一手情报分析原创素材。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pBCQrIFuT7eO8PCEDA6UdFUASJwbywsTvQx5YQ3sJLk3iaUMooMgFple2Y4tUzoKzIfCDf5uMH2gWice3yrdu8QRqjT8gnSZ9d4AInvndaubI/640?wx_fmt=jpeg&from=appmsg)

**【深度研判】俄罗斯军方黑客（Sandworm）伪装招聘人员以乌克兰IT从业人员为目标，其社会工程招聘手法对我IT人才与供应链安全风险研判****（资料编码260822914，24页，9797字）**

![](https://mmbiz.qpic.cn/mmbiz_png/pBCQrIFuT7cXQAH8BvVVoB5fOnficKFhOXvmrjSRYOHfLbaBqZUwVs3LLTicE12MLoWPXiahrfJGaRL9Ld5HiaItoPSicMYXpT8enAjiacBqib954c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pBCQrIFuT7cenbHKgXet1zibwgw0v9kCJZ0hnkjDpPdy8Sia6qXHRW9Go0diagW66H7wldLyDMJkA4lmDpU6U0W27Y8EibCvLUk9aYia2iaN17RTM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/pBCQrIFuT7d5VcNhUCGnibMatBsXzqSMtwwxXx3aXR4iaDR9iahfSS0vNtniamlg6ZfFOZNhfHabl6VLpw4cL9ayKq65opHvh6ncIYOJ1Lkqf84/640?wx_fmt=jpeg&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/pBCQrIFuT7fYlY94yNM2mmE00FWzVic2GJ3wQpOkbn4G9soF8yLQzwkCLqXncbbQJkKDamdK2E5DFBCHDARl53BlP398yjMhLvWrOF8J2d9U/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517122&idx=1&sn=b1ef2ff537a3a6c16425da0c6776e8fe&scene=21#wechat_redirect)

[【深度研判】乌克兰SBU持续捣毁俄特工网络（含星链激活与机场监视），俄乌前线情报战手法对我T海与周边反间谍能力建设的风险借鉴](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517122&idx=1&sn=b1ef2ff537a3a6c16425da0c6776e8fe&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pBCQrIFuT7cYv0cDJkfSDaicTjic3S8XFqYMJRDGkbt2SLDicvibOL7iaIyNluzfWPxmyXL4JMfNEicHVq10LX9ulqeQ8sTG0mKtUibCvBcabQVGJ8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517110&idx=1&sn=74e984aab75c4812b954ad9902782edf&scene=21#wechat_redirect)

[【深度研判】美国海军确认弗吉尼亚级特种海底侦察潜艇配置，海底作战能力升级对我海底光缆及南海、西太平洋利益的影响](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517110&idx=1&sn=74e984aab75c4812b954ad9902782edf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/pBCQrIFuT7cNwNVm7GehlbvTc9WRkcYBibbd2TEaVZTSsuJAe3eLSqQc35lxC9GPm6dCljIHYhbWHUGqlAUUia40xyCwATN2grwiczeZzWTcWQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517094&idx=1&sn=5b33d05e56ca29c68df92e4ca8a7255f&scene=21#wechat_redirect)

[【深度研判】日本警方披露以“偶然相遇”方式物色并转化工业间谍线人，对我在日企及人员技术安全与反间谍防护的风险警示](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517094&idx=1&sn=5b33d05e56ca29c68df92e4ca8a7255f&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/pBCQrIFuT7eenYtibh6g7MicL7GI2Qan208rLxN1sde9WZ9lenlkVe4kicNL7qsicFz3DQNzkHlfzN3eiaAVvxvm44FEeKOkw5570lbjqNpdOKZA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517085&idx=1&sn=3b3d8519d5ba1b5733683d13324f0b9b&scene=21#wechat_redirect)

[【深度研判】印度空军中校因涉嫌间谍活动及协助安装间谍软件被捕，南亚军事人员被“美人计”渗透对我相关军事交流与情报安全的潜在风险](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517085&idx=1&sn=3b3d8519d5ba1b5733683d13324f0b9b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/pBCQrIFuT7eV1AmG6jvHBIChaeTYtQNPzFfVXSw4gkqtrntOtbPyvk06N8Ttw25UkHabFfQQy8Z3xRlwuOYH2DH5XF1dJQXmsTnxbb3tS7c/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517061&idx=1&sn=1764aaa0f705940b1eb006806b082069&scene=21#wechat_redirect)

[【深度研判】巴基斯坦三军情报局通过社交媒体网红试图在西孟加拉邦建立间谍网络，南亚情报渗透模式对我周边安全与孟加拉利益的潜在风险](https://mp.weixin.qq.com/s?__biz=MzkwNzM0NzA5MA==&mid=2247517061&idx=1&sn=1764aaa0f705940b1eb006806b082069&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Mkvak7WiccmUO5dhXictxTG5ooia6EeoxUEWwpdMstx1ibGcNTPKQKdW4lNVR4j8qr8uuWMBNGaGiaRMR0wKXP4hxAw/0?wx_fmt=png)

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