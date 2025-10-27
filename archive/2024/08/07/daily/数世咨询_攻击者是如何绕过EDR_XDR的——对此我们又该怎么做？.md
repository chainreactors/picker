---
title: 攻击者是如何绕过EDR/XDR的——对此我们又该怎么做？
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514543&idx=1&sn=df41f535123e65c513418ac284ac6809&chksm=c144cb12f6334204bac644721de05271f54920c005bda8a829ba413c9dd51556ce5d83927aab&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-08-07
fetch_date: 2025-10-06T18:04:27.632404
---

# 攻击者是如何绕过EDR/XDR的——对此我们又该怎么做？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqr7kEmTnRCxYPVEJfQnUtyHJ9us56siaI76IoD9eL85juMmibTZgXym3EwoHUD2Xiagpy7Bpcnz8yGyw/0?wx_fmt=jpeg)

# 攻击者是如何绕过EDR/XDR的——对此我们又该怎么做？

原创

晨雨

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqr7kEmTnRCxYPVEJfQnUtyHyXDgEelrUZ0wBicApXjj0onrFA6g7VjtquJtFUm7Q2ekh33wcqS3Mibw/640?wx_fmt=jpeg&from=appmsg)

最近的一项全球分析指出，**CISO及其组织可能过于依赖终端检测和响应（EDR）和扩展检测和响应（XDR）系统，因为攻击者绕过这些系统的成功率正越来越高。**

一定程度上，**绕过EDR/XDR系统一直是并将继续是大多数现代攻击者的基本要求。****“被绕过”这一说法通常指防护/检测系统未发现任何异常。**从技术角度来说，这一说法是准确的，但细节描述的缺乏阻碍了网络安全专业人员进一步采取更为准确的补救措施。例如，检测逻辑错误与XDR平台控制的agent失效，这两个问题是完全不一样的。

更重要的是，问题发生后该怎么办，为了更好地了解攻击者如何绕过EDR/XDR系统，需要了解它发生的三个领域：

**• 监测
• 检测
• 响应和预防**

**01**

**攻击者如何绕过XDR的“监测”**

XDR系统的核心是处置来自于终端操作系统或云服务提供商等各种来源的安全事件。这些事件——通常由agent监测发现——构成了检测的基础。XDR只能检测系统可以发现和收集的内容。**第一种类型的绕过就发生在XDR没有接收到检测恶意行为所需的事件时。**

这种类型的绕过有几个常见的原因。首先 “最纯粹”的技术绕过，是攻击者的行为没有产生相关的监测数据。操作系统中发生的每一个行为都会产生一定数量的监测数据，但是这些事件可能对有效的检测没有帮助。换句话说，可以把这看做系统中缺失了某些事件源，而非XDR自身的缺陷。

**第二种情况，操作系统中产生了一些监测数据，但XDR并未有效采纳。**一般来说，可供XDR订阅的事件来源有数千个，XDR供应商的工作是决定其中哪些事件源满足他们的检测需求。例如，如果某个XDR供应商对Active Directory活动目录相关的行为特别感兴趣，他们会优先从AD收集事件，而非流量。不收集某些类型的事件，无论是出于选择还是无知，都会导致XDR在某些技术领域的覆盖范围内出现可被攻击者利用的空隙。

**最后一种情况，攻击者可能会主动干扰XDR的agent**，这样事件就不会被发送汇总到负责收集和关联的服务器。攻击者的干扰有多种形式，包括停止或卸载agent、阻止agent与服务器的通信（例如通过修改主机防火墙配置）或篡改传感器（例如禁用AMSI）。

总的来说，**上述三种情况都代表了XDR供应商的失败。**如果因为agnet没有收集到相关监测数据而遗漏了攻击，供应商是唯一可以通过添加新的数据源或扩展丰富现有数据源的行为主体；在agent被干扰的情况中，除了必要的agent防篡改措施外，供应商还应当能检测出攻击者对agent的这些干扰行为。这些问题对每个甲方安全团队来说都是最难解决的，因此除了求助于他们的XDR供应商，他们实际上无能为力。

**02**

**攻击者如何绕过XDR的“检测”**

当大多数人谈到XDR绕过时，他们几乎总是指绕过XDR中的检测逻辑。**检测本身只是评估一个事件或一组事件的方法，以确定是否存在某种可能表明恶意行为的条件。**这些检测规则可以是精确的，这意味着它们针对的是恶意软件或攻击工具独有的特定属性（如Mimikatz的命令行参数特征）；这些检测规则也可以是鲁棒的（原文为robust，译者注），这意味着它们针对的是多个恶意软件样本或工具共性的行为。

这两种类型的检测都有其缺陷。**精确的检测容易被绕过，因为它们通常过于具体，这意味着对目标样本的任何修改都会导致漏报。**这方面的一个例子是攻击者修改Mimikatz的参数字符串，即只需将“sekurlsa::logonpasswords”改为“::happening\_here”，就破坏了针对攻击者控制字符串的脆弱的检测逻辑。

**鲁棒的检测尽管表面上看起来不太容易被绕过，但却因其误报而臭名昭著，这会导致规则中的排除被攻击者利用。**一个真实例子是，XDR将Chrome更新进程“GoogleUpdate. exe”加白，排除在凭据转储检测之外，因为它的正常操作涉及打开LSASS进程的特权句柄。尽管XDR收集的事件中包括所有行为信息，但这种排除允许攻击者伪装成更新助手或注入到进程中，进而绕过检测提取凭据。

