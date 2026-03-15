---
title: 在看 | 周报：工信部通报24款侵害用户权益的APP及SDK；深圳程序员因OpenClaw疏漏，3天损失1.2万元
url: https://mp.weixin.qq.com/s/0VfpCoFPJibkpLAk-j6WJg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:26:42.201430
---

# 在看 | 周报：工信部通报24款侵害用户权益的APP及SDK；深圳程序员因OpenClaw疏漏，3天损失1.2万元

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38nTRvKLpoqoXqeVic62ibaIJvtgiankmicl8nIYognnwqRFj8RPC3e7XouV01BHHd2k9ppdWcbEqlrUw/0?wx_fmt=jpeg)

# 在看 | 周报：工信部通报24款侵害用户权益的APP及SDK；深圳程序员因OpenClaw疏漏，3天损失1.2万元

原创

管窥蠡测
管窥蠡测

安在

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT39x3nndZanlbZOk0K8ibhGOS3mskN8Bwx0bJ9KgpRsYSJ106ib1991xicajm3DeAcXdpEVl2icku02jBg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**[导读]**

本周周报围绕数据安全及个人信息保护、AI 安全、网络安全三大核心板块展开。梳理了工信部通报违规 APP、多起国内外重大数据泄露与网络攻击事件，重点关注 OpenClaw 开源框架的系列安全漏洞及实际受害案例，同时解析了文言文突破大模型防线、新型网络攻击技术等新风险，为相关主体防范各类网络安全威胁提供核心参考。

**数据安全及个人信息保护**

