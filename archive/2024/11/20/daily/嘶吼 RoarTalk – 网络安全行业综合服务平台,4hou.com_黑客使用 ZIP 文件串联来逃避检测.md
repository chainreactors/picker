---
title: 黑客使用 ZIP 文件串联来逃避检测
url: https://www.4hou.com/posts/MX5P
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-20
fetch_date: 2025-10-06T19:15:56.790965
---

# 黑客使用 ZIP 文件串联来逃避检测

黑客使用 ZIP 文件串联来逃避检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客使用 ZIP 文件串联来逃避检测

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-11-19 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)82027

收藏

导语：应谨慎对待附加 ZIP 或其他存档文件类型的电子邮件，并应在关键环境中实施过滤器以阻止相关文件扩展名。

黑客利用 ZIP 文件串联技术以 Windows 计算机为目标，在压缩档案中传递恶意负载，而目前安全解决方案却无法检测到它们。

该技术利用了 ZIP 解析器和存档管理器处理串联 ZIP 文件的不同方法。有安全公司发现了这一新问题，在分析利用虚假发货通知引诱用户的网络钓鱼攻击时，发现了隐藏木马的串联 ZIP 存档。

安全研究人员发现，该附件伪装成 RAR 存档，并且恶意软件利用 AutoIt 脚本语言来自动执行恶意任务。

![phish.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241112/1731383425100528.png "1731383219336092.png")

网络钓鱼电子邮件将特洛伊木马隐藏在串联的 ZIP 文件中

**将恶意软件隐藏在“损坏的”ZIP 中**

攻击的第一阶段是准备阶段，威胁者创建两个或多个单独的 ZIP 存档，并将恶意负载隐藏在其中一个中，剩下的则保留无害的内容。

接下来，通过将一个文件的二进制数据附加到另一个文件，将其内容合并到一个组合的 ZIP 存档中，将单独的文件连接成一个文件。尽管最终结果显示为一个文件，但它包含多个 ZIP 结构，每个结构都有自己的中心目录和结束标记。

![structure.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241112/1731383427127822.png "1731383299213334.png")

ZIP 文件的内部结构

**利用 ZIP 应用程序漏洞**

攻击的下一阶段依赖于 ZIP 解析器如何处理串联档案。安全公司测试了 7zip、WinRAR 和 Windows 文件资源管理器，得到了不同的结果：

**·**7zip 仅读取第一个 ZIP 存档（这可能是良性的），并可能生成有关其他数据的警告，用户可能会错过这些数据

**·**WinRAR 读取并显示这两个 ZIP 结构，显示所有文件，包括隐藏的恶意负载。

**·**Windows 文件资源管理器可能无法打开串联文件，或者如果使用 .RAR 扩展名重命名，则可能仅显示第二个 ZIP 存档。

根据应用程序的行为，威胁者可能会微调他们的攻击，例如将恶意软件隐藏在串联的第一个或第二个 ZIP 存档中。

研究人员在尝试 7Zip 攻击中的恶意存档时还发现，只显示了一个无害的 PDF 文件。不过，使用 Windows 资源管理器打开它会发现恶意可执行文件。

![7zip.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241112/1731383428614824.png "1731383408569968.png")

7zip（上）和 Windows 文件资源管理器（下）打开同一文件

为了防御串联的 ZIP 文件，安全研究人员建议用户和企业用户尽可能使用支持递归解包的安全解决方案。一般来说，应谨慎对待附加 ZIP 或其他存档文件类型的电子邮件，并应在关键环境中实施过滤器以阻止相关文件扩展名。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-now-use-zip-file-concatenation-to-evade-detection/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GKShbIR2)

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