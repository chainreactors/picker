---
title: 谛听 | 针对工业物联网中小规模后门攻击的精确防御方法
url: https://mp.weixin.qq.com/s?__biz=MzU3MzQyOTU0Nw==&mid=2247492081&idx=1&sn=cfd2d8d46d59468c7183fd2a075c28a8&chksm=fcc363b5cbb4eaa3b7527d9a46eb52a18b873847f532f7f18afb3131f6f5259d564c35a695a6&scene=58&subscene=0#rd
source: 谛听ditecting
date: 2024-12-25
fetch_date: 2025-10-06T19:39:21.838744
---

# 谛听 | 针对工业物联网中小规模后门攻击的精确防御方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/smuOnscQgdFX7JI4vjCib53BEzpvyRL5Tdgwmt70RW23vP8RzwsUnLrD7Zdq4GENDHwib92NXCIibrYs6icYu9vPiag/0?wx_fmt=jpeg)

# 谛听 | 针对工业物联网中小规模后门攻击的精确防御方法

谛听网络安全团队

谛听ditecting

近日，“谛听”团队冉子用博士撰写的论文《Precise Defense Approach Against Small-Scale Backdoor Attacks in Industrial Internet of Things》（针对工业物联网中小规模后门攻击的精确防御方法）被国际期刊《IEEE Internet of Things Journal》录用。（点击文后“阅读原文”可获取论文）

随着深度学习从海量数据集中提取高维结构的卓越能力，其在工业物联网(IIoT)中的应用越来越普遍。然而，深度学习固有的安全漏洞对工业物联网系统构成了重大威胁，特别是以后门攻击的形式。目前的防御方法主要是为图像处理任务而设计的，由于工业环境的独特性，当直接应用于工业物联网应用时，由于缺乏精度，其有效性显着降低。为了解决这些挑战，本文提出了一种适合工业环境的触发检测方法，能够在检测过程中精确计算触发值。在此基础上，本文引入了一种基于显著性映射的触发器修剪方法来进一步优化触发器。最后，利用这些改进的触发器，我们执行触发器恢复以完成针对IIoT模型的后门防御。此外，通过整合这些方法，构建了一个针对工业环境中后门攻击的综合检测-修剪-恢复防御框架。跨多个工业场景的实验结果表明，本文提出的方法增强了工业应用对后门攻击的鲁棒性，优于现有的防御机制。

《IEEE Internet of Things Journal》是IEEE旗下的一本权威学术期刊，旨在促进不同领域的交叉融合与创新应用，其涵盖了传感器技术、嵌入式系统、通信与网络、数据分析与处理、安全与隐私等关键主题，该期刊以其高质量的学术论文和严格的审稿流程闻名，吸引了来自全球范围内的顶尖研究者和学者的投稿。其发表的论文通常具有创新性、前瞻性和实用性，为学术界和工业界提供了一个重要的交流平台，推动了物联网技术的快速发展与应用。

影响因子：10.6

文章引用方式：

Ran Z, Yao Y, Li W, et al., Precise Defense Approach Against Small-Scale Backdoor Attacks in Industrial Internet of Things," in IEEE Internet of Things Journal, doi: 10.1109/JIOT.2024.3490579.

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRkiaxftJLLj40kjMEDOwoW9M82NUXFjUum6lAI0wlYOI4rdmRX0Q0hkrw/640?wx_fmt=png&from=appmsg)

**论文内容介绍**

**1 研究背景**

工业人工智能（Industrial AI，简称IAI）在故障检测、入侵检测和时间序列分类等领域具有广泛应用。在故障检测中，IAI通过实时分析设备的传感器数据，能够准确识别潜在故障并提前预警，减少停机时间并实现预测性维护。在入侵检测方面，IAI通过监控网络流量和系统行为，能够及时发现异常操作或网络攻击，提高工业系统的安全性。而在时间序列分类中，IAI能够分析生产过程中的多维数据，识别趋势和异常，预测设备性能变化或生产瓶颈，优化生产调度和资源利用。总体来看，IAI的应用不仅提升了工业生产的效率与安全性，还推动了智能化管理的实现。

