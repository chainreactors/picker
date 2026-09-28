---
title: 俄罗斯全国手机预装的Max聊天应用的技术底牌
url: https://mp.weixin.qq.com/s/flfNgC8gp37WbKasUgnZ9w
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:52:27.255368
---

# 俄罗斯全国手机预装的Max聊天应用的技术底牌

# 俄罗斯全国手机预装的Max聊天应用的技术底牌

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2025年9月1日起，任何在俄罗斯卖出的新手机和平板，开机就自带一个叫Max的应用。MAX是由俄罗斯VK互联网公司研发的跨平台即时通信应用程序，作为应对西方制裁的国产替代方案于2025年3月立项，同年6月获总统普京签署法律确立推广框架。 该应用集国家服务、数字身份与人工智能功能于一体，自2025年9月1日起依法预装于俄罗斯境内新销售的电子设备。 该软件除支持私信、群聊和多媒体分享功能外，未来深度整合国家服务系统实现电子政务操作，用户可完成点餐、打车、缴税及数字身份认证等事务。同一时间，Signal在2024年8月被封，WhatsApp在2026年2月被封，连域名都从俄罗斯国家DNS服务器里被摘掉，Telegram从2026年3月中旬开始被大规模屏蔽。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDo6E8Cw8XLyEI0DWNmPD4bqJEHwkTgL3OLwG5gfsjuoUk7ZItRibMficCZrKicziaWFHsFIib6nIqibjNwtIfBXXypqcWwUBrb0X9w4g/640?wx_fmt=png&from=appmsg)

Max由VK Group开发，这家公司如今的股权握在Gazprom体系手里，实际运行Max的主体2026年1月才改名成OOO“MAX”。一个叫InterSecLab的安全研究团队将其分析了一遍，他们看的版本是Android端26.12.0，build 6664，包名ru.oneme.app。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDos6MV31YaFVYQcBG73peGsMnibjJJiaEhp1k0DhpcHr4yfwRE5oXXBdwqagqlF67F9KnnCpFQ1fafW2Rjibqh5aV0lmrtdctI7z0/640?wx_fmt=png)

图：事件时间线上半段，从2016年TamTam诞生到2026年5月InterSecLab开测。图源：The Max Messenger报告

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqHFjBwaEZDBd7Xxjtn3h7Kk0IebzfjqTbgJCNdmLCItEPxViaD4OKDoBdvUbKhdrwHBhU7V0z3Zg9zKhiaYrgxpibpPFAz8eq1GI/640?wx_fmt=png)

图：时间线下半段，Apple下架、欧盟制裁、Google Play下架，直到报告发布。图源：The Max Messenger报告

俄罗斯早就有一套成熟的大表哥体系。一套叫[SORM](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451177246&idx=1&sn=0ca1cca0bd247e9d96af0819dc5bd04f&scene=21#wechat_redirect)（对侦查活动进行的系统保障），运营商和信息服务必须给FSB开技术后门，让他们能拿到用户数据。另一套叫TSPU（对抗威胁的技术手段），监管机构Roskomnadzor可以在运营商网络里放深度包检测设备，过滤、限速所有流量。有了这两样，国家本来就很清楚谁在什么时候、从哪里、连到了哪里。

Max从设计上就抗拒被研究。它不用大多数App依赖的标准Web加密，改用俄罗斯联邦标准密码，实现密码库的公司持有FSB颁发的许可证。它一检测到Frida这类动态分析框架，几秒钟内就自杀退出。它把要访问的服务器地址，不是以可读字符串，而是以打乱的整数数组形式藏在代码里，普通字符串搜索根本找不到。服务器还会拒绝一切不协商俄罗斯加密套件的连接，常规抓包代理连不上。

分析人员想办法在消息被加密之前、在App内部那一刻就把它截下来，相当于在信封封口之前偷看一眼，再把看到的每一件事和产生它的代码对上。报告里反复标注哪些是“亲眼看到发生的”，哪些只是“从代码推出来的”。

研究团队最后得出结论：Max不提供端到端加密（end-to-end encryption）。每一条消息，VK的服务器都能直接当明文读。

研究团队是这么证实的：

他们在Max把消息交给GOST TLS密码库的那一刻，截到了还没加密的明文。那个被命名为“secret chat”的功能，名字极具误导性，其实只是一个消息过段时间自动消失的定时器，一点密码学保护都没有。在俄罗斯，Telegram当年用“secret chat”这个词特指它的端到端加密模式，Max沿用同一个词，却给了个完全不同的东西。

还有更主动的一步。每条文本消息都带着一个标志位，指令服务器去检查里面的链接和分享内容。这和Signal的做法形成鲜明对比：Signal的链接预览是在你自己手机上生成的，你去抓那个网址、本地生成预览图再塞进加密消息，服务器压根看不到链接长什么样。Max相反，服务器是例行公事地把每条文本拆开看。

注册时，App会弹窗要你的通讯录权限。那个弹窗只有“允许”按钮，没有“不允许”或“跳过”，点掉它会在新手引导里反复弹，直到你同意。

一旦同意，你整本通讯录就被整包上传到VK服务器，电话号码和你给每个联系人存的名字成对出现，而且是明文。它不是Signal那种“隐私保护的联系人发现”，不需要在不暴露完整名单的前提下算出共同好友。

研究人员在这次全新注册账号的过程中，直接在网络上抓到了这次上传：号码就是一串明明白白的数字。他们回去查那段被读成哈希的代码，发现那只是个格式化规整函数，剥掉非数字字符、去掉国家前缀、把开头的8改写成7，全程没有调用任何加密函数。

更别说，任何一个号码只要注册过Max，别人就能查，不需要互为好友，对方收不到任何通知，研究方也没发现频率限制。

同时，语音消息不是在你手机上转文字，是传到VK服务器上转写的。你自己发出去的和你收到的，都能转，所以VK手里既有你说的话，也有别人对你说的话。协议层面用两个专门命令TRANSCRIBE\_MEDIA和NOTIF\_TRANSCRIPTION来处理。研究里观察到的转写都是用户自己点开按钮触发的，无法确认是否存在自动转写的通道。

通话时发生的事更值得琢磨。通话过程中的实时音频，会被送进一个跑在你手机上的机器学习模型做关键词检测。关键是这个模型并不打包在App里，它在运行时从服务器给的一个URL下载，用服务器给的校验和核对完整性，再对通话音频执行。这套流水线理论上能跑VK下发的任何TensorFlow Lite模型。

他们这次抓到的模型，只听一句俄语短语“не слышу”（听不清），用作通话质量的信号，触发后把一个置信度分数上报。但重点不是这个模型听什么，而是机制本身：它听什么词，是服务器随时可以改的，不用更新App。今天它在听“听不清”，明天它可以听任何词。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqRQGUibmYoicYVyJxygFGpXDmEibMCVJqNrdHU2WsdibLjNoQmLQ4q5sO2jLZBt1kV2bRtdIiaICLiaWajI7hu5fExOCyASDdFcfybQ/640?wx_fmt=png)

图：Max收集的数据分成四类：识别身份与社交关系的、通讯内容、网络环境信息、App内行为记录。图源：The Max Messenger报告

每次你打开Max，或者把它切到后台，它都会顺便探测一下网络环境。具体做这些事：通过最多六个外部服务查你设备的公网IP，检查有没有VPN在跑，读出你连的是哪家运营商，再测一串互联网服务能不能连上，然后打包成一份报告发给VK。

