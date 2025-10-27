---
title: ITDR何以成为IAM的最佳搭档？
url: https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131768506
source: ZAWX_NETSTARSEC的博客
date: 2023-07-18
fetch_date: 2025-10-04T11:52:50.579589
---

# ITDR何以成为IAM的最佳搭档？

# ITDR何以成为IAM的最佳搭档？

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[网星安全（中安网星）](https://blog.csdn.net/ZAWX_NETSTARSEC "网星安全（中安网星）")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2023-07-17 16:03:01 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量438
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数

CC 4.0 BY-SA版权

文章标签：
[安全](https://so.csdn.net/so/search/s.do?q=%E5%AE%89%E5%85%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131768506>

**摘 要**

❖随着零信任方案的逐渐落地，身份成为企业的新边界。同时，身份基础设施成为了攻击焦点。

❖最近的身份攻击变得更加巧妙和复杂，甚至可以绕过MFA。

❖当前的IAM解决方案只能起到预防作用。

❖企业更需要一个能够检测和响应身份威胁的 ITDR 解决方案。

❖ITDR 供应商目前被收购和整合发展迅速。

❖选择 ITDR 解决方案时需要考虑两点：

(1) 能够接入多场景，不限于AD。

(2) 从不同的供应商处分别购买 IAM 和 ITDR，以避免锁定的风险。

### **零信任时代到来，身份是新的边界和漏洞**

零信任作为新安全框架，在日本推广进度迅猛，其核心思想是基于传统身份边界的身份验证和授权的转变。

另一方面，随着组织转向零信任并越来越依赖以身份基础设施为中心的环境，意味着身份基础设施成为攻击者的最佳目标。事实上，我们还发现，凭据滥用这一攻击手段正在被黑客广泛利用。

![](https://i-blog.csdnimg.cn/blog_migrate/112407ee2b5e26bb3bac05e43fa97bb5.png)

### **近年来不断增加的身份威胁和攻击是什么？**

特定的身份威胁会潜入目录服务器（如 Active Directory）、基于云的标识和访问管理 (IAM) 解决方案（如 Okta 和 Azure AD）以及身份基础设施（如证书颁发机构）。它是指通过跟踪易受攻击的设置来获取特权身份等凭据信息并进行渗透的网络攻击。

由于它在没有像过去那样使用恶意软件进行远程控制的情况下入侵，因此无法被 EDR 等恶意软件检测引擎检测到。

近来，安全研究人员发现即便启用了多因素身份认证保护措施，用户仍可能收到钓鱼攻击的侵害，并且针对身份的攻击变得越来越复杂。

![](https://i-blog.csdnimg.cn/blog_migrate/3e0c3a05c818732b7cf468556ee9de5d.png)

### **现有的身份管理方案（IGA、PAM、CIEM）只是预防**

那么，是否有可能使用我们目前使用的各种身份和访问管理工具（如IAM，IGA，PAM和CIEM）来应对这些攻击？

像Savyint这样的IGA（身份治理和管理）和像CyberArk这样的PAM（特权访问管理）也具有防止不必要的特权身份过度配置的功能。对于 AWS 和 Azure 等云基础设施环境，使用以CIEM为代表的云基础设施授权管理功能，可以发现并防止过多的云身份权限颁发和脆弱的IAM设置。

此外，通过在云上或者本地应用IAM 提供的 MFA（多因素认证），可以最大程度地减少管理员权限被利用的机会（例如，更改为每次执行 SSH 或 RDP 时都需要 MFA 的定时设置）。

但是，如上所述的身份管理解决方案本身所提供的功能，只是预防身份攻击，并不能在IAM基础设施被入侵后进行相应的检测与阻断。

### **ITDR——身份威胁检测与响应**

即使您能够使用IAM等尽可能适当地设置公司的身份基础设施环境，毫不夸张地说，想要完全阻止攻击者通过巧妙的方法入侵您的身份基础设施是不可能的。基于身份基础设施将受到威胁的假设，有必要单独考虑在其遭到入侵后如何检测和响应对身份基础设施的威胁。

我们可以通过新的解决方案——ITDR（身份威胁检测与响应）来实现。

ITDR 是一种与EDR（端点检测和响应）、NDR（网络威胁检测和响应 ）相邻的新解决方案。具体而言，正如 EDR 对端点设备的行为进行分析，ITDR通过AI 和机器学习技术，对以Active Directory 和 Okta为代表的身份基础设施上交换的身份验证流量的行为进行分析。

ITDR能够检测与异常行为或威胁情报相一致的可疑身份，并实现各种“响应”，例如阻止来自相应ID 的身份验证以及与IAM一起请求额外的 MFA，例如 Okta。

![](https://i-blog.csdnimg.cn/blog_migrate/23f74d09094e16ef115ef96cd80ea064.png)

### **正在被快速收购和整合的ITDR供应商**

过去几年中，对身份基础设施的攻击快速增长以及XDR多种检测技术的日益集成导致EDR供应商（如CrowdStrike和SentinelOne）迅速收购和整合ITDR供应商。

像Proofpoint这样的安全供应商已收购威胁管理提供商ObserveIT，意在加强公司的企业网络安全产品组合。ITDR目前是一个新兴类别，许多供应商仍然保持独立研发运营，并且头部安全供应商对ITDR这条赛道的前景十分认可，预计对ITDR供应商的收购还将持续很长一段时间。

一些头部安全供应商的收购新闻

2020年9月，CrowdStrike 以9600万美元的价格收购零信任网络安全初创公司Preempt Security。

2022年3月，SentinelOne宣布达成6.165亿美元交易,收购身份安全供应商Attivo Networks。

### **选择ITDR，你应该注意这两点**

ITDR是一个新兴类别的解决方案，目前已有10多种ITDR解决方案，每个公司的方案各有特点。以下是选择 ITDR 解决方案时需要考虑的几个关键点：

**（1）能够接入多场景，不限于AD**

作为身份基础设施的核心，Active Directory被广泛使用。此外，在多AD和域环境中实现灵活的身份访问管理的Okta等各种IAM解决方案的采用和引入，以及向Azure AD的迁移以及SSO向SaaS的迁移也在逐步发展。

因此，不仅要全面保护Active Directory，各种IAM解决方案都需要作为企业应该保护的身份基础设施进行全面保护。选择能够支持多场景的ITDR解决方案非常重要。某些ITDR解决方案只支持AD，有时被称为“ADTR”而不是“ITDR”。

![](https://i-blog.csdnimg.cn/blog_migrate/55538ff04392fe8ac5912857258ddbb6.png)

**（2）从不同的供应商处分别购买 IAM 和 ITDR**

随着ITDR重要性的增加，IAM供应商将以选项或子集的形式提供ITDR功能。

企业所使用的IAM解决方案并非只有一种，可以使用多家供应商的解决方案。由于使用特定 IAM 供应商提供的 ITDR 功能存在供应商锁定的风险，因此我们建议您购买来自不同供应商的 IAM 和ITDR解决方案。

![](https://i-blog.csdnimg.cn/blog_migrate/fa5e7f26a8af58895cef95a6b5b89684.png)

国际上，Silverfort、Authomize等安全厂商已经探索出了相对成熟的ITDR解决方案。而国内对ITDR技术的探索实践刚刚起步。

中安网星依托于多年的攻防经验，率先在国内拓展ITDR解决方案。**中安网星ITDR（身份威胁检测与响应）平台主要围绕Identity及Infrastructure为核心进行防护，涵盖主流身份基础设施及集权设施，从攻击的事前加固、事中监测、事后阻断出发，产品的设计思路覆盖攻击者活动的全生命周期。**

基于身份的攻击活动不断增长，攻击手段越来越难以防范，对企业网络安全的管理者提出更加严苛的要求。中安网星将继续立足于用户的根本需求，通过对ITDR技术的深度钻研与应用实践，助力客户构建起更加主动的身份威胁检测和响应能力。

\*本文部分节选自MACNICA公司发表的《ITDRとは？～ID脅威を検知・対応する注目の新ソリューション～》一文。

原文链接：

https://mnb.macnica.co.jp/2023/01/zerotrust/itdr.html

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/8b87a58891594bbaab06aa3616d9a702_zawx_netstarsec.jpg!1)

网星安全（中安网星）](https://blog.csdn.net/ZAWX_NETSTARSEC)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  0

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  0

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

参与评论
您还未登录，请先
登录
后发表或查看评论

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[K8S安全风险及防护建议](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131766750)

07-17
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1160

[例如，攻击者可以创建一个特权容器，该容器可以访问宿主机上的资源，并在该容器内执行命令，从而使其获得更高的权限。事中，通过融合图计算、身份欺骗等技术，对K8S进行全方位的监测，及时发现针对K8S的漏洞利用、身份窃取等风险，在遭受攻击的第一时间及时发现攻击者，对攻击行为进行阻断。比如攻击者可通过容器中运行的SSH服务执行命令，如果攻击者通过暴力破解或者其他方法获得了容器的有效凭证，他们就可以通过SSH获得对容器的远程访问。但同时，K8S也因其高度复杂的架构和众多组件，成为了攻击者攻击的目标之一。](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131766750)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[攻防演练中红队常用的攻击方法之横向移动（下）](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561543)

07-05
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
551

[启动域防火墙能阻止DCOM对象实例化。通过以上手段，我们能有效防止黑客从系统中窃取明文密码，但是当黑客窃取到了用户凭据，使用哈希传递等手段登录系统时，并没有一个能彻底解决哈希传递的方法，我们只能减轻这种攻击。尤其是在企业等组织机构中，由于内网的复杂性，攻击团伙的手段也比较高超，一般的防护手段不能有效地防范横向移动攻击，要保护企业内网安全，最好选择专业的运营团队。如果攻击者已进入内网，为了防止他横向移动到更多主机，我们可以监测内网中活跃的用户账号，将这些账户设置为高风险账户，降低其权限，阻止其使用内网资源。](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561543)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[攻防演练中红队常用的攻击方法之横向移动（中）](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561532)

07-05
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
647

[尤其是主机RDP相关的弱口令，这类系统远控桌面服务的弱口令一旦被黑客利用，就能通过“撞库”等方式暴力破解，进而实现内网计算机的远程控制。例如，在前不久的美国燃油管道勒索攻击事件中，darkside攻击团伙从文件、内存和域控制器中收集凭据，并利用这些凭据来登录其它主机，再对重要数据和控制端口进行加密，进而实施勒索。黑客为了造成更大影响，通常选择重要的信息系统，如金融、电信、交通、能源等计算机系统，利用横向移动进行大面积网络攻击，导致系统瘫痪，严重影响基本的社会生活。黑客横向移动的手段已经非常成熟。](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561532)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[攻防演练中红队常用的攻击方法之横向移动（上）](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561487)

07-05
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1104

[实际上，在横向移动攻击过程中，攻击者不仅可以运用相关技术与思路访问共享文件夹、凭证等敏感信息，也可以通过“横向移动”的方法渗透其它...