---
title: ESD K9电子搜检汪汪队
url: https://www.4hou.com/posts/vwom
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-13
fetch_date: 2025-10-06T18:03:41.526291
---

# ESD K9电子搜检汪汪队

ESD K9电子搜检汪汪队 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# ESD K9电子搜检汪汪队

RC2反窃密实验室
[技术](https://www.4hou.com/category/technology)
2024-08-12 14:49:24

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)56462

收藏

导语：ESD K-9 电子存储设备搜检汪汪队~~

******篇首语：******很多部门都在思考如何使用低技术手段来解决高科技犯罪，反窃密行业同样如此。

嗯，总有些另辟蹊径的思路，比如今天要介绍的是，可以帮小姐姐查针孔偷拍的：**ESD K-9 电子存储设备搜检汪汪队**~~

**小贴士：****K-9**这个词源于英文单词Canine，原意指犬科动物，**K9**其实指的就是警犬或者是军犬，这个词最先流行于美国的警犬部门，现在已被广泛接受~~

大家在机场见过防爆和缉毒的狗狗吧？

![1.1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980927110387.jpg "1721980118127200.jpg")

**声明：****以下内容符合****OSINT国际开源情报搜集定义****，不涉及任何非法行为，仅供交流与参考。**

**01 为什么要**搜检**电子存储设备？**

在现代社会，针对未成年人的互联网犯罪，包括创建和传播未成年人色情制品、儿童性奴、未成年人性侵犯和性虐待的直播等等。近些年，这类犯罪正在以惊人的速度增加。

这些疑犯通常的做法是将其对话信息、图片、视频和其他联系信息都保存在外部存储设备（例如硬盘、U盘、Micro SD卡等）并藏匿，这对执法人员的搜查工作制造了很大难题。

![1.2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980928343739.jpg "1721980214684443.jpg")

来自美国计算机犯罪部门的警官表示：

在搜查令期间，通常会要求执法人员查找与这些罪行有关的实物证据。这些证据对于识别受害者，并将这些嫌疑人从社区中驱逐及逮捕至关重要。

但当他们依法执行搜查工作时，由于电子存储设备通常很小，容易隐藏，所以虽然搜查工作通常要花费数小时，但总会疏漏些电子物证，甚至有些设备可能永远都找不到。

**而每个未发现的设备，都可能是一个或多个身份不明的受害者的血泪证据。**

这些被称为数字媒体电子存储设备（**DMESD**），包括笔记本硬盘、小型U盘、TF卡、SD 卡、Micro SD卡、智能手机以及许多其他存储设备。要知道，不到一毫米厚的微型microSD卡里，可以容纳100GB的各种数据。

![1.3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980928146927.jpg "1721980253671354.jpg")

**02 ESD狗狗是如何训练的**

时针拨回到2012年，康涅狄格州**K9**小组警官被上级召见，后者询问是否有可能训练警犬来定位计算机硬盘驱动器之类的设备。

于是，**K9**小组邀请了科学服务部法医实验室的化学家杰克·哈伯（Jack Hubball）博士参与。

Hubball第一反应是怀疑，但鉴于他已经在缉毒和排爆部门工作30多年，对狗狗的能力非常了解，这些履历又让他对产生了信心。

Hubball仔细检查了硬盘、U盘、SD卡等所有电子存储设备，并开始测试各种电路元器件。

![1.4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980929320991.jpg "1721980295558224.jpg")

大约六个月后，他发现了一种名为三苯基膦氧化物（**TPPO**）的化合物，从大容量硬盘到microSD卡的所有存储设备中的电路板中都出现该化合物，其作用是防止它们过热。

同时，也成功地从可移动介质（如CD、DVD、磁带甚至软盘）中提取了另一种化合物：羟基环己基苯基酮（**HPK**）。

**小贴士：**

杨叔搜了一下，以下中英文供行业人士参考：

> 中文：三苯基氧化膦
>
> 英文：Triphenyl PhosPhine Oxide
>
> 中文：羟基环己基苯基酮
>
> 英文：Hydroxycyclohexyl Phenyl Ketone

至此，有了关键的化学“**钥匙**”，**K9**中心开始训练两只拉布拉多犬作为**ESD**狗狗，**ESD**即**Electronics Storage Detection K-9，**有时也简称为**：Electronic Detection K-9**。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980929422261.png "1721980340205194.png")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980930504408.jpg "1721980345182041.jpg")

在成功完成培训后，其中一只名叫Selma的，开始与康涅狄格州警察计算机犯罪部门合作。

直到2015年底，Selma已经处理了100多个案件，主要涉及儿童色情作品，还涉及凶杀、假释遵守工作和黑客案件。

Selma强大的嗅觉协助执法部门找出了隐藏在垃圾桶、通风口和散热器中的小型存储设备。

![1.7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980930108172.jpg "1721980428941545.jpg")

