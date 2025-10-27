---
title: G.O.S.S.I.P 阅读推荐 2024-05-08 不要追踪！
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247497948&idx=1&sn=c6e443f8217e6b7f8d01bf7e07a494a4&chksm=c063d605f7145f13b7efebc7da6922907123953c43f9e7316d972a685aba58825b2ed28571c4&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-05-09
fetch_date: 2025-10-06T17:17:01.048493
---

# G.O.S.S.I.P 阅读推荐 2024-05-08 不要追踪！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FJckWb3DZxqeOBHrAjBubz9ntoibo496kf4Cjs9cKzOMAhga5ianp9OM3NRc4nNO5JmfiaVnBw4Yp4g/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-05-08 不要追踪！

原创

G.O.S.S.I.P

安全研究GoSSIP

Android和iOS系统从诞生至今，早期方方面面的安全漏洞基本都修复得差不多了，安全特性也不断加强，所以最近这几年的趋势是如何保护用户隐私，毕竟数据是可以当成真金白银来交易的，先必须要看护好。今天我们主推的论文*Exploring Covert Third-party Identiﬁers through External Storage in the Android New Era*来自USENIX Security 2024，讨论了在Android系统上一些三方SDK开发的用户身份认证功能（identifer）的问题；无独有偶，在今年的同一会议上还有另一篇讨论iOS系统上同类问题的论文*ATTention Please! An Investigation of the App Tracking Transparency Permission*，我们也一起推荐了~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubz3u1ynjryK8fZiaSu6CF2PfwhiaJtsHNAsQVmEsuPEf60Oick8KfEXMIFw/640?wx_fmt=png&from=appmsg)

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubziaDPMZobdlUQH3vW70qCst2ibYicFUYajk8ehYuzmZgxVgjwyt0nKIicLg/640?wx_fmt=png&from=appmsg)

在第一篇论文中，作者主要研究了Android APP中常见的第三方SDK自己开发的identifer记录功能，由于从2019年发布的Android 10（API level 29）开始，访问硬件相关的identifer需要显式的权限申请，用户完全可以拒绝这种行为，所以很多第三方SDK必须要在夹缝中求生存，所以它们就搞了很多自己的套路，比如下图中的这家A字开头的SDK，它首先去尝试各种传统的获取硬件identifer的方法，如果不行，就再试试——换成一套自己生成特定的信息并且存储在SDCard分区的方法：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubzJGWtkLicIKiaGicssClI9TEctfNjJdkptD8AD8p7Hmy3JafvLCB3ian6VA/640?wx_fmt=png&from=appmsg)

在这篇论文中，作者关注的是这种自定义生成并存储identifer的方法的安全性：包括这些identifer是否机密（有没有可能被别家APP盗取了），是否防篡改（被修改了是否能识别出来）；同时也关注了这种方法的健壮性：是否能生成独一无二的identifer且在特定设备上保持稳定？

实际上要问答上述的问题也不难，作者在论文中使用的研究方法示意图，大家一看就能明白，首先肯定是动态监控APP和系统的所有交互行为（通过对系统进行instrumentation），然后进行启发式地分析，找到可能的identifer生成的行为，最后进行人工分析：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubzGFbFPvVPqNyPY76iazgHkwsW2ibdrIVxrZx3BRGALJNymEqZ6EDmbrsA/640?wx_fmt=png&from=appmsg)

这篇论文的精华当然是在分析结论中，作者首先对8000个APP进行了大规模分析，发现了3230个存在自己生成identifer行为的app（其中国内app市场是重灾区，Google Play好很多）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubzeh6M3oqibkHNZKzibl8c19lgicZa4OfnU87uTy53AhpCeH7kHibqE5Z2dg/640?wx_fmt=png&from=appmsg)

实际上，虽然分析发现了3000多个APP中自己生成identifer的行为，但是也就涉及了17家SDK，关于这些SDK生成identifer的技术的总结如下表：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubztEFYE5ibxWtiahZUjcxeiajn5uYyRCTNgMGTViaUzfia0xg2QlR89cIr55w/640?wx_fmt=png&from=appmsg)

对这些identifer的安全性进行分析后，作者发现很多SDK并没有严格检查identifer是否会被别的APP篡改（缺乏数据完整性保护），甚至也没有考虑到会被别人读取的风险（缺乏机密性保护），但是identifer在不同APP间进行分享也许正是SDK的设计特性？？？

---

简单讲完了第一篇论文，刚好可以马上去接着读第二篇论文，看看iOS上的情况，实际上iOS用户肯定很早就发现了这个“Ask App Not to Track”的提示吧？Apple作为最重视用户隐私（广告法警告）的公司，设定了这种要求APP不跟踪用户的开关，具体来说就是要求APP在iOS上只能用系统提供的一个Advertised item ID来作为标识用户特定设备的记号，但是如果用户不允许你使用，你就不能用。

> https://developer.apple.com/app-store/ad-attribution/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubzlagNiaD6h1nm7vyO9ZKPsYlLPJPyK2CyU87aVcRLKHyGDGiap9CUFahw/640?wx_fmt=png&from=appmsg)

作者观察到，很多APP在“诱骗”用户去允许访问Advertised item ID上有一套手法，首先会先弹出来一些“坑蒙拐骗”的提示窗口给你动之以情晓之以理，然后就是系统弹框——也就是论文中定义的ATT alert——请用户选择。在读这篇论文之前，编辑本来都不知道还有这种套路，以为这个弹框完全是一样的，反正从来不看，直接就是拒绝，现在才知道原来在这个弹框里面还有一些文字（上图红框框）是可以由开发者自定义的，开发者可以想办法在这里请求审稿人用户高抬贵手。论文中还收集了挺多不同的案例（如下图所示）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubzvHKGRQvLrMT69bSay5z5qmBia2SlKIibibuiak5Wwb6VKibnDrBlprhAfYg/640?wx_fmt=png&from=appmsg)

关键是，很多APP为了防止像编辑这种不看文字的文盲用户直接拒绝，还会在弹框之前弄一些花里胡哨的提示，作者也收集了挺多的案例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubzj2cTArXRlIXFuLRibhYsH12tibzS970cDftYRiatN7PbqLkwibiaTp2WPXA/640?wx_fmt=png&from=appmsg)

为了调查这些不同的情况，作者搞了一套分析流程，先是静态收集了IPA（未砸壳，但是可以提取其中的metadata），分析里面`Info.plist`和ATT alert相关的信息，如果IPA涉及到ATT alert，那么再砸壳分析。作者表示他们只有iPhone 6，系统和越狱都没法搞定iOS高版本，所以只能对那些兼容低版本的IPA进行分析（美区AppStore上的IPA会心一笑：安全了）。下面给出了分析流程示意图和APP数据集的总结：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubzR5UxmXd9jFnAWmf3lodJFxX4PAiblibJZrpicnbUDvf1kL7YYX83X18iaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubzatBBAtxX8WodY9KoHyZsmPCFQCQHJrJpzt8ysDxX1sNK47nSFe3ibVA/640?wx_fmt=png&from=appmsg)

作者把调查的IPA分成了random selected组和popular app组，然后进行了分析总结，发现其中有7%的APP确实是有那种弹框之前花里胡哨的提示；在所有的APP中，有超过50%的比例会用模棱两可（ambiguous）、欺诈性（misleading）或者激励性（incentive）的提示文字来想办法说服用户允许Advertised item ID的使用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubz8j1zgD7gdg3svKoIQ7V5ZDl3XZmrS1zBkiaERjVnZN7ibH2cKWNxebyg/640?wx_fmt=png&from=appmsg)

作者也详细标记了各种提示文字情况：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubz8wDGfd7x6uz6zENEvx6OECEBnecBed2xcgOREwByWDo75WpjSC7ruA/640?wx_fmt=png&from=appmsg)

---

读完这两篇文章，你有什么感觉？是不是觉得APP开发者很辛苦，想尽办法要追踪用户，我们用户是不是也要考虑下李彦宏李总的呼吁呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FJckWb3DZxqeOBHrAjBubzic2nA8t7Wxd9NicSmPicl7PEEA8qkDEnAVRIxqmWM0BXRtAn9NcN5JBjw/640?wx_fmt=png&from=appmsg)

---

> 论文（Android）：https://www.usenix.org/conference/usenixsecurity24/presentation/dong-zikan
> 论文（iOS）：https://www.usenix.org/conference/usenixsecurity24/presentation/mohamed

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过