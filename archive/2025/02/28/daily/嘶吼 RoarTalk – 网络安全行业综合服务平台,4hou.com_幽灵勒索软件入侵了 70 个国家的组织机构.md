---
title: 幽灵勒索软件入侵了 70 个国家的组织机构
url: https://www.4hou.com/posts/yz56
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-28
fetch_date: 2025-10-06T20:35:31.078369
---

# 幽灵勒索软件入侵了 70 个国家的组织机构

幽灵勒索软件入侵了 70 个国家的组织机构 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 幽灵勒索软件入侵了 70 个国家的组织机构

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-02-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)78477

收藏

导语：Fortinet在2019年8月、2020年7月、2020年11月和2021年4月多次警告客户，要针对CVE-2018-13379给SSL VPN设备打补丁。

CISA 和 FBI 表示，部署“幽灵”勒索软件的攻击者已入侵了来自 70 多个国家多个行业领域的受害者，其中包括关键基础设施组织。

受影响的其他行业包括医疗保健、政府、教育、科技、制造业以及众多中小型企业。

CISA、FBI 以及 MS-ISAC 联合发布的一份咨询报告称：“自 2021 年初开始，幽灵黑客开始攻击那些互联网服务所运行的软件和固件版本过时的受害者。”目前，这种对存在漏洞的网络不加区分的攻击已导致全球 70 多个国家的组织受到侵害。

幽灵勒索软件的运营者经常更换其恶意软件可执行文件，更改加密文件的扩展名，修改勒索信的内容，并使用多个电子邮件地址进行勒索沟通，导致该组织的归属很难被及时确定。

与该组织有关联的名称包括 Ghost、Cring、Crypt3r、 Phantom、 Strike、 Hello、 Wickrme、HsHarada、和 Rapture。其攻击中使用的勒索软件样本包括“Cring.exe”“Ghost.exe”“ ElysiumO.exe” 和“Locker.exe”。

这个以盈利为目的的勒索软件团伙利用公开可获取的代码来攻击存在安全漏洞的服务器。他们针对的是 Fortinet（CVE-2018-13379）、ColdFusion（CVE-2010-2861、CVE-2009-3960）和 Exchange（CVE-2021-34473、CVE-2021-34523、CVE-2021-31207）中未修补的漏洞。

为防范幽灵勒索软件攻击，建议网络防御人员采取以下措施：

1.定期和异地备份不能被勒索软件加密的系统；

2.尽快修补操作系统、软件和固件漏洞；

3.重点关注幽灵勒索软件针对的安全漏洞（即CVE-2018-13379、CVE-2010-2861、CVE-2009-3960、CVE-2021-34473、CVE-2021-34523、CVE-2021-31207）；

4.分割网络以限制受感染设备的横向移动；

5.对所有特权帐户和电子邮件服务帐户实施防网络钓鱼的多因素身份验证（MFA）。

Amigo\_A和Swisscom的CSIRT团队在2021年初首次发现Ghost勒索软件后，他们的运营商就开始投放定制的Mimikatz样本，然后是CobaltStrike信标，并使用合法的Windows CertUtil证书管理器部署勒索软件有效载荷，以绕过安全软件。

除了在Ghost勒索软件攻击中被用于初始访问之外，国家支持的黑客组织还扫描了易受攻击的Fortinet SSL VPN设备，并针对CVE-2018-13379漏洞进行了攻击。

攻击者还滥用了同样的安全漏洞，破坏了可以通过互联网访问的美国选举支持系统。

Fortinet在2019年8月、2020年7月、2020年11月和2021年4月多次警告客户，要针对CVE-2018-13379给SSL VPN设备打补丁。

CISA、FBI和MS-ISAC本周发布的联合咨询报告还包括妥协指标（ioc）、战术、技术和程序（TTPs），以及与FBI调查期间发现的幽灵勒索软件活动相关的检测方法（最近在2025年1月）。

文章翻译自：https://www.bleepingcomputer.com/news/security/cisa-and-fbi-ghost-ransomware-breached-orgs-in-70-countries/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Wz0V7hm5)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

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

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)