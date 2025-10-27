---
title: 干货 | 实战中通过AccessKey与AccessSecret接管文件存储服务的攻击场景
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495384&idx=1&sn=f272c5c121e091f15cbf883a3b36c981&chksm=e8a5e4bbdfd26dad46c9460a66001be4a54b9b27380a98939f3f0b84c6781f2fba0e60f7f0e0&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-07-30
fetch_date: 2025-10-06T17:45:48.294543
---

# 干货 | 实战中通过AccessKey与AccessSecret接管文件存储服务的攻击场景

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6ibQXDiaYVaCqFCxBp8pxeH7dwPRMyibW5uggCbg6ACJWewa1SRDt5qoC0BziblpfQ3a4RJ1ibW674HdQ/0?wx_fmt=jpeg)

# 干货 | 实战中通过AccessKey与AccessSecret接管文件存储服务的攻击场景

迪哥讲事

以下文章来源于HACK学习呀
，作者L@2uR1te

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM40Ey25ia7icKDtM0hyhYQeTnJdaC9NzZRHPkFM71EAD3Fw/0)

**HACK学习呀**
.

HACK学习，专注于互联网安全与黑客精神；渗透测试，社会工程学，Python黑客编程，资源分享，Web渗透培训，电脑技巧，渗透技巧等，为广大网络安全爱好者一个交流分享学习的平台！

**0X00    前言**

互联网的时代正在高速发展。在互联网的发展中，数据存储技术的各种应用方式也在经历不断地变换。在如今，OSS对象储存已经成为一种被广泛采用的存储模式，很多企业都习惯将大量的数据都通过云储存的形式为商户实现便捷服务。

所谓对象存储OSS，是在云上提供无层次结构的分布式存储产品，为用户提供单价较低且快速可靠的数据存储方案。用户可通过云服务器实例或互联网使用Web API接口存储和检索数据。在OSS上的数据，用户使用指定域名的URL地址，通过HTTP/HTTPS协议存储和检索每个独立的数据对象内容。简单理解，类似AI停车。我们（前端应用）把车停进去，换来一张卡片（对象的标识符）。我们不用关心车（数据）具体停在车库（存储）的哪个车位，这样省事儿、省时间。

使用OSS进行文件的存储是有非常多的好处的，它可拓展性高、效率高、安全性高、成本低、访问方便。

如今主流的公有云厂商有这些：亚马逊（AWS S3），腾讯云（COS），阿里云（OSS），华为云（OBS），百度云（BOS）,网易（NOS），快快云（OSS）。虽然各厂商的产品还是有些区别的，但是在利用方式上仍然大同小异

**0X01    实战利用**

**AccessKey ID与AccessKey Secret之于OSS服务的重要性**

关于OSS存储的诸多技术细节不再赘述，我们只关心在实战中如何针对各类OSS服务进行攻击，针对OSS的攻击，绕不开的一点就是AccessKey ID与AccessKey Secret的获取（各大厂商对其的命名略有不同，但它们的功能是类似的）。下面通过阿里云和AWS两家厂商对AccessKey ID（下文简称AK）、AccessKey Secret（下文简称AS）的描述来简要介绍其功能。

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBiaJYSW2lGTrwRRa7JNjh9hHEUyZsjWCmdicdyicYKEVUskMwkn8XlO3lg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBn8ZFSUDasbuYfBqHwehTlyvQMLCQA71R2zkaAWcUWH3o5tfsru3ibNg/640?wx_fmt=png)

简单来说，AK与AS就是一种调用服务API的凭据，可以简单理解为在这种特殊场景下的“账号”与“密码”，我们想要使用OSS的各种功能，也是无法离开AK与AS的。换句话说，如果攻击者设法找到了AK与AS，是否意味着对OSS云存储服务的直接接管呢？

**0X02    实战场景中AK与AS的寻找方法**

在实战中要如何寻找AS与AK是我们要面临的重要问题，笔者以对某厂商的一次测试为例，抛出第一种寻找方法——敏感文件的泄露。这里的敏感文件是广义的，可以是各种内存的泄露、可以是某些数据库里存储的信息、甚至可以是运维人员图方便而写的一些备忘文本。本案例是通过找到Spring泄露的heapdump文件进行分析的。

