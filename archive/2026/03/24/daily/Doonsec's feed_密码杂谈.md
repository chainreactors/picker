---
title: 密码杂谈
url: https://mp.weixin.qq.com/s/WUCuhLZGNo9Ey3N58aTs0A
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:14:40.295625
---

# 密码杂谈

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wRiczRKCKsT3ga5HmkiaiaABv8PMUud4KPrzlgibCprrAp07RrB20lsVBbn4NxoYsWxNM1ScuugWQQASQnbTRNic7ib2bxC14j7cAB5ibq4vTdv0T8/0?wx_fmt=jpeg)

# 密码杂谈

小杨
小杨

网络安全小杨

![]()

在小说阅读器中沉浸阅读

作为一位网安系密码学专业的学生，我是时候该回归一下自己的老本行---密码学

其实，作为一个很“新”的学科，它时刻被应用在我们的生活中，但是大家好像都没有感觉到，很多方面，大家可能都是：“我靠，这个方面竟然用到了密码学”

相信读者们都意识到了，上面的“新”字被我放在了引号中，没错，这个学科并没有那么“新”，这个学科其实很早就出现了，让我们把时间拨回古代，那时候还没有密码这种说法，但是大家或多或少都听说过古人那些手段，例如：大名鼎鼎的凯撒密码，姜太公的阴书，阴符，等等，可能以现代人的视角来看，这些加密方法简直是小儿科，这些保密方式就好比我们小时候和好朋友传纸条，但是 你们还不想让别人知道你们说了啥，你和你的好兄弟约定了一些符号，代表你们沟通的字符，什么拼音，英语字符，颜文字......

例如这样：

