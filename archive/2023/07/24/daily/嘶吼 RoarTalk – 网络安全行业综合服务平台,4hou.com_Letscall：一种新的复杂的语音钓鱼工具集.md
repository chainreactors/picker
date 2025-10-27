---
title: Letscall：一种新的复杂的语音钓鱼工具集
url: https://www.4hou.com/posts/1pEZ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-24
fetch_date: 2025-10-04T11:51:51.679023
---

# Letscall：一种新的复杂的语音钓鱼工具集

Letscall：一种新的复杂的语音钓鱼工具集 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Letscall：一种新的复杂的语音钓鱼工具集

lucywang
[技术](https://www.4hou.com/category/technology)
2023-07-23 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)125843

收藏

导语：近年来，随着Vishing的兴起，人们便不再信任未知号码呼叫。

Vishing即语音钓鱼，是网路钓鱼(Phishing)的电话版本。黑客们利用语音钓鱼的方式,在短短的几分钟内就可清空人们的账户。近年来，随着Vishing的兴起，人们便不再信任未知号码呼叫。

比如，接到冒充银行员工的联系人打来的电话是非常令人讨厌的，最近研究人员遇到了一组以前从未见过的恶意应用程序，开发者将其称为“Letscall”，目前针对的是来自韩国的个人用户。从技术上讲，没有任何规定禁止他们将攻击范围扩大到欧盟国家。换句话说，我们正在处理一个随时可用的框架，任何攻击者都可以使用它，因为它包含了关于如何操作受影响设备以及如何与受害者沟通的所有说明和工具。

**该组织可能包括：**

熟悉现代VOIP流量路由概念的Android开发人员，我们称其为“开发人员”，因为我们在其中一个阶段观察到命令命名的差异。

设计人员负责网页、图标以及管理面板、网络钓鱼网页和移动恶意应用程序的内容。

前端开发人员熟悉JavaScript开发，包括VOIP流量处理。

后端开发人员熟悉保护后端API免受未经授权访问的技术。

呼叫具有语音社会工程攻击技能的接线员，他们可以流利地说不同的语言。

**攻击分为三个阶段：**

受害者访问一个特别制作的钓鱼网页，看起来像Google Play Store。受害者从该页面下载恶意应用程序链的第一阶段。

第一阶段（我们称之为下载程序）在设备上运行准备工作，获得必要的权限，打开钓鱼网页，并安装第二阶段恶意软件，该恶意软件将从控制服务器下载。

第二阶段是一个强大的间谍软件应用程序，它将帮助攻击者窃取数据，并将受攻击的设备注册到P2P VOIP网络中，该网络用于通过视频或语音通话与受害者通信。此应用程序还会释放第三个阶段，即链的下一个部分。

letcall使用WEBRTC技术来路由VOIP流量，并将受害者与呼叫中心操作员连接起来。为了达到最大的电话或视频通话质量，并克服NAT和防火墙，Letscall使用STUN/TURN方法，包括Google STUN服务器。

第三阶段是第二阶段恶意软件的配套应用程序，并扩展了一些功能，它包含电话呼叫功能，用于将呼叫从受害者设备重定向到攻击者呼叫中心。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689753646126836.png "1689753646126836.png")

Vishing技术迭代过程

这种钓鱼攻击已经发展得非常先进和复杂了，因为欺诈者现在使用现代技术进行语音通信路由和自动呼叫受害者的系统（所谓的自动窃取者，用于通过电话自动广告），并播放预先录制的诱惑信息。如果受害者上钩了，接线员就会接起电话，引导受害者按照骗子的要求行事。攻击者可能会欺骗受害者到最近的自动取款机取现金，或者迫使受害者披露个人信息，如银行账户数据、信用卡详细信息或银行凭证。

在过去的几年里，这种攻击已经成为一种明显的趋势，没有证据表明欺诈者会放弃该方法。

如今，受害者和安全行业都在发展，并通过各种防御机制对抗这种攻击。使用呼叫者识别应用程序或了解欺诈者策略可能足以抵御攻击者。

