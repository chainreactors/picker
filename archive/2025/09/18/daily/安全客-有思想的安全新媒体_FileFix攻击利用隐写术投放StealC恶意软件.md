---
title: FileFix攻击利用隐写术投放StealC恶意软件
url: https://www.anquanke.com/post/id/312175
source: 安全客-有思想的安全新媒体
date: 2025-09-18
fetch_date: 2025-10-02T20:17:25.586495
---

# FileFix攻击利用隐写术投放StealC恶意软件

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

# FileFix攻击利用隐写术投放StealC恶意软件

阅读量**48360**

发布时间 : 2025-09-17 17:33:56

**x**

##### 译文声明

本文是翻译文章，文章原作者 Lawrence Abrams，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/new-filefix-attack-uses-steganography-to-drop-stealc-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

近期发现的FileFix社会工程学攻击通过伪造Meta账号停用警告，诱骗用户在不知情的情况下安装StealC信息窃取恶意软件。

FileFix是ClickFix攻击家族的新变种，该类攻击通过社会工程学手段，诱使用户将恶意命令粘贴到操作系统对话框中，谎称是解决问题的“修复方法”。FileFix技术由红队研究员mr.d0x创建，与传统ClickFix诱骗用户在Windows“运行”对话框或终端粘贴恶意PowerShell命令不同，FileFix**滥用文件资源管理器的地址栏执行命令**。

此前，Interlock勒索软件团伙曾使用FileFix安装远程访问木马（RAT），但早期攻击仅使用原始FileFix概念验证（PoC），未对诱饵进行更新。

### **新型FileFix攻击活动**

Acronis发现的新一轮攻击使用**多语言钓鱼页面**伪装成Meta支持团队，警告收件人若不查看所谓Meta共享的“事件报告”，账号将在7天内停用。然而，该“报告”并非文档，而是用于在目标设备上安装恶意软件的**伪装PowerShell命令**。

钓鱼页面引导用户点击“复制”按钮复制看似文件路径的内容，点击打开文件资源管理器按钮，再将“路径”粘贴到地址栏以打开文档。但点击复制后，剪贴板中实际复制的是**含空格的PowerShell命令**——粘贴到文件资源管理器时，仅显示文件路径。

Acronis解释：“攻击者在载荷末尾添加变量，包含大量空格和虚假路径，使地址栏仅显示文件路径，隐藏真实恶意命令。传统ClickFix攻击使用#符号（PowerShell注释符）实现此效果，而本攻击改用变量，导致依赖#符号检测的安全工具可能失效。”

![]()

### **攻击链：隐写术与内存解密**

![]()

此FileFix活动的突出特点是**利用隐写术**，将第二阶段PowerShell脚本和加密可执行文件隐藏在Bitbucket上托管的**看似无害的JPG图像**中。目标用户无意中执行的第一阶段PowerShell命令会先下载该图像，提取嵌入的次级脚本，进而在内存中解密载荷。

### **最终载荷：StealC信息窃取器**

最终投放的StealC恶意软件会窃取受感染设备的以下数据：

1. 网页浏览器（Chrome、Firefox等）的**凭证和身份验证Cookie**；
2. messaging应用（Discord、Telegram等）的**登录凭证**；
3. 加密货币钱包（Bitcoin、Ethereum等）的**私钥**；
4. 云服务（AWS、Azure）的**访问凭证**；
5. VPN和游戏应用（ProtonVPN、Battle.net 等）的**账号信息**；
6. 截取**活动桌面截图**。

### **攻击演变与防御建议**

Acronis在两周内观察到多个攻击变种，涉及不同载荷、域名和诱饵，显示攻击者在**社会工程学技巧和技术实现上持续进化**。尽管多数组织已对员工进行钓鱼防范培训，但ClickFix和FileFix等新型战术仍在快速迭代。

Acronis建议企业加强用户教育，警示此类新型战术风险，避免将网站内容复制到看似无害的系统对话框中。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/new-filefix-attack-uses-steganography-to-drop-stealc-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312175](/post/id/312175)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/new-filefix-attack-uses-steganography-to-drop-stealc-malware/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/new-filefix-attack-uses-steganography-to-drop-stealc-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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