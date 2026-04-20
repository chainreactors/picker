---
title: 国外：一周网络安全态势回顾之第146期，全球知名教育出版商麦格劳-希尔数据泄露
url: https://mp.weixin.qq.com/s/ZHZ5vXYNEanq0CO152ClXg
source: Doonsec's feed
date: 2026-04-19
fetch_date: 2026-04-20T04:54:50.721388
---

# 国外：一周网络安全态势回顾之第146期，全球知名教育出版商麦格劳-希尔数据泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hfjKPyxBDjogJ2SF8qZ0ic8ibE3gkxDdXvtd2J8PdFhbdGQJoatWCdLdibHQbGTUMfywCqQn9WZFncIsBFlvVgZxmMkyLoxicVcGf6TsmhzQlws/0?wx_fmt=jpeg)

# 国外：一周网络安全态势回顾之第146期，全球知名教育出版商麦格劳-希尔数据泄露

原创

铸盾安全
铸盾安全

河南等级保护测评

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下是本周的精彩亮点：

**参议院采取行动加强商业卫星防御**

由参议员加里·彼得斯和约翰·科宁共同提出的两党法案近期通过了关键的委员会审批，旨在帮助卫星运营商打击黑客和外国敌对势力。《2025年卫星网络安全法案》指示商务部建立一个安全最佳实践中心资源库，并要求美国政府问责局（GAO）对卫星网络安全防护措施进行研究。这项加强保护的举措正值研究表明，尽管商业卫星信号承载着敏感数据，但仍有大约一半未加密之际。

**当局拆除了W3LL网络钓鱼工具包基础设施**

美国联邦调查局亚特兰大分局和印尼国家警察联手捣毁了一个复杂的网络犯罪团伙，该团伙利用定制的钓鱼服务平台，企图诈骗超过2000万美元。据称，该团伙的主要开发者GL出售W3LL钓鱼工具包的访问权限，并运营一个交易平台，导致超过25000个账户被盗用。

**Meta为顶尖研究人员配备专业的测试套件**

Meta与PortSwigger合作，向在其漏洞赏金平台HackerPlus上达到白银级别的安全研究人员提供Burp Suite Pro许可证。此举旨在帮助研究人员提升技能，更高效、更创新地寻找漏洞。

**AWS RES漏洞可导致命令执行和权限提升**

AWS Research and Engineering Studio (RES)中存在多个漏洞，允许已认证用户执行任意命令并提升权限。CVE-2026-5707和 CVE-2026-5709 源于未经过过滤的输入，使得攻击者能够对虚拟桌面主机和集群管理器EC2实例进行命令注入攻击；而CVE-2026-5708 则允许攻击者通过精心构造的 API 请求获取实例配置文件权限。AWS已在2026.03版本中修复了这些问题。

**GlassWorm插件已推广至所有开发者IDE**

一种新的GlassWorm变种利用嵌入在恶意 OpenVSX 扩展中的 Zig 编译的本地投放器，该扩展伪装成 WakaTime，使其能够绕过典型的扩展沙箱机制，并以完全系统权限执行。执行后，它会扫描基于 VS Code 的 IDE（Visual Studio Code、Cursor、Windsurf、VSCodium 和 Positron），并在所有检测到的环境中安装第二阶段有效载荷。

**ShinyHunters瞄准了Rockstar Games**

威胁组织ShinyHunters威胁要泄露据称从Rockstar Games窃取的数据，这些数据是通过利用Anodot云成本监控工具中的身份验证令牌泄露的。该组织称，此次泄露事件导致Rockstar的Snowflake数据仓库实例遭到未经授权的访问。Rockstar Games已确认第三方泄露事件导致少量非实质性信息“有限”泄露，但坚称核心运营和玩家数据未受影响。

**ShowDoc中的关键远程代码执行漏洞已被发现并被积极利用。**

攻击者正积极利用ShowDoc（一款在中国广受欢迎的IT文档和协作平台）中的一个严重远程代码执行漏洞来部署Web Shell。该漏洞编号为 CVE-2025-0520，源于ShowDoc不受限制的文件上传机制，该机制未能正确验证未经身份验证用户的文件扩展名。2.8.7版本已发布了补丁。最新情报显示，仍有数千个实例暴露在互联网上。

**警方逮捕了一名扰乱教育网络秩序的青少年。**

北爱尔兰警方拘留了一名16岁少年，该少年涉嫌对C2k教育系统发起定向网络攻击。C2k教育系统为该地区几乎所有学校提供核心IT服务。教育局证实，此次攻击导致少数机构的个人数据泄露。

**美国环保署将网络安全预算增加至1900万美元。**

