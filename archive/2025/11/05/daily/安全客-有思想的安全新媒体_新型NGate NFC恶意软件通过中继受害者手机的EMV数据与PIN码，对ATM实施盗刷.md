---
title: 新型NGate NFC恶意软件通过中继受害者手机的EMV数据与PIN码，对ATM实施盗刷
url: https://www.anquanke.com/post/id/313012
source: 安全客-有思想的安全新媒体
date: 2025-11-05
fetch_date: 2025-11-06T03:12:20.488332
---

# 新型NGate NFC恶意软件通过中继受害者手机的EMV数据与PIN码，对ATM实施盗刷

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 新型NGate NFC恶意软件通过中继受害者手机的EMV数据与PIN码，对ATM实施盗刷

阅读量**20993**

发布时间 : 2025-11-05 17:54:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/ngate-nfc-malware-steals-cash-from-atms-by-relaying-emv-data-and-pins-from-victims-phone/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

波兰国家网络安全事件响应团队（CERT Polska）发现了一种新型基于Android的**NFC中继恶意软件NGate**，该恶意软件使网络犯罪分子能够使用受害者自己的支付卡在ATM机上取现，**无需物理窃取卡片**。

根据CERT Polska的报告：“该攻击活动旨在利用受害者的支付卡进行未授权ATM取现。犯罪分子不会物理窃取卡片，而是将受害者Android手机中的卡片NFC流量中继到攻击者在ATM机旁控制的设备。”

### **攻击流程：从钓鱼到NFC中继**

攻击始于**仿冒银行客服的钓鱼和电话社会工程**。受害者通过电子邮件或短信收到虚假安全警报，声称存在“技术问题或安全事件”，并引导至钓鱼网站，诱骗用户下载恶意Android应用。

CERT Polska解释：“骗子会致电受害者，冒充银行工作人员‘验证身份’并为安装应用找借口。用户还会收到确认所谓银行员工身份的短信。”

恶意应用随后指示受害者“在应用内直接验证支付卡”——将卡片贴近手机（通过NFC）并在伪造的键盘界面输入PIN码。

“当受害者贴近卡片时，应用会捕获卡片的NFC通信数据（与在终端/ATM机上流动的数据相同），并通过互联网发送给攻击者在ATM机旁的设备，”CERT Polska指出，“攻击者使用中继的卡片数据+PIN码取现。”

### **技术细节：HCE伪装与实时数据中继**

分析发现，恶意APK将自身注册为Android**主机卡模拟（HCE）支付服务**，使其能够充当虚拟卡片或读卡器。CERT Polska分析称：“该应用在Android上注册为主机卡模拟（HCE）支付服务（因此可模拟虚拟卡片）。”

安装后，恶意软件激活一个原生库（libapp.so ），从嵌入式资源中解密配置。报告显示，恶意软件的命令与控制（C2）服务器地址在运行时通过应用签名证书派生的密钥解密：

“我们解密了该资源，恢复了活跃的C2端点：IP/端口：91.84.97.13:5653。”

随后，恶意软件与该IP地址建立**TCP连接（未加密，tls=false）**，实现受感染设备与攻击者ATM中继终端之间卡片数据和PIN码的实时传输。

CERT Polska的逆向工程显示，原生代码对配置文件执行XOR解密，密钥派生自“APK签名证书的SHA-256哈希”。这种混淆帮助攻击者隐藏服务器地址、令牌和连接模式等关键参数。

### **数据窃取机制：NFC拦截与PIN捕获**

当受害者贴近卡片时，恶意软件利用Android的NFC读取器API拦截EMV数据，包括**主账号（PAN）、有效期和应用标识符（AID）**。恶意软件的CardData类将这些值与PIN码一起序列化为二进制结构后泄露。

CERT Polska报告证实：“用户界面包含PIN码键盘；PIN码与NFC数据一起发送给攻击者。”

PIN码捕获机制使用自定义键盘组件（PinCodeField），在输入第四位数字后立即发布完整PIN字符串。CERT Polska强调：“一旦达到所需长度（默认4位），它会将完整PIN字符串发布到内部事件总线”，然后通过套接字一步发送至C2服务器。

