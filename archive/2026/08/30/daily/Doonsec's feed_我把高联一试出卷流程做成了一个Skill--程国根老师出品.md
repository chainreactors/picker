---
title: 我把高联一试出卷流程做成了一个Skill--程国根老师出品
url: https://mp.weixin.qq.com/s/_7yWYad7dCmBzdJlOhZMhA
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:52:15.987055
---

# 我把高联一试出卷流程做成了一个Skill--程国根老师出品

# 我把高联一试出卷流程做成了一个Skill--程国根老师出品

简单读写

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

编者荐语：

这个是 程国根 老师做的一个skill，我已经阅读了他的skill的一些流程，里面有很多规则性的东西以及python代码，不止是纯“提示词”的skill，我通过阅读skill学到了高联一试的出题方法以及题型和给分这一块的知识。

以下文章来源于恩次方根
，作者程国根

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM7tJCbYJSThFsuWYGAhwzTu9GRv18vNBVpbd9YDyCm2tw/0)

**恩次方根**
.

主要发一些日常解题记录，不定期更新。

这一个月，我一直在折腾一个很具体的东西：让一套出卷流程按高联一试的结构，自己完成候选题生成、解答、筛选、校验、排版，最后给出可以打印的试卷和参考答案。

最早的想法很简单。高联一试的结构固定，8 道填空、3 道解答，80 分钟、120 分。如果把题材、难度、解答格式和排版要求都写清楚，应该能跑出一套像样的模拟卷。

做了几轮之后，坑很快就出来了。

11 道题凑齐不难。难的是题位要对，Q6 不能突然比 Q5 简单很多，Q9～Q11 不能只是题面长；参考解答也不能在最该展开的地方留一句“分类可得”。再往后还有原创性检查、PDF 排版、逐页检查，以及一个很现实的问题：流程会不会自己写出一堆 PASS，然后把没做好的东西放过去。

现在这套 Skill 做到 R5.2。我把它当成一个半成品，离稳定使用还有距离。

先把当前版本跑出来的一套卷子放出来。它是一次真实输出，也正好保留了目前还没解决干净的问题。

## 先看试卷

![](https://mmbiz.qpic.cn/mmbiz_png/8ibDNcwCoiaUzSLbHJDYqBRSZ7NHQ1jIyulqqWK5Bpff1HKaLWWZkJrq2KqYwKeZCpLHLMJu6ia9ibBIsRk5gbpBSmKc95uBQFPqCiaMu1YGBNW4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8ibDNcwCoiaUxe5ChB0fD5ic9sUicSJXXWsfo6pTa1SibCkoMo5IH9CRHL7zfnGDYUXZCGyPXnhiaDqnQSdb1uA758WAoiaaUkDWq8mqS5tzkiazpKo/640?wx_fmt=png&from=appmsg)

<<< 左右滑动见更多 >>>

这套卷子采用高联一试常见结构：前 8 题填空，后 3 题解答。当前版本已经能把题目、分值结构和正式排版一次生成出来。

## 再看参考答案与评分标准

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8ibDNcwCoiaUw4ia2QpnaJ6jVcdOvzbVibhvSzqnSvkaAibjulueyll6KL0iaEqqLuF4QNAvCSqKE5k9SG8pdUdHc0zyQjTgFnjxBpAn8Fx2Uxybo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8ibDNcwCoiaUxsxArGPhibNsPfYC0kPS4iaicVhqpicbgDUuicmmnsovpqHtrQ5xBR6oJFkK0Oc3c1w9GKoo9k0iadhXkQqPtdic2dEXbGpcLw2eRzms/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8ibDNcwCoiaUxabNLh69M8zmCPZZ0NBMJA1srSr7xFGibNl5HTfL1RSVrzgNcqmic3lOv0PW31aKXoCOW3r08cB7a2hAL8lRiasv1Ckc06RC9bWY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8ibDNcwCoiaUyhGibYMEibibvhG2oUlibiazEibzMLUXX4HuCZQcEew9fNt7Wc3UicDbUzBPqcSibbbLOYCibv73eib7TgyZ1mc3jRtj3wAoZ1RQ9qQaMWg/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8ibDNcwCoiaUzBtDntpN8bc3x0DpGccs5QsmIoJmQZldPxcZvfo8bMibrIERcVZXaywlsAicrw9En2Tm7p7PSwrk2Vwic7pjMgQqTw1vQ7MfzvpM/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8ibDNcwCoiaUxCLeBmjeLjA05ic1bbeBDyIhAicFOFQgyk7cSdSZOegtgkBJzgRwHp08dgKCa6BibXldPwz1EfRtzdQtfjKsESpsgBKGXoEicibJSw/640?wx_fmt=webp&from=appmsg)

<<< 左右滑动见更多 >>>

这份解析里，填空题给出答案和过程，解答题按评分节点排版。形式已经比较接近我想要的样子，内容质量还需要继续打磨。

## 这套样卷现在有什么问题

我暂时不会把上面这套卷子当成“成品示范”。

它刚好把几个问题暴露得很清楚。

第 9 题和第 10 题偏简单。两题模块不同，一个是解析几何，一个是立体几何，但实际做起来都比较接近“建系或参数化—套公式—整理恒等式”。放到 16 分、20 分的位置，思考量还不够。

第 8 题的答案没有问题，不过参考解答在最重要的分类计数处写了“按连通段数分类，可得……”，随后直接列出一组数字。对一份正式解析来说，这里应该继续展开，让学生能看清这些数到底怎么数出来。

我还发现一个更麻烦的问题：早期版本会把“求一个交点、算一个距离、整理一个式子”记成三个独立难点。这样一来，一道很顺的题也可能被评到很高的位置。候选题数量看起来很多，也不代表里面真的有足够强的 Q10、Q11。