美国环保署（EPA）2027财年预算提案大幅增加信息安全和水务网络安全防御方面的资金，以应对恶意行为者日益增长的威胁。其中一项关键举措是申请在现有的饮用水基础设施韧性补助计划（Drinking Water Infrastructure Resilience Grant Program）内新增网络安全补助金，旨在帮助供水系统加强基础设施建设。该机构信息安全计划的总资金预计将翻一番，达到1910万美元。

**ShinyHunters泄露了数百万条麦格劳-希尔用户记录**

ShinyHunters勒索团伙利用配置错误的Salesforce环境，泄露了与1350万个麦格劳-希尔（McGraw Hill）账户相关的数据。该数据集总计超过100GB，包含电子邮件地址、姓名、电话号码和实际地址。提供教育解决方案的麦格劳-希尔表示，其核心系统和敏感数据并未受到损害。

**Chrome漏洞为研究人员赢得9万美元奖金**

谷歌在 Chrome 147版本中修复了31个漏洞，其中包括ANGLE图形组件中一个严重的堆缓冲区溢出漏洞（编号CVE-2026-6296），该漏洞的发现者“Cinzinga”因此获得了9万美元的奖励。此次更新还修复了V8、PDFium和媒体子系统等组件中的多个高风险内存安全问题，例如释放后使用和类型混淆漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hfjKPyxBDjrnE3XjiakAs1rTsiciaW7ia6XGNRLX86wux5qmfTOPTKL7uVPNlc21uk7zA0ia1qyulpwkiaQicqhITPub6gomicgCakZgTAyvMmVC39I/640?wx_fmt=png&from=appmsg)

**ShinyHunters泄露了数百万条麦格劳-希尔用户记录**

全球知名教育出版商麦格劳-希尔（McGraw Hill）在2026年4月确认发生一起大规模数据泄露事件，此次事件由知名数据勒索组织 ShinyHunters 发起。攻击者通过利用该公司在 Salesforce 云环境中的配置错误，获取了存储在相关网页中的数据，并在未支付赎金的情况下将数据公开泄露。该公司成立于1909年，是覆盖K-12、高等教育及职业教育领域的重要数字教育服务提供商，此次事件也因此引发广泛关注。

从影响范围来看，数据泄露规模巨大。根据数据泄露监测平台“Have I Been Pwned”的统计，此次事件共涉及约1350万个用户账户，泄露数据总量超过100GB，包含大量用户邮箱地址，并在部分记录中包含姓名、电话号码及物理地址等信息。这些数据具备较强的可利用性，可能被攻击者用于后续的钓鱼攻击、身份冒用及精准诈骗等活动。

从攻击路径来看，此次事件并非传统意义上的系统入侵，而是典型的云配置错误导致的数据暴露。麦格劳-希尔官方表示，攻击者访问的是托管在 Salesforce 平台上的某个网页数据，属于“有限数据集”，且未涉及其核心系统、客户数据库或教学平台。这种攻击方式说明，在云服务环境中，即便核心系统安全，外围配置不当同样可能成为数据泄露的突破口。

在事件博弈层面，ShinyHunters 延续其一贯的数据勒索策略。该组织声称其掌握多达4500万条包含个人身份信息（PII）的记录，并将麦格劳-希尔列入其暗网泄露站点，要求在截止日期前支付赎金，否则将公开数据。尽管企业方面对数据敏感性进行了弱化表述，但攻击者公开的数据规模与第三方验证结果之间存在明显差异，反映出当前数据泄露事件中“实际影响”与“官方披露”之间的常见信息不对称问题。

从行业视角看，此次事件再次凸显教育行业面临的系统性风险。一方面，教育平台积累了大量学生及用户的个人信息，是攻击者的重要目标；另一方面，云服务（如 Salesforce）广泛应用，但配置管理复杂，一旦权限控制或访问策略出现疏漏，极易形成“无感暴露”。此次事件也被认为是近年来多起 Salesforce 相关数据泄露事件中的典型案例，表明云环境配置安全已成为企业数据安全治理的关键短板。

总体而言，该事件的核心教训在于：数据安全风险正从“系统漏洞”向“配置错误”和“第三方平台风险”转移。即使企业核心系统未被攻破，只要存在云资源暴露、权限过度开放等问题，依然可能造成大规模数据泄露，并引发后续的连锁安全威胁。