### **双角色运作：读卡器与发射器模式**

研究人员发现，NGate支持两种操作角色——一种用于收集卡片数据（读卡器模式），另一种用于在ATM机上模拟支付卡（发射器模式）。

这种设置使攻击者能够在两台设备之间实时中继EMV APDU指令和PIN码：一台设备与受害者的卡片交互，另一台在ATM机上模拟该卡片，无需复制物理卡片即可**克隆交易会话**。

### **网络层分析：明文传输与持久连接**

CERT Polska对网络层的分析显示，恶意软件使用简单的帧式TCP协议发送长度前缀消息和明文载荷。由于TLS被禁用，“网络中的帧易于识别签名，且因tls=false，载荷为明文”。

恶意软件通过每7秒发送一次保活ping维持持久连接，确保攻击者的中继在ATM交易过程中保持同步。

**防御建议**：

1. 警惕任何要求下载“安全验证应用”的银行相关短信/电话，通过官方渠道核实异常通知。
2. 避免从未知来源安装APK，仅使用官方应用商店。
3. 对应用的NFC权限保持警惕，定期检查已安装应用的权限列表。
4. 在输入银行卡PIN码时，注意周围环境是否存在可疑设备，防止被窥视或中继攻击。

本文翻译自securityonline [原文链接](https://securityonline.info/ngate-nfc-malware-steals-cash-from-atms-by-relaying-emv-data-and-pins-from-victims-phone/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313012](/post/id/313012)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/ngate-nfc-malware-steals-cash-from-atms-by-relaying-emv-data-and-pins-from-victims-phone/)

如若转载,请注明出处： <https://securityonline.info/ngate-nfc-malware-steals-cash-from-atms-by-relaying-emv-data-and-pins-from-victims-phone/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **653**

* 粉丝
* **6**

### TA的文章

* ##### [一文读懂香港金融科技周：DART将带领香港金融科技驶向何方？](/post/id/313039)

  2025-11-05 18:35:34
* ##### [WordPress的AI引擎插件中存在严重漏洞（CVE-2025-11749），可致网站被攻击者完全控制](/post/id/313004)

  2025-11-05 17:54:53
* ##### [深度解析Tycoon 2FA钓鱼工具包针对Microsoft 365与Gmail账户的攻击手法](/post/id/313007)

  2025-11-05 17:54:36
* ##### [新型NGate NFC恶意软件通过中继受害者手机的EMV数据与PIN码，对ATM实施盗刷](/post/id/313012)

  2025-11-05 17:54:19
* ##### [CISA发布关键漏洞紧急警报：Gladinet LFI/RCE漏洞与控制面板CWP管理员权限接管漏洞正遭积极利用](/post/id/313015)

  2025-11-05 17:53:59

### 相关文章

* ##### [WordPress的AI引擎插件中存在严重漏洞（CVE-2025-11749），可致网站被攻击者完全控制](/post/id/313004)

  2025-11-05 17:54:53
* ##### [深度解析Tycoon 2FA钓鱼工具包针对Microsoft 365与Gmail账户的攻击手法](/post/id/313007)

  2025-11-05 17:54:36
* ##### [CISA发布关键漏洞紧急警报：Gladinet LFI/RCE漏洞与控制面板CWP管理员权限接管漏洞正遭积极利用](/post/id/313015)

  2025-11-05 17:53:59
* ##### [全球网络间谍组织利用ZipperDown漏洞及Android零日漏洞，通过邮件客户端实现一键远程代码执行与账户接管](/post/id/313018)

  2025-11-05 17:53:37
* ##### [React Native CLI 中存在严重漏洞（CVE-2025-11953，CVSS 9.8），攻击者可经由暴露的Metro开发服务器实现RCE](/post/id/313021)

  2025-11-05 17:53:18
* ##### [Bugcrowd收购自动化测试工具Mayhem，以强化其应用安全测试平台能力](/post/id/313024)

  2025-11-05 17:52:48
* ##### [Open VSX扩展市场中出现新型“SleepyDck”恶意软件，允许攻击者远程控制Windows系统](/post/id/313027)

  2025-11-05 17:52:17

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)