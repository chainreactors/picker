---
title: 新出现的TgToxic恶意软件的自动化框架专门针对东南亚Android用户
url: https://www.4hou.com/posts/mXDr
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-15
fetch_date: 2025-10-04T06:35:41.170093
---

# 新出现的TgToxic恶意软件的自动化框架专门针对东南亚Android用户

新出现的TgToxic恶意软件的自动化框架专门针对东南亚Android用户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新出现的TgToxic恶意软件的自动化框架专门针对东南亚Android用户

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-02-14 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)140412

收藏

导语：该恶意软件窃取用户的凭证和资产，如数字钱包中的加密货币，以及银行和金融应用程序中的资金。

最近趋势科技的研究人员发现了自2022年7月以来针对中国台湾、泰国和印度尼西亚的Android手机用户的持续恶意软件活动，并将其命名为TgToxic。该恶意软件窃取用户的凭证和资产，如数字钱包中的加密货币，以及银行和金融应用程序中的资金。

通过分析恶意软件的自动化功能，研究人员发现了攻击者滥用了合法的测试框架Easyclick，为点击和手势等功能编写了基于javascript的自动化脚本。研究人员发现攻击者的目标是通过嵌入多个虚假应用程序的银行木马，趋势科技根据其特殊的加密文件名将其检测为AndroidOS\_TgToxic，该木马从金融和银行应用程序(如加密货币钱包、手机上官方银行应用程序的凭据和存款)中窃取受害者的资产。虽然之前针对的是中国台湾的用户，但在撰写本文时，研究人员已经观察到针对泰国和印度尼西亚用户的欺诈活动和网络钓鱼。建议用户小心打开来自未知电子邮件和消息发送者的嵌入链接，并避免从第三方平台下载应用程序。

**发现过程**

自2022年下半年以来，研究人员一直在监测这个活动，发现它的基础设施和目标在不断变化。以下是该活动时间表：

2022年7月：Facebook上出现了欺诈性帖子，通过社交工程在社交媒体平台上嵌入了针对中国台湾省用户的钓鱼链接；

2022年8月下旬至10月：色情欺诈还针对中国台湾和印度尼西亚用户，诱使他们注册，以便攻击者窃取他们的证件；

2022年11月至2023年1月：短信钓鱼(SMiShing)针对泰国用户，在此期间使用的一些网络钓鱼网站还显示，攻击者通过加密货币骗局将其活动进一步扩展到印度尼西亚。

**早期活动：通过Facebook进行欺诈**

2022年7月，研究人员发现两个可能被黑客入侵的Facebook账户在一些台湾社区团体上发布了诈骗信息，声称用户可以获得飓风、洪水和新冠疫情的救助补贴。这些帖子告诉用户可以在download.tw1988[.]link中注册申请，而这实际上是一个钓鱼网站。不知情的用户可能会成为受害者，因为该链接伪装成政府官方网站https://1988.taiwan.gov.tw/，该官方网站用于向困难人群提供补贴。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675925958142507.png "1675925958142507.png")

Facebook上发布的诈骗帖子示例，文字翻译为“夏季将发放28000项福利，现在输入https[:]//st7[.]fun/20就可以收到你的劳工补贴”。该应用程序还显示了潜在受害者就业类别的选项：“农民和渔民的生活津贴”、“无固定雇主的自营职业工人和劳动生活津贴”，以及“旅游巴士、出租车司机、导游、领队和其他补贴”。

**色情诈骗和加密货币**

通过追踪TgToxic使用的网络基础设施，研究人员随后发现了中国台湾和印度尼西亚色情和加密货币诈骗的幕后黑手。这些恶意应用程序也可以通过down[.]tw1988[.]link从同一网站下载，并伪装成约会、消息、生活方式或加密货币相关应用程序，诱骗用户安装并启用其权限。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675925976954534.png "1675925976954534.png")

虚假应用程序在下载后立即启动注册页面以诱导用户，恶意软件TgToxic开始在后台运行

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675925987203812.png "1675925987203812.png")