这可能是欺诈者试图利用他们所掌握的任何类型的信息，而不仅仅是使用姓名和电话号码来获得受害者信任的原因之一。为了获得更高级别的信任，攻击者通过访问受害者设备对受害者进行侦察。

将这两种类型的攻击(手机攻击和Vishing)结合起来，欺诈者可以“一举两得”：我们观察到的一种常见攻击类型包括在请求受害者小额贷款。如果受害者注意到一些不寻常的活动，攻击者将打电话给受害者，冒充银行安全小组的成员，并向受害者保证没有什么可担心的。

在完全控制受攻击设备的情况下，攻击者还会将任何呼叫重新路由到由攻击者管理的另一个呼叫中心。如果受害者决定联系银行并询问与可疑活动有关的问题，准备充分的接线员将接听电话。使用这种作案手法，攻击者还可能要求受害者提供更多细节，以帮助他们进行犯罪活动并完成资金转移。

这种攻击是非常危险的，因为受害者必须偿还贷款，金融机构可能不会关心这种攻击和设备攻击，从而降低了调查潜在欺诈攻击的可能性。这就是为什么这样的攻击应该被业界披露和报告的原因。

对于“letcall”恶意软件的所有三个阶段，攻击者都使用了强大的逃避检测技术。一些版本的下载程序使用腾讯Legu模糊处理或Bangcle（SecShell）进行了保护。对于第二和第三阶段，使用了ZIP文件目录树中的长名称和清单攻击技术。Checkpoint最近也报道了同样的技术。然而，从代码和基础设施的角度来看，这些活动是不同的。攻击者有可能彼此分享知识，或者受到同一地区其他攻击者的影响。

“Letscall”第二和第三阶段规模巨大，我们的研究仍在进行中。然而，我们现在想提供一些见解。

**下载程序**

目前还不知道攻击者如何说服受害者访问可以找到下载程序的诱饵网页，这可能是一种黑化的SEO技术或使用垃圾邮件的社会工程。到目前为止，我们知道这些页面模仿了Google Play store，并针对移动屏幕分辨率进行了优化。这里一个值得注意的细节是页面的语言为韩语。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689753674207798.png "1689753674207798.png")

从技术角度来看，使用的下载程序是相对简单的应用程序，有时使用我们稍后将描述的自定义技术。下载程序的目标是做两件事：下载并运行第二阶段应用程序。有效负载的URL地址被硬编码到应用程序中。

![3.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689753738865193.jpg "1689753738865193.jpg")

打开带有网络钓鱼窗口的web视图，该窗口也硬编码到应用程序中。

这些页面会因正在进行的传播活动而有所不同，研究人员发现至少有3个页面模仿了Banksala（贷款比较聚合器）、Finda（贷款对比聚合器）和KICS（韩国刑事司法服务信息系统）。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689753753560389.png "1689753753560389.png")

每个页面都会诱使受害者输入敏感信息，如居民注册号（身份证）、电话号码、家庭地址、工资大小和雇主姓名。该输入数据将自动发送给攻击者。同样的数据也被输入到贷款聚合器的原始网页中。我们可以非常肯定地说，攻击者要么会使用窃取的数据在合法网站上填写类似的表格来申请贷款，要么也可能是网络钓鱼页面在受害者和贷款聚合页面之间充当代理：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689753777184385.png "1689753777184385.png")

**第二阶段**

乍一看，这个应用程序显然是非常模糊的，要分析它的功能需要很长时间。让我们来看看其中的每一种技术：

1.APK文件中包含长路径名。一些分析系统将无法处理提取此类APK文件的内容。

![6.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689753838160467.jpg "1689753838160467.jpg")

2.XML文件攻击。

3.代码打包：核心DEX文件不包含清单中列出的代码。然而，它包含模糊代码，这些代码将从APK收集文件，对其进行解密并加载。这些文件位于APK文件的根目录中，它们的名称以“o”开头，以“bf”结尾，即“obf”或模糊处理：

![7.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689753931183159.jpg "1689753931183159.jpg")

所有的文件都有相似的标题和相对较低的熵。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689753961808451.png "1689753961808451.png")

甚至还隐藏了一些字符串：

![9.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689753980235105.jpg "1689753980235105.jpg")

