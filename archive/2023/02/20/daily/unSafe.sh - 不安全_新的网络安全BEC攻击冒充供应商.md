---
title: 新的网络安全BEC攻击冒充供应商
url: https://buaq.net/go-150042.html
source: unSafe.sh - 不安全
date: 2023-02-20
fetch_date: 2025-10-04T07:32:17.777231
---

# 新的网络安全BEC攻击冒充供应商

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/20a8eb6b112a1722d1e9e961dc3550dc.jpg)

新的网络安全BEC攻击冒充供应商

导语：一伙新的商业电子邮件攻击威胁分子正在
*2023-2-19 12:0:0
Author: [www.4hou.com(查看原文)](/jump-150042.htm)
阅读量:16
收藏*

---

导语：一伙新的商业电子邮件攻击威胁分子正在使用一种隐蔽策略，以避免像典型的社会工程攻击那样泄露踪迹。读者可以通过本文了解保护贵公司的最佳防御方法。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230217/1676616922120083.png "1675492861940585.png")

金融行业供应链攻击是商业电子邮件攻击（BEC）下面的一个子类，其手段似乎非常有效，似乎越来越猖獗。Abnormal Security近日发现了一伙恶意威胁分子——它称之为Firebrick Ostrich，该团伙使用金融供应链攻击这种花招来诱骗目标进行支付。

这家安全公司此前已发现了四种金融供应链攻击，这几种攻击不需要冒充目标公司的内部高管，而是冒充目标公司的其中一家供应商。Abnormal Security表示，Firebrick Ostrich使用了其中一种类型的金融供应链攻击：第三方侦察攻击，实施了346起BEC攻击活动（最早可以追溯到2021年4月），冒充151家组织，并使用212个恶意注册的域名，几乎全部在美国境内。

Abnormal Security的威胁情报主管Crane Hassold表示，通过冒充外部第三方骗取的资金比传统的BEC攻击手法多出三倍。攻击能够得逞，源于受害者缺乏安全意识，因为许多公司及员工接受培训后只懂得寻找冒充内部高管的邮件，而不是冒充供应商的邮件。

他说：“此外，如果你仔细观察第三方侦察及其他金融供应链攻击，就会发现诱骗的有效性取决于他们能够在邮件中添加的信息量——这些信息使它们看起来比其他形式的BEC更为逼真。”

Hassold特别指出，每年因BEC而造成的损失高达数百亿美元；BEC是自2016年以来企业蒙受经济损失的主要原因。

他说：“由于攻击者冒充外部实体，BEC在去年上半年真正呈井喷之势，达到了高峰。这是一个很大的变化，因为自BEC问世以来，其手段主要是冒充内部实体。BEC攻击者已将第三方（包括供应商）视为整条链中的薄弱一环。”

**靠技术含量低的冒充手段大捞一把**

据Hassold声称，从网络犯罪这门行当的角度来看，发起第三方侦察攻击所需的开销很低。只需要基本的侦察和信息收集，不需要底层基础设施或开发人员来维护和改进恶意软件。只需要发送电子邮件，所以从开销角度来看，这非常有利可图。

据Abnormal声称，冒充第三方的攻击（主要源自西非）使用了分三步走的过程（图A）。

![2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230217/1676616923804921.jpeg "1675492883813042.jpeg")

图A：第三方侦察攻击的三个步骤是1）进行开源研究，2）搭建攻击基础设施，3）向客户发送针对性的电子邮件（图片来源：Abnormal Security）。

1. 对供应商客户关系进行开源研究，信息可能来自州和地方政府（提供有关新旧合同的详细信息），也可能来自供应商网站（供应商在网站上显示了客户的名称或标志），甚至可以上网搜索公司名称以查看可能的联系信息。

2. 搭建攻击基础设施：威胁团伙注册一个域，使用Namecheap或谷歌作为注册机构以冒充供应商的域，然后欺骗这家供应商的应付账款员工的电子邮件地址。

3. 向客户发送针对性的电子邮件：攻击者向供应商的客户发送电子邮件，询问潜在的未付发票或提供更新后的账户信息（以便接收将来支付的款项）。

**注册域名一周内攻击**

据Abnormal Security声称，Firebrick Ostrich使用新注册的域名恰恰表明，新注册域名结合其他行为指标是识别威胁的有效信号。Abnormal Security声称，Firebrick Ostrich注册的域名中60%是在实施使用了这些域名的BEC活动的当天注册的；大约四分之三的域名是在攻击后48小时内获得的，89%的域名是在攻击后一周内注册的。