在印度尼西亚，虚假应用程序诱导潜在受害者进入色情勒索和加密货币诈骗钓鱼网站

**针对泰国的网络钓鱼活动**

当研究人员继续监控TgToxic恶意软件及其网络基础设施时，他们发现，在2022年底至2023年1月初的几周内，该活动背后的攻击者开始以泰国用户为目标，并观察到类似的色情和网络钓鱼诱饵针对中国台湾用户，该组织开始添加恶意代码，以窃取银行应用程序中的凭据。研究人员还发现，这两个攻击已经引起了当地媒体的关注，并在Facebook上受到了大众社区的报道。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926005110298.png "1675926005110298.png")

泰国当地流行的社交媒体账户讨论了使用流行聊天和约会应用程序的假冒版本的网络钓鱼计划(左)，以及与一名受害者的对话，该受害者也证实了恶意软件是通过smishing发送的(右)

网络钓鱼、色情和加密货币骗局与TgToxic恶意软件的最新部署样本都有关系，因为它们都是从同一个网站下载的，下载链接为down[.]tw1988[.]link。通过观察命令和控制（C&C）服务器之间的通信，这些应用程序和恶意软件的C&C从api[.]tw1988[.]link更改为test[.]ja7[.]site，后来更改为us[.]ja7[.]site。

**TgToxic的技术分析**

研究人员分析了恶意软件TgToxic是基于一个名为Eacyclick的合法自动化测试框架开发的，该框架支持通过JavaScript编写自动化脚本。该脚本可用于自动劫持Android设备的用户界面（UI），以自动执行诸如监视用户输入、执行点击和手势等功能。

使用上述框架，TgToxic可以开发自己的自动化脚本，通过窃取受害者放置用户名和密码的用户凭据来劫持加密货币钱包和银行应用程序。一旦获得了凭证，攻击者就可以在不需要用户批准或确认的情况下，使用官方应用程序进行小额交易。与其他银行恶意软件一样，TgToxic还可以通过短信和安装的应用程序窃取用户的个人信息，这些信息可以用来通过进一步扫描设备是否存储了攻击者感兴趣的应用程序来选择目标受害者。

目前，TgToxic仍在快速发展，并继续添加新功能，复制更多应用程序以窃取凭据并适应不同的应用程序UI，并从受害者那里收集更多信息。在这次分析中，研究人员选取了针对泰国移动用户的最新样本进行分析。

**代码混淆和有效负载加密**

TgToxic恶意软件使用两种方法来逃避检测和分析，研究人员将其分为两部分：

代码混淆：TgToxic混淆了类名、方法名和字段名，这使得一些分析师更难进行逆向工程。

有效负载加密：TgToxic将Easylick脚本放在一个名为“tg.iapk”的资产文件中，该文件是一个加密的Zip文件，并将在应用程序启动时动态读取其中的内容。该恶意软件实现了一种无文件的方式来解密和加载负载，并在解压缩后添加了一个额外的逻辑。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926017130920.png "1675926017130920.png")

APK结构和有效负载

**解密有效负载并滥用辅助功能服务劫持设备UI**

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926028865759.png "1675926028865759.png")

tg.iapk加密过程

正如McAiden的研究人员所指出的，tg.iapk是一个加密的.zip文件。通过静态分析，研究人员发现解压密码经过特殊编码并存储在.zip注释部分，该部分通常用于记录.zip描述。此部分的内容不会影响压缩后的内容。要获得.zip文件的密码，注释部分的内容将按照代码中指定的方式进行解码。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926044811078.png "1675926044811078.png")

Zip密码解码功能

解压缩后，研究人员发现所有文件都是二进制文件，所有文件的前四个字节都是“0x00092383”，这是专门加密的文件。通过反向分析，研究人员找到了解密函数。为了隐藏解密细节，使用反射调用密钥类和密钥方法，并加密相关的符号名称。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926073775036.png "1675926073775036.png")

特殊加密文件

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926087172905.png "1675926087172905.png")

