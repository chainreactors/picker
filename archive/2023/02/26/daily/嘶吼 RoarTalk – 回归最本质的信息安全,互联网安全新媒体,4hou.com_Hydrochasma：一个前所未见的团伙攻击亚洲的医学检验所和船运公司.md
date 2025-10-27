---
title: Hydrochasma：一个前所未见的团伙攻击亚洲的医学检验所和船运公司
url: https://www.4hou.com/posts/KEPY
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-26
fetch_date: 2025-10-04T08:07:56.483864
---

# Hydrochasma：一个前所未见的团伙攻击亚洲的医学检验所和船运公司

Hydrochasma：一个前所未见的团伙攻击亚洲的医学检验所和船运公司 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Hydrochasma：一个前所未见的团伙攻击亚洲的医学检验所和船运公司

布加迪
[新闻](https://www.4hou.com/category/news)
2023-02-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)174920

收藏

导语：这起攻击活动根本没有部署自定义恶意软件，似乎完全依赖开源工具。

亚洲的多家船运公司和医学检验所近日遭到一起活动的攻击，这起可能旨在收集情报的攻击完全依赖公开可用的离地攻击（LotL）工具。

这起活动背后的威胁团伙Hydrochasma与任何之前已确定身份的团伙毫无关联，似乎对从事新冠病毒相关治疗或疫苗的行业颇有兴趣。

这起活动至少自2022年10月以来一直在肆虐。虽然赛门铁克没有发现任何数据在这起活动中泄露，但攻击目标以及所使用的一些工具表明，这起活动最有可能的动机是收集情报。

**攻击链**

Hydrochasma使用的感染途径极有可能是一封网络钓鱼邮件。在受害者系统上看到的第一个可疑活动是一个诱饵文件，其文件名使用受害者组织的母语，似乎表明这是电子邮件附件：

[翻译自原文]产品规格-货运公司资质信息wps-pdf Export.pdf.exe

另一个诱饵文件似乎是在模仿简历：

[翻译自原文]University-Development Engineer.exe

攻击者在一台机器上获得初始访问权后投放了快速反向代理（FRP），这种工具可以将位于NAT或防火墙后面的本地服务器暴露在互联网的面前。这投放一个合法的微软Edge更新文件：

%TEMP%\MicrosoftEdgeUpdate.exe

然后在受害者机器上可以看到另一个文件%TEMP%\msedgeupdate.dll。但这个文件实际上是Meterpreter，它是Metasploit框架的一部分，可以用于远程访问。

**随后在该受害者的网络中发现了其他工具，包括如下：**

Gogo扫描工具：最初为供红队使用而设计的自动扫描引擎。

进程转储器（lsass.exe)：允许攻击者转储域密码的工具。

Cobalt Strike Beacon：一个现成的工具，可用于执行命令、注入其他进程、提升当前进程的权限、冒充其他进程以及上传/下载文件。它具有渗透测试工具的正当用途，但总是被恶意分子利用。

AlliN扫描工具：一个渗透测试扫描工具，可用于横向渗透到内联网。

Fscan：一个公开可用的黑客工具，可以扫描敞开的端口等。

Dogz代理工具：一个免费的VPN代理工具。

威胁团伙还在这个受害者的网络上部署了外壳代码（shellcode）加载器和受损的可移植可执行文件（PE）。

**这次活动使用了其他战术、技术和程序（TTP），包括如下：**

SoftEtherVPN：该工具的出现最先促使赛门铁克的研究人员着手调查该活动。它是免费开源的跨平台VPN软件。

Procdump：这个微软Sysinternals工具用于监控应用程序的CPU峰值并生成崩溃转储内容，但也可以用作通用进程转储实用工具。

BrowserGhost：可以从互联网浏览器获取密码的公开可用的工具。

Gost代理：一个隧道工具。

Ntlmrelay：NTLM中继攻击允许攻击者拦截有效的身份验证请求，以便访问网络服务。

任务调度器：允许任务在计算机上自动执行。

Go-strip：用来缩小Go二进制文件的大小。

HackBrowserData：可以解密浏览器数据的开源工具。

Hydrochasma部署的这些工具表明，企图实现持久性，偷偷访问受害者机器，并且竭力提升特权，以便在受害者网络中横向传播。

虽然赛门铁克的研究人员没有观察到数据因此从受害者机器泄露出去的迹象，但Hydrochasma部署的一些工具确实允许远程访问，可能被用于泄露数据。受到攻击的行业也表明，这次攻击背后的动机是收集情报。

