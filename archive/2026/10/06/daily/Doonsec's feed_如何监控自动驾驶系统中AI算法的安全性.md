---
title: 如何监控自动驾驶系统中AI算法的安全性
url: https://mp.weixin.qq.com/s/iwyTTTvTPPex0htz8eaDUw
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:52:07.755685
---

# 如何监控自动驾驶系统中AI算法的安全性

# 如何监控自动驾驶系统中AI算法的安全性

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**01**

**相关工作**

我们通过将现有方法分为两类来进行区分：（i）“训练阶段”，即仅在神经网络的开发和训练阶段使用的方法；（ii）“运行阶段”，即在神经网络的运行时环境中用于确保其正常运行的方法（研究问题 2）。

**训练阶段**

属于这一类别的现有方法包括：

（i）训练 / 验证 / 测试划分 —— 该方法用于确保所开发的自适应系统在给定的输入集下能够令人满意地工作。该方法涉及对可用数据进行划分，以获得三个集合，其中最大的集合仅用于训练，剩余的两个集合中，一个用于微调神经网络的超参数，另一个用于测试已训练的神经网络，以研究其对先前未见过的数据点的反应情况。尽管这种方法有助于验证神经网络的工作情况，但对于高关键性系统而言，其程度尚不足以被视为安全保障。

（ii）自动化测试数据生成 —— 对训练 - 验证 - 测试划分方法缺乏信任的根源在于，用于测试的数据样本非常少，很可能会在测试阶段遗漏高关注度的案例。克服这一问题的一种方法是使用测试数据生成工具来生成合成数据点，这些数据点可用于测试已训练的神经网络。诸如自动化测试轨迹生成（ATTG）以及最近使用本体生成自动驾驶汽车可能遇到的场景的方法等工具都属于这一类别。这种方法可以通过揭示固定神经网络中缺失的知识，并增加对自适应神经网络工作的信心，从而帮助神经网络的验证与确认过程。

（iii）形式化方法 —— 形式化验证指的是使用数学规范对系统进行建模和分析。尽管这些方法在传统软件中效果良好，但在自适应软件系统领域却未取得太多成功。这是由于在对环境的非确定性进行建模方面存在挑战，难以建立正式的规范来编码系统的期望行为和非期望行为，以及需要考虑系统的自适应行为。相反，神经网络的形式化验证技术使用诸如李雅普诺夫分析等方法来证明系统的收敛性和稳定性。

（iv）规则提取 —— 规则被视为神经网络内部工作的描述性表示。规则提取算法，如 KT、有效性区间分析（VIA）、DeepRed，可用于对神经网络在训练阶段获得的知识进行建模。这些规则可以表示为易于理解的 “如果 - 那么” 语句，由于其人类可读的格式，可以手动验证，也可以使用模型检查器进行自动化验证。这种方法有助于建立对系统的信任，因为它增强了系统的可解释性。它还有助于需求追溯，因为可以验证规则是否描述了为系统指定的功能需求。它们还可以帮助检查系统的各种功能模式，并确保某些输入能够诱导安全的操作模式，同时遵守预期的安全限制。尽管这种方法带来了巨大的优势，但它更适用于离线学习系统，在这种系统中，验证与确认从业者可以在训练完成后从网络中提取规则。

**运行阶段**

属于这一类别的解决方案可以更准确地称为 “在线监控技术”，该技术涉及使用一个或多个监控器作为预言机，以确保神经网络随着时间的推移持续正常运行。这里的目标是确保适应动态不会导致网络发散，从而触发不可预测的行为。

数据嗅探是基于上述技术的一个示例，它研究进入和退出神经网络的数据。如果某个输入可能产生负面结果，那么监控器会生成警报，甚至可能标记该数据，从而不允许其进入系统。这种方法在异常值可能会降低系统功能的情况下非常有用。

**02**

**提出的方法**

从 “相关工作” 部分可以明显看出，大多数当代方法都涉及在将开发的模型部署到运行环境之前对其进行测试。然而，基于机器学习的组件存在以下问题：运行数据 / 平台与模型训练时的不同，从运行数据中获得的新推断的不确定性，甚至硬件 / 软件的磨损。这些都使基于机器学习的组件容易出错。因此，有必要关注基于监控的方法，这些方法最近开始受到关注（Fridman、Jenik 和 Reimer），以帮助缓解与此类系统相关的安全问题。

为了详细说明所提出解决方案的具体内容，我们选择了用于变道操作的端到端深度学习模型。这种模型使用深度神经网络，该网络从代表自动驾驶汽车周围环境的传感器获取输入数据，并生成三种动作之一，允许自动驾驶汽车继续在当前车道行驶，或者根据障碍物的存在切换到左车道或右车道。

