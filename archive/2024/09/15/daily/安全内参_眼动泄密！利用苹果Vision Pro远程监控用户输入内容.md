---
title: 眼动泄密！利用苹果Vision Pro远程监控用户输入内容
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512624&idx=1&sn=6269cd44b8a01e2b008d46149088e178&chksm=ebfaf510dc8d7c06f1c9e28d0a8c3ac78db1ff96aa5c8b27623b69f4385308e9f1a641a23972&scene=58&subscene=0#rd
source: 安全内参
date: 2024-09-15
fetch_date: 2025-10-06T18:26:29.472261
---

# 眼动泄密！利用苹果Vision Pro远程监控用户输入内容

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7sHIq7ia494KfibIZ5dQZia9jR7m5hdI6sl16dDpiaWf0w9EpnHmYsAmcbjz8SflU3S85SVQqEbuVOE5w/0?wx_fmt=jpeg)

# 眼动泄密！利用苹果Vision Pro远程监控用户输入内容

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7sHIq7ia494KfibIZ5dQZia9jRXzYqEZ70KT2NDFFrlUDqSqPjY1ic4rEFevO4NLf98ibc3kBwoOIfGbcg/640?wx_fmt=webp&from=appmsg)

**Vision Pro在通话和流媒体中使用3D头像，研究人员利用眼动追踪技术暴露的数据，破解了用户通过其头像输入的密码和PIN码。**

前情回顾·**新技术安全**