通过一款heapdump自动化分析工具，我们可以方便快捷的分析heapdump中泄露的各种敏感信息，如下图，工具找到了泄露的AK与AS

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBxxTOvBkWl5BMYB048ibnTyD64WY3porP3cpt3LGyRLH3W1ibAwhcrdOw/640?wx_fmt=png)

于是我们通过该AK与AS，成功接管了该OSS服务，并且找到了海量的数据（进一步说明，对于这种文件存储服务，只要被攻击者接管，所泄露的数据量将会是巨大的）

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBQZt7wSxkpRIdofrsdt8ic28iaF3H24XCjuZB3GS4JONNaSoKpjTJezyQ/640?wx_fmt=png)

值得注意的是，某些情况下phpinfo等探针文件也会抛出AS与AK（如下图），攻击队在找到探针类文件后，可以尝试搜寻AccessKEY、AK、OSS、SECRET等字样来分析是否存在AK与AS的泄露

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBlgicHj0dolAfJnkiaryhiau7G0qy9T82mYo1cnz6Rk8iaxqQ1HIe2iaZ99A/640?wx_fmt=png)

还有一种比较偏门的地方是通过各种报错进行泄露，比较可能的情况有ThinkPHP的Debug模式，以及其他的一些因配置不当报错而泄露AK与AS

类似下图这种就是比较典型的报错泄露：

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBuC8vhVc5D5Fibyso5GjDmsZda4kibzqtfd7CJeYp8eicjMwKicOHMX6wHg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBOcvwT7qBibCccoJo1uh78ia4CH31ZY1VMCfxQb3toy51hp7TFpic6icYiag/640?wx_fmt=png)

如图，直接抛出了AWS的AK与AS。但是通过报错来寻找AK与AS在实战中具有相当大的不可控性，属于是可遇不可求的一种发现方法

实战中还有一种可能性较大的寻找方法就是从github等开源平台入手（适用于体量较大的目标），有些开发者可能关注到员工账密、员工个人信息等敏感信息的脱敏，但是忘记了对AK与AS进行脱敏，在通过github查询目标的各种信息时，要留意一下有没有泄露AK与AS。如下图，就是从github上发现了相关信息

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EB52mZSvOJ1o6su39GdHWD8v5dBI7jkOuRhBmTSCobbtDlsiaLzrGWOicA/640?wx_fmt=png)

我们最后介绍一种实战中容易碰见的，并且也是危害性最大的——在JS文件甚至是文件上传数据包中发现AK与AS。在介绍这种情况之前，可以简单的了解一下文件上传到OSS服务器过程中的三种经典验证方式。

```
①  在客户端通过JavaScript代码完成签名，然后通过表单直传数据到OSS。②  在服务端完成签名，然后通过表单直传数据到OSS。③  在服务端完成签名，并且服务端设置了上传后回调，然后通过表单直传数据到OSS。OSS回调完成后，再将应用服务器响应结果返回给客户端。
```

当我们在文件上传处看到下图类似的字样时，基本可以判断这是使用OSS进行文件存储（还有一个常见特征是OSS文件存储分多步进行，一个文件上传操作会产生好几个数据包，普通的文件上传操作基本只用一个数据包即可完成）。当看到这个特征时，攻击者要马上反应过来——到JS文件中尝试寻找AK与AS

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBUFnKgUe4CZfCjasdy8Gk7UvkWia0YwfyCV8of3n3Nan171ictgn8cp2Q/640?wx_fmt=png)

为什么呢？我们不难看出，上文提到的第一种方式是非常危险的。因为AK与AS写死在前端文件了，这意味着我们只需要花点时间就可以找到他。如下图就是在JS文件中分析出的明文AK与AS。攻击者也可以自己动手，开发工具来尝试读取JS中的这类关键词从而节省人工寻找的时间！

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBRbMEa7e9cLvunVBiaOgjS584TibGSeiaT8df43Q6wPRyyIYVUR2D3uasQ/640?wx_fmt=png)

