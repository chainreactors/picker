---
title: G.O.S.S.I.P 阅读推荐 2023-03-20 That Person Moves Like A Car
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494597&idx=1&sn=ea941047e111b111fbafd7a3e8a63a96&chksm=c063c51cf7144c0ae9a476580b6555147f223ccfccb1eebb8846bfc3531f330229b670ae3409&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-21
fetch_date: 2025-10-04T10:09:51.549237
---

# G.O.S.S.I.P 阅读推荐 2023-03-20 That Person Moves Like A Car

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21GcicZPGPbGKCg4awuAph4PVv9WOSFwlEgqQDPKPvLpK7miaY4eZ7caia9bv8qxekca1o5b9YiaAicgU3g/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-20 That Person Moves Like A Car

Yanmao@WiSer

安全研究GoSSIP

今天为大家推荐的论文是来自USENIX Security 2023的That Person Moves Like A Car: Misclassification Attack Detection for Autonomous Systems Using Spatiotemporal Consistency。该工作由亚利桑那大学（University of Arizona）李明教授的 WiSer 研究团队主导，与普渡大学和弗吉尼亚理工大学的研究人员合作完成并投稿。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GcicZPGPbGKCg4awuAph4PVpgwiaHYH79yOiaia2j9fc0EhwibPRcxHQauh813OFz6DiaZaic0IwfAicxavw/640?wx_fmt=png)

**研究背景**

在自动驾驶系统的感知系统里，目标检测和跟踪（Object Detection and Tracking, ODT）是十分重要的一环，因为它负责着对周围环境的理解和预判。在一辆自动驾驶汽车上，摄像机拍摄到的画面就会被ODT分析，得出的结果会被用来做决策。比如说，当我们看到一个行人即将要过马路，那么自动驾驶汽车就会提前减速，而不是等到行人已经在过马路了才开始减速。

但是，最近的研究表明ODT系统具有安全隐患。攻击者利用感知攻击（Perception Attacks）来造成ODT出错。攻击目标有三类，包括目标移除（Object Disappearance），目标伪造（Object Creation），以及目标分类篡改（Object Misclassification）。攻击方式也有多种，既可以通过物理攻击（Physical Attacks），也可以通过传感器欺骗（Sensor Spoofing）——也就是攻击者可以依靠攻击传感器，使得传感器的输出会让相应的机器学习模型做出错误的判断。比如在高速公路上，攻击者可以在前车背后贴上 adversarial patches，使得后车将前车识别成了行人而不是汽车，于是后车决定在高速公路上急刹车。这类感知攻击在数据的源头对数据进行改动，绕过传统的基于密码学的数据认证等保护措施，使得这类攻击更隐蔽，更容易实现，同时更难防御。

在这篇文章里，**作者着重解决目标分类篡改攻击（Object Misclassification）的检测问题**。作者假设攻击者拥有 ODT 系统的白盒信息，并且利用它来生成可以在物理世界实现的对抗噪声（physically-realizable adversarial noise）。这些噪声通过对基于优化方程的对抗机器学习的方法（optimization-based adversarial machine learning）来生成，使得被攻击的机器学习模型做出攻击者所期望的预测。

最新的防御工作大多都限制在某一种传感器，比如 LiDAR，GPS，IMU 等，或者某一种具体的攻击方式，比如 norm-bound attacks 或者 adversarial patches。之所以这些防御存在这些限制，根本原因是它们都关注在 ODT 的输入，所以每当有新的攻击方式出现（伴随着新的噪声模式），已有的防御就会失效。

**方案**

这篇文章提出了一个通用的目标分类篡改的检测算法。核心思想是通过分析ODT的输出，而不是输入。对于每一个目标，ODT会输出其分类和运动轨迹（历史帧的边框序列）。作者提出的方案叫做 **PercepGuard**，就是去分析边框序列的时空特性是否与其分类结果一致——如果不一致，那就说明系统当前可能正在遭受攻击（下图所示）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GcicZPGPbGKCg4awuAph4PVHia2E2bZKO0MAkPAaejuC8rC5guIibK4jW0GvCoetzbsOOmiaSus5Yk1w/640?wx_fmt=png)

之所以能这样做，是因为每个不同目标分类的边框序列蕴含着独一无二的时空特征。举例来说，一个目标要被分类成”行人“，不仅它要看起来像个行人，而且移动起来也要像个行人。换句话说，目标的分类和移动轨迹有着天然的联系，然而现有的 ODT 系统却对他们独立地预测。相反地，PercepGuard 把两者融合在一起，尝试着去分析两者之间的一致性——一旦不一致，说明有可能有攻击。如下图所示，汽车的边框通常呈扁平状，而行人的边框成瘦高状。不仅如此，当把时间维度考虑进来后，汽车通常移动得比行人更快。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GcicZPGPbGKCg4awuAph4PVS7eD8l9AIrFXwff3MjXJ5BpvicWDH7lYAdVgkzR5sbzNvklK78XC4lA/640?wx_fmt=png)

当然，这类认知对人类来说很显而易见，但把它运用到攻击检测的话还有几个挑战需要解决。第一，必须保证上述时空特性在统计上提供了充分的信息，才能够区别不同目标分类。第二，要找到高效的方法来学习时空特性，使得伪阳性（false positives）和伪阴性（false negatives）尽量少，并且有易拓展的特性。第三，检测算法要对物理世界的自适应攻击（adaptive attacks）也有效。

