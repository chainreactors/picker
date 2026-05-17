---
title: 从菜鸟到高手：50分钟拿下RFID门禁系统
url: https://mp.weixin.qq.com/s/EQh8rnqW0iC6H6NmxAqQvQ
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:45:11.868842
---

# 从菜鸟到高手：50分钟拿下RFID门禁系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfSicUaR1SkdibNAvNicp1Lv7OC7maR4Oibu0f8FiarFf16I0Yxj8WibaGn4QSpRIr59H5snLSGHIaOTnyvyGFbNnevMCLBgOGYDCAOg/0?wx_fmt=png&from=appmsg)

# 从菜鸟到高手：50分钟拿下RFID门禁系统

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 一位自称两年前还是纯新手的黑客，在BSides安全会议上用50分钟完整演示了如何破解RFID门禁系统。从基本原理讲到实战攻击，连制造一个开源门禁模拟器都教给你了——这才是你需要的知识，而不是几个命令砸脸上。

说真的，RFID这东西听起来高大上，但拆开看真没那么玄乎。

我刚入行的时候就是个小白。两年零基础，抱着个小设备去了St. Con，在RF village撞见Iceman——就是圈里那个大神——他正办首届CTF比赛。我心想这是个学东西的好机会，于是硬着头皮上了。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfSicUaR1SkdibNAvNicp1Lv7OC7maR4Oibu0f8FiarFf16I0Yxj8WibaGn4QSpRIr59H5snLSGHIaOTnyvyGFbNnevMCLBgOGYDCAOg/640?wx_fmt=png&from=appmsg)

猜怎么着？我拿了第一名。

说这个不是炫耀。我想告诉你的是：今天你觉得自己啥都不懂，可能两年后就在台上讲现在不知道的事了。相信社区，相信导师。那边坐着Iceman，还有Woody——就是给我起外号叫ShortRange那家伙，因为我搞不定长距离射频的挑战。

> 所以别怕自己是新手。怕的是不敢开始。

## 先搞懂基础：频段、格式、三件套

射频频谱一大坨，但我们只看两样：低频125 kHz和高频13.56 MHz。记住这两个就够了。

门禁系统就三个部分：你钱包里的卡片、墙上的读卡器、后台的数据库。就这么简单。

来，做个实验：打开手机手电筒照你的门禁卡，能看到那个线圈吧？沿着腕带边缘走的。线圈紧密的是低频，间距大的高频。这技巧够实用。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcL9GJ99hdVibibEU31bCdKEyxxiaYra3dClEa1dHTFKoJGYlGKXSFJS01Braicibk2RFvWFV4DcHwiblLFKicxxBhJZYw3BF7QX9E4ZY/640?wx_fmt=png&from=appmsg)

另一个小技巧：手机贴墙上的读卡器，如果弹出支付界面，那肯定是高频——因为NFC跑在13.56 MHz上。

卡片和读卡器怎么通信？磁感应。就像MagSafe充电一样。读卡器供电给卡片，卡片回传数据。数据是二进制，格式叫Wigand。

记住一件事就行：Wigand里藏着设施代码和卡号。设施代码整个公司都一样，卡号是你的专属。读卡器把信号发给数据库，数据库一对——这人在不在系统里？在，开门。

明白了吧？你只要拿到正确的设施代码和卡号，就能假装是那个人。

### 低频：纯文本式的裸奔

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibelcLOAlWU6cQAITdJLPNJpiaNQm9zJldURhJ7myJnUNrIPAyAEtwCFzSFRLBZP7yWNmGV8AKWEN2Esc0BrrJ9fBKSUrPesBjtw/640?wx_fmt=png&from=appmsg)

低频卡的数据直接明文写在区块0里。你拿设备一读——一码，卡号，全暴露。这就是为什么低频安全低。但很多公司只用得起这个，所以满大街还是低频。

### 高频：加密了，但也没那么安全

高频卡聪明点，把设施代码和卡号挪进加密区。但别高兴太早——大量加密密钥已经被逆向出来了。研究者们拆读卡器固件，硬编码密钥到处都是。基本上现在主流的高频系统，用的都是公开密钥和公开漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfytQQPiaYVG6kfrSMjb1hq1fw2z9MbXrwOV0Oc1IiaBhL0lVibYQp357BAGfTqvBKmoxzekp4fngVwRmicGT0NlEiasoGvv0cUXEhM/640?wx_fmt=png&from=appmsg)

接下来我教你的三步攻击法，管的就这些系统。

## 三步攻击法：别急着掏工具

太多人拿到Flipper Zero或Proxmark就开始瞎扫。这是最大错误。

第一步：侦察。这是低频还是高频？谁制造的？有没有公开漏洞？

第二步：明确目标。你要克隆卡？还是干脆不碰加密、直接搭线窃听？90%的读卡器用Wiegand协议——白色和绿色两根线。你直接往线上发二进制信号，门就开了。搞什么加密？

第三步：选工具。前两步决定了你用啥。

> 我办过40多种RFID挑战的CTF，第一个问题永远是：你知道目标是什么吗？九成人不知道。

## 工具三件套：从入门到专业

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcHCRsjxmbeoSpFdbbExZj7fib4gygTzaPtq21MGdlcDRdvChv12mdibI2ZpSIkq1lrHjFOPgocLYyrEsibFGdgnVcMZPLqQFHJtw/640?wx_fmt=png&from=appmsg)

### Flipper Zero：瑞士军刀

不是最好的刀片，不是最好的开瓶器，但每样都能干。低频是它的强项，高频正在变好。我们来演示一下——志愿者上来操作——看到没？一读就显示设施代码和卡号了。就这么简单。

关键是，别满足于“克隆了张卡”。这不是终点。

### Proxmark 3：行业标准

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibe4GfIbkl7iaQ0GbJ1JTXHWvKYjehiaS23KNbfsAT1tIf1BSqVTljgx0o5J2lH2T40FanVFW06A1aj35g0cbsbRWrICD352QuxBI/640?wx_fmt=png&from=appmsg)

45到450美元，看你选什么版本。初学者买512KB版本，别贪小便宜——内存容量很关键。

两个线圈：紧绕的是低频松绕的是高频。插上设备，打命令`lf search`或`hf search`，系统就会尝试跟你手里的卡片握手。

遇到卡住的问题？敲`tack h`看帮助。Iceman说的。

### ESP密钥：攻击型读卡器

这东西塞在读卡器后面，变成攻击型读卡器。就算我不知道卡片的密钥，也能从背面拿到正确的二进制数据。

## 最大的痛点：有工具没靶场

这是我最常被问到的问题：在家怎么练？

你说你在真实系统上练？进机场？想坐牢。对着学校系统试？想被开除。没有靶场，学RFID就像只有开锁工具没有锁。

所以我花了一年时间做了个东西——

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdWaWyQsYlVaORcEibLdu2HjkUib4hianR970XfuPBGOezapQo7XiaLL8ZMn7I7ibjVNBHkXmibicW1Tm3ibgcA1YIdV6ZfcpTTjzDPp9g/640?wx_fmt=png&from=appmsg)

OpenDorsen。

开源门禁模拟器。所有零件亚马逊上就能买到，不用订制PCB，固件一样跑。背面有MagSafe环，能吸钱包或支架。磁吸贴片砰砰响——这个声音太解压了。

大学生教育工作者自学狂魔——这个就是给你们做的。

## 现场搭建：30分钟教你做门禁系统

看好了。接线：两根线。D0（绿色）和D1（白色）。我记这个的笨办法——草是绿的，天是白的，零对绿一对应白。现在你忘不掉了吧。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibff4XSRSRImBU5qEBqpXU3YsOD5d3MujzowG0nicmmePBDmFeDlialkBVvsWMSySswUOYaWVwCD4IRPHmJ45h7DoaTQXkcuJ9HMg/640?wx_fmt=png&from=appmsg)

便携版装进螺丝端子，接5伏电源和地线。30分钟，我们就在台上搭好了一个能跑的门禁系统。

插电接WiFi打开网页。硬件菜单能看到输出数据，原始模式扫任意卡片——信息同时显示在屏幕上。

CTF模式更狠。设置挑战卡，输入设施代码和卡号，添加用户。然后拿你的克隆卡来测试——要是匹配，门就开。如果你在公司的系统上找到漏洞，这样提交给安全团队，至少不会被炒鱿鱼。

> 我经历过。

## 完整攻击演示：10分钟从陌生到开门

场景：我是一个戴着工牌的普通员工，要去有零食的秘密楼层。旁边站着三个小伙伴——一个是电梯门，一个是社交工程师，一个拿窃听读卡器。

社交工程师跟我进电梯，聊了个家常，瞄到我工牌上的信息。然后他拿读卡器一扫——二进制数据全抓出来了。

26位格式设施代码15卡号41885。记好这个。

这哥们跑到电脑前，打开浏览器连上ESP密钥，日志里跳出十六进制数据。复制粘贴到Proxmark，敲`lf em4x decode -raw`——砰，设施代码和卡号全部解码。

然后他拿空白iClass卡，敲`hf iclass encode`。写入我们的设施代码和卡号。注意，iClass用的默认密钥ki0——很多安装都不改。

写完后再敲`hf iclass dump`验证——里面确实是我们写进去的数据。再加一条`hf iclass decrypt`解密，确认没错。

然后，门开了。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdJCP9ic5n4f9jMMMibWgmDLSDSJfo2oE86Mh3KKzw2pFic0CzJcYC55MfDd7CWKia1Zj83qTgOJXB6JibCP3X6MlgOdlYlib8xWDyDs/640?wx_fmt=png&from=appmsg)

那哥们拿着克隆卡刷了一下——"访问授权，欢迎享用零食"。

台下一片掌声。

这就是10分钟从陌生到进门。从头到尾，没有任何魔法。

## 不是终点，是起点

两年零基础做到这个程度，不是因为我多牛。是因为我去找导师去参加CTF，去拿免费的资源学习。

IcemanWoody这些大神——他们不仅做出好公司和好项目，更重要的是他们是好人。愿意提携新人，愿意分享知识。

你也可以。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfYqwA9pNiawfHicC350oLSkxicLHhzC3LI51fgcsRUd1WxeBSj20vE4Dib9JyQQrS2sCtlFI1NFGj9TPicrPvmVuAODNavRGxVn2aE/640?wx_fmt=png&from=appmsg)

所有代码在GitHub上。文档还在写，但我先把它放出来，你可以现在就上手看。

我今天在这里熬夜做这些，用宿舍的3D打印机吵醒室友——这些都是我自己的热情。我相信你也可以找到让你兴奋的东西。不一定非得是RFID。只要相信自己的学习能力，相信社区的力量，去做那些让你两眼放光的事。

做那个愿意帮助别人的人。

谢谢BSides。

---

> 来源地址：https://www.youtube.com/watch?v=UbCxSDWRlDk

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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