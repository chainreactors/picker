---
title: 使用eUICC卡片将手机变成eSIM手机
url: https://www.leavesongs.com/THINK/using-euicc-card-to-support-esim.html
source: 离别歌
date: 2024-07-23
fetch_date: 2025-10-06T17:38:26.317267
---

# 使用eUICC卡片将手机变成eSIM手机

* [主页](/)
* 返回

Back to top
Share post

# 使用eUICC卡片将手机变成eSIM手机

phithon

Jul 22, 2024, 10:00 AM

阅读：45680

[心得与体会](/sort/THINK)

[eUICC](/tag/eUICC),
[eSIM](/tag/eSIM)

虽然离开中国已经快三年了，但是我现在仍然在用国内时候购买的国行iPhone 12手机。我在《[2022年欧洲游记](https://www.leavesongs.com/THINK/europe-trip-2022.html)》这篇文章里也提到过，实体sim卡导致我出门旅游很不方便，每次都要提前至少一个月时间在淘宝买到旅游卡，然后海运来新加坡。如果在Shopee上买，时间虽然短一点，但价格会贵很多。

去年10月去印尼bromo火山，我尝试了另一种方案，因为当时在公司申请了一台pixel 4xl测试机，这台机器是支持eSIM的。所以我没有买实体卡，直接网上买的eSIM下载到手机上，然后测试机开热点让我的iPhone 12上网。

结果不知道是因为当时买的eSIM信号太差，还是备用机信号不行，一路上网速极其不稳定，有大量时间完全没网，同行其他人的情况比我好得多。而且测试机开热点耗电很快，两台手机电量损耗X2，最终我就没再尝试过这个方案。

今年接触到eUICC卡片的方案，试用过几次，感觉这就是我这种情况的最优解，也是国内很多想用eSIM卡的人的一种方式，我写篇文章记录一下。

## [第一次尝试：购买5ber卡片](#5ber)

我们平时使用的SIM卡，其正式的名字叫UICC卡（Universal Integrated Circuit Card，通用集成电路卡）。而eUICC指Embedded UICC，嵌入式通用集成电路卡，准确来说eUICC更像一个芯片，正常情况下厂商在制造支持eSIM设备的时候就直接焊接在电路板上，不可拆卸。

但由于中国对于eSIM的管制，很多人想了很多方法让国行手机支持eSIM。比如最早有人拆卸廉价的物联网设备，将里面的eUICC芯片拆解下载想办法转接到手机上使用。

这两年国内有一个很火的eUICC卡片叫5ber，5ber和它的前辈eSIM.me开创了一种新的支持eSIM的方式。他们制造了一种eUICC的白卡，其形状和大小完全和正常SIM卡相同，可以直接插到国行手机里。然后这两个厂商都提供了App，通过App的方式可以将网上购买的eSIM卡下载到这张实体eUICC卡上，最后实现正常使用。

这其中涉及的技术细节我就不介绍了，有兴趣的小伙伴可以查看参考链接中的文章详细了解。

我大概在2022年就知道esim.me了，后来也听说了5ber，但是当时看官网发现这两个厂商都只支持Android设备，于是只能作罢。今年5ber请了很多自媒体做宣传，我才知道其实这张卡并不是只支持Android设备，而是写卡的时候只支持Android设备。如果已经将esim配置写到卡片里以后，卡片就可以正常在iPhone手机里使用了。

于是我就想买一张来，主要在旅游的时候使用。

当时5ber有卖两个版本，Standard和Premium。Standard版只能写卡两次，后续需要付费，Premium则可以无限制写卡，两个价格相差一倍：

[![image.png](/media/attachment/2024/07/21/19857da3-e71f-4a13-a271-985d2372eca9.b064dca196f2.png)](/media/attachment/2024/07/21/19857da3-e71f-4a13-a271-985d2372eca9.png)

按照我的需求，每次出门都得下载新的eSIM卡，对次数有要求，所以我买的Premium版本。实际上后面在了解原理以后，发现完全没必要，十分后悔，这一点后面会说。

拿到手以后，我尝试买了一张马来西亚的Yodoo虚拟运营商的eSIM卡，并用备用Android机安装官方App，把卡下载到5ber上：

[![image.png](/media/attachment/2024/07/21/d7100e59-3453-4f6a-af8c-ec10ef688dc0.d03c4958f212.png)](/media/attachment/2024/07/21/d7100e59-3453-4f6a-af8c-ec10ef688dc0.png)

Yodoo的eSIM卡购买时需要实名认证，但优点是有电话号码。我将其插到iPhone 12上能正常使用，我测试了它可以收到Telegram的短信，但收不到微信的短信，有可能是微信对这个号段做了限制。

## [第二次尝试：购买estk.me卡和读卡器](#estkme)

购买5ber的时候我完全没了解过其中的技术原理，后来经过朋友的介绍，我发现5ber通过App写卡的操作其实是有安全风险的：据说官方App在写卡时会将卡片信息和eSIM信息上传到云端，包括电话号码等。

我们在购买eSIM后，一般会收到一个二维码，正常手机扫码后就可以安装eSIM，而5ber则是使用官方App扫码。其实这个二维码的内容很简单，格式如下：

```
LPA:1${SM-DP+_ADDRESS}${MATCHING_ID}
```

[![image.png](/media/attachment/2024/07/21/5d6332db-b467-4168-8225-42480f072f67.a770368fa920.png)](/media/attachment/2024/07/21/5d6332db-b467-4168-8225-42480f072f67.png)

`SM-DP+_ADDRESS`是一个域名，`MATCHING_ID`是一个id标示符。扫码以后，手机会带上`MATCHING_ID`，去`SM-DP+_ADDRESS`这个域名所在的服务器中下载对应的profile文件，并写入eUICC中。

由于写卡的过程需要下载profile文件，所以是不能断网的，我们无法规避5ber App上传隐私信息的问题。

那么是否有其他方法可以替代5ber App的功能呢？

类似于5ber App这种与eUICC卡片通信的软件被称为LPA（Local Profile Assistant），其借助手机提供的eUICC API接口或者OMAPI （Open Mobile API）接口与卡片通信。这个通信的过程中还涉及到证书的验证，这里不深入研究技术，我们只要知道LPA并不只有5ber的App即可。

我们常用的LPA有：

* [PeterCxy/OpenEUICC](https://gitea.angry.im/PeterCxy/OpenEUICC)
* [estkme-group/lpac](https://github.com/estkme-group/lpac)
* [creamlike1024/EasyLPAC](https://github.com/creamlike1024/EasyLPAC)

所以，只要换用开源的LPA，就可以规避上述隐私问题。但并不是所有LPA都可以用来写5ber的卡，LPA还需要使用5ber卡片支持的证书。

我在学习的过程中发现eSTK.me推出的卡，这也是一个eUICC卡片，但相比于5ber有几个优势：

* 包含更多证书id，所以支持的LPA更多
* 支持在iPhone上进行卡片切换和写卡
* 当时购买的时候会送一个读卡器，可以在PC上进行写卡操作

我大概是在今年5月初购买的早期版本eSTK.me卡片，花了200港币。我之所以购买第二个eUICC卡，主要是给我老婆用，这样两个人出去旅游就都可以使用eSIM了。

eSTK.me最大的优点就是支持iPhone上进行卡片切换和写卡操作，原理是使用了Applet，也就是所谓的SIM卡应用。我们以前在使用非智能手机的时候安装SIM卡后里面会有自带的一些应用，最简单的就是一些官方的链接等等。

这个功能在iPhone里也存在，eSTK.me就是把切卡和下卡的功能放在了这里面：

[![image.png](/media/attachment/2024/07/21/af88cf09-c854-4496-a7b3-357fe6f73cde.9599e37cb874.png)](/media/attachment/2024/07/21/af88cf09-c854-4496-a7b3-357fe6f73cde.png)

使用SIM卡应用，我们就可以通过远程LPA进行写卡操作。7月份eSTK.me官方也开始发行更便宜的卡片，并通过限制SIM卡应用来收费，如果不使用这个功能，只使用读卡器来写卡和切换卡，完全可以购买低价版本。

使用读卡器+EasyLPAC来写入和管理eSIM卡：

[![image.png](/media/attachment/2024/07/21/589ea3ef-d9e4-42ca-bed4-dcf4c68dd01b.d0ed87232f1a.png)](/media/attachment/2024/07/21/589ea3ef-d9e4-42ca-bed4-dcf4c68dd01b.png)

有趣的是，这个读卡器同样可以用于管理我之前买的5ber卡片。这样一来，就完全解决了我的隐私忧虑，但这也让我买的Premium版本毫无意义，当时如果买便宜的Standard版本，再配合读卡器，就能无限制写卡了，很气。

## [国内和国外的三次实际尝试](#_1)

大部分国内同学购买eUICC卡片的目的是使用国外的eSIM卡，这样可以拥有一个可以在国内接收短信的号码，用于注册国外的各种服务。

我肉身本身就在国外，需求就不是这个了，前面也说了主要是旅游使用。当时购买eSTK.me卡片的时候正好准备回国内出差，就把卡片先寄到了国内的办公室。

卡片装在读卡器上后长这个样：

[![image.png](/media/attachment/2024/07/21/2485a1ea-2474-4eff-9895-9b667cfc6b8c.2923530b2755.png)](/media/attachment/2024/07/21/2485a1ea-2474-4eff-9895-9b667cfc6b8c.png)

我在国内的时候，下载安装了[Airhub](https://www.airhubapp.com/free-esim)的eSIM卡，Airhub提供一个100MB的免费套餐，当时直接下到eSTK.me卡片上在国内就能用了，而且这100MB流量是可以直接翻墙的。我当时查了下IP地址，是一个波兰的IP：

[![image.png](/media/attachment/2024/07/21/50225248-6e8c-4be5-9986-9df96921ef2f.8b27c3072e01.png)](/media/attachment/2024/07/21/50225248-6e8c-4be5-9986-9df96921ef2f.png)

后来回新加坡以后，我和老婆去马来西亚玩了一天，分别买了两个1G的eSIM套餐下到eSTK.me和5ber的卡上。进入马来西亚的时候两张卡都只有2G信号，原因是自动识别到的运营商错误，我们在iPhone上找到Network Selection，取消掉自动选择的按钮，选择自己购买eSIM卡时商家提供的运营商即可。

7月份，我老婆去日本玩了一周多，购买了[esim4travel](https://www.esim4travel.com/?p=esimdb)的eSIM套餐，6美刀5G流量可以用一个月，流量用完了降速到128kbps，可以再充钱增加流量。这一次去日本没有遇到运营商错误的问题。

其实相比于淘宝上的实体卡套餐，eSIM套餐的价格是更贵的，我找了一圈，esim4travel已经属于最便宜的一档了。大部分便宜的eSIM套餐都是香港运营商的“漫游卡”，而我3月份去日本时，在淘宝专门买的日本本地运营商软银的实体卡，这张卡甚至比eSIM卡更便宜。

如果大家也有旅游的需求，我推荐一个eSIM聚合的网站：<https://esimdb.com/>。你输入你要去的目的地，它就会帮你列出很多可以使用的eSIM套餐，然后你可以比价，最后选择最便宜的跳转到官方进行购买。

如果平时旅游比较多，也可以购买类似于[3hk diy](https://www.three.com.hk/prepaid/DIY/en/offer/travel)这样的包年eSIM套餐，亚太地区365天12G流量268港币，这样就不用每次出门都购买新的卡了。

## [提供境外电话号码的运营商](#_2)

前面也说了，很多同学使用eSIM的需求是拥有一个境外的电话号码可以注册各种服务。但是很多旅游时候购买的eSIM卡是“漫游卡”，是不包含电话号码的。

什么是漫游卡？就比如我上面说的esim4travel和3hk，这些套餐实际运营商来自香港，只不过套餐中的流量支持在旅游目的地使用。在落地目的地以后，开启漫游，就可以上网了。

这类漫游卡上网时IP地址是实际运营商的地址，我不太清楚正常上网时流量是不是也会绕路，比如在日本访问日本网站，流量却从香港绕一圈。但总之是肯定不如本地运营商提供的卡好的，优点是便宜。

有部分国家运营商提供prepaid套餐，是专门针对游客，甚至有些本地人也会使用。除了日本，大部分国家本地运营商提供的prepaid套餐一般是有电话号码的，这类运营商就成了国内人的目标。

我虽然没有这类需求，但也凑热闹买了几个可以低成本保号的eSIM套餐：

* yodoo，马来西亚，申请只花了几块钱人民币，但保号政策好像有点变动现在已经不推荐了
* Ooredoo Qatar，卡塔尔，申请完全免费，保号一年22人民币
* Simyo，荷兰，优点是无需实名，首次申请时充值5欧得12.5欧，保号一年0.5欧，相当于可用12年

当然，如果只是为了海外号码，我觉得完全不需要买eUICC。作为信息安全工作者，很多人都拥有pixel作为备用测试机，pixel 3开始就支持eSIM了，完全使用备用机来接验证码就可以了。

关于eSIM套餐的介绍，youtube上有很多，直接搜索“esim”就行了。很多视频里面都有5ber的广告，可以说5ber就是这群自媒体的衣食父母，但我们只关注内容就行了，至于是否购买eUICC卡片，以及购买哪个eUICC卡片，就自行决定了，我个人是更推荐eSTK.me的。

## [EID白名单限制](#eid)

我推荐eSTK.me的原因，除了上面列出的几个优点以外，还有一个就是这张卡的EID。

EID（eUICC Identifier）是eUICC的全球统一物理标识，类似于网卡的Mac地址。EID存储于卡片中，只能读取不能修改。

有部分国家，比如美国和日本，在购买本地运营商的eSIM套餐时，其SM-DP服务器对于EID有白名单限制。这会导致我们无法将eSIM下载到eUICC卡上。

比如，我查了一下日本的一个叫b-mobile的运营商，其出售的eSIM套餐的[白名单](https://www.bmobile.ne.jp/english/devicesesim.html)如下：

* 89049032～
* 89033023～
* 89033024～
* 89043051～
* 89043052～

只有EID是这5个开头的eUICC卡才能从服务器下载eSIM profile。在下载eSIM profile的时候，服务端会使用证书进行验证，所以这个限制很难通过软件方式绕过。

我查了一下eSTK.me的EID开头是符合这个白名单限制的：

[![image.png](/media/attachment/2024/07/21/d314dd32-c660-407e-828d-837969f88cc5.89d710e2d893.png)](/media/attachment/2024/07/21/d314dd32-c660-407e-828d-837969f88cc5.png)

但5ber的EID不符合这个限制：

[![image.png](/media/attachment/2024/07/21/360dbb25-4af7-43f0-bdc7-0d23082d808f.f3f7542f9c55.png)](/media/attachment/2024/07/21/360dbb25-4af7-43f0-bdc7-0d23082d808f.png)

这也是我推荐eSTK.me的原因。

我们通过这个[网页](https://euicc-manual.osmocom.org/docs/pki/eum/)可以看到不同的EID对应的制造商是什么。可见，eSTK.me的制造商来自德国，5ber的是中国的。

当然，对于EID的限制只存在于下载profile的阶段，如果你发现自己已经成功下载profile到卡里了，就不用再担心EID的限制了，这个卡肯定可以在日本上网。如果真的因为EID的限制无法购买日本本地的eSIM，买我上面说的相关漫游卡就好了，毕竟价格是真的便宜很多。

到这里，我使用eSTK.me和5ber的卡也有两个多月了，出国好几次，完全没有遇到不能使用的问题。另外，有了eUICC卡片以后，我也不那么想换非国行手机了，毕竟双实体sim卡槽其实更加方便。

新加坡的eSIM普及率还不高，很多eSIM套餐都要加钱，如果换本地的手机我就只能将卡装在实体卡槽里，或者必须加钱购买eSIM，否则我国内的手机卡就没位置插了，还不如继续用国行手机。

参考链接：

* 很经典的一篇文章，可以说是奠基之作，必看：<https://iecho.cc/2023/10/20/Convert-eSIM-to-physical-SIM/>
* 合法eUICC CI证书id列表：<https://euicc-manual.osmocom.org/docs/pki/ci/>
* eSTK.me: 下一代可插拔消费者 eSIM 卡：<https://iecho.cc/2024/03/16/estk-me-next-generation-removable-consumer-esim/>
* EID列表：<https://euicc-manual.osmocom.org/docs/pki/eum/>

# 赞赏

喜欢这篇文章？打赏1元

![](/static/wx.jpg)

# 评论

![](/static/placeholder.jpg)

老李

Jul 08, 2025, 9:51 PM
回复

大佬我有安卓备用机是不是可以不买读卡器啊

![](https://secure.gravatar.com/avatar/c4267eb6d17276fa31c547ac71611e90.jpg?s=100&d=mm&...