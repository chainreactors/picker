---
title: 安全资讯汇总：2026.11.9-2026.11.13
url: https://mp.weixin.qq.com/s/fGXiOt466arbBg9nzN77mg
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:17:35.136597
---

# 安全资讯汇总：2026.11.9-2026.11.13

# 安全资讯汇总：2026.11.9-2026.11.13

江南信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**点击蓝字 关注江南信安**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/41AD92vfadSmGv36Z8hDtibLcicK5wXWGYx7otjSPeIl1emFfcFbyjCDNMlIOyUH86FuzoQKPdlUHH2dRun2IfeQ/640?wx_fmt=png)

**安全专栏**

**2026/11/9-2026/11/13**

江南信安网络安全汇总专栏，每周为您提供网络安全领域「标准规范、安全热点、行业发展、深度好文、融资信息」等最新资讯的追踪与共享。

**标准规范**

**1、**商用密码加密传输丨强制性国标《卫星导航定位基准站网安全要求》发布

市场监管总局（国家标准委）批准发布强制性国家标准《卫星导航定位基准站网安全要求》（GB 48567—2026）。该标准由自然资源部提出并归口，从设施、数据、服务全链条明确安全技术要求，为依法规范基准站网建设运行管理、保障国家时空基准和测绘地理信息安全提供技术支撑。

原文链接：

