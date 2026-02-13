---
title: 生图和编辑二合一！实测阿里最新模型Qwen Image 2.0【附提示词】
url: https://mp.weixin.qq.com/s/cYS5WKmbRoDNKSo_iutSiA
source: Doonsec's feed
date: 2026-02-12
fetch_date: 2026-02-13T04:15:09.861869
---

# 生图和编辑二合一！实测阿里最新模型Qwen Image 2.0【附提示词】

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TLxcOlNibqPicg7rIGQK0rXpibjEW9dCyC7zjbyqtxItqxiaxq6aKaF7vicFxgU3xlEPRTV30wSkxanvd7oHl3ribnonWnbJERxfNERssTY4nuNEQ/0?wx_fmt=jpeg)

# 生图和编辑二合一！实测阿里最新模型Qwen Image 2.0【附提示词】

原创

天欣
天欣

天欣AI

![]()

在小说阅读器中沉浸阅读

可能是临近过年的缘故，AI 圈最近都没消停过，学不过来，真的学不过来了![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_05.png)

OpenClaw 我还没玩顺呢，字节又发布了堪称地表最强的视频生成模型：Seedance 2.0 ，本来打算先实测一下 Seedance 2.0 的，我感觉这个模型还挺有意思的，但是奈何使用的人太多了，我要生成一个十几秒的视频竟然要等 4 个小时！这我真没招了![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_1@2x.png)。

![等待时间超长.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqPicAQKl1yXNXvBKVfibZSicSCj5yWtYffFWnRdBxvJhicgcq1YxN5Cs29QiboohOjd549yDBlMJgEbSkXkRjnwKofuXHhMOu5mFovYY/640?from=appmsg)

算了算了，还是先测一下阿里刚刚发的这个 "二合一" 图像模型：Qwen Image 2.0 吧。

![主页大字png.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqPibgobU5UMDriaw7cWXIKWNpIuQMiapYesniaaW6IUgicICdiaL5WI41nPLIsx4TZO8vFCCeGZfIARicUORsuqm3Ox3qRV5a1Ezp5AVWQ/640?from=appmsg)

为什么我说它是 “二合一” 呢？这其实是因为阿里最开始做图像模型的时候，将图像生成和图像编辑分为了两个不同的方向去发展，也就是在 Qwen Image 2.0 之前的图像模型，要么只负责生成图像，要么只负责编辑图像。

![阿里图像模型发展历史.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPiclEfVCfUtomY5fd4kZjfibzUcSPzWldlzZglzdlydYmWiaibaSWdRxr5RSHsRo6FLQ33VbJYia7Vib5wdIjG6pDlv1EvYW66mClia8M/640?from=appmsg)

此图由 Qwen Image 2.0 生成

对了，关于千问历史模型的测评和对比，大家可以查看历史文章：

