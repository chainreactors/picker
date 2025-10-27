---
title: Meta被指控利用81.7TB影子图书馆数据训练AI模型Llama；英国政府下令苹果公司创建后门，隐私争议再起 | 牛览
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651135017&idx=2&sn=6b43493a6bdbe33adb3dfad3d4d01126&chksm=bd15acfa8a6225ec1210c6d7638dcc3eb3f44cac131b95205da8e580db2b500a12029cd75f9e&scene=58&subscene=0#rd
source: 安全牛
date: 2025-02-11
fetch_date: 2025-10-06T20:38:29.066297
---

# Meta被指控利用81.7TB影子图书馆数据训练AI模型Llama；英国政府下令苹果公司创建后门，隐私争议再起 | 牛览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCb2ZNsiaibeeVyI8zTAkGaKEwJ4KibnH1c1CT6sZ9ezNZm2cDS004ZU6b4pwkMrY9Zx3BjicRR9KYh4Q/0?wx_fmt=jpeg)

# Meta被指控利用81.7TB影子图书馆数据训练AI模型Llama；英国政府下令苹果公司创建后门，隐私争议再起 | 牛览

安全牛

点击蓝字·关注我们 / aqniu

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBjwIRcuxcIx3fvDBydiaqkxw4o55dLPMJBKVsRbYl7ULkJDmFtatY9fWSIcZttiaeQm76cm0TXSBCA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**新闻速览**

* 工信部CSTIS：防范PLAYFULGHOST恶意软件风险
* LLMjacking攻击升级，黑客以月租30美元售卖大语言模型访问权限
* 英国政府下令苹果公司创建后门，隐私争议再起
* Meta被控利用81.7TB影子图书馆数据训练AI模型Llama
* 索尼PlayStation网络一度大面积中断，导致服务全线中断
* 网络攻击重创美国报业巨头，数十家报纸被迫缩版或停刊
* 英国工程巨头IMI证实遭黑客攻击，疑发生数据泄露
* 18岁“危险黑客”Natohub被捕，曾攻击北约等机构
* 网络攻击者利用SimpleHelp RMM漏洞实现持久访问和勒索软件攻击
* 网络安全初创公司Island估值飙升至45亿美元

**特别关注**

**工信部CSTIS：防范PLAYFULGHOST恶意软件风险**

近日，工业和信息化部网络安全威胁和漏洞信息共享平台（CSTIS）发布关于防范PLAYFULGHOST恶意软件的风险提示，指出PLAYFULGHOST恶意软件持续活跃，主要针对Windows用户实施攻击窃取敏感信息。

PLAYFULGHOST恶意软件攻击目标主要针对搜狗、QQ和360安全等应用程序，通过钓鱼邮件和搜索引擎优化（SEO）投毒技术分发经过篡改的合法VPN应用程序（如LetsVPN）进行传播。在感染过程中，PLAYFULGHOST利用DLL劫持、侧加载等技术，加载恶意DLL文件，进而解密并将PLAYFULGHOST注入内存。一旦感染成功，攻击者将控制系统，进行键盘记录、屏幕截图、远程Shell访问以及文件传输与执行等恶意活动。此外，PLAYFULGHOST在攻击过程中使用了Mimikatz（密码提取工具，用于从内存中提取明文密码）与Rootkit（隐藏工具，能够隐藏自身及恶意行为），并利用Terminator开源工具，通过植入自带漏洞驱动（BYOVD）终止安全进程，进一步增强其功能性和隐蔽性。

CSTIS建议相关单位及用户立即组织排查，及时更新防病毒软件，定期实施全盘病毒查杀和重要数据备份，谨慎点击不明来源的链接或下载运行来源不明的应用程序，加强网络安全意识培训，防范网络攻击风险。

原文链接：

https://mp.weixin.qq.com/s/F2OMMJQ84yhLjKQRGKDHUQ

**热点观察**