这份报告里的IP地址，单独看就能给出每个用户的大致地理位置，而且每次打开App都刷新一次。被它测连通性的名单里，有Max自己的服务器、Google的静态内容分发、Google Cloud Messaging、Odnoklassniki的CDN，还有俄罗斯政府服务门户gosuslugi.ru。更早的版本里，这份名单还包含Telegram和WhatsApp，直到2026年3月这件事被公开报道后，VK才把这两项从活跃名单里删掉，但代码原封不动留在安装包里，随时能加回来。

为什么测Telegram和WhatsApp能不能通很重要？因为这等于一台被动的定位仪：这两个服务能连上，说明你的设备大概率不在俄罗斯的封锁网络里。更进一步看，俄罗斯的网络运营商依法必须落实对这两家的封锁，那几百万台装了Max的手机，就变成了一张分布式测量网，能告诉政府哪家运营商在乖乖执行封锁、哪家在阳奉阴违。而报告里恰好带着运营商信息和IP，正是画这张图需要的数据。

上面这个模块的探测目标是写死在App里的，服务器改不了，得发新版才行。但报告发现还有第二条、藏得更深的通道。这个叫DPS的模块，包名ru.trace\_flow.dps，上报地址是trace-flow.ru。它和前面那个模块完全独立，有自己的初始化、自己的网络客户端、自己的凭证，连代码都不共用。别的服务器地址在代码里都是明文，唯独这个地址是打乱存放的，得解码才读得出来。

这条通道会主动向服务器要一份“去测哪些地址”的清单，而清单内容不受任何限制，可以带端口。拿到清单后，手机对每个地址做最多三项测试：域名能不能解析、连接能不能建立、加密连接能不能跑完，把每个结果分别上报，连同你的账号标识、设备标识、表观IP、运营商和VPN状态。多久跑一次，也是服务器说了算。

这个开关默认是关的，但研究人员的测试账号显然被打开了。他们翻了26天的录包，找到手机联系这个地址19次，分别在2026年4月21日、5月14日和5月22日，每次都完成一次加密交换。他们从连接形态反推出被测目标，包括Max自己的API和通话基础设施、gosuslugi.ru，以及Google、Apple、Huawei三家的推送服务端点。其中Apple推送的地址，在App里用任何字符编码都搜不到，只能是服务器下发的。

那trace-flow.ru到底是谁的？它解析到三个地址，全都在AS47764自治系统内，注册方是莫斯科的LLC VK；它出示的TLS证书颁给莫斯科的VK LLC，由需要核验企业法人身份的GlobalSign签发。所以藏来藏去，藏的不是什么第三方，而是VK自己的一条上报通道，只是不想让读代码的人一眼看到。

现在可以讲整份报告里最关键的一句话了。Max的这些监控能力，是由VK服务器上的feature flag（功能开关）控制的，按账号实时下发，不用更新App，界面上也没有任何提示。

网络探测、VPN检测、语音转写、提高日志级别、允许哪些服务拿到你的身份，全都挂在这种开关后面。VK可以单独给某一个人打开某项能力，别的用户毫无感知。这意味着“Max今天在做什么”和“Max是什么”是两回事。我们在代码里发现处于休眠状态的能力，明天可能只对你一个人醒来，而你完全看不出来。

换个人、换个版本，看到的可能就是另一个App。

回到前面说的“查任意手机号”。你输入一个注册过的号码，服务器返回对方的内部ID、显示昵称、账号创建时间，还有最近一次资料更新时间。不需要互为好友，不通知对方，也没看到频率限制。

然后怪事来了。查询发出后1.2秒内，VK的服务器就开始把对方的实时在线状态持续推送给查询者，一推就是十五分半钟，对方什么时候活跃、什么时候空闲、什么时候下线，全被记录。同一秒钟里，服务器还自动生成了一个把两个账号连起来的聊天对象，哪怕两人从没说过话、也没互相加好友。也就是说，只要你查了某个人，这两人之间的关联就已经在服务器上建立了，VK看得见，哪怕你们之后一个字都不发。

2026年4月的一次双账号互动测试里，一台设备上的用户想回一条消息，Max直接弹出全屏提示，让你先关掉VPN才能继续，发消息功能被整体锁死，点不过去也切不走聊天，唯一的办法就是关VPN。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqp1xaPsuLRAbKBk6Tk4Z31uDEDduttKY4ZtNoujjnKmbwSVJtCWWEArX9GOdFdGkBcGl12rka5viav9bQWpfBAaia5ZuiaepGyjA/640?wx_fmt=png)

图：Max检测到VPN后弹出的全屏拦截，俄语意为“关闭VPN才能使用MAX”。图源：报告实测截图

他们换了个方式验证：

把本机VPN客户端换成VPN路由器，让所有流量在网关那里就走VPN隧道，手机上根本看不到VPN网卡，Max就恢复正常了。原因在于，Max的VPN检测查的是手机本机上有没有VPN网络接口，而不是从流量的IP地址、MTU这些特征去推断。这个检测在本地完成，把VPN挪到路由器上就能躲开，当然前提是你得买得起、会配、还能掌控自己的网络。

Max不是从零写的。它的网络协议和大量代码，继承自TamTam，那是VK当年（还叫Mail.ru）2016年放在Odnoklassniki平台上的一个聊天产品，从没真正成过Telegram或WhatsApp的对手。反编译出来的代码里到处是ru.ok.tamtam这样的包名。

从TamTam到Max，换的主要是服务器地址和密码。协议本身没变，还是那种专有的、基于MessagePack的二进制格式跑在TLS上。变的是传输加密被迁到了GOST TLS，也就是俄罗斯联邦密码体系，主服务器换成了api-gost.oneme.ru。具体用的对称分组密码叫Kuznyechik，写在俄罗斯联邦标准GOST R 34.12-2015里，国际上以RFC 7801公开，而这个密码库由一家叫CryptoPro的商业公司实现，它持有FSB的许可证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDq5wUUKfwGxAqJfIbQGNlfGicHHmich8zMUiblLdCibbWaPzxzvlHibumI3kicGON5Hg7a1cZzrgdCBUo1esXLicRqtFDUNIibhNdLJONI/640?wx_fmt=png)

图：Max的协议架构。红色部分继承自TamTam，蓝色虚线部分是Max新换的GOST TLS传输，消息内容在加密隧道里仍是明文，隧道挡住了网络旁观者，挡不住VK。图源：The Max Messenger报告

Max的后端，挤在一整个4096个IP地址的网段里，这个网段是2025年9月5日，也就是强制预装生效那个月，专门拨给莫斯科LLC VK的。它核心功能联系的每一台服务器，都是俄罗斯运营、俄罗斯托管、经俄罗斯骨干网可达的。研究期间唯一观测到流向境外的，是几个公开的IP地址查询服务。

为了防研究，App下了狠手：类名方法名大多换成短乱码，要探测的主机名存成整数数组，VPN检测代码要查的网卡名是加密的，检测到Frida就自杀，服务器拒绝一切不谈GOST加密套件的连接。

现代Android默认要求所有流量走TLS，App可以在网络安全配置文件里给特定域名开例外。

Max列了8个例外：6个是俄罗斯四大运营商MegaFon、MTS、Tele2、Beeline的域名，用于Mobile ID这种运营商级身份验证；另外两个是\*.gov.ru和\*.voskhod.ru通配符，后者关联运营ESIA（俄罗斯统一身份认证系统）的国家科研机构，而ESIA正是政府服务门户Gosuslugi的身份底座。这些连接有可能是明文的，路上任何设备，包括运营商和SORM监控设备，都能看见。

以上仅是黑鸟挑出的一些感兴趣的内容，有需可自行查阅剩余内容。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqdfrejsU8TJzwgd7ibiaVfth32N7TCicGSj41lLLkSPyciamicMWtmerYPJmqlyYykSbwQVk7dxHexXywAF9bNpZafopQEozmmBjFk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

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