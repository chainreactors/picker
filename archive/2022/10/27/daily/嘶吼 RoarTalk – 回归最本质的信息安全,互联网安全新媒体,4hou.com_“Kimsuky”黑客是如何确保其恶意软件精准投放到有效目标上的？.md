---
title: “Kimsuky”黑客是如何确保其恶意软件精准投放到有效目标上的？
url: https://www.4hou.com/posts/xjz9
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-27
fetch_date: 2025-10-03T20:59:25.282275
---

# “Kimsuky”黑客是如何确保其恶意软件精准投放到有效目标上的？

“Kimsuky”黑客是如何确保其恶意软件精准投放到有效目标上的？ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# “Kimsuky”黑客是如何确保其恶意软件精准投放到有效目标上的？

布加迪
[新闻](https://www.4hou.com/category/news)
2022-10-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)136920

收藏

导语：朝鲜的“Kimsuky”威胁分子正在不遗余力地确保他们的恶意有效载荷仅由有效目标下载。

朝鲜的“Kimsuky”威胁分子正在不遗余力地确保他们的恶意有效载荷仅由有效目标下载，而不是下载到安全研究人员的系统上。

据卡巴斯基近日发布的报告显示，这个威胁团伙自2022年初以来就一直在采用新颖的手法来过滤掉无效的下载请求，当时该团伙针对朝鲜半岛的多个目标发动了新的攻击活动。

Kimsuky实施的新保护措施非常有效，以至于卡巴斯基声称即使它在成功连接到了这伙威胁分子的指挥与控制（C2）服务器之后，也无法获取最终的有效载荷。

**多阶段验证方案**

卡巴斯基发现的攻击始于发送给朝鲜和韩国的政治家、外交官、大学教授和新闻记者的一封网络钓鱼电子邮件。

由于获取了含有攻击目标部分电子邮件地址的C2脚本，卡巴斯基能够整理出一份列有潜在目标的列表。

![p1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220827/1661561903104041.png "1661561903104041.png")

图1. 卡巴斯基列出的潜在目标

电子邮件附有一个链接，该链接将受害者引到一台负责第一阶段的C2 服务器，该服务器在传递恶意文件之前检查并验证几个参数。如果访问者与攻击目标列表不匹配，就向他们提供无害的文件。

参数包括访问者的电子邮件地址、操作系统（Windows是有效操作系统）和第二阶段服务器投放的文件“[who].txt”。

与此同时，访问者的IP地址被转发给第二阶段C2服务器，作为后续的校验参数。

第一阶段C2服务器投放的文件含有一个恶意宏命令，该宏命令将受害者连接到第二阶段 C2服务器，获取下一阶段有效载荷，并使用mshta.exe进程运行它。

![p2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220827/1661561929118667.png "1661561929118667.png")

图2. 发送给攻击目标的一些文件（图片来自卡巴斯基）

有效载荷是一个.HTA文件，该文件还创建自动执行的计划任务。其功能是检查ProgramFiles文件夹路径、AV名称、用户名、操作系统版本、MS Office版本和.NET框架版本等信息，从而详细分析受害者。

指纹结果存储在一个字符串（“chnome”）中，一份副本被发送到C2服务器，新的有效载荷被获取后，向持久性机制注册登记。

下一个有效载荷是一个VBS文件，该文件可以将受害者引到合法博客，或者如果受害者是有效攻击目标，将它们引到下一个有效载荷下载阶段。

![p3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220827/1661561940110071.png "1661561940110071.png")

图3. 在感染的每个步骤都执行C2检查（图片来自卡巴斯基）

卡巴斯基详细说明，值得关注的是，这个C2 脚本会根据受害者的IP地址生成一个博客地址。在计算受害者IP地址的MD5哈希之后，它会截断最后20个字符，并将其转换成博客地址。

脚本作者在这方面的意图是，为每个受害者运营一个专门的虚假博客，从而减小其恶意软件和基础架构被暴露的风险。

这时候，检查受害者的系统，查找是否存在异常的“chnome”字符串，该字符串被故意拼错，以便用作仍然不会引起怀疑的唯一验证器。

![p4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220827/1661561959185509.png "1661561959185509.png")

图4. Kimsuky最新感染过程（图片来自卡巴斯基）

遗憾的是，卡巴斯基无法从这里继续获取下一阶段的有效载荷，因此这是不是最后一个阶段或是否有大多数验证步骤仍然不得而知。

Kimsuky是一个手法非常老练的威胁团伙，最近它部署自定义恶意软件并使用Google Chrome 扩展程序来窃取受害者的电子邮件。

卡巴斯基披露的活动表明了韩国黑客采用高明的手法来阻止分析，并大大加大跟踪难度。

本文翻译自：https://www.bleepingcomputer.com/news/security/how-kimsuky-hackers-ensure-their-malware-only-reach-valid-targets/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GblRjTLs)

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