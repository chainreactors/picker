---
title: 【顶刊论文分享】DeepSec：深度学习模型的安全性分析平台
url: http://blog.nsfocus.net/deepsec/
source: 绿盟科技技术博客
date: 2022-12-09
fetch_date: 2025-10-04T01:00:37.630631
---

# 【顶刊论文分享】DeepSec：深度学习模型的安全性分析平台

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 【顶刊论文分享】DeepSec：深度学习模型的安全性分析平台

### 【顶刊论文分享】DeepSec：深度学习模型的安全性分析平台

[2022-12-08](https://blog.nsfocus.net/deepsec/ "【顶刊论文分享】DeepSec：深度学习模型的安全性分析平台")[员苗](https://blog.nsfocus.net/author/yuanmiao/ "View all posts by 员苗")[对抗攻击](https://blog.nsfocus.net/tag/%E5%AF%B9%E6%8A%97%E6%94%BB%E5%87%BB/), [深度学习模型](https://blog.nsfocus.net/tag/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B/)

阅读： 1,918

## ****一、概述****

在对抗攻击场景下，攻击者通过对合法输入的微扰生成对抗样本（Adversarial Example, AE），并试图使用对抗样本使目标深度学习（DL）模型误分类。由于DL模型在对抗样本的攻击下较为脆弱，因此限制了深度学习应用于具有较高安全性要求的领域，如自动驾驶、人脸识别、恶意软件检测等。防守方通常希望增强模型对对抗样本的防御能力，同时又能最大限度地保证模型的分类性能。虽然学术界和工业界对对抗样本的研究逐渐深入，攻击和防御手段在不断更新，但是仍很难说明哪些攻击样本隐蔽性或可转移性更高，或者哪种防御方法更加有效通用。

DEEPSEC平台的设计初衷便是希望构建一个对攻击和防御手段进行全面评估的平台，该工作发表在2019年IEEE symposium on security and privacy（S&P）。DEEPSEC平台内包含了16种先进的攻击手段和10种攻击效用指标，以及13个防御手段和5项防御效用指标，评价指标体系十分完善。通过对多种场景进行广泛的分析，不仅能够帮助研究人员和从业者评估各种攻击/防御手段的有效性，还能对各类攻击和防御手段进行全面比较。图1展示了DEEPSEC平台的整体架构。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/图１-300x100.png)

图１DEEPSEC平台的整体架构

## ****二、D********EEPSEC********平台的设计思路****

为了保证平台的实用性，DEEPSEC平台在相同环境下对不同的攻击/防御方法进行比较，且该平台具有较高的可拓展性，支持加入新的攻击/防御方法。在这一工作中，作者主要是对非自适应和白盒攻击场景进行分析，这意味着攻击者非常了解目标DL模型，但不知道可能防守方可能使用的防御手段。表1中列举了DeepSec平台评估的攻击/防御方法。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/表1-210x300.png)

表1. DeepSec平台中评估的攻击/防御方法

从对抗特异性的角度来说，可以将攻击分为无目标攻击（UA，Un-targeted Attack）和有针对性的攻击（TA，Targeted Attack）。UA的目标是生成可能被误分类的对抗样本，而TA的目标是生成可能被误归类为特定类别的AE。从攻击频率的维度出发，则可以分为非迭代攻击（Non-iterative attack）和迭代攻击（Iterative attack）两种，其中非迭代攻击只需一步就可以生成AE，而迭代攻击则需要多次迭代更新AE。下面简单的从其中选取几个攻击方法作为例子进行说明。Fast Gradient Sign Method（FGSM）是第一个也是速度最快的非迭代特异性攻击方法，其核心思路是通过线性化损失函数，选取最大化受约束的损失来对图像进行扰动。Basic Iterative Method（BIM）方法则是在FGSM的基础上增加了迭代步骤，需要多次迭代优化并在每一次迭代后调整优化方向。Least-Likely Class（LLC）攻击方法是FGSM方法的有目标攻击版本，这一方法会指定与原始图像差异最大的类别作为目标类，而Box-constrained L-BFGS（BLB）则是迭代的特异性攻击方法，但是这一方法仍存在耗时且难以在大规模数据集上实现等问题。

对于攻击者而言，攻击手段的效用意味着能够生成成功攻击的AE的概率。一般来说，成功的AE不仅可以被模型错误分类，而且通常人也不易察觉，且具有较强的鲁棒性。因此，这一工作定义了10个评价攻击方法的指标，如表2所示。与表征对抗样本分类情况相关的特征包括误分类率（Misclassification Ratio, MR）以及Average Confidence of Adversarial Class（ACAC）和Average Confidence of True Class（ACTC），前者是指将对抗样本错误分类的概率，后两个指标则分别描述将对抗样本分类到错误和正确的类别的平均置信度。

此外，DEEPSEC平台还设计了多个描述AE的不可感知性的效用指标，如Average Lp Distortion（ALDp）描述的是对抗样本与其他数据的距离，平均结构相似性（ASS）描述的是两幅图像之间相似性等。在将数据输入到DL模型之前，通常都需要对数据进行预处理，这一步骤可能会导致对抗样本的误分类率下降，因此描述对抗样本的鲁棒性也十分重要。例如可以通过计算错误分类的概率与所有其他类的最大概率之间的差距，从而得到噪声容忍限度（Noise Tolerance Estimation, NTE）来估计。

