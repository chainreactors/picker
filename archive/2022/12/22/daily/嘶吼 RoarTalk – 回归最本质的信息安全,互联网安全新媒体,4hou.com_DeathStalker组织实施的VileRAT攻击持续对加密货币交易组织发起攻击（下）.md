---
title: DeathStalker组织实施的VileRAT攻击持续对加密货币交易组织发起攻击（下）
url: https://www.4hou.com/posts/PJgW
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-22
fetch_date: 2025-10-04T02:11:48.308850
---

# DeathStalker组织实施的VileRAT攻击持续对加密货币交易组织发起攻击（下）

DeathStalker组织实施的VileRAT攻击持续对加密货币交易组织发起攻击（下） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# DeathStalker组织实施的VileRAT攻击持续对加密货币交易组织发起攻击（下）

gejigeji
[技术](https://www.4hou.com/category/technology)
2022-12-21 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)115443

收藏

导语：自2022年3月以来，研究人员已经识别出更多与VileRAT相关的恶意文件和新基础设施的示例，这可能是攻击尝试增加的征兆。

![vilerat_featured-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660209034201927.jpeg "1660209034201927.jpeg")

**VileRAT：一个复杂的Python植入物**

VileRAT是来自DeathStalker的复杂同名攻击链的最后一个已知阶段。它是一个经过混淆和打包的Python3 RAT，与py2exe捆绑为一个独立的二进制文件。研究人员在2020年第二季度首次发现它，随后它也被其他供应商命名为PyVil。

**关于VileRAT的介绍**

嵌入在py2exe捆绑二进制文件中的Python库(DLL)通常来自官方Python版本。在分析VileRAT示例时，我们注意到它的Python DLL是Python 3.7源代码的自定义编译：DLL版本被标记为“heads/3.7-dirty”而不是官方发布的“tags/v3.7.4”，并引用缩短的Git提交ID“0af9bef61a”。这个缩短的提交ID与标准CPython实现的3.7分支的源代码存储库中的一个匹配，该实现的日期为2020年5月23日。考虑到这个提交日期，以及在2020年第二季度首次发现VileRAT，研究人员相信VileRAT是在2020年6月首次部署的。

**解包VileRAT**

当我们第一次遇到VileRAT时，我们注意到所有用于Python3的常用反编译工(uncompille6、decompyle3和unpyc37等都无法从VileRAT字节码中正确检索Python源代码。

VileRAT的第1阶段已在Python字节码级别进行了混淆，目的是破坏现有的反编译器。字节码通过以下方式混淆：

添加多个在执行时没有任何影响的操作(中立操作)和无用数据；

添加令人困惑的分支和异常处理程序；

在执行期间永远不会到达的部分中插入无效的字节码，反编译器仍然尝试反编译，但失败。

![24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660209047214417.png "1660209047214417.png")

VileRAT的第1阶段Python字节码，原始形式（左）和反混淆形式（右），只需看红色部分即可

一旦在字节码级别进行了清理，VileRAT解包的第1阶段就可以被正确反编译为Python代码：

![25.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660209056521279.png "1660209056521279.png")

VileRAT嵌入不少于三层的包装。目的就是使Python脚本(VileRAT)难以从人类角度分析，这也是DeathStalker的独特做法，考虑到他们也对感染链的所有其他步骤进行了相同的尝试，证明这是惯用做法。

最后的解包步骤最终提取了VileRAT的Python代码和它在内存中的整个依赖包，所有这些内容导致绑定py2ex的VileRAT样本的重量大约为12MB。使用第二类算法解包利用解码和BZIP2解压缩。最后的VileRAT Python包包含一个conf.pyc模块，其中包括一个版本号，以及默认的C2域名：

![26.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660209066315542.png "1660209066315542.png")

VileRAT版本和函数

通过分析并比较了各种VileRAT示例，版本号是从2.4到8。虽然版本号跨度这么大，但VileRAT的功能没有太大变化，研究人员分析的最早示例中的一些功能实际上已经被删除，例如将SSH用作C2通道，或者截图，后者现在在VileLoader中实现，其余功能包括：

1.使用现有或下载的二进制文件执行任意远程命令；

2.建立与远程服务器的SSH连接，可能利用它们将目标计算机的端口转发到远程服务器；

键盘记录；

3.使用计划任务设置持久性；

4.列出安装在目标计算机上的安全解决方案；

5.从C2服务器自我更新。

6.VileRAT有五种不同的专有执行模式，可从命令行启用，所有这些模式都可以通过来自C2的附加命令开关、参数或数据进一步更改：

命令行选项、内部名称和执行模式说明如下：

1.-a， enc\_cmd\_data  RUN\_CMD\_AS\_USER\_ARG，任意命令执行：“命令”一词范围很广：它可以是一个现有的二进制文件、一个shell命令、一个下载的可执行文件、一个Python包，或者一个内部的VileRAT函数。为了指定“命令”，一个JSON字典作为可选参数传递。有些命令将通过再次启动VileRAT(使用一组不同的命令选项)来执行。执行完成后，VileRAT退出。

2.-l，enc\_cmd\_data\_rss  RUN\_R\_SSH\_SHELL\_ARG，SSH连接测试：VileRAT启动自己的一个新进程，它连接到一个远程SSH服务器(使用一个私钥)，然后关闭连接。这个SSH连接在以前的示例中用作C2通道，但是在最近的示例中删除了C2逻辑。为了指定SSH连接设置，将传递一个JSON字典作为可选参数。执行完成后，VileRAT退出。

3.-r，enc\_cmd\_data\_rds RUN\_R\_DYN\_SSH\_ARG，SSH隧道本地端口转发：VileRAT启动自己的一个新进程，它连接到远程SSH服务器(使用密码)。此连接用作将端口从目标计算机转发到远程服务器的隧道。为了指定SSH连接设置，JSON字典作为可选参数传递。一旦远程端至少连接到转发端口一次，VileRAT就会退出，然后关闭连接。

4.-c，cp\_exe\_path，任意文件删除：VileRAT尝试删除一个文件，其路径以明文命令参数的形式给出。当文件被删除或达到最大尝试次数(10)时，VileRAT将退出。

5.-t，rts IS\_TASK\_SCHED\_ARG，C2主客户端模式：这是VileRAT的主要执行模式。它定期在C2服务器上轮询要执行的命令。可以执行的命令是此表中描述的命令之一（RUN\_R\_SSH\_SHELL\_ARG、RUN\_CMD\_AS\_USER\_ARG、RUN\_R\_DYN\_SSH\_ARG），或其他VileRAT内部更新命令之一。CMD\_UPDATE\_SVC从C2下载的包触发（部分或完整）VileRAT更新，而CMD\_UPDATE\_CONF可以更新内部延迟并在C2需要时启用键盘记录器。

正如我们在2022年确定的那样，在一个典型的VileRAT第一次执行中，植入程序从以下参数开始：

![28.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660209078739798.png "1660209078739798.png")

请注意，在这种情况下，作为第一个参数传递的目标标识符实际上并未被VileRAT利用，攻击者可能只是使用它来轻松识别稍后运行的VileRAT进程。较旧的VileRAT变体通常使用显式的“-f”和“-t”命令行开关启动，这些现在是隐式的并默认启用。

以下是研究人员发现的VileRAT版本发展过程中一些值得注意的变化，除了定期更新以修复代码错误或处理未捕获的异常、重构代码、更新依赖项和更改配置：

1.在2.4和2.7版之间，VileRAT释放了使用远程SSH服务器作为C2通道的功能，以及截图实现；

2.在3.0版中，用于各种加密例程的base64编码RC4密钥从“Ixada4bxU3G0AgjcX+s0AYndBs4wiviTVIAwDiiEPPA=”更改为“XMpPrh70/0YsN3aPc4Q4VmopzKMGvhzlG4f6vk4LKkI=”，并在编码方案中添加了额外的XOR通道（使用第2类算法）。重构了VileRAT远程更新机制，增加了一个额外的命令开关（称为pmode）；

3.在3.7版中，研究人员最初确定用于2.4版本的特定Chrome版本和Trezor钱包侦察功能被从代码中删除，VileRAT失去了从运行它的文件系统上提供的文件进行更新的能力；

4.在5.4版中，生成UUID类型标识符的方式发生了变化；

5.在6.5版中，添加了一个额外的命令开关（称为jmode）；

6.在6.6版中，“-f”和“-t”命令选项默认启用。

**VileRAT HTTP C2协议**

VileRAT的主C2通信循环，在主C2客户端模式下执行，非常简单，并且在一个单独的线程中运行：

1.每隔2-5分钟，VileRAT会尝试向其配置中存在的每个C2服务器发送HTTPPOST请求，直到有一个响应或列表用尽。环境数据嵌入到一个JSON字典中，使用RC4加密，使用第二类的XOR算法编码，base64编码和URL编码，最后设置为HTTP请求URL路径；

2.C2服务器可能会响应一个HTTP响应，其正文可以包含一个编码和加密的JSON数组。如果是这样，JSON必须至少包含一个要执行的命令。

![29.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660209087196702.png "1660209087196702.png")

VileRAT C2请求准备函数

就像在VileLoader中一样，HTTP请求中的User-Agent值是从可能值的固定列表中随机选择的。传递给C2服务器的JSON可以分解如下：

![30.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660209096155794.png "1660209096155794.png")

简单介绍一下VileRAT的基础设施

我们寻找了可以从收集的示例（恶意DOCX文件、DOTM文件及其宏、VileDropper、VileLoader或VileRAT）中检索到的C2域中的特性，这些特性在本报告中有所描述。我们忽略了2021年10月中旬之前注册的域名，因为其中大部分已经在公共来源中被披露，所有已知的恶意域名和IP都在下面的攻击指标部分中完整列出。值得注意的是，迄今为止，我们已经确定了数百个与VileRAT攻击链相关的域。

这使我们能够确定一些可能的VileRAT特定的基础设施创建偏好：

1.最迟从2021年10月开始，DeathStalker基础设施IP均属于AS42159（DELTAHOST UA，位于NL）。根据研究人员的分析，DeathStalker可能早在2021年6月就开始利用具有来自该AS（以及其他AS）的IP地址的服务器；

2.恶意域名通常在NAMECHEAP、PorkbunLLC或PDRLtd.批量注册（同一天多个域）；

3.许多恶意域名试图伪装成看似合法的数字服务提供商名称（例如“azcloudazure[.]com”或“amzbooks[.]org”），其中一些表示可能试图利用全球关注的事件进行攻击活动（例如“weareukrainepeople[.]com”或“covidsrc[.]com”）；

4.大多数时候域使用似乎是分开的，一个域仅用于攻击DOCX/DOTM、VileLoader或VileRAT，并且可能表明攻击者希望将其操作紧密聚集在一起。但是所有这些域通常都指向一组非常有限的IP地址；

5.研究人员通过对恶意活动期间暴露在C2IP上的服务特征的快速分析，注意到一些常见的签名：HTTP服务发送的内容和标头值的组合只能针对此类恶意基础设施进行检索。

**VileRAT的目标**

从2021年8月至今，在保加利亚、塞浦路斯、德国、格林纳丁斯、科威特、马耳他、阿拉伯联合酋长国和俄罗斯联邦发现了10个受攻击或目标组织。

![31.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660209106504345.png "1660209106504345.png")

DeathStalker的VileRAT活动所针对的组织区域分布（较深的颜色表示较高的集中度）

研究人员目前还无法对所有已确定的组织进行分析，但其中一半是外汇(FOREX)和加密货币交易所经纪人。一些已识别的恶意文档和基础架构域包含目标组织的名称，并确认了这一目标。

值得注意的是，被确认的机构包括近期的初创公司和老牌行业领袖，包括可疑的加密货币交易平台。从我们手头有限的数据来看，确定这样的组织是极其困难的，因为一个小型FOREX公司可能在不同的国家托管其基础设施，雇佣几个来自不同国家的远程工作人员，并合法地设在避税天堂。

**归因**

当研究人员在2020年6月首次发现VileRAT时，一开始将植入物和相关攻击链归因于DeathStalker。这主要是因为它与先前已知的EVILNUM活动的相似性，比如LNK文件中的常见特定元数据，类似的TTP——尤其是利用GoogleDrive文件和虚假角色的鱼叉式网络钓鱼方法，受害者特征也一样。EVILNUM活动和DeathStalker之间的联系已经在我们之前的文章中介绍过。

如上述分析所述，研究人员仍然高度相信所描述的更新植入物和相关攻击链是由DeathStalker开发和运营的，原因如下：

1. 本次活动所使用的主要植入物(VileLoader和VileRAT)是之前分析过的内容的更新，并且仍然与之前的样本共享大量代码和实现细节；

2.上述感染链的各个组件(DOCX、启用宏的DOTM、VileDropper)共享了之前被DeathStalker用作其他活动(尤其是PowerSing和PowerPepper)一部分的实现逻辑和技术；

3.使用受害者从电子邮件中下载的恶意文档作为攻击媒介；

4.向远程服务器发送攻击进度和错误信号；

5.使用类似实现的XOR算法进行字符串混淆，在DOTM宏中，以及以前记录的PowerPepper加载程序中；

6.利用Office对象属性作为隐藏数据源；

7.使用具有预设常量的类似哈希函数，在VileDropper中生成目标标识符，在PowerSing中解码IP地址。

**总结**

1.VileRAT及其加载程序和相关攻击链在两年多的时间里不断且频繁地更新，并且仍然被用来持续针对外币和加密货币交易经纪人，其目的是逃避检测。

2.逃避检测一直是DeathStalker的目标，VileRAT活动足以证明这一切，毫无疑问，它是我们迄今为止发现的最成功的逃避检测成功的攻击，使用了最复杂、混淆手段最多和试探性规避的技...