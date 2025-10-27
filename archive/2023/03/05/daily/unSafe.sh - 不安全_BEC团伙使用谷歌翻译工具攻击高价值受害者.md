---
title: BEC团伙使用谷歌翻译工具攻击高价值受害者
url: https://buaq.net/go-151939.html
source: unSafe.sh - 不安全
date: 2023-03-05
fetch_date: 2025-10-04T08:43:17.049792
---

# BEC团伙使用谷歌翻译工具攻击高价值受害者

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

![](https://8aqnet.cdn.bcebos.com/6008452ccc07dcfa9166c93a780449e2.jpg)

BEC团伙使用谷歌翻译工具攻击高价值受害者

导语：威胁团伙广泛研究了攻击目标的职责及其
*2023-3-4 12:0:0
Author: [www.4hou.com(查看原文)](/jump-151939.htm)
阅读量:23
收藏*

---

导语：威胁团伙广泛研究了攻击目标的职责及其与公司首席执行官的关系，创建了以假乱真的伪造电子邮件账户。

![p1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230303/1677813339997324.png "1676551434273873.png")

Abnormal Security安全公司近日发现了两个团伙在使用冒充高管的手段，对全球各地的公司实施商业电子邮件入侵（BEC）。

第一个团伙Midnight Hedgehog（“午夜刺猬”）从事支付欺诈勾当，而第二个团伙Mandarin Capybara实施工资转移攻击。这家安全公司的研究人员特别指出，这两个团伙都实施了采用至少13种不同语言的BEC活动，包括丹麦语、荷兰语、爱沙尼亚语、法语、德语、匈牙利语、意大利语、挪威语、波兰语、葡萄牙语、西班牙语和瑞典语。

Abnormal Security威胁情报主管Crane Hassold在研究文章中写道，虽然攻击多个地区的目标、使用多种语言并不是什么新鲜事，但在过去，这些攻击主要由拥有更庞大预算和更先进资源的复杂组织实施。

随着技术变得更触手可及、成本更低廉，这拉低了攻击的准入壁垒，使威胁分子更容易实施BEC攻击。攻击背后的骗子们使用相同的商业在线服务，许多销售和营销团队依赖这些服务来识别潜在客户，并撰写个性化的通讯内容。他们还使用包括谷歌翻译（Google Translate）在内的自动翻译工具，将恶意电子邮件立即翻译成所需的任何语言。

**Midnight Hedgehog支付诈骗**

Midnight Hedgehog使用冒充高管的手段，通常冒充某家公司的首席执行官，欺骗收件人为虚假服务付款。

威胁分子广泛研究攻击目标的职责及其与首席执行官的关系后，创建以假乱真的伪造电子邮件账户。Abnormal Security表示，通常，该团伙的目标是负责发起公司金融交易的财务经理或高管。

该团伙实施的攻击可以追溯到2021年1月，从托管在Gmail、Yandex、Earthlink和Web.de等各种免费网络邮箱提供商的账户以及该团伙向NameCheap或GoDaddy注册的域名发起攻击。

研究人员特别指出，团伙成员可能住在英国、加拿大、美国和尼日利亚等国家。Midnight Hedgehog在攻击活动中使用了两个版本的初始电子邮件，这些邮件用11种语言写成，包括丹麦语、荷兰语、爱沙尼亚语、法语、德语、匈牙利语、意大利语、挪威语、波兰语、西班牙语和瑞典语。

在第一个版本的电子邮件中，威胁分子冒充首席执行官，紧急要求攻击目标对英国一家公司完成付款。在第二个版本中，冒充者要求攻击目标透露公司银行账户的当前余额，并要求立即完成指定金额的付款。一旦收件人回复该团伙的初始电子邮件，攻击者就提供接收所请求付款的银行账户的详细信息。

据研究人员声称，这些虚假服务的支付金额从1.6万欧元到4.2万欧元不等（约合1.7万美元到4.5万美元）。与Midnight Hedgehog相关的钱骡账户（mule account）大多数位于英国，这证实了该团伙在英国设有实体的证据。Hassold写道：“我们还发现该团伙使用在葡萄牙、德国、法国和意大利的银行开设的钱骡账户。”

**Mandarin Capybara工资转移**

Mandarin Capybara针对人力资源员工发动工资转移攻击，要求他们将高管的直接存款详细信息更改为该团伙控制的另一个账户。该团伙最早的攻击可以追溯到2021年2月。该团伙使用Gmail账户来实施攻击，更新每封电子邮件的显示名称，以模仿被冒充的高管的姓名。

Mandarin Capybara的目标是北美、澳大利亚和欧洲的公司。Abnormal Security特别指出：“我们观察到该团伙以英语攻击美国和澳大利亚的公司、以法语攻击加拿大的公司，以六种语言（包括荷兰语、法语、德语、意大利语、葡萄牙语和西班牙语）攻击欧洲的公司。”

在最初的电子邮件中，攻击者询问他们是否可以更新员工的工资账户。研究人员特别指出：“我们观察到有好多次，该团伙用一种语言发起了BEC活动，然后从同一个电子邮件账户用第二种语言发起了第二次活动。”

在美国，工资转移团伙最常用的银行是Green Dot、GoBank、Sutton Bank和MetaBank，这些银行都与预付卡或移动支付服务相关。Mandarin Capybara在欧洲金融科技机构（包括Revoilut、Saurus、Monese、Bunq和SisalPay）设立了钱骡账户，以便从工资转移攻击中接收资金。

**BEC诈骗仍然是日益严重的威胁**

BEC攻击是目前全球组织面临的成本最高昂的威胁。自2016年以来，BEC攻击一直排在美国联邦调查局（FBI）成本最高昂的网络犯罪活动排行榜的首位。

BEC攻击占2021年网络攻击造成的所有经济损失的三分之一以上，全年损失近24亿美元。在2022年7月至2022年12月期间，BEC攻击猛增了81%。

本文翻译自：https://www.csoonline.com/article/3688429/bec-groups-are-using-google-translate-to-target-high-value-victims.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?8UbKgkX9)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/1676551434273873.png)

  BEC团伙使用谷歌翻译工具攻击高价值受害者](https://www.4hou.com/posts/8YGL)
* [![](https://img.4hou.com/images/微信截图_20230303103353.png)

  勒索软件在2022年影响了200多家政府、教育和医疗组织](https://www.4hou.com/posts/O9rr)
* [![](https://img.4hou.com/images/24c7ce39ad379c8f2191bc56c0ae40b6fade6210.jpg)

  SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据的黑客活动](https://www.4hou.com/posts/r7PK)
* [![](https://img.4hou.com/images/1665271394917273.png)

  回拨网络钓鱼攻击改变社会工程的伎俩](https://www.4hou.com/posts/N1yK)
* [![](https://img.4hou.com/images/1677222214187636.png)

  细述SQL注入攻击杀伤链的七个步骤](https://www.4hou.com/posts/zl1m)
* [![](https://img.4hou.com/images/微信截图_20230224143522.png)

  Hydrochasma：一个前所未见的团伙攻击亚洲的医学检验所和船运公司](https://www.4hou.com/posts/KEPY)

![]()

文章来源: https://www.4hou.com/posts/8YGL
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)