[商用密码加密传输丨强制性国标《卫星导航定位基准站网安全要求》发布](https://mp.weixin.qq.com/s?__biz=MzUzNTU2NTYwNQ==&mid=2247519850&idx=2&sn=b1f501baaff76d9f5ee96edfe6cd25f2&scene=21#wechat_redirect)

**安全热点**

1、**今年最高金额！零售巨头因网络攻击损失近20亿元**

2026 年 8 月，德国柏林市政府证实遭到 Rhysida 勒索软件团伙攻击，该组织自 2023 年年中开始活跃，主要针对医疗机构、政府机构、教育单位与关键基础设施。攻击疑似发生在 8 月 7 日至 12 日，8 月 14 日受影响参议院部门断开政务网络隔离处置，8 月 28 日攻击者在泄露站点公开此次事件。

欧洲零售巨头Ahold Delhaize表示，上个月发生的网络攻击干扰了其美国及欧洲多国业务，预计导致公司第四季度净销售额减少2亿至2.5亿欧元（约合14.9亿至18.6亿元人民币）。

Ahold Delhaize系荷兰与比利时合资，旗下拥有Albert Heijn、Delhaize、Food Lion和Hannaford等零售品牌。该公司在公布第三季度业绩时，披露了上述损失预估。此次网络攻击发生在第三季度结束之后。

公司预计，此次网络安全事件还将影响第四季度基础营业利润和按国际财务报告准则（IFRS）计算的营业利润，预计损失7500万至1亿欧元（约合5.6亿至7.5亿元人民币）。此外，公司还将承担事件响应和系统修复等相关费用，但预计这些费用对2026年按IFRS计算的营业利润影响不大。

原文链接：

[今年最高金额！零售巨头因网络攻击损失近20亿元](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516856&idx=1&sn=91e168ff0afe7ddee4774202f0fd85a1&scene=21#wechat_redirect)

**2、****未履行网络安全合规义务，某军工企业被罚超8600万元******

美国特拉华州一家国防与航空航天企业与美国政府机构近日达成和解。此前，美国政府指控该公司未能履行政府合同中规定的网络安全义务。

ILC是指ILC Dover和ILC Astrospace两家关联公司，该公司同意支付1300万美元（约合人民币8670万元），以了结美国政府依据《虚假申报法》提出的指控。相关合同涉及美国陆军部、美国导弹防御局和美国国家航空航天局（NASA）。

原文链接：

[未履行网络安全合规义务，某军工企业被罚超8600万元](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516884&idx=1&sn=fbc2f4c0b3415dfb4e9ef13eee73caeb&scene=21#wechat_redirect)

3、**无需虚拟机逃逸，配置缺陷引发 ESXi 与 Proxmox 大规模勒索加密**

卡巴斯基 GERT 团队披露两起虚拟化平台勒索攻击真实案例，两起事件均未利用虚拟机逃逸漏洞，攻击者依靠配置缺陷与凭证泄露拿下虚拟化管控层，完成集群加密。

第一起为 BlackNevas 勒索软件攻击 ESXi 环境，PRTG 监控系统持有 ESXi 的 root 账号，且多台主机复用同一组密码。攻击者攻陷监控平台后，经由 SSH 登录主机，关闭 execInstalledOnly 安全策略，上传并执行勒索恶意程序，横向加密多台 ESXi 节点。

第二起是 The Gentlemen 组织攻击 Proxmox 集群，攻击者攻陷管理员工作站，获取明文存储的 root 凭证，调用 VNC web socket 接口接管集群，对全部虚拟化环境实施加密。

报告归纳高危错误配置：监控账号权限过度、凭证复用、开放 root 直连 SSH、安全策略可被高权限账号关闭、明文保存特权凭据。报告建议将监控与管理权限分离，启用 Lockdown Mode，管控 SSH 访问，将配置变更纳入安全告警，同时强化凭证保管。该案例提示，补丁更新之外，虚拟化管理平面的配置加固同样不可忽视。

原文链接：

https://securelist.com/virtualization-security-esxi-and-proxmox-ransomware-cases/121819/

**行业动态**

**1、**欧盟《量子法案》草案曝光：PQC 要写成采购门槛了****

****监管情报媒体 MLex 披露了欧盟《量子法案》（Quantum Act）的草案全文，欧洲委员会定于 11 月 18 日正式提出。草案显示：关键部门的基础设施和设备采购，原则上必须"抗量子就绪 + 密码敏捷"——这是欧盟第一次拟以法律形式，把后量子密码要求写进采购规则。****

原文链接：

[欧盟《量子法案》草案曝光：PQC 要写成采购门槛了](https://mp.weixin.qq.com/s?__biz=MzUzNTU2NTYwNQ==&mid=2247519853&idx=1&sn=ab55d75c9f966f5ddde6bd7b0c73d73f&scene=21#wechat_redirect)

**2、******国科大密码学院在全同态加密高性能实现方面取得新进展，相关成果发表于 CHES 2026********

中国科学院大学密码学院郑昉昱副教授参加第二十八届密码硬件与嵌入式系统国际会议，并作学术报告，介绍课题组在全同态加密高性能实现方面的研究成果。会议期间，郑昉昱还与参会学者围绕全同态加密、密码算法高性能实现等问题进行了交流。

该论文围绕全同态加密中自举运算的性能瓶颈，提出了面向图形处理器（GPU）的统一高效自举框架 BOLT-FHE。全同态加密能够支持对密文数据直接进行计算，是实现数据安全处理和隐私保护的重要技术。但其中的自举运算计算量大、数据访问频繁，成为制约其实际应用效率的关键环节。针对这一问题，BOLT-FHE 结合 GPU 体系结构特点，采用片上局部分块和计算融合等技术，充分利用片上存储资源，减少数据传输与内核间同步开销，并为不同参数配置下的 TFHE 自举提供统一的实现框架。该研究为提升全同态加密的计算效率和推动隐私保护技术的实际应用提供了技术支撑。

原文链接：

[国科大密码学院在全同态加密高性能实现方面取得新进展，相关成果发表于 CHES 2026](https://mp.weixin.qq.com/s?__biz=MzUzNTU2NTYwNQ==&mid=2247519862&idx=2&sn=6a41cdffdbdac418da7e42f181596435&scene=21#wechat_redirect)

3、**纽约州AI安全法即将生效：OpenAI、Anthropic须在72小时内报告重大安全事件**

11月10日，美国纽约州正式开放前沿AI开发商注册平台，为2027年1月1日生效的《RAISE Act》（负责任AI安全与教育法案）做准备。OpenAI、Anthropic等大型AI企业将面临更严格的安全监管。

根据该法案，年营收超过5亿美元的前沿AI开发商须在2027年1月1日前完成注册，并履行三项核心义务：在官网公开安全框架、72小时内报告重大安全事件，以及定期发布公开的模型透明度报告。

新成立的数字创新、治理、诚信与信任办公室（DIGIT）将负责监管和执法。单次违规最高罚款100万美元，后续违规最高罚款300万美元。未按规定注册的企业也可能面临执法行动。

与此同时，纽约州州长Kathy Hochul宣布成立纽约AI责任与研究中心，依托Binghamton University独立评估先进AI系统的安全性、网络安全及运行情况，并协助DIGIT审查企业安全框架。该项目此前获得5500万美元资金支持。

美国各州正加速完善AI安全监管体系。加利福尼亚州SB 53法案要求企业在15天内报告重大安全事件，伊利诺伊州SB 315法案则引入独立安全合规审计。相比之下，纽约州72小时的报告时限更为严格，进一步提高了前沿AI企业的安全治理与事件响应要求。

原文链接：

https://techcrunch.com/2026/11/10/openai-anthropic-face-new-oversight-as-new-yorks-ai-safety-law-takes-effect/

**深度好文**

1、密码不买了，改租了：政务云换了一种密码供给方式？

四川省密码管理局官网 11 月 9 日发布《巴中市召开专题会议部署推进云平台密码资源池建设》：巴中市密码管理局组织召开商用密码应用专题推进会，听取巴中移动、联通、电信、数据集团四家云平台运营单位关于密码资源池建设和密评情况的汇报。

会议要求的部分，是一个完整的工程清单：各云平台运营单位要加快推动云平台密码资源池建设，全面梳理云平台政务信息系统承载情况，同步推进密码资源池扩容，强化跨平台密码服务、应用适配等技术支撑，做好信息系统批量集中调用密码服务的各项准备工作。

# 原文链接：

[密码不买了，改租了：政务云换了一种密码供给方式？](https://mp.weixin.qq.com/s?__biz=MzUzNTU2NTYwNQ==&mid=2247519850&idx=1&sn=7cf34ab6e8b893f9cb2bd7a428e59bfe&scene=21#wechat_redirect)

**2、云晓春院士：以系统思维筑牢智能时代网络安全人民防线**

**近年来，我国有序推进人工智能安全测评等工作，为网络智能技术行稳致远筑牢底座。这是总体国家安全观在人工智能治理领域的具体运用，体现了统筹发展和安全的内在要求。当前，算法被广泛运用于信息推送、风险研判、资源调配、公共服务等场景，这在极大提升社会运行效率的同时，也带来算法黑箱、数据滥用等问题。部分互联网平台为了绘制用户画像超范围采集个人信息，依托海量数据与算法规则形成数字权力，普通群众往往难以看清算法决策逻辑，权益受损时又难以依靠自身力量维权，这已成为目前网络安全治理亟须破解的现实难题。**

原文链接：

[云晓春院士：以系统思维筑牢智能时代网络安全人民防线](https://mp.weixin.qq.com/s?__biz=MzA5MzE5MDAzOA==&mid=2664268472&idx=2&sn=fafef7166ed3dc996e420e08edec4cd3&scene=21#wechat_redirect)

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/41AD92vfadSXHTH1scEGm9rr9ibJduPzOEm2eQUpLPWJwpsmlqCzCVuLrGgxBAlbjCqHzYrAhYfaP1XFyId58ew/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/XYUkuDD17Pickg7BesWrKzNdf4JtoCtsOH2Xibib98vGeiaQO53BHoFtelNwib4eLvZmeXPSRfM9hRFYC4Fl0MXEzvQ/640?from=appmsg)

**点点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/XYUkuDD17Pickg7BesWrKzNdf4JtoCtsOGmgiaibiat2qwrCSseEOYfyb86icshIsLqZ0YMHks4NsBvahmiaaofz1QTA/640?from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/B7LNzOKP0LJXMuChCUaliaCusxMWdjA128apnzfhqdEI9FH69rRrCIHzPyQ33nPQiakSUxhFxF5LhOKenaz5rjEQ/640?from=appmsg)

**点喜欢**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/41AD92vfadTn69kCsyd3JGMOAQ1beOTiba8Tg48QcxWibG2CPEWxAZcrpOj9noP6fCPUIELUGayNJEeZVdhWia0rw/0?wx_fmt=png)

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