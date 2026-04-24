---
title: LARYBench 发布：定义具身动作表征 ImageNet，首次度量从人类视频学习的泛化表征
url: https://mp.weixin.qq.com/s/AZ3r96L--DJEhHMzjlDJyw
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:50:55.832506
---

# LARYBench 发布：定义具身动作表征 ImageNet，首次度量从人类视频学习的泛化表征

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/V95GN2mm0DwUPvYNHELWmuQL9PhqnTe81SGQno4EuHWicBCvWJj555B9ia8WA9nQzWAia5vSf358PMN1unezFlnYVoyfTVIY15oaTekr4a6JIM/0?wx_fmt=jpeg)

# LARYBench 发布：定义具身动作表征 ImageNet，首次度量从人类视频学习的泛化表征

龙猫LongCat
龙猫LongCat

美团技术团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojvsQiapkP9KLJck4PQlmUXfaT3HOnCdPzFFYcRzyGvz9UkO84SnHar3c3DOEQPoJyTfdjvNsH31Via8pia163NPTDcaulNiaEFIsU/640?wx_fmt=png&from=appmsg#imgIndex=0)

如果你看过今年春晚武术节目《武BOT》，一定会对那群与人类武者同台对打的机器人印象深刻。但在流畅的武术动作背后，是一个工程师团队连续数周针对特定舞台、特定灯光反复调试后才可能达到的动作丝滑。

为什么机器人在固定场景下表现良好，但换一个环境、任务，泛化能力就会明显下降？

究其根源，是具身行业缺少带动作标注的训练数据进行泛化学习，而互联网上大规模人类数据是极具潜力的数据来源。为了指引具身智能走向GPT时刻，像大模型一样走通大规模数据学习范式，通过人类视频数据学习通用的、跨本体的隐式动作表征是关键。

为此，我们提出了 **LARYBench （Latent Action Representation Yielding Benchmark）** ，一个指引从大规模的视觉数据学习到通用的隐式动作表征的系统化评测基准。**实验结果表明：在动作泛化和控制精度上，通用视觉模型的表现均显著优于专门为具身智能设计的动作专家模型**，具身动作表征可以从大规模人类视频数据中涌现。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojaJKG4MJSyCvwm4kVOebGUOtQjicNSvxZicdtYHxFr1M5FHCiaNqjbJ0zwfGAk5SFlPWelTaAUEZvbRR0WcGCZ2hl9J69zClU7ws/640?wx_fmt=png&from=appmsg#imgIndex=1)

当前主流的 Vision-Language-Action（VLA）模型，其泛化能力受限于一个核心矛盾：互联网上存在海量的人类视频，视觉信号极其丰富，但如何将这些视觉信息转化为机器人可用的动作表征，始终缺少高效的路径。具体表现为三个层面：

* **数据瓶颈**：带精确动作标注的机器人数据依赖遥操作采集，成本高、规模小；而人类视频虽体量庞大，却天然缺失机器人可执行的动作标签，画面与动作之间存在模态断层。
* **表征瓶颈**：即便从人类视频中提取信息，传统做法输出的本体动作数据高度绑定特定硬件，难以跨形态迁移。隐式动作表征通过学习“帧与帧之间的变化”来抽象与本体无关的动作语义，为打通从视觉到动作的链路提供了更具泛化潜力的中间表示。
* **范式瓶颈**：长期依赖人工标注使得具身智能局限于“固定场景精调”，无法像大语言模型那样从规模化数据中涌现能力。隐式动作表征路线的本质，正是试图以无标注的人类视频驱动规模化预训练，让从视觉到动作的学习也能走上数据驱动的扩展轨道。

自 2024 年 LAPA 等早期工作提出以来，基于隐式动作表征的研究已陆续展开。然而，现有评测大多只看端到端任务成功率，始终缺少一个能独立衡量中间表征质量的标准基准——动作表征领域，还没有自己的 ImageNet。具体表现为：表征与下游策略难以解耦、跨本体泛化能力无法检验、训练策略的系统性分析缺失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoh8ib6icyJclonUicGABiakj9Yfb3g4fRUEBwwG3OgCDlpo3QXayI86w3LThaThh5ZNPGdRDPibufveOVOzyatET3GHKFibHGJogsYqQ/640?wx_fmt=png&from=appmsg#imgIndex=2)

