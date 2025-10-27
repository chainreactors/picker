---
title: 新的SophosEncrypt勒索软件冒充知名网络安全公司Sophos
url: https://www.4hou.com/posts/8zWj
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-06
fetch_date: 2025-10-04T11:58:41.249487
---

# 新的SophosEncrypt勒索软件冒充知名网络安全公司Sophos

新的SophosEncrypt勒索软件冒充知名网络安全公司Sophos - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的SophosEncrypt勒索软件冒充知名网络安全公司Sophos

布加迪
[新闻](https://www.4hou.com/category/news)
2023-08-05 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)126825

收藏

导语：网络安全供应商Sophos近日被一种名为SophosEncrypt的新型勒索软件即服务冒充，威胁分子打着这家公司的旗号实施攻击活动。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118319100136.png "1689820557647700.png")

网络安全供应商Sophos近日被一种名为SophosEncrypt的新型勒索软件即服务冒充，威胁分子打着这家公司的旗号实施攻击活动。

MalwareHunterTeam昨天发现了这个勒索软件，起初还以为是Sophos红队演习的一部分。

然而，Sophos X-Ops团队在推特上表示，他们并没有创建这个加密器，他们在调查其相关情况。

Sophos发推文声称：“我们早些时候在VT上发现了这个勒索软件，一直在调查。我们的初步调查结果显示，Sophos InterceptX可以抵御这些勒索软件样本。”

此外，ID Ransomware显示了来自被感染受害者的一份提交，表明这起勒索软件即服务活动处于活跃状态。

虽然目前对RaaS活动及推广方式知之甚少，但MalwareHunterTeam发现了一个加密器的样本，让我们可以快速了解它是如何运作的。

**SophosEncrypt勒索软件**

勒索软件加密器是用Rust编写的，使用C:\Users\Dubinin\路径作为其crate。在内部，勒索软件被命名为“sophos\_encrypt”，因此它被称为SophosEncrypt，检测结果已经被添加到了ID Ransomware中。

一旦执行，加密器提示勒索软件加盟组织输入与受害者相关的令牌，该令牌可能最初从勒索软件的管理面板中获取。

输入令牌后，加密器将连接到179.43.154.137:21119，并验证令牌是否有效。勒索软件专家Michael Gillespie发现，可以通过禁用网卡来绕过这道验证，从而实际上在离线状态下运行加密器。

输入有效的令牌后，加密器将提示勒索软件加盟组织在加密设备时使用额外的信息。这些信息包括联系邮箱、jabber地址和一个32个字符的密码，Gillespie称该密码作为加密算法的一部分来使用。

然后，加密器将提示加盟组织加密一个文件或加密整个设备，如下所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118319275334.png "1689820576127168.png")

图1. 加密器在加密前提示信息（图片来源：BleepingComputer）

在加密文件时，Gillespie告诉IT外媒，它使用带PKCS# 7填充的AES256-CBC加密。

每个加密过的文件都会有已输入的令牌、已输入的电子邮件以及以.[[]].[[]].sophos这种格式添加到文件名后面的sophos扩展名。下面是测试加密中的情况。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118320106774.png "1689820591199187.png")

图2. SophosEncrypt加密的文件（图片来源：BleepingComputer）

在文件被加密的每个文件夹中，勒索软件将创建一封名为information.hta的勒索函，加密完成后它可自动开启。

这封勒索函含有受害者的文件发生了什么，以及加盟组织在加密设备之前输入的联系信息。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118320355077.png "1689820605235635.png")

图3. SophosEncrypt勒索函（图片来源：BleepingComputer）

勒索软件还能够改变Windows桌面壁纸，当前壁纸醒目地显示它所冒充的“Sophos”品牌。

需要澄清的是，这张壁纸是由威胁分子创建的，与正规的Sophos网络安全公司没有一点关系。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118320570447.png "1689820619408205.png")

图4. SophosEncrypt壁纸（图片来源：BleepingComputer）

加密器包含许多对位于http://xnfz2jv5fk6dbvrsxxf3dloi6by3agwtur2fauydd3hwdk4vmm27k7ad.onion的Tor网站用。

这个Tor网站不是谈判或数据泄露网站，更像是勒索软件即服务活动的加盟组织面板。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230804/1691118321168318.png "1689820634165037.png")

图5. 勒索软件即服务加盟组织面板（图片来源：BleepingComputer）

研究人员仍在分析SophosEncrypt，看看是否有任何漏洞可以免费恢复文件。

如果发现任何弱点或加密问题，我们会发布本文的更新内容。

在文章报道发表后，Sophos也发布了一份关于新的SophosEncrypt勒索软件的报告。

据报告显示，勒索软件团伙的指挥和控制服务器（179.43.154.137）也与之前攻击中使用的Cobalt Strike C2服务器有关。

Sophos的报告解释：“此外，两个样本都含有一个硬编码的IP地址（我们确实看到样本连接到这样一个地址）。”

“一年多来，这个地址一直与Cobalt Strike指挥和控制以及自动攻击有关，这些攻击试图用加密货币挖掘软件感染面向互联网的计算机。”

本文翻译自：https://www.bleepingcomputer.com/news/security/cybersecurity-firm-sophos-impersonated-by-new-sophosencrypt-ransomware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?czFBWXHs)

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