![](https://mmbiz.qpic.cn/mmbiz_png/wRiczRKCKsT1mZVNGvab9MyDnmhzkBNc2VYrtCqI7h7EwZRdd6F42micKF1WKr5OrkhPUHUvsGhgQXCdraZqA7jDH4zfLDtF33epq9Pp4huVc/640?wx_fmt=png&from=appmsg)

或者这样：

![](https://mmbiz.qpic.cn/mmbiz_png/wRiczRKCKsT0XicZtJNlPxctSXxqqpAg2EMQhs4WEpQo0wGvKOd27S991EsMcdEWYe8D9TtZPzW68fibnv2XFguX8WVRyQd2fn4WibugjWcEeXU/640?wx_fmt=png&from=appmsg)

当然，当你和你的兄弟使用过多次这样的符号，同时老师也截获了你们一定的纸条时，老师可能就会通过找规律的方式破解你们的悄悄话，这很不安全。

其实作为古典密码，无外都是各种各样的字符替换，字符隐藏 ，只要得到足够的样例，结合一定的情况和分析，就可以得到密码的破解方式

这些古典密码看上去很简单，不是吗

接下来让我们隆重介绍一下，最伟大的古典密码------‌**恩尼格玛密码（这不是骂人话）**

恩尼格玛是音译的希腊语，在希腊语中，它叫做秘密

那么作为一个典型的多表替换密码，它到底神秘在哪里，又有什么本事称得上最伟大的古典密码

作为二战时期德意志所使用的密码，他可以说是古典密码向现代密码过渡阶段的产物，它使用机械和电子设备来实现多表替换和移位，那它里面是什么样的呢，他又是如何工作的呢？

![](https://mmbiz.qpic.cn/mmbiz_jpg/wRiczRKCKsT3op7QB3mv5XxcYAWrVicZWN6Tjib3hN3icbibAdsQ2t88sVc7icaiaib0XW9FHXgaUDtAasTHWVeaWFGV850eO4JvKIYjkoMe0fWvNaU/640?wx_fmt=jpeg&from=appmsg)

看起来有点像老式的打字机，可以看到，他的键盘和我们的键盘没什么区别，都是26键，可以看到，这台机器旁边有三个转轴，可别小瞧这三个转子，他们可是这台密码机的主要工作部件。

首先，请大家在大脑里面构想三个转盘，每个转盘上都刻着从A到Z的26个字母，构想好了吗，我们要开始“转”了。

每个转子内部都有一套独特的线路映射：比如按下字母 A，第一个转子可能会把它变成 E，第二个转子再把 E 变成 Q，第三个转子把 Q 变成 M。

每输入一个字符，最右侧转子会右移一格，改变字母的映射关系；当右侧转子转满一圈（26 格），就会带动中间转子转动一格；中间转子转满一圈，再带动最左侧转子转动一格。

这样的动态加密方式，以当时的计算能力根本没法破解

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wRiczRKCKsT1BGDefkx8nmsJNafJxDXyCylIAeZHBMG6Tb3USCUjLyvGiaUG6nicDESt5cQBj1ndbGjkalEf1RWoXCEo3oljiaxeOh29icdUOBag/640?wx_fmt=jpeg&from=appmsg)

这样看是不是能清晰点

当然，你以为这就完事了吗，当然不是，哪可能这样简单，这台密码机还有另外的措施，来保证他的密文更难被破解

首先便是——反射器（可以理解为镜子）

那这个“镜子”又是“照”什么的呢？

准确说，他个功能不是“照”，而是“反射”，当字母走完了这三个转子，经过反射器，字母又被反射回去，再次走一遍三个转子，这也意味着，即使是相同的字母，也会被加密为完全不同的密文，同样的，当解密的时候，只要有相同的转子设置，就可以轻松解密。

其次的设备叫做插线板

没错，就是你们想的那个插线板，它负责先将任意两个字母先连接一下，也就是说，当字母还没有进入转子的时候，它就已经被替换了

有点晕，让我们以A为例子跑一遍：

假设转子初始位置为 `AAA`，插线板设置为 `A↔F`，要加密字母 **A**：

按下 A → 插线板把 A 替换成 F；

F 进入三个转子，经过动态映射变成 K；

K 进入反射器，反射后变成 X；

X 反向经过三个转子，再次映射变成 P；

P 经过插线板，最终输出密文 **P**；

输入完成后，右侧转子转动一格，位置变为 `AAB`，下一个字母的加密规则完全不同。

好像只转换了9次，这很难破解吗？

还真的很难，接下来我们使用概率计算一下这密码是否能够暴力破解（这里会用到高中的数学知识，各位观众扶好站稳）

转盘选择：从 5 个转盘里挑 3 个，有 5×4×3 = 60 种

转盘初始位置：每个转盘 26 个位置，26×26×26 = 17576 种

插线板：最多连 10 对字母，组合数约 150万亿种

全部乘起来，密钥空间大到天文数字，在那个时代，这根本无法破解

那密文又是如何转换为明文的呢

这很简单，只要加密方和解密方的设置一致，只要将密文输入进去就可以得到明文

总结一下：

加密：明文 → 插线板 → 转子（转）→ 反射器 → 转子（转回来）→ 插线板 → 密文

解密：密文 → 插线板 → 转子（转）→ 反射器 → 转子（转回来）→ 插线板→ 明文

只要转子位置和插线板一致，机器会自动把密文 “翻译” 回明文。

那这样伟大的密码是如何被破解的吗，未来又有什么密码现实呢，且听下回分解

写在最后的话：{有关于密码学的介绍会做成一个专辑，小杨坚持更新哈，最近学院事情不少，小杨很忙，希望读者对于不定时更新报以理解，感谢大家}

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rgwbiaeeibAp9lAWWeoPncH248nwjhBtpJcfxRibSAlCichobdJF5Xf9gYmZEQ5QNjqpqpEWibFiaa92fxPo6F9dMJDQ/0?wx_fmt=png)

网络安全小杨

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rgwbiaeeibAp9lAWWeoPncH248nwjhBtpJcfxRibSAlCichobdJF5Xf9gYmZEQ5QNjqpqpEWibFiaa92fxPo6F9dMJDQ/0?wx_fmt=png)

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