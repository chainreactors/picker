---
title: 如何揪出贵企业网络中的Cl0p勒索软件？
url: https://www.4hou.com/posts/YYVY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-03
fetch_date: 2025-10-04T11:52:32.938722
---

# 如何揪出贵企业网络中的Cl0p勒索软件？

如何揪出贵企业网络中的Cl0p勒索软件？ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 如何揪出贵企业网络中的Cl0p勒索软件？

布加迪
[话题](https://www.4hou.com/category/attitude)
2023-07-02 11:33:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)2067468

收藏

导语：专家表示，在攻击者部署恶意载荷之前，被黑客组织用Cl0p勒索软件盯上的公司通常有数次机会来揪出攻击。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230628/1687906166154592.png "1687906166154592.png")

通过MOVEit管理文件传输平台的三个零日漏洞针对公司企业和政府机构的广泛攻击使Cl0p勒索软件组织臭名昭著。

受影响的数据还在不断增加，包括数百万投资加州公务员退休基金（CalPERS）的员工的个人数据、BBC和英国航空公司超过10万名员工的雇员信息、美国能源部的敏感数据以及加拿大新斯科舍省公民的个人信息。

网络安全和合规服务公司Exabeam的安全研究主管Steve Povolny表示，这次攻击的广泛影响充分说明了该勒索软件组织具有的技术能力。

他说：“我看到出现在这些大型威胁组织、尤其是勒索软件组织身上的转变是，他们资金充足，资源充足，拥有庞大的组织，他们不再只是在GitHub上找零日漏洞了。这些都是精心策划的攻击，一开始悄无声息，随后突然爆发出来。”

由于战术发生变化，确定指明任何攻击背后攻击者的技术指标总是很棘手。以下指标为组织提供了一个起点，以调查Cl0p组织是否利用了MOVEit文件传输实用程序中的漏洞、是否可能潜伏在网络中。

**MOVEit攻击：“Human2”指纹**

Cl0p背后的组织利用了文件传输服务中的许多漏洞，比如1月份的GoAnywhere MFT （CVE-2023-0669）和5月底6月初的MOVEit管理文件传输平台（CVE-2023-34362）。

最初，攻击者安装了一个名为LEMURLOOT的Web shell，使用的名称是“human2”，并使用通过HTTP请求发送的命令，标头字段设置为“X-siLock-Comment”。来自网络安全和基础设施安全局（CISA）的公告还包括用于检测MOVEit漏洞的四条YARA规则。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230628/1687906192503494.png "1687906192503494.png")

图1. 用于检测MOVEit攻击的YARA规则（图片来源：CISA公告）

这起攻击还在关联数据库中留下管理员帐户以实现持久化，即使Web服务器已经全面重新安装，攻击者也可以恢复其攻击。据CrowdStrike声称，“activesessions”数据库中Timeout =“9999”的会话或User数据库中Permission =“30”和Deleted =“0”的用户可能表明攻击者活动。

然而MOVEit攻击的一个特点是，它通常不会留下多少技术指标。漏洞管理公司Rapid7的安全经理Caitlin Condon表示，Cl0p对MOVEit管理文件传输软件的攻击取得了大范围的成功，而且很难找到攻陷指标，这表明产品供应商需要花更大的精力来确保对取证分析有用的日志记录是可用的。

日志记录里面有很多蛛丝马迹，有很多东西可以跟踪。许多公司在竭力修复漏洞和根除威胁分子的访问时，常常完全删除应用程序，这也将删除证据。

**Cl0p勒索软件的迹象**

在攻击过程中的某个时刻，Cl0p组织可能会部署同名的勒索软件。最初，恶意软件是通过网络钓鱼攻击安装的，但越来越多的攻击针对大型组织，常常利用文件传输或管理软件中新的或最近的漏洞。

该勒索软件组织通常使用合法的代码签名证书来逃避安全软件的检测。比如说，据Pal Alto Networks发布的技术公告显示，在过去，Cl0p勒索软件安装程序使用Corsair软件解决方案公司日期标为2021年2月12日星期五的证书，或者使用Insite软件公司日期标为2020年12月25日星期五的证书。

攻击者还会停止多个系统进程，包括属于备份程序和安全解决方案的进程。

在执行之后，Cl0p勒索软件将各种扩展名附加到受害者的文件中，包括.clop、.CIIp、.Cllp和.C\_L\_O\_P。理想情况下，公司企业希望在文件被解密之前检测到勒索软件。

