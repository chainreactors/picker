---
title: AI 生成人物视频翻车？商汤推出可控人物视频生成模型 Vimi
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653047035&idx=1&sn=797c17eb7785d4864c5972613ae98f82&chksm=7e57354d4920bc5b7023e39e261cb1430c627594bf5b84d19afdd2551df910c9335f61281c7e&scene=58&subscene=0#rd
source: 极客公园
date: 2024-07-09
fetch_date: 2025-10-06T17:46:01.983009
---

# AI 生成人物视频翻车？商汤推出可控人物视频生成模型 Vimi

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5aTKEIiaWxIULl9gG52icv9oTN26XRclnGSPaVkVy7IicYcc0X0quB5B3bB8GCpluRRNDatpzkgIjB7A/0?wx_fmt=jpeg)

# AI 生成人物视频翻车？商汤推出可控人物视频生成模型 Vimi

原创

Li Yuan

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5aTKEIiaWxIULl9gG52icv9oTFzrvibmZaicVKiaG5w3mia5x4IhaXOibK31nW9OX7Lf3dzUyKENXUiasa2pQ/640?wx_fmt=jpeg)

商汤推出「可控」视频生成模型 Vimi，可精确模仿人物微表情。

**作者 | Li Yuan****编辑**| 郑玄****

6 月，又是 AI 视频生成的一个重要月份，Runway 3、Luma AI、快手可灵纷纷推出了普通用户可用的视频生成模型。用 AI 生成视频，距离我们越来越近。

不过，相对于对话式机器人、AI 图片生成这些成熟的大模型使用场景，「AI 视频」离走出尝鲜还有一定距离。比如，无论是在影视剧里，还是在短视频中，视频的最重要的场景之一就是人脸，而在网上的视频生成测试中，最容易翻车之一的场景，也正是人脸。

下面是笔者用 Luma AI 尝试通过一张科学家图灵的照片生成的视频，让人物本身动起来相对容易，但一旦动起来，图灵的脸很快就变成了另一个人。

Luma AI 生成

在大模型和智能视觉技术领域有深厚积累的商汤，希望解决视频生成中这种「不可控」的痛点。最近在上海的 WAIC 2024 上，推出了最新的人物 AI 视频模型 Vimi，主打技术的「可控性」。

同一张照片，在商汤的演示下，生成是这样的。

视频来源：商汤 Vimi 模型

不仅光影和谐，且人物的一致性保持度极高。

商汤是怎么做到的？

**01**

****第一个人物「可控」****

****的视频生成模型****

据极客公园了解，此次的可控人物 AI 视频模型 Vimi 模型，由商汤数字文娱团队出品。

商汤从 2016 年开始，就持续深耕在人物表情的 AI 处理上，是亚洲地区最大的特效引擎提供商。作为用户，我们可能提起小狗滤镜，变脸特效，只能想起抖音这样的 C 端软件，不过其实背后，许多这样的特效的提供，都来自于商汤数字文娱团队。

去年，早在 Sora 的 demo 发布之前，他们就开始立项，进行可控人物 AI 视频模型的研发。重点发力「人物」、「可控」两个难点。

在视频生成中，可控性其实一直是不少模型努力的方向。

在 Vimi 模型之前，其实市面上已经有一些模型，能够较为可控地生成人物动作。

其中最出圈的，可能就是阿里出品的 AnimateAnyone，也就是曾经让兵马俑也能跳「科目三」的背后技术。

采用了姿态引导器（Pose Guider）的技术，通过 Denoising UNet 模块进行视频的生成，AnimateAnyone 能够让人们在只输入一张图片的情况下，让图片做出姿态引导器所做出的动作。

简单讲，科目三的动作是被提前设置好的，而输入照片后，AnimateAnyone 可以让一张照片中的人物按照科目三的动作动起来。

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5aTKEIiaWxIULl9gG52icv9oTozshUDlWf3Kh7eibukP2B2OnicAZuBtQLPV4nTliaTia4F1EoVGQ5afuhQ/640?wx_fmt=gif&from=appmsg)AnimateAnyone 生成

不过很明显可以看出，AnimateAnyone 的姿态控制，更针对大范围的肢体动作。

而商汤团队的优势，在于塑造人物表情上更加鲜活。

同样是同时输入一张图片，和一个动作（可以是动画模型的 3D 骨架动作，也可以是一段视频），商汤的 Vimi 模型，能够做到对脸部和上半身动作进行精准地控制。这也是目前发布的第一个能够对人脸和上半身做如此精准可控的模型。

视频来源：商汤 Vimi 模型

商汤表示，模型训练本身，并没有使用特别的数据，只是采用了公开数据库进行训练。

而**能够在人脸方面，成为第一个精准控制人脸表情的模型，主要源于商汤多年在面部跟踪方面的积累：**「对人脸实现技术角度的精准控制，需要更精准地去跟踪人物表情中的每一个细节，包括牙齿、耳朵、眼球、睫毛等等。细节能够做的好，在人物的参数化上就可以做得非常的精准，之前的技术积累都是实现这个模型的前提。有了这些积累，真正训练的时候，使用的数据量可以少许多。」

事实上，除了专注于面部的可控之外，商汤的 Vimi 模型和 AnimateAnyone 在底层架构上也不同。AnimateAnyone 使用类似 ControlNet 的方法，从图像中的身体部位提取一些锚点，作为生成视频每一帧的动作参考；而**商汤的 Vimi 模型，****将人的动作和表情做了全面的理解和抽象，将整段动作信息作为一个整体，与生成模型对图像和视频信息的特征理解相融合，**这样生成的视频在空间和时间上都能保持很好的整体性。不同的训练架构，导致从生成效果来看，商汤的模型，对光影一致性的控制，效果非常优秀。