这次攻击没有使用自定义恶意软件也值得注意。完全依赖公开可用的离地攻击工具可以帮助加大攻击的隐秘性，同时加大了追根溯源的难度。赛门铁克没有发现该活动与已知威胁团伙有关联的证据，我们于是为该活动背后的威胁团伙赋予了新的身份Hydrochasma。

**保护/缓解**

想参阅保护方面的最新更新，请访问赛门铁克保护公告：https://www.broadcom.com/support/security-center/protection-bulletin。

**攻陷指标（IOC）**

如果IOC是恶意的，文件又能被我们获取，那么赛门铁克端点将检测并阻止该文件。

**文件指标**

SHA256

409f89f4a00e649ccd8ce1a4a08afe03cb5d1c623ab54a80874aebf09a9840e5 – 快速反向代理

47d328c308c710a7e84bbfb71aa09593e7a82b707fde0fb9356fb7124118dc88 – GoGo扫描工具

6698a81e993363fab0550855c339d9a20a25d159aaa9c4b91f60bb4a68627132 – 释放器

7229bd06cb2a4bbe157d72a3734ba25bc7c08d6644c3747cdc4bcc5776f4b5b9 –进程转储器（lsass.exe）

72885373e3e8404f1889e479b3d46dd8111280379c4065bfc1e62df093e42aba –快速反向代理

72bc8b30df3cdde6c58ef1e8a3eae9e7882d1abe0b7d4810270b5a0cc077bb1a–Cobalt Strike Beacon

7b410fa2a93ed04a4155df30ffde7d43131c724cdf60815ee354988b31e826f8 –快速反向代理

7f0807d40e9417141bf274ef8467a240e20109a489524e62b090bccdb4998bc6 –进程转储器（lsass.exe）

8c0f0d1acb04693a6bdd456a6fcd37243e502b21d17c8d9256940fc7943b1e9a – Cobalt Strike Beacon

8e32ea45e1139b459742e676b7b2499810c3716216ba2ec55b77c79495901043 – 快速反向代理

981e5f7219a2f92a908459529c42747ac5f5a820995f66234716c538b19993eb – GoGo扫描工具

9ebd789e8ca8b96ed55fc8e95c98a45a61baea3805fd440f50f2bde5ffd7a372 – 快速反向代理

9f5f7ba7d276f162cc32791bfbaa0199013290a8ac250eb95fd90bc004c3fd36 – Cobalt Strike Beacon

a0f5966fcc64ce2d10f24e02ae96cdc91590452b9a96b3b1d4a2f66c722eec34 – AllIn扫描工具

cb03b5d517090b20749905a330c55df9eb4d1c6b37b1b31fae1982e32fd10009 – Fscan

d1c4968e7690fd40809491acc8787389de0b7cbc672c235639ae7b4d07d04dd4 – 外壳代码加载器

de01492b44372f2e4e38354845e7f86e0be5fb8f5051baafd004ec5c1567039f – Cobalt Strike Beacon

e378d8b5a35d4ec75cae7524e64c1d605f1511f9630c671321ee46aa7c4d378b – PE文件

eba22f50eedfec960fac408d9e6add4b0bd91dd5294bee8cff730db53b822841 – 释放器

fc4b5f2ee9da1fe105bb1b7768754d48f798bf181cbc53583387578a5ebc7b56 – Dogz代理工具

**网络指标**

IP

39.101.194[.]61 – Cobalt Strike Beacon C&C

47.92.138[.]241 – Cobalt Strike Beacon C&C

106.14.184[.]148

180.119.234[.]147

**域名**

alidocs.dingtalk[.]com.wswebpic[.]com – Cobalt Strike Beacon C&C

csc.zte[.]com.cn.wswebpic[.]com – Cobalt Strike Beacon C&C

taoche[.]cn.wswebpic[.]com – Cobalt Strike Beacon C&C

**URL**

hxxp://47.92.138[.]241:8090/update.exe

hxxp://47.92.138[.]241:8000/agent.exe

hxxp://47.92.138[.]241:8000/update.exe

hxxp://47.92.138[.]241:8000/ff.exe

hxxp://47.92.138[.]241:8000/aa.exe

hxxp://47.92.138[.]241:8000/runas.exe

hxxp://47.92.138[.]241:8090/a.exe

hxxp://47.92.138[.]241:8000/t.exe

hxxp://47.92.138[.]241:8000/po.exe

hxxp://47.92.138[.]241:8080/t.exe

hxxp://47.92.138[.]241:8899/t.exe

hxxp://47.92.138[.]241:8000/logo.png

hxxp://47.92.138[.]241:8080/t.png

hxxp://47.92.138[.]241:8000/frp.exe

本文翻译自：https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/hydrochasma-asia-medical-shipping-intelligence-gathering如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?fKxQc0v5)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![]...