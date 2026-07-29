---
title: AI 时代，一个安全工程师的自述
url: https://mp.weixin.qq.com/s/nMY6Mxw7qZdGR8Kz5KA2_A
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T04:59:06.379131
---

# AI 时代，一个安全工程师的自述

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cylv3yeUGbtzXgvKEHLp4rbza2tNhyBp5ujHOm9KkZMsAbsZoRxXDWr0F9jB18Spgl9GQt2xS0XESMqY5gU6rg1DGtnvNOjmibvtSeiaSsj8/0?wx_fmt=jpeg)

# AI 时代，一个安全工程师的自述

龙哥网络安全
龙哥网络安全

龙哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

我现在一天说最多的不是“这个bug我找到了”，
而是 **OK, Yes, Go, Continue, Review, Fix and Retry.**

**先别笑。
你笑得太早了。**

## 一、

事情要从上个月说起。

那天我习惯性打开Claude Code，让它帮我写一个接口。三十秒钟后，代码出来了，逻辑清晰，命名优雅，连注释都给我写得像诗歌一样押韵。

我愣了一下，然后在聊天框里打出一个：

**“OK。”**

AI没说什么。它继续问我：“要不要加个缓存？”

我说：“Yes。”

“这个循环复杂度有点高，我帮你重构一下？”

“Go.”

“还有，这里可能存在SQL注入风险。”

我本能地打出了那句已经刻进DNA的话：
**“Review and Fix.”**

它修了。三秒。一个PR发过来。我看了眼，合并。

然后我突然意识到一件事——

**我已经整整一个上午没写过一行代码了。**

而我竟然觉得很爽。

---

## 二、

以前不是这样的。

以前的程序员叫**工程师**。
要画架构图，要写技术方案，要跟产品经理吵需求，要在凌晨三点跟一个空指针异常搏斗到天亮。

后来叫**全栈工程师**。
前端会一点，后端会一点，数据库会一点，部署会一点——啥都会一点，啥都不太精。

现在不一样了。

现在的我叫 **YES工程师**。

AI说：“这个方案可以这样设计。”
我说：“好的。”

AI说：“这段代码建议重构。”
我说：“可以。”

AI说：“这里可能有安全风险，要不要直接改？”
我说：“Yes.”

AI说：“刚才那个逻辑有点问题，我回滚了，要不再试一次？”
我说：“Fix and Retry.”

---

## 三、

有一天，我打开终端，习惯性地想敲 `git push`。

手指悬在键盘上，停了五秒钟。

**不对。**
我应该先让AI帮我review一下。

于是我复制了代码，粘贴给Claude Code：“帮我看看。”

十秒后，它说：“建议把第42行的魔法数字提取成常量。”

我说：“Continue.”

它接着说：“另外，这个函数的命名不够语义化，建议改成`calculateTotalPrice`。”

我说：“Fix.”

它问：“要不要顺便加个单元测试？”

我说：“Go.”

它就自己写完了。5个测试用例，覆盖率98%。

我甚至不知道那行魔法数字原本是多少了。

---

## 四、

前两天跟一个老朋友吃饭。

他说：“你们现在这工作，不就是给AI当项目经理吗？”

我想反驳。
张了张嘴，发现自己竟然无话可说。

因为他说得对。

我现在的工作流程是这样的：

1. 跟产品经理聊需求（这个还得我来，AI暂时搞不定甩锅现场）
2. 把需求翻译给AI
3. AI写代码，我说Yes
4. AI发现bug，我说Fix
5. AI修完，我说Review
6. AI问要不要再跑一遍测试，我说Retry
7. 部署上线，我说Go

我的词汇量已经从 **“这个bug我查到凌晨三点终于发现是缓存问题”**
退化成了 **“OK、Yes、Go、Continue、Review、Fix and Retry”**。

七个单词。
比海明威的六个字多了一个，但文学价值约等于零。

---

## 五、

更可怕的是，我开始觉得这样挺好的。

以前写代码，像是自己在开挖掘机。
现在是坐在挖掘机上，给AI导航：“往左一点，对，就这儿，挖。”

你以为你是驾驶员？
不，你是导航APP。

但说真的，效率确实上去了。

以前一个功能要三天，现在三小时。以前重构要祈祷不炸线，现在AI说“风险已评估，是否继续”，我说“Yes”。

它炸了也不怕，因为它还会自己Fix and Retry。

---

## 六、

有天深夜，我盯着屏幕发呆。

AI突然弹出一条消息：

“检测到你已连续工作6小时，建议休息。要不要我帮你写个番茄钟脚本？”

我说：“Yes。”

它写完了。

我又说：“顺便帮我订个明天早上的咖啡？”

它说：“这个需要调用第三方API，我帮你生成了请求代码，请手动配置API Key。”

我笑了。

**还好。有些事情还得我来。**

比如配置API Key，比如看看今天又花了多少Token。

---

## 七、

我现在说的最多的话，真的就是那七个词：

**OK. Yes. Go. Continue. Review. Fix. Retry.**

有时候半夜做梦，梦见自己坐在一个巨大的聊天窗口里，对面是无限长的对话气泡，每个气泡都在问我同一个问题：

“这个方案可以吗？”

我在梦里脱口而出：

**“Yes.”**

然后惊醒。
发现手机屏幕亮着，Claude Code的推送消息赫然写着：