加密文件解密功能

通过分析解密函数，研究人员得到了加密文件的格式。加密文件对密码进行了编码，并将其保存在文件的开头（紧跟魔术数字），同时将加密数据保存在文件末尾。密码的解码方式与zip密码的解码方法相同。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926097523825.png "1675926097523825.png")

特殊加密文件格式

**运行时引擎中运行的预编译脚本**

自动化脚本被预编译为Java，并使用Rhino的运行时，Rhino是一个在Java中运行JavaScript的开源引擎。调用函数中的每个开关分支都是一个JavaScript函数，研究人员将解释代码如何使用来自恶意软件的简单函数运行。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926116191679.png "1675926116191679.png")

从一个Javascript函数编译的Java字节码

此函数用于收集设备信息并发送到C&C服务器。它首先遍历一个预定义的变量“walletListAry”，其中包含攻击者感兴趣的加密货币钱包的包名列表。然后，恶意软件调用“isAppExist”来检查应用程序是否在系统中。如果确认，包名称将被推送到数组中。

然后，恶意软件以同样的方式检查电子邮件应用程序，并创建一个.json对象，其中包含它收集的信息。“apps”字段包含已安装的加密货币钱包的包名称，“mails”字段包含安装的电子邮件应用的包名称。最后，它调用“JSON.stringify”将.JSON对象序列化为字符串，并调用“emitEnc”通过WebSocket将信息发送到C&C服务器。

**C&C通信和数据泄露**

恶意软件使用WebSocket作为脚本执行的C&C通道。它将调用“StartWs”连接到WebSocket服务器，然后设置“new\_msg”事件侦听器以接收和解析C&C命令。完整的C&C命令列表如下所示：

![12.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926136189105.png "1675926136189105.png")

![1675926145785857.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230214/1676344084101393.png "1676344084101393.png")

另一个值得注意的细节是，TgToxic将根据受感染设备的地区连接到不同的C&C服务器。虽然研究人员仍在继续跟踪，但除了目前确定的三个国家之外，还没有在其他地区或国家发现TgToxic活动，但他们认为，这次攻击背后的攻击者正试图根据这些不同服务器的可用性将其活动扩展到其他国家。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926172107831.png "1675926172107831.png")

根据设备区域获取C&C主机前缀

数据通过C&C通道泄露。以短信窃取为例，恶意软件首先调用“getSmsInPhone”从邮件收件箱中提取所有短信，然后通过WebSocket C&C通道将窃取的数据上传到服务器。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926183108331.png "1675926183108331.png")

提取所有文本消息

**自动授予权限和防止卸载**

TgToxic可以劫持系统应用程序自动授予自己权限，并在受害者试图卸载恶意软件时阻止卸载。以下是恶意软件试图劫持的系统应用程序及其相应用途的列表：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926193168191.png "1675926193168191.png")

恶意软件试图控制的系统应用程序列表

**控制自动转账的金融应用程序**

TgToxic实施自动转账服务（ATS），用户不知情的情况下向攻击者转账。该恶意软件首先秘密窃取密码并解锁手势，当它检测到用户拥有钱包应用程序时，恶意软件将检查特定的活动，并通过密钥日志记录用户是否输入密码。如果用户用手势解锁设备，它还可以截屏。

一旦收到来自C&C服务器的“walletSend”命令，恶意软件就会覆盖全黑屏幕，以防止受害者意识到恶意活动和传输。然后，它打开钱包应用程序并收集链类型和余额等详细信息。然后，TgToxic将通过无障碍服务模拟用户点击所有链类型的特定收件人：

1.检查链类型是否为“usdt”，并输入钱包详细信息；

2.点击转移按钮；

3.输入接收者地址；

4.输入转账资金；

5.进入转账详情页面；

6.输入密码；

7.点击“确认”按钮；

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926236213278.png "1675926236213278.png")

检查链类型并输入钱包详细信息

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230209/1675926248753733.png "1675926248753733.png")

输入被盗的地址信...