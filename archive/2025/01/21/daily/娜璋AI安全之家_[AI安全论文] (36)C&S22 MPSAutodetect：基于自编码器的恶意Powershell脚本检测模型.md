---
title: [AI安全论文] (36)C&S22 MPSAutodetect：基于自编码器的恶意Powershell脚本检测模型
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501253&idx=1&sn=7f467401adcf67cc67d7c2d3573e7c2e&chksm=cfcf7508f8b8fc1e5be31d7896f233c533e1591fe41a83de83293ee9930109814a8eadfc435b&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2025-01-21
fetch_date: 2025-10-06T20:11:44.889398
---

# [AI安全论文] (36)C&S22 MPSAutodetect：基于自编码器的恶意Powershell脚本检测模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rjA189uVth7ysQhCToGYkeZekrickribUWTfFsUUd8IsMjJRFice43Kiadw/0?wx_fmt=jpeg)

# [AI安全论文] (36)C&S22 MPSAutodetect：基于自编码器的恶意Powershell脚本检测模型

原创

姚迪

娜璋AI安全之家

> 2024年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koyCt0jxRGu7e9Yic09B3CmrBZ70xVJicDHicAK2icfWRXL561kJvJCY9zPw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

《娜璋带你读论文》系列主要是督促自己阅读优秀论文及听取学术讲座，并分享给大家，希望您喜欢。由于作者的英文水平和学术能力不高，需要不断提升，所以还请大家批评指正，非常欢迎大家给我留言评论，学术路上期待与您前行，加油。

该文是贵大0624团队论文学习笔记，分享者姚迪同学，未来我们每周至少分享一篇论文笔记。前一篇博客介绍了TIFS’24 基于攻击表示学习的高效内存APT猎杀系统（MEGR-APT）。这篇文章将带来Computers & Security2022的MPSAutodetect，提出一种基于堆叠去噪自编码器的恶意Powershell脚本检测模型。本文首次结合SDA（自编码器）来提取PowerShell脚本的关键特征，并使用XGBoost进行分类。由于我们还在不断成长和学习中，写得不好的地方还请海涵。希望这篇文章对您有所帮助，这些大佬真值得我们学习。fighting！

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63riaWX19cTSohKUsrP68PlOxUBSCIcA07CiaKWgf7NQNLF0KlUFIh0SBQA/640?wx_fmt=png&from=appmsg)

```
原文作者：Amal Alahmadi, Norah Alkhraan, Wojdan BinSaeedan 原文标题：MPS Autodetect: A Malicious Powershell Script Detection Model Based on Stacked Denoising Auto-Encoder 原文链接：https://www.sciencedirect.com/science/article/pii/S0167404822000578 发表会议：Computers & Security 2022博客作者：贵大0624团队 姚迪
```

**一.摘要**

PowerShell是一个用于自动化管理任务的重要工具。它是一个预安装在Windows机器上的开源工具，可以在许多其他操作系统上访问。管理员通常使用PowerShell来执行一系列典型的管理任务，例如添加和删除帐户、编辑组以及访问难以找到的用户信息。

然而，研究人员最近发现PowerShell被用来执行各种攻击。这些攻击利用PowerShell的大量属性来访问特权信息，获得对整个机器的控制或在组织中传播。由于这些恶意脚本的混淆性和复杂性，检测成本高昂且困难重重。

在这里，我们提出了恶意PowerShell脚本自动检测(MPSAutodetect)，这是一种依靠机器学习技术检测恶意PowerShell脚本的检测模型。我们的模型是通过使用堆叠去噪自编码器(sda)来提取有意义的特征而构建的。这些有价值的、容易获得的特征被输入到极端梯度增强（XGBoost）分类器中。收集了两个实质性的数据集（已标记和未标记），以监督和半监督的方式训练和测试MPSAutodetect。该数据集包含恶意和良性混淆脚本。实验结果表明，无论从SDA中提取的特征如何，监督方法都能获得更好的检测效果，其真阳性率显著达到98%，假阳性率低至0.6%。因此，对MPSAutodetect的分析表明，该模型在没有手动特征工程的麻烦过程中取得了令人满意的性能。

**二.引言及前置知识**

PowerShell是一种流行且功能强大的面向对象脚本语言和命令行shell，预安装在Windows机器上。它允许管理员和用户在操作系统上操纵和运行命令。最近，许多报告表明，网络犯罪分子已经利用PowerShell的能力来实施攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rhyqmmAAHNuqLkgMfhafvGtjvKGuiaonNI6B8XM6CyLWgLYJgUPDAKZA/640?wx_fmt=png&from=appmsg)

