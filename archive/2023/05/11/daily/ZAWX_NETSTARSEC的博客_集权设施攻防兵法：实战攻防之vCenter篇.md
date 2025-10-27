---
title: 集权设施攻防兵法：实战攻防之vCenter篇
url: https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/130607298
source: ZAWX_NETSTARSEC的博客
date: 2023-05-11
fetch_date: 2025-10-04T11:37:09.246573
---

# 集权设施攻防兵法：实战攻防之vCenter篇

# 集权设施攻防兵法：实战攻防之vCenter篇

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2023-05-10 18:35:38 发布
·
428 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

0

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

0
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#服务器](https://so.csdn.net/so/search/s.do?q=%E6%9C%8D%E5%8A%A1%E5%99%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#网络安全](https://so.csdn.net/so/search/s.do?q=%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#网络](https://so.csdn.net/so/search/s.do?q=%E7%BD%91%E7%BB%9C&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文探讨了黑客为何瞄准vCenter，常见的攻击路径和手段，以及攻击vCenter可能带来的严重损失。同时，提供了vCenter的安全加固最佳实践和中安网星ITDR平台的防御方案，以应对vCenter的各类安全威胁。

### **一、黑客视角下的vCenter**

在现实的攻防场景中，越来越多的攻击者开始关注vCenter。因为vCenter涉及资产多，拥有权限大，攻击者对vCenter实施攻击，如果攻击成功，可以让他们迅速地建立攻击据点，为后续攻击提供有利条件。

回归本质，攻击者喜欢攻击vCenter，都得益于利用vCenter存在的漏洞进行攻击，对漏洞进行利用往往能够起到事半功倍的效果。

在vCenter中被攻击者经常利用的漏洞及手法有CVE-2021-21972、CVE-2021-21985、CVE-2021-22005、Provider-logo SSRF漏洞、log4j2 JNDI注入、SAML证书登录、CVE-2022-22948权限配置不当、CVE-2021-22015、提权等，以实现获取初步权限或者权限的提升，为后续深入利用提供条件。

对于攻击者来说，对vCenter发起攻击，具有强烈的目的性：

**1.为什么要攻击vCenter？**

vCenter人送外号小域控，拿下vCenter之后，不单单只是获取一台服务器的权限，vCenter中存在的虚拟机以及ESXI主机都有可能成为后续的攻击目标，因此拿下vCenter的价值不亚于域控的价值。

**2.怎么寻找公网的vCenter？**

通过搜索语法查找公网vCenter服务器，一般vCenter开放的端口为5480。此外，使用工具获取网页title时，也可以发现vCenter服务器。

```
title="+ ID_VC_Welcome +"
```

**3.获取到vCenter权限之后应该做什么？**

获取到vCenter一定权限之后，继续进行信息收集，对vCenter中的虚拟机和ESXI主机进行攻击，将会成为主要目标。

### **二、攻击者如何攻击vCenter？**

攻击者对vCenter实施攻击的方式多种多样，以下是一些常见的攻击方式：

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
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
647

[尤其是主机RDP相关的弱口令，这类系统远控桌面服务的弱口令一旦被黑客利用，就能通过“撞库”等方式暴力破解，进而实现内网计算机的远程控制。例如，在前不久的美国燃油管道勒索攻击事件中，darkside攻击团伙从文件、内存和域控制器中收集凭据，并利用这些凭据来登录其它主机，再对重要数据和控制端口进行加密，进而实施勒索。黑客为了造成更大影响，通常选择重要的信息系统，如金融、电信、交通、能源等计算机系统，利用横向移动进行大面积网络攻击，导致系统瘫痪，严重影响基本的社会生活。黑客横向移动的手段已经非常成熟。](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561532)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[攻防演练中红队常用的攻击方法之横向移动（上）](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561487)

07-05
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1104

[实际上，在横向移动攻击过程中，攻击者不仅可以运用相关技术与思路访问共享文件夹、凭证等敏感信息，也可以通过“横向移动”的方法渗透其它主机，窃取商业数据、财务信息等。除此以外，还能以域控主机为跳板，横向移动到其它域内主机，通过已获取的密码直接登录目标主机，执行远程命令，完成域内控制，进而以关键信息与权限为由，实施勒索行为。此时，黑客会在已控制的普通主机上查找与目标主机和环境相关的信息，获知目标主机开放的端口、存在的漏洞等，然后利用该漏洞渗透目标主机获取凭证，再使用哈希传递、黄金白银票据等方式进行登录。](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561487)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[中安网星版大模型来了！三大关键能力，不输专业红队攻击手](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131452991)

06-29
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
848

[通过已经识别到的攻击对即将发生的攻击进行预警，企业可以提前做好准备，加强系统和网络的安全防护措施，阻止潜在的攻击行为，并保护重要的业务和敏感数据。其次，ITDR提供了风险提示功能。同时凭借自身强大的算力以及庞大的攻击数据样本可以就当前基线配置，进行攻击推演拟合出攻击线路，运营人员可以采取针对性的措施来加固安全防护，斩断攻击路径中的关键节点，保护其关键资产免受攻击的同时避免对业务的流畅性造成影响。通过与预先设定的基线进行比对，模型能够及时发现与正常状态有所偏离的设置，从而识别出潜在的安全漏洞和风险点。](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131452991)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[集权设施管理-AD域安全策略（二）](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131202295)

06-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1506

[本文我们探讨了AD域的资源管理、身份验证和策略配置等功能属性，此基础上，更多特性等着我们在企业应用实践中一一探索。同时，AD域在发展得越来越适应企业管理需求时，也面临着更多针对它的独特攻击手法。在大量应用AD域的基础上，我们也应当注重其安全防护建设。](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131202295)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[集权设施管理-AD域安全策略（一）](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131202106)

06-14
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1491

[实际上，域树域林的形成是借助了活动目录...