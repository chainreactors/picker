---
title: Windows App 运行控制机制 Smart App Control 的内部安全架构分析（下）
url: https://www.4hou.com/posts/GKrQ
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-29
fetch_date: 2025-10-03T23:56:33.112844
---

# Windows App 运行控制机制 Smart App Control 的内部安全架构分析（下）

Windows App 运行控制机制 Smart App Control 的内部安全架构分析（下） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Windows App 运行控制机制 Smart App Control 的内部安全架构分析（下）

luochicun
[技术](https://www.4hou.com/category/technology)
2022-11-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)121724

收藏

导语：从好的方面来看，这篇文章的绝大多数可以推断出其他WDAC策略是如何评估的。

下面的伪代码或多或少地展示了SmartLocker非继承属性的最后一部分是如何工作的。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653645238321.png "1665653645238321.png")

注意: 根据稍后如何使用此函数中的值来填充TraceLogging字符串，我们知道防御措施将评估过程的所有这一部分视为: Is防御措施Shell。

这或多或少就是我们通过在调用之后立即双击从资源管理器启动的进程所需要的：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653655169766.png "1665653655169766.png")

CipCheckSmartlockerEAandProcessToken的情况就这样了，现在再说说CipExternalAuthorizationCallback。

现在，让我们说说Intelligent Security Graph所使用的代码段，它现在已被扩展以添加一些SAC功能。首先，将再次检查策略选项Intelligent Security Graph Authorization（智能安全图授权），如果未设置，函数将使用从CipCheckSmartlockerEAandProcessToken获取的值退出。如果该值在策略中处于活动状态（SAC策略就是这种情况），该函数将使用前面讨论的IsTrustedSigning来确定它是否应该继续。如果映像可信，将执行以下检查：

如果ValidatedSigningLevel等于“由使用AMPPL(7)的产品的AV签名”，并且策略的值为VerifiedAndReputableAllowAntiMalware，则分数将用值AllowAnti Malware（0x100000）进行异或运算，函数将返回。

如果映像不可信，则函数将继续查询防御措施。如上所述，向防御措施发出查询的函数是CiCatDbSmartlockerDefenderCheck。此函数将接收两个MPFILE\_TRUST\_EXTRA\_INFO结构，一个填充请求数据，另一个接收回复数据。代码还将从FileObject传递FileName。MPFILE\_TRUST\_EXTRA\_INFO结构如下所示。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653665645359.png "1665653665645359.png")

双方之间的通信是使用RPC实现的，CI.dll将实现客户端，服务器将在cryptcatsvc.dll中实现。为了记录，RPC存根的IID是f50aac00-c7f3-428e-a022a6b71bfb9d43。

cryptcatsvc在服务CryptSvc中运行。在用于RPC服务器的发送函数中，我们重点关注以下函数：

```
s_SSCatDBSmartlockerDefenderCheck (Already present in 22H1)；s_SSCatDBSmartlockerDefenderCheck2 (New to 22H2)；s_SSCatDBSendSmartAppControlBlockToast；s_SSCatDBSendSmartAppControlSwitchEnforceToast；
```

SmartLockerDefenderCheck函数的v1和v2之间的最大区别在于，在v2中，该函数接受请求和回复MPFILE\_TRUST\_EXTRA\_INFO作为其参数的一部分。这两个函数最终都调用了助手函数CatDBSmartlockerDefenderCheckHelper。

CI将从这些函数调用s\_SSCatDBSmartlockerDefenderCheck2，它将首先加载MpClient.dll。

注意：在第一次执行时，将在防御措施配置中启用SmartLocker。该函数将调用MpClient导出的函数MpSmartLockerEnable。此函数只需注册Defender ELAM证书信息（打开Wdboot.sys的句柄并调用InstallELAMCertificateInfo），然后使用RPC从MpSvc.dll调用方法ServerMpEnableSmartLocker，它将检查防御措施配置中是否设置了SmartLockerMode，如果没有，它将写入。

打开库的句柄后，该函数将使用CI.dll提供的文件名来打开一个文件句柄，该句柄将被传递给MpClient导出的函数MpQueryFileTrustByHandle2，该函数只在来自于DefenderCheck2时被调用，如果是旧版本的DefenderCheck，则将调用MpQueryFileTrustByHandle。

在MpQueryFileTrustByHandle2内部，代码将使用该文件的句柄来创建文件映射，该文件映射将被防御程序用于对其进行内存扫描。下面的InSequence函数将通过从MpClient(客户端)到MpSvc(服务器)发出RPC调用来执行。显然，我们刚才看到的所有函数调用都接受CI.dll设置的MPFILE\_TRUST\_EXTRA\_INFO作为参数的一部分。

ServerMpRpcMemoryScanStart：设置CMpMemScanContext和CMpMemScanEngineVfz（使用GetAttributeTrustCheck作为GetAttributions函数），并进行异步扫描；

ServerMpRpcMemoryScanQueryNotification：检索扫描信息；

ServerMpRpcMemoryScanClose：关闭并清除CMpMemScanContext。

这些函数的内部结构不在本文所讲的范围，我想强调的是，当启用SAC时，防御措施将主动扫描文件并进行云查询。

从扫描检索到的信息中有三个可能的信号：

0x31001：检索到的MPTRUST\_INFO（IGS）；

0x31002：检索到的MPFILE\_TRUST\_EXTRA\_INFO（SAC）；

0x4005：与RSIG\_VIRINFO相关；

