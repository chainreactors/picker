---
title: 每周文章分享-253
url: https://mp.weixin.qq.com/s/rev-6noZZ37ukjEM8yYe8A
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:40:45.194778
---

# 每周文章分享-253

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jBQAokCLibp2IdEb5FicLTicoGFhtQEmnpU3J2DJKENCAYruu5O85D5rYt88lkGVAGxadKNnXSs4YqR9KN8AfvIia4hGJJoeugZzsl6lHzZToFc/0?wx_fmt=jpeg)

# 每周文章分享-253

网络与安全实验室

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4DAaJy0Ok82ibMPxwHY4mibwrjmLoqmvIickMFksSta2uNYdIpd6BSh7GAKsqdYvoQq3Sg4RqvtofvuJLvGnIwDAIicnMN8A6wjias/640?wx_fmt=png&from=appmsg#imgIndex=56)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd79GRlwNhZak3b6NicAtrelJ5wXr5U8icCFGbOq9olPBSsVfSynibKpYAErrW6LMx4lyXdp5ibny1uCN8uPlrgJQNibuH3hYkIW2aBo/640?wx_fmt=png&from=appmsg#imgIndex=57)

**每周文章分享**

2026.03.23至2026.03.29

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd4Ohaz7tlbUgBU08mJu9dD8frItmtjJ1C9xvR9d9Gic4CYK1bBjJA40NMpK6T89bFlj2aNTod2cSPT666sMXxIEia1FJy7QbLnrQ/640?wx_fmt=png&from=appmsg#imgIndex=60)

**标题:**LGP: Layerwise Gradient Purify for Robust Federated Learning against Poisoning Attacks

**期刊:** IEEE TRANSACTIONS ON DEPENDABLE AND SECURE COMPUTING, VOL. 23, NO.1, JANUARY/FEBRUARY 2026

**作者:**Wael Issa, Nour Moustafa, Benjamin Turnbull, Zahir Tari.

**分享人:**河海大学——王礼育

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd7PdTwqxaMfpIS26krIsxls3gvlWl17nYzpFj5Zhtqcwy3z6MhbZh7hZmegdwno07C0icPN2GlR16gtHMFHOjswwUIO0ZHZRjKM/640?wx_fmt=png&from=appmsg#imgIndex=73)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***01.***

**研究背景**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

联邦学习（FL）凭借客户端本地保数据隐私的优势广泛应用，但开放性易遭投毒攻击，例如恶意客户端上传恶意梯度破坏全局模型。现有梯度聚合规则存在局限：依赖传统度量指标易被新型攻击规避、恶意客户端占比限制严格、固定阈值缺乏灵活性、部分违背隐私原则，难以适配复杂场景。为此，本文提出分层梯度净化（LGP）方案，有望实现更精准的恶意梯度识别与过滤。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***02.***

**关键技术**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

本文提出了一种鲁棒的梯度过滤方案，设计分层梯度净化（LGP）方法，在联邦学习全局聚合前过滤有害梯度。本文设计的LGP方案采用的关键技术如下：

1）MAD动态梯度修剪：先计算各层梯度的L2范数，以范数中位数与中位数绝对偏差（MAD）构建动态阈值区间，过滤超出区间的异常梯度。该技术摒弃固定阈值的僵化设计，自适应梯度分布特性，初步筛除明显恶意梯度，为后续精准识别奠定基础。

2）统计特征聚类：对修剪后的梯度按层分析，提取正负零计数、峰度、偏度、按层计算的欧氏距离、与全局梯度的绝对偏差等多维统计特征，全面刻画梯度内在属性。基于这些特征执行层次聚类（AHC），将梯度划分为两类集群，实现诚实与恶意梯度的分离。

3）多维度无辜准则筛选：构建融合四大核心指标的无辜准则，即集群内客户端信誉分数总和、梯度多样性、稳定性、与全局梯度的一致性，综合判定诚实集群。该技术摆脱传统距离、相似度度量的依赖，有效应对新型模仿攻击，提升复杂场景下恶意梯度识别的精度与可靠性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***03.***

**算法介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

![](https://mmbiz.qpic.cn/mmbiz_gif/M82cWMKlQSUJjXpd6Uib1r9IuyZQJJPWVo2lY1bxf9icgUyU4ZY8N7xMbQ3qeoCSBBTAicXm1ogAlbpHmKiaRD2nxtlo34Wvu0qlFiaal588qvBM/640?wx_fmt=gif&from=appmsg)

LGP算法以层级别梯度净化为核心，图1展示了其完整工作流程。该算法主要包含两大核心模块：基于中位数绝对偏差（MAD）的范数过滤算法，以及基于层次聚类（AHC）的统计特征聚类算法。其中，前者通过动态阈值筛选，高效过滤超出正常分布范围的极端恶意梯度，初步筛选出诚实客户端的候选集合；后者则针对候选集合中可能潜藏的、伪装性较强的攻击者，通过提取多维统计特征并执行聚类分析。为突破传统方案对恶意客户端占比的强假设局限，本文还创新性地提出无辜准则，通过多维度指标综合评判集群属性，最终实现诚实簇与恶意簇的精准辨认，保障梯度聚合的安全性与可靠性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp0icSa0dRTjn7nGlIYicFqNoXPwbibqTNuYHuEjpERsw4U9msH9ibVSE3MrJFeEkWhvnJQ24tOPGL8xVk8ia5WaibZxFqA9DbGicrhT3I/640?wx_fmt=png&from=appmsg)