据网络威胁专家声称，与任何技术指标一样，静态签名用途有限，因为攻击者常常会定制其方法，以绕过基于固定规则的检测。

**其他迹象：Truebot和Raspberry Robin**

Cl0p组织的其他常见技术指标是他们用来扩展攻击的辅助工具，或者他们获得初始访问权限的替代方法。

比如说，Truebot下载程序是一种流行的中间恶意载荷，常常导致Cl0p感染，并与Silence组织相关联。据思科Talos部门的分析显示，Truebot常常会导致安装Cobalt Strike及/或Grace下载程序恶意软件。还经常使用一种名为Teleport的自定义工具，用于泄露数据。

据微软声称，Silence使用了一种通过USB驱动器传播的蠕虫病毒：Raspberry Robin，有时也会通过第三方按安装付费服务来传播。微软如今将该组织归类为Lace Tempest。截至今年4月，微软特别指出，近1000家组织的近3000个设备感染了Raspberry Robin，随后没多久就感染了Truebot及/或Cobalt Strike，因为Lace Tempest试图攻击更多的系统。

据微软声称，可以使用组策略或注册表设置来阻止插入USB驱动器时自动运行或执行代码，从而阻止Raspberry Robin感染。

NCC Group旗下FOX-IT安全服务部门的高级威胁情报分析师Mike Stokkel表示，最后，企业应该时刻留意大量数据正在被泄露的迹象，尤其是被泄露到已知由Cl0p组织使用的基础设施。

标准的安全措施已经可以提供帮助，比如在MOVEit系统或GoAnywhere系统的文件传输应用程序上部署[端点检测和响应]解决方案。使用网络传感器和跟踪出站网络流量也有所帮助。如果看到600 GB的数据流出贵企业的网络，这相当异常。

本文翻译自：https://www.darkreading.com/dr-tech/cl0p-in-your-network-how-to-find-out如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?KcUh4xbx)

#### 你可能感兴趣的

* [![]()

  塑造网络安全行业未来格局的九大技术趋势](https://www.4hou.com/posts/4vqn)
* [![]()

  容易成为勒索软件攻击目标的13个行业](https://www.4hou.com/posts/m0Vr)
* [![]()

  如何揪出贵企业网络中的Cl0p勒索软件？](https://www.4hou.com/posts/YYVY)
* [![]()

  企业应重视员工使用 ChatGPT 带来的安全风险](https://www.4hou.com/posts/9Xlx)
* [![]()

  知道手机投屏可以看剧，不知道还能被用来窃取隐私！](https://www.4hou.com/posts/XVvo)
* [![]()

  披露！币圈空投黑吃黑“脏”手段，“偷家”这招儿真有你的](https://www.4hou.com/posts/2JMM)

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [塑造网络安全行业未来格局的九大技术趋势](https://www.4hou.com/posts/4vqn)
  2023-09-15 12:33:00
* [容易成为勒索软件攻击目标的13个行业](https://www.4hou.com/posts/m0Vr)
  2023-09-14 11:40:00
* [如何揪出贵企业网络中的Cl0p勒索软件？](https://www.4hou.com/posts/YYVY)
  2023-07-02 11:33:00
* [企业应重视员工使用 ChatGPT 带来的安全风险](https://www.4hou.com/posts/9Xlx)
  2023-03-30 11:00:00

[查看更多](https://www.4hou.com/member/VGrO)

# 相关热文

* [塑造网络安全行业未来格局的九大技术趋势](https://www.4hou.com/posts/4vqn)

  布加迪
* [容易成为勒索软件攻击目标的13个行业](https://www.4hou.com/posts/m0Vr)

  小二郎
* [如何揪出贵企业网络中的Cl0p勒索软件？](https://www.4hou.com/posts/YYVY)

  布加迪
* [企业应重视员工使用 ChatGPT 带来的安全风险](https://www.4hou.com/posts/9Xlx)

  丝绸之路
* [知道手机投屏可以看剧，不知道还能被用来窃取隐私！](https://www.4hou.com/posts/XVvo)

  360反诈中心
* [披露！币圈空投黑吃黑“脏”手段，“偷家”这招儿真有你的](https://www.4hou.com/posts/2JMM)

  360反诈中心

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