为填补这一空白，我们提出了 LARYBench ，一个从本体动作和语义动作两个粒度出发，系统评估隐式动作表征质量的基准。如图1所示，评测数据集涵盖超过一百万段精心标注的视频（总时长超过 1000 小时），涉及 151 种不同类型的动作，同时包含 62 万对图像和 59.5 万条运动轨迹，覆盖了多样化的机器人形态与操作环境。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoghTToibIs3q8pTe6Vc7Qbme9XUjFibg6TNazCdjFGtDLxaT0TfrD61dHH2XiaeSMeJKAB2tVgnyA5MMbooibaLtFHL3Sicrug0uVWU/640?wx_fmt=png&from=appmsg#imgIndex=3)

*图1：LARYBench概览*

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaogXw6bGelBibqgiaIfJgq2sB9BGnrJDh6KzPicMQ01gQWMuJDZHewMZ1ZYE77FnKb1E3Fm1h4dWO73WAiaia5cJauVXs77PqElanbY0/640?wx_fmt=png&from=appmsg#imgIndex=4)

评测的核心逻辑如图2所示：输入一段视频或图像序列，通过待测的隐式动作模型（Latent Action Model, LAM）提取出动作表征 z ，随后通过浅层探测头（probing）来验证 z 的质量。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaogjDia9eSTMb5JJvVDd5xbL1wuNVFolmwUuCsFnxQSASdtCLYnx4NsibPfXHv1xXXW0tgMv35s59ul5Fy4Vicw1ZyJX5YPVXMbgbM/640?wx_fmt=png&from=appmsg#imgIndex=5)

*图2：LARYBench整体流程*

**动作的定义由细到粗分为三个层级：**