这些问题现在都被当作回归样本留在系统里。下一次再遇到相同类型，程序会优先把它拦下来。

## 这个 Skill 现在怎么出一套卷子

这里说的 Skill，可以理解成一套可以重复运行的出卷工程。里面有规则，也有实际执行的校验脚本。

一轮出卷会先产生不少于 16 个构思，再选 13～14 个做完整解答。这个阶段不给它们贴 Q1、Q9、Q11 的标签，只编号 C01、C02……先看题本身。

候选题随后会经历一次匿名审题。审题时重新找最短解，看看入口是不是太熟，找到入口以后会不会一路机械计算，能不能很容易改成填空题。

等这一轮结束，才开始给题目分位置。

现在我还给候选池加了一个比较硬的要求：准备选 Q10、Q11 之前，池子里必须先有足够数量的高位候选。池里没有，就继续补题。不能从一堆中档题里挑两道最难的，然后把题号改成 Q10、Q11。

## 最后三道题会再被“压缩”一次

Q9～Q11 写完正式参考解答以后，还要重新检查一次。

这一步不看前面的自评，只看最终题面和最终解答。

比如一题最后只剩下：

建系、点面距离、外接圆公式、恒等式整理。

程序会把它识别成一条比较标准的公式路线，并限制它能进入的题位。类似的短路线会一点点积累成回归库。

我现在更愿意用这种方式调难度。已经发现的简单题，下一版不要再犯。新类型继续靠真实样卷去暴露。

## 题材不同还不够

早期我主要限制 Q9、Q10、Q11 的题材不能重复。

实际跑起来以后发现，题材标签有时候很会骗人。

解析几何可以是坐标计算，立体几何也可以是坐标计算。题目表面分别写着抛物线和三棱锥，学生做题时却在重复同一种工作。

R5.2 开始检查三道尾题的大致解法路线。题材、入口、后续动作都要尽量拉开。

这个部分目前还比较粗，需要继续靠老师和学生的实测来校准。

## 参考答案也要过检查

参考答案现在单独有一组检查。

我比较在意两种情况。

一种是关键计数直接给数字。比如前面的第 8 题，最需要展开的地方正是那组分类计数，解析里就应该交代清楚。

另一种是高分解答题在最后写一句“直接整理可得”。如果这一步占了很大的实际工作量，解析应该展开。

对学生来说，题目只是一次训练；解析决定这次训练最后能留下多少东西。这部分我会继续往教学可读性方向调。

## 原创性检查也还在试

目前每道题会从题面、结构和解法三个方向做公开检索。

这里踩过一个很典型的坑：三个查询全部搜不到结果，看上去很安全，但也有可能只是关键词写得太窄。

现在遇到三类查询都为 0 的情况，会自动换成更概括的数学机制继续搜。

如果搜到相近题，也不能只看数字、初值、最后问法有没有变化。数学机制很接近时，仍然要提高风险等级。

这套机制只能降低明显撞题的概率。我现在不会给任何一道题写“绝对原创”这样的结论。

## PDF 也有自己的检查流程

题目通过前面的检查后，会生成 TeX、试题 PDF 和解析 PDF。

PDF 会逐页导出成图片，再做一次页面检查。现在每一页的检查记录都会和那一页图片的 SHA-256 绑定。

这么做是为了避免一个很容易忽略的问题：检查完版本 A，最后发布时又重新编译出版本 B。R5.2 里，逐页检查完成以后不会再重新编译。

最终发布前，还会从原始候选题、盲审记录、最终题面和解答重新跑一遍主要校验。以前生成出来的 PASS 文件只能作为记录，最后还得再算一次。

## 目前就是一个半成品

R5.2 还处在调试和开发阶段，目前适合拿来测试、挑错、收集样本，不适合把每次生成的结果直接当作正式训练材料。

尤其是难度。高联一试的题位感很依赖长期做题和教学经验，仅靠程序规则很难一次调准。

我现在最缺的也正是这部分真实反馈。

有些题在生成阶段看起来很漂亮，学生一做几分钟就结束了；有些题程序觉得步骤不多，实际课堂上却卡住一大片。这样的反馈比再加十条抽象规则有用得多。

## 想找一批老师、学生和家长一起测试

接下来准备建一个小范围测试群。

群里会放测试版本、样卷和更新记录，也会收集错题、坏题、排版问题和功能建议。

欢迎感兴趣的朋友进群。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8ibDNcwCoiaUzoVk1DuhmKxY8cIebJNtBsWqB5O0wCQZPOnzWHDnsD2icF8bw4Kpn5j2bKHqjwo5s3gdyQKZ2DqiaVZdxORbSBBsX4F6tOXIAbY/640?wx_fmt=webp&from=appmsg)

为避免无关人员进群打扰，入群请进行备注。

## 后面准备怎么做

短期先把几件事继续做扎实：解答题的难度、参考答案的完整度、原创检索，以及每次坏样卷的回归测试。

我也会继续把实际失败保留下来。

哪一类题被老师认为偏简单，哪一类题学生实测很快，哪一种解析经常跳步，就把它变成下一版的测试用例。

等流程稳定一些，校验规则和样例库也整理清楚之后，我会把这套 Skill 和配套脚本开源。

到时候希望它能成为一个可以继续修改、继续补规则的公开工程，大家也可以拿自己的坏题去测试它。

现在先从一个半成品开始。

欢迎进群，帮我挑错。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OCOHF928I9a7kKm699bm7hDv8HmzINwuiaytTT1Id92xDSIcRMYKwlo5K9yDeCr2aPoWKxpibdsEn6pqGPpnaclA/0?wx_fmt=png)

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