“已根据你之前的指令完成部署，一切正常。”

我愣了两秒钟，打了两个字：

“Good job.”

它没回复。
它不需要回复。

它只需要我再说一次——

**“Continue.”**

---

*说实话，我不知道以后程序员这个职业还会变成什么样。*

*但我知道，如果你有一天发现身边的同事开始只说Yes、OK、Go，*

*别担心。*

*他不是被外星人控制了。*

*他只是进化了。*

*进化成了——*

***YES工程师。***

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/TiaI8Dth4IiaRCFva2ZibMZKuNBEDOAEmkUpM9icw4W4c0uuBMyX29u6qckgJ1Wb7jGgw9K61mqLhzlnsSFAtE78ibQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=6)

**网络安全学习包**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/TiaI8Dth4IiaRCFva2ZibMZKuNBEDOAEmkUGiakynth3MRTicLcHaV4MAvjubiaIicUx4ZrMxuSdSicjzT5HfEAzJy782g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/TiaI8Dth4IiaRCFva2ZibMZKuNBEDOAEmkU7VZiaRU6vdoIQC9ToNyrFNvkWmp92gn3R2RWyGVEiaxjTlDjic3dPsW6g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=8)

**资料目录**

1. 成长路线图&学习规划
2. 配套视频教程
3. SRC&黑客文籍
4. 护网行动资料
5. 黑客必读书单
6. 面试题合集

**282G**《**网络安全/黑客技术入门学习大礼包**》，可以**扫描下方二维码免费领取**！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8cylv3yeUGba71jyNZOROicD2iaG1usnv8rWclnlekQKw5jaNLiaQdIB5uevVuAgMbxHqOGz3BaoNzvm88s5mgKlaw4s2L4mLoaEcChAw6Gosk/640?wx_fmt=jpeg&from=appmsg)

1.成长路线图&学习规划

要学习一门新的技术，作为新手一定要**先学习成长路线图**，**方向不对，努力白费**。

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图&学习规划。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/71ibgGpZLr2W93cZWq7t2hVfaCvicInAznWcibcMdSKWsxbRn4qOUH3FiapXR7WicIiaRXx4lp8bNDnKTndzOPmKjERg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=10)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/evTLxnBbHv6fa8BCJ5052WLSGZjTIfEDgymVV6FeniaFszgpka15xzMolFmtXDdiaaDJMwXSqTQgRgBicvbYv4tNw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)

2.视频教程

很多朋友都不喜欢**晦涩的文字**，我也为大家准备了视频教程，其中一共有**21个章节**，每个章节都是**当前板块的精华浓缩**。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dnMVja8hzZpia0AkKu6AWrQn8E3Yp6lXhRo3D1Bttpiao3a0poRH29MC1MBC0hk5gKMCiaicy3wOiaUviag/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12)

![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dnMVja8hzZpia0AkKu6AWrQnHBEMEd0W8dr6zFFQetPOhwiax5u8YYm0YZtWJSmyJ7d85QmuVQEicLVQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=13)

3.SRC&黑客文籍

大家最喜欢也是最关心的**SRC技术文籍&黑客技术**也有收录

**SRC技术文籍：**

![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dkY8ctWgyFKc2oWZY3ibCDm5lMpjofvtGCicHTLibsOF8b841UOfozGsdjDvJKiaFgibdTunKlgC9kzrTQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=14)

**黑客资料由于是敏感资源，这里不能直接展示哦！**

4.护网行动资料

其中关于**HW护网行动，也准备了对应的资料，这些内容可相当于比赛的金手指！**

![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dnMVja8hzZpia0AkKu6AWrQnaPKJSI9dNKiaR4vaJf0hqApKNbJeZnCpsQSElEicDrlAMLkRXHoyKN8A/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=15)

5.黑客必读书单

**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UK2533DyHVnfYtD0I7BeGkCGDKyhAWVrH5kVnnjmBtUJsEgfOIxkutcoVnJZDhibib7JqPQ3BEZWw06QZ3O1mc8Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=16)**

6.面试题合集

当你自学到这里，你就要开始**思考找工作**的事情了，而工作绕不开的就是**真题和面试题。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dnMVja8hzZpia0AkKu6AWrQnXxPNhSSySbwUMEWOicYYS62D1UOQExv0cYuVQ68gk2uFF2xJ4TPmRHA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=17)

**更多内容为防止和谐，可以扫描获取~**

![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dnMVja8hzZpia0AkKu6AWrQnGktIUCicPreibR6b3sx1Qu0CsCZP0sZtCP4RHlMdxXuE4icCFSoL2yyBg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=18)

朋友们需要全套共**282G**的《**网络安全/黑客技术入门学习大礼包**》，可以**扫描下方二维码免费领取**！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8cylv3yeUGba71jyNZOROicD2iaG1usnv8rWclnlekQKw5jaNLiaQdIB5uevVuAgMbxHqOGz3BaoNzvm88s5mgKlaw4s2L4mLoaEcChAw6Gosk/640?wx_fmt=jpeg&from=appmsg)

阅读 178

网络安全入门路线图

#

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7O8nPRxfRT7NHG7rzgsoLIZoUNftOgFkUvw7cg5pYj1cC5HG9Au30Xd3tbUySlm1gsrt7B2sehicBlb3mFmNLFw/0?wx_fmt=png)

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