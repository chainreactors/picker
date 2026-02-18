---
title: 针对叙利亚军人的复合式攻击活动分析
url: https://www.secrss.com/articles/61066?app=1
source: Over Security - Cybersecurity news aggregator
date: 2026-02-17
fetch_date: 2026-02-18T04:15:47.262403
---

# 针对叙利亚军人的复合式攻击活动分析

Toggle navigation

[![logo](https://www.secrss.com/logo_lg.png)](https://www.secrss.com "首页")

* [首页](https://www.secrss.com)
* [政策法规](https://www.secrss.com/articles?tag=政策法规)
* [威胁态势](https://www.secrss.com/articles?tag=威胁态势)
* [技术前沿](https://www.secrss.com/articles?tag=技术前沿)
* [安全实践](https://www.secrss.com/articles?tag=安全实践)
* [产业研究](https://www.secrss.com/articles?tag=产业研究)

* [登录/注册](https://www.secrss.com/login)

# 针对叙利亚军人的复合式攻击活动分析

奇安信病毒响应中心
2023-11-24

摘要：此次针对向叙利亚军人的复合式攻击具有迷惑性强，破坏性大，难以追踪的特点，一旦感染，甚至威胁到受害者及其家人的生命财产安全。

![](https://s.secrss.com/anquanneican/66ac15fa21d9613df60873790654d7c7.png)

**摘 要**

近日，奇安信病毒响应中心移动安全团队监测到一款伪装成叙利亚发展信托基金应用的恶意软件。

其为针对叙利亚军人的钓鱼和木马复合式攻击，会窃取受害者隐私信息和社交账号信息。

钓鱼页面宣称是叙利亚发展信托基金支持叙利亚军队中英雄的一个新项目，要求填写个人信息和家庭信息，如姓名、电话、军衔、服务地点及妻子姓名、子女信息等。

SpyMax的功能非常全面，包含监控SMS、访问麦克风、录制音视频、窃取通讯录和通话记录、窃取文件、实时定位等。

此次针对向叙利亚军人的复合式攻击具有迷惑性强，破坏性大，难以追踪的特点，一旦感染，甚至威胁到受害者及其家人的生命财产安全。

**关键词：**叙利亚发展信托基金、叙利亚军队中英雄、钓鱼攻击、Spymax RAT

**概述**

近日，奇安信病毒响应中心移动安全团队监测到一款伪装成叙利亚发展信托基金应用的恶意软件。经过分析，发现其为针对叙利亚军人的钓鱼和木马复合式攻击，会窃取受害者隐私信息和社交账号信息。

叙利亚发展信托基金是叙利亚的一个非政府、非营利的组织。

**攻击分析**

攻击活动中的移动端恶意软件样本，都采用知名的Android RAT工具SpyMax进行开发，先后有阿拉伯语和英语两个版本，其中包装的URL为钓鱼链接。

**PART** **0****1**

**钓鱼攻击**

钓鱼攻击分发在移动端和web端，根据其使用域名、服务器和内容可以确定两个钓鱼站点同属于此次针对叙利亚军人的攻击活动。

**移动端**

移动端钓鱼攻击首先在应用名称和图标上进行伪装，应用名称为“الأمانة السورية للتنمية”和“syria-trust-for-development”，应用图标则为叙利亚发展信托基金标志；其次其钓鱼链接为“https://syr1.store/”，也与官网地址“https://syriatrust.sy/”相似；最后是其利用官网内容和样式进行的钓鱼页面内容伪装。

“مشروع جديد للأمانة السورية للتنمية يهدف إلى دعم الأبطال في الجيش العربي السوري الذين يضحون لتحيا سوريا بعزة وكرامة”（译：叙利亚发展信托基金的一个新项目旨在支持阿拉伯叙利亚军队中的英雄，他们为叙利亚能够自豪和有尊严地生活而做出牺牲）。钓鱼页面宣称是叙利亚发展信托基金支持叙利亚军队中英雄的一个新项目，要求填写个人信息和家庭信息，如姓名、电话、军衔、服务地点及妻子姓名、子女信息等。

钓鱼页面上传数据如下：

![](https://s.secrss.com/anquanneican/c91a7c47094008102721eec6433c1294.png)

在钓鱼页面的底部，诱导受害者将此程序保留在设备上，还提供了紧急情况下社交软件Facebook的联系方式，然而这又是针对受害者社交账号的钓鱼，数据会提交到“shame5sham.000webhostapp.com”服务器。

Facebook钓鱼页面上传数据如下：

![](https://s.secrss.com/anquanneican/358b234d503187987afd6defe91fd6bc.png)

**Web端**

经过数据挖掘，我们发现除了2个移动端的样本外，此次攻击活动还在同一服务器上部署有钓鱼web应用程序，域名为“syr1.online”，此程序利用爬取叙利亚发展信托基金官网与军人相关活动的照片和推文进行伪装，与官网（syriatrust.sy）内容对比如下：

![](https://s.secrss.com/anquanneican/61f3b1f3932a0c106e1a2cdc7f0cc74e.png)

在页面底部同样提供了社交软件Facebook的联系方式，此次的社交账号信息是直接提交到当前服务器。数据上传如下：

![](https://s.secrss.com/anquanneican/3d094d8ae89434d61963557cafb7d09f.png)

**PART** **0****2**

**SpyMAX 攻击**

**SpyMAX介绍**

SpyMax是近几年Android端的流行监控工具，它的前身SpyNote 是最广泛使用的间谍软件框架之一，曾被誉为市场上最好的Android RAT工具。SpyMax的功能非常全面，包含监控SMS、访问麦克风、录制音视频、窃取通讯录和通话记录、窃取文件、实时定位等。

SpyMax的功能UI展示如下：

![](https://s.secrss.com/anquanneican/254a7d0a19a8cbef57ed14d15e79b831.png)

**样本配置信息**

样本中的钓鱼地址和主控地址，均硬编码配置在资源文件中，配置文件如下：

![](https://s.secrss.com/anquanneican/10f00c59c3f670c007e70713cd745ff0.png)

**网络资产分析**

此次攻击活动在情报分析时具有很大的难度，移动端样本采用SpyMax开发，除关键配置外，并没有开发者相关指纹信息，样本采用SpyMax默认证书和公开测试证书签名；所使用的网络资产也多为云服务商资产，都极大的剔除了自身资料，使攻击活动变得更加隐匿。以下是我们对此次攻击活动使用到的网络资产的一些分析。

**PART** **01**

**主控地址分析**

使用的2个样本的主控地址为“khalefaa-40441.portmap.host”和“nurth-36527.portmap.host”，经过分析发现，它们都来自portmap平台，此站点生成域名常常被用于恶意软件，采用的是OpenVPN服务实现，注册平台如下：

![](https://s.secrss.com/anquanneican/6fbfbcda48149177ec1913bf79d14887.png)

**PART** **02**

**钓鱼地址分析**

用于钓鱼的服务器有两个，分别用于伪装成叙利亚发展信托基金站点和社交软件Facebook登录页面。

**Syr1服务器**

我们暂且把 “syr1.store”和“syr1.online”解析的仿冒叙利亚发展信托基金站点服务器称为Syr1服务器，服务器地址为“154.56.47.207”，位于美国，域名解析结果如下：

![](https://s.secrss.com/anquanneican/481e65234f07a542abe62c7a4dc3e76e.png)

通过域名反查发现，曾解析过100+域名，域名反查结果如下：

![](https://s.secrss.com/anquanneican/3da968cbd3c42bdafa30e91843ca20ef.png)

**000webhostapp服务器**

用于钓鱼窃取Facebook账号信息的服务器域名为“shame5sham.000webhostapp.com”，它属于一家云服务器服务商，该服务商提供廉价的虚拟主机和免费的托管服务，换一个角度来看，这也降低了攻击者成本，而且能更好的隐藏自己。该服务商主页如下：

![](https://s.secrss.com/anquanneican/77d5384fb0b1b08e499337f41e854732.png)

**攻击时间分析**

通过对三个钓鱼站点的分析，结合样本打包信息，基于以下三点，我们怀疑此次攻击活动的开始时间为2023年9月份，并在不断的完善和持续攻击。

样本签名文件修改时间：

![](https://s.secrss.com/anquanneican/09a0fc6820300ed01d2e2423beff470d.png)

资产扫描发现时间：

![](https://s.secrss.com/anquanneican/df1dc3d17fcaf20b1e090cb60c56e5ac.png)

站点证书信息：

![](https://s.secrss.com/anquanneican/5e98ab36bfd856691c745204563ea196.png)

**总结**

此次针对向叙利亚军人的复合式攻击具有迷惑性强，破坏性大，难以追踪的特点，一旦感染，甚至威胁到受害者及其家人的生命财产安全。针对特定人群如何避免遭受移动端上的攻击，奇安信病毒响应中心移动安全团队提供以下防护建议：

及时更新系统和应用，在正规的应用商店下载应用。国内的用户可以在手机自带的应用商店下载，国外用户可以在Google Play下载。不要安装不可信来源的应用、不要随便点击不明URL或者扫描安全性未知的二维码。

移动设备及时在可信网络环境下进行安全更新，不要轻易使用不可信的网络环境。

不轻易开启Root权限；对请求应用安装权限、激活设备管理器等权限的应用要特别谨慎，一般来说普通应用不会请求这些权限，特别是设备管理器，正常的应用基本没有这个需求。

确保安装有手机安全软件，进行实时保护个人财产安全；如安装奇安信移动安全产品。

目前，基于奇安信自研的猫头鹰引擎、QADE引擎和威胁情报数据的全线产品，包括奇安信威胁情报平台（TIP）、奇安信天狗漏洞攻击防护系统、天擎、天机、天守、天眼高级威胁检测系统、奇安信NGSOC（态势感知与安全运营平台）、奇安信监管类态势感知等，都已经支持对此类攻击的精确检测。

**PART** **01**

**IOCs**

|  |
| --- |
| **MD5** |
| 14584006027594b856ef2bd1883138c0 |
| 87cc2f6f5e3150b6fb9a758adc74261a |

|  |
| --- |
| **C&C** |
| **syr1.store** |
| **syr1.online** |
| **shame5sham.000webhostapp.com** |
| **khalefaa-40441.portmap.host** |
| **nurth-36527.portmap.host** |

**PART** **02**

**附录1奇安信病毒响应中心**

奇安信病毒响应中心是北京奇安信科技有限公司（奇安信集团）旗下的病毒鉴定及响应专业团队，背靠奇安信核心云平台，拥有每日千万级样本检测及处置能力、每日亿级安全数据关联分析能力。

结合多年反病毒核心安全技术、运营经验，基于集团自主研发的QOWL和QDE（人工智能）引擎，形成跨平台木马病毒、漏洞的查杀与修复能力，并且具有强大的大数据分析以及实现全平台安全和防护预警能力。

奇安信病毒响应中心负责支撑奇安信全线安全产品的病毒检测，积极响应客户侧的安全反馈问题，可第一时间为客户排除疑难杂症。中心曾多次处置重大病毒事件、参与重大活动安全保障工作，受到客户的高度认可，提升了奇安信在业内的品牌影响力。

**PART** **03**

**附录2奇安信病毒响应中心移动安全团队**

奇安信病毒响应中心移动安全团队一直致力移动安全领域及Android安全生态的研究。目前，奇安信的移动安全产品除了可以查杀常见的移动端病毒木马，也可以精准查杀时下流行的刷量、诈骗、博彩、违规、色情等黑产类软件。

通过其内部分析系统可以有效支持对溯源分析等追踪。团队结合自研QADE引擎和高价值移动端攻击发现流程已捕获到多起移动攻击事件，并发布了多篇移动黑产报告，对外披露了多个APT组织活动。近三年来已首发披露五个全新APT组织（诺崇狮组织SilencerLion、利刃鹰组织BladeHawk、艾叶豹组织SnowLeopard、金刚象组织VajraEleph和沙猁猫组织Caracal Kitten）。

声明：本文来自奇安信病毒响应中心，版权归作者所有。文章内容仅代表作者独立观点，不代表安全内参立场，转载目的在于传递更多信息。如有侵权，请联系 anquanneican@163.com。

相关资讯

* ## [工信部：关于防范MuddyWater组织网络攻击的风险提示](https://www.secrss.com/articles/87230)

  [APT](https://www.secrss.com/articles?tag=APT)
  [网络安全威胁和漏洞信息共享平台](https://www.secrss.com/articles?author=网络安全威胁和漏洞信息共享平台)
  2026-01-22

  [MuddyWater组织近期针对政府、军事、电信、能源等机构实施网络攻击，窃取系统凭证、机密文件等敏感数据。](https://www.secrss.com/articles/87230)
* ## [高级持续性威胁（APT）十年嬗变](https://www.secrss.com/articles/87130)

  [APT](https://www.secrss.com/articles?tag=APT)
  [威胁棱镜](https://www.secrss.com/articles?author=威胁棱镜)
  2026-01-19

  [十年间，APT 有什么趋势性的变化？](https://www.secrss.com/articles/87130)
* ## [网军“捡漏”：数据泄露如何助力国家级APT搭建C2基础设施](https://www.secrss.com/articles/86025)

  [APT](https://www.secrss.com/articles?tag=APT)
  [黑鸟](https://www.secrss.com/articles?author=黑鸟)
  2025-12-13

  [一次普通的恶意软件感染，竟能成为国家级APT的基础设施资源来源，串联起地方性虚假信息行动与跨国网络攻击。](https://www.secrss.com/articles/86025)

* [关于我们](https://www.secrss.com/info/about)
* [联系我们](https://www.secrss.com/info/contactus)
* [用户协议](https://www.secrss.com/info/agreement)
* [隐私政策](https://www.secrss.com/info/privacy)

安全内参 © 2026 [沪ICP备19008222号-1](https://beian.miit.gov.cn)

![](https://www.secrss.com/wx_qrcode.jpg)

微信公众号
回到顶部