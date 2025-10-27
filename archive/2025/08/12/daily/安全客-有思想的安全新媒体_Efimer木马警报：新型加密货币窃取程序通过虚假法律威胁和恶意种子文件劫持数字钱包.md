---
title: Efimer木马警报：新型加密货币窃取程序通过虚假法律威胁和恶意种子文件劫持数字钱包
url: https://www.anquanke.com/post/id/311036
source: 安全客-有思想的安全新媒体
date: 2025-08-12
fetch_date: 2025-10-07T00:16:47.471355
---

# Efimer木马警报：新型加密货币窃取程序通过虚假法律威胁和恶意种子文件劫持数字钱包

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

# Efimer木马警报：新型加密货币窃取程序通过虚假法律威胁和恶意种子文件劫持数字钱包

阅读量**58294**

发布时间 : 2025-08-11 17:11:14

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/efimer-trojan-new-crypto-stealer-hijacks-wallets-via-fake-legal-threats-malicious-torrents/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

卡巴斯基实验室近日披露了一起复杂的**多向攻击行动**，攻击者利用假冒法律威胁、被入侵的 WordPress 网站以及恶意种子文件，投递一款名为 **Efimer** 的加密货币窃取型木马。该木马最早于 2024 年底被发现，已演化为模块化威胁，不仅能**窃取资金、收集账号凭证，还能对存在漏洞的网站发动暴力破解攻击**。

2025 年 6 月，卡巴斯基研究人员发现了一轮“律师函钓鱼”式的群发邮件攻击，攻击者冒充某大型企业的律师，声称收件人的域名侵犯了商标权，并威胁将采取法律行动，但同时给出一个“退路”——更改域名或将其出售。邮件附件为一个 ZIP 压缩包，号称包含争议详情，实则内含伪装成 **Requirement.wsf** 文件的 Efimer 木马。

为规避检测，攻击者甚至在密码文件名中使用 Unicode 相似字符，增加自动化分析工具识别的难度。一旦执行，该脚本会检测管理员权限、修改 Windows Defender 排除项，并安装核心载荷——一个专注加密货币劫持的 **ClipBanker 木马**。

Efimer 主要通过“**剪贴板劫持**”技术，将用户复制的加密货币钱包地址替换为攻击者控制的地址。同时，它会嗅探助记词（mnemonic phrase）并替换复制的加密钱包地址，确保受害者在交易时不易察觉。

如果任务管理器被打开，木马会立刻停止运行以规避分析；否则，它会安装 Tor 代理客户端，与其 C2 服务器通信，每隔 30 分钟上传窃取的助记词、截图和钱包数据，以保持隐蔽性。

针对不同加密货币，Efimer 定制了差异化策略：

**· 比特币（BTC）**：替换时保留部分原地址以降低怀疑；

**· 以太坊（ETH）**：直接替换 0x 前缀地址为攻击者控制的地址；

**· 门罗币（XMR）、波场（TRX）、索拉纳（SOL）**：使用预设地址，并尽量减少匹配要求以绕过肉眼检查。

Efimer 还通过入侵的 WordPress 站点传播，攻击者在这些站点发布虚假的电影下载链接，引导用户下载受密码保护的压缩包，内含伪装成媒体播放器的恶意 EXE 文件，执行后同样会安装木马和 Tor 代理客户端。

卡巴斯基指出，攻击者会主动搜寻安全防护薄弱的网站，通过暴力破解获取权限，然后发布“热门电影下载”诱饵链接。这不仅是投递木马的渠道，也为后续大规模暴力破解活动提供跳板。

Efimer 的模块化架构支持额外脚本扩展：

**1. btdlg.js**：暴力破解工具，可通过 Google 和 Bing 搜索目标域名，并利用 XML-RPC 接口尝试登录；

**2. Liame**：邮件收集工具，从指定域名收集邮箱地址并回传，可能用于后续垃圾邮件或钓鱼攻击；

**3. assembly.js**：增强版变种，增加虚拟机检测功能，并深入搜索加密钱包信息，涵盖浏览器扩展与钱包应用，数据会被发送至独立的 C2 基础设施。

2024 年 10 月至 2025 年 7 月间，Efimer 共感染了 5,015 名卡巴斯基用户，其中巴西受害者数量最多（1,476 人）。

卡巴斯基警告称，Efimer 结合了隐蔽性、适应性和多向投递能力，对个人用户和网站管理员，尤其是在加密货币生态中，构成了严重威胁。

本文翻译自securityonline [原文链接](https://securityonline.info/efimer-trojan-new-crypto-stealer-hijacks-wallets-via-fake-legal-threats-malicious-torrents/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311036](/post/id/311036)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/efimer-trojan-new-crypto-stealer-hijacks-wallets-via-fake-legal-threats-malicious-torrents/)

如若转载,请注明出处： <https://securityonline.info/efimer-trojan-new-crypto-stealer-hijacks-wallets-via-fake-legal-threats-malicious-torrents/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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