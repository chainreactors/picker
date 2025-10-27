---
title: IAM的主流身份验证方法之OIDC协议
url: https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/130711256
source: ZAWX_NETSTARSEC的博客
date: 2023-05-17
fetch_date: 2025-10-04T11:37:11.639314
---

# IAM的主流身份验证方法之OIDC协议

# IAM的主流身份验证方法之OIDC协议

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
[网星安全（中安网星）](https://blog.csdn.net/ZAWX_NETSTARSEC "网星安全（中安网星）")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2023-05-16 18:07:54 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

5

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
1

CC 4.0 BY-SA版权

文章标签：
[网络](https://so.csdn.net/so/search/s.do?q=%E7%BD%91%E7%BB%9C&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[服务器](https://so.csdn.net/so/search/s.do?q=%E6%9C%8D%E5%8A%A1%E5%99%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[运维](https://so.csdn.net/so/search/s.do?q=%E8%BF%90%E7%BB%B4&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/130711256>

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)本文详细介绍了OpenID Connect (OIDC) 协议，包括OIDC的发展历史、与OAuth2.0的区别，以及认证流程。重点讨论了OIDC的安全性，如SSRF、接口泄露、令牌伪造等问题，并列举了实际的漏洞案例，帮助读者理解OIDC的攻击面和潜在风险。

### 一、OIDC协议介绍

#### 1.OIDC简介

OpenID Connect（简称OIDC）是一种安全认证机制，第三方应用连接到身份认证服务器（Identify Service）获取用户信息，并把这些信息以安全可靠的方式返回给第三方应用。

OAuth2.0通过Access Token作为向第三方应用授权访问自身资源的凭证。OpenID Connect对OAuth2.0进行协议进行了扩展，通过扩展的ID Token字段，提供用户基础身份信息，ID Token使用JWT（JSON Web Token）格式进行封装，提供自包含性、防篡改机制，可以安全的传递给第三方应用程序并容易被验证。除了ID Token，还可以通过Access Token从认证服务的UserInfo Endpoint接口获取更详细的用户信息。

#### **2.发展历史**

* 2014年，OIDC规范发布。
* 2015年，OIDC认证计划启动。
* 2021年，OIDC联合规范第三实施者草案获得批准。
* 2022年，OIDC注销规范得以确定。

从这些时间点我们可以看出，OIDC的发展也是一个漫长且历经考验的过程，相对CAS、Oauth之类的协议，他具有长足的优势才能在的检验之后应用到大众的生活中，前面我们讲了一些用于单点登陆的身份协议，比如我们熟知的Oauth协议，Oauth从授权的角度来讲已经很完善了，为什么还会出现基于Oauth 2.0的OIDC协议呢，我们下面来进行介绍

#### 3.为什么会出现OIDC？

大家已经学习过Oauth了，而且在生活中Oath的使用也相当广泛，而且相比于其他协议，Oauth安全性也有很大的提高，那么Oauth已经算是不错了，为什么还会有OIDC的出现呢，因为在Oauth协议的认证流程里，强调的是针对授权、授权范围以及给客户端哪些信息，并没有对用户有特殊的验证机制，换句话说，在Oauth流程中，它的重点是授权，那么OIDC呢，是认证。打个不太恰当的比方，Oauth只是门上插了一把钥匙，谁都可以打开这扇门，OIDC是指纹锁，只有特定的用户才可以打开。

#### 4.OIDC和OAuth2.0的区别

Oauth流程注重的是授权，是验证统信实体是否有权限访问资源的过程，即“用户能做什么”，OIDC更注重认证的过程，确保通信实体是其所声称的实体，即“是哪一个用户”。

①OIDC流程中，授权服务器验证成功会响应会返回一个ID令牌，这在Oauth里是没有的。

②OIDC流程中客户端请求会在请求范围参数中包含字符串“openid”，当然，基本的OIDC架构是这样的，这一条并不绝对，因为随着OIDC的普及，我们也看到了一些重新开发过的OIDC实现，是没有这一部分的

③在Oauth的认证流程里，对于响应的令牌格式是没有规定，但是OIDC规定了令牌的格式为JWT。其实在实际应用的时候，很多Oauth其实也用的是JWT格式的令牌

#### 5.OIDC协议前置知识

客户端：客户端指的是用户访问的web应用或者移动应用。也叫RP。

用户代理：用户代理指的是用户用于访问客户端的工具，通常为浏览器。

授权范围（scope）：OIDC规范明确定义了客户端向认证服务器发起授权请求时必须在请求的scope参数中声明授权范围。

ID令牌（id\_token）：认证服务器验证用户身份后，除了向客户端返回响应令牌和刷新令牌，还会返回一个标识令牌所有者的ID令牌（id\_token）。

响应类型（response\_type）：响应类型请求参数response\_type告知授权服务器所需的授权处理流程，包括从使用的端点返回的参数。

#### 6.OIDC认证协议认证流程

![](https://i-blog.csdnimg.cn/blog_migrate/27fed494b03c8b8d61dc7ab8baf5504d.png)

上面是从OIDC规范里扒的认证流程图，刚刚我们说了这里面的OP和RP。

RP就是客户端，也就是供用户访问的web应用，OP就是身份认证提供者，也可以说是认证服务器，用于对用户和客户端进行身份验证并颁发令牌。这里展示的是通常情况下用户不能看到的部分，也就是在认证流程中，用户代理访问的web应用或者移动应用与认证服

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

  1

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  5

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  1](#commentBox)

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

1 条评论
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

[实际上，在横向移动攻击过程中，攻击者不仅可以运用相关技术与思路访问共享文件夹、凭证等敏感信息，也可以通过“横向移动”的方法渗透其它主机，窃取商业数据、财务信息等。除此以外，还能以域控主机为跳板，横向移动到其它域内主机，通过已获取的密码直接登录目标主机，执行远程命令，完成域内控制，进而以关键信息与权限为由，实施勒索行为。此时，黑客会在已控制的普通主机上查找与目标主机和环境相关的信息，获知目标主机开放的端口、存在的漏洞等，然后利用该漏洞渗透目标主机获取凭证，再使用哈希传递、黄金白银票据等方式进行登录。](https://blog.csdn.n...