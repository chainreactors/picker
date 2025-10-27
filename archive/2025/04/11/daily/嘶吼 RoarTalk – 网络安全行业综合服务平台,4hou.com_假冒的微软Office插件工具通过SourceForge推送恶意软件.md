---
title: 假冒的微软Office插件工具通过SourceForge推送恶意软件
url: https://www.4hou.com/posts/omPX
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-11
fetch_date: 2025-10-06T22:02:46.288635
---

# 假冒的微软Office插件工具通过SourceForge推送恶意软件

假冒的微软Office插件工具通过SourceForge推送恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 假冒的微软Office插件工具通过SourceForge推送恶意软件

胡金鱼
[技术](https://www.4hou.com/category/technology)
2025-04-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)58896

收藏

导语：尽管恶意项目已不在 SourceForge 上，但卡巴斯基表示，该项目已被搜索引擎收录，吸引了搜索“办公插件”或类似内容的用户访问。

据了解，威胁者正在滥用 SourceForge 分发假冒的微软插件，这些插件会在受害者的电脑上安装恶意软件，以同时挖掘和窃取加密货币。

SourceForge.net 是一个合法的软件托管和分发平台，还支持版本控制、错误跟踪以及专门的论坛/维基，因此在开源项目社区中非常受欢迎。

尽管其开放的项目提交模式为恶意行为留下了很大的空间，但实际上通过它传播恶意软件的情况却极为罕见。

卡巴斯基发现的新一轮攻击已影响到超过 4604 台系统，其中大部分位于俄罗斯。

尽管恶意项目已不在 SourceForge 上，但卡巴斯基表示，该项目已被搜索引擎收录，吸引了搜索“办公插件”或类似内容的用户访问。

![search.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250409/1744169350147224.png "1744169145434303.png")

源代码托管网站 SourceForge 上的恶意软件出现在搜索结果中

**假冒Office插件**

“officepackage”项目是一个Office插件开发工具的集合，其描述和文件是GitHub上合法的微软项目“Office- addin - scripts”的副本。

![miner-clipbanker-EN1.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250409/1744169351110565.png "1744169211113172.png")

恶意项目（左）和合法工具（右）

然而，当用户在谷歌search（和其他引擎）上搜索office插件时，他们得到的结果指向“officpackage .sourceforge”。由SourceForge提供给项目所有者的单独的web托管功能提供支持。

该页面模仿了一个合法的开发者工具页面，显示了“Office插件”和“下载”按钮。如果单击任何一个，受害者将收到一个包含密码保护的归档文件（installer.zip）和带有密码的文本文件的ZIP文件。

![site.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250409/1744169352341078.png "1744169270542982.png")

散布恶意软件的网站

该归档文件包含一个MSI文件（installer.msi），其大小膨胀到700MB，以逃避AV扫描。运行它会删除‘UnRAR.exe’和‘51654.rar ’，并执行一个Visual Basic脚本，从GitHub获取批处理脚本（confvk.bat）。

该脚本执行检查，以确定它是否在模拟环境中运行，以及哪些防病毒产品处于活动状态，然后下载另一个批处理脚本（confvz.bat）并解压缩RAR归档文件。

bat脚本通过修改注册表和添加Windows服务来建立持久性。

RAR文件包含一个AutoIT解释器（Input.exe）， Netcat反向shell工具（ShellExperienceHost.exe）和两个有效负载（Icon.dll和Kape.dll）。

![diag.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250409/1744169354447868.png "1744169326223757.png")

完整的感染链

DLL文件是一个加密货币矿工和一个剪刀。前者劫持机器的计算能力，为攻击者的账户挖掘加密货币，后者监控剪贴板上复制的加密货币地址，并将其替换为攻击者控制的地址。

攻击者还通过Telegram API调用接收受感染系统的信息，并可以使用相同的通道向受感染的机器引入额外的有效负载。

这次活动是威胁者利用任何合法平台获得虚假合法性和绕过保护的另一个例子。所以建议用户应从可信的出版商那里下载软件，并在执行之前使用最新的反病毒工具扫描所有下载的文件。

文章翻译自：https://www.bleepingcomputer.com/news/security/fake-microsoft-office-add-in-tools-push-malware-via-sourceforge/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?nAUlzCN0)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

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

[查看更多](https://www.4hou.com/member/BVMN)

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

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)