[豆包 vs 千问：实测对比，谁才是你心中国内文生图模型第一？（含提示词）](https://mp.weixin.qq.com/s?__biz=MzkxMDc1NzU1Ng==&mid=2247485037&idx=1&sn=f108102ce238f4d2bee1db60aa783804&scene=21#wechat_redirect)

[实测 Qwen-Image-2512：开源文生图的“天花板”出现了！](https://mp.weixin.qq.com/s?__biz=MzkxMDc1NzU1Ng==&mid=2247485028&idx=1&sn=096797ded8cb189f5c6e1e56da747d95&scene=21#wechat_redirect)

[AI 修图进入“图层时代”：阿里的Qwen-Image-Layered 能把图片拆成 RGBA 图层了？](https://mp.weixin.qq.com/s?__biz=MzkxMDc1NzU1Ng==&mid=2247485018&idx=1&sn=8f9f44aed72980a846628b06697437e0&scene=21#wechat_redirect)

所以说，这里的 “二合一” 指的就是图像编辑和图像生成能力的合并。

但是阿里 Qwen Image 2.0 远远不止是能力合并那么简单，对于文字的生成、上下文长度等方面，都做了非常大的提升！

在全球性的模型盲测榜单中，无论是文生图还是图片编辑的能力，都取得了全球前三的成绩：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqP8iaCNIWAaY581OM5ibMtRmBdG4eiaYQowgMnaSEkZcbg3ibS2sP5kSza3KKoNsIiaUInmhPHXVCuwRLPqQv9Kml3jvqpoFmfXR5Ro8/640?from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPibAlUKImiaCIobXuEuGrILeQqs5Hib5MBx0jb79FUoWwUGaHibxk78GPbJhiaNHlBds7bhcyic70fWwiah2TwqRwv47CAD6DWjICcOKw/640?from=appmsg)

所以我们来几个实际的例子来看看 Qwen Image 2.0 的表现如何吧！

首先，我让 Qwen Image 2.0 生成一个课程表，提示词如下：

```
A4竖版手绘课程表，纯白背景，横向五列布局对应周一至周五，每列顶部用马卡龙色块区分：周一柔粉、周二天蓝、周三薄荷绿、周四奶油黄、周五薰衣紫。左侧垂直时间轴标注8:00-8:45、8:55-9:40、10:00-10:45、10:55-11:40、12:50-13:35、13:45-14:30、14:40-15:25、15:35-16:20。每节课用圆角矩形框呈现，框内仅显示学科名称（无“晨读”字样）：周一：语文、数学、英语、体育、历史、音乐周二：英语、语文、数学、美术、道德与法治、物理周三：语文、英语、数学、生物、地理、自习周四：英语、数学、语文、体育、化学、班会周五：语文、数学、英语、美术、历史、劳动顶部居中艺术字标题“初二（3）班 课程表”，手写毛笔字体，周围点缀手绘星星与云朵。四角装饰文具插画：左上彩色铅笔、右上橡皮与尺子、左下摊开课本、右下胶带卷。底部居中手写标语“好好学习天天向上”，自然笔触。整体风格：日系手账风，彩色铅笔质感，轻微纸张纹理，柔和阴影，温暖治愈色调，2K高清，俯拍平铺视角，无文字水印，无真人出镜。
```

最后生成的效果有些出乎我的意料了，竟然毫无渲染问题，简直堪称完美！

![课程表.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqP8pdlJ8B6Mic2WZw8xJpG3NYdeklfeAibd5QTB7YKmQXts6g0chwpw8NCrMsUnsOPc0c5NzGO043sRtSnlmo3EdMEQddqd5LYP5Y/640?from=appmsg)

Qwen Image 2.0 无论是排版上还是具体的汉字渲染上，都非常优秀。

我们再来看看豆包在同一套提示词下的表现如何呢？下面是豆包生成的效果：

![豆包课程表.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPib9Y0icY1dQmAMDXHL7HxmXXzY6jvqdZic6SjbqGD0fkOWbkkeCWHbwvOXZdeaFgrR50t4omKUHb3kViaMxZrIjoLeSQIrMIjywmI/640?from=appmsg)

豆包的颜色和风格我更喜欢，但是在汉字的渲染上，还是有一些肉眼可见的瑕疵的。

这不是马上就过年了嘛，大家也可以让 Qwen Image 2.0 生成一张精美且写实的新年贺卡。如下：

![写实贺卡.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqP8QXRic1ucmtxHb9k2ygzoRE7wcib5QF2Gyia80CrkeicicqlaaOjQYuG6CDkxPoQp2wibkIuCicWg9GozBhJwJp9TmDSqEptuAFNhia90/640?from=appmsg)

这样的贺卡，高级感直接拉满了，而且非常的真实！具体的提示词如下：

```
中国新年贺卡，实体贺卡特写视角，高品质珠光朱红卡纸，表面细腻纹理，精致烫金工艺呈现金色祥云纹样，传统剪纸风格梅花立体浮雕效果，花瓣层次分明，枝干蜿蜒优美，左侧浮雕六角宫灯，镂空设计，红色流苏自然垂落，右侧梅花与灯笼相互呼应，画面中央预留优雅椭圆留白区域，内含烫金文字“祝王周俊 福启新元 春满华堂 梅映瑞雪 灯暖岁长 身安业顺 心栖吉祥 年年胜意 岁岁安康”，文字清晰端正，边缘微微凸起，整体层次丰富，专业贺卡摄影，柔和侧光营造立体感，浅景深虚化背景，2K高清，商业级印刷品质.
```

Qwen Image 2.0 不仅汉字渲染能力顶呱呱，甚至还能渲染不同的书法字体，我靠，这有点意思了！

我特别喜欢李清照的诗，所以我打算使用瘦金体来生成一幅诗词的插图，瘦金体版《醉花阴》，这悲伤感直接拉满了！提示词如下：

```
一幅宋代宫廷风格工笔重彩画：画面中央为一位身着月白色对襟褙子、内搭藕荷色抹胸的纤丽年轻仕女，独坐于太湖石旁的菊圃之中，手执青瓷酒盏，眉目含愁，凝望远处；身旁一丛丛金蕊白瓣的重瓣秋菊竞相绽放，花瓣层层叠叠，花影摇曳；背景为深秋皇家园林，几株丹枫如燃，叶片随风飘零；远处隐约可见重檐歇山顶的凉亭与斑驳青石小径；左下角一尊古朴铜香炉袅袅升起瑞脑香烟，画面右上方一角斜伸入几竿修竹，竹叶间露出一弯淡月。整幅画采用绢本设色，色调沉静婉约。画面自上而下、自右向左以瘦金体工整题写全文：“薄雾浓云愁永昼，\n瑞脑消金兽。\n佳节又重阳，\n玉枕纱厨，\n半夜凉初透。\n东篱把酒黄昏后，\n有暗香盈袖。\n莫道不销魂，\n帘卷西风，\n人比黄花瘦。” 字体纤劲挺拔，笔锋锐利如削，墨色乌亮。
```

最后的效果，我感觉已经可以媲美 Nano Banana Pro 了。

![瘦金体李清照.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqP92nCwVT3RXFuICiaDWuDJXqicRXanLUemIjQSM2iaibfZhZnAI23Xmn9SGShdxGdqXr5xciawnmuboCI5NqMxcRJGjPvAx0J4HPxrY/640?from=appmsg)

这还不算完，官方文档的例子中，甚至你可以将一整个兰亭集序塞进 AI 生成的图片中！

![兰亭集序.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPibdgdakCtS2iaQyhPiaAtgAmmeCZlJsPC8LHxFOmGiatjXVxbqkxXBPOiaHwRnJ5BmVcsA4rOYadn3iaWdybZWoicoWiavVib0RxZVT16I/640?from=appmsg)

官方介绍文档：https://qwen.ai/blog?id=qwen-image-2.0

我们再来看一个 PPT 的生成案例，提示词如下：

```
生成一张信息密集的横版16:9中文PPT页面图片。页面主题：2025年AI助手产品商业化表现页面布局：左侧为关键指标数据卡片、右侧为增长趋势图、底部为文字总结主标题：AI助手产品商业化核心数据（2025 Q2）

左侧四个数据卡片：总注册用户：1.2亿、月活用户：6800万、付费用户：950万、季度收入：3.4亿美元

右侧折线图数据：Q1：收入1.2亿美元Q2：收入3.4亿美元底部总结文字（三条）：用户增长主要来自教育与办公场景、移动端使用时长提升42%、企业订阅收入环比增长63%风格要求：高级科技公司PPT风格、卡片式设计、蓝紫渐变配色、层级清晰、所有中文和数字必须清晰可读
```

最后的生成效果如下：

![PPT展示.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPibicc6qicBia6wwbcWwk09U8PibUB2kibHYIGGLhPZqCXvVAwwGNA6Gj0PvBuqwOmg8mxV6iaTUDefnWRkibuL760ic09t51VRjIdYUE14/640?from=appmsg)

生图能力展示完毕，我们再来简单测试一下模型的图片编辑能力。我随便找了一张网络上的情侣合照。

![情侣合照.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TLxcOlNibqP9zfzx7QyjF8JSaxIY6zopib8DWEI2e3LRvzPRKtUoWV6iaibYLoKGMIxxyjlg90qesDnNEzLJL5EJRlZMGUiaTBpxWibf3cyWic27H0/640?from=appmsg)

然后我想将其转换为Q版小人的那种效果。具体的提示词如下：

```
Q版动漫风格，严格还原人物原始动作和表情，大头小身体比例（头身比1:2至1:3），圆润柔软的轮廓线条，微腮红，日系赛璐璐上色，干净线稿，柔和阴影，纯色背景，高清细节。
```

最后的效果如下，可以看到 Q 版小人的表情和动作都和原图几乎一模一样，稍微有些瑕疵的地方就是男方手心的字母没有渲染出来。

![q版情侣合照.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPibrKwhmzdqFwMAQh7o15YWPmVreelwHgbm8evvibocCmeyLGic0QO9ywMHvd0TUTicqD9bDMFYcXXicdetByxnX2FgiaiaInhk1ySUB4/640?from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNz2bAzZDNvNXR9yvPBwu4HyfdFk7GADDDIbK5DWYWHQDoyyiauJY36pVkQZ8sATZZDRMpbczyBWmJw/0?wx_fmt=png)

天欣AI

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNz2bAzZDNvNXR9yvPBwu4HyfdFk7GADDDIbK5DWYWHQDoyyiauJY36pVkQZ8sATZZDRMpbczyBWmJw/0?wx_fmt=png)

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