[2025收集更新信通院白皮书系列合集（665个）下载](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652113841&idx=1&sn=36cf821dc3aae2832507d255896a6f38&scene=21#wechat_redirect)

---

——等级保护

[数据安全风险评估培训杂谈](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247502078&idx=1&sn=c8ff1cb33e5fb5a3aefcf54a9e2a1ea9&scene=21#wechat_redirect)

[打破“一考定终身”测评师迎来严峻挑战](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247501857&idx=1&sn=9daec7361aa26521d68729e5fba5561a&scene=21#wechat_redirect)

[欲等保定级先数据分类分级](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652115712&idx=1&sn=8792bea80ee757559a21d2934d800fef&scene=21#wechat_redirect)

[2025公安部网安局等保工作最新要求逐条解析](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652115704&idx=1&sn=97c79312f974a40385ce03bf2381ce93&scene=21#wechat_redirect)

[公网安〔2025〕1846号文：风险隐患及工作方案释疑浅谈](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247499841&idx=1&sn=a42dcf1861cce1b959c39f8230402853&scene=21#wechat_redirect)

[公网安〔2025〕1846号文：数据摸底调查释疑浅谈](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247499830&idx=1&sn=b441c2c13965d7d7e74c2bd43691d2de&scene=21#wechat_redirect)

[公网安〔2025〕1846号文：第五级网络系统释疑浅谈](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247499811&idx=1&sn=e9b727e59da503bd8f785d243e52613f&scene=21#wechat_redirect)

[公网安〔2025〕1846号文：定级备案的最新释疑浅谈](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247499830&idx=3&sn=92345b977ed71a23fed133012fed329a&scene=21#wechat_redirect)

[关于25年定级备案公安部网安局释疑的一点浅谈](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652115561&idx=1&sn=109b35f8c1612b9bbe835225f6a4266d&scene=21#wechat_redirect)

[公网安〔2025】1846号关于对网络安全等级保护有关工作事项进一步说明的函](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247499807&idx=1&sn=f432e39e58fbe52a89b40cf59e962422&scene=21#wechat_redirect)

[新等保测评真的取消打分了吗？一点杂谈！](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652114894&idx=1&sn=ee5d37877f28e57d7ad82fcb227bd29f&scene=21#wechat_redirect)

[新定级备案模板明确数据安全纳入等级保护体系](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652114892&idx=1&sn=2a3c14fefe37d4ddbf5bc1cedab86328&scene=21#wechat_redirect)

[等保定级新模板新要求，2025定级工作新变化](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652114980&idx=1&sn=e981e9b0d43a96a353846ada0692b7da&scene=21#wechat_redirect)

[2025新形势下新等保备案如何开展](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247498851&idx=1&sn=f65f19a55aab01105b64674d30165654&scene=21#wechat_redirect)

[测评机构老板与销售注意：浅谈测评机构如何更好的满足属地网安监管？](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652114960&idx=1&sn=1415212a3dd2dc55471853fd5b1efe54&scene=21#wechat_redirect)

[网络安全等级保护：等级保护工作、分级保护工作、密码管理工作三者之间的关系](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652098579&idx=1&sn=56da5aedb263c64196a74c5f148af682&scene=21#wechat_redirect)

[河南省新规定测评与密评预算再调低](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652113691&idx=1&sn=a3dcddb5a5b14aa2d8a69d33ebc1d547&scene=21#wechat_redirect)

[四川省等级测评与商密评估预算计算方法](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652113755&idx=1&sn=7a45cccd0c72be5cd3c7c07fd7878dd8&scene=21#wechat_redirect)

[广西壮族自治区等级测评与商密评估预算为几何？](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652113803&idx=1&sn=f9bbfaf9193865b0419628a0c7d349ef&scene=21#wechat_redirect)

[黑龙江财政关于等级测评与商密评估预算为几何？](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652113921&idx=1&sn=5ea1712d0f628e52676a6068a25c204a&scene=21#wechat_redirect)

[和Deepseek一起共同探讨《国家信息化领导小组关于加强信息安全保障工作的意见》](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652114662&idx=1&sn=13021aa20b9d685b57ff950ec3908ef1&scene=21#wechat_redirect)

[和Deepseek一起共同探讨《关于信息安全等级保护工作的实施意见》](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652114684&idx=1&sn=59de3b0fa94b3ea300beb1fcdb5b87ae&scene=21#wechat_redirect)

[与Deepseek一起谈开展等级测评的必要性！](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652114693&idx=1&sn=dd12972dcbea1242e5064ae4189a0dbb&scene=21#wechat_redirect)

——数据安全

[《网络数据安全管理条例》解读](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652113680&idx=1&sn=86da41ae8e79d457e121599e64b266f3&scene=21#wechat_redirect)

[跟着DAMA专家看数据管理的未来](https://mp.weixin.qq.com/s?__biz=Mzg2NjY2MTI3Mg==&mid=2247502078&idx=2&sn=79c04453574daf5d78f00b3ab64b811f&scene=21#wechat_redirect)

[市场监管总局印发《网络交易合规数据报送管理暂行办法》](https://mp.weixin.qq.com/s?__biz=MzA5MzU5MzQzMA==&mid=2652115101&idx=1&sn=96dcac6598142fe6dd586ef5e25a5f6d&scene=21#wechat_redirect)

[数据安...