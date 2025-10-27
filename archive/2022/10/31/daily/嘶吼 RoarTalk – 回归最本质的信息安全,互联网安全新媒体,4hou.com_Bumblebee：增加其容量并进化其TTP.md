---
title: Bumblebee：增加其容量并进化其TTP
url: https://www.4hou.com/posts/pVPr
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-31
fetch_date: 2025-10-03T21:20:40.299177
---

# Bumblebee：增加其容量并进化其TTP

Bumblebee：增加其容量并进化其TTP - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Bumblebee：增加其容量并进化其TTP

luochicun
[技术](https://www.4hou.com/category/technology)
2022-10-30 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)110077

收藏

导语：Bumblebee服务程序在6月前后发生的行为变化表明，攻击者可能已经将他们的重点从大规模监测恶意软件转向了攻击尽可能多的受害者。

年初，Bumblebee加载程序的活动激增，由于其与几个著名的恶意软件家族有关，因此引起了安全研究人员的注意。

Bumblebee一直在快速迭代，其加载系统在几天内经历了两次彻底的更新，首先是从使用ISO格式文件到包含powershell脚本的VHD格式文件，然后再恢复原貌。

Bumblebee服务程序在6月前后发生的行为变化表明，攻击者可能已经将他们的重点从大规模监测恶意软件转向了攻击尽可能多的受害者。

尽管该攻击包含一个名为group\_name的字段，但它可能不是一个与集群相关的活动的良好示例：具有不同group\_name值的示例显示了类似的行为，这可能表明同一个攻击者同时运营多个group\_name。加密密钥的情况并非如此：不同的加密密钥通常意味着不同的行为。

Bumblebee的有效负载因受害者类型而异。受感染的独立计算机可能会受到银行木马或信息窃取者的攻击，而组织网络可能会受到更先进的后期利用工具（如CobaltStrike）的攻击。

**技术分析**

Bumblebee加载程序通常以类似于DLL的二进制文件的形式出现，并使用自定义打包程序打包。此DLL的传播方法似乎会随着攻击者而异。目前最流行的方法是将打包的DLL直接嵌入另一个文件（通常是ISO）中，在6月份的一段短暂时间内，恶意软件的操作人员尝试使用VHD文件，执行PowerShell下载并解密打包的DLL本身（用一个非常不同的打包程序打包）。这种趋势似乎已经消失，现在可以再次在第一阶段文件中直接找到DLL，无论是ISO还是VHD。

一旦解压，Bumblebee将执行检查，以避免在沙箱或分析环境中执行，负责这项工作的大部分代码都是开源的，直接从Al-Khaser项目中提取出来。如果避开安全监测，Bumblebee将继续将其配置加载到内存中。这是通过从它的.data部分加载四个指向连续加密配置结构中的四个不同缓冲区的指针来实现的。第一个指向一个80字节的部分，它存储一个RC4 ascii密钥(在我们所观察到的所有示例中都要短得多)。其他三个指针指向两个80字节的部分和一个1024字节的部分，所有这些部分都包含随后使用上述RC4密钥解密的数据。

解密后，大多数示例中的第一个80字节缓冲区仅包含数字“444”，恶意软件没有使用这个数字，所以它的意义不清楚。第二个缓冲区包含一个被恶意软件标记为group\_name的ASCII码。最后，1024字节块包含一个命令和控制服务程序列表（其中大多数通常是假的）。

![1.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221004/1664857297149489.jpeg "1664857297149489.jpeg")

Bumblebee加密配置

Bumblebee通过连接一些不可变机程序参数(在本例中为机程序名和GUUID)的常用方法计算特定于机程序的伪随机受害者ID(内部命名为client\_id)，然后计算结果的哈希值(在本例中为MD5摘要)。

利用这些数据和从受害系统收集到的其他特点，Bumblebee以JSON格式构建了C&C签入，如下所示：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221004/1664857306181832.png "1664857306181832.png")

该字符串使用之前配置时使用的相同的RC4密钥加密，并以25秒到3分钟的随机延迟重复发送到其C2服务程序，而不管服务程序是响应还是关闭。来自命令和控制服务程序的响应也是JSON格式，也使用相同的RC4密钥加密。响应本身的内容自然是不同的，例如，可以是一个空响应:

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221004/1664857313127532.png "1664857313127532.png")

或者一些要注入或执行的负载：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221004/1664857321192090.png "1664857321192090.png")

在接收有效负载的示例中，响应的结构将包含json任务部分中的特点列表，每个特点都有一个命令和一个有效负载。每个特点都将包含一个任务字段，其中包含要执行的命令的名称，以及一个名为task\_data的部分中一个base64编码的有效负载。

**僵尸网络行为分析**

直到7月初，我们一直观察到命令和控制服务程序的一个非常奇怪的行为。一旦为受感染的受害者生成client\_id并将其发送到命令和控制服务程序，该命令和控制服务程序将停止接受来自同一受害者外部IP的其他不同的client\_id代码。这意味着，如果一个组织中使用同一公共IP访问internet的多台计算机受到感染，C2服务程序将只接受第一台受感染的计算机。但是几个星期前，这个功能突然被关闭，大大增加了与受感染受害者建立的连接的数量（可能表明该恶意软件的测试阶段已经结束）。

