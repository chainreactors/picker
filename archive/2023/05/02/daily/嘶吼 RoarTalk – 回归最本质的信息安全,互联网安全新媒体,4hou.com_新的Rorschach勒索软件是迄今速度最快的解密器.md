---
title: 新的Rorschach勒索软件是迄今速度最快的解密器
url: https://www.4hou.com/posts/QKW7
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-05-02
fetch_date: 2025-10-04T11:36:40.588852
---

# 新的Rorschach勒索软件是迄今速度最快的解密器

新的Rorschach勒索软件是迄今速度最快的解密器 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的Rorschach勒索软件是迄今速度最快的解密器

布加迪
[技术](https://www.4hou.com/category/technology)
2023-05-01 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)113081

收藏

导语：据研究人员的测试结果显示，Rorschach是如今最快速的勒索软件威胁。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230428/1682652238990286.png "1680650279179473.png")

一家总部位于美国的公司遭到网络攻击之后，恶意软件研究人员发现了一种似乎具有“独特技术功能”的新型勒索软件，他们将其命名为Rorschach。

研究人员观察到的功能之一是加密速度：据研究人员的测试结果显示，Rorschach凭此速度成为如今最快速的勒索软件威胁。

分析师们发现，黑客在利用一款威胁检测和事件响应工具存在的弱点之后，在受害者网络上部署了恶意软件。

**Rorschach的细节**

网络安全公司Check Point的研究人员在应对美国一家公司的安全事件时发现，Rorschach是通过Cortex XDR中的签名组件使用DLL侧加载技术部署的，Cortex XDR是知名网络安全公司Palo Alto Networks 的一款扩展检测和响应产品。

攻击者使用Cortex XDR转储服务工具（cy.exe）版本7.3.0.16740来侧加载Rorschach加载器和注入器（winutils.dll），这导致将勒索软件的攻击载荷“config.ini”投放到记事本（Notepad）进程中。

加载器文件具有类似UPX的反分析保护机制，而主攻击载荷通过使用VMProtect软件对部分代码进行虚拟化处理来防止逆向工程和检测。

Check Point声称，Rorschach在Windows域控制器上执行时会创建一个组策略，以传播到域中的其他主机。

在攻陷机器之后，恶意软件会删除四个事件日志（应用程序日志、安全日志、系统日志和Windows Powershell日志），以清除其痕迹。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230428/1682652240170944.png "1680650298104010.png")

图1. 攻击链（图片来源：Check Point）

虽然带有硬编码配置，但Rorschach支持可以扩展功能的命令行参数。

Check Point特别指出，这些选项是隐藏的，如果不对恶意软件进行逆向工程分析，就无法访问。以下是研究人员发现的一些参数：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230428/1682652241136267.png "1680650315134061.png")

图2. Check Point 破解的参数

**Rorschach的加密过程**

只有当受害者的机器用独联体（CIS）之外的语言加以配置时，Rorschach才会开始加密数据。

加密方案结合了curve25519算法和eSTREAM cipher hc-128算法，遵循间歇加密趋势，这意味着它只对文件进行部分加密，从而提高了处理速度。

![4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230428/1682652242211985.jpeg "1680650331213184.jpeg")

图3. Rorschach的加密方案（图片来源：Check Point）

研究人员特别指出，Rorschach 的加密例程表明“通过 I/O完成端口高效地实现线程调度”。

Check Point表示：“此外，为了加快速度，似乎格外重视编译器优化，大部分代码进行了内联处理。所有这些因素使我们认为，我们面对的可能是外面速度最快的勒索软件之一。”

为了了解Rorschach的加密速度有多快，Check Point在一台六核CPU机器上搭建了含有220000个文件的测试环境。

Rorschach花了4.5分钟来加密数据，而被认为最快的勒索软件家族的LockBit v3.0却用了 7 分钟才完成加密。

在锁定系统之后，恶意软件投放一封勒索函，其格式类似Yanlowang勒索软件所用的勒索函。

据研究人员声称，这个恶意软件的以前版本使用了类似DarkSide的勒索函。

Check Point表示，这种相似性可能导致其他研究人员将不同版本的Rorschach误认为是 DarkSide，后者于2021年更名为BlackMatter，并于同年销声匿迹。

![5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230428/1682652243121000.jpeg "1680650343848435.jpeg")

图4. Rorschach投放的最新勒索函（图片来源：Check Point）

BlackMatter的成员后来策划了ALPHV/BlackCat勒索软件行动，该行动于2021年11月启动。

Check Point评估后认为，Rorschach从一些在线泄露的主要勒索软件家族（Babuk、LockBit v2.0和DarkSide）借鉴了更好的功能。

除了自我传播能力外，该恶意软件还“提高了勒索攻击的门槛”。

目前，Rorschach勒索软件的运营商仍然不得而知，也没有什么品牌，这种情况在勒索软件领域很少见。

本文翻译自：https://www.bleepingcomputer.com/news/security/new-rorschach-ransomware-is-the-fastest-encryptor-seen-so-far/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?dt0kS1dc)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/VGrO)

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