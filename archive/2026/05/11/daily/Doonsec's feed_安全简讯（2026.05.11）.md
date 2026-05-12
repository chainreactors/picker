---
title: 安全简讯（2026.05.11）
url: https://mp.weixin.qq.com/s/RodLjAYh1q_fB1LFUVvI7A
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:37:31.937150
---

# 安全简讯（2026.05.11）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309Zry4bH2duPtS4szjCgwNibJQrAezs2mMOnhAPQbt66K6W34atrPYQaJqKbSNnJWfYn9uuzW7FsOZWV93YhAtAwGncxf6hTkeiamSg/0?wx_fmt=jpeg)

# 安全简讯（2026.05.11）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. 恶意广告滥用Claude共享聊天记录攻击Mac用户**

5月10日，近日，一场针对macOS用户的恶意广告活动正在活跃进行，攻击者巧妙利用Google Ads和Anthropic公司的Claude.ai共享聊天记录功能传播恶意软件。安全工程师Berk Albayrak首先发现了这一威胁，并在社交平台上发出警告。当用户搜索“Claude mac 下载”等关键词时，赞助搜索结果会显示指向合法域名claude.ai的链接，但实际上用户会被诱导执行恶意指令。攻击者武器化了Claude的共享聊天功能，创建了看似官方“Mac版Claude Code”安装指南的聊天记录，甚至标注来自“Apple支持”。这些聊天提示引导用户打开终端并粘贴Base64编码的命令，该命令会在Mac上静默下载并运行恶意软件。研究人员发现了两个独立变种，它们结构相同但使用不同的域名和有效载荷。其中一个变种通过多态交付技术，为每个请求提供独特混淆的有效载荷，使安全工具难以基于哈希或签名进行检测。另一个变种则直接执行信息窃取，收集浏览器凭证、Cookie和macOS钥匙串内容，并将其打包泄露。

https://www.bleepingcomputer.com/news/security/hackers-abuse-google-ads-claudeai-chats-to-push-mac-malware/

**2. 德国警方再次捣毁重启后的Crimenetwork犯罪市场**

5月10日，德国当局近期成功关闭了重新上线的网络犯罪交易平台“Crimenetwork”，并逮捕了其运营者。Crimenetwork原是德国最大的在线网络犯罪交易平台，自2012年开始运营，拥有约10万注册用户，主要提供非法服务、毒品和被盗数据的交易。2024年末，法兰克福检察官办公室、中央打击网络犯罪办公室和联邦刑事警察局联合行动，查封了该平台并逮捕了其一名管理员。然而，仅几天后，该平台便以相同名称在新运营商的管理下重新上线，并搭建了全新的技术基础设施。本周早些时候，一名涉嫌管理新版Crimenetwork的35岁德国男子在西班牙马略卡岛的住所被西班牙国家警察特别小组根据欧洲逮捕令抓获。德国联邦刑事警察局表示，嫌疑人被指控在前一版本关闭、前管理员被捕后迅速重建了该犯罪平台。重启后的平台同样提供非法商品和服务，并迅速吸引了约2.2万名用户和100多家供应商。警方收集的证据表明，新版Crimenetwork至少产生了360万欧元的收入。此外，警方还查获了约19.4万欧元的涉嫌非法资产，并获取了大量用户和交易数据，以支持后续调查。

https://www.bleepingcomputer.com/news/security/police-shut-down-reboot-of-crimenetwork-marketplace-arrest-admin/

**3. JDownloader官网被黑，恶意安装程序植入Python木马**

5月9日，热门下载管理器JDownloader的官方网站遭到入侵，攻击者篡改下载链接，向用户分发带有恶意软件的Windows和Linux安装程序。此次供应链攻击发生在2026年5月6日至7日期间，通过Windows“下载备用安装程序”链接或Linux shell安装程序从官网下载安装包的用户均受到影响。该漏洞最初由Reddit用户“PrinceOfNightSky”发现，他注意到下载的安装程序被Microsoft Defender标记为恶意软件，且开发者显示为“Zipline LLC”或“The Water Team”，而非合法的开发商Appwork。JDownloader开发团队随后证实网站遭入侵，并将网站下线调查。攻击者利用了一个未修补的漏洞，通过网站的内容管理系统在未经身份验证的情况下更改了访问控制列表和页面内容，但并未获得对底层服务器文件系统或操作系统的控制权限。此次事件仅影响了备用Windows安装程序链接和Linux shell安装程序链接，应用内更新、macOS下载、Flatpak、Winget、Snap软件包及主JAR包均未受影响。开发人员提醒用户，合法安装程序应由“AppWork GmbH”进行数字签名，未签名或签名名称不符的文件应避免使用。

