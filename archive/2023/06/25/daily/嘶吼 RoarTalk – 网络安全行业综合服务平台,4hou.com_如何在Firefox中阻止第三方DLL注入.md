---
title: 如何在Firefox中阻止第三方DLL注入
url: https://www.4hou.com/posts/kj8Y
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-25
fetch_date: 2025-10-04T11:44:15.696764
---

# 如何在Firefox中阻止第三方DLL注入

如何在Firefox中阻止第三方DLL注入 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 如何在Firefox中阻止第三方DLL注入

lucywang
[技术](https://www.4hou.com/category/technology)
2023-06-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)118425

收藏

导语：将DLL注入Firefox可能会导致性能、安全性或稳定性问题。

在Windows上，第三方产品有多种方式将其代码注入其他正在运行的进程。这样做的原因有很多，最常见的是杀毒软件、硬件驱动程序、屏幕阅读器和银行的需要，当然恶意软件也会趁机而入。

将第三方产品的DLL注入Firefox进程是非常常见的，超过70%的Windows用户至少有一个这样的DLL！需要明确的是，这意味着没有经过Mozilla或操作系统部分数字签名的任何DLL。

大多数用户不在Windows上，第三方产品有多种方式将其代码注入其他正在运行的进程。这样做的原因有很多，最常见的是杀毒软件、硬件驱动程序、屏幕阅读器和银行的需要，当然恶意软件也会趁机而入。

将第三方产品的DLL注入Firefox进程是非常常见的，超过70%的Windows用户至少有一个这样的DLL！需要明确的是，这意味着没有经过Mozilla或操作系统部分数字签名的任何DLL。

大多数用户不知道DLL何时被注入Firefox，因为大多数时候除了检查about:third-party page.之外，没有明显的迹象表明正在发生这种情况。

不过，将DLL注入Firefox可能会导致性能、安全性或稳定性问题。原因如下：

1.DLL通常会挂钩到Firefox的内部函数中，这些函数会随着版本的不同而变化。所以，第三方产品的发行商必须努力使用新版本的Firefox进行测试，以避免稳定性问题。

2.Firefox作为一种网络浏览器，可以从不受信任和潜在的恶意网站加载并运行代码。所以，安全研究人员需要付出很多努力来保护Firefox的安全，第三方产品可能对安全性没有这么关注。

3.研究人员在Firefox上运行了大量的测试，第三方产品可能不会测试到这种程度，因为它们可能不是专门为配合Firefox而设计的。

事实上，我们的数据显示，在所有Windows上的Firefox崩溃报告中，只有2%以上是第三方代码造成的。尽管Firefox已经阻止了许多已知会导致崩溃的特定第三方DLL，但情况依然如此。

这也低估了由第三方DLL间接引起的崩溃，因为研究人员的指标只在调用堆栈中直接查找第三方DLL。此外，第三方DLL在启动时更容易导致崩溃，这对用户来说要严重得多。

Firefox有第三方注入策略，只要有可能，我们建议第三方使用扩展来集成到Firefox中，因为这是官方支持的，而且更稳定。

**为什么不在默认情况下阻止所有DLL注入？**

为了获得最大的稳定性和性能，Firefox可以尝试阻止所有第三方DLL注入其进程。然而，这会破坏一些有用的产品，比如用户希望能够与Firefox一起使用的屏幕阅读器。这在技术上也很有挑战性，不可能阻止每个第三方DLL，尤其是使用比Firefox更高权限运行的第三方产品。

自2010年以来，Mozilla已经能够为Firefox的所有Windows用户屏蔽特定的第三方DLL。这样做只是作为最后的手段，在尝试与供应商沟通以解决潜在问题后，研究人员会尽可能严格地进行调整，以使Firefox用户不再崩溃。目前研究人员只能阻止特定版本的DLL，并且只能在特定的Firefox进程中阻止它。这是一个有用的工具，但只有当特定的第三方DLL导致大量崩溃时，研究人员才会考虑使用它，这样它就会出现在Firefox崩溃列表中。