还有一些粗心的开发人员甚至直接在数据包中明文传递AK与AS，这无疑是为攻击者提供了便利，注意OSS上传数据包中传递的这些数据，它们也很有可能是明文的AK与AS！

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBHNBKFljM93ajF6Wp261IuB7jCZsUxKic85vIicyNic0LBOdk3icfZiaC7ZQ/640?wx_fmt=png)

**0X03    如何利用AK与AS**

上文总结了常见的AK与AS泄露情况，那么攻击方人员如果拿到了AK与AS，应该如何去利用？其实获得这两个信息之后允许攻击者做出非常多危险的操作。上至命令执行，下至文件泄露，本文也着重介绍一下这两种攻击手法。

Github上有相当多的AK与AS利用工具，基本上覆盖了所有主流的云厂商，足够满足我们正常攻击中的各种需求，本文就以阿里云AK与AS泄露来演示其利用。使用下图的这款工具

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBAcvp736xHZhaicS6QtKQ0S2N3ET0gSFiabPvvvgda1cI81I9djMTPiaQg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EB24lh2pkKxHKjechSJeHeH7ibVCXbKicwic1YP5hV6meuhz06AURvE99lA/640?wx_fmt=png)

可以以root权限执行任意命令，在这种情况下等于直接拿下目标服务器的权限。据了解AWS提供的OSS服务一旦泄露AK与AS，也可以造成类似的命令执行问题，笔者未对其它主流厂商提供的服务进行了解与实践，各攻击队可以自行研究尝试。

以上便是AK与AS最具威胁性的一种利用方式。下面介绍一种威胁性稍小的，就是任意文件的上传下载。上文提到了笔者使用AK与AS进入了OSS服务并且完成了任意文件的上传下载。这其中我们借助的就是这个MinIO Browser，攻击队如果在资产搜集的过程中遇到了类似的、使用AK与AS进行验证的资产，应该也可以使用类似的方式登陆进去并对其接管。

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBQZt7wSxkpRIdofrsdt8ic28iaF3H24XCjuZB3GS4JONNaSoKpjTJezyQ/640?wx_fmt=png)

当然，通过OSS Browser、行云管家之类的现成的工具，攻击者也可以方便快捷的对OSS服务进行接管

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBSQGt6ckeobibT8LL8Za8EkH7MMd3bLicdXrDVzvKicNZ4kg1N43tOnrBg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibfYn2AO9XC17gbH1IKQ4EBJdEZXnOZmEgcvHwCj71hiaI0HV1ufHK5XtLnkcv4cP7cd0gUSph57LQ/640?wx_fmt=png)

**0X04    攻击层面上的一些小思考**

上文主要介绍了两种对OSS的攻击方式，但是在利用方法上，还是能衍生出非常多有意思的点的。比方说命令执行来说，既然我们可以用root方式进行命令执行，那么我们拿下一台低权限机器的时候，是否可以通过寻找AK与AS实现提权？再比如说任意文件上传下载，虽然OSS服务上的文件不支持解析，但是我们是否可以通过替换一些文件（比方说目标网站支持下载文件之类的功能），从而实现投毒？在利用层面上，OSS服务也可以衍生出许多“异想天开”的攻击方法，值得攻击者深入思考！

**0X05    结语**

随着中国互联网的不断进步，OSS存储服务这类相较于传统上传方式有大量优点的云存储模式毫无疑问会逐渐成为主流，这是互联网发展的大势所趋。因此在往后的攻防演练、渗透测试中，攻击者会遇到越来越多的OSS服务以及相关的云服务，深入研究分析其攻防技术是必不可少的，本文以实战中遇到的案例为引，简单总结了实战中关于OSS服务攻击的一些常见情况，希望能起抛砖引玉之效用！

**![](https://mmbiz.qpic.cn/mmbiz_png/ndicuTO22p6ibN1yF91ZicoggaJJZX3vQ77Vhx81O5GRyfuQoBRjpaUyLOErsSo8PwNYlT1XzZ6fbwQuXBRKf4j3Q/640?wx_fmt=png)**

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，...