这些绕过利用了EDR内置检测中的逻辑问题，无论它们是由供应商提供还是由内部检测工程师编写。例如，对技术或程序的理解不完全、检测瓶颈、对业务环境的妥协以及较弱的agent进一步导致XDR检测逻辑的薄弱……这些问题在端点保护领域都很常见。

**解决这些问题的方法是缩小这些逻辑差距**，但不幸的是，这在现实环境中并不总是可能的。有时必须接受一定程度的脆弱性才能快速检测到新出现的威胁，但是**精确检测应该与鲁棒检测配合进行，以弥补不可避免地漏报。**

强大的检测几乎总是需要一定程度的降噪，以避免告警淹没安全团队，但这些降噪应该尽可能受到限制，并不断评估以确定它们是否需要继续保留。实际上，检测工程是一个永无止境的调整和修补过程，目标是使检测尽可能具有弹性，同时将漏报和误报都保持在团队可以容忍的范围内。

**03**

**攻击者如何绕过XDR的“响应和预防”**

最后一种类型的绕过围绕在响应阶段中的某个错误上，当真正的告警出现时，这个错误可能会伴随出现。对告警的响应过程因组织而异，但通常都包括**确定优先级、分析和响应等三个阶段。**这些阶段的复杂过程包含许多不同的问题点。

在一个常见的安全运营流程中，**第一个发生绕过的机会是在确认优先级阶段**，即一级分析师收到告警并错误地将其标记为误报。这会导致尽管XDR完成了它的工作，但该行为却被忽视了。这种故障可能源于告警疲劳，导致单纯为了阻止告警队列的不正确降噪，或者源于对检测目标和信息含义缺乏理解。修复这个故障点通常涉及队列和疲劳管理，如通过减少误报（如上一节所述）以及更好地对分析师的文档与培训工作来实现。

接下来，在**正确的告警发出后是分析阶段。**主要内容是辅助信息收集，以进一步具体确定告警是否值得升级为全面事件。这一过程通常是手动的，需要熟练的分析师查询相关系统并提取支持信息，例如留在文件系统上的上下文信息。

这里有许多涉及分析人员与攻击者的技能对抗点。如果分析人员需要检查磁盘上的文件，但对手已经抢先删除了该文件，怎么办？如果需要内存取证，但对手已经重新启动了系统，怎么办？如果对手采用了分析人员不熟悉的技术，导致他们错过了攻击者留下的踪迹，怎么办？解决这些问题需要强大的支持文档，例如在对真正的有效告警产生怀疑的情况下应该收集什么信息，以及这些信息意味着什么。

最后，在**告警被确认为真正的有效告警，并定性为安全事件后，才来到真正的响应阶段。**主要内容为驱逐威胁参与者。在确定事件范围（涉及多少系统、用户等）后，安全团队有许多选项来清除攻击者，从简单地重新启动主机以清除内存驻留的恶意软件到烧毁整个环境等激烈措施。最终，成功在这里是二元的——对手是否被完全驱逐。

某只红队在这个阶段遇到过一次响应团队的“经典”错误，响应团队没有正确地确定事件范围，导致驱逐不完全，允许红队在他们的环境中存在了近18个月（只有当红队驻留的服务器被信息技术团队按照设备生命周期退役时，红队才最终被踢出）。**要改进响应能力，减少对手绕过的机会，还是要依赖于经受过验证的可靠响应流程，识别安全事件的整个范围的能力，以及确保完全消灭对手的能力。**

**04**

**文档**

用足够的颗粒度描述XDR绕过可以让人更好地识别整个流程中的哪个组件失效了，更重要的是，安全团队可以做些什么来修复它。总结一下，大多数绕过可以分为**监测**（XDR是否看到了恶意行为）、**检测**（XDR是否肯定地将其识别为恶意行为）与**响应**（该行为是否导致安全团队做出了充分的响应）。在下次遇到绕过时，希望上述内容可以帮助您做出相应的改进。

\* 本文为 **晨雨**编译，原文地址：https://www.csoonline.com/article/3476179/how-your-xdr-is-evaded.html
图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#数字安全交流群来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

😄 嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&token=340500352&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrXJOcAym9Txd8SXyYpsl5tMKKKZOkjKCyFF73OcERMobc16eBGprcrFxpXPqf7uBeueamyuxTI9w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514336&idx=1&sn=e69b1126e86ab2c59c8ca8e315637031&chksm=c144ca5df633434b94b06186e74fa9475521d0ffe272ebfd78f9123b1017b1e2fe548a47a1a6&token=85424237&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpM6fVpib3ficMmxPXTULy4YxbmwckZnudDYBnPvV3icV1ibdoMWpSS7QzE9g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514264&idx=1&sn=34960d59e3146dcce9f986129c3593c2&chksm=c144ca25f633433381c6bb3bc13fe3e8f2c15984de2aa8f072497dc07648f85c713aa1347ba1&token=340500352&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqr7kEmTnRCxYPVEJfQnUtyHhJ1febUo87hiaCicE3m8sYIzlnEcyUic8A60P2TToZbMMxCVDGm1lCQDg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247497252&idx=1&sn=ea2a356333528bcd50bb40f91c04a959&chksm=c1448499f6330d8f3863ac0b89679018102c531e98e724c1c8c1ba14fecb6e659b4bfca4fee2&token=529062578&lang=zh_CN&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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