随着深度学习从海量数据集中提取高维结构的卓越能力，其在工业物联网(IIoT)中的应用越来越普遍。然而，深度学习固有的安全漏洞对工业物联网系统构成了重大威胁，特别是以后门攻击的形式。目前的防御方法主要是为图像处理任务而设计的，由于工业环境的独特性，当直接应用于工业物联网应用时，由于缺乏精度，其有效性显着降低。为了解决这些挑战，本文提出了一种适合工业环境的触发检测方法，能够在检测过程中精确计算触发值。在此基础上，引入了一种基于显著性映射的触发器修剪方法来进一步优化触发器。最后，利用这些改进的触发器，执行触发器恢复以完成针对IIoT模型的后门防御。此外，通过整合这些方法，构建了一个针对工业环境中后门攻击的综合检测-修剪-恢复防御框架。

**2 关键技术**

为了解决现有深度学习模型在应用于工业物联网应用时存在的挑战，构建了一个针对工业环境中后门攻击的综合防御框架，主要贡献如下：

* 提出了一种工业物联网后门触发器的检测方法。通过迭代分析模型的所有标签，识别出显著的异常值，并确定后门触发器的组成和相应的目标标签。此外，使用L1正则化项来限制计算触发器的大小，使用L2正则化项来最小化触发器与原始数据特征之间的差异。这种方法提高了触发器的精度，以更好地适应工业环境的特定要求。
* 提出了一种提高触发精度的触发修剪方法。该方法通过去除触发器中不相关的特征和噪声，提取重要成分，提高触发器的精度。通过这种方法，改进的触发器可以捕获相关信息，同时最小化不相关的特征，从而提高触发器的总体精度。
* 提出了一个检测-修剪-恢复框架来保护工业模型免受后门攻击。该框架侧重于提高每一步的触发精度，然后利用保护方法对模型进行保护，以有效地适应工业环境。
* 文章在三个工业背景下进行了比较实验，对应于三个公共数据集，以验证提出的方法的有效性。实验结果表明，该方法能有效提高后门防御的有效性，优于对比方法。

**3 方法介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRkr4CN8iaZTf7tMtqIicaOiaBicx1rCP5Gwic9cVLoh52SEFH1zRkWeozkNdg/640?wx_fmt=png&from=appmsg)

文章提出了一个三步框架，旨在逐步提高每个阶段的准确性，从而提高受损工业物联网深度学习模型的恢复性能。

![](https://mmbiz.qpic.cn/mmbiz_svg/WD4FduqfeKJX8cI1MPCqIQQnnKggSybAQDpibj3VicWU0JJucjEibFIRvXrCuib3icQBrVWCyiavkhgrxZPbztZPniaNs6BSI8jdROW/640?wx_fmt=svg&from=appmsg)

**触发器检测**

![](https://mmbiz.qpic.cn/mmbiz_svg/WD4FduqfeKJX8cI1MPCqIQQnnKggSybARJfBJricUZriboT2vB40rW1GYNakVEVqs1Q3uibN8VxLgibBSfmlFpUBnXkC078Nicqfe/640?wx_fmt=svg&from=appmsg)

在执行后门攻击期间，攻击者需要操纵训练数据。许多方法，如BadNet和特洛伊木马等，都是为此目的而设计的。这些方法可以简洁地表示为一个通用形式：

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRkzMibrgMzxjZiad1yZqsjCpMBbTj2S0lIT0HOd0jCGry7amZiaQy2EZqAA/640?wx_fmt=png&from=appmsg)

对于即将部署的经过训练的工业深度学习模型，本文的目标是检测后门的存在。在受损模型中，与未受影响的标签相比，被感染的标签显示出减少了诱导误分类的修改需求。因此，通过迭代模型的所有标签，可以确定是否存在只需要微小修改即可实现错误分类目标的标签。这个过程不仅可以作为工业模型中存在后门的指示器，还可以识别作为后门攻击目标的标签。在每次迭代中，可以使用优化方法计算指定目标标签对应的临时触发器，优化公式如下:

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRkQ6WoTwBpj0D1DEbgciajLwhqwSnEjB4oaibE3hibMiaZwKhblS0MQJvmcg/640?wx_fmt=png&from=appmsg)