「传统模型最大的一个问题是，它不太能合理地生成周边的内容，包括身体的动作和环境的一些变化。而**采用大模型训练，可以整个的环境都跟着肢体的控制去变化，包括生成合理的头发的抖动。甚至能够模拟镜头角度，**比如输入镜头是逐渐拉近，输出也能有自然的逐渐拉近的效果。而原本，要做出这样的效果，需要复杂的 3D 建模，绑定各种光效渲染才能做出来。」采访中商汤表示。

视频来源：商汤 Vimi 模型

而与专门的生成式模型比起来，可控人物 AI 视频模型又在人物生成效果稳定多了。尤其在长视频的情景下，能够稳定保持人物的脸部可控。目前，团队可以做到一分钟以上的稳定视频生成。

Vimi 模型使用情深深雨濛濛视频片段作为控制生成的长视频

**02**

****可控，才可用****

人脸生成，是 AI 生成视频中最难的场景之一。

原因，首先是因为人类对人脸本身就很敏感。一个细微的肌肉表情，就能被解读出不同的含义。人们自拍经常要拍几十张相似的照片，才能挑到合适的角度。因此涉及到人脸的一些形变，很容易就会引起我们的注意。

而其次，人脸生成本身，存在一定技术难度。人的身体，并不是一个刚性的物体——刚性物体，只要对其进行环绕拍摄，模型就能很容易学习其物理属性。而**人体本身，有许多关节，人身体上会穿柔软的衣服，人脸周围有毛发，对于模型来说，学习难度就会更高。**

然而对于创作者来说，人脸视频生成却是最不可或缺的一块。

无论是影视作品，还是短视频作品，用人脸去传达感情，都是重要环节，无法被替代。

而商汤布局于这块硬骨头，也正是源于商汤多年在 B 端积累的客户洞察。

商汤科技数字文娱事业部总经理栾青在接受采访时表示：「我们和许多做动画电影的人聊了之后，发现他们普遍想要讲好一个故事。而**现在的大模型，无法进入生产流程的最大问题，就是没有一个很可控的方法，让他们电影中的人物，真的具有表现力。**最后 AI 视频还是只能用在过场的大场景中。」

而布局可控模型，也与商汤对于今天的大模型发展看法一脉相承。

在刚刚结束的 WAIC 上，商汤科技董事长兼 CEO 徐立提到，大模型技术走向应用，在商汤的认知中，有几个核心的重要的突破点。其一是人工智能的推理问题，要用高阶逻辑知识学习来解决。二，则是实时交互性带来流畅体验，在 WAIC 上，商汤发布也发布了商汤的阶段性成果「日日新 5o」模型。

而最后，很重要的一点，就是可控性。不管是文本生成、图像生成、视频生成，如果没有具备可控性，AI 作为一个工具，本身能够带来的效能的提升就非常的有限。

而 Vimi 模型，就是商汤在可控性方面，针对用户需求，做出的人物视频生成大模型。

今日的创作者，无需再在 prompt 上苦下功夫，一遍遍地生成，寄希望于大模型的盲盒，能够终于生成一个可用的人脸视频，既花功夫，又花成本。

对于原本的影视、动画创作者来说，Vimi 模型现在可以直接使用动画创作者最熟悉的骨架生成动作。而对于更多只有想法的视频创作者，自己录制一段视频，也能直接实现很好的生成效果。

视频来源：商汤 Vimi 模型

Vimi 模型仍然在快速持续迭代升级中。目前的模型，能够更可靠的生成的，主要是人物的上半身视频，而进一步的迭代的方向包括脸部表情的进一步控制、身体姿态控制、手部控制等等。

再进一步，Vimi 希望能够控制身体更多更复杂的动作，对更大的场景和多人的情景也能进行控制等等。

**可控，才可用。**

站在今天的时间点，我们也在 Vimi 模型身上，洞见了未来的可能性。

例如，曾经爆火的 AI 写真生成应用，利用的是成熟的 AI 生图技术，那么，在人脸生成稳定的新技术后，我们是不是可以期待一波 AI 视频写真的爆火？

视频来源：商汤 Vimi 模型

再比如，借助可控人物 AI 视频模型，原本不熟悉视频创作的人，是不是未来也可以低成本，低门槛地生成视频，来讲出自己想讲的故事，极大地丰富未来的视频内容？

抑或者，在不远的未来，我们再也不用担心明星没有演技了。因为明星的演技，也可以使用大模型微调了。

\*头图来源：Vimi

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**极客一问**

**AI 视频生成技术将**

**如何影响影视和短视频创作？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Z5rEl2poJuZqVBGZteWibbvpuA2OibrtXHS6bAJibcYSkxdsV1VicAF088bxt3yluWTQeMyL38W8bfrw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频**

来自马斯克的人生建议：尝试变得有用，努力不是为了变成领导。

**点赞关注****极客公园视频号****，**

**观看更多精彩视频**

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Yz23rwvLmdLxxhzOVmtoxnXyDUpLYjVUJqO5enFibbcuiaOxQHOfLoovCWnQ75a7pX4vTFNw8Y1ojA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653046893&idx=1&sn=8da53bbbea1d3bd251243d5607f2d3c5&chksm=7e5735db4920bccdb07b5ebee85ca720917685be83fbcaf8d6fcd08443a27efae9e517312b5b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5ao79ficmRnKJfiapiaUbanrtjicmtYdTZUknbucfyFBkGxDsTYribZkIvuiceBYqz3LthibpbiaHG4HQJC2w/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653046868&idx=1&sn=bc637d0f22037760f3dbecf9f2895674&chksm=7e5735e24920bcf4ba2d191d0678530e835d853e126601dc9495dbe11cf8d13153daccefd607&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif)![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

极客公园

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

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