这种行为促使研究人员特别关注Bumblebee在不同执行环境中的行为。值得注意的是，尽管在每个示例中都硬编码了一个名为group\_name的字段，但在每个请求中都会将该值发送到命令和控制服务程序。此外，上述“每个IP地址一个client\_id”策略似乎适用于不同的group\_name，但不适用于不同的RC4加密密钥，这似乎意味着同一僵尸网络使用多个group\_name可能标记不同的活动或不同的受害者集。因此，与按group\_name分组相比，按加密密钥分组活动似乎是一种更前后一致的方法。

研究人员观察到几个具有相同RC4密钥和不同group\_name的示例在非常接近的时间范围内行为相同并实现了相同的攻击，而使用不同RC4密钥的示例表现出完全不同的行为，这一事实进一步支持了这一假设。

![5.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221004/1664857331119880.jpeg "1664857331119880.jpeg")

不同Bumblebee示例根据其RC4密钥释放了相同的有效负载

事实上，不同的示例使用相同的RC4密钥接触的不同IP地址的命令和控制服务程序会返回相同的有效负载，并为受害者阻止相同的client\_id，这一事实也表明，这些IP地址实际上只是一个主命令和控制服务程序的前端，所有Bumblebee连接都中继到该服务程序。

这些僵尸网络行为的另一个有趣的特点是，Bumblebee释放到受害者机程序中的工具集是如何根据目标的类型而有所不同。为了部署攻击，在bumblebee支持的5个命令中，有3个命令导致从C2服务程序下载代码并执行：

DEX：将可执行文件部署到磁盘并运行它。

DIJ：将库注入进程并执行它。

SHI：向进程中注入并执行shellcode。

作为对各种Bumblebee僵尸网络持续监控的一部分，研究人员一直在监控基于网络类型或地理位置等因素的行为差异。虽然受害者的地理位置似乎对恶意软件的行为没有任何影响，但研究人员观察到，Bumblebee在感染了属于域(共享同一个Active Directory服务程序的逻辑网络组)的机程序后，与连接到工作组(微软术语，表示点对点局域网)的从公司网络中隔离出来的机程序之间存在非常明显的差异。

如果受害者连接到WORKGROUP，在大多数示例中，它会收到DEX命令(下载和执行)，这将导致它从磁盘上释放并运行一个文件。这些有效负载通常是常见的盗窃程序，如Vidar Stealer，或银行木马：

![6.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221004/1664857341178631.jpeg "1664857341178631.jpeg")

Bumblebee C2响应，其中包含一个Base64编码的有效负载的DEX命令

另一方面，如果受害者连接到AD域，它通常会收到DIJ(下载和注入)或SHI(下载shellcode和注入)命令。

![7.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221004/1664857349112079.jpeg "1664857349112079.jpeg")

带有DIJ命令的Bumblebee C2响应，其中包含Base64编码的有效负载

在这些示例中，产生的攻击来自更先进的后开发框架，如cobalt tstrike、silver或Meterpreter。

在这些示例中，还可以观察到，无论命令和控制服务程序的IP和group\_name字段如何，使用相同RC4密钥的示例都会使用相同的团队服务程序释放相同的Cobalt Strike信标，这已被证明是将不同示例作为同一僵尸网络的一部分相互关联的非常有用的方法。

由Bumblebee释放的有效负载的最后一个有趣特性是，在许多示例中，使用DEX命令下载的二进制文件和使用DIJ命令下载的那些二进制文件都是使用同一个Bumblebee打包程序打包的。

**总结**

通过分析Bumblebee操作人员使用的命令和控制服务程序的行为，研究人员观察到他们如何调整其感染链的行为方式，有时这种方式会大大增加活动受害者的数量和C2流量

目前，即使在不同的Bumblebee僵尸网络中，在部署第二阶段有效负载之前的行为也非常相似，但从选择第二阶段的有效负载开始的进一步行为会根据所使用的RC4密钥而变得不同。除了使用RC4密钥本身之外，此行为还可以将活动分组到不同的集群中。

与其他使用第三方打包程序和现成的绕过防病毒工具的攻击不同，Bumblebee对攻击本身和部署在受害者电脑上的一些示例使用自己的打包程序，就像其他高级恶意软件家族(如Trickbot)一样。虽然这让Bumblebee操作员在改变行为和添加功能方面有了更大的灵活性，但使用独特的自定义工具也可以作为一种快速识别Bumblebee野外活动的方法。

本文翻译自：https://research.checkpoint.com/2022/bumblebee-increasing-its-capacity-and-evolving-its-ttps/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?SXn1dgWl)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/07/6cfb327dad8fe371f6fa.jpg)

# [luochicun](https://www.4hou.com/member/aOZG)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/aOZG)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://w...