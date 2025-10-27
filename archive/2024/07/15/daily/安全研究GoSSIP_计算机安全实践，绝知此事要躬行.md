---
title: 计算机安全实践，绝知此事要躬行
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498439&idx=1&sn=dd3b6e693f4ae9bebe4f6f99a64d1888&chksm=c063d41ef7145d08e450f5040da485279859a7d0aafd40ed496166dcba799aaffed979f054cb&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-07-15
fetch_date: 2025-10-06T17:40:49.326212
---

# 计算机安全实践，绝知此事要躬行

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FHRY0DsEqGZ9mrl60sxBHZwoV4oIz8lO7vcEpo2lyaWlmxdJUOhGuvaRgbsgAn4MAwibXL8Nzj2PQ/0?wx_fmt=jpeg)

# 计算机安全实践，绝知此事要躬行

原创

G.O.S.S.I.P

安全研究GoSSIP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FHRY0DsEqGZ9mrl60sxBHZkoNQHKo92ia6cic8NibETcCb7n3jJb7q6CmYLeSlwcrQVKMgvpCkYdAzA/640?wx_fmt=png&from=appmsg)

南宋宁宗庆元五年（公元1199年）底，大诗人陆游写下了著名的《冬夜读书示子聿》。从此以后，在语文课堂上，我们一遍遍吟诵“纸上得来终觉浅，绝知此事要躬行”，然后努力去践行“*我听过很多道理，却还是依然过不好这一生*”（手动狗头）的每一天。

今天的计算机专业的本科生是无比幸福的，畅游互联网，放眼望去，满是道理：20多年前的2002年，国内的大学还在普及互联网接入的时代，大家突然发现麻省理工学院上线了包含50门课程的教材，起名叫“麻省理工开放课件”（MIT OpenCourseWare）；而随着后续一大批国内外大学跟随着MIT的步伐，互联网学习资源日渐丰富，2010年11月1日，网易也上线了《网易公开课》网站；随着GitHub这样的代码共享平台和Youtube这样的视频分享平台的普及，更多的学子也会把自己的学习经验上传，更多的心路历程得到了分享。似乎今天已经从根本上颠覆了学习的模式，难怪很多人会说“‘你是哪里毕业的？’ ‘我是B站毕业的’”。

“有了在线课程，是不是学校就可以关门了？”，这种问题已经不是第一天出现了，如果互联网能够实现完全的时光回溯，可以打赌，2002年绝对已经有人在思考这件事。直到现在，我们也没有看到大学关门大吉（甚至也看不到这个趋势），除了无法克服的惰性需要人监督你，还有什么问题呢？

我们在设计今年的[暑期学校课程](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498401&idx=1&sn=59d0ee86bf0d2dc6701e26d310c8e87c&chksm=c063d478f7145d6ea29b3718d9ad8ba5c52931386fa3e52bc968862704ecb5da5aeeaebc7b2b&scene=21#wechat_redirect)之前，就随手搜索了一下各位老师的课程资料，好家伙，不看不知道，一看吓一跳，现在想要速通某门课程还真的挺容易的。你不光可以找到这个：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FHRY0DsEqGZ9mrl60sxBHZAJnTVGLfmpELMicljoYWz42fA2LPiaMptynWJE4QOtm6F17mj1KCLP4w/640?wx_fmt=png&from=appmsg)

还可以找到这个：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FHRY0DsEqGZ9mrl60sxBHZfVAQ6QsHfaEZWYeQ6y2P1sRCKoYPsg2CScJS5obFebibyI57PAGZX2g/640?wx_fmt=png&from=appmsg)

除了课程内容，甚至还有人帮你总结了老师是谁，课程风格是什么：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FHRY0DsEqGZ9mrl60sxBHZSrKibMyPVeS1YygG90icP56a3tibicLYC5ia1CL8dDOA1KNANSPWC6T5MRA/640?wx_fmt=png&from=appmsg)

你看看，这恨不得手把手教你怎么考满分的节奏，饼都喂到嘴边了，怎么你还是成不了计算机安全领域的大牛？

不知道大家有没有那种“我看梅西带球过人很简单，自己试试就把脚崴了”的感觉？网络上的知识再多，光看不练，是不是永远找不到诀窍？更重要的是，在大约2001年有一篇文章，里面有一段话是这么说的：

> 高手快的诀窍在于他很熟悉各种东西。高手看书很快，因为每一本新书里，值得他好好看的新技术只有一两章的内容。他能迅速看完，并准确领会这本书的中心思想和价值。而对于一个新手，每句话都是新的，他都需要去理解，每一段例子，他都需要去试。
> 高手喜欢用轻量级的工具，像VIM，notepad，最多到UltraEdit这样复杂的。高手用这种工具写出很多的东西。这些工具就像东方不败的针。那根针已具有神奇的魔力，有时候它可以当激光枪来用。
> 对于一些重量级的工具，高手虽不常用，但一经使出也威力大于常人。如果让东方不败用剑，最厉害的剑术名家也会败得很难看。高手其实用过很多的重量级工具，而且深知其优缺点。所以使出来，就会把威力发挥到最大，而把缺陷减少到最小。而低手则不然，总是把缺陷加以大大地发扬而浑不知其精髓何在。

我们是不是都经历过“总是把缺陷加以大大的发扬，而浑不知其精髓何在”这个阶段呢？也许大家都听说过一个很有名的“一万小时定律”，它是由著名作家格拉德威尔在《异类》一书中提出的定律。他认为，“人们眼中的天才之所以卓越非凡，并非天资超人一等，而是付出了持续不断的努力。1万小时的锤炼是任何人从平凡变成世界级大师的必要条件。” 但是后来很多的研究一直在质疑这个结论，例如发表在1993年科学期刊《the Royal Society》上的论文 *The role of deliberate practice in expert performance: revisiting Ericsson, Krampe & Tesch-Römer* 就说，单纯只是不停的练习，并不能让你成为专家。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FHRY0DsEqGZ9mrl60sxBHZ3aOHmbbY75U6c0zA1yGD6bnNdichp6gjwKK7qKHYmribTp1gg08Fpn2A/640?wx_fmt=png&from=appmsg)

在诸多网络讨论中，大家也会经常提到：“刻意练习需要精心的安排，如果只是强调反复练习，缺乏策略性的苦练，效果并不会很好，虽然总会有效但却无法将效果最大化。”

让我们重新回到“有了在线课程，是不是学校就可以关门了”那个问题来，如果同学们真的只要能够看视频就能学好知识，老师们简直是要开心到做梦都笑醒过来！人类的学习这个过程还远远不像我们训练AI那样可行（再说了，人家AI可以忍受枯燥的重复，你能吗？），个体的差异化使得每个人都需要和老师和同学进行充分的沟通交流，搞清楚自己的弱项，加以改进，方能得到进步。

所以，[Let’s GoSSIP 2024暑期学校](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498401&idx=1&sn=59d0ee86bf0d2dc6701e26d310c8e87c&chksm=c063d478f7145d6ea29b3718d9ad8ba5c52931386fa3e52bc968862704ecb5da5aeeaebc7b2b&scene=21#wechat_redirect)今年要重拳出击，官方逼死同人，老师们亲自来帮你们进步。你们想着速通课程，老师们却希望每个同学都能从课程中最大化地得到成长，例如我们第一天的课程实践，是来自南方科技大学张锋巍老师的计算机本科课程 **CS315 《计算机安全》**，这门课学完了会得到什么收获呢？

> https://cse.sustech.edu.cn/en/news/view/id/845
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FHRY0DsEqGZ9mrl60sxBHZYMC9M25bbwozsC78CPQpnQUvMUEibRMFfHRHlx9cgjFyeia7DDhePQtQ/640?wx_fmt=png&from=appmsg)

