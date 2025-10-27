---
title: Emotet僵尸网络在沉寂5个月后再次开始大肆散发恶意软件
url: https://www.4hou.com/posts/vJML
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-08
fetch_date: 2025-10-03T21:54:58.459079
---

# Emotet僵尸网络在沉寂5个月后再次开始大肆散发恶意软件

Emotet僵尸网络在沉寂5个月后再次开始大肆散发恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Emotet僵尸网络在沉寂5个月后再次开始大肆散发恶意软件

布加迪
[新闻](https://www.4hou.com/category/news)
2022-11-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)999757

收藏

导语：在基本上销声匿迹了近五个月之后，臭名昭著的Emotet恶意软件团伙再次大肆发送恶意电子邮件。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667786889126116.png "1667423149173159.png")

在基本上销声匿迹了近五个月之后，臭名昭著的Emotet恶意软件团伙再次大肆发送恶意电子邮件。

Emotet是一种恶意软件，通过含有恶意Excel或Word文档的网络钓鱼活动来感染系统。一旦用户打开了这些文档并启用宏，Emotet DLL就会被下载并加载到系统内存中。

一旦被加载，该恶意软件就会搜索和窃取电子邮件，用于将来的垃圾邮件活动，并投放额外的攻击载荷，比如Cobalt Strike或通常导致勒索软件攻击的其他恶意软件。

虽然Emotet过去被认为是传播最广的恶意软件，但它在2022年6月13日却突然停止发送垃圾邮件。

**Emotet卷土重来**

Emotet研究部门Cryptolaemus的研究人员报告称，大约在美国东部时间11月2日凌晨4点，Emotet团伙突然重新活跃起来，向全球的电子邮件地址发送垃圾邮件。

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667786890939636.png "1667423139171961.png")

图1

Proofpoint的威胁研究人员、Cryptolaemus的成员Tommy Madjar告诉IT安全外媒BleepingComputer，今天的Emotet电子邮件活动使用窃取的电子邮件回复链来分发恶意的Excel附件。

BleepingComputer从上传到VirusTotal的样本中看到了以不同语言和文件名称针对全球用户的附件，假装是发票、扫描件、电子表格及其他诱饵。

下面列出了示例文件名称的部分内容：

Scan\_20220211\_77219.xls

fattura novembre 2022.xls

BFE-011122 XNIZ-021122.xls

FH-1612 report.xls

2022-11-02\_1739.xls

Fattura 2022 - IT 00225.xls

RHU-011122 OOON-021122.xls

Electronic form.xls

Rechnungs-Details.xls

Gmail\_2022-02-11\_1621.xls

gescanntes-Dokument 2022.02.11\_1028.xls

Rechnungs-Details.xls

DETALLES-0211.xls

Dokumente-vom-Notar 02.11.2022.xls

INVOICE0000004678.xls

SCAN594\_00088.xls

Copia Fattura.xls

Form.xls

Form - 02 Nov, 2022.xls

Nuovo documento 2022.11.02.xls

Invoice Copies 2022-11-02\_1008, USA.xls

payments 2022-11-02\_1011, USA.xls

今天的Emotet活动还采用了一个新的Excel附件模板，其中含有绕过微软受保护视图（Protected View）的指令。

![33.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667786890573662.png "1667423163268434.png")

图2. 恶意Emotet Excel文档（来源：BleepingComputer）

当一个文件从互联网上下载时（包括作为电子邮件附件），微软就会为该文件添加一个特殊的Web标记（MoTW）标志。

当用户打开含有MoTW标志的Microsoft Office文档时，Microsoft Office会在受保护视图中打开它，以防止执行安装恶意软件的宏。

然而，在新的Emotet Excel附件中，您可以看到威胁分子在指示用户将文件复制到受信任的“Templates”文件夹中，因为这么做可以绕过Microsoft Office的受保护视图，即使是含有MoTW标志的文件。

"RELAUNCH REQUIRED In accordance with the requirements of your security policy, to display the contents of the document, you need to copy the file to the following folder and run it again:

for Microsoft Office 2013 x32 and earlier - C:\Program Files\Microsoft Office (x86)\Templates

for Microsoft Office 2013 x64 and earlier - C:\Program Files\Microsoft Office\Templates

for Microsoft Office 2016 x32 and later - C:\Program Files (x86)\Microsoft Office\root\Templates

for Microsoft Office 2016 x64 and later - C:\Program Files\Microsoft Office\root\Templates"

虽然Windows会警告用户将文件复制到“Templates”文件夹需要“管理员”权限，但用户试图复制文件这一事实表明，他们很有可能也会按下“继续”按钮。

![44.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667786890498395.png "1667423178967930.png")

图3. 请求管理员权限（来源：BleepingComputer）

当附件从“Templates”文件夹启动时，它会直接打开，并立即执行下载Emotet恶意软件的宏。

![55.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667786891115091.png "1667423196339478.png")

图4. 绕过Microsoft Office受保护视图（来源：BleepingComputer）

Emotet恶意软件以DLL的形式下载到%UserProfile%\AppData\Local下的多个随机命名的文件夹中，如下图所示。

![66.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667786891969497.png "1667423219467250.png")

图5. Emotet存储在%LocalAppData%下的随机文件夹中（来源：BleepingComputer）

然后宏将使用合法的regsvr32.exe命令启动DLL。

![77.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667786891949854.png "1667423233158253.png")

图6. 通过Regsvr32.exe运行的Emotet DLL（来源：BleepingComputer）

一旦下载，恶意软件将在后台悄悄运行，同时连接到指挥和控制服务器以接收进一步指示，或安装额外的攻击载荷。

Madjar告诉BleepingComputer，今天的Emotet感染活动还没有开始在受感染的设备上投放额外的恶意软件载荷。

然而在过去，Emotet因安装恶意软件TrickBot、最近安装Cobalt Strike信标而臭名远扬。

这些Cobalt Strike信标随后被勒索软件团伙用于获得初始访问权，这些团伙在网络上横向传播，窃取数据，并最终加密设备。

Emotet感染在过去被用来让Ryuk和Conti勒索软件团伙初步进入企业网络。

自6月份Conti关闭以来，Emotet被认为与BlackCat和Quantum勒索软件团伙相勾结，以获得已经被感染的设备的初始访问权。

本文翻译自：https://www.bleepingcomputer.com/news/security/emotet-botnet-starts-blasting-malware-again-after-5-month-break/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?6UJmpcIo)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou...