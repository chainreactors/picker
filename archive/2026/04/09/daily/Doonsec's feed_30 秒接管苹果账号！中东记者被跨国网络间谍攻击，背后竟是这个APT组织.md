---
title: 30 秒接管苹果账号！中东记者被跨国网络间谍攻击，背后竟是这个APT组织
url: https://mp.weixin.qq.com/s/rk0l-0CUIoXPWax4lF6iwQ
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:40:49.643721
---

# 30 秒接管苹果账号！中东记者被跨国网络间谍攻击，背后竟是这个APT组织

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqFOt1mwQmHnc8qPt6PEQuxoaJclWj17oTcfIfTJnUXxD9tFpoWVQ6AFhickwLBE25nibtjdgvK6XGzIVWibqgO2fKMf6xtd0z4Js/0?wx_fmt=jpeg)

# 30 秒接管苹果账号！中东记者被跨国网络间谍攻击，背后竟是这个APT组织

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

近期，国际数字权利组织 Access Now 与西亚北非地区数字安全机构 SMEX 联合和移动安全公司 Lookout发布了三份调查报告，揭露了一起持续三年的跨国雇佣黑客行动。

该行动专门针对中东和北非地区的记者、人权活动人士等公民社会群体，攻击者能在 30 秒内完成苹果账号的完全接管，甚至部署安卓间谍软件窃取全部隐私数据。

经分析，这一系列攻击高度关联知名印度APT组织BITTER。

这场跨国间谍行动的受害者均为中东地区具有影响力的公民社会成员，攻击时间跨度从 2023 年持续至 2025 年，呈现出高度的针对性和持续性。

### 埃及记者：从苹果账号到谷歌账号的连环攻击

###

2023 年 10 月 18 日，埃及独立记者穆斯塔法・阿萨尔在黎巴嫩收到一条来自 iMessage 的消息，发件人冒充苹果官方，声称他的苹果账号绑定的手机号需要验证，否则将被冻结。消息中附带了一个看似官方的链接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrqqo1AGWkXzfNOTcpAf6umlswibK5kp6sPuY6Vet9QJET5jOFHiajpUgk1qmAaH95exZFx1O8umTHbN65UQsxibNqNIMhhY56fns/640?wx_fmt=png&from=appmsg)

尽管阿萨尔最初并未理会，但攻击者持续发送消息施压，最终他点击了链接并输入了账号密码。就在此时，苹果向他的可信设备发送了登录提醒，显示新设备正在埃及开罗尝试登录，而他本人当时身处黎巴嫩。这一异常让他立刻警觉，拒绝了登录请求并联系了 Access Now 的数字安全热线。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrPg11ARiaXJWKy50DzXXlFy4JDcrwnB4PS6ibrtvSssuwfafDTwibe6zwnaiaZhpt5Ug46JOI99rm4mAOdM2vh4kpDpMmeqicuYH4w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrzStbvicM4EjLPGWn2icjcBnA7blVF96uicI3EBmnhbCSTw65X4zfGW6pCS4iavSblgkvXm3icA4ib6mpWZyeibibofD3E5pcylWQiaGkg/640?wx_fmt=png&from=appmsg)

手法类似：[我差点就把苹果账号弄丢了:这是我见过的最狡猾的钓鱼攻击](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451183775&idx=1&sn=740e073c7a8c28a9163d66cd728fe43f&scene=21#wechat_redirect)

然而攻击者并未放弃。2024 年 1 月，他们又伪装成跨国电商平台 Mercado Libre 的人力资源专员，通过 LinkedIn 向阿萨尔发送工作邀请。在获取他的邮箱和手机号后，攻击者发送了带有 Zoom 会议链接的邮件，实际上这是一个利用谷歌开放授权协议的钓鱼页面。如果阿萨尔点击授权，攻击者将获得他谷歌邮箱的完全访问权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpZrouBfX0X2syG4f3maCLVmJUN77SmoZm2ibLDycqXVYM7AeZCFH6jSNn5fSYWmjyAsF3n3lvZly2YqmIeR5BXmYmZQIefiaKnM/640?wx_fmt=png&from=appmsg)