嗯嗯，这个广告效果挺好的。如果你想知道张锋巍老师课程团队在2024年7月22日这一天会给大家设计什么样的课程实践，赶紧来报名吧！

当然，如果第一天的内容还不能让你从入门到放弃满足，后面干货可就更多了：被大家誉为浙大系统贯通课程的“总设计师”的常瑞老师及其课程团队，要带领大家由浅入深认识真实的系统，整个实践内容从攻防两方面看系统安全：通过程序分析发现系统的问题，用形式化方法描述并验证系统特性，这个知识密度是不是够大？常老师还表示，实践的内容“可以很简单，也可以很难，现场感受一下🤦‍♂️🤦‍♀️”

为了能够充分折磨大家为大家提供充实的学习内容，复旦大学潘旭东老师课程团队本来是要用他们的“AI安全攻防系列Lab”来给大家练习，但是潘老师表示“我会重新来设计一些lab，尽量让大家在一天之内掌握AI安全研究的几类重要攻击”，每个老师都有一颗虐待善待学生的心！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FHRY0DsEqGZ9mrl60sxBHZEuj3hibFibef41ibvQRBfa7L4PovUdnj89tmLqbJNmRqw7OPjJdL1CwUA/640?wx_fmt=jpeg&from=appmsg)

硬件、系统、AI都齐全了，网络安全自然也不能少，我们请到的重量级嘉宾——清华大学的段海新老师正在清华大学的致理书院“基础学科交叉实践课程”中开设一门《**网络安全攻防实践**》，我们把段老师从百忙中“抓”过来，不需要去清华也能体验相关的精华内容啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FHRY0DsEqGZ9mrl60sxBHZzqAdDwJJBKW7VDnD3NiaxKU3pEKhsknkicicVhayek8ZiaXeF328lz5g1w/640?wx_fmt=png&from=appmsg)

最后，肯定少不了G.O.S.S.I.P自己的特色内容，今年我们为大家带来的主题是《安全漏洞的时空穿越之旅》，抛出了这么一个灵魂发问：如果你现在穿越回到历史的各个时期，你能够拯救数字世界吗？作为一个带着2024年知识、技术和工具的未来人类，在1980年代、1990年代、2000年代和2010年代你能成为网络安全的王者吗？别以为生在牛顿的时代，你就比他微积分厉害，那些历史上出现过的安全问题，可没有你想象的简单，原汁原味复原的历史环境，可能会让你在一开始就败下阵来，怎么样，不服来战啊！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FHRY0DsEqGZ9mrl60sxBHZqUMI650zEC7uicKH4Mbqq8rIVshOIOk9qMMZHSGo2s7ZhfEMpHBtJ8g/640?wx_fmt=png&from=appmsg)

---

过去的9年，我们在暑期学校中邀请了很多老师，介绍了很多的前沿的研究成果，暑期学校的同学中也有很多人成长为安全研究社区的中坚力量。来到了暑期学校的第10年，我们还是要提起那个可能被用滥了的词——“不忘初心”，不是每个人都是学神，但是所有人都需要也应该去参与到一套高质量的安全课程实践中去，把Linus Torvalds的名言挂在嘴边（误）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FHRY0DsEqGZ9mrl60sxBHZAIlpoTrtx1ykvIYyJGvFnPEZ7ia9ME1uf1d9E6iaeERtSia7VmrcMmtnw/640?wx_fmt=png&from=appmsg)

友情提醒，明天（7月15日）就是优惠注册的最后一天啦，[大家抓紧报名](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498364&idx=1&sn=cb274a5852cd36c892b7f5af30882e25&chksm=c063d4a5f7145db3f55ce28d903b8fd7cc67453fb0265b375053ec72230abed9fa8d7d2a51e4&scene=21#wechat_redirect)！（不过正常价格也还好，你去上海迪士尼玩5天，门票都要3500块钱呢，还要排队~）。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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