[1、工信部通报24款侵害用户权益的APP及SDK](https://mp.weixin.qq.com/s?__biz=MjM5OTUwMTc2OA==&mid=2650948151&idx=1&sn=39cdb5bcd1a6acb12ee218b561d54789&scene=21#wechat_redirect)

3月13日，工信部发布2026年第2批侵害用户权益行为通报，经第三方检测机构抽查，共发现24款APP及SDK存在违规行为，问题集中在违规收集个人信息、强制频繁过度索取权限、信息窗口乱跳转、SDK信息公示不到位等方面。工信部要求涉事主体按规整改，整改不到位将依法依规开展处置。

[2、美国教育行业高层敏感联系数据库泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074555&idx=3&sn=f61b2e905144b2bbad4c6f2a6eefc31a&scene=21#wechat_redirect)

暗网论坛出现美国教育行业敏感数据泄露事件，发帖人免费公开了约9000条美国校长与督学的完整数据库记录，覆盖全美50个州。每条记录包含姓名、邮箱、电话、学校信息、地址等15个敏感字段，数据源自商业邮箱列表供应商，此次公开将大幅降低针对相关人员的网络攻击与诈骗门槛。

[3、医疗设备巨头遭史诗级数据擦除：公司完全停摆、大量员工电脑手机被清空](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515670&idx=1&sn=a83b469ceac2025f4e94eeab3b40ad16&scene=21#wechat_redirect)

因遭受伊朗黑客组织Handala的数据擦除攻击，万亿市值的美国医疗设备巨头史赛克业务完全停摆，内部微软业务环境全球范围中断，员工反馈大量服务器被清空、工作应用无法使用、员工工作电脑手机也被清空；该组织声称，已清除了超20万个服务器、系统和移动设备，窃取了超50TB的内部数据。

[4、伪装OpenClaw，恶意GhostClaw大肆洗劫开发者数据](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

近期，名为GhostClaw的恶意软件伪装成OpenClaw开发者工具，通过npm包传播。该软件利用社会工程学诱骗开发者输入系统密码，在后台静默安装恶意程序，窃取开发者的SSH密钥、浏览器密码、加密钱包信息等敏感数据，覆盖macOS、Linux和windows三大平台。

[5、阿联酋国防部网络中心机密文件数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074672&idx=2&sn=0ccdef7c5a1b3ce01b4cfd8a8d22e057&scene=21#wechat_redirect)

威胁行为者JRINTEL在暗网公开泄露阿联酋国防部网络中心机密文件，压缩包达68.6MB，含2021至2026年多份PPT提案。文件披露其构建“第五域”进攻性网络能力的路线图，包括本土网络战士培训、零日漏洞培养、收购美企策略及年度预算等核心机密，威胁等级高，或加剧海湾网络军备竞赛，泄露动机为经济利益。

[6、乐天信用卡违反《个人信息保护法》，被罚超4400万元](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515674&idx=1&sn=c1822b23879433ef46e07a9b9c830046&scene=21#wechat_redirect)

3月13日消息，韩国个人信息保护委员会（PIPC）表示，委员会决定因违反《个人信息保护法》对乐天信用卡处以96.2亿韩元行政罚款，并追加480万韩元罚金。同时，委员会还发布了整改命令和公开披露命令。

**AI安全**

[1、深圳程序员因OpenClaw疏漏，3天损失1.2万元](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247653092&idx=2&sn=d685f423323fec062dc9ef43eceb2876&scene=21#wechat_redirect)

近日，深圳一名软件开发从业者因开源AI智能体框架OpenClaw的使用与配置疏漏，遭遇API密钥泄露和恶意盗刷，短短3天内累计产生1.2万元的非正常服务扣费，成为近期AI智能体安全风险集中爆发期的典型个人用户受损案例。

[2、国家信息安全漏洞库（CNNVD）通报了OpenClaw多个安全漏洞](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247653038&idx=2&sn=967cc99601549ddb298f11a953d64110&scene=21#wechat_redirect)

根据国家信息安全漏洞库（CNNVD）统计，自2026年1月-2026年3月9日，共采集OpenClaw漏洞82个，其中超危漏洞12个，高危漏洞21个、中危漏洞47个、低危漏洞2个，包含了访问控制错误、代码问题、路径遍历等多个漏洞类型。OpenClaw多个版本受到漏洞影响。

[3、工信部发布关于防范OpenClaw开源AI智能体安全风险的预警提示](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247653001&idx=2&sn=edefca274359bfcba3fdf467cd81616e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpfvsQZEnoqMKCCu9ibjwgI9YicQoFEwtxHBppqlrAVtYFqlDKR9pticiaic2yAYa54HUoQy5Ysp8JTlZNOONp21CI4k3UT9aZib0eOVA/640?wx_fmt=png&from=appmsg)

[4、研究证实文言文可100%突破主流大模型安全防线](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074602&idx=1&sn=71541cba8e88493809b1ead0467372e1&scene=21#wechat_redirect)

ICLR 2026收录的研究显示，文言文可绕过当前主流大模型的安全检测机制。研究团队设计的CC-BOS攻击框架，结合文言文提示词工程与仿生优化算法，对GPT-4o、Claude-3.7、Gemini等六大顶级大模型攻击成功率达100%，平均仅需1-3次尝试，且跨模型迁移能力极强，暴露了大模型体系的普遍安全弱点，也给AI智能体带来全新安全挑战。

[5、腾讯版小龙虾WorkBuddy爆火致服务不稳定，公司致歉并紧急扩容](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074555&idx=1&sn=34ac7df2817d6d6a28a9276c0d93309f&scene=21#wechat_redirect)

腾讯旗下全场景AI智能体WorkBuddy（腾讯版小龙虾）正式上线后，因用户访问量远超预期，出现登录及服务不稳定故障。官方随即发布致歉信，技术团队已第一时间紧急扩容10倍，目前服务已完全恢复稳定。

[6、麦肯锡AI平台遭红队AI智能体攻陷，数千万条敏感数据可被访问](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515662&idx=1&sn=da8c2dc81017a413362c5e32f3ce20a6&scene=21#wechat_redirect)

红队安全企业CodeWall的自主进攻型AI智能体，在无预先凭证的情况下，仅用2小时就入侵了麦肯锡内部生成式AI平台Lilli，获取其生产数据库完整读写权限，可访问4650万条明文聊天记录、72.8万个含客户机密的文件等核心数据。此次攻击源于公开暴露的API端点与SQL注入漏洞，麦肯锡已在数小时内完成漏洞修复，称未发现客户数据被非法访问。

**网络安全**

[1、国家网络安全通报中心公布重点防范境外恶意网址与IP](https://mp.weixin.qq.com/s?__biz=MzA5MzE5MDAzOA==&mid=2664260053&idx=3&sn=477d45d73d6941588a165559600da6ba&scene=21#wechat_redirect)

2026年3月，国家网络与信息安全信息通报中心公布一批境外恶意网址和IP，其归属地主要涉及美国、英国、德国、瑞典、新加坡，关联SoftBot、NjRAT等多种木马及僵尸网络程序，可发起DDoS攻击、远程控制、数据窃取等恶意行为，对国内联网单位和用户构成重大威胁。

[2、新型 “Zombie ZIP” 技术让恶意软件绕过安全工具](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074639&idx=2&sn=a9136aab554468e0643fa955a64f6248&scene=21#wechat_redirect)

安全研究员研发的“ZombieZIP”新型规避技术，可通过操纵ZIP文件头，将恶意压缩载荷伪装成未压缩数据，让安全工具无法识别恶意特征，可绕过VirusTotal平台51款杀毒引擎中的50款，相关概念验证代码已公开，该问题已分配CVE-2026-0866编号。CERT/CC已发布风险警告，敦促安全厂商完善检测机制，同时提醒用户警惕陌生来源压缩文件。

[3、新型ClickFix攻击激增500%，虚假验证码诱骗Mac用户运行恶意代码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074602&idx=3&sn=ade2e5b7f2961b4a3f5082131d35b995&scene=21#wechat_redirect)

ClickFix新型攻击近期快速蔓延，其2024至2025年检测量激增超500%，已成为增长最快的社会工程学威胁之一。攻击者通过伪造人机验证页面，诱骗Mac用户在系统终端粘贴执行恶意命令，利用系统自带工具绕过常规安全防护，进而窃取浏览器凭证、加密货币钱包等敏感数据。专家提醒，正规验证绝不会要求用户执行终端命令，遇此类提示应直接关闭页面。

[4、Windows系统级漏洞开卖：要价超150万元！可获系统级权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074602&idx=2&sn=a2631a48700407c06cf33e85949c71f4&scene=21#wechat_redirect)

暗网市场出现Windows零日漏洞售卖信息，卖家以22万美元（约合人民币151万元）兜售编号为CVE-2026-21533的Windows远程桌面服务漏洞。该漏洞可助力攻击者获取系统级权限，微软已于2026年2月发布补丁完成修复，覆盖主流Windows桌面及服务器系统，黑客售卖核心瞄准未及时更新补丁的企业级用户。

[5、维基百科遭 JavaScript 蠕虫攻击，数千页面被恶意篡改](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074508&idx=3&sn=0b609a09de916ae555c540378853c449&scene=21#wechat_redirect)

维基媒体基金会（WikimediaFoundation）披露旗下维基百科近期遭遇网络攻击事件，多个百科页面遭到一种具备自我传播能力的JavaScript蠕虫入侵，为防止攻击蔓延，开发团队暂时限制了部分编辑功能，并紧急恢复受影响的页面内容。

**RECOMMEND**

推荐阅读

# [●](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652760&idx=1&sn=91ee011e26421e6018bb3d721677098b&scene=21#wechat_redirect)在看 | 周报：浦发建行涉数据安全违规合计被罚8600万元； OpenClaw删光Meta安全总监邮箱

# [●](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652596&idx=2&sn=f2c956b45b4e314f83f22a07ae1f75ca&scene=21#wechat_redirect)在看 | 周报：重庆某企业未履行网络安全保护义务，企业负责人被约谈；广东中山查获一起无人机黑飞案

#

#

[●](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652934&idx=1&sn=63f61e578df72d7530cb86c078f57123&scene=21#wechat_redirect)在看 | 周报：北京农商行因数据安全问题被罚100万；央行重庆分行开出大额支付罚单

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT3ibRpa5yOEg8zZ5voaDbvKA75C5LJDKwGFzKfWoxFGdDfCOUYRAiaH27KC1O6npvh4UbX3ZWliblsiatg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

扫码加入诸子云知识星球。

**END**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AAfIzicyojXwPTCxD0QGZHhyRcRicJAHhUv382sYFibICoxjzktlJwEEPag/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AApXU9ib7vkMD4KMHhjVfkTqOCUrDibUaBDoH0OGGCMasLLJyv5xppK6rA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AArbhGtTxVSkCv3A7f6fo6n1dmFJEGEtMuDxGyeR81CndSR08OKTGQaw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38HPkvxLkOy5rLCeVBtj8H9SUbVPNZbibc4N2knPCDFjTKduRLhiaAZVQShUa2IZqsBShI2GG2dpqBg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

点击这里阅读原文

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

安在

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEX...