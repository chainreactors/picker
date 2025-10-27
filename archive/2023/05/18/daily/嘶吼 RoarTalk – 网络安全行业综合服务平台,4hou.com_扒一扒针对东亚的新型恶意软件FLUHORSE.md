---
title: 扒一扒针对东亚的新型恶意软件FLUHORSE
url: https://www.4hou.com/posts/vxQg
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-18
fetch_date: 2025-10-04T11:37:05.091454
---

# 扒一扒针对东亚的新型恶意软件FLUHORSE

扒一扒针对东亚的新型恶意软件FLUHORSE - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 扒一扒针对东亚的新型恶意软件FLUHORSE

luochicun
[技术](https://www.4hou.com/category/technology)
2023-05-17 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)138254

收藏

导语：FluHorse针对东亚市场的不同领域，并通过电子邮件进行传播。

![微信截图_20230512233738.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907262108624.png "1683907262108624.png")

Check Point的研究人员最近发现了一种名为FluHorse的新型恶意软件。该恶意软件具有几个模仿合法应用程序的恶意安卓应用程序，其中大多数安装量超过100万次。这些恶意应用程序窃取受害者的凭据和双因素身份验证（2FA）代码。FluHorse针对东亚市场的不同领域，并通过电子邮件进行传播。在某些情况下，第一阶段攻击中使用的电子邮件属于知名对象。恶意软件可以在数月内不被发现，这使其成为一种持久、危险且难以发现的威胁。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907283423319.png "1683907283423319.png")

其中一个恶意软件样本在3个月后仍未在VirusTotal（VT）上检测到

攻击者使用规避技术、模糊处理和执行前的长时间延迟等技巧来躲过虚拟环境的检测。通常，这些技巧都有自定义实现，需要开发者付出大量的努力。

令人惊讶的是，FluHorse内部没有使用自定义实现的技巧，因为恶意软件的开发者在开发过程中完全依赖开源框架。尽管一些应用程序部分是用Kotlin创建的，但恶意功能是用Flutter实现的。Flutter是一个开源的用户界面软件开发工具包，由谷歌创建。它用于为各种平台开发跨平台应用程序，包括用于移动设备的Android和iOS，使用单个代码库。Flutter之所以成为恶意软件开发人员的一个有吸引力的选择，是因为它使用自定义虚拟机（VM）来支持不同的平台，而且它易于创建GUI元素。此外，由于自定义的虚拟机，分析此类应用程序非常复杂，这使得该框架成为Android网络钓鱼攻击的完美解决方案。

**模拟应用程序**

攻击者会为每个国家的目标开发一个虚假应用程序：攻击者努力仔细模仿所有关键细节，以避免引起任何怀疑。

**网络钓鱼**

让我们看一下如何在应用程序的不同变体中实现网络钓鱼，有趣的是，恶意应用程序不包含任何东西，除了为受害者提供输入可能性的几个窗口副本。没有添加额外的函数或检查。这种刻意的简单性让我们得出结论，恶意软件的开发者并没有在他们创建的编程部分投入太多精力，又或者他们可能故意做出这个决定，以进一步减少被安全解决方案检测到的机会。

不管他们的意图是什么，这个计划都很有效。受害者输入敏感数据后，这些数据会被泄露到C&C服务器。与此同时，恶意软件要求受害者在“处理数据”时等待几分钟。在这一步中，短信拦截功能发挥作用，将所有传入的短信流量重定向到恶意服务器。如果攻击者输入被盗凭证或信用卡数据，然后被要求输入双因素身份验证（2FA）代码，这也会被拦截。网络钓鱼方案如下：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907298180932.png "1683907298180932.png")

恶意软件如何进行网络钓鱼攻击

请注意，根据恶意应用程序的类型（针对电子收费、银行或约会用户），可能不需要凭据或信用卡号。

**感染链和目标**

在受害者的设备上安装恶意应用程序之前，必须先发送恶意应用程序。这就是电子邮件诱饵派上用场的地方。我们追踪了不同类型恶意应用程序的感染链，并在这些电子邮件的收件人中发现了多个知名对象，包括政府部门和大型工业公司的员工。

电子邮件诱饵很好地利用了社会工程，并与随后安装的恶意APK的所谓目的一致：支付通行费。

这是一个带有fetc.net.tw-notice@twfetc.com发件人地址：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907314750679.png "1683907314750679.png")

攻击者发送给政府接收者的电子邮件示例

攻击者使用的恶意fetc-net[.]com域与fetc公司的官方网站fetc.net.tw非常相似。

在这个恶意网站上，攻击者添加了一个额外的保护层，以确保只有受害者才能下载APK：如果目标的用户代理与预期的用户代理匹配，就会下载APK。此检查是通过客户端JavaScript执行的：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907330192103.png "1683907330192103.png")

恶意软件安装完成后，需要短信权限：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907351159036.png "1683907351159036.png")

ETC APK请求SMS权限

在此步骤中获得的权限将在受害者输入敏感数据后生效。

**恶意电子收费APK**

此应用程序仅包含3个窗口：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907368153522.png "1683907368153522.png")

恶意ETC APK按顺序显示的窗口

第一个窗口询问用户凭证，第二个窗口询问信用卡数据。所有这些敏感数据都被泄露到恶意的C&C服务器。接下来，第三个窗口要求用户等待10分钟，因为“系统繁忙”。希望用户关闭应用程序，或者至少在合理的时间内不被怀疑。当用户被“系统繁忙”消息误导而产生虚假的安全感时，攻击者会执行所有必要的操作，即拦截所有带有2FA代码的短信，并利用被盗数据。

这个诱饵应用程序的整个GUI看起来像是原始ETC应用程序的一个简单副本，用于收取通行费。以下是恶意和合法应用程序入口窗口的可视化比较：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907382878469.png "1683907382878469.png")

原始输入窗口(左)和恶意APK输入窗口(右)

原始应用程序不显示任何用于登录或输入用户凭据的字段。相反，有一个单独的窗口用于此目的：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907486198467.png "1683907486198467.png")

原始应用程序登录表格

**恶意VPBank APK**

此应用程序仅包含2个窗口：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907501134144.png "1683907501134144.png")

恶意VPBank APK按顺序显示的窗口

其原理与其他恶意APK相同：要求用户输入凭据，然后等待15分钟（而恶意ETC APK则为10分钟）。在此期间，恶意软件拦截所有传入的SMS，从而为攻击者提供他们可能需要的所有2FA代码。请注意，此应用程序不要求提供信用卡详细信息。

恶意和合法应用程序登录窗口之间的比较：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907517210348.png "1683907517210348.png")

原始登录窗口（左）和恶意APK输入窗口（右）

如上所示，即使缺少某些GUI元素，恶意副本看起来也很好。

**恶意约会APK**

约会应用程序不包含任何窗口。相反，它实际上充当了一个浏览器，引导用户进入钓鱼约会网站。但是，窃取和处理数据的原理是一样的。

我们没有与受害者交互的所有步骤的屏幕截图，因为在撰写本文时，负责处理从该APK窃取的数据的恶意服务器尚未激活。根据代码，只有信用卡数据被盗，不需要凭证。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907531162218.png "1683907531162218.png")

APK中显示的钓鱼交友网站窗口

所示消息的翻译如下：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907549142691.png "1683907549142691.png")

网络钓鱼网站上显示的消息翻译。

**技术细节**

与分析纯Android应用程序相比，分析基于flutter的应用程序需要一些中间步骤才能达到目的。

**深度分析**

如上所述，Flutter使用自定义的虚拟环境来支持具有单一代码库的多平台开发。开发过程中使用了一种名为Dart的特定编程语言。分析Flutter平台代码变得更容易了，因为它是一个开源项目，但仍然是一个繁琐的过程。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907568199039.png "1683907568199039.png")

Flutter Github页面中的Dart演示

让我们来看看在处理Flutter运行时的特殊领域时遇到的一些复杂情况。我们用哈希2811f0426f23a7a3b6a8d8b7e1bcd79e495026f4dcdc1c2fd218097c98de684解剖了一个APK。

ARM的Flutter运行时使用自己的堆栈指针寄存器（R15）而不是内置的堆栈指针（SP）。哪个寄存器用作堆栈指针在代码执行或反向工程过程中没有区别。然而，这对反编译器来说有很大的不同。由于寄存器的使用不规范，会生成错误且难看的伪代码。

启动恶意软件分析的一个好方法是确定与C&C服务器的通信协议。这可以说明很多恶意功能。里面有一个字符串，对应于我们在钓鱼电子邮件中看到的网站：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907593109455.png "1683907593109455.png")

恶意APK中字符串中C&C服务器的地址

然而，当我们试图找到对此字符串的一些引用时，分析失败：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907613171848.png "1683907613171848.png")

IDA中没有对C&C服务器字符串的引用

我们的目标是创建对该字符串的引用，以定位执行C&C通信的代码。

Flutter -re-demo和reFlutter可以用来处理Flutter应用程序，其主要思想是使用运行时快照来创建Dart对象并查找对它们的引用。reFlutter的主要目的是收集函数的名称，而flutter re-demo允许我们处理在应用程序执行期间收集的内存转储。

然而，除了内存快照之外，还需要一些更多的运行时信息。Flutter运行时使用堆来创建对象，并将指向已创建对象的指针存储在一个称为对象池的特殊区域中。指向该池的指针被传递到寄存器X27中的方法。我们需要找到对象池的位置。

flutter-re-demo使用Frida收集内存转储并获取对象池地址。如果我们使用在flutter-re-demo存储库中可用的dump\_flutter\_memory.js脚本运行APK，我们会看到所需的地址：

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907643189899.png "1683907643189899.png")

带有所需地址的Frida脚本输出

现在我们已经拥有了开始一个高效的逆向工程所需的所有元素。

在用map\_dart\_vm\_memory.py加载转储文件并运行create\_dart\_objects.py脚本后，我们现在至少可以看到一些对象：

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907659768845.png "1683907659768845.png")

脚本创建的对象

有一个名为create\_dart\_objects.py的脚本，用于创建dart对象。该脚本通过遍历对象池、解析记录和创建对象来工作。脚本没有关于这些对象的信息，脚本会为它们创建以下描述对象格式的结构：

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907695105990.png "1683907695105990.png")

这里的NNN被“class id”取代，如下所示：

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907717617303.png "1683907717617303.png")

由create\_dart\_objects.py创建的结构

在Flutter应用程序逆向工程时，研究人员注意到最后一个字段（unk）经常被用作指针。可以考虑将该字段从简单的QWORD转换为OFFSET QWORD。这可能会给带来一些误报，但也可能非常有助于创建参考。因此，我们决定更改由脚本创建的unkin结构的字段类型。以下是对原始脚本的更改：

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230513/1683907735694330.png "1683907735694330.png")

对dart\_obj\_create.py脚本的更改

研究人员提到的存储库包含一个用于创建对Dart对象引用的脚本：add\_xref\_to\_art\_objects.py。当运行它时，该脚本会遍历代码并创建对create\_Dart\_objects.py脚本创建的Dart对象的引用。不过此时仍然只有一个对我们...