这个被称为 “碰撞预测网络” 的解决方案涉及一个神经网络模型，其任务是在任何给定的时间步确定碰撞的可能性和严重性（研究问题 3）。该模型考虑了多个特征，如车辆感知模块的输出、自动驾驶汽车的计划轨迹 / 动作、障碍物的预测（或预期的，如果通过车对车通信获得）轨迹，可能还包括自动驾驶汽车和障碍物之前涉及的碰撞次数和严重程度等信息。通过区分模型的训练阶段和运行阶段（部署后），可以理解该系统的具体情况。

训练阶段（如图 1 所示）依赖于模型接收前面所述特征集的所需输入值，并且知道是否发生了碰撞。因此，该模型需要一个涉及强化学习环境的架构，该环境将允许模型在给定一组特征值的每个时间步知道结果。这也将允许车辆经常发生碰撞，这是强化学习代理的特点，尤其是在训练开始时。因此，我们建议通过允许模型与强化学习代理进行对抗来训练模型，使得自动驾驶汽车紧密模仿现实世界中的车辆，能够执行上述变道操作用例等任务。在每个时间步，强化学习代理和碰撞预测网络将能够访问有关车辆环境的信息，碰撞预测网络将预测是否会发生碰撞，同时，强化学习代理将与环境交互以确定是否真的发生了碰撞。根据两个网络输出的差异，碰撞预测网络将被更新，最终能够以高准确度预测碰撞。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9SJbcI1YJnCWNvicVRqUuHJw3RLKvyILRVKV3Sp8yQjgWCq5JF7udumfUmVVV37wzTm908nPIVgEw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

图1：碰撞预测网络的训练

该模型的运行阶段（如图 2 所示）设计为：输入通常被馈送到负责确定自动驾驶汽车要执行的变道操作的基于机器学习的组件。然而，车辆不会直接对生成的变道动作命令采取行动。动作命令以及传感器数据形式的环境输入被引导至碰撞预测网络，该网络执行其预测碰撞可能性的任务。只有当可能性较低时，车辆才被允许执行所需的动作，否则车辆将进入故障安全模式，该模式根据预测的碰撞严重性而有所不同。值得注意的是，为了使模型与环境保持相关，它需要在运行阶段也进行学习和改进。因此，与训练阶段类似，实际输出和预测输出之间的差异被用于更新模型。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9SJbcI1YJnCWNvicVRqUuHJELIDISpwKrSO4Fb1PkbsoKICT6IBZKhGaq4KFhvMa3Ttz5eRSUrtqQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

图2：碰撞预测网络的运行

碰撞预测网络基于贝叶斯深度学习（BDL）。原因在于，目前使用的其他深度学习方法已知会根据它们所看到和感知的内容进行硬性分类。在像自动驾驶汽车这样由多个组件组成一个复杂整体的系统中，这种方法的缺点变得明显，一个组件的错误可能会在管道中产生滚雪球效应，导致后续组件产生灾难性的输出。克服这个问题的一种方法是使用贝叶斯深度学习（McAllister 等人）。贝叶斯模型将提供更好的结果（Kendall 和 Gal），因为此类模型生成考虑了不确定性的概率分布作为输出，这可以用于模型预期生成的碰撞可能性输出。此外，这意味着模型不仅会传播分类输出，还会传播与输出相关的模型不确定性，以便高层组件可以被开发为在管道中前一个组件的不确定性较高时以保守的方式做出反应。

所提出的系统具有明确的优势。最重要的是，这样的系统不仅关注未来的自动驾驶汽车，还可以用于当前的高级驾驶辅助系统（ADAS），从而允许在未来更平稳地过渡到自动驾驶汽车。其次，该模型可以被视为通过考虑来自多个来源的数据做出直观的 “知情决策”。此外，这样的系统还可以很好地泛化和扩展到车辆可能遇到的不同场景。然而，在模型开发过程中可能遇到的主要问题之一是考虑处理来自不同来源、不同格式的输入数据。接下来，需要内置冗余来补偿传感器故障 / 故障，使得传感器的故障不会影响系统的准确性。另一个与该方法相关的需要实验和验证的主要方面是使用一个基于机器学习的组件来监督另一个组件。

**03**

**结论**

这项工作涵盖了使用机器学习技术的智能组件的安全的不同方面，以便实现人工智能在自动驾驶中的集成。重点是确保基于机器学习方法的高关键应用安全的主要关注点和挑战，特别强调神经网络。传统的安全方法对此类系统不够充分，因此，需要更具体的方法，如监控技术，如所提出的碰撞预测网络，该网络保证系统功能的可接受安全水平。

来源：

https://mp.weixin.qq.com/s/jfI-wXnPobhtEvNNla6OWQ

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=...