https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/

**4. Hugging Face恶意存储库借OpenAI之名传播窃密木马**

5月9日，一个名为“Open-OSS/privacy-filter”的恶意存储库近期登上人工智能模型托管平台Hugging Face的热门榜单首位，并累计获得约24.4万次下载，随后被平台下架。该存储库冒充OpenAI的“隐私过滤器”项目，向Windows用户传播窃取敏感信息的恶意软件。HiddenLayer公司的研究人员于5月7日发现了这一攻击活动。研究人员指出，该恶意存储库抢注了OpenAI合法隐私过滤器的名称，几乎逐字复制了其模型卡内容，同时提供了一个名为“loader.py”的恶意文件。该Python脚本表面包含与AI相关的伪造代码以掩饰其真实意图，实际则在后台禁用SSL验证，解码Base64编码的外部资源URL，获取并执行包含PowerShell命令的JSON负载。该命令在不可见窗口中运行，下载一个用于提权的批处理文件，继而下载最终有效载荷“sefirah”，将其添加到Microsoft Defender的排除列表后执行。最终有效载荷是一个基于Rust语言编写的信息窃取程序。研究人员还强调，该恶意软件具备广泛的反分析功能，能够检测虚拟机、沙箱、调试器和分析工具，从而逃避安全分析系统的监测。

https://www.bleepingcomputer.com/news/security/fake-openai-repository-on-hugging-face-pushes-infostealer-malware/

**5. 全球最大食品供应商Sysco遭麒麟勒索团伙攻击**

5月6日，全球最大的食品供应商Sysco近日成为勒索软件组织“麒麟”的最新受害者。该组织在其暗网受害者博客上发布了Sysco的相关信息，并设定了最后期限，要求该公司在5月12日之前就赎金事宜与其联系。Sysco成立于1969年，总部位于美国德克萨斯州休斯顿，业务覆盖全球10个国家，拥有超过340个配送中心和约7.5万名员工，为餐厅、医院、学校、酒店、政府机构、军事设施、航空公司、游轮、体育场、赌场及超市等约75万个地点供应近500种食品、烹饪用品及餐厅设备。麒麟组织作为此次攻击的声称方，提供了三个样本文件作为其涉嫌未经授权访问Sysco IT网络的证据。第一个样本日期为2021年至2022年，盖有“机密”印章，内容是一份采用公式计算的食品客户定价表；第二个样本是2026年2月向明尼苏达州一家当地餐馆开具的客户发票；第三个样本日期为2025年6月，显示的是某食品用纸供应商提交给伊利诺伊州税务局的转售税证明文件。不过，该组织并未说明据称从Sysco服务器窃取的数据总量或具体类型。

https://cybernews.com/news/sysco-qilin-ransomware-claim-food-supplier/

**6. 黑客兜售声称窃自Coinbase的50万法国用户数据集**

5月7日，一名网络威胁者正在黑客论坛上兜售一个据称包含50万法国加密货币用户的数据集，并声称这些数据是从知名交易平台Coinbase窃取的。卖家提供了多种购买“套餐”，包括所谓的“入门包”和高级访问权限，这种结构化销售方式与网络钓鱼及加密货币攻击生态系统中常见的策略高度相似。攻击者上传的示例截图显示了23条疑似用户的个人身份信息记录，包括全名、电子邮件地址、物理地址和电话号码。虽然这些信息看起来指向真实的法国个人，但样本中没有任何内容能够明确将这些数据与Coinbase用户直接关联起来。如果这些数据被证实属实，相关用户将面临更高的社交工程和网络钓鱼攻击风险。这一安全漏洞指控可能加剧Coinbase在安全方面长期面临的困境，尤其是涉及社交工程和网络钓鱼的攻击。

https://cybernews.com/security/coinbase-france-data-leak-500k-users/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

启明星辰安全简讯

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

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