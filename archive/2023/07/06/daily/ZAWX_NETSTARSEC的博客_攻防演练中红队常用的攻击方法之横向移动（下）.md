---
title: 攻防演练中红队常用的攻击方法之横向移动（下）
url: https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561543
source: ZAWX_NETSTARSEC的博客
date: 2023-07-06
fetch_date: 2025-10-04T11:53:08.328227
---

# 攻防演练中红队常用的攻击方法之横向移动（下）

# 攻防演练中红队常用的攻击方法之横向移动（下）

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[网星安全（中安网星）](https://blog.csdn.net/ZAWX_NETSTARSEC "网星安全（中安网星）")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2023-07-05 18:11:34 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量551
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数

CC 4.0 BY-SA版权

文章标签：
[网络](https://so.csdn.net/so/search/s.do?q=%E7%BD%91%E7%BB%9C&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[安全](https://so.csdn.net/so/search/s.do?q=%E5%AE%89%E5%85%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131561543>

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)文章介绍了防止攻击者横向移动窃取密码的措施，包括关闭WDigest、使用KB2871997增强RDP安全性、限制Mimikatz工具的使用。此外，还讨论了防护哈希传递攻击的DefenderATP和管理层模型，并提出通过监控异常活动和更改系统配置，如防火墙规则，来提升安全性。

综合【安全科普】系列前两篇文章内容，我们可以得知，攻击者在横向移动过程中，其最终目的是登陆目标主机并窃取机密数据。

因此我们必须采取多种防护措施，以防止攻击者窃取密码或进行凭证传递。除此之外，还可利用监控手段来探查攻击者的踪迹，并增加系统配置以提高域内安全性。

接下来将会详细介绍以上所述:

**一、防止攻击者窃取密码**

在使用WDigest（摘要式身份验证）的系统中，密码会以明文形式存储在内存，攻击者通过Mimikatz可以直接抓取密码。为了防止密码泄露，我们可以关闭WDigest。

但该功能只有在Windows Server 2012以上版本的系统才能被关闭，而在Windows Server 2012以下版本的系统中只能通过安装补丁KB2871997来解决问题。

KB2871997支持RDP 网络登录，即在登录过程中使用登录令牌来进行身份验证。这种方法不会在RDP服务器中存储用户凭证，用户注销时，也会清除主机缓存中的凭证，以此来保护凭证安全。

同时，KB2871997支持创建“受保护的用户”组。只要把域功能级别设置为Windows Server 2012 R2，系统就会创建受保护的组，在该组中的用户只能使用Kerberos协议进行身份验证。相比于WDigest，Kerberos验证方式更安全，因为它不会在内存中存储明文密码。

想要防止密码被盗的话，除了安装补丁，我们还需要对攻击者常用的工具进行防范，比如Mimikatz。

由于Mimikatz与内存（LSASS进程）交互需要Debug权限，我们可以将拥有Debug权限的本地管理员从Administrators组中移出。这样，当攻击者以本地管理员身份登录时，就没有权限使用Mimikatz从内存导出密码。

**二、防护哈希传递攻击**

通过以上手段，我们能有效防止黑客从系统中窃取明文密码，但是当黑客窃取到了用户凭据，使用哈希传递等手段登录系统时，并没有一个能彻底解决哈希传递的方法，我们只能减轻这种攻击。

这里介绍两种方法——Defender ATP和微软管理层模型。

Defender ATP : 是微软提供的一种安全工具，它能检测攻击者访问LSASS进程的行为。如果发现某时刻LSASS进程被读取的内存数量过多，就会报警，提示管理员“敏感凭据内存读取”。

微软管理层模型 : 将不同权限的用户划分到不同层级，并规定高层级不能登录低层级。举例来说，将能够访问网络上所有关键服务器的管理员划分为第0级，将工作站管理员划分为第2级，那么即使黑客窃取到了关键服务器管理员的凭证，以管理员身份也无法登录关键服务器。

**三、监控异常活动**

攻击者横向移动过程通常难以被察觉，但我们可以分析其行为特征，监控是否有存在满足其特征的活动来确定系统是否被入侵。

对于在目标范围内安装恶意软件的横向攻击行为，我们可以监控应用安装情况。例如当安装应用的时间固定在一个时间段，而其它时间段的安装行为都将被认为是异常的。

攻击者进行横向移动攻击的另一个典型行为就是窃取信息。通过监控文件创建行为和SMB传输文件行为，可以发现远程文件复制活动；通过监控可移动介质上的文件访问，能识别可移动介质复制行为；通过监控多文件写入共享能发现共享文件污染行为等。

如果攻击者已进入内网，为了防止他横向移动到更多主机，我们可以监测内网中活跃的用户账号，将这些账户设置为高风险账户，降低其权限，阻止其使用内网资源。

监控内网中的异常活动，能帮助我们发现攻击者侵入企业内网的行为，以便及时采取措施阻止其损害企业利益。

**四、更改系统配置**

给系统配置防火墙是防范一般网络攻击的重要手段，对横向移动攻击也能起到一定的作用。比如，通过配置防火墙的进站/出站规则阻止445端口的连接，能防范利用SMB协议漏洞的攻击；启用防火墙禁止RDP流量能防止RDP远程连接系统；启动域防火墙能阻止DCOM对象实例化。

此外，我们也可以通过配置Windows系统规则来防范横向移动攻击。

当攻击者利用Windows打印机后台处理程序来执行特权操作时，我们可以禁用“允许打印后台处理程序接收客户端连接”，也可以直接禁用打印后台处理程序服务。

当系统遭受NTLM中继攻击时，我们可以禁用NTLM并切换成Kerberos验证，或启用SMB签名和LDAP签名等。（NTLM中继攻击：攻击者劫持受害者会话，将受害者凭证转发到其它服务器获取信任）

正确配置系统规则，不仅能防范横向移动攻击，还能保护系统资源的合法使用

**结语**

攻击者进行横向移动的手法多种多样，以上方法并不能完全防范横向移动攻击。要有效阻止横向移动，需要分析具体事件来制定有针对性的防护措施。

尤其是在企业等组织机构中，由于内网的复杂性，攻击团伙的手段也比较高超，一般的防护手段不能有效地防范横向移动攻击，要保护企业内网安全，最好选择专业的运营团队。

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
439

[具体而言，正如 EDR 对端点设备的行为进行分析，ITDR通过AI 和机器学习技术，对以Active Directory 和 Okta为代表的身份基础设施上交换的身份验证流量的行为进行分析。即使您能够使用IAM等尽可能适当地设置公司的身份基础设施环境，毫不夸张地说，想要完全阻止攻击者通过巧妙的方法入侵您的身份基础设施是不可能的。此外，在多AD和域环境中实现灵活的身份访问管理的Okta等各种IAM解决方案的采用和引入，以及向Azure AD的迁移以及SSO向SaaS的迁移也在逐步发展。](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131768506)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[K8S安全风险及防护建议](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131766750)

07-17
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1161

[例如，攻击者可以创建一个特权容器，该容器可以访问宿主机上的资源，并在该容器内执行命令，从而使其获得更高的权限。事中，通过融合图计算、身份欺骗等技术，对K8S进行全方位的监测，及时发现针对K8S的漏洞利用、身份窃取等风险，在遭受攻击的第一时间及时发现攻击者，对攻击行为进行阻断。比如攻击者可通过容器中运行的SSH服务执行命令，如果攻击者通过暴力破解或者其他方法获得了容器的有效凭证，他们就可以通过SSH获得对容器的远程访问。但同时，K8S也因其高度复杂的架构和众多组件，成为了攻击者攻击的目标之一。](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131766750)

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
849

[通过已经识别到的攻击对即将发生的攻击进行预警，企业可以提前做好准备，加强系统和网络的安全防护措施，阻止潜在的攻击行为，并保护重要的业务和敏感数据。其次，ITDR提供了风险提示功能。同时凭借自身强大的算力以及庞大的攻击数据样本可以就当前基线配置，进行攻击推演拟合出攻击线路，运营人员可以采取针对性的措施来加固安全防护，斩断攻击路径中的关键节点，保护其关键资产免受攻击的同时避免对业务的流畅性造成影响。通过与预先设定的基线进行比对，模型能够及时发现与正常状态有所偏离的设置，从而识别出潜在的安全漏洞和风险点。](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131452991)

![](https://csdnimg.cn/release/blogv2/dist/components/i...