与Power-Shell相关的最常见攻击是Livingoff The Land攻击（离地攻击）。这种攻击是指利用系统的本地工具来攻击自身，攻击者使用自动现成的工具反复混淆脚本，导致检测方案面临更大的挑战。此外，大多数PowerShell日志记录在默认情况下是禁用的。因此，恶意的脚本很容易传播。同时，PowerShell命令和文件不会写入磁盘。网络犯罪分子利用这一漏洞几乎没有留下任何活动痕迹供法医分析。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63r1tFqoltNtwBzLbbzW9n1ldLPasQ2gbBPibpEJGV6lDl9ibOaI13BZwZg/640?wx_fmt=png&from=appmsg)

什么是PowerShell？
PowerShell 是一种跨平台的任务自动化解决方案，由命令行 shell、脚本语言和配置管理框架组成。

什么是autoencoder？
autoencoder是一种无监督的学习算法，主要用于数据的降维或者特征的抽取，在深度学习中，autoencoder可用于在训练阶段开始前，确定权重矩阵W的初始值。自动编码器是一种无监督的数据维度压缩和数据特征表达方法。在大部分提到自动编码器的场合，压缩和解压缩的函数是通过神经网络实现。

* 隐藏层从输入到隐藏层即为Encoder（编码器），从隐藏层到输出即为Decoder（解码器）。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rw67m6hQd7YGe7Q7I7D7elcL6JRTaUAHQZnw9ODKYJTP6GoAicKGEZjA/640?wx_fmt=png&from=appmsg)

powershell检测系统现有工作：

* 利用机器学习算法提出了一个字符级深度神经网络该网络的构建和训练是为了在字符级别检测恶意脚本。考虑使用统一长度的字符来构建字符级的one-hot编码表示脚本。这种向量表示被输入到许多卷积神经网络(CNN)配置以及传统的自然语言处理(NLP)检测器中
* 提出了一种使用混合特征检测恶意PowerShell脚本的方法。他们专注于可以从脚本中提取的特征类型，其中在使用FastText进行脚本嵌入的同时呈现了许多手动提取的特征。从恶意程度的角度分析了这些单个特征之间的差异。特征集合被输入到随机森林分类器中

现有方法的局限:

* 攻击复杂性与检测难度的增加，检测成本高昂且困难重重；
* 恶意脚本种类繁多，行为模式和特征差异很大，使得统一检测模型的泛化能力受到限制；
* 传统方法通常需要手动提取特征，这一过程复杂且耗时，难以应对不断变化的恶意脚本技术。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rxPOaIsVvEuK7yiah9tichnwYJ1xiam1xv4csgRexQJiceO1Es1icJsXHqfA/640?wx_fmt=png&from=appmsg)

本文贡献可以总结如下：

* 提出恶意PowerShell脚本自动检测(MPSAutodetect)，这是一个使用机器学习算法检测恶意PowerShell脚本的模型，同时消除了手动查找特征的过程。MPSAutodetect依赖于SdA从PowerShell脚本中提取有意义的特征。
* 整合了强大的XGBoost分类算法，利用从SdA结构中获得的特征。以两种方式实现MPSAutodetect，比较监督和半监督方法的效率。
* 通过定义四个具有不同恶意对良性脚本解释比率的数据集来验证模型的效率。用于训练和评估模型的数据集语料库包含混淆的脚本，本质上赋予MPSAutodetect识别PowerShell脚本的能力，即使它具有复杂的形式。

**三.本文模型**

1.总体架构

MPSAutodetect整体框架如下图所示：

* PowerShell预处理
* Auto-Encoder模型提取特征
* 梯度增强及分类预测

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63roAgicicA62It3JIdicFbDSbXia9v6svajfqF7mibLxqsmAaTUoJD8dm6KIA/640?wx_fmt=png&from=appmsg)

2.PowerShell预处理

PowerShell是一种面向对象的脚本语言，具有跨平台的命令行shell。它可以与net、COM、WMI和XML对象一起工作，这使PowerShell命令行与其他命令行区别开来PowerShell中的命令称为cmdlet，它具有动词-名词语法。

攻击者利用PowerShell的原因有很多，主要是因为它提供了对重要操作系统功能的访问。预处理算法如下：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rdxZFgXEugRTkYiaFbt5YIzibLeEMJo8mx73Ap0ZjKskQlCRDf31jAEfA/640?wx_fmt=png&from=appmsg)

3.Auto-Encoder

堆叠自编码器（Stacked denoising auto-encoder，SDA）结构如下所示：

* 构建单层自编码器
* 逐层堆叠训练
* 反向解码器构建

该结构以一种方式降低了维数， 即将x维的输入编码为h维表示，同时在对输入进行解码之前保持h < x。这个h维表示层被称为瓶颈层，将编码器与解码器结构分开。当SdA用于特征提取时，这一层非常有价值。在这种情况下，省略 了重建过程（解码器），并从这个瓶颈层中提取特征。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rMydEf26Iqqj8Fmrrrcibvzibvwa2Uat5624vsicWDtqWE22icYgVsmJTfw/640?wx_fmt=png&from=appmsg)

4.XGBoost