即使我们知道第三方DLL会导致Firefox崩溃，但有时DLL提供的功能对用户来说是必不可少的，用户不希望安全人员代表他们阻止DLL。如果用户的银行或当地政府需要一些软件来访问他们的账户或报税，我们屏蔽它不会给他们带来任何好处，即使屏蔽它会使Firefox更加稳定。

**赋予用户阻止注入DLL的权限**

在Firefox 110中，用户可以阻止第三方dll加载到Firefox中。这可以在about:third-party上完成，该页面已经列出了所有加载的第三方模块。about:third-party还显示了哪些第三方DLL与之前的Firefox崩溃有关，还有就是DLL发布者的信息也会显示，希望这能让用户在知情的情况下决定是否阻止DLL。下面是一个最近导致Firefox崩溃的DLL示例，点击带有破折号的按钮将阻止它：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230511/1683797864903462.png "1683797864903462.png")

以下是阻止DLL并重新启动Firefox后的情况：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230511/1683797872132735.png "1683797872132735.png")

如果阻止DLL导致问题，在故障排除模式下启动Firefox将禁用该运行的Firefox的所有第三方DLL阻止，并且可以像往常一样在about:third-party上阻止或取消阻止DLL。

**工作原理**

阻止DLL加载到进程中是一项棘手的业务，为了检测加载到Firefox进程中的所有DLL，必须在启动过程中尽早设置阻止列表。为此，使用启动进程，它创建处于挂起状态的主浏览器进程。然后，它设置任何沙盒策略，从磁盘加载阻止列表文件，并在启动该进程之前将条目复制到浏览器进程中。

复制是以一种有趣的方式完成的，启动程序进程使用CreateFileMapping()创建一个操作系统支持的文件映射对象，在用块列表条目填充后，复制句柄并使用WriteProcessMemory()将句柄值写入浏览器进程。具有讽刺意味的是，WriteProcessMemory()经常被用作第三方DLL将自己注入其他进程的一种方式，这里我们使用它在已知位置设置一个变量，因为启动器进程和浏览器进程是从同一个.exe文件运行的！

因为所有的事情都发生在启动的早期，在加载Firefox配置文件之前，被阻止的dll列表是按Windows用户而不是按Firefox配置文件存储的。具体来说，文件位于%AppData%\Mozilla\Firefox中，文件名格式为blocklist-{install hash}，其中install hash是Firefox磁盘上位置的哈希值。这是一种简单的方法，可以将不同Firefox安装的阻止列表分开。

**检测并阻止加载DLL**

为了检测DLL何时试图加载，Firefox使用了一种称为函数拦截或挂钩的技术。这会修改内存中的现有函数，以便在现有函数开始执行之前可以调用另一个函数。之所以如此，原因有很多，它允许更改函数的行为，即使函数不是为了允许更改而设计的。Microsoft Detours是一种常用于拦截函数的工具。

在Firefox中，研究人员感兴趣的函数是NtMapViewOfSection()，每当加载DLL时都会调用它。我们的目标是在发生这种情况时得到通知，这样我们就可以检查阻止列表，并禁止加载DLL（如果它在阻止列表上）。

为此，Firefox使用一个自定义的函数拦截器来拦截对NtMapViewOfSection()的调用，并返回如果DLL在阻止列表上则映射失败的消息。为此，拦截器尝试了两种不同的技术：

在32位x86平台上，从DLL导出的一些函数将以一条不执行任何操作的两字节指令（mov edi, edi）开始，并且在此（nop或int 3）之前有五条未使用的一字节指令，例如：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230511/1683797880100220.png "1683797880100220.png")

如果拦截器检测到这种情况，它可以将未使用指令的五个字节替换为要调用的函数地址的jmp。由于研究人员是在32位平台上，因此只需要一个字节来指示跳转，四个字节来表示地址，因此：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230511/1683797887753961.png "1683797887753961.png")

当修复的函数想要调用未修复版本的DLLFunction()时，它只需跳过DLLFunction()地址2个字节即可启动实际的函数代码