由于主优化过程寻求相应的临时触发器，因此包含L1、L2惩罚项有助于从数据中提取最关键的特征。这种增强有助于提高触发器识别的精度，避免由于缺乏精度而导致的后门恢复失败。这在工业场景中的小幅度后门攻击中尤为重要。

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRkDKxgzWQnkvttyuAKBJmUGh9hPzs4D6RicNu24LKjTnMSjh1pGOYhW8Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/WD4FduqfeKJX8cI1MPCqIQQnnKggSybAQDpibj3VicWU0JJucjEibFIRvXrCuib3icQBrVWCyiavkhgrxZPbztZPniaNs6BSI8jdROW/640?wx_fmt=svg&from=appmsg)

**基于显著性图的触发器修剪**

![](https://mmbiz.qpic.cn/mmbiz_svg/WD4FduqfeKJX8cI1MPCqIQQnnKggSybARJfBJricUZriboT2vB40rW1GYNakVEVqs1Q3uibN8VxLgibBSfmlFpUBnXkC078Nicqfe/640?wx_fmt=svg&from=appmsg)

通过使用工业深度学习模型来计算测试样本的显著性图，不仅可以深入了解模型在存在后门的情况下对测试样本进行错误分类的原因，还可以对这些样本中特征的重要性进行排序。这个过程有助于确定导致构建更精确触发器的基本特征。然而，在获得临时触发器后，面临的挑战是缺乏一个阈值来过滤哪些特征是触发器的有效成分。这是由于工业应用对真正触发因素的确切大小缺乏了解。因此，为了区分无用和必要的特征，并为它们建立一个阈值，本文将临时触发器注入多个测试样本中。利用预测函数进行预测，叠加预测函数的显著性图，消除触发检测部分检测到的临时触发中不相关的特征和噪声，并采用中位数绝对偏差(MAD)方法来构建阈值。这个过程可以从原来较大的触发器中提取有效成分，去除无用的特征，提高触发器的精度。预测函数显著性图的计算公式如下:

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRkCCoWbGP50iaZtkgW38TI2I9lvvIXB88OmIYJ3kfF7PHybuZFObNOphA/640?wx_fmt=png&from=appmsg)

然后使用以下公式修剪触发器:

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRkl9UGRC6NgDkiaicNAJkDm5RBgFTo3EVN3WBKBQSpdbuxGJMejlGmcYZg/640?wx_fmt=png&from=appmsg)

利用MAD计算异常分数，可以识别每个样本中对预测模型至关重要的特征。这对于确定触发器的位置至关重要。通过控制所选特征相对于原始特征集的百分比，确定一个阈值，只允许有效的特征保留在触发器中。

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRkuibIzAf1ia4XBtCd3jGSicXQbqy0qsRTicKdlM6icC1czUFcakX6voYHvag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/WD4FduqfeKJX8cI1MPCqIQQnnKggSybAQDpibj3VicWU0JJucjEibFIRvXrCuib3icQBrVWCyiavkhgrxZPbztZPniaNs6BSI8jdROW/640?wx_fmt=svg&from=appmsg)

**触发器恢复**

![](https://mmbiz.qpic.cn/mmbiz_svg/WD4FduqfeKJX8cI1MPCqIQQnnKggSybARJfBJricUZriboT2vB40rW1GYNakVEVqs1Q3uibN8VxLgibBSfmlFpUBnXkC078Nicqfe/640?wx_fmt=svg&from=appmsg)

本文提出了一种动态结合数据增强和反学习方法的新策略。通过增加测试集中样本空间的密度，增强了反学习方法的有效性，从而提高了模型对后门攻击的鲁棒性。该策略不仅增强了模型抵御此类攻击的能力，而且还保持了模型在正常输入上的有效性，从而提供了一个平衡的解决方案，在不显著影响性能的情况下确保安全性。

通过结合CutMix和Mixup技术，将训练点的凸组合与相应的凸组合标签对齐。这种融合使输入空间中的类区域凸化，提供了类边界的系统描述，并促进了小的非凸区域的去除。在这些区域中，攻击数据实例被分配了一个对抗标签，而周围是带有不同标签的(非攻击)实例。当面对不同的工业场景和业务需求时，该技术展示了增强的通用性和鲁棒性。因此，模型可以在保持最佳性能的同时适应工业环境的不同复杂性。公式如下:

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRkKBJBp69biaW1gONuiaYXKVjfQlYvqawJ6hVCP9weOgZfHWsbUjdRv8XQ/640?wx_fmt=png&from=appmsg)