2015年，另一只名叫Bear的**ESD**狗狗，在参与的首次现场勘查中，就发现了调查人员错过的一部手机。

Bear在西雅图的第一年，协助了56份搜查令，并在现场搜索中，成功地找出16个被警员物理搜查中完全遗漏掉的设备。

而在整个华盛顿州的搜索任务中，Bear成功地在咖啡罐、特百惠厨房用品以及成堆的垃圾中找出了小型存储设备。

![1.8.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980930213084.jpg "1721980461115709.jpg")

于是，**ESD K9**在执法圈里被传颂开来~

**03 来自一线的反馈**

2016年，仅仅是Jordan Detection K9训练中心就培训了六只**ESD**狗狗，这些优秀的狗狗们被立即送往全美多个执法机构的特别**K9**小组里工作。同年，很多**K9**中心都开启了**ESD**训练班。

下图是康涅狄格州警察**K9**中心开设的第一个班里的5只**ESD**狗狗毕业照。

![1.9.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980931224076.jpg "1721980512158271.jpg")

新墨西哥州检察长办公室的特工Iris是Jordan Detection K9中心的毕业犬之一。对，你没看错，这些**ESD**狗狗岗位是特工

2016年在**FBI**的一次搜查中，联邦调查局的特工们确信房间里已经找不到任何东西，但Iris出现后，很快就表示桌子上方抽屉里有东西。

**FBI**特工拉开抽屉，没有看到任何物证。

当他说：“指给我”，Iris把鼻子伸到便签纸上。

这位**FBI**特工有些恼火地认为狗狗在偷懒捣乱，结果当Iris叼起便签纸并将其翻转过来，一个microSD卡掉了出来。

“Iris很棒，她是对的，是我搞错了，”现场工作结束后，这位特工说道。

“很多时间我们根本看不见也找不到证据，这些狗狗的作用真的很大。”

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980931168010.jpg "1721980580315633.jpg")

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980932948915.jpg "1721980585672756.jpg")

2017年，康涅狄格州的**K9**中心开设了超过三个**ESD**狗狗训练班。这些狗狗除了参与未成年人色情取证工作及刑事案件外，还将用于反恐。

康涅狄格州甚至接待了来自英国的训犬师，澳大利亚官员也表示有兴趣采购该训练项目。

![1.12.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980932143283.jpg "1721980648639779.jpg")

**04 来自一线的担忧**

一些执法人员的担忧是：

如果科技公司知道这些狗狗正在追踪的化合物类型，他们可能会尝试制造没有含有这类化合物的存储设备。

但Hubbell说，他不认为这种情况会广泛发生。

![1.13.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980932135296.jpg "1721980692197460.jpg")

Hubball说：“目前在电路板上广泛使用的是一种非常便宜的化工品，而且效果非常好，而近些年在大规模制造电路板的材料选择上很难发生重大变化。”

“在这种情况下，因为设备中已经装有这些电路板，所以不太可能掩盖住气味。”

而且，在康涅狄格州警察局法医实验室，Hubball正在努力提升狗的最低可检测极限。

他说：“我们已经降低到非常低的百万分之一水平，而现在我们将致力于更高的十亿分之一的**TPPO**水平。”

他说，到目前为止，这些狗狗甚至可以检测到微量的化合物。

![1.14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980933102896.png "1721980763306209.png")

**05 TSCM反窃密领域的应用**

同样地，在各种刑事以及商业间谍案件中，对于电子存储设备的搜查愈发重要。

到2020年底，仅仅Jordan Detection K9中心就已训练了超30只**ESD**及20只毒品侦查犬，有力地支援了一线各个部门的需求。

![1.15.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980933181405.jpg "1721980796457209.jpg")

现在，经过几年的实战证明，**ESD K-9**对物理搜查至关重要，因为电子存储设备确实很容易被人眼忽略，尤其是当隐藏在墙体裂缝、衣服、天花板或扔进盒子、脏衣服甚至垃圾中。

![](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980934178129.jpg "1721980832947421.jpg")

![1.17.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980934210253.jpg "1721980900811981.jpg")

从某种程度上而言，**ESD K-9****的能力超过了专业检测设备，哈哈~**

目前国外有好几个社区型**K9**团队，都是自发训练狗狗开始查找微型电子设备，据说前不久成功地找到了针孔偷拍器材！

What？以后出门还买啥反偷拍装备，带上自家狗狗不就行了

![1.18.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240726/1721980937545573.jpg "1721980937545573.jpg")

不过，虽然说**ESD K-9**小组里确实有很多家犬品种的身影，比如拉布拉多等，但对于二哈这样的狗，杨叔个人表示怀疑，这货不会趁机把房间撕碎了吧？

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?WeDPmghs)

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

![](https://img.4hou.com/portraits/182735b0219b1d7a63869aa0c554f245.png)

# [RC2反窃密实验室](https://www.4hou.com/member/33jn)

专注TSCM，物理安全和隐私保护~

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS...