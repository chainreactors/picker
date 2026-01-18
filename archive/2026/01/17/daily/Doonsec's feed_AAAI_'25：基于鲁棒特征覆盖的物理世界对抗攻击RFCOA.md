---
title: AAAI\'25：基于鲁棒特征覆盖的物理世界对抗攻击RFCOA
url: https://mp.weixin.qq.com/s/IOjv1Xbuqm1zDIRviBTvZw
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:35:48.954498
---

# AAAI\'25：基于鲁棒特征覆盖的物理世界对抗攻击RFCOA

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN8B9yMgPgVvj87RZHfJ92zraicWdgtpacGiatvMr9FTZfq26RYUAPK2yvRIfGeorAicKKt9DudAngokg/0?wx_fmt=jpeg)

# AAAI'25：基于鲁棒特征覆盖的物理世界对抗攻击RFCOA

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

以下文章来源于穿过丛林
，作者王乙臣、胡胜山

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM43hfq5XChrMrwrNMXvE9jgADEiavGmTEzv3q86B7GQoKg/0)

**穿过丛林**
.

大数据技术与系统国家地方联合工程研究中心服务计算技术与系统教育部重点实验室集群与网格计算湖北省重点实验室大数据安全湖北省工程研究中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2hibICVjqiaGAzvXWicltGudgpDnibaAr3ZUgMKrSf1lwhz2rB4P252u0Sg/640?wx_fmt=png)

随着深度神经网络逐渐应用于自动驾驶、机器人操纵等真实物理场景，物理世界对抗样本（PAEs）的研究受到广泛关注。PAEs通过向输入引入扰动来误导模型，但现有方法面临两大核心挑战：其一，攻击性能不足，包括跨模型迁移性差以及在光照、角度、距离等环境变化下缺乏鲁棒性；其二，攻击有效性与隐蔽性难以兼顾，增强攻击强度往往导致扰动更加明显，易被检测。

针对这些问题，论文构建了鲁棒特征覆盖攻击（RFCoA）。该方法包括两个策略：首先为提升攻击性能，论文引入欺骗性鲁棒特征注入策略，利用具有可预测性、环境稳定性与跨模型一致性的鲁棒特征，将目标类别的鲁棒特征覆盖到原始图像的预测特征上，从而显著增强迁移性与物理鲁棒性。为改善隐蔽性，论文进一步提出对抗语义模式最小化，在保持攻击能力的前提下去除大量冗余扰动，仅保留关键的对抗语义结构。实验表明，RFCoA 在迁移性、鲁棒性与隐蔽性方面均明显优于现有方法。此外，该方法在大规模视觉语言模型上同样有效，展现出应用于更加复杂任务的潜力。

该成果“**Breaking Barriers in Physical-World Adversarial Examples: Improving Robustness and Transferability via Robust Feature**”发表在第39届AAAI Conference on Artificial Intelligence （AAAI 2025）上，AAAI是人工智能领域顶级会议之一，也是中国计算机学会（CCF）推荐的A类会议，该会议2025年录用率为23.4%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2HWyJLiaI5CWqUQK8D5qyE4azMVYFWD5xWmiawF6xxvPy7vyU1wJOOrvw/640?wx_fmt=png)

* 论文链接：https://ojs.aaai.org/index.php/AAAI/article/view/32870
* 代码链接：https://github.com/CGCL-codes/RFCoA

**背景与动机**

深度神经网络在图像识别、自动驾驶、语音交互和机器人控制等现实应用中取得显著进展，但其安全性问题也愈发突出。对抗样本研究表明，即便是在高性能模型上，极小扰动也能导致严重的误判。然而，传统研究大多集中于数字空间中的对抗样本，而真实世界中的物理因素——包括光照变化、拍摄角度、距离偏差、遮挡、成像噪声等——使得数字对抗扰动在物理环境中极不稳定。因此，物理世界对抗样本（PAEs）逐渐成为研究焦点，在自动驾驶交通标志识别、人脸验证、机器人导航等应用中都对系统安全构成现实威胁。

现有物理攻击方法主要包括基于扰动的方法、基于补丁的攻击方法以及基于光影操控的光学攻击。补丁类攻击虽然具备较强的攻击性能，但扰动区域大且显著，极易被人眼察觉，难以用于高安全性场景。光学类方法（如激光、阴影投射）具有更高隐蔽性，但对环境变化极其敏感，只能在高度受控的场景下奏效，缺乏普适性和稳定性。基于扰动的物理方法虽然具有更高的隐蔽性，但在迁移性和鲁棒性方面表现不佳，往往只能在特定白盒模型或固定环境条件下成功，缺乏跨模型和跨场景的攻击能力。因此，现有PAE面临两大核心挑战：其一，真实环境下的攻击性能不足——特别是跨模型迁移性弱、对环境扰动不稳定；其二，攻击有效性与隐蔽性难以同时满足，强化攻击能力必然导致更显眼的扰动，限制了物理部署。

进一步分析显示，现有扰动方法大多操作模型的“非鲁棒特征”（non-robust features）。这些特征虽对模型预测有显著影响，但在不同模型间共享性弱，且对环境因素高度敏感。然而在真实世界场景下，这类脆弱的非鲁棒特征通常被光照、角度、噪声破坏，从而导致攻击失效。相比之下，“鲁棒特征”（robust features）具备与图像语义高度相关、在不同模型之间可被一致感知、对物理扰动天然稳定等优势。相关研究表明，鲁棒特征是模型更本质的语义基础，在不同网络结构之间迁移性强，且能够在现实场景中保持激活区域相对一致。因此，将鲁棒特征引入物理世界攻击，可能从机制层面突破迁移性与鲁棒性瓶颈。

基于这一认识，论文从特征空间重新审视物理世界对抗样本的生成机制，其动机在于摆脱对非鲁棒特征的依赖，而转向利用跨模型一致且在物理世界稳定的鲁棒特征。为此，论文提出两项关键策略，如图1所示：其一是“欺骗性鲁棒特征注入”，通过提取目标类别的鲁棒特征并将其覆盖至原图的预测特征区域，使模型在语义层面被引导至目标分类，从根本性提升迁移性与物理稳健性；其二是“对抗语义模式最小化”，通过掩码优化移除冗余扰动，仅保留关键语义对抗结构，从而在确保攻击有效的同时显著提高隐蔽性。两者结合使得对抗样本既能在物理世界中稳定生效，又能保持接近自然图像的外观，兼顾攻击能力与隐蔽性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2xSdicpobGOribeWF8JKgsMGdwCicdiaqJ1Yd23MCu7266ClRlIDtSHvgqA/640?wx_fmt=png)

图1  RFCA设计思路示意图

**设计与实现**

现有基于扰动的物理世界对抗样本方法普遍依赖操控“非鲁棒特征”（N-RFs），这些特征虽然与模型预测强相关，但在不同模型间缺乏一致性，且对噪声、光照和视角变化极为敏感，导致在真实环境中容易失效，也难以迁移至黑盒模型。因此，要从根本上突破PAE的鲁棒性与可迁移性瓶颈，需要摆脱对N-RFs的依赖，转而利用在多模型间具有一致可感知性、并能在物理扰动下保持稳定的“鲁棒特征”（RFs）。

论文通过数字与物理世界的跨域可视化实验（实验结果如图2所示）发现，RFs在不同模型间展现出高度一致的注意力模式（图2 (c)的结果），并对环境噪声保持稳健（对比图2 (c)、(d)、(e) 的结果），说明其在物理世界依然可作为攻击操控的核心特征。因此，方法需要考虑的第一个问题是：将目标类别的RFs注入到原图像的关键预测区域，从而提升攻击的跨模型迁移性与物理鲁棒性。

然而，RFs本身通常具备明显的语义结构，若直接叠加到图像中会造成较高可察觉性。因此，需要考虑的第二个问题是：通过动态权重控制与掩码机制，对RFs的融合过程进行细粒度调节，仅保留必要的对抗语义成分，并抑制冗余扰动，从而在不破坏攻击强度的前提下最大化隐蔽性。

综合而言，该方法通过“鲁棒特征注入”与“扰动最小化”相结合，实现对物理世界对抗样本在鲁棒性、迁移性与隐蔽性之间的系统性平衡，方案的整体框架如图3所示，分为鲁棒特征提取和对抗性特征融合两部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2keeG0O1dNf1okAwTQvOwiaf7gTicWkN9e1RVgbfCRicbqVeEenoP4t0mA/640?wx_fmt=png)

图2  数字世界与物理世界模型感知分布图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2TWEKSWANJzjxXIdgUic0sDonYKWmm47hhA9Cfic3xXuXrxibxIaV8t5wA/640?wx_fmt=png)

图3  RFCOA的框架图

**1**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FhwyFd6snAVxesxNeE1t3B9iaUao0eP0VV4u7bNnLEEr1micZb2lPyCnHWKkRgcBbu0t8dEULLQUvA/640?wx_fmt=gif)

**鲁棒特征提取**

为充分提取攻击目标类别的鲁棒特征，论文采用了自编码器，将图像编码到高维特征空间中，便于分解其鲁棒特征与非鲁棒特征。首先想目标类别图像中加入加入扰动，然后在特征空间中不断优化图像的特征，使得图像解码后与标签的交叉熵损失最小，该过程可表示为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2h3Ok5XEsBTuXk6wMuFvEbly9EW0AcibCBqt0gSLgiaicZzicAibhmpjZwyQ/640?wx_fmt=png)

其中Mi为第i个代理白盒分类模型，D为自编码器的解码器模块，f初始化为目标图像经过编码器后的特征。该过程的目的在于使得目标类别的特征能够在范数为epsilon扰动的条件下仍然能保持语义，即为图像的鲁棒特征。

**2**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FhwyFd6snAVxesxNeE1t3B9iaUao0eP0VV4u7bNnLEEr1micZb2lPyCnHWKkRgcBbu0t8dEULLQUvA/640?wx_fmt=gif)

**对抗性特征融合**

在充分提取到目标类别的鲁棒特征后，接下来需要将这些鲁棒特征覆盖到干净图像上以生成对抗样本。论文采用了梯度分布图来确定干净图像的关键特征的分布，梯度越大的地方说明该区域特征越重要。随后生成权重掩码将这些区域的特征屏蔽掉，然后与所提取的目标类别的鲁棒特征融合。这一过程表示为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2jRzlaLSEPedGAicZbCaV1qTYwniakO0U4R2Ff8jj6wSWOIia8blBS2Cyw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2rqeWBHMAiczWSLlCeyNW8xlnZ6faaEEmZMovoicrNXeO5sy3Tz3BJibbQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2QvpjoJxZwY3rRwVq6a7licBhT6Y44Lyd7lXYPvR0dnFweIaBAn0HY1Q/640?wx_fmt=png)

其中fc为干净图像的特征，alpha为特征融合系数。

为进一步去除融合后，特征中不必要的扰动以增强对抗样本的隐蔽性，论文采用了最小化认知模式，使用掩码将扰动后的图像与原图像相加，即仅保留关键位置的对抗扰动。该过程表示为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2JvLTKU2ZFGqVBHAJDTjV3kLSOaBRR8avnDO4Tzm8HamcwomtreZVnA/640?wx_fmt=png)

为平衡对抗样本的攻击性能与隐蔽性，论文设计了两个损失函数来进一步优化两个重要参数alpha和m。该优化过程为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2EZhqxmSCjlxiagW4DLibQ6uBicRPZRPZPetAQe26iabKT095ic124uvXW9Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2Nww0mpZicNwjKVoulNHibuibibNZo5QeTsjBiaZAhibWqgLhoqMLQoLX8JLQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2RCrxwsqOasj0qicEMfY9zM6bibZdkvFebl1QTQL0icDvBT8RXnbUsk7ibw/640?wx_fmt=png)

**实验评估**

本文在ImageNet数据集上对所提出的方案进行了实验验证，实验包含物理世界和数字世界的评估，实验指标为攻击成功率（ASR）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2XU0BqqWG5DicUkgGyqJzm0qqo0J7LolicboPGKqOt258MtrpqJ9ylRAQ/640?wx_fmt=png)

图4  多个模型下的实验结果

根据图4的实验结果，现有的最先进的对抗攻击的方法在白盒设置下均能取得较高的ASR，但是它们在黑盒模型上的ASR较低，并且在物理世界场景设置下ASR下降显著。这说明了它们迁移性较差，在物理世界中的可部署性差。相比之下，本文提出的RFCOA在多个黑盒模型和物理世界场景下均能保持较高的ASR，说明了其优异的迁移性和可部署性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2gib2g7fP0QKPD2YDOgbdYE2XDkUu9rdJcgoPI5DchZneic5deCk4B9jg/640?wx_fmt=png)

图5  多种物理世界采样条件下的实验结果

为进一步验证RFCOA对于物理世界各种环境扰动的鲁棒性，本文还在各种物理世界采样条件下进行了实验，结果如图5所示。现有的攻击方法在不同的采样距离和角度下ASR变化显著，鲁棒性较差；而RFCOA在多种扰动下仍然可以保持较高的ASR，说明了其对于物理世界环境扰动的鲁棒性强。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OF0DpXXH9ZAG8vjBRbbrSAfRyEIK9pV2MUSxf6iaSCaASUNNDibd3JanremNyYTkglAqsN5JgCZc0AvLAqrY4Jiaw/640?wx_fmt=png)

图6  各种对抗攻击方法隐蔽性实验结果

图6实验结果同样说明了RFCOA的隐蔽性较好，与典型的光学攻击方法RFLA的效果接近，SSIM达0.89，LPIPS为0.14，说明其在物理世界环境中不易被检测。

**详细内容请参见**

Yichen Wang, Yuxuan Chou, Ziqi Zhou, Hangtao Zhang, Wei Wan, Shengshan Hu, Minghui Li, "Breaking barriers in physical-world adversarial examples: Improving robustness and transferability via robust feature", In Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI 2025), Feb 25-Mar 4, 2025, Philadelphia, PA, USA, pp. 8069-8077.

https://ojs.aaai.org/index.php/AAAI/article/view/32870

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

信息网络安全杂志

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

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