经过一些修改之后，很明显，这几十个文件都是DEX文件，只是在它们的标头文件中做了微小的修改。通过观察文件第一个字节中重复的0x1f值，我们可以猜测，为了隐藏原始标头，使用了一个字节的异或加密，并且只加密了文件的0x64字节。

我们重建了APK文件并分析了代码。在第一步分析之后，我们意识到我们面临着一些重大问题。

![10.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689753994139171.jpg "1689753994139171.jpg")

由此产生的APK文件基于十几个不同的框架，包括okhttp3和butterknife等流行的框架，以及我们第一次观察到的一些库。

最有趣的库是im/zego。

第二阶段滥用合法服务ZEGOCLOUD作为IP语音通信和消息传递的提供商。为了处理这种依赖于WEB RTC的通信，攻击者使用中继服务器。特别使用的公开可用的STUN/TURN服务器，包括来自Google的服务器，以及自配置的服务器。在此过程中，他们还窃取了应用程序代码中的凭据。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689754025264756.png "1689754025264756.png")

需要这样的功能来执行呼叫中心运营商和受害者之间的P2P语音/视频连接，并且相同的信道也用于具有许多不同命令的C2通信。此外，该恶意软件还支持使用网络套接字进行通信。来自P2P服务和web套接字通信的命令有时会相互重复，共涉及32个命令。

为了过滤数据并更改配置，恶意软件使用传统的http通信：

![13.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689754062151375.jpg "1689754062151375.jpg")

攻击者还可以对需要重定向的电话号码配置白名单，对需要绕过重定向的电话号码配置黑名单。

我们注意到的另一件有趣的事情是nanoHTTPD的使用，这个应用程序创建一个本地http服务器，然后打开Chrome浏览器进行访问。

![14.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689754088170233.jpg "1689754088170233.jpg")

通过滥用可访问性服务，它将把必要的界面元素推入Chrome，并将第三阶段的恶意软件传递给受害者。这种更复杂的方法被用来以更有效的方式欺骗受害者。

**第三阶段**

从技术角度来看，安装的下一个APK文件看起来与第二阶段APK非常相似，使用了相同的逃避检测技术，并且相同的xor加密DEX文件位于APK文件的根文件夹中。此应用程序还包含一个大型代码库：

![15.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689754104173867.jpg "1689754104173867.jpg")

第三阶段最有趣的部分是名为“phonecallapp”的包，该包包含负责电话操纵攻击的代码，它将拦截传入和传出的呼叫，并根据攻击者的愿望重新路由。

为了配置处理电话呼叫的方式，攻击者使用具有以下结构的本地SQLite数据库：

![16.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689754121142175.jpg "1689754121142175.jpg")

在第三阶段APK的资产中，已经准备好了MP3语音信息，如果有人试图拨打银行电话，就会播放给受害者。

![17.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689754186936091.jpg "1689754186936091.jpg")

对于攻击者来说，他们的目标显然是模仿客户给银行打电话时的体验。

第三阶段有自己的一组命令，其中还包括Web套接字命令。

其中一些命令与地址簿的操作有关，例如创建和删除联系人。其他命令涉及创建、修改和删除过滤器，这些过滤器确定哪些调用应该被拦截，哪些应该被忽略。

**基础设施**

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689754224667960.png "1689754224667960.png")

在我们获得Downloader之后，我们开始分析C2服务器并分析了管理面板。

![19.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689754236733851.jpg "1689754236733851.jpg")

与许多不同的WEB应用程序一样，它由两部分组成。

基于VueJS的前端，用于向攻击者提供可视化内容；

基于Laravel PHP框架的后端，使用API与前端和恶意应用程序通信；

前端是最有趣的部分，因为它为管理员和电话接线员提供了一个功能齐全的工作帐户。从这个面板中，电话接线员可以选择受害者，并直接从浏览器开始视频/音频对话。运营商还可以看到从目标泄漏并上传到基础设施的完整详细信息列表。它由至少33000个代码字符串组成。

我们确定了操作员可以使用的至少19个与受攻击设备控制相关的菜单：

![20.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230719/1689754279159528.jpg "1689754279159528.jpg...