**![](https://mmbiz.qpic.cn/mmbiz_jpg/JhVy5CXYiaogJX944UoGTibcUa7Fk4Ra9lWAGOvb8otPricdH6hDCVM3GiaHAgHbiauq9oib9pKYt3oT8ZUNRuV1HSXtNStOPkfG5uTomAo1PXS20/640?wx_fmt=jpeg#imgIndex=6)**

* **本体动作**：机器人操作的控制信号，主流使用末端位姿，包括腕部 3D 坐标、3D 旋转角及夹爪开闭等。
* **原子语义动作**：本体动作聚合为可用自然语言描述的原子操作，如上下左右前后移动、夹爪开闭。
* **复合语义动作**：原子动作进一步聚合为有完整语义的行为，如拿起、放下、擦拭等。

针对不同粒度的动作，评测采用不同的验证方式：

* **语义动作分类**：对提取的表征 z 接入 Attentive Probing 结构，进行动作类别分类，以准确率衡量表征对高层动作语义的捕捉能力。
* **本体动作回归**：对表征 z 接入 Action Expert 解码器（可选 MLP 或 Diffusion Transformer），进行连续动作回归，以均方误差（MSE）衡量表征对底层控制信号的还原能力。

### ![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojWdEMdUVGv8zdOYBg2icw7CXKT6aOxCECr9XhGtC0zoJySz3bxvU6UcZbHkzJjfYPWXqa0MRFs1a6L2f0hYktpUxa2toRdcVib0/640?wx_fmt=png&from=appmsg#imgIndex=7)

针对多种粒度的动作，我们收集了主流常用的第一视角人类数据以多视角、跨本体的机器人数据，并通过自动化数据处理流程构建为动作表征数据集。处理流程包括，动作片段切片、视频描述、动作提取和归一化，最后通过人工抽检做质检校验，确保训练集准确率在 85% 以上，测试集准确率在 95% 以上。数据集涵盖 151 个明确定义的动作，以及对应的 121.5 万个标注样本。数据集覆盖的人类活动范围广泛，从常见的"pick"和"place"动作，到长尾分布的"shovel"(snow)和"float"(balloon)动作均有涉及。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaohRtw7SugQc9Dr0fYyuKm51rdtLGcIJVxwemyE78nwATknAia9ZjlvRvc8lLeJtaXWQW99R7DqZkC2iaRAMjUfVibGsXyHep2hwUk/640?wx_fmt=png&from=appmsg#imgIndex=8)

*图3：LARYBench 数据构建流程*

为确保形态多样性，数据集涵盖 11 种不同的机器人形态，从广泛使用的 Franka 单臂操作器，到 AgiBot G1、Agilex Cobot 和 Realman 系列等复杂的双臂及半人形平台，同时包含大量人类第一视角交互数据。

为保证环境多样性，数据集记录了数千种独特的物体操作场景，涵盖模拟桌面、真实住宅厨房、商业场所和工业场景等非结构化环境。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoiaGWnic01icVpHmD9ytiad6IPVa1bbuhjLFFl3TPYvib0WJviahHpaAVib3iblU5xuI0H6zhju7Q7gbwPhESfs7UfFNgLv2QDSRiaPSIfw/640?wx_fmt=png&from=appmsg#imgIndex=9)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaogtlgHge5ywibkv42jtJJSNDPp29Zy7W2E1mhC50RdM4WH6WhibHr5LvfuGic3XGuqkREjWGfDdooE4q4rEibs8sLk63KJNSsiaDdcg/640?wx_fmt=png&from=appmsg#imgIndex=10)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaohX9ZblA0ron2XS8qjPHpeeKKdKhSE5o3qia1ggyaMacIh9lgybDXTMDJKUzP7z3DjmLiaic34Imw3TVUmpgpQO1wnS62NE4Ddzns/640?wx_fmt=png&from=appmsg#imgIndex=11)

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojkjobG5VS3hecCoBeTeTQqQVlyakBcs4XNFA0QibSyo1ZN2YticxOr3KywfghibOCUmxhFakKutadMibQ9lk7lChFZe3FZ2A3JG3s/640?wx_fmt=png&from=appmsg#imgIndex=12)

△右滑查看更多

数据分布信息如下:

* 可视化云图

![](https://mmbiz.qpic.cn/mmbiz_jpg/JhVy5CXYiaohTm4ddfyVl2z5Uribic1MrUIuIjRzbmYmOUSGO6syn4tGZPn87jT5I6wOfZveFKxwaLXtKcQCDMugOtkw0GmLhCT5TZvwH54icdc/640?wx_fmt=jpeg&from=appmsg#imgIndex=13)

* 动作分布

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoh7IlrM5MdSqwXEfznDCfCcPYurQice2CghJUhNDHI5xaxsDBJpUAftkfo3kRxicXDAujtibRxGTbmz6JLZPcibjA3QjP6u9l70yHY/640?wx_fmt=png&from=appmsg#imgIndex=14)

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaojCRJxqfCnQ3RaHBUKDhTasVBEpAaYDKszPtkMlTrytW0jB2kSDUXAHPy9zzG4aVkXibLRnZUnNWJzYwzercHbMK79JDJUibVdYU/640?wx_fmt=png&from=appmsg#imgIndex=15)

评测按任务类型分为两类。本体动作任务以起始帧与结束帧构成的图像对作为输入，通过浅层 Action Expert 模块将动作表征映射为末端执行器位姿参数，以均方误差（MSE）衡量回归精度。语义动作任务同样输入图像对，通过浅层分类头进行多类别分类，以分类准确率作为评估指标。

待评测模型覆盖四类动作表征范式，包括专为具身智能设计的隐式动作模型、语义级与像素级通用视觉编码器，以及在通用编码器基础上训练的隐式动作模型，以形成从专项到通用的完整能力参照。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohxov3M3Tz231Sibbar75h453trmiaSLsvYqkLeiboiceN1lK7Vz07NopOHnb7IjibYq3cC94RyQ1MRBfUWHnuKw2FGGqQARGYWtyZk/640?wx_fmt=png&from=appmsg#imgIndex=16)

论文实验部分围绕三个核心问题展开：

* 动作表征是否足够编码精细的控制信息
* 动作表征是否能覆盖多样化的动作类型
* 以及如何构建有效的隐式动作模型

以下从本体动作回归、语义动作分类、可视化分析和消融实验四个维度展开。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiaYwYqemOJwgxngjPdGemZTCVBiaNE4LYpve0SvQ8Yopj99oSkM1ZJf8HxQO9hORUtgCSUVWkCLLnkic2zY2B3azbMXIsZehI5z8/640?wx_fmt=png&from=appmsg#imgIndex=17)

本体动作回归任务评估的是模型将视觉信号还原为末端执行器绝对位姿的能力。评测覆盖四个数据集：CALVIN（第三人称仿真单臂）、VLABench（第三人称仿真单臂）、RoboCOIN（第一人称真机双臂）和 AgiBotWorld-Beta（第一人称真机双臂）。所有模型均以均方误差（MSE）作为评估指标，数值越低表示回归精度越高。

综合来看，DINOv3 在四个数据集上的平均 MSE 低至 0.19，而具身专项模型 LAPA 的平均 MSE 高达 0.97。语义级表征（V-JEPA-2、DINOv3）的回归误差普遍略低于像素级表征（Wan2.2 VAE、FLUX.2-dev VAE），说明本体动作信息同样可以在语义级特征空间中得到有效保留。

![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoh3k6zLjZzdxEYVZB1KJdWWiaTJsLic9yDEicNzO4zAicD3xxZC3y24WMibBjsFUm8qMdNeL9uwyaRciccUFmiafGUKrZCM1iaNicgvyq5M/640?wx_fmt=png&from=appmsg#imgIndex=18)

### ![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaoia6xSKfwGa8icFFGHqOYSWjBkL8pTPBqmLF2vTCkKkiaH246CHqEtzh0hyxicSkoXlR9bNE95ib10Bct6iae0K7GVVLrYtRxpbqic5Jg/640?wx_fmt=png&from=appmsg#imgIndex=19)

语义动作分类评估模型对高层动作语义的识别能力，按数据来源分为原子动作、复合人类动作和复合机器人动作三类任务。综合来看，语义级通用编码器在三类任务上持续领先，具身专项模型表现普遍偏低，通用 LAM 居中。视觉自监督学习在动作语义捕捉上优于图文对比学习，前者能够兼顾视觉中的动作语义与控制细节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaognQbrf2RFwiauHXMDd2CyHJFxoibibw30tezxzlQZAsbmpgzeh2chZdpvfKtkJibT5523kyTOSHGUk0AWJ2Tqv9icM2ZVYWvdP0B60/640?wx_fmt=png&from=appmsg#imgIndex=20)

### ![](https://mmbiz.qpic.cn/mmbiz_png/JhVy5CXYiaohtWUake3dQeg3EqQsxtyibCKFWRMU997LRyUmuNO8SrzaC0iaEaPEdItibLDw90ZesGpibuU6y9SAZZ4juk9kgssrqRq9g1Hp2vo4/640?wx_fmt=png&from=appmsg#imgIndex=21)

为了进一步探讨以上实验结论所表现出的原因，我们进行了以下定性的可视化分析实验。

**3.3.1 长尾分布分析**

从 Composite Human 数据集上的分类性能随样本频率变化的分布来看，各方法在高低频动作上的趋势基本一致。在长尾部分（样本量较少的动作类别），强模型与弱模型之间的性能差距进一步拉大。这表明表征能力更强的模型在低频场景下具有更好的泛化表现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JhVy5CXYiaoiaAiaW0wacTm8VUQugydlibnc0OSP61ibTEzbOUwaia6pDLJgZyUicI0ATCndKxSibiaqenz2drial83tqv5Yd0pg57C3MhKgM5xDTpkfo/640?wx_fmt=png&from=appmsg#imgIndex=22)

*图4：复合人类数据集中动作分类性能在长尾分布上的表现*

#### **3.3.2**表征可视化分析

对“倾倒”动作序列的可视化显示，语义级表征模型 V-...