就在阿萨尔遭受攻击的同一天，另一位埃及知名记者、前总统候选人艾哈迈德・坦塔维也收到了几乎一模一样的 iMessage 钓鱼消息。坦塔维此前曾多次成为网络攻击目标，2021 年和 2023 年曾被发现感染 Cytrox 公司的 [Predator 间谍软件](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451184834&idx=1&sn=9370a0d59636bba8440ef349cbfa1afc&scene=21#wechat_redirect)。2024 年 2 月，坦塔维因政治活动被埃及政府逮捕，而针对他的网络攻击在此之前就已密集展开。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqZCZ4ZEvc01Q8zUkWKNC7Hjx7W6jf2EY9ouEs45vDXmdZPk8LgvQfqrPY8INy2EGLE4RoylGgqVdp8FpfUftXyicYoQs4IcLfI/640?wx_fmt=png&from=appmsg)

###

2025 年 5 月 19 日，一位不愿透露姓名的黎巴嫩资深记者收到了来自 idapple.review@icloud.com 的 iMessage，内容同样是苹果账号验证提醒。这次攻击成功骗过了记者，他的苹果账号被完全接管，攻击者还在账号中添加了一台名为 “iPhone VMWare” 的虚拟设备，获得了对他云存储中所有文件、联系人、邮件和位置信息的持久访问权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqgj0MgvGcA0B5UWGwvs16JLibBLMkbmH45aLcHcfbo3Das1KunLZR84tOLjo8YyIMnF4enqiaqgsCSbMPhCmWicz0icgibDYdzan4E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqwfTYv53ZHicmZYUrUSvjwQACAoLa3heicRPtMicLictyXRydMia3NgdDLic5h5cBEqOP1q9YFqfHzXdPKmH9VxSn2dTEiaOfiaVyPbGw/640?wx_fmt=png&from=appmsg)

记者发现异常后，立即终止了攻击者的会话并修改了密码。但仅仅两天后，攻击者又通过 WhatsApp 发送了两条新的钓鱼消息，声称他的苹果密码已被修改，需要再次验证。

SMEX 数字取证实验室介入后，在受控环境中模拟了这次攻击，结果令人震惊：从受害者输入密码到攻击者完成账号接管，整个过程仅用了 30 秒。

这一系列攻击展现了极高的技术水平和周密的策划，攻击者的手段涵盖了从基础钓鱼到高级间谍软件的全谱系工具。

攻击者构建了一套庞大且逼真的钓鱼域名体系，这些域名采用统一的命名模式，通过模仿官方服务和添加地区标识来迷惑受害者。例如针对黎巴嫩的攻击使用 com-en.io 后缀，针对阿联酋的使用com-ae.net后缀，针对阿拉伯语用户的使用 ar-id.cc 后缀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDp57iaZ5oQx0cSRLKP8jZbOubySFxcc9ZZ43EyyRRicvUKHaRGo9xLrc87jBQp43oIfK3vlDShpEJ9xkWXviabBSP24lnficjbCz9s/640?wx_fmt=png&from=appmsg)

每个主域名下又生成大量子域名，分别模仿苹果 ID、FaceTime、Signal、Telegram 等不同服务。仅在 com-en.io 这个主域名下，就发现了 id-apple、facetime、secure-signal、join-telegram 等多个子域名。这些域名的注册和使用时间都非常短，通常只在攻击当天激活，事后立即关闭，以逃避安全检测。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqNicNapNMKW4buiaZNlUUnpgBazD7SPfTpqMicGEz0cbbdqxPicylEHtLMCicrrU0AJ0kQLdI0Wo5CtCLqvicqGhNLkibh0BNT1ZQCXs/640?wx_fmt=png&from=appmsg)

###

最令人担忧的是攻击者突破双因素认证的能力。传统的双因素认证被认为是保护账号的有效手段，但在这次攻击中，攻击者使用了实时中继技术。当受害者在钓鱼页面输入验证码时，攻击者会同时在真实的苹果登录页面输入相同的验证码，整个过程在几秒钟内完成，让双因素认证完全失效。

SMEX 的测试显示，攻击者的系统会自动提交输入的第 6 位验证码，无需任何人工干预。这意味着只要受害者在钓鱼页面输入了密码和验证码，账号就会立即被接管。

### 功能强大的安卓间谍软件

###

除了账号钓鱼，攻击者还会分发伪装成 Signal 加密插件的恶意安卓应用安装包。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDomicUxdLzANNGbBRXAiaFAAFSyRHkMhyXlNlM2ficlvbGKv5mErsr504rzNxzMGLNhd9w7l4RLY8beibEibiaPzkbomj0Xep8lYnOoc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp33X99Um0snB03Ty1iciafIx9uyicbDBm9sbpnib1eTlIMfAEtusI3EZlOhOledkAXzRgia61kaQgrlSYiaAayia4Nvsb3nHbTnXx6zs/640?wx_fmt=png&from=appmsg)

这款被 ESET 命名为 “ProSpy” 的间谍软件，当时使用这款间谍软件的攻击者似乎主要以阿联酋的目标为攻击对象，一旦安装就能获取手机的全部权限，黑鸟去年恢复更新后第二天发的东西，终究还是会被Callback：[发现新的攻击阿联酋用户的间谍软件们](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451182865&idx=1&sn=3e74aff4ea5576ac1e5479f435259ea2&scene=21#wechat_redirect)，没想到还能关联到这里去了。

功能包括：

* 扫描并窃取所有文档、图片、音频和视频文件
* 读取并导出全部短信和通讯录
* 监控最近修改的文件和备份文件
* 自动上传所有窃取的数据到攻击者的服务器

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrz49OXqy0rzgsJukQeficbVML06BDwEFVg7Pgqho5XrIo15zOemkIV3DlFu6uTJhohFUtSrlkbRUxicJJzricveyKEibKGxCI56ZQ/640?wx_fmt=png&from=appmsg)

为了躲避安全研究人员的分析，攻击者在钓鱼页面中加入了多层反取证措施，包括约 600 行的十六进制填充代码、开发者工具拦截、控制台劫持和调试器陷阱。

这些技术会导致分析工具崩溃或无法获取页面的真实代码，大大增加了研究难度。

攻击者还会在受害者设备上设置有效期长达 10 年的跟踪 Cookie，以便长期监控受害者的活动。

通过对攻击基础设施、战术技术和程序的交叉分析，Lookout 公司将这一系列攻击归因于印度的 APT 组织 BITTER。

BITTER 组织传统上活跃于南亚地区，主要针对政府、军事、外交和关键基础设施部门进行网络间谍活动。近年来，该组织的活动范围不断扩大，已延伸至沙特阿拉伯、土耳其、南美洲以及现在的中东和北非地区。

与传统的国家支持的 APT 组织不同，BITTER 似乎采用了雇佣黑客的运营模式。Access Now 和 Lookout 的分析表明，有未知实体雇佣了该组织或与其有联系的机构，专门针对中东地区的公民社会成员进行监控和情报收集。这种模式使得攻击的溯源和追责变得更加困难。

值得注意的是，本次攻击中使用的部分基础设施和工具，与 2022 年 Meta 公司披露的一个攻击工具包存在技术关联，这表明 BITTER 组织的工具库在不断演进和完善。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrokPXo66uq8icopXK3s5CMN7FZpaoVhebFWb0NXoCQaQ7p2rTwyQ2LicqN2b982N0d48ic2RPXiaPDFewoG3mOo9bQ6VZ4YLbIQps/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqCVGDcUChVunkZXBH4bLD90AOmYciasaeUGKshLicf4uthFrkma5ktiaiaZibZuEYeoD3fuGxibOMjRRrOe0wj1ricYpXkdQWib45WxS8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrlnJ45frFhQVHIrCfnB9m4ocwjFGzW5wG8y6ka2iahMpNPE0uN4L4BDyWsETWKq9aYgsOEGibjYF1YhYTZbhTjvtOicjWRgQia3vY/640?wx_fmt=png&from=appmsg)

对于上述结论，黑鸟倾向于雇佣黑客多头干活所导致的结果。

有需要报告PDF、IOCs和相关链接见下自取：

https://github.com/blackorbird/APT\_REPORT/tree/master/bitter/2026

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDq7eg8m4fOJ5CZCcGKuNrM5Dk8hKTf1nX2Mx1uQuZ2QxhTcWFiayuXBe6YMpq3OKSVpc0CpQyLqxpl9icNbbq0Ihib7L6vyyJvumE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpb33bicgibClJv0VlDTY4wq12pdCG4p622oDYz3ZiayNOqRIKJevvlciaHJGIKtrc4ew4Rv0qQgNFX77zgic9Vm6TsBTibPjTDaWdo0/640?wx_fmt=png&from=appmsg)

往期:

[你身边的光纤，可能正在偷偷听你说话](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186251&idx=1&sn=277a34cc55cbf5915e62f83479ccbe38&scene=21#wechat_redirect)

[人工智能加持的新型钓鱼即服务平台EvilTokens](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186267&idx=1&sn=8f8a82d6eeed10560bdeeb7c950bd3eb&scene=21#wechat_redirect)

更多：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

向上滑动看下一个

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