否则，事情会变得更加复杂。以x64的情况为例。跳转到已修复函数的指令需要13个字节：10个字节用于将地址加载到寄存器中，3个字节用于跳转到该寄存器的位置。因此，拦截器需要将至少前13字节的指令移动到一个蹦床函数中，如果需要的话，还要加上完成最后一条指令所需的足够的字节。之所以被称为蹦床，因为通常代码会跳转到那里，这会导致一些指令运行，然后跳转到目标函数的其余部分。让我们看看一个真实的示例，下面是我们要截取的一个简单函数，首先是C源代码（Godbolt编译器资源管理器链接）：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230511/1683797895298808.png "1683797895298808.png")

以上是用-O3编译的，所以它有点密集：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230511/1683797910123898.png "1683797910123898.png")

现在，从fn()开始计算13个字节将我们置于lea eax,[rdi+rdi\*2]指令的中间，因此我们必须将所有内容复制到蹦床上。

最终结果如下所示：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230511/1683797918127041.png "1683797918127041.png")

如果Firefox 修复函数想要调用未修复的fn()，那么修复程序已经存储了蹦床的地址（在本例中为0x3000000）。在C++代码中，我们将其封装在FuncHook类中，修复后的函数可以使用与普通函数调用相同的语法来调用蹦床。

整个过程比第一种情况要复杂得多，你可以看到第一个示例的修复只有200行左右，而处理这个示例的修复有1700多行，不过有些注意事项要注意：

1.并非所有转移到蹦床上的指令都必须保持完全相同，一个示例是跳转到一个没有移动到蹦床的相对地址，由于指令已经在内存中移动了，修复程序需要用绝对跳跃来代替它。修复程序并不能处理所有类型的x64指令，否则它必须更长！但研究人员已经进行了自动化测试，以确保能够成功拦截所知道Firefox需要的Windows函数。

2.研究人员专门使用了r11来加载修复函数的地址，因为根据x64调用约定，r11是一个不需要被调用方保存的易失性寄存器。

3.由于我们使用jmp从fn()返回到修复函数，而不是ret，并且类似地从蹦床返回到fn()的主代码，这使代码堆栈保持中立。因此，调用其他函数和从fn()返回都可以正确地处理堆栈的位置。

4.如果从fn()的后面跳转到前13个字节，这些字节现在将跳转到修复函数的中间，肯定会发生问题。幸运的是，这是非常罕见的。大多数函数在开始时都在进行函数序言操作，所以对于Firefox拦截的函数来说，这不是问题。

5.类似地，在某些情况下，fn()在前13个字节中存储了一些数据，这些数据将被后面的指令使用，将这些数据移动到蹦床将导致后面的指令获得错误的数据。我们已经遇到了这个问题，如果我们可以在前2GB的地址空间内为蹦床分配空间，那么可以通过使用较短的mov指令来解决这个问题。这将导致10字节的修复而不是13字节的修复，在许多情况下，这足以避免问题。

其他一些需要注意的复杂情况：

6.Firefox也有一种跨进程拦截的方法；

7.对于Control Flow Guard安全措施来说，蹦床很棘手：由于它们是合法的间接调用目标，在编译时不存在，所以需要特别注意允许Firefox修复过的函数调用它们；

8.蹦床还包括一些额外的异常处理；

9.如果DLL在阻止列表中，我们的修复版本NtMapViewOfSection()将返回映射失败，这将导致整个DLL加载失败。这不会阻止所有类型的注入，但它确实阻止了大多数注入；

一些DLL将通过修改firefox.exe的导入地址表来自我注入，该表是firefox.exe调用的外部函数的列表。如果其中一个函数加载失败，Windows将终止Firefox进程。因此，如果Firefox检测到这种注入并想要阻止DLL，我们将把DLL的DllMain()重定向到一个什么都不做的函数。

**总结**

希望读者在阅读本文后，可以让Firefox用户更加安全地访问互联网。用户大可不必在卸载有用的第三方产品和Firefox的稳定性问题之间做出选择，现在用户有了第三种选择，即保留第三方的产品并阻止其注入Firefox！

本文翻译自：https://hacks.mozilla.org/2023/03/letting-users-block-injected-third-party-dlls-in-firefox/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2fYCsx8d)

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

![](https://img.4hou.com/uploads/20171229/1514527090244385.gif)

# [lucywang](https://www.4hou.com/member/eXPv)

这个家伙很懒,什么也没...