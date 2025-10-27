---
title: 机器学习如何检测那些使用沙盒逃避和静态防护的恶意软件
url: https://www.4hou.com/posts/ZX2w
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-17
fetch_date: 2025-10-04T06:50:51.027682
---

# 机器学习如何检测那些使用沙盒逃避和静态防护的恶意软件

机器学习如何检测那些使用沙盒逃避和静态防护的恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 机器学习如何检测那些使用沙盒逃避和静态防护的恶意软件

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-02-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)121192

收藏

导语：Unit 42研究人员讨论了基于虚拟机监控程序的沙盒中基于内存的工件构建的机器学习渠道，该沙盒是Advanced WildFire的一部分。可以提高对恶意软件的检测精度。

Unit 42研究人员讨论了基于虚拟机监控程序的沙盒中基于内存的工件构建的机器学习渠道，该沙盒是Advanced WildFire的一部分。可以提高对恶意软件的检测精度。

正如我们以前所介绍的，恶意软件开发者正在不断完善他们的攻击手段，以使静态分析和沙盒等策略失效。封装方法和沙盒逃避等技术的不断发展让防御者防不胜防。

更糟糕的是，流行的检测技术，如结构分析、静态签名和许多类型的动态分析，并不能很好地应对目前越来越复杂的攻击。

恶意软件开发者越来越多地采用逃避技术，如混淆、封装和在进程内存中执行动态注入的shellcode。使用来自文件结构的线索进行恶意软件检测可能并不总是成功的。封装技术可以充分修改文件结构以消除这些线索。因此，仅在这类特征上训练的机器学习模型将无法有效地检测出此类样本。

这种检测方法的另一种流行的替代方法是使用机器学习模型，该模型基于恶意软件在沙盒内的执行痕迹来预测恶意行为。然而，正如我们原来所详细介绍的那样，沙盒逃避非常普遍，有效负载通常会根据任何数量的线索选择不执行，这些线索会指向正在模拟的样本。

恶意软件也可能会无意或有意地破坏沙盒环境，覆盖日志文件，或由于其所使用的低级技巧而阻止成功分析。这意味着，在执行日志上训练机器学习模型也不足以捕捉这些逃避类的恶意软件。

**使用NSIS Crypter加密的GuLoader恶意软件**

在这篇文章中，我们将分析一个使用Nullsoft Scriptable Install System（NSIS）加密器加密的GuLoader下载器。NSIS是一个用于创建Windows安装程序的开源系统。

Hash cc6860e4ee37795693ac0ffe0516a63b9e29afe9af0bd859796f8ebaac5b6a8c

**为什么静态分析没有帮助**

GuLoader恶意软件是加密的，它也是通过NSIS安装文件传递的，这对于静态分析来说并不理想，因为必须首先解压缩文件内容。一旦它被解压缩，我们仍然有加密的数据和一个NSIS脚本。脚本本身也会动态地解密代码的某些部分，这是使其难以检测的另一个因素。

然而，没有太多的结构线索可以识别这可能是恶意软件。因此，在可移植可执行文件(PE)结构上训练的机器学习模型将不能有效地将该文件与其他良性文件区分开来。

**NSIS脚本和提取GuLoadershellcode**

要提取NSIS脚本，我们必须使用7-Zip的旧版本15.05。这个版本的7-Zip能够解包脚本，而新版本已经删除了解包NSIS脚本的功能。一旦我们提取了文件内容和NSIS脚本(如图1所示)，我们就可以开始分析脚本并查看GuLoader示例是如何执行的。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605282171779.png "1675605282171779.png")

NSIS脚本

如果向下滚动脚本，我们会很快注意到文件正在复制到新创建的名为%APPDATA%\Farvelade\Skaermfeltet的文件夹中。虽然不清楚原因，但所使用的文件路径似乎是丹麦语。在复制活动之后，脚本中有常规的安装逻辑，但是有一个名为func\_30的有趣函数。

在此函数被调用之前，字符串$INSTDIR\Filterposerne\Malkekvg. exeNat被复制到名为$4的字符串变量中，如图2和图3所示。函数func\_30从Programmeludviklinger210中读取数据。Kon文件并构建代码，它将在字符Z被看到后立即调用这些代码。

NSIS允许开发人员能够从Windows DLL调用任何导出的函数，并且还允许他们将结果直接保存在NSIS寄存器/堆栈中。此功能允许恶意软件开发者在运行时动态调用Windows API函数，并使静态分析更加困难，因为在分析之前必须对其进行评估。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605300109039.png "1675605300109039.png")

调用函数func\_30

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605315132250.png "1675605315132250.png")

解码NSIS代码

要解码动态代码，我们可以编写一个简短的Python脚本，该脚本再现行为并提取Windows API调用：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605331873281.png "1675605331873281.png")

下图显示了上述脚本产生的解码数据

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605354102495.png "1675605354102495.png")

解码的Windows API调用

解码后的函数一起从NSIS压缩文件中的另一个文件中读取shellcode，并使用EnumWindows函数执行它。如果我们必须用伪代码编写这个过程，它看起来应该是这样的：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605370214564.png "1675605370214564.png")

为了使其余的分析更容易，我们将使用shellcode生成一个PE。为了生成可执行文件，我们可以使用Cerbero Profiler或LIEF Python库等工具。

在本例中，我们使用了LIEF库来构建一个新的可执行文件。我们所要做的就是添加一个包含Malkekvg.Nat文件内容的新部分，并将入口点设置为正确的偏移量。一旦我们得到了这些，就应该能够在IDAPro中打开shellcode，并看到它包含有效的x86指令。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605384154179.png "1675605384154179.png")

![8.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605394884304.png "1675605394884304.png")

在IDA Pro的入口点生成PE文件

**Shellcode分析**

现在我们在PE文件中有了Shellcode的第一阶段，我们可以在动态分析中运行它，看看会发生什么。我们将看到的第一件事是它检测到虚拟机，并在显示消息框后停止执行。此文本在运行时使用4字节XOR密钥解密。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605410154140.png "1675605410154140.png")

无法在虚拟环境中执行该示例

如果我们在IDA Pro中打开文件并稍微遵循代码，就应该能够看到用于解密第一阶段的大函数。虽然函数图概述看起来很大，但识别垃圾代码仍然很容易。

进行解密的代码如下图所示。在下图中，我们可以看到跳转到第二阶段的最终调用。此时，我们可以将第二阶段转储到另一个可执行文件中进行解密。

我们可以直接从内存中转储可执行文件，但是必须确保将入口点修补到正确的地址(在本例中为0x404328)。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605425992687.png "1675605425992687.png")

第一阶段的Shellcode解密

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605834908259.png "1675605834908259.png")

调用到下一阶段

第二阶段使用了许多反分析技术，其中的一些反分析技术为：

内存扫描已知沙盒字符串；

虚拟机监控程序检查；

时间测量；

为了获得GuLoader正在下载的最终负载，我们必须手动绕过所有这些检查，在不受所有这些技术影响的沙盒中运行它，或者在裸金属沙盒上运行它。

**提取有效负载信息**

为了在不分析第二阶段的情况下获得有效负载信息（包括所有字符串），我们可以使用Spamhaus描述的一个小技巧。GuLoader使用简单的XOR加密来加密其字符串，其中包括有效负载URL。

要解密字符串，我们可以对已经知道存在于第二阶段中的模式使用暴力。XOR运算的结果就密钥。对此的唯一限制是模式必须足够大，以便我们能够完全解密有效负载URL。例如，一个好的模式可能是用户代理字符串，默认设置为Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) ，如Gecko。

为了快速自动找到解密密钥，我们必须首先加密一个短模式（例如，用户代理字符串的前8个字节），然后搜索该结果是否在文件中的某个位置。如果它在文件中的某个位置，那么我们可以继续解密剩余的模式以获得完整的加密密钥。

我们会在本文的最后附上Python脚本，该脚本能够通过上述方法从有效负载中找到加密密钥。在任何转储的第二阶段GuLoader负载上运行脚本后，我们应该能够看到一些字符串和负载URL。

GuLoader有时在有效负载URL前面包含7到8个随机字符，它在运行时将其替换为http://或https://。使用http还是https的区别是由随机模式中的第四个字符决定的。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675605854301720.png "1675605854301720.png")

在此示例中，有效负载URL为http://ozd[.]com[.]ar/wp-includes/nHMoYlbGLWls101.qxd，并且在分析时有效载荷仍然在线。

最终下载的有效负载来自FormBook恶意软件家族，其SHA256值为fa0b6404535c2b3953e2b571608729d15fb78435949037f13f05d1f5c1758173。

**机器学习如何检测？**

在之前的一篇文章中，我们详细介绍了在实时沙盒运行期间可以从内存中提取的几种可观察工件。我们发现，当与机器学习结合使用多种逃避技术检测恶意软件时，来自内存分析的数据是非常强大的。

接下来我们回仔细观察所有这些关于运行时内存中被修改的内容，并将它们与大规模的机器学习相结合，用于恶意软件检测。该算法可以自动找到模式，并且可以识别恶意软件试图在内存中隐藏其足迹、动态分配和执行shellcode或使用解包的共性。

在这个GuLoader示例中，人类分析人员会立即识别出有几个独特的函数指针。我们还会注意到，恶意软件已经将其自身进程内存中的多个页面的页面权限更改为可写和可执行。我们的机器学习模型能够自动执行这些活动，从各种内存构件中提取有关特征来检测GuLoader示例。

如上所述，我们为Advanced WildFire创建的自动分析平台将以一种高性能的方式自动提取所有这些基于内存的工件。这意味着所有与动态解析函数指针、权限更改和解包可执行文件相关的信息都可以在我们手动管理的检测逻辑中使用，也可以用于我们的机器学习渠道。

**使用机器学习模式的检测**

下图显示了我们如何创建一个机器学习模型渠道的高级视图，该模型渠道是根据从上述基于内存的工件中提取的自定义特征进行训练的。我们选择的特性被设计成保留来自冗长工件的最有用的信息。

我们还将恶意软件执行跟踪作为额外的信息源，并构建了一个集成模型来检测恶意样本。如下图所示，从四个内存工件和恶意软件执行痕迹中自动提取各种自定义特征，并将它们传递给一个分类模型以检测恶意样本。此外，我们还构建了一个集成模型，该模型基于内存工件和基于执行跟踪的特性进行训练，以提高其性能。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675606211154975.png "1675606211154975.png")

机器学习模型架构

文件样本由流程渠道处理，以将内存工件和其他恶意软件属性保存到功能存储中。特征提取阶段使用流式处理和批处理PySpark作业的组合来生成用于训练模型的最终特征向量。

ground truth标签来自一个单独的渠道，该渠道根据恶意软件特征和研究人员输入为样本分配标签。该渠道通过使用样本首次出现的时间和哈希来生成非重叠的训练和评估数据集。

**解释模型预测**

为了识别模型的局限性和能力，理解机器学习模型的预测是至关重要的。机器学习很容易出现误报，因为它严重依赖于训练数据的质量和多样性，以及对不断变化的文件进行预测的泛化能力。因此，具有识别预测的因果特征的能力是非常有用的。

**Shapley值**

Shapley加法解释（SHAP）是一种博弈论方法，用于解释任何机器学习模型的输出。与基线预测相比，SHAP值解释了每个特征对输入特征向量的实际预测的影响。在下图中，从右到左的红色特征是将模型推向恶意预测的最顶层特征。从左到右，蓝色的特征表示降低预测为恶意软件概率的最顶层特征。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230205/1675606233140527.png "1675606233140527.png")

如上图所示，我们绘制了具有重要SHAP值的前七个特征及其相应原始特征值的力图。由于这些顶级特征的存在，我们的机器学习模型能够检测到GuLoader。这些特性对应于几个特定的动态解析API指针及其在内存中的相对位置，以及样本所做的内存页权限更改的相对类型。

**通过聚类寻找相似样本**

另一种理解模型预测的方法是在训练数据集中识别相似的样本。我们使用基于密度的扫描(DBScan)作为聚类技术，如下图所示，因为它允许异常值和不同形状的聚类。

![16.png](https://img.4hou.com/uploads/ueditor/php/...