其中，在Mixup和CutMix方法中，使用相同的参数来确保数据样本点在样本空间中被密集平均。对于测试数据集中每三个连续的样本，计算一个新的样本，并通过与样本类似的计算得到其对应的标签。这种样本生成过程有效地增加了样本空间中数据点的密度，促使触发器恢复效果显著提高。

**4 实验评估**

**实验设置**

为了验证方法在各种工业环境中的有效性，本文选择了三种不同的工业场景进行实验验证:故障检测(CWRU)、入侵检测(MSU)和时间序列分类(UCR-ED)。

**故障检测**:故障检测是指对设备、机械或系统的运行状态进行监测和分析，并对异常进行识别和预测，以保证生产过程的可靠性、安全性和高效性。这是工业环境中的常见要求。凯斯西储大学轴承数据集(CWRU)是一种广泛应用于故障检测的数据集。在本文的实验中，提取了代表电机转速为1797 RPM、故障直径分别为0.1778mm、0.3556mm和0.5334mm的9组数据。这些选择的数据与一组标准数据相结合，构建一个10类数据集用于实验分析。

**入侵检测**:入侵检测系统(IDS)在保障工业运行安全方面发挥着重要作用。密西西比州立大学天然气数据集(MSU)是从天然气管道SCADA系统收集的，包含各种特征和多种类型的攻击。它经常用于评估复杂工业控制环境中IDS的性能。

**时间序列分类**:在工业场景中，时间序列数据通常来自传感器、机器日志和操作记录。这些数据可以用于多种任务，包括质量监测和能源管理。UCR Archive是一个著名的时间序列分类任务的公共数据集。在实验中，选择了UCR Archive中的ElectricDevices数据集进行实验分析，该数据集由几个电气设备及其相应的特征组成。

**后门攻击效果基准**

为了评估触发器检测和触发器恢复方面的性能，本文评估了工业模型在数据集上的分类准确性以及当触发器应用于测试样本时的攻击成功率。“攻击成功率”量化了分类到目标标签的攻击样本的百分比。作为基准，衡量了每个模型的干净版本的良性准确率。

/无模型保护的不同工业场景下后门攻击的攻击成功率和良性准确率/

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRkRJNFRljpyIc716OGDDbYiaZ7c4aonVzGWl0ELS4LEQyxXhXuP6ll8WA/640?wx_fmt=png&from=appmsg)

**触发器检测效果**

实验评估了提出方法在各种工业环境中的检测能力。结果表明，与传统的图像域触发检测方法相比，提出的触发器检测方法在各种工业环境中保持一致的检测性能。

/不同方法在触发器检测中的性能/

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRk38WUF4sPzuP4Wm5u7c2YVWLpQicdwa5jUQqePeO2frmzsxoe9CRrkUg/640?wx_fmt=png&from=appmsg)

在检测性能的基础上，以MSE和SSIM为指标，评估了不同触发检测方法获得的临时触发器和实际触发器之间的差异。差异的大小被用来衡量临时触发的精度。结果表明，提出的方法在保持检测精度的同时，实现了更精确的临时触发器计算，使其更接近原始触发器，精度提高。

/真实触发器和临时触发器的差异/

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRku8YibNKxEMSpOZC6wojHC4gIAe2uIUWFzXZ2ssv7v0JJNtAyl3vZBew/640?wx_fmt=png&from=appmsg)

将表格中的数据可视化后如图所示，提出的方法在准确率上优于对比方法，实现了更低的MSE和更高的SSIM。这表明我们的方法不仅保持了整体检测性能，而且在精确定位触发位置方面表现良好。

![](https://mmbiz.qpic.cn/mmbiz_png/smuOnscQgdGWzuSdpqGkLN6APibLTiaaRkmIn7L29cCMduVgjtJpqwBKaNdymsPstNabWPCIv1Ku447m69tFI7Kg/640?wx_fmt=png&from=appmsg)

结论：证明了提出的方法可以在保持检测准确率的前提下，提高检测触发器的精度。

**触发器修剪效果**

通过MSE和SSIM评估修剪前后临时触发器之间的差异。将实验结果可视化后可以看出，图(b)中的红框明显小于图(a)中的红框，说明触发器修剪方法去除了无用...