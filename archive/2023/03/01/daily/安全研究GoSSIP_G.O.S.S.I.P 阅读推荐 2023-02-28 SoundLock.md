---
title: G.O.S.S.I.P 阅读推荐 2023-02-28 SoundLock
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494307&idx=1&sn=5ac2f5ce84127c137bbc110ea9c4881e&chksm=c063c47af7144d6cbb19e325d346a11fdb9c41685888a4b36a8df31282b1026d52f1eb587523&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-01
fetch_date: 2025-10-04T08:20:40.491788
---

# G.O.S.S.I.P 阅读推荐 2023-02-28 SoundLock

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTyQsR4379Oibtib4ub179xE8eOWxcCAnz2TNVEu3SwZHlRibtq0WYODdCNQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-02-28 SoundLock

MobiSec研究组

安全研究GoSSIP

今天为大家推荐的论文是SoundLock: A Novel User Authentication Scheme for VR Devices Using Auditory-Pupillary Response，将发表于NDSS 2023。该文章由德克萨斯大学阿灵顿分校（UT Arlington）黎明教授MobiSec研究团队完成。该团队研究领域包括移动计算、物联网、和人本计算，重点关注于以上领域的安全与隐私以及创新型应用等方向。MobiSec实验室长期招募热爱学术研究的博士生，感兴趣的朋友可以浏览实验室主页，与黎老师进一步沟通呀~

MobiSec实验室主页：https://ranger.uta.edu/~mingli/

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTyTVDjEIWqfkegzM4rsLmpv5jdfiaiarAfjB51pxyZjRia98UJicVqW7kkhw/640?wx_fmt=png)

**研究背景**

近些年来，虚拟现实（VR）领域取得了突破性的革新，这项技术已成为学术界与工业界的研究重点之一，并将在不久的未来凭借更实用的性能走进千家万户。由于其广泛的应用，VR设备也保存了大量的个人信息，例如平台账号、聊天记录、银行信息等。所以，如何让VR设备准确识别合法用户显得尤为重要。

目前，VR设备上的用户认证目前仍处于萌芽阶段。现有的解决方案大多遵循一般智能设备上的传统用户认证模式，例如密码、PIN和图案锁，而用户必须借用手柄在虚拟键盘上输入认证信息。这种方法有两个缺陷：首先，这种输入方式十分繁琐，大大降低了用户认证的可用性；其次，这种方法在肩窥攻击（shoulder-surfing attack）面前尤为脆弱——沉浸在虚拟世界中的用户往往难以察觉身边的窥视者，而其手部运动轨迹可以被窥视者轻易地用来推测键盘布局和输入的认证信息。

为了解决上述问题，研究者们提出了许多替代方案。其中，生理生物认证（physiological biometric authentication）方式以其高可用性和准确性吸引了最多的关注。然而，这类方法仍然面临着两个挑战。其一，采集生物信息（如脑电图、心电图、肌电图和虹膜）所需要的传感器专精且昂贵，暂时无法在市面上的VR设备中装配。其二，大多数生理生物信息是不可重制的。举例来说，一旦指纹信息被盗，用户无法重制认证信息——因为人类无法长出一组新的指纹。这一特性也被称为可取消性（cancelability）。

**可行性研究**

在文中，作者观察并利用了一种新型的动态生理生物认证信息，即听觉-瞳孔反应（auditory-pupillary response）——通过VR设备向用户提供听觉激励（如白噪音、提示声效、人声等）并观察其瞳孔的大小变化（见图一）实现用户认证。听觉-瞳孔反应是一种自主反射，由自主神经系统中的交感和副交感神经系统介导，虹膜桡侧肌与虹膜括约肌共同作用控制下的瞳孔扩张或收缩（见图二）；人类复杂的神经通路和虹膜肌肉结构中的生物独特性为用户识别提供了理论上的可能。

在可行性研究中，作者首先测试了用户内与用户间在相同声音激励下的瞳孔反应模式。如图三、图四所示，同一用户在多次实验中的反应模式较为稳定，而不同用户之间的反应模式则有明显差异。这一特性为利用听觉-瞳孔反应实现用户认证奠定了基础。此外，作者还测试了同一用户在不同声音激励下的瞳孔反应模式。如图五所示，不同激励引起的瞳孔反应模式也不尽相同。这一发现启发了作者扩大激励池以增大熵从而进一步加强系统安全性。不仅如此，以上两个特性启发了作者采用质询-响应认证（challenge-response authentication）方式。这类方式常与生物信息结合，利用用户对特定激励独特的生理反应实现用户认证。因此，即使某中特定激励下的生物信息（瞳孔反应）被泄漏，用户可以通过更新质询信号（声音激励）轻松地重制认证信息。得益于此，SoundLock实现了认证的可取消性。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTyZcgXxyaSaOaiavneIBIszhVh9Uv19wpuYwCOa8IOHRE0Qcj5xfBbW1Q/640?wx_fmt=jpeg)

图一 白噪音下的瞳孔变化实例

![](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTynKa6Ztv2v0cW9icGY2VfNic9LyArVeMGnia6lRWicpNOvNYtCbtwUEjbzQ/640?wx_fmt=jpeg)

图二 人类瞳孔变化的生物学机制

![](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTyzMDuQQGdTTJC6JjqU005OtXYvqfpeCs0iak0VhcVZjqdOZRSicKv18Fw/640?wx_fmt=jpeg)

图三 用户内与用户间的瞳孔反应模式