**LLMjacking攻击升级，黑客以月租30美元售卖大语言模型访问权限**

Sysdig研究人员观察到，LLMjacking正在商业化，通过ORP（反向代理服务器）出售大语言模型的访问权限。据报道，一个实例每月售价为30美元，而一个运行仅4.5天的实例就产生近5万美元的费用。

LLMjacking攻击由于利用云端大语言模型的高昂费用而兴起，黑客通过入侵账户来免费使用这些昂贵服务。ORP是当前LLMjacking的常用方式，通过Nginx或TryCloudflare等动态域名暴露服务器，充当各种大语言模型的反向代理，从而掩盖攻击者的来源。这些代理中常包含从OpenAI、谷歌AI、Mistral AI等多家供应商窃取的大量API密钥。凭证盗窃是LLMjacking的重要一环，黑客针对易受攻击的服务，利用验证脚本识别访问机器学习服务的凭证。公开资源库中也存在暴露的凭证。4chan、Discord等网络社区促进了通过ORP共享大语言模型访问权限，Rentry.co则被用来分享工具和服务。

研究人员指出，为遏制LLMjacking，确保访问密钥安全、实施强大的身份管理至关重要，包括避免硬编码凭证、使用临时凭证、定期轮换访问密钥，并监控暴露凭证和可疑账户行为。

原文链接：

https://hackread.com/hackers-monetize-llmjacking-selling-stolen-ai-access/

**英国政府下令苹果公司创建后门，隐私争议再起**

近日，英国政府下令苹果公司为其创建一个后门，允许他们检索任何苹果用户在全球范围内上传到云端的所有内容。

这项于上月发布的未公开命令，要求苹果拥有查看完全加密材料的全面能力，而不仅仅是协助破解特定账户。这在主要民主国家中从未有过先例。知情人士表示，该命令的执行将标志着科技公司在几十年来与政府对抗、避免被利用来监视用户的斗争中遭受重大失利。

这一命令引发了广泛关注，因为它可能会严重损害苹果用户的隐私和数据安全。加密技术被广泛认为是保护个人隐私和网络安全的关键手段，但政府一直希望能够在必要时访问加密数据。这场争论在英国此次命令中达到了新的高度。苹果公司长期以来一直坚持不会在其产品中设置后门，并多次拒绝了政府的相关要求。但这项空前的命令可能会迫使苹果做出让步。如果苹果拒绝执行，则可能会面临严重的法律后果和声誉损失。

此事再次引发了隐私与安全之间权衡的争论。支持者认为，这一命令有助于打击犯罪和保护国家安全。但批评人士则担心，它会破坏加密技术的完整性，并为政府监视大众打开方便之门。

原文链接：

https://www.washingtonpost.com/technology/2025/02/07/apple-encryption-backdoor-uk/

**Meta被控利用81.7TB影子图书馆数据训练AI模型Llama**

近日，Meta公司被指控在训练其Llama人工智能模型时，非法使用了81.7TB来自暗网图书馆的盗版书籍数据。以作家理查德·卡德里等人为代表的原告方指控Meta公司从Z-Library和LibGen等暗网图书馆下载了大量盗版作品，尽管内部曾对此行为的合法性和道德性提出质疑。

原告方声称，Meta在2024年12月13日临时披露了2000多份文件，其中包含员工关于使用盗版素材训练AI的内部交流记录。根据解密的电子邮件，有Meta员工明确表示"使用盗版材料已经超出了我们的道德底线"，另一名员工则称Meta使用LibGen一事已上报给CEO扎克伯格。一些员工警告盗版行为的非法性，但Meta却试图掩盖，直至2024年4月仍在秘密下载和共享暗网图书馆的数据。

原告方表示，他们正寻求重新审问关键证人、获取Meta的下载记录和即将发布的Llama新版本训练数据集，并要求法院根据"犯罪-欺诈例外"审查Meta律师的特权通信。如果原告胜诉，可能会为科技行业在AI开发中使用未经授权内容设置新的责任标准。Meta公司尚未对最新指控作出公开回应。

