---
title: 从RPC协议看集权设施防护
url: https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131106255
source: ZAWX_NETSTARSEC的博客
date: 2023-06-09
fetch_date: 2025-10-04T11:44:13.710141
---

# 从RPC协议看集权设施防护

# 从RPC协议看集权设施防护

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[网星安全（中安网星）](https://blog.csdn.net/ZAWX_NETSTARSEC "网星安全（中安网星）")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2023-06-08 13:56:29 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量670
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数

CC 4.0 BY-SA版权

文章标签：
[rpc](https://so.csdn.net/so/search/s.do?q=rpc&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[服务器](https://so.csdn.net/so/search/s.do?q=%E6%9C%8D%E5%8A%A1%E5%99%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[网络](https://so.csdn.net/so/search/s.do?q=%E7%BD%91%E7%BB%9C&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/ZAWX_NETSTARSEC/article/details/131106255>

![](https://img-home.csdnimg.cn/images/20240711042549.png)RPC协议使得程序能在不同机器间进行通信，通过客户端存根和服务器存根处理序列化和寻址等复杂过程，提高效率。但同时，RPC也存在安全风险，如Zerologon和Printnightmare漏洞，提醒我们在使用中需要注意安全防护。

RPC协议主要用来进行远程过程调用，用一句话来概括，就是允许用户程序调用服务器上的函数进行计算，由此实现两者交互。

早先的企业环境中，所有的服务都在一台主机上，就会导致服务器负荷过重，无法保证业务的正常运作。正因如此，后来企业就更换了一种思路，将不同服务分开，分别存放在不同主机上，暂时解决了负荷问题。但是久而久之，这样的方式也开始显现弊端，比如当用户需要使用不同服务器上的服务协作来完成任务时，服务与服务之间该如何交互？

这就是RPC要解决的问题，简言之，RPC可以允许一台机器上的程序调用另一台机器上的函数，通过各计算机协作进行计算，以保证用户任务顺利完成

接下来我们详细说说RPC的原理。

## RPC原理

同AD域内的大多数协议一样，RPC也采用的是请求响应模式。通常的请求响应，只需要客户端和服务器直接做交互就行了，但在RPC中，增加了两个处理过程，即客户端存根和服务器存根。

此存根的作用为：当客户端想调用服务器上的某函数时，需要把客户端的参数提供给服务器。而为了保证参数的保密、完整、可用和响应的高效性，客户端需要对传输过程做些特殊处理，包括将数据序列化、封装数据、寻址、传递数据等。

如果这一系列复杂行为都由客户端来操作，将会耗时耗力，所以RPC就建立了一个存根，让它来协调管理这些过程，减轻客户端负担。

在存根的作用下，客户端将参数递交给它，后续只需要等待接收服务器返回的数据就行了。因此，用户其实是感受不到这个跟服务器交互的过程的，这一切似乎都像在本机上完成的一样。

以上内容，我们提到存根的一个重要作用——序列化。

所以，什么是序列化？

客户端把参数交给存根后，如果存根直接将参数交给服务器，当服务器的系统与客户端不一样时，服务器就不能解析该参数，也无法调用相应函数，等于客户端也就得不到正确的返回结果。

为了让服务器能正确解析客户端的参数，我们就需要将参数转化成服务器能理解的方式。

在RPC中，客户端存根就把要传递的数据信息序列化成二进制，以方便服务器识别并处理。

这里的数据信息不单包括参数，还有要调用的函数ID。客户端存根将它们统一序列化成二进制后，打包递交给传输层。

传输层使用TCP协议，所以RPC中，上层传递下来的二进制信息需要进一步封装在TCP包中，寻址后发送给相应的服务器。

可都封装好了，为什么要有寻址这一步骤呢？

简而言之，寻址的重要作用就是找到该函数对应的服务器地址。但是企业环境中，各服务分散在不同的服务器上，如果都由客户端来“记忆”，将导致巨大的资源浪费。为了方便查询分散的服务地址，RPC中会将所有服务和对应地址都集中在一起，这个集中了所有服务地址的机器就是注册中心。

通过注册中心，客户端和服务器可以更方便地交互。

对服务器来说，它每增加或注销一项服务就通知注册中心进行更改，而不必一一告知客户端。对客户端来说，它也不必记住每一项服务所在地址，也不用管服务地址是否有变化。只需要在申请服务时，从注册中心查找到服务地址，向该地址发送数据包就行了。也就是说服务端的变化对客户端几乎没有影响。

数据包传递到服务器后，先由传输层对其解析，得到序列化过的二进制包。

要把这个二进制包转化成服务器能理解的数据格式，就需要与序列化相对的反序列化。

通常在服务器上，同样拥有一个服务端存根，它和客户端存根的作用一样，用来管理RPC过程中的大部分事务，反序列化也由它来完成。

在这里，服务端存根对二进制包反序列化，得到参数和要调用的函数ID，然后递交给服务器。服务器计算后得到结果，返回给客户端。

RPC中，结果返回时，同样需要服务端存根来对其进行序列化后传输，客户端收到响应数据包后由客户端存根再次对其反序列化，得到结果。

这样，在RPC协议规范下，客户端就成功调用了服务端的函数来完成计算。

## 结语

相比于HTTP等传输协议，RPC将数据序列化成二进制，直接在传输层上与服务端交互，极大地提高了传输效率。并且使用存根来管理RPC的底层过程，让客户端和服务端的交互变得透明，从而为用户提供了方便。

不过，抛开传输效率的便利，RPC中同样也存在很多安全威胁，比如Zerologon(CVE-2020-1472)、Printnightmare(CVE-2021-34527)等，攻击者利用这些漏洞，可以直接通过RPC协议连接服务器，并向其发送恶意代码，从而获取控制目标服务器的权限，这也是使用协议时要提防的一个方向。

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
[中安网星版大模型来了！三大关键能力，不输专业红队攻击手](https://blog.csdn.net/ZAWX_NETSTARSEC/article/details...