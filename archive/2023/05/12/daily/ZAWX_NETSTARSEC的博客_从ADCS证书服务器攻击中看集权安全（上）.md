---
title: 从ADCS证书服务器攻击中看集权安全（上）
url: https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/130621491
source: ZAWX_NETSTARSEC的博客
date: 2023-05-12
fetch_date: 2025-10-04T11:38:08.834996
---

# 从ADCS证书服务器攻击中看集权安全（上）

# 从ADCS证书服务器攻击中看集权安全（上）

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[网星安全（中安网星）](https://blog.csdn.net/ZAWX_NETSTARSEC "网星安全（中安网星）")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2023-05-11 14:38:57 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量322
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

2

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数

CC 4.0 BY-SA版权

文章标签：
[服务器](https://so.csdn.net/so/search/s.do?q=%E6%9C%8D%E5%8A%A1%E5%99%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[安全](https://so.csdn.net/so/search/s.do?q=%E5%AE%89%E5%85%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/130621491>

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文分析了ADCS（Active Directory Certificate Services）的安全风险，特别是在证书模板错误配置下的攻击手段，如ESC1、ESC2、ESC3和ESC4。攻击者可能通过这些漏洞获取域控制器权限，影响AD集权安全。文章讨论了PKI、CA、证书模板等概念，并介绍了证书注册流程和PKINIT协议，展示了如何通过证书模板错误配置进行权限提升攻击。

在2021年的BlackHat大会上，由Will Schroeder和Lee Christensen发布了关于Active Directory Certificate Services 利用白皮书《Certified Pre-Owned - Abusing Active Directory Certificate Services》，其中包含了大量的针对ADCS的攻击手法，通过对ADCS的攻击，将域渗透的攻击面扩展到了最大。尽管ADCS并不是默认安装在域环境中，但是在一些大型企业的域环境中却被广泛部署。

**本文分为上中下三篇，重点介绍如何在域环境中使用ADCS技术攻击域控制器，以及如何利用对象ACL来维持更高的权限。同时，我们将深入探讨ADCS的基础架构、攻击面以及后利用。这些内容将通过实战演练的方式进行讲解。**

### **一、技术背景**

**1.什么是PKI？**

**公钥基础建设** (Public Key Infrastructure，简称PKI) 是一组由硬件、软件、参与者、管理者与流程组成的基础架构，其目的在于创造、管理、分配、使用、存储以及撤销**数字证书**。PKI依赖于经过身份验证的用户和受信任的资源之间的数字证书交换。可以使用证书来保护数据安全，并管理来自组织内外的用户和计算机的标识凭据。

**2.什么是CA？**

**数字证书认证机构** (Certificate Authority，简称CA) 是负责签发证书、认证证书、管理已颁发证书的权威机构。它要制定政策和具体步骤来验证、识别用户身份，并对用户证书进行签名，以确保证书持有者的身份和公钥的拥有权。

**3.什么是证书？**

证书是一个小文件，此文件包含了公钥信息、拥有者身份信息、以及数字证书认证机构对这份文件的数字签名，以保证这个文件的整体内容正确无误。

拥有者凭此文件，可向电脑系统或者其他用户表明身份，从而获得对方的信任并授权访问或使用某些敏感的电脑服务。在证书注册过程中，客户端会生成公钥/私钥对，然后客户端将公钥发送到CA，而CA会确认客户端信息，用自己的私钥对其进行签名，随后再将包含客户端公钥的证书发送回客户端。

在概念上，证书相当于驾照，交警部门相当于CA。将身份信息与考核情况递交给交警部门，他们会给我们一个带有特有盖章的驾照，这样才可以开车上路。乘客会因为驾照而信任你的驾车技术，因为只有通过考核交警部门才会给你发驾照。如果严重违反了交通规则，你会被吊销驾照，不能开车载人。

**4.什么是ADCS？**

AD域作为当前企业的办公内网广泛应用的集权管理方案，其域控在AD域内扮演着“大脑”的角色，至关重要，而不少企业在会在安装AD域的同时安装ADCS证书服务器来管理证书，攻击者会针对ADCS来进行攻击从何获取域控权限，导致AD集权安全收到威胁。

**5.搭建ADCS**

搭建ADCS可参考文章[https://learn.microsoft.com/zh-cn/windows-server/networking/core-network-guide/cncg/server-certs/install-the-certification-authority](https://link.zhihu.com/?target=https%3A//learn.microsoft.com/zh-cn/windows-server/networking/core-network-guide/cncg/server-certs/install-the-certification-authority "https://learn.microsoft.com/zh-cn/windows-server/networking/core-network-guide/cncg/server-certs/install-the-certification-authority")注意不要将证书服务器和域控搭建在一台主机上。

### **二、什么是证书模板？**

证书模板定义了用户和设备如何根据模板来请求和使用企业CA颁发的证书。例如你可以创建一个模板来提供文件加密或电子邮件签名功能。CA依赖于ADDS来存储配置的模板。注意，只有在使用企业CA时才可以使用证书模板，这意味着，在使用独立CA时，必须手动创建每个证书请求，并添加需要在证书中包含的必须信息。

CA针对用户和计算机提供了模板，**可以向证书模板分配相应的权限**，以定义可以管理模板的人员、可以执行注册或自动注册的人员，以及默认的有效期和续订期。可以**通过复制预定义的证书模板来应用其他修改**。

**1.模板版本**

Windows Server AD CS 中的 CA 支持四个版本的证书模板，它们具有以下功能差异：

* 版本 1 模板。这些模板只允许修改与证书相关的权限。在安装 CA 时，默认情况下会创建版本 1 证书模板。
* 版本 2 模板。利用这些模板，可以自定义其他设置，如有效期和续订期。这也是支持自动注册的最低版本。AD CS 的默认安装内容包含多个预配置的版本 2 模板。你可以创建版本 2 模板，也可以复制版本 1 证书模板来创建新的版本 2 模板。
* 版本 3 模板。版本 3 证书模板支持下一代加密技术 (CNG)。CNG 支持高级加密算法。可以复制默认版本 1 和版本 2 模板，并将其升级到版本 3。使用版本 3 证书模板时，可以将 CNG 加密和哈希算法用于证书请求、颁发的证书，以及密钥交换和密钥存档方案的私钥保护。
* 版本 4 模板。版本 4 证书模板支持加密服务提供程序 (CSP) 和密钥存储提供者。还可以将其配置为要求使用相同的密钥进行续订。

可以使用certtmlp.msc打开证书模板控制台，使用certsrv.msv打开证书颁发机构。

![](https://i-blog.csdnimg.cn/blog_migrate/712b3826d0bc029de8516daf580744f0.png)

其中版本架构就是我们上面所说的模板版本，预期用途就是这个证书模板申请之后用来干什么，例如可以客户端身份验证、服务器身份验证等，**如果要设置模板特定用途可以右击模板属性在应用程序策略中添加或删除证书模板用途。**

![](https://i-blog.csdnimg.cn/blog_migrate/140b8c0d464558c74ed25d6134f34124.png)

在证书模板属性中我们主要关注使用者名称、发布要求、扩展和安全。

<

![](https://csdnimg.cn/release/blogv2/dist/pc/img/lock.png)最低0.47元/天 解锁文章

200万优质内容无限畅学

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

  2

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
[ITDR何以成为IAM的最佳搭档？](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131768506)

07-17
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
438

[具体而言，正如 EDR 对端点设备的行为进行分析，ITDR通过AI 和机器学习技术，对以Active Directory 和 Okta为代表的身份基础设施上交换的身份验证流量的行为进行分析。即使您能够使用IAM等尽可能适当地设置公司的身份基础设施环境，毫不夸张地说，想要完全阻止攻击者通过巧妙的方法入侵您的身份基础设施是不可能的。此外，在多AD和域环境中实现灵活的身份访问管理的Okta等各种IAM解决方案的采用和引入，以及向Azure AD的迁移以及SSO向SaaS的迁移也在逐步发展。](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131768506)

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
![](https://csdnimg.cn/release/blogv2/dist/pc/img/...