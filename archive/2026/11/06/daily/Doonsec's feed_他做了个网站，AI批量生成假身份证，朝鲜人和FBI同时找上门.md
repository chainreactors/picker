---
title: 他做了个网站，AI批量生成假身份证，朝鲜人和FBI同时找上门
url: https://mp.weixin.qq.com/s/2TQsHkfGmkLb6Non381-9A
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:55:38.307094
---

# 他做了个网站，AI批量生成假身份证，朝鲜人和FBI同时找上门

# 他做了个网站，AI批量生成假身份证，朝鲜人和FBI同时找上门

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

几年前，乌克兰小伙Yuriy Nazarenko坐在祖父公寓的书桌前，面前四块电脑屏幕，手里攥着烟和Lay's薯片，一张一张地P假护照。

其中一块屏幕开着Telegram，另一块上摊着护照扫描件，Photoshop窗口铺满了整个显示器。

他放大到几百倍，一个像素一个像素地修。护照上的MRZ码（Machine Readable Zone，机器可读区，就是证件底部那两行密密码码的字符），证件照上别人的脸要合成上去，不同国家护照的尺寸和防伪细节，全得手动对齐。

一张高质量假身份证，他有时候对着电脑折腾超过12小时，整整一周才出一张成品。

当时他以为这就是他的生意。手工活，慢，但精细。后来他建了个网站把流程自动化。再后来生成式AI火了，他把AI也接了进去。

这个网站叫OnlyFake。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDodaSiccop4uCRwxL2TuSJibIiaJuuhNtv3fvrPHkkSJly0tKUVaZsiaCr6zJ11Ciabzz8u1upfPKH6kPx8dRAP8P9SzQJuLgPkCh7k/640?wx_fmt=png)

图1 OnlyFake生成的假驾照效果，证件随意摆放再拍照的逼真感

Yuriy Nazarenko创建了OnlyFake，一个让任何人用AI批量生成逼真假身份证的网站。后来朝鲜IT工人找上了门。

Nazarenko在乌克兰敖德萨郊外长大，父亲在乌克兰国家安全局工作。他打过各种零工，在餐厅当厨师、服务员，在超市理货，还在当地一家电视台做过摄像。

他还运营过一个YouTube游戏频道。做视频封面和缩略图需要大量画图工作，他就这么练出了一手Photoshop。后来他发现网上有人愿意花钱买高质量的身份证扫描件，于是入行做假证。

"当你把一张普通护照放大几百倍，你才会发现它到底有多复杂。"Nazarenko说，"看着就是张塑料卡片，实际上里面塞满了微小的安全特征和设计细节。"

他开始雇程序员帮他自动化制证流程。其中一个黑客"以前专门黑政府网站"。他还雇了设计师，通过私人关系和网上社区招人。

最开始OnlyFake根本没用AI。自动化主要是把重复劳动砍掉：客户填好姓名等个人信息，上传一张照片，网站自动生成一张看起来像扫描件的驾照或护照。

后来Nazarenko的团队建了一个庞大的假证件数据库。他们先自己拍了一堆背景照片，后来"随着神经网络进步，我们开始用AI生成背景"。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDq4iaJODOP9IWUVdaDKCNUia04UkEDAyjF3PLLE1cjLtiakw5y6diaiasvrhV89lWXOiaEyEA5fdcdhR9iboMfbWISQtticPRHKkzUjLX4/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDreKlJH47JQvVfHKl0EYF8iaBIaIuaJc6EQQQQhIgBtDMl8IDpicIN1iad4m4TxuibyjJjC91MGEc1kNdVFC3SVrZZhqWS65LOiaq0A/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDoj1EkgMHZLGWVZqBXL6FAlPlby7Pz9DIEaDBljz9U6eWayxQYpFaO2EDwmiaDetPViaEK4MiakQuCe4XggHctcofRicia9n559lXbg/640?wx_fmt=jpeg)

图2 Nazarenko本人提供的生活照

要生成各种不同国家、不同类型的证件，关键是攒够不同证件的扫描模板。Nazarenko在Telegram上发了一条收购消息：谁有清晰的驾照、护照扫描件，他出钱买，美国证件尤其值钱。

很快他就有了从阿根廷到西班牙的海量假证件模板库，全部喂给了OnlyFake。

网站界面长这样：选国家、选证件类型，填姓名、出生日期、地址、身高体重瞳色，上传一张人脸照片，点一下生成，一张看起来像刚从钱包里掏出来拍的证件照就出来了。

更绝的是，生成的假证件不是光秃秃的扫描件。它会把证件"放"在沙发上、地毯上、办公桌上，旁边还有随意的光影和角度，就像有人真的掏出钱包用手机拍了一张。

要一张加州驾照开加密货币账户？要英国护照在海外注册公司？要社保卡？都没问题。生成的结果是一些并不存在的人的证件照片，但足以骗过那些做证件验证的人和系统。