原文链接：

https://cybersecuritynews.com/meta-trained-its-llama-ai-models-using-81-7-tb-of-books-stolen-from-torrent-shadow-libraries/

**18岁“危险黑客”Natohub被捕，曾攻击北约等机构**

西班牙警方通过联合行动成功逮捕了一名被指控对西班牙和国际知名组织发动40多起网络攻击并窃取了大量个人数据和敏感文件"危险黑客"Natohub。

这名18岁的嫌疑人在Breach Forums网站上使用"Natohub"的昵称，其攻击的受害机构包括西班牙国民警卫队、国防部、教育部、国家钞票和印花厂、多所大学以及瓦伦西亚自治区政府。在国际上，北约、美国陆军、联合国和国际民航组织的数据库也遭到攻击。根据西班牙警方的新闻发布会，这名嫌疑人利用匿名消息应用程序和专门的导航工具，构建了一个复杂的技术网络，使追查工作变得极为困难。警方从嫌疑人住所查获了计算机设备、一部iPhone和约50个加密货币账户。

西班牙情报机构国家密码中心、欧洲刑警组织和美国国土安全调查局也参与了这一行动。此次逮捕是西班牙执法部门打击网络犯罪的一部分，他们与国际机构合作，旨在摧毁源自西班牙境内的网络犯罪活动。

原文链接：

https://hackread.com/teen-hacker-natohub-caught-nato-un-us-army-breach/

**网络攻击**

**索尼PlayStation网络一度大面积中断，导致服务全线中断**

2月8日，索尼PlayStation网络遭遇大规模中断，导致全球玩家无法访问关键在线功能，包括账号登录、在线游戏、PlayStation商店等，引发玩家的强烈不满。

根据索尼官方状态页面显示，受影响的服务包括账号管理、游戏及社交功能、PlayStation视频、PlayStation商店、PlayStation直营店。此次中断不仅波及PS5和PS4，PS3、PSVita以及基于网页的访问均受影响，说明问题范围广泛，并非针对特定主机或地区。对许多人来说，PlayStation主机不仅是游戏设备，也是流媒体、数字购物和社交互动的娱乐中心。此次长时间中断影响了依赖PlayStation观看影视、在线购物的用户，加剧了不满情绪。

根据PlayStation网络服务状态页面和索尼官方社交媒体账号，所有受影响服务已恢复。索尼尚未披露具体中断原因，网上猜测包括服务器故障甚至网络攻击，但没有官方证实。导致当天长时间中断的具体原因仍有待查明。

原文链接：

https://hackread.com/playstation-network-down-outage-gamers-frustrated/

**网络攻击重创美国报业巨头，数十家报纸被迫缩版或停刊**

美国媒体公司李企业集团近日遭遇"网络安全事件"，导致旗下数十家报纸陷入混乱，部分报纸被迫缩短版面或暂停印刷。但未透露攻击发生方式或幕后黑手。

李企业集团拥有《圣路易斯邮报》等70多家日报，以及近350家周报和专业刊物，分布于25个州。其旗下报纸报道了此次网络攻击，大多数问题始于上周一。每家报纸都详细介绍了攻击如何扰乱了它们的运营。位于弗吉尼亚州夏洛茨维尔的《每日进步报》和威斯康星州拉克罗斯的《拉克罗斯论坛报》均表示，自上周一以来一直无法印刷报纸。

网络攻击不仅影响了报纸的印刷和发行，也可能导致敏感数据泄露、系统瘫痪等严重后果。该公司发表声明称，目前其重点是确定是否有任何信息受到影响，并正在尽快彻底地调查此事。

原文链接：

https://www.nytimes.com/2025/02/09/business/media/newspaper-cyberattack-lee-enterprises.html

**英国工程巨头IMI证实遭黑客攻击，疑发生数据泄露**

英国工程公司IMI近日向伦敦证券交易所提交报告，证实公司系统遭到"未经授权访问"，成为最新一家遭遇网络攻击的工程巨头。

据科技媒体TechCrunch报道，IMI拒绝进一步讨论此事，因此目前无法确定攻击的性质、黑客身份或其入侵IMI基础设施的方式。英国信息专员办公室透露，IMI已就此次事件提交了数据泄露报告，因此可以推断至少有部分公司数据被盗。信息专员办公室正在"评估IMI提供的信息"。

IMI成立于1862年，主营精密工程、关键工程和水力工程等领域，服务于石油天然气、制药、电力和运输等行业。2023财年，IMI报告了3.98亿美元的税前利润，同比增长6%。

原文链接：

https://www.techradar.com/pro/security/imi-confirms-hack-becomes-latest-engineering-giant-to-face-cyberattack

**网络攻击者利用SimpleHelp RMM漏洞实现持久访问和勒索软件攻击**

近日，网络安全公司Field Effect发现，黑客正在利用近期披露的SimpleHelp远程监控和管理(RMM)软件安全漏洞， 获得初始访问权限，并在未经授权的目标网络中维持持久远程访问，最终可能部署勒索软件。

相关漏洞CVE-2024-57726、CVE-2024-57727和CVE-2024-57728于上月由Horizon3.ai披露，可能导致信息泄露、权限提升和远程代码执行。在Field Effect分析的事件中，攻击者通过位于爱沙尼亚的一个易受攻击的SimpleHelp RMM实例获得了目标终端的初始访问权限。获取远程连接后，攻击者进行了一系列后渗透行动，包括侦查和发现操作，以及创建名为"sqladmin"的管理员账户，以便部署开源框架Sliver。攻击者随后利用Sliver提供的持久性功能，在网络中横向移动，在域控制器(DC)和易受攻击的SimpleHelp RMM客户端之间建立连接，并最终安装Cloudflare隧道，通过Cloudflare的基础设施将流量隐蔽地路由到攻击者控制的服务器。

Field Effect在这一阶段检测到了攻击，阻止了尝试执行隧道，并将系统与网络隔离，防止进一步入侵。如果攻击未被发现，Cloudflare隧道可能会被用作渠道，获取其他有效载荷，包括勒索软件。

原文链接：

https://thehackernews.com/2025/02/hackers-exploit-simplehelp-rmm-flaws.html

**行业动态**

**网络安全初创公司Island估值飙升至45亿美元**

随着企业对安全浏览器的需求不断增长，网络安全公司Island的估值自2023年10月以来已经增长了四倍。彭博社报道，Island正在新一轮融资中以45亿美元的估值筹集资金。

2024年4月，Island在D轮融资中筹集了1.75亿美元，估值较之前翻了一番，达到30亿美元。而在2023年10月的C轮融资中，Island以15亿美元的估值筹集了1亿美元。迄今为止，Island已经总共融资4.87亿美元。D轮融资由新投资者Coatue和现有投资者红杉资本(Sequoia Capital)牵头，其他现有投资者如Insight Partners、Stripes、Georgian和Prysm Capital也参与其中。

Island目前在全球拥有超过250名员工，估计年收入将达数千万美元。据悉，Island企业浏览器旨在为企业提供高级安全性、IT和网络控制、数据保护、应用程序访问和高级生产力功能。使用该浏览器，安全团队可以完全控制最后一英里，从基本保护如复制、粘贴、下载、上传和屏幕截图捕获，到更高级的安全需求，如数据编辑、数字水印和多因素身份验证插入。

原文链接：

https://www.calcalistech.com/ctechnews/article/r19pbmbtye

![](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkAibeib6HUSIXJ4IhpazTYic3uwicySgIEk8ZeMC7X5evYXoNPHxoUlibqgo6Ilq0dRkGrMKibWtfcibYwsg/640?wx_fmt=jpeg)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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