XGBoost全称为eXtreme Gradient Boosting，本文利用其进行识别恶意Powershell。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rk4jkiaK2w1ibhFdEvJGYQRgaVibej9o23Bja6XTkC7c4Piag5ORZlCZDAw/640?wx_fmt=png&from=appmsg)

**四.实验评估**

1.数据集

PowerShellGallery

* 该数据集由5463个良性脚本和6609个恶意脚本和命令组成，这些脚本和命令是在MPSAutode-tect的训练和测试期间使用的。重要的是，该语料库包含来自恶意类和良性类的混淆脚本，允许MPSAutodetect对实际的脚本表示进行训练。该数据集的构建是为了以监督的方式训练和测试模型。
* https://www.powershellgallery.com

Github

* 提供的一些未标记脚本来构建半监督算法，这是通过实现无监督预训练和微调来实现的。未标记的数据集由40,765个脚本组成。
* https://www.github.com

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rsy0wtethmUQNt7ibeNYDPOo1AF2VgoLFORhcARQ0hUfdTUQSVXjRmKg/640?wx_fmt=png&from=appmsg)

2.实验结果分析

（1）在不同类型的噪声对MPSAutodetect效率的对比

当噪声因子为0.5时，高斯噪声的AUC值最高，为0.974；高斯噪声被证明比随机噪声产生更好的性能。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rziaZ5JSp9xz0njoxCHkmRkPSTUIO9NXDrekiapAe6icYGic7WZibWWgMSHQ/640?wx_fmt=png&from=appmsg)

（2）在不同深度和单元尺寸对MPSAutodetect模型性能对比
1024个单位代表数据集的维度，产生了0. 990 AUC分数；单位大小的减小可能会导致维度过于模糊，导致模型表现不佳。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rLE4Ae4zVDg8wpOBtBOSguTeXSib9dicR4WGXOL3hmyhIA49niaAIUr8Lw/640?wx_fmt=png&from=appmsg)

（3）在XGBoost分类器不同参数对比
参数调优是优化分类器性能的关键部分，它可以提高MPSAutodet ect的效率
XGBoost参数对模型性能有显著影响。综合调整这些参数，可显著优化模型的性能和鲁棒性。

* eta参数：控制学习率，较小值（如0.1）提高AUC分数，优化模型精度。
* colsample\_bytree参数：控制特征采样比例，合适的值（如0.8）可提升分类器稳定性和AUC分数。
* alpha和lambda参数：正则化项防止过拟合，默认值1和0效果最佳

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rrTeZmgpVo8MLYxy87icnWMTRz5ah1PCNicicjSYictnKM8lG6cpgYxj5Fg/640?wx_fmt=png&from=appmsg)

（4）在不同数据集上监督和半监督运行对比
监督和半监督两种方法的AUC值都很高，分别为0.991和0.980，但监督模型优于半监督模型。当数据集比率相对均匀时，半监督方法表现优异。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rfLckVhzfhp5j6cef4A5v95bbtyfrWtEQ3Mko6CBxB7QHsiaSB574EKQ/640?wx_fmt=png&from=appmsg)

性能比较如下表所示：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPOic8pEnFq20HVfxLYSH63rhJ5LtNzntzgsHugNYhrPAnjNLpcxJAVUIBrpQ8KFricfNglw8kia2CXA/640?wx_fmt=png&from=appmsg)

**五.总结及个人感受**

本文提出并验证了 MPSAutodetect模型，来确定这些脚本的恶意性。

* 该模型利用SdA架构来提取分类所需的特征，实现特征提取方法以帮助简化检测过程的工作
* 该模型以监督和半监督的方式实现，旨在利用未标记脚本的可用性
* 有监督的MPSAutodetect模型显示出令人满意的结果，低0.6%的FPR和高98%的TPR

本文作者提出了未来该方向工作的重点：

* 收集更多的恶意样本，以确保该模型对攻击技术不断变化的行为保持有效
* 研究将这种方法扩展到用不同编程语言编写的攻击中
* 计划增加脚本恶意软件家族分类的特殊性，并评估是否可以检测到新恶意软件家族的引入

> 『网络攻防和AI安全之家』目前收到了很多博友、朋友和老师的支持和点赞，并且保持每周七次更新，尤其是一些看了我文章多年的老粉，购买来感谢，真的很感动，类目。未来，我将分享更多高质量文章，更多安全干货，真心帮助到大家。虽然起步晚，但贵在坚持，像十多年如一日的博客分享那样，脚踏实地，只争朝夕。继续加油，再次感谢！
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koyCt0jxRGu7e9Yic09B3CmrBZ70xVJicDHicAK2icfWRXL561kJvJCY9zPw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

(By:Eastmount 2025-01-20 写于贵阳)

**前文推荐：**

* [[AI安全论文] 01.人工智能真的安全吗？浙大团队分享AI对抗样本技术](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247488844&idx=1&sn=5b6ee2f94c1d1af00879291c5d09a8b7&chksm=cfcca581f8bb2c97969f13181f75efba8425d106091e19bdca0d691917e6a2f2cc287d674b17&s...