![](https://blog.nsfocus.net/wp-content/uploads/2022/12/表2-300x170.png)

表2. DEEPSEC平台使用的对攻击方法的评价指标

与此同时，DEEPSEC平台也对5种防守方法进行了评价。第一种防守方法是对抗训练，主要是通过在训练集中加入对抗样本来增强模型的鲁棒性，例如Naive Adversarial Training（NAT）方法。梯度掩蔽/正则化方法则是从模型梯度的角度出发，例如Defensive Distillation（DD）方法就是通过减少或平滑神经网络梯度的振幅，使防御模型对AE中的扰动不太敏感。此外，输入转换防御方法是在数据输入到原始模型之前，就消除测试输入中的对抗性干扰。例如在Random Transformations（RT）的防御方法中，测试图像首先经过两个附加的随机化层，然后将变换后的图像传递给原始模型。此外，表2中也列举了5个可以用于度量防御效果的指标。其中，最重要的指标是分类的准确性，而分类精度的方差（Classification Accuracy Variance, CAV）则描述的是防御增强的模型相对于原始模型的分类精度差异，Classification Rectify/Sacrifice Ratio（CRR/CSR）评估的是应用防御前后预测的差异。尽管采用防御手段后模型的准确性可能不会受到影响，但预测置信度可能会显著降低。因此，作者引入了Classification Confidence Variance (CCV)指标来描述防御增强模型与原始模型预测置信度间的方差，并使用Classification Output Stability (COS)来描述原始模型和防御增强模型之间的分类输出稳定性。

## ****三、样例分析结果****

在实际测试中，DEEPSEC平台中现有的大多数攻击方法都具有很强的攻击能力以及较高的MR。从迭代和非迭代攻击的比较结果来看，由于前者会多次迭代以找到最优扰动，因此误分类的概率通常会更高。除MR外，使用其他指标来对攻击方法进行评估也很重要。从将对抗样本分类到错误和正确的类别的置信度来看，通常ACAC较高的AE，其ACTC较低。而对于具有相似ACAC值的AE，通常ACTC较低的AE对其他模型具有更好的适应力，因为其他模型将其正确分类的概率较低。

在与不可感知性相关的指标中，PSD是对AE扰动最敏感的指标，其中L2攻击的PSD相比其他攻击（即L∞ 或L0攻击）更低。这意味着L2攻击生成的AE相对来说更难以察觉。相比之下，ASS则是最不敏感的指标，因为各种攻击方法生成的AE计算得到的ASS指标均差异不大。从鲁棒性的角度来说，通常ACAC较高的AE具有更强的鲁棒性，且与TA相比，大多数UA具有更高的鲁棒性。从可转移性的角度而言，不同的攻击方法展示出不同的可转移性，其中UA比TA的可转移性更高，而L∞ 攻击比其他攻击（即L2和L0攻击）更容易转移。

DEEPSEC平台对防御方法的测试结果显示，当使用准确度为指标对模型进行防御增强的训练或调整时，大多数模型都可以保持其分类性能。但是从防御方法的通用性来说，目前并未发现某个完整的防御方法是通用的，大多数方法都只能防御某些对抗攻击，且具有不同的优势和局限性。在对集成方法的评估中，分析结果表明不同防御方法的集成并不能显著提高整体的防御能力，但可以提高单个模型防御能力的下限。

通过对多个样例进行分析，DEEPSEC平台得到的上述结论对研究和应用的意义在于以下几个方面：首先，在公开共享或部署预训练的DL模型之前，模型的所有者可以使用DEEPSEC方便地选择现有的防御措施来保护其模型，并且还可以用来评估防御增强模型是否满足其效用/安全要求。其次，DEEPSEC可以统一系统地评估不同的对抗攻击和防御方法，可以在相同的实验设置（例如，DL模型、参数设置、评估指标、测试环境等）上进行实施和评估，从而避免在同样的问题上得出矛盾的结论。

## ****四、结论****

DEEPSEC平台的实验结果表明，目前使用的深度学习模型都需要在漏报和误报率之间进行权衡，难以同时保证较低的漏报率和误报率，而且大多数声称普遍适用的防御方法只能在有限的攻击场景下有效。此外，多种防御手段的集成虽然无法提高整体的防御能力，但可以提高单个防御方法效能的下限。DEEPSEC平台的设计、实现和评估，整体上搭建了一个用于深度学习模型的统一安全分析平台，其完备的评价体系建设是十分值得学习的。与此同时，DEEPSEC对现有的攻击和防御进行的统一标准评估，可以作为对抗性深度学习研究的有效基准，从而促进这一领域不断发展。

### 参考文献

[1] X. Ling **et al**., “DEEPSEC: A Uniform Platform for Security Analysis of Deep Learning Model,” in S&P, 2019.

[2] N. Papernot, P. McDaniel, S. Jha, M. Fredrikson, Z. B. Celik, and A. Swami, “The limitations of deep learning in adversarial settings,” in EuroS&P, 2016.

[3] N. Carlini and D. Wagner, “Towards evaluating the robustness of neural networks,” in S&P, 2017.

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/oss/)

[Next](https://blog.nsfocus.net/docker/)

### Meet The Author

员苗

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)