图1. LGP算法流程

**A. 基于MAD的范数过滤算法**

中位数绝对偏差（MAD）是一种具备强稳健性的离散程度度量指标，核心用于量化数据点相对于数据中心即中位数的绝对偏离程度。与均值、标准差等传统离散度量指标不同，MAD的计算以中位数为核心基准，先求解所有数据点与中位数的绝对差值，再取该组绝对差值的中位数作为最终结果，这一特性使其对异常值的敏感度显著降低，即便数据中存在极端偏离的异常样本，也不会大幅扭曲对整体数据分布离散程度的判断，能够更稳定、客观地刻画数据的正常分布范围。考虑到FL中恶意客户端上传的极端恶意梯度（如随机攻击、Min-Max攻击产生的梯度）属于典型异常值，而传统固定阈值或基于标准差的过滤方法易受此类异常值干扰，导致阈值失真、过滤失效。MAD凭借其抗异常值干扰的优势，能够自适应梯度的层间分布特性，对每层梯度的L2范数独立计算 MAD，结合范数中位数构建动态阈值区间，既无需人工预设阈值参数，又能精准圈定正常梯度的分布范围，高效过滤超出该区间的极端恶意梯度，为后续统计特征聚类与诚实集群筛选奠定可靠的候选基础，同时保留潜在的、伪装性较强的梯度样本供进一步甄别。

服务器接收所有客户端的梯度G\_r={g\_1,g\_2,…,g\_M}，按模型层结构拆分梯度，得到每层的梯度集合G\_r,l（l为层索引，如CNN的卷积层、全连接层）。然后对每层梯度G\_r,l执行修剪，筛选潜在诚实梯度，过滤异常梯度，具体流程如下：

1）计算每层中每个梯度的L\_2范数（量化梯度幅度）：

![](https://mmbiz.qpic.cn/mmbiz_png/jBQAokCLibp2dMZr26qfAiau0xgdMnkKblzbEUtMvHDDG8VCa2dX5OhrxdWUuRGMWttun6QSeehokUYaUlUOiaku1SgC3NqGR9q9VSOe7ibKXjc/640?wx_fmt=png&from=appmsg)

2）计算范数的中位数绝对偏差：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp0MWK2pkByZk5UZSYVKH7XEAFAicz4hgMIK1SnIKe5NqbwsXW19HBThM63HuaP0ZmNHGOVBTkpjr6XWmsia0lKlvK1b1v9qwRydc/640?wx_fmt=png&from=appmsg)

3）构建动态阈值区间：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2ZBUeicVSkeRsj4ZLcicNlvSDg2RWmueLK1Ynd26OEp0HFGe5AdqhUJ8Rs8VcAm6PLvNLIjsmFwBAibryNGwCMxqYmYMw5nZPPRc/640?wx_fmt=png&from=appmsg)

4）过滤梯度：保留norm\_l[m]落在区间内的梯度，得到每层的过滤后梯度集合G\_f^l及对应的客户端索引I\_f^l，剔除超出区间的明显恶意梯度。

**B. 基于AHC的统计特征聚类算法**

聚类之前对每层过滤后的梯度G\_f^l，逐客户端提取多维度统计特征，以更全面地刻画客户端梯度特性。

1）基础计数特征：梯度中正数个数（PC）、负数个数（NC）、零值个数（ZC）。

2）分布特征：梯度的峰值、偏度。

3）关联性特征：与其他客户端梯度的对应层的欧氏距离均值（D\_mean）、与上一轮全局平均梯度G\_avg,l的绝对偏差（Dev\_mean）。

4）方向特征：通过点积计算与G\_avg,l的梯度方向的一致性。

服务器将提取到的所有特征整合成特征向量，形成每层的特征矩阵features\_all^l。然后对每层的特征矩阵features\_all^l执行层次聚类(AHC)。AHC作为自下而上的聚合型聚类方法，核心优势在于无需预先指定簇的数量或簇中心，能完全依据数据自身的相似性结构自然形成合理分组，完美适配层级别梯度特征的复杂分布特性，既避免了预设簇参数带来的适配偏差，又能精准捕捉梯度特征间的内在关联。基于AHC的统计特征聚类具体流程如下：

1）初始化簇结构：将每层特征矩阵features\_all^l中的每个客户端特征向量，均视为一个独立的初始簇，确保每个样本的个体特征不被初始假设掩盖。

2）簇间合并迭代：以欧氏距离作为特征向量间的相似度度量（距离越小相似度越高），采用平均链接法计算簇间距离（取两簇内所有样本两两欧氏距离的均值），迭代找出当前相似度最高的一对簇进行合并，更新簇结构并重复该过程。