![](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTyXCStLeqAMLHJmCo1S7SlbKHxjrAln2385adcIicGjicHdHcOiciaibdw2Hw/640?wx_fmt=jpeg)

图四 基于皮尔逊相关系数的混淆矩阵

![](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTylRWtQjmW1Y9h4QJibkpZQgxROIsycibrQC7ShMhVDxFWbsNegZp2GibTQ/640?wx_fmt=jpeg)

图五 不同激励下的瞳孔反应模式

**方法介绍**

在上述发现的基础上，作者开发了SoundLock，一种基于听觉-瞳孔反应的新型动态生理生物认证机制。SoundLock解决了前文提到的可用性、安全性、普适性、可取消性等方面的问题。SoundLock分为注册和认证两个阶段，前者用于采集合法用户的认证信息、激励优化以及模型训练，后者用于识别合法用户。

从技术层面来讲，作者解决了两个主要问题。第一，如何从原始的瞳孔大小测量中提取出有效的用户特征。作者首度全面地研究了这种新的生物信息的特征，包括特定于瞳孔反应的形态学特征和一般的统计学特征。如图六，作者将瞳孔反应过程划分为激发阶段与恢复阶段，并根据各阶段的形态与生理过程提出并讨论了相应的形态学特征。激发阶段特征包括响应延迟（由神经通路主导）、波峰/波谷与扩张/收缩率（由瞳孔肌肉与神经通路中的众构件决定）、用以近似激励阶段的响应波形的n次多项式系数等。恢复阶段特征包括恢复时间、瞳孔动荡指数（取决于动眼神经副核与蓝斑的活动）、基线尺寸、用以近似恢复阶段的阻尼震荡函数参数等。统计学特征包括常用的平均值、方差、中位数、偏度和峰度等。最后，作者通过费雪分数从两类特征中选出了若干最能代表个人独特性的特征。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTy9tNOLkW7kwTIx7L31GHomRcaDYAXc4jSh1Vc2Javt4MiaSMOOGN00Zg/640?wx_fmt=jpeg)

图六 听觉-瞳孔反应的部分形态学特征

第二，为了进一步提高认证精度，作者在单激励的基础方案之上提出了多激励的进阶方案以增大系统熵。如图七所示，通过线性引入多个听觉激励，我们可以获得更丰富的瞳孔变化。对每一个用户来讲，其“密码”的唯一性也大大加强了。然而，这种方案会显著地延长认证时间而影响可用性。作者将该问题拟建为一个优化问题，即在满足时间约束的条件下，挑选激励及其有效时域区间以最大化认证精度，从而平衡安全性和实用性。鉴于该优化问题的非线性与自变量相关性等特性，作者用Kullback-Leibler散度（KLD）作为认证性能的指标，并设计了一个两阶段启发式算法来高效地找到近似最优解。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTyVCZo3s3VeFju0cW9x0Zm5asMyFuR25iaCDoosVUZlG3WvGBpibW1dicJQ/640?wx_fmt=jpeg)

图七 多激励线性连接示意图

**实验评估**

作者在一款主流VR设备HTC  VIVE Pro上搭建了SoundLock原型并全面地评估了其性能。44名实验对象在多种实验条件下用SoundLock原型完成了注册、认证、模拟攻击等步骤并参与用户调研。基于这些结果，作者从多角度评估了SoundLock的性能。如图八所示，与常用的PIN、图案锁和最先进的诸多生物认证方法相比，SoundLock拥有最低的错误接受率（0.76%）和错误拒识率（0.91%）、最高的F1分数（0.984）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTyeVwBTt0piafrNOaQh7jkHOP1A8ZmpwTaF1o2RFOtJTdu7z3hQloNCmw/640?wx_fmt=jpeg)

图八 与现有方法的性能比较

随后，作者探究了可能影响SoundLock的准确率的若干因素，如用户动作、时刻、环境噪音、接触虚拟环境时长以及长期漂移等（部分结果见图九、图十）。实验结果表明眼动、噪音和接触虚拟环境时长会略微增加错误拒识率而对错误接受率影响甚微，因此即使在这些场景下安全性也不会明显降低。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTy5Hxg6gGbetUrqO5hY4nLWCcuWpb555KzqsgmcHWH038N28LejyFzpQ/640?wx_fmt=jpeg)

图九 用户动作与时刻对性能的影响

![](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTywiaB84KesMWxG1qCibEfDybhhJmM27jUlIOceDGSxCcRgXt5Tzn684yg/640?wx_fmt=jpeg)

图十 环境噪音类型与强度对性能的影响

最后，作者根据用户调研的结果讨论了用户主观上对SoundLock的接受程度（部分结果见图十一）。在封闭式问卷中，作者通过T检验法得出了用户偏爱SoundLock的结论并分析了其原因。在开放式问卷中，作者分析了用户对SoundLock的总体反馈、顾虑和建议，并总结了未来改进方向。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GPQr9PU7RL51XVq4UPhPTyDVK4vxN5UtLXiaX53wDNlrlkuGxNDicQS8Y8RlJO3Ixh8mXBzGiaBPyEQ/640?wx_fmt=jpeg)

图十一 实验对象主观反馈分布情况

论文下载可以联系投稿作者呀~

投稿作者简介

朱华棣，德克萨斯大学阿灵顿分校四年级博士生，主要研究方向是人本计算和系统安全，侧重VR平台的应用，相关研究成果已发表于NDSS、CCS、Sensys、Ubicomp等国际顶级会议上。个人主页：https://huadizhu.wixsite.com/huadizhu

预览时标签不可点

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