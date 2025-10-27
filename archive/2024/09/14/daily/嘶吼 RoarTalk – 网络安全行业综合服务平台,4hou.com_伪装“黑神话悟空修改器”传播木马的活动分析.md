---
title: 伪装“黑神话悟空修改器”传播木马的活动分析
url: https://www.4hou.com/posts/rpmw
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-14
fetch_date: 2025-10-06T18:24:28.357963
---

# 伪装“黑神话悟空修改器”传播木马的活动分析

伪装“黑神话悟空修改器”传播木马的活动分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 伪装“黑神话悟空修改器”传播木马的活动分析

安天
[技术](https://www.4hou.com/category/technology)
2024-09-13 15:52:11

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)105714

收藏

导语：近日，安天CERT通过网络安全监测发现利用“黑神话悟空修改器”传播恶意代码的活动。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214434183577.jpg "1726129109157930.jpg")

**1 概述**

近日，安天CERT通过网络安全监测发现利用“黑神话悟空修改器”传播恶意代码的活动，攻击者将自身的恶意代码程序与《黑神话：悟空》第三方修改器“风灵月影”捆绑在一起，再通过在社媒发布视频等方式引流，诱导玩家下载。玩家一旦下载了带有恶意代码的修改器版本，在运行修改器的同时，也将在后台自动运行恶意代码，导致计算机被控制，产生隐私泄露、经济损失等风险。

《黑神话：悟空》作为国产首款3A游戏大作，千万玩家在线狂欢，尽享盛宴。但玩家尽情在痛殴游戏中的BOSS（或被BOSS痛殴）的时候，也要小心网络中的妖魔鬼怪、恶意代码。祝玩家在游戏中都成为齐天大圣，在上网时也擦亮火眼金睛，穿上金甲战衣。

**经验证，安天智甲终端防御系统（简称IEP）可实现对捆绑的恶意代码的有效查杀**。

**2 样本传播渠道**

**1.利用视频图文引流，携带恶意钓鱼网址**

攻击者在视频网站、博客等平台发布视频、图文等格式钓鱼内容，并在其中附带捆绑木马的游戏修改器下载链接，诱导用户下载并执行恶意程序。

![2-1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214434185494.jpg "1726128978520089.jpg")

图 2‑1通过视频网站引流钓鱼网址

![2-2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214435183155.jpg "1726128930690285.jpg")

图 2‑2通过发帖引流钓鱼网址

**2.警惕利用闲鱼、淘宝等购物平台传播捆绑木马**

《黑神话：悟空》的大量“修改器”上架闲鱼、淘宝平台，售价在1~10元左右，这些修改器很多都标注称是“风灵月影”，但实际上，该修改器均为完全免费软件，在风灵月影的网站上就可免费下载。攻击者可能会将携带恶意代码的《黑神话：悟空》修改器挂到购物网站上引流，请广大用户谨慎购买。

![2-3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214435131930.jpg "1726128903104204.jpg")

图 2‑3 闲鱼、淘宝平台售卖大量修改器

**3 样本分析**

**3.1样本标签**

表 3‑1二进制可执行文件

|  |  |
| --- | --- |
| 病毒名称 | Trojan/Win32.PoolInject |
| 原始文件名 | 黑神话悟空修改器.exe |
| MD5 | 2C00D2DA92600E70E7379BCAFF6D10B1 |
| 处理器架构 | Intel 386 or later, and compatibles |
| 文件大小 | 6.88 MB (7,215,452 字节) |
| 文件格式 | BinExecute/Microsoft.EXE[:X86] |
| 时间戳 | 2022-12-14 13:40:00 UTC |
| 数字签名 | 无 |
| 加壳类型 | 无 |
| 编译语言 | Visual C/C++ |
| VT首次上传时间 | 2024-08-25 06:21:11 UTC |
| VT检测结果 | 44/75 |

**3.2样本分析**

样本是一个Advanced Installer安装包，执行时会在桌面释放“Black Myth Wukong v1.0 Plus 35 Trainer.exe”并执行，该文件为正常修改器程序。另外还会启动msi文件的安装。该安装包可使用/extract参数解包。

![3-1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214435128182.jpg "1726128875104271.jpg")

图 3‑1样本安装包

msi文件设置了执行条件，不支持虚拟机中运行。

![3-2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214436651917.jpg "1726128825827653.jpg")

图 3‑2检测虚拟机环境

其捆绑的恶意程序WindowsSandBoxC.exe存放在streams流中，会在运行正常修改器后执行。

![3-3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214436149096.jpg "1726128777107730.jpg")

图 3‑3安装包内嵌的恶意程序

样本伪装图标和数字签名为Windows Sandbox组件，但与实际系统组件无关。

![3-4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214437377360.jpg "1726128759591342.jpg")

图 3‑4伪装的图标和数字签名

样本使用ZeroMQ库在进程内传递数据。攻击者对样本中的载荷下载地址中的符号进行了替换，实际的载荷下载地址为**https[:]//a-1324330606.cos.accelerate.myqcloud[.]com/a**和**https[:]//xyz-1324330606.cos.accelerate.myqcloud[.]com/xyz**。相关地址为腾讯云对象存储服务。

![3-5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214437197184.jpg "1726128634275838.jpg")

图 3‑5利用ZeroMQ进行通信

相关下载代码如下所示。

![3-6.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214437991861.jpg "1726128621212446.jpg")

图 3‑6下载载荷

目前该载荷下载地址已失效，但通过情报关联，可以发现其后续载荷还通过相同对象云存储账号下的多个位置下载了载荷。

![3-7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214438867215.jpg "1726128604626857.jpg")

图 3‑7关联后续载荷

通过对其载荷下载地址中的腾讯云COS存储桶ID进行关联搜索，可发现近期在该腾讯云存储账号中还出现过多次恶意载荷，包括与目前活跃的“游蛇”（又称银狐）组织相关的攻击样本。

此外还发现多个其他软件被捆绑的样本，他们的行为中包含下载多个云存储文件，以及类似%ProgramFiles%\Adobe\![3-8.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214438762286.jpg "1726128587134949.jpg")

图 3‑8更多被捆绑的样本

**安天智甲终端防御系统（简称IEP）可实现对捆绑的恶意代码的有效查杀。**

建议企业用户部署专业的终端安全防护产品，对本地新增和启动文件进行实时检测，并周期性进行网内病毒扫描。安天智甲终端安全系列产品（以下简称“智甲”）依托安天自研威胁检测引擎和内核级主动防御能力，可以有效查杀本次发现病毒样本。

智甲可对本地磁盘进行实时监测，对新增文件自动化进行病毒检测，对发现病毒可在其落地时第一时间发送告警并进行处置，避免恶意代码启动。

![3-9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214439142296.png "1726128567179016.png")

图 3-9发现病毒时，智甲第一时间捕获并发送告警

智甲还为用户提供统一管理平台，管理员可通过平台集中查看网内威胁事件详情，并批量进行处置，提高终端安全运维效率。

![3-10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726214439156428.png "1726128552143856.png")

图 3-10通过智甲管理中心查看并完成威胁事件处置

**4 loCs**

|  |
| --- |
| 2C00D2DA92600E70E7379BCAFF6D10B1 |
| 308D7792233286B2AE747DA9F9343487 |
| http://tgfile.1258012.xyz/cac1be36221 |
| https://a-1324330606.cos.accelerate.myqcloud.com/a |
| https://xyz-1324330606.cos.accelerate.myqcloud.com/xyz |

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mudNZ4Cw)

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

![](https://img.4hou.com/wp-content/uploads/2017/10/a4d310d551660a09a8f6.jpg)

# [安天](https://www.4hou.com/member/e3QQ)

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

[查看更多](https://www.4hou.com/member/e3QQ)

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
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov...