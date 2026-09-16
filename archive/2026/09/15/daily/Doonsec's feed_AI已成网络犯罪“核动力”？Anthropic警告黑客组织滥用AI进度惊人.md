---
title: AI已成网络犯罪“核动力”？Anthropic警告黑客组织滥用AI进度惊人
url: https://mp.weixin.qq.com/s/1Ab9FSweRv8z_OB19ymlTw
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T06:59:18.134082
---

# AI已成网络犯罪“核动力”？Anthropic警告黑客组织滥用AI进度惊人

# AI已成网络犯罪“核动力”？Anthropic警告黑客组织滥用AI进度惊人

安全内参编译
安全内参编译

安全内参

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/mmbiz_jpg/wT9KAyOic0NBe7URsuIBFNfnhov8O52Lf38IFkcAtoicWEutEDpdUjSPZY47ChnW0zTMqf7QlvfNpZpUPdav2ibfe1pkJicmPKXtt3d0A6koYGw/640?wx_fmt=jpeg&from=appmsg)

Anthropic最新报告披露了近8个月以来大量滥用AI实施的网络犯罪活动，包括利用AI搭建针对百万级安卓APP、Github项目硬编码密钥的网络窃密流水线，数小时内完成后入侵环节窃取大量敏感数据，大规模编排国家级网络间谍活动等；

从上述案例可以看出，AI正在成为网络犯罪、诈骗、舆论操纵等犯罪活动的力量之源，显著降低了实施攻击所需的成本和规模。AI不再只是网络犯罪的工具，而是变成了其运行机制的组成部分。

前情回顾·AI网络攻击能力动态

* [首个AI智能体驱动的大规模漏洞利用：数天攻陷近400家企业](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516580&idx=1&sn=bd9b75622a8f018f62dec496c54cd44b&scene=21#wechat_redirect)
* [AI网络武器能力评估：中美哪家大模型遥遥领先？](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516547&idx=1&sn=78b6c98558f3723aae608aed7081935c&scene=21#wechat_redirect)
* [OpenAI警告：AI网络攻击将永不停歇，企业应做好防御准备](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516476&idx=1&sn=39e1f322a125cf3e11930ca3b191d493&scene=21#wechat_redirect)
* [首个政府预警！AI驱动攻击已对水务、能源等行业构成真实威胁](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516468&idx=1&sn=9965d010744a2b88eee0297016cac828&scene=21#wechat_redirect)

安全内参9月15日消息，美国AI巨头Anthropic日前发布报告称，多个威胁组织曾试图滥用其Claude AI模型从事恶意活动，其中包括出于经济利益实施攻击的黑客团伙、与俄罗斯等有关联的国家支持型间谍组织等。

![](https://mmbiz.qpic.cn/mmbiz_png/wT9KAyOic0ND7fSfJ7T3zVxAX6h1UKpgz72km3Eqz3l8icb5cFWRxHFAMfejVQMMcUU6kpKqBY0Tzowb74xBHKnXibngDLDyCo0lP3n7Mxza5k/640?wx_fmt=png&from=appmsg)

这家AI公司称，2025年12月至2026年8月期间，公司发现了多种形式的AI滥用行为，涉及网络攻击和影响行动、监控、诈骗、生物武器和常规武器研发，以及模型蒸馏等。

搭建网络窃密流水线

在近8个月里，Anthropic挫败了多起与ShinyHunters黑客组织有关的活动。该组织因大规模数据窃取攻击而臭名昭著，通常利用社会工程和账号入侵发动攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/wT9KAyOic0NAeU7ZRkhIWLEs4XIcNjRUjOfw7ibKt0Q6LHz6OMia3XPBZFTkmmYtwDah2eeWjtufXmyR6CtYCtyBib0BSJ9XsVmgLxdSW1dPibOo/640?wx_fmt=png&from=appmsg)

图：Anthropic视野的ShinyHunters组织的AI工作流

据称，一名使用“frkoo”网名、讲法语的ShinyHunters成员，将一套窃取凭据的攻击流程部署到10台AWS EC2云服务器上。这些服务器从多个应用商店下载应用，并扫描180万份安卓APK文件，查找机密信息。

Anthropic称：“这套流程从多个应用商店来源批量下载了180万份不同的安卓APK文件，对其进行反编译，并利用TruffleHog扫描其中硬编码的机密信息。”

“经过验证的结果会实时发送至一个Telegram群组，并按照100多种来源类型进行分类。”

同一攻击者还利用另一套自动化流程收集GitHub组织的电子邮件地址，并利用这些地址获取GitHub个人访问令牌（PAT）。

这两套攻击流程为“frkoo”提供了获取初始访问权限所需的凭据。Anthropic表示，这些凭据被用于该黑客“绝大多数已确认的入侵行动”。

Anthropic称，“frkoo”还搭建了一个名为policenationale[.]cc的盗刷卡交易网站，冒充法国国家警察，出售被盗支付卡数据、完整的持卡人信息，以及显示受害者地址的交互式地图。

疑似ShinyHunters成员还窃取AI API密钥，并利用这些密钥入侵其他组织或开展侦察活动。

在其中一起事件中，攻击者入侵了一家软件即服务（SaaS）提供商，并窃取了约200家下游客户的数据。

加快网络攻击速度

借助Claude，一名疑似ShinyHunters仅用约34小时，就窃取了身份验证数据，并获取了2100多组Azure AD身份验证令牌。这些令牌涉及40多个微软企业租户。Anthropic表示，“AI智能体几乎完成了全部工作”。

Anthropic还披露了其他与ShinyHunters关联人员有关的恶意活动，包括入侵一家科技服务商并窃取1TB数据、攻陷一家航空公司，以及访问一家能源企业的系统。

ShinyHunters在获得初始访问权限后行动迅速。在针对一家企业软件公司的攻击中，黑客仅用数小时便开始大规模窃取数据。

另一起事件中，攻击者从一枚被盗的开发者令牌入手，不到3小时便取得了系统的完整管理员控制权。

编排国家级网络间谍活动

Anthropic的报告介绍了与俄罗斯间谍组织“午夜暴雪”有关的活动。该组织利用Claude自动化开展恶意软件开发、信息搜集、基础设施采购、钓鱼攻击、持久化、命令与控制（C2）以及数据外传等工作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wT9KAyOic0NBeQeueoG1vxiaAwbCMyMgTzNdRtVCyLRVRuNMaGMpv6ZQVuXGhyauq6xiahVicwibyfatt34ByjWqNUgyKtGIfGLNKdUCK9emUrek/640?wx_fmt=png&from=appmsg)

图：Anthropic视野的“午夜暴雪”的AI工作流

该威胁组织还建立了一套反馈机制。一旦安全产品检测到恶意软件，系统就会自动重新构建恶意软件，以规避检测。

Anthropic发现，午夜暴雪的攻击目标包括20多个政府、国防、外交、情报和对外政策机构。

相关攻击行动涵盖设备代码钓鱼、ClickFix攻击、利用遭入侵的酒店Wi-Fi服务商实施DNS劫持、WhatsApp账号接管、云端电子邮件窃取，以及针对Windows、安卓和iOS系统的恶意软件攻击。Claude被用于攻击的各个阶段。

午夜暴雪还围绕Claude Code技能构建AI驱动的工作流，实现攻击行动自动化。人工操作人员主要在相关技能需要进一步完善时进行修改。

报告还披露了另一个黑客组织GTG-10007的间谍活动，该组织将Claude作为攻击行动的“工程和编排层”，用于协调一系列任务，具体如下：

* 针对生产系统发起入侵尝试；
* 对中东、欧洲和东南亚的外国政府网络开展侦察；
* 持续研究漏洞并开发针对主要终端安全产品的漏洞利用工具；
* 开发恶意软件；
* 搭建情报收集平台。

GTG-10007还运行自动化漏洞研究工作流，即使人工操作人员暂时离开，系统仍可自主开展工作，并在某款主要安全产品中发现了多项此前未知的漏洞。

此外，这套自动化系统还开发出了可用的漏洞利用工具，针对多个网络设备和安全设备产品系列。随后，该组织利用这些漏洞利用代码攻击了全球多个政府机构。

该组织的攻击行动涉及政府、教育、零售、能源、科技、医疗、金融和制造等领域的约50家机构。目前已确认遭到入侵的包括一家教育科技公司、一家零售企业和一家东南亚政府机构。

Anthropic表示，公司已阻断这些攻击者利用Claude从事恶意活动，并封禁了相关威胁组织的账号。

此外，Anthropic还根据此次发现的恶意使用情况调整了安全防护机制，增加了更快识别未来滥用行为的措施，并向执法部门、行业合作伙伴和受害者通报相关情况。

**参考资料：bleepingcomputer.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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