3）聚类终止与输出：持续迭代合并直至簇的数量减少为2个（cluster\_1^l和cluster\_2^l），强制聚类终止，得到分别对应潜在诚实集群与恶意集群的聚类结果。

4）关联集群与客户端索引，得到每层两个集群的梯度集合G\_c1^l、G\_c2^l及客户端索引I\_c1^l、I\_c2^l。

这种贴合层级别分析逻辑的聚类方式，既充分考虑了不同层梯度的分布差异，又能输出结构清晰的聚类结果，为后续通过无辜准则精准甄别诚实簇、剔除恶意簇奠定了坚实基础。

**C. 无辜准则**

通过层次聚类（AHC）可将客户端梯度划分为两类集群，但仅靠聚类结果无法直接判定哪一集群为诚实簇。传统方案往往依赖恶意客户端占比不超过一半的强假设，简单将规模更大的集群标记为诚实簇，难以适配高比例恶意客户端场景。为此，本文提出一种新颖的无辜准则，通过多维度指标综合评判集群属性，实现诚实簇与恶意簇的精准辨认，突破了传统方案对恶意客户端占比的局限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp2pLgiazXMaAXWb7Dlcbxc6nwZWMKV6Zx0ysrVweatRic3KYlkulLwjlMk3S7UR3Ts2K51iauqCyucexNb7jR7AHr6DdXl5OLwPxM/640?wx_fmt=png&from=appmsg)

图2. 无辜准则的判定流程

基于如图所示的无辜准则，从每层的两个集群中筛选出诚实集群C\_honest^l：

1）计算每个集群的四大核心指标：信誉分数（RS），即集群内客户端信誉分数总和；梯度多样性，即集群内梯度各层欧式距离均值（D\_mean），诚实客户端梯度因数据、模型特性存在合理差异，多样性较高，而恶意客户端梯度可能因协同攻击呈现同质化，多样性偏低；稳定性，集群内梯度标准差均值（SD\_mean），诚实梯度的数值分布相对平稳，稳定性指标更优；一致性，集群内所有客户端梯度与上一轮全局梯度G\_avg,l的绝对偏差均值（Dev\_mean），诚实梯度通常与全局优化方向一致，偏差更小，恶意梯度则可能偏离全局方向，偏差更大。

2）执行筛选原则：基于上述四大指标，按以下规则逐步判定诚实集群，优先满足高优先级条件，不满则向下匹配。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jBQAokCLibp3CiaH4qmqd0JKWSzosF5Xluicrm48r1icDvafrJ2FqjdZPtoqT616AVJySiaRJMXMQ6StMXf29ics5ZczbM6yEEldMPz1OseT7Emf0/640?wx_fmt=png&from=appmsg)

高优先级条件如上述第一个公式，集群c\_2同时满足梯度多样性D\_mean更高、稳定性SD\_mean更优、与全局梯度一致性Dev\_mean更强、信誉分数RS\_cluster更高，则直接判定其为诚实集群。若集群未满足高优先级条件，但是满足梯度与全局梯度一致性Dev\_mean更强、信誉分数RS\_cluster更高、多样性较低（可能因为数据分布集中），则仍判定其为诚实集群，适配部分场景下诚实梯度多样性偏低的情况。若c\_2未满足上述两种条件，则默认c\_1为诚实集群。

通过无辜准则的判定，服务器获得诚实集群的集合，此时对诚实集群的客户端的信誉分数进行更新RS+1。以此建立一个长期的信任记录，使得这些被选中的参与者在后续通信轮次的筛选步骤中获得优先地位。基于上述三个流程，服务器实现了对客户端模型的筛查，最终对诚实客户端的模型进行聚合，得到新一轮的全局模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oWag3KdTBd74MTR6QwdQ2MWrdOjiacNKvy0ia4x2JibzxL9C6oCKicaz9I9SCopibesl0RhZMPnl9CH7EQ2mBLENUpLLSbTRdhwGn70ePAVwojlE/640?wx_fmt=png&from=appmsg#imgIndex=62)

***04.***

**实验结果分析**

![](https://mmbiz.qpic.cn/mmbiz_png/oWag3KdTBd6I3RLBtIv7ljVoueDNafLdSBAiaWUDia0LOYdATRyyyThW6dPFfymuS1EjmDsUrIJTmwnIMXQC2mU4jPqib8BFakpA1bYy3cUnCQ/640?wx_fmt=png&from=appmsg#imgIndex=63)

实验设置：FL系统总客户端数量设定为50个，恶意客户端占比涵盖 10%~50%；全局训练轮次为100轮，客户端本地批量大小固定为50，学习率η默认设为0.1，数据分布同时支持IID与非IID两种场景。实验选取四类典型数据集，覆盖图像分类、文本分类、IoT入侵检测三大任务场景，适配不同类型的深度学习模型，确保实验结果的通用性。实验还选取了9类主流联邦学习投毒攻击，涵盖不同攻击策略与隐蔽性等级，全面测试L...