作者提出用基于 long short-term memory (LSTM) 的 Recurrent Neural Networks (RNN) 来学习边框序列的时空特性（下图所示）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GcicZPGPbGKCg4awuAph4PVBbX5IHktmcwPsYJREUKREzM1gUXibFWt7ZLX9y5eNo6kr4rR8NYEoGg/640?wx_fmt=png)

每一帧的运算基于上一帧的 hidden feature 和当前的 raw feature，也就是边框描述。计算出来的特征一方面通过 fully connected layer 和 softmax 方程来进行分类计算，另一方面为下一帧的recurrent运算提供新的 hidden feature。作者用 BDD100K 数据集来验证他们的算法，得出了只有5%的伪阳性。作者用 adversarial patches 作为攻击方法，得出了99%的真阳性。

但是，当考虑自适应攻击时，情况却不一样了。自适应攻击者不仅拥有ODT的白盒信息，同时也拥有检测算法的白盒信息。自适应攻击者在试图攻击ODT的同时，也试图绕过检测方案。在这种威胁模型下，检测算法的真阳性降到了85.6%，因为自适应攻击者在某些样例下能找到可以同时达到上述两种目标的 adversarial patches。比如说，为了把汽车改成行人，自适应攻击者把目标的边框进一步地改成瘦高状，这样的话RNN就会把该边框序列也分类成行人。

为了提高检测方法的对抗鲁棒性（adversarial robustness），作者提出利用上下文的信息来辅助分类。这些上下文信息可以是自车的移动速度，或者与目标的相对速度。这些信息来自不同的车载传感器，比如速度传感器和激光雷达。比如说，有了自车速度和相对速度，就能推算出目标的绝对速度。这样的话，即使攻击者把边框改成了瘦高状，算法还是可以根据速度来正确地对目标分类，因为行人一般不会移动得像汽车这么快。作者用 Carla 来生成带有上下文的数据集，结果显示对自适应攻击检测的真阳性提高到了99%。

**实验和结果**

主要的实验结果展示在如下两个表格。表一说明 patch 越大，攻击越成功。其次，自适应攻击（defense-aware）在小部分样例中能绕过 PercepGuard 的检测。当对比表一和表二，能看到当把上下文信息考虑进来之后，PercepGuard对于自适应攻击的检测率大大提高到了99%。另外，攻击者攻击越多的传感器，那么其攻击成功率也会相应提高，这也符合预期。但是要着重说明的是，在这种情况下的攻击难度以及攻击代价将大大增加。实际上，PercepGuard 的优越性正是在它的杠杆作用——仅仅利用少量的防御代价（轻量化的设计），使得攻击难度和代价大大增加。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GcicZPGPbGKCg4awuAph4PVdUic9gjZn7iallwgzULxURjQicy6Y6QYmpuhUfTHvJwHpwLicVzUbpReZA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GcicZPGPbGKCg4awuAph4PVRNgRBJC8KgmS817QPop4jbj8gWPffojWkkq96ticQw2psl1vyt7lOnA/640?wx_fmt=png)

作者还做了真车实验来验证 PercepGuard。如下图所示，作者在前车尾部安装了一台LCD电视屏幕作为一种攻击方法。这台电视在播放 dynamic adversarial patches，用来适应不同的环境和背景。后车安装了一个便携式投影仪作为另一种攻击方法。后车另外还安装了行车记录仪来模拟自动驾驶汽车上的摄像头。结果显示这两种攻击方式均有不错的成功率，但是 PercepGuard 能把它们都检测出来。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GcicZPGPbGKCg4awuAph4PVAtKBIKKqUtWGMqIiapLvJhOHm8RJADZtAwE0Bysn2PAEKwNpwJUAq1A/640?wx_fmt=png)

**结论**

作者提出了 PercepGuard 来检测自动驾驶系统下的目标分类错误，办法是利用目标的时空特征来验证 ODT 的分类结果。为了提高对抗鲁棒性，作者进一步地利用多个传感器所提供的上下文信息来验证他们之间的时空一致性。PercepGuard 的设计考虑到了高效性和通用性，方便日后拓展到更多的传感器和别的ODT系统。作者不仅进行了大规模的模拟实验，而且还实现了真实世界的攻击与检测，展示了 PercepGuard 的有效性。

论文下载：

https://www.usenix.org/system/files/sec23summer\_278-man-prepub.pdf

投稿人：Yanmao Man@WiSer

个人主页：manyanmao.com

投稿团队介绍：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21GcicZPGPbGKCg4awuAph4PVQHKRKWDaKyWib04MTcWSrmG1hWx6FN5E6fiaSRyqMrW7KuBiaETqxEJeA/640?wx_fmt=png)

李明教授带领的WiSer 实验室的研究领域包括下一代无线网络及其安全隐私问题，隐私保持的数据分析、机器学习，以及信息物理系统的安全（着重关注互联与自动驾驶车辆的安全）。WiSer 实验室长期招募热爱学术研究的博士生，感兴趣的朋友可以浏览实验室主页，与李老师进一步沟通～

WiSer实验室主页：http://wiser.arizona.edu/index.html

李老师个人主页：http://wiser.arizona.edu/mingli/index.html

点击👇原文进入WiSer实验室主页

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