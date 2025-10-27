---
title: 虚假的成人网站推送伪装成勒索软件的擦除工具
url: https://www.4hou.com/posts/17Po
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-13
fetch_date: 2025-10-03T22:36:59.741769
---

# 虚假的成人网站推送伪装成勒索软件的擦除工具

虚假的成人网站推送伪装成勒索软件的擦除工具 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 虚假的成人网站推送伪装成勒索软件的擦除工具

布加迪
[新闻](https://www.4hou.com/category/news)
2022-11-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)167254

收藏

导语：恶意成人网站推送虚假的勒索软件，这类勒索软件实际上充当了擦除工具的角色，悄悄地企图删除他人设备上的几乎所有数据。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150394183218.png "1665354072164916.png")

恶意成人网站推送虚假的勒索软件，这类勒索软件实际上充当了擦除工具的角色，悄悄地企图删除他人设备上的几乎所有数据。

虽然目前尚不清楚这伙威胁分子是如何宣传推广这类网站的，但他们无不使用表明他们提供裸照的主机名，比如nude-girlss.mywire[.]org、sexyphotos.kozow[.]com和sexy-photo[.]。

据最先公开报道该活动的威胁情报公司Cyble声称，这类网站会自动提示用户下载一个名为SexyPhotos.JPG.exe的可执行文件，这个文件会冒充是JPG图片。

![p1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150396100343.png "1665354084204923.png")

图1. 投放恶意软件的交友网站（来源：Cyble）

然而，由于默认情况下Windows禁用文件扩展名，用户会在他们的Downloads（下载）文件夹中看到一个名为SexyPhotos.JPG的文件，可能会双击它，以为这是图片。

一旦双击启动，虚假的勒索软件就会在用户的%temp%目录中投放四个可执行文件（del.exe、open.exe、windll.exe和windowss.exe）以及一个批处理文件（avtstart.bat），并运行它们。

![p2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150397133842.png "1665354095117239.png")

图2. 恶意软件投放的文件（来源：Cyble）

这个批处理文件通过将所有四个可执行文件复制到Windows Startup（启动）文件夹来获得持久性。

接下来，执行“windowss.exe”以投放另外三个文件，包括执行重命名操作的“windows.bat”。该批处理文件针对的文件类型和文件夹如下表所示。

![p3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150398199849.png "1665354110744763.png")

图3. 虚假勒索软件针对的文件和目录（来源：Cyble）

结果是将所有文件重命名为通用名称，比如“Lock\_6.fille”。因此，虽然这些文件的内容并没有被修改或加密，但受害者根本无法弄清楚它们的原始名称。

![p4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150400195020.png "1665354119151786.png")

图4. 文件在虚假加密后的外观（来源：Cyble）

勒索函由“windll.exe”以“Readme.txt”的名称放在不同位置。

勒索函要求受害者在三天内支付300美元的比特币，并威胁在七天的延长期内将赎金翻倍至600美元，之后将永久删除攻击者的服务器上的所有文件。

![p5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150401147851.png "1665354142760498.png")

图5. 勒索函投放在不同位置（来源：Cyble）

实际上，这个虚假勒索软件并没有窃取任何数据，而且如前所述，恶意软件开发者不太可能开发出了恢复文件的工具。

Cyble在报告中表示：“即使提供了解密工具，也不可能将文件重命名为原始文件名，因为恶意软件在感染期间并不将文件存储在任何地方。”

**伪装的数据擦除工具**

然而，该恶意软件似乎不是勒索软件，其唯一的目的只是使用虚假加密作为诱饵，同时删除受害者驱动器上的几乎所有文件。

Cyble发现，在执行虚假加密后，恶意软件会企图执行“dell.exe”，但由于命名错误导致了改而投放“del.exe”，因此这个步骤在Cyble看到的样本中不起作用。

![p6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150402681884.png "1665354164670859.png")

图6. 错误文件名导致的错误（来源：Cyble）

如果威胁分子修复了这个小错误，“dell.exe”将运行，从[A:\ – Z:\]中删除所有系统驱动器，但C:\驱动器除外。

![p7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150403104189.png "1665354178168639.png")

图7. 驱动器擦除工具的代码（来源：Cyble）

最后，恶意软件执行“open.exe”，它会投放并运行“open.bat”，然后连接到URL“hxxps[:]//lllllllllll.loseyourip[.]com/downloads”，之后打开勒索函。

这个虚假勒索软件是一个典例，充分表明了粗心大意会如何导致数据丢失，哪怕是有缺陷的、并不高明的恶意软件。

受害者遇到这个恶意软件后恢复的一种可能有效的方法是，将操作系统恢复到以前的状态，因为虚假勒索软件并不删除卷影副本。

当然，这仍然可能导致数据丢失，具体取决于上一个还原点的日期。

一般来说，最好的做法是定期备份最重要的数据，因为重新安装操作系统应该是彻底摆脱这个麻烦的最快方法。

本文翻译自：https://www.bleepingcomputer.com/news/security/fake-adult-sites-push-data-wipers-disguised-as-ransomware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?UyjWyoUL)

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
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)