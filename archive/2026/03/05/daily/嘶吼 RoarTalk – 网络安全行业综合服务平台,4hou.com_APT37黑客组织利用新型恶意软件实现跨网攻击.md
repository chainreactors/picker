---
title: APT37黑客组织利用新型恶意软件实现跨网攻击
url: https://www.4hou.com/posts/mkA3
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-03-05
fetch_date: 2026-03-06T04:02:20.301377
---

# APT37黑客组织利用新型恶意软件实现跨网攻击

APT37黑客组织利用新型恶意软件实现跨网攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# APT37黑客组织利用新型恶意软件实现跨网攻击

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-03-05 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)14986

收藏

导语：研究人员对APT37 Ruby Jumper活动中使用的恶意软件进行分析，识别出五款恶意工具构成的工具集。

黑客组织正在使用一批新曝光的恶意工具，在联网设备与物理隔离系统之间传输数据，通过可移动存储设备横向扩散，并实施隐秘监控。

这场恶意攻击活动被命名为Ruby Jumper，系黑客组织APT37（又称ScarCruft、Ricochet Chollima、InkySquid）所主导。

物理隔离通过在硬件层面移除所有联网模块（Wi‑Fi、蓝牙、以太网）实现；逻辑隔离则依托VLAN、防火墙等软件定义策略。在关键基础设施、军事及科研领域常见的物理隔离环境中，数据传输主要依靠可移动存储设备完成。

研究人员对APT37 Ruby Jumper活动中使用的恶意软件进行分析，识别出五款恶意工具构成的工具集：RESTLEAF、SNAKEDROPPER、THUMBSBD、VIRUSTASK、FOOTWINE。

**突破物理隔离**

攻击链始于受害者打开恶意Windows快捷方式文件（LNK），该文件释放PowerShell脚本，提取内嵌在LNK中的载荷；为转移注意力，脚本还会同时打开一个诱饵文档。研究人员未明确具体受害者，但指出该诱饵文档是朝鲜某报纸一篇关于巴以冲突文章的阿拉伯语译本。

该PowerShell脚本加载首个恶意组件RESTLEAF，这是一款通过Zoho WorkDrive与APT37命令与控制（C2）基础设施通信的远控木马。

研究人员从C2服务器获取加密Shellcode，以下载下一阶段载荷——基于Ruby语言的加载器SNAKEDROPPER。

攻击继续进行：攻击者安装Ruby 3.3.0运行环境（包含解释器、标准库与Gem组件），并将其伪装成名为usbspeed.exe的合法USB相关工具。

SNAKEDROPPER通过替换RubyGems默认文件operating\_system.rb为恶意修改版本，实现随Ruby解释器启动自动加载，并通过名为rubyupdatecheck的计划任务每5分钟执行一次。随后，攻击者下载Ruby文件ascii.rb形式的THUMBSBD后门，以及bundler\_index\_client.rb文件形式的VIRUSTASK恶意程序。

THUMBSBD的主要功能是收集系统信息、存储指令文件、准备数据外发；其核心作用是在检测到的USB驱动器中创建隐藏目录，并向其中复制文件。

研究人员称，该恶意软件可将可移动存储设备变为双向隐秘命令与控制中继，使威胁组织能够向物理隔离设备下发指令，并从中窃取数据。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260228/1772264468131523.png "1772261959154100.png")

ThumbSBD 执行流程

研究人员指出：“通过将可移动介质作为中间传输层，该恶意软件实现了对物理隔离网段的跨网渗透。”

VIRUSTASK的作用是将感染扩散到新的物理隔离设备：它会对可移动驱动器进行武器化处理，隐藏合法文件并替换为恶意快捷方式，一旦打开便执行内嵌的Ruby解释器。

该模块仅在插入的可移动设备剩余空间不小于2GB时才会触发感染流程。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260228/1772264472187281.png "1772262003105580.png")

Ruby Jumper攻击链概述

报告称，THUMBSBD还会投递FOOTWINE——一款伪装成Android安装包（APK）的Windows间谍后门，支持键盘记录、屏幕截图、音视频录制、文件操作、注册表访问及远程Shell执行。

研究人员在APT37 Ruby Jumper活动中还观察到另一款恶意软件BLUELIGHT，这是此前已与该朝鲜黑客组织关联的完整功能后门。

基于多项指标，可高度确信Ruby Jumper活动归属于APT37，包括使用BLUELIGHT恶意软件、以LNK文件为初始入口、两阶段Shellcode投递方式，以及该组织惯用的C2基础设施特征。

研究人员同时指出，诱饵文档表明Ruby Jumper活动的目标对象关注朝鲜官方宣传叙事，与该威胁组织的典型受害者画像高度吻合。

文章来源自：https://www.bleepingcomputer.com/news/security/apt37-hackers-use-new-malware-to-breach-air-gapped-networks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?CovMSMzg)

#### 你可能感兴趣的

* [![]()

  2026 年 AI + 网络安全产业生态图谱调研正式开启：诚邀行业同仁共建真实、有价值的产业画像](https://www.4hou.com/posts/Bvzo)
* [![]()

  APT37黑客组织利用新型恶意软件实现跨网攻击](https://www.4hou.com/posts/mkA3)
* [![]()

  AI 时代中国网络安全产业的五年变局|| 从 “亡羊补牢” 到 “未雨绸缪”，网安技术彻底换打法](https://www.4hou.com/posts/vwNn)
* [![]()

  打破边界防御思维！AI驱动攻击席卷55国，600台防火墙敲响警钟](https://www.4hou.com/posts/pnEy)
* [![]()

  嘶吼安全产业研究院 | 2026网络安全产业图谱调研启动](https://www.4hou.com/posts/omDL)
* [![]()

  国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/l0z1)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [2026 年 AI + 网络安全产业生态图谱调研正式开启：诚邀行业同仁共建真实、有价值的产业画像](https://www.4hou.com/posts/Bvzo)
  2026-03-05 14:00:00
* [APT37黑客组织利用新型恶意软件实现跨网攻击](https://www.4hou.com/posts/mkA3)
  2026-03-05 12:00:00
* [AI 时代中国网络安全产业的五年变局|| 从 “亡羊补牢” 到 “未雨绸缪”，网安技术彻底换打法](https://www.4hou.com/posts/vwNn)
  2026-03-04 11:58:59
* [打破边界防御思维！AI驱动攻击席卷55国，600台防火墙敲响警钟](https://www.4hou.com/posts/pnEy)
  2026-03-03 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [2026 年 AI + 网络安全产业生态图谱调研正式开启：诚邀行业同仁共建真实、有价值的产业画像](https://www.4hou.com/posts/Bvzo)

  山卡拉
* [APT37黑客组织利用新型恶意软件实现跨网攻击](https://www.4hou.com/posts/mkA3)

  胡金鱼
* [AI 时代中国网络安全产业的五年变局|| 从 “亡羊补牢” 到 “未雨绸缪”，网安技术彻底换打法](https://www.4hou.com/posts/vwNn)

  山卡拉
* [打破边界防御思维！AI驱动攻击席卷55国，600台防火墙敲响警钟](https://www.4hou.com/posts/pnEy)

  山卡拉
* [嘶吼安全产业研究院 | 2026网络安全产业图谱调研启动](https://www.4hou.com/posts/omDL)

  山卡拉
* [国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/l0z1)

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