* [汽车雷达可被“伪造信号”欺骗，无法识别道路车辆](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247511007&idx=1&sn=6eb549510198840c41d72a6825650c8d&chksm=ebfaecffdc8d65e968961a77ff083c0f18f838716057d73204f94fdae7d0f91be38dd593f642&scene=21#wechat_redirect)
* [量子安全加密遭破解：因加密组件存在漏洞](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247510774&idx=1&sn=c2dfe84a9892e4cf672449b14b67e9f8&chksm=ebfaedd6dc8d64c0dcdb5d3ba4958db03163ba3dd4046107342d61eed505ca170215a5a8da42&scene=21#wechat_redirect)
* [新型蓝牙攻击让医疗/金融等物联网终端“停摆”，该如何防护？](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247510667&idx=1&sn=e1f2f38749ee7b035feb04aef4c0af4b&chksm=ebfaedabdc8d64bdb14c728151c6f55facf1294296320f67544603ad8b11642b61c35058839f&scene=21#wechat_redirect)
* [新型攻击动摇互联网安全基础，SSH安全性是否被打破？](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247510639&idx=1&sn=23ef7f0c0ef1406bb9b4e071f29961e9&chksm=ebfaed4fdc8d64596d9ecd3deb1f8b770a49af23b5bf33230552f3c8092f7624e387c291118e&scene=21#wechat_redirect)

安全内参9月14日消息，你的眼睛能泄露很多信息。它们可以显示你有多累、你的情绪状态，甚至提供健康问题的线索。但更令人担忧的是，它们还可能泄露更隐秘的信息：你的密码、PIN码以及你输入的消息。

日前，六位计算机科学家揭示了一种针对苹果Vision Pro混合现实（MR）头显的新攻击方式。

**攻击者通过获取暴露的眼动追踪数据，解密用户通过设备虚拟键盘输入的内容**。这种攻击被命名为GAZEploit。研究人员成功地重构了用户通过眼睛输入的密码、PIN码和消息。

参与该研究的主要研究员之一Hanqiu Wang表示：“通过眼睛移动的方向，黑客可以判断受害者当前正在输入哪个按键。”在五次预测中，他们能够准确识别77%的用户密码字母，并能正确识别92%的输入信息。

需要明确的是，研究人员并没有直接访问苹果的头显去查看用户的视线位置。他们是**通过远程分析由Vision Pro生成的虚拟头像的眼动，来推断用户正在输入的内容**。这些虚拟头像可以在Zoom、Teams、Slack、Reddit、Tinder、Twitter、Skype和FaceTime中使用。

研究人员于今年4月向苹果报告了这一漏洞，苹果在7月底发布了补丁，防止了潜在的数据泄露。研究人员指出，这是首次利用人类“注视”数据进行的攻击。

研究结果强调了生物特征数据（比如人体信息及其测量数值）可能泄露敏感信息，并成为新兴监控产业的一部分。

**眼睛间谍**

使用Vision Pro时，眼睛相当于鼠标。输入信息时，用户会注视一个悬浮在空中的虚拟键盘，键盘尺寸可以调整。当用户看到正确的字母时，双指轻点即可完成输入操作。

虽然所有操作都会保留在头显内，但如果用户需要快速加入Zoom会议、FaceTime通话或与朋友直播，就需要使用一个Persona，也就是Vision Pro通过扫描用户脸部生成的3D头像。

研究人员在一篇预印本论文中详细阐述了他们的研究成果：“在视频通话中，用户的虚拟头像会反映他们的眼动，这种技术可能意外泄露关键的面部生物特征，包括眼动追踪数据。”Hanqiu Wang表示，研究依赖于两种可以从Persona录制中提取的生物特征：眼睛纵横比（EAR）和注视方向的估计值。

领导研究的Zihao Zhan解释道：GAZEploit攻击分为两个阶段。首先，研究人员通过分析用户共享的3D头像，开发了一种方法来识别佩戴Vision Pro的用户何时在输入内容。为此，他们利用递归神经网络（一种深度学习模型）对30人的头像录制数据进行了训练，这些人完成了不同的输入任务。

研究人员发现，当用户使用Vision Pro进行输入时，他们会集中注视某个可能按下的键，然后迅速转移到下一个按键。Zihao Zhan解释道“我们在输入内容时，眼动表现出一定的规律性。”

Hanqiu Wang指出，这种规律在输入时比在浏览网页或观看视频时更为明显。她说：“在进行注视输入等任务时，由于更加专注，眨眼的频率会降低。”简而言之：在QWERTY键盘上查看字母并在其间移动的行为具有很强的独特性。

在研究的第二阶段，研究人员使用几何计算推断出用户键盘的位置和尺寸。Zihao Zhan解释：“只要我们能获得足够的注视信息准确还原键盘，后续的所有按键输入都可以被检测到。”

结合这两个因素，研究人员能够预测用户可能正在输入的按键。在一系列实验室测试中，即便研究人员对受害者的输入习惯、速度或键盘位置毫无先验知识，仍能在五次预测中正确猜对字母，输入信息、密码、PIN码的预测准确率分别达到92.1%、77%和73%，而电子邮件、网址和网页的预测准确率为86.1%。（在第一次预测中，字母的准确率在35%至59%之间，具体取决于他们尝试推断的信息类型。）重复的字母和打字错误增加了预测的难度。

美国波莫纳学院的计算机科学副教授Alexandra Papoutsaki表示：“知道某个人在看哪里是一种非常强大的能力。”她多年来一直研究眼动追踪技术，并为连线杂志评审了GAZEploit的研究成果。

Papoutsaki指出，这项研究的独特之处在于它仅依赖于用户Persona的视频流。相比于黑客获取用户的头显并试图获取眼动追踪数据，这是一种更“现实”的攻击场景。她补充道：“现在，仅通过流媒体中的Persona，某人可能会泄露他们的操作，这使得这一漏洞更加关键。”

虽然这种攻击是在实验室环境中创建的，并未在现实世界中针对使用Persona的人实施，研究人员仍警告，黑客可能会利用数据泄露。他们指出，理论上，犯罪分子可以在Zoom通话期间与受害者共享文件，诱使他们登录谷歌或微软账号。攻击者随后可在目标登录时记录其Persona，并利用这种攻击方法恢复密码，进而访问其账号。

**快速修复**

GAZEploit的研究人员在4月向苹果报告了这一发现，并随后提供了概念验证代码，以便这种攻击可以被复制。苹果在7月底发布的Vision Pro软件更新中修复了该漏洞，停止了在使用虚拟键盘时共享Persona。

苹果发言人证实公司已修复该漏洞，问题已在VisionOS 1.3中解决。虽然软件更新说明中未提及修复内容，但其安全专用说明中有详细说明。研究人员表示，苹果为该漏洞分配了CVE-2024-40865编号，并建议用户下载最新软件更新。

这项研究突显了个人数据可能无意间被泄露或暴露的方式。近年来，警方已经从网上发布的照片中提取指纹，并通过监控视频中的步态识别身份。执法机构也已开始测试将Vision Pro作为其监控手段的一部分。

随着可穿戴技术变得更小、更便宜，并能够捕捉到更多关于个人的信息，这些隐私和监控问题将变得更加紧迫。康奈尔大学助理教授Cheng Zhang指出：“随着像眼镜、扩展现实（XR）和智能手表等可穿戴设备逐渐融入日常生活，用户往往忽视了这些设备可以收集多少关于其活动和意图的信息，以及由此带来的隐私风险。”他也应WIRED的邀请，评审了针对Vision Pro的这项研究。（Cheng Zhang的研究方向包括开发可穿戴设备，以帮助解释人类行为。）

Cheng Zhang表示：“这篇论文清楚地展示了注视输入所带来的特定风险，但这只是冰山一角。尽管这些技术是为了积极的目的和应用而开发的，但我们也需要意识到它们对隐私的影响，并开始采取措施减轻未来可穿戴设备在日常使用中的潜在风险。”

**参考资料：wired.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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