最后完成防御措施通信，下图显示了代码到达防御措施时客户端（CI）和服务器（cryptcatsvc）堆栈。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653677759981.png "1665653677759981.png")

需要注意的是，如果我们的SAC处于强制状态，并且设备中没有互联网连接，则默认操作是阻止该进程，并且将显示一条通知，提示“智能应用程序控制无法验证此应用程序，请检查您的互联网连接，然后重试”。

返回外部授权回调，如果RPC调用失败，则未设置策略设置VerifiedAndReputableAllowUnknown，并且ValidateSigningLevel不是以下任何一项：

```
Microsoft Store signed app PPL (Protected Process Light)Microsoft Store-signedMicrosoft signedWindows signedOnly used for signing of the .NET NGEN compilerWindows Trusted Computing Base signed
```

然后将验证分数与值Unattainable（0x40000）进行异或运算，函数将返回。如果RPC调用成功，则将调用函数CiHandleDefenderSignals。顾名思义，此函数将处理防御措施发送回的消息。它将遍历返回的元素数，其中每个元素的类型为MPFILE\_TRUST\_EXTRA\_INFO。根据ReplyType字段，它将执行不同的操作。更有趣的两种情况是：首先，当返回信任结果时。在该示例中，信息将指向MP\_INFO\_RESULT，其中的值将复制到验证上下文：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653691412788.png "1665653691412788.png")

第二个有趣的示例是信息指向MP\_NW\_CONTROL枚举。在该示例中，根据控制命令，该功能将被禁用或切换到强制模式。这基本上将更新VerifiedAndReputablePolicyState RegKey，并更新WorkItem中的策略。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653703107714.png "1665653703107714.png")

在我们从学习模式更改为强制模式的情况下，将发出对函数s\_SSCatDBSendSmartAppControlSwitchEnforceToast的RPC调用。在此函数中，DLL wldap . DLL将被加载，然后调用函数WldpSendSmartAppControlSwitchEnforceToast。

从信号处理程序回来后，有一些细微差别。如果NW控制命令设置了标志IsUnfriendlyFile，则Score将更新为值UnfriendalyFile（0x80000），函数将返回。如果未设置标志，则TrustInfo和FileObject将被传递到带有标志0x82的函数CipSetFileCache中，这意味着EA $Kernel.Purge.CIpCache将用于存储此信息。

最后，需要根据防御程序返回的信任调整分数，有5个选项：

Trust == 1：分数将使用值0x202进行异或运算，不过我对这个值不太了解；

Trust == -1 (0xFFFFFFFF)：如果策略设置VerifiedAndReputableAllowUnknown被设置，则分数将使用值AllowUnderknown（0x20000）进行异或运算；

Trust == -2 (0xFFFFFFFE)：分数将使用值Malicious (0x80)进行异或运算；

Trust == -3 (0xFFFFFFFD)：分数将用PUA（0x100）值进行异或运算；

任何其他情况下，分数将用值0x42进行异或运算。

这几乎就是外部授权回调的全部内容，现在我们回到调用外部授权回调时的SIPolicyValidateImageInternal！

**SIPolicyValidateImageInternal**

在进入外部授权回调之前，我们将讨论SIPolicyObjectValidationEngine函数如何遍历策略并调用内部SIPolicy ValidateImageInternal，后者稍后将调用外部auth回调。现在，调用回调后，我们返回到SIPolicyValidateImageInternal，并返回验证分数。如果启用了SAC，则该函数将继续评估分数，并将此分数传播到验证引擎分数，并根据该得分设置相应的NTSTATUS。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653714194674.png "1665653714194674.png")

如上图所示，在大多数分支中，它会将相应的NTSTATUS设置为验证状态，然后跳转到我所称为ProcessDbgAndReprieve的状态。这只不过是一种检查内核调试器是否附加到调试器控制台中以记录策略冲突的方法。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653726188089.png "1665653726188089.png")

如果未遵循前一个映像中的任何分支，或者分数为Unattainable但设置了AllowUnknown，则函数将继续根据策略规范评估对象。首先检查文件规范，这将在函数SIPolicyMatchFileRules内完成。此函数将接收以下参数：

具有要评估的文件规范的策略；

```
OriginalFileName；InternalName；FileDescription；ProductName；
```

我强烈建议阅读MSDN的“理解Windows防御应用程序控制(WDAC)策略规范和文件规范”一节，以了解更多关于策略规范和可用于它们的不同选项的内容。

与我们在第1部分中看到的Policy Secure Settings类似，该函数将使用作为key传递到函数bsearch的数据建立一个结构。关键结构具有以下原型：

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653736134262.png "1665653736134262.png")

bsearch函数的base和num将取自SI\_POLICY结构。将策略解析为SI\_policy结构时，将设置一个包含两个场景的数组。每个场景都包含其特定的文件规范、允许的签名者、拒绝的签名者和异常规范。如上所述，当调用SIPolicyMatchFileRules时，要评估的场景的特定数量被传递给函数。此数字将用作函数的索引，以了解要选取Scenarios数组的哪个元素。每个场景都由以下结构表示：

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653747150899.png "1665653747150899.png")

如果没有FileName级别的文件规范匹配，则函数将继续计算哈希级别的文件规范：

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221013/1665653756684041.png "1665653756684041.png")

如果FileName或Hash匹配，则SIPolicyMatchFileRules返回TRUE，验证状态将设置为status\_SYSTEM\_INTEGRITY\_POLICY\_VIOLATION。

如果对SAC策略使用的哈希和文件名感兴趣，可以查看策略的FileRule标签下的整个列表。

如果没有匹配...