Firebrick Ostrich使用新注册的域名，创建电子邮件地址，冒充实际的供应商账户管理人员，然后趁机为攻击提供便利，主账户通过模仿供应商的实际应收账款专员与攻击目标进行联系。辅助性的电子邮件账户可能包括供应商的财务高管，为攻击增加了一层真实性。

**“合理”的请求和长远策略**

Abnormal Security的报告称，Firebrick Ostrich攻击中的初始电子邮件通常以问候开头，比如供应商“非常感谢您这个重要客户，我们感谢您的持续合作”，后面可能跟有两个请求：

第一个请求表明供应商希望想要更新保存在客户处的银行账户。邮件特意提到了供应商无法通过支票收款，于是ACH和电汇支付是唯一的两个选择。

第二个请求查询应付给供应商的任何未付款项。邮件声称，由于供应商的会计团队无法审核账户，供应商因而无法跟踪已开的发票。Firebrick Ostrich在一封电子邮件中提供了更多细节，声称账户团队“无法进入到服务器或无法进入到Oracle系统，以审查账户或公布已收到的付款。”

Hassold说：“我们发现，在许多第三方侦察攻击中，谎称遇到技术问题是一个常见的借口，以解释为什么供应商无法访问自己的发票库存，但邮件开头先奉承收件人似乎是这个BEC团伙所特有的。”

另一种策略特别隐秘，因为它不要求当前发票付款，而只是要求更新供应商存储的银行账户资料，以便将来的任何付款都可以转入到这个新账户。Abnormal Security表示，这避开了应付账款专员接受过培训后可能会留意到的危险信号。得到下一笔发票款项的将是威胁分子，而不是实际供应商。

这个团伙的独特之处在于，即使不需要攻陷帐户，也不需要深入研究供应商与客户的关系，他们照样大获成功。据Abnormal Security声称，只需使用相当明显的社会工程伎俩，威胁团伙就能发现开展成功的BEC活动所需要的一切，不需要往初始研究上投入大量的时间或资源。

**最佳防御是全面筛查**

Hassold表示，可识别静态攻击指标的电子邮件标记技术不足以防御BEC攻击；他推荐采用一种更全面的防御方法，使用行为分析等技术来了解发件人和收件人之间的关系。这种全面策略还包含关于目标公司的第三方供应商生态系统的信息，并密切关注欺骗供应商的特定的冒充攻击以及可疑的语言和线索。

他说：“了解整个网络威胁领域所出现的趋势，并确保员工们意识到这些趋势，这一点至关重要。这意味着，当他们看到请求账户更改或咨询技术问题之类邮件的类似Firebrick Ostrich的攻击时，他们已经有了内部策略，在实际更改之前就已经向供应商线下验证了这些请求。我们认为网络攻击错综复杂，但归根结底，绝大多数网络攻击只不过是社会工程伎俩，企图操纵人类行为——让人们做一些他们原本不会做的事情。”

本文翻译自：https://www.techrepublic.com/article/cybersecurity-bec-attack-mimics-vendors/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?Mcf6NIyZ)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/1676090032121551.jpeg)

  工业无线物联网解决方案中的缺陷可让攻击者深入访问 OT 网络](https://www.4hou.com/posts/ykqP)
* [![](https://img.4hou.com/images/1675492861940585.png)

  新的网络安全BEC攻击冒充供应商](https://www.4hou.com/posts/QLP0)
* [![](https://img.4hou.com/images/2_副本.png)

  嘶吼安全产业研究院参与编写 | 《2022年工业信息安全态势报告》正式发布](https://www.4hou.com/posts/VZwW)
* [![](https://img.4hou.com/images/1676165837113822.png)

  Enigma、Vector和TgToxic：加密货币用户面临的新威胁](https://www.4hou.com/posts/JX4P)
* [![](https://img.4hou.com/images/1675803288122360.png)

  半导体设备制造商MKS Instruments成为勒索软件攻击的受害者](https://www.4hou.com/posts/mXD9)
* [![](https://img.4hou.com/images/221.webp)

  犯罪分子使用谷歌广告针对Bitwarden密码库进行攻击](https://www.4hou.com/posts/oJwB)

![]()

文章来源: https://www.4hou.com/posts/QLP0
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)