"用Photoshop渲染证件的时代正在结束。"OnlyFake的Telegram频道发过这么一条。2022年俄乌冲突后，Nazarenko离开乌克兰，辗转欧洲。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoczGvMdvAicog5uUF746DWibian02RwDapGMQ55ia96NFwaK2DQHnlhoIicvTcf1VorJvL4b91jjbhw5vhrpxBwbjpLW6S9pmXAfRc/640?wx_fmt=png)

图3 OnlyFake网站操作界面，填入信息即可生成对应国家的证件

客户可以单次购买证件生成次数，也可以订阅套餐。

Light套餐每月99美元，给10次生成额度。Ultimate套餐每月1500美元，客户可以上传一个Excel表格批量灌入个人信息，出证速度更快，还配Telegram专属客服。

Nazarenko说其他罪犯都在卖成品假证，而他在卖"钓鱼竿"。客户不用找假证师傅定制一张假证，自己上网站想生成多少生成多少。

美国司法部后来的公告说，OnlyFake生成了至少一万份假ID，总收入超过120万美元，每份假证售价仅15美元左右。

钱进来之后Nazarenko又投回OnlyFake，打广告、搞开发、扩团队。"到后来我发现这已经不是设计活了，变成了纯粹的工程问题。"他说，"实际运作起来跟正常科技创业公司差不多，只不过我们在非法市场里做生意。"

竞争者很快冒出来。有人DDoS（Distributed Denial of Service，分布式拒绝服务）轰炸OnlyFake，有人想偷他的模板数据库，还有个竞争对手挖出了OnlyFake的一名员工，逼Nazarenko让步，被他拒绝。

Nazarenko白天接客户订单，晚上调证件细节。为了提神他喝咖啡和功能饮料，后来成为了瘾君子。"那已经不是为了工作了，是为了让一个好几年没关过机的脑袋停下来。"

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpuxs1QYuia12dKjRWYw7XXESfzoUfxVEnlWYy83V4f5iaoOwxSCiaCz6DlmJnP0SPaAkdBicqk17pcacTYZ2JDjc0F9A442kTU0Rw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDplzh9xGmzBgG0nMx3FxIOJwRhDoiafP6CEHKuz7ZZ5QYOKibXm1ib89uaibb8iasDgI1wIZag44B1RST6t88uslOHxUzBYribnGyotI/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDoTvuHQaPXKlYHX1icD8yxxSyCDanoicqbxgumV8eyC3SGgb4ico5GVehg7CeN4ReUy9dcpnVuVryfsic3q8lhOV06qRzCNuFxys2s/640?wx_fmt=jpeg)

图4 Nazarenko流亡期间在东南亚的照片

2024年初，404 Media记者Joseph Cox在刷Telegram时发现了OnlyFake。他登录网站，充了一小笔加密货币，生成了几张假证。

"我被那些放在地毯和沙发上的假证件照震住了。"Cox回忆，"这东西对欺诈的影响太大了。KYC（Know Your Customer，了解你的客户）那套流程，就是让你上传护照来验证身份，现在任何人都能生成一张别人的证件，KYC还有什么意义？"

他输入了一个名字David Creeks，随机生日，网站自动填好了驾照编号、签发日期、有效期这些信息。几分钟后，他手里有了一张加州驾照的照片，"放"在一块地毯上。他还生成了一本英国护照。

然后他拿这些假证去试。他用虚构的身份成功在加密货币交易所OKX注册了账户。OKX前员工后来告诉Cox，他那次测试引发了交易所内部一轮整改，急急忙忙把系统做得更能抵御AI生成假证。

网络安全研究员Abhishek Mathew一直在追踪OnlyFake的增长，他告诉Cox，犯罪分子在用OnlyFake开银行账户，或者拿着假证去Binance解封被封的加密货币账户。

文章发出来之后，Nazarenko慌了。他删了所有个人邮箱，砸了笔记本电脑，买了新手机。他以为当天就会有警察来敲门。

他还在OnlyFake的Telegram频道发了个公告撇清关系："新闻说我们的生成器被用来伪造证件。完全是胡说八道。这种事以前从没发生过。至少因为它根本不能用来伪造证件。"

后来他对Cox承认，当时躲在"客户自己决定怎么用"这套说辞后面，其实他心里清楚这些证件会被用来洗别人的账户、洗钱、隐藏真实身份。

文章越传越广，DDoS攻击也跟着升级。Nazarenko还收到消息，说有"非常有权势的人"在用他的网站。

2024年2月26日，联合国给OnlyFake发了一封信。

信是用联合国官方信笺写的PDF，发到了OnlyFake网站上留的邮箱。因为OnlyFake毕竟是个地下犯罪组织，它没有公共办公室，也没有地址。

"亲爱的先生/女士，"信开头这么写，显然联合国的人也不知道到底是谁在运营OnlyFake，"专家小组收到情报，DPRK（Democratic People's Republic of Korea，朝鲜）IT人员一直在使用贵方服务。"

信里说朝鲜人用OnlyFake申请[美国的远程工作岗位](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451188319&idx=1&sn=5732d230422338a8c985c89ec3fe749f&scene=21#wechat_redirect)。

众所周知，[数千名朝鲜籍IT人员](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451183614&idx=1&sn=36601a9c6de60a2adcc63146929379a7&scene=21#wechat_redirect)通过远程岗位为美国公司工作，把工资汇回朝鲜资助核计划。联合国说这些人正在用OnlyFake制作假身份证，在自由职业平台、社交媒体和支付平台上注册账号。

联合国要求Nazarenko交出：所有DPRK用户的数据，OnlyFake为DPRK制作的全部证件，以及OnlyFake采取了什么措施阻止朝鲜人使用该站。

顺便说一句，朝鲜黑客最近从加密货币交易所Binance偷走了63亿美元，被认为是史上最大黑客案之一。

联合国的信对Nazarenko冲击很大。他说他感觉自己只是在做一个小项目，结果联合国找上门来，告诉他朝鲜人在用他的服务。他拒绝交出任何数据。但后来回想，这是他第一次意识到自己捅了大娄子。

而一个更深层的威胁也在盯着OnlyFake的增长：FBI。

2024年5月，Cox的文章发表几个月后，纽约南区联邦检察官派了一名执法人员卧底。

这名卧底探员先从OnlyFake买了一张纽约州的假身份证。据法庭记录，他后来又买了一本假美国护照卡。过了一周多，他又买了一张纽约州驾照和一本美国护照。几天后他又下单买了一张假社保卡。

OnlyFake的客服欣然提供了以上全部证件。更夸张的是，客服还主动教这名卧底探员怎么用这些假证绕过加密货币交易所的KYC审核。

Nazarenko一边靠保护别人身份吃饭，一边自己的安全防护却一塌糊涂。网站运营赚的钱，他用自己的真名把Bitcoin打到了一个加密货币交易所账户。一个造假证的人，居然懒得给自己也做个假身份。

当局要查OnlyFake是谁运营的，简直不费吹灰之力。乌克兰当局搜了他父母的房子。2025年6月13日，Nazarenko和女友飞布加勒斯特参加朋友生日，边境官员收走他的护照，盯着他的电脑看了很久，然后把他带到另一个房间问话。

他这才知道，美国已经对他发出了逮捕令。他被戴上手铐，关于OnlyFake的一切"突然变得无比真实"。当局还查封了OnlyFake的部分服务器。

他在罗马尼亚监狱待了三个月，然后被引渡到纽约。在布鲁克林大都会拘留中心，因为帮派成员袭击，监狱方面把他转到了另一个设施。他的律师后来在法庭信里提到了这件事。

"我当时在建一个可以用来伤害人的东西，还从中赚钱。直到我坐在水泥牢房里，我才真正理解这一点。"Nazarenko说。

他的律师Igor Litvak说，Nazarenko提出配合当局，包括提供潜在客户信息。他甚至把联合国的信拿给FBI看，证明他平台上用的是什么人。但检察官没有接受他的合作提议。纽约南区联邦检察官办公室确认收到了Cox的采访请求，但没有回复为什么没有和Nazarenko达成合作安排。

今年6月，也就是他被捕一年后，法官判处他12个月监禁。跟最高15年的量刑比，这个刑期轻得反常。部分原因可能是当局没能锁定OnlyFake的任何具体受害者，只确认了网站存在且被用来制作假证。他坐牢的大部分时间里，OnlyFake还在正常运行，只不过站长本人进去了。

出狱后的事更糟。他以为律师会直接开车送他去机场自我遣返，结果刚走出法庭，ICE（U.S. Immigration and Customs Enforcement，美国移民海关执法局）就把他扣了。他又在拘留所待了两个月。"那比监狱差远了，"他说，"睡地板，有人就在你眼前死掉。"

8月17日，他和几个乌克兰人一起被包机遣返。在波兰机场走出来的时候，他只有身上带着的东西。"什么都没了，我还活着。"他当时脑子里就这一句话。然后他被陆路送回乌克兰，直接拉去征兵站报到。他说他逃了出来，步行离开乌克兰，最终飞到了泰国。

OnlyFake催生了一堆山寨网站。FBI已经盯上其中一些，有的被端掉了。但更根本的问题是，有了OnlyFake打样，犯罪分子甚至不再需要一个专门的地下网站来做假证。

研究人员已经在用商用AI聊天机器人生成手持身份证的人脸照片。当然主要AI厂商仍在技术层面加了防护。一些公司也升级了检测能力，可以识别AI生成假证件的痕迹，即使肉眼看起来完全真实。

Nazarenko现在在泰国做一款叫TapMap的app，一个社交和活动发现平台。他的律师把这个app作为证据提交给法庭，证明Nazarenko不会再犯罪。"这么久以来我第一次有了想拼命去做的东西。"他说，指的是做app和戒酒。

8月21日，也就是他被遣返几天后，Nazarenko给Cox发了一封邮件。Cox让他发点东西证明他就是Yuriy Nazarenko本人，他发了一张自己护照的照片。Cox用在线工具检测了一下，那张护照照片没有任何AI篡改痕迹。

这个做了一辈子假证件的人，最后用一张真护照证明了自己的身份。

预览时标签不可点

修改于

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过