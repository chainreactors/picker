---
title: LLM Serving中的排队论（Queueing Theory）
url: https://blog.csdn.net/ariesjzj/article/details/150994691
source: 世事难料，保持低调
date: 2025-09-01
fetch_date: 2025-10-02T19:28:37.398003
---

# LLM Serving中的排队论（Queueing Theory）

# LLM Serving中的排队论（Queueing Theory）

最新推荐文章于 2025-10-01 20:42:40 发布

原创
最新推荐文章于 2025-10-01 20:42:40 发布
·
864 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

12

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

14
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#机器学习](https://so.csdn.net/so/search/s.do?q=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#概率论](https://so.csdn.net/so/search/s.do?q=%E6%A6%82%E7%8E%87%E8%AE%BA&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#LLM](https://so.csdn.net/so/search/s.do?q=LLM&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#排队论](https://so.csdn.net/so/search/s.do?q=%E6%8E%92%E9%98%9F%E8%AE%BA&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#Queueing Theory](https://so.csdn.net/so/search/s.do?q=Queueing+Theory&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756916.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

AI
专栏收录该内容](https://blog.csdn.net/ariesjzj/category_1243833.html "AI")

43 篇文章

订阅专栏

排队论（Queueing theory）是研究排队系统，或称随机服务系统的科学。它是运筹学的一个分支。现实中有很多应用，如银行、公交车、咖啡店、游乐场、高速公路和电话热线等等。

具体的理论可以参阅相关的资料。这里只提一下基础概念和符号。首先由于现实中的排队系统有很多变体。对应地，排队论也有对应的抽象模型。模型的命名一般采用Kendall命名法（由英国数学家Kendall于1953年提出），即`X/Y/Z/A/B/C`的形式。其中A表示到达时间间隔分布，B表示服务时间分布，X表示服务员数，Y表示系统容量，Z表示排队规则。比如`M/M/1`代表到达时间和服务时间分布都符合泊松分布，服务员为1个。`M/D/1`代表服务时间是常量。`M/G/c`代表服务时间为一般概率分布，服务员数有c个。这里A和B中的字母M代表泊松（Poisson）分布。它是排队论中最为常用的分布之一，其PDF(Probability distribution function)为：
P(X=k)=e−λλkk!
P(X=k) = e^{-\lambda }\frac{\lambda^k}{k!}
P(X=k)=e−λk!λk​
其中kkk为自然数。它的均值和方差均为λ\lambdaλ。该分布用于描述在固定时间间隔内某事件发生次数。它的优点在于一方面很多时候能较好地近似现实情况，另一方面有很好的性质。

与它密切相关的另一个分布是指数分布。其PDF为：
P(X=t)=λe−λt
P(X=t) = \lambda e ^{-\lambda t}
P(X=t)=λe−λt
其中λ\lambdaλ的含义为单位时间发生该事件的次数。其期望与方差分别为1λ\frac{1}{\lambda}λ1​和1λ2\frac{1}{\lambda^2}λ21​。指数分布具有无记忆性，且是唯一具有该性质的分布。无记忆性表示事件发生之前的剩余等待时间与已经等待的时间无关。当事件间隔服从指数分布，那单位时间内事件发生的分布为泊松分布。

泊松过程是在任一区间内，到达用户数服从泊松分布的随机过程。泊松过程具有一些有趣的性质，如：

* 泊松过程具有平稳增量性，即一个给定的时间区间内的发生的事件数的分布仅与该区间的长度有关，与区间的绝对位置无关。
* 泊松过程有均匀分布的性质，可推导出称为Poisson arrivals see time averages（即PASTA）的性质。即任意按泊松过程到达系统的顾客看到系统中的随机过程处于某个状态的概率与系统外部的观测者在任意时间点到的处于该状态的概率是相同的。

排队论中的常用符号：

* λ\lambdaλ表示平均到达速率。
* SSS表示服务时间的随机变量。其期望的倒数μ\muμ为平均服务速率。
* r=λμr=\frac{\lambda}{\mu}r=μλ​为输入负荷，ρ=λcμ\rho=\frac{\lambda}{c\mu}ρ=cμλ​为流量强度，其中ccc为服务员数。前者为忙碌服务员的平均数，后者为每个服务员都处于忙碌状态的时间占比。

在一个排队系统中，我们会关注一些量，比如：

* LLL和LqL\_qLq​：分别表示系统中顾客的平均数，与等待队列中顾客的平均数。它们之间有关系L=Lq+rL=L\_q + rL=Lq​+r。
* WWW和WqW\_qWq​：分别表示单个顾客在系统中花费的平均时间（sojourn time），与在等待队列中花费的平均时间。它们有关系W=Wq+E[S]=Wq+1μW = W\_q + \mathbb{E}[S] = W\_q + \frac{1}{\mu}W=Wq​+E[S]=Wq​+μ1​。

Little’s law是排队论中最重要的基础定律之一，即L=λWL=\lambda WL=λW，Lq=λWqL\_q=\lambda W\_qLq​=λWq​。它揭示了三个关键量的关系。

对于效益指标，我们关心其在稳定状态下的情况。要使稳态存在，需要traffic intensity ρ<1\rho < 1ρ<1。直觉上，即顾客到来的平均速率得严格小于系统的平均服务速率。否则，服务系统无法承载需求，如果顾客不会退出，则随着时间的推移，队列迟早会爆。

近年来LLM的广泛研究与应用使得LLM serving有了更高的需求。那排队论是否可有助于LLM serving的分析与研究呢？首先来看LLM的特点会给排队论的应用带来一些什么挑战：

* 推理普遍用GPU这样的加速器进行计算。而对于GPU来说，多个request放在一个batch中是可以提高计算密度，进而提升吞吐的。因此，实际中我们一般都会将request组成batch来计算。且吞吐相对于batch的函数通常并不是线性的。
* Auto-regressive的生成方式是LLM相对于传统的DNN所特有的。传统的DNN（如视觉网络）大多都是无论输入是什么计算量是一定的。而LLM是逐个输出token，且不到最后不知道输出多少token。有些网络还会根据输入来调节要计算的部分，导致不同输入的计算量也不同。
* LLM通常会引入一些复杂的调度机制，如dynamic batching，continuous batching, chunked prefill，preemption，PD disaggregation等，它们使得对服务系统的建模更加复杂。

2025年论文《Queueing, Predictions, and LLMs: Challenges and Open Problems》讨论了LLM与传统queueing system的关系与挑战。其中3.4节讨论了LLM Serving系统与标准和queueing system的区别，提到KV cache，preemption multi-stage processing等。如果涉及到复杂场景，如speculative decoding，RAG，reasoning等，那就更挑战了。很多目前都还是开放问题。

这几年业界有一些论文在推理服务的分析与优化中也用到了排队论，如：

* 2023年论文《AlpaServe: Statistical Multiplexing with Model Parallelism for Deep Learning Serving》中使用`M/D/1`模型分析了多模型场景。
* 2024年论文《DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving》使用`M/D/1`排列模型研究PD disaggration场景中的prefill-only instance。
* 2025年论文《BestServe: Serving Strategies with Optimal Goodput in Collocation and Disaggregation Architectures》用tandem queue对PD disaggreation架构建模。

还有一些论文研究了如何用排队论更好地对LLM推理进行建模。如：

* 2021年的论文《Queueing Analysis of GPU-Based Inference Servers with Dynamic Batching: A Closed-Form Characterization》

该文用排队模型对基于GPU的dynamic batching推理服务进行建模。GPU有个特点是batch越大其吞吐越高（当饱和时便不再增大）。虽然排队论中也有对batch处理的研究（称为balk service），但它们大多假设处理时间与batch size无关。显然这样的假设对GPU是不适合的。还有些工作虽然假设batch-service队列的处理时间与batch size相关，但需要使用数值方法，无法得到closed-form形式。

文中假设maximum batch size无穷大且batch processing time是batch size的线性函数，表示为：
τ[b]=αb+τ0
\tau^{[b]} = \alpha b + \tau\_0
τ[b]=αb+τ0​
并证明了在此假设下可以推导出mean queueing delay的closed-form上界。首先，文中在Lemma 2中给出了mean latency：
E[W]=E[B2]−E[B]2λE[B]+E[H^]
\mathbb{E}[W] = \frac{\mathbb{E}[B^2] - \mathbb{E}[B]}{2\lambda \mathbb{E}[B]} + \mathbb{E}[\hat{H}]
E[W]=2λE[B]E[B2]−E[B]​+E[H^]
其中λ\lambdaλ为输入速率；BBB为服从BnB\_nBn​的stationary distribution的随机变量，而BnB\_nBn​为第nnn个batch结束时正在等待的inference job数量；H^\hat{H}H^为随机选取一个inference job的处理时间的随机变量。

然后在Theorem 2中给出了mean latency的上界，表示为：
min⁡(ϕ0(λ,α,τ0),ϕ1(λ,α,τ0))
\min (\phi\_0(\lambda, \alpha, \tau\_0), \phi\_1(\lambda, \alpha, \tau\_0))
min(ϕ0​(λ,α,τ0​),ϕ1​(λ,α,τ0​))
其中
ϕ0(λ,α,τ0)=α+τ02(1−λα)(1+2λτ0+1−λτ01+λα)ϕ1(λ,α,τ0)=32⋅τ01−λα+α2⋅λα+21−λ2α2
\begin{align\*}
\phi\_0(\lambda, \alpha, \tau\_0) &= \frac{\alpha + \tau\_0}{2(1 - \lambda \alpha)} (1 + 2\lambda \tau\_0 + \frac{1-\lambda \tau\_0}{1 + \lambda \alpha}) \\
\phi\_1(\lambda, \alpha, \tau\_0) &= \frac{3}{2} \cdot \frac{\tau\_0}{1- \lambda \alpha} + \frac{\alpha}{2} \cdot \frac{\lambda \alpha + 2}{1 - \lambda^2 \alpha^2}
\end{align\*}
ϕ0​(λ,α,τ0​)ϕ1​(λ,α,τ0​)​=2(1−λα)α+τ0​​(1+2λτ0​+1+λα1−λτ0​​)=23​⋅1−λατ0​​+2α​⋅1−λ2α2λα+2​​
且当λ≤1α+τ0\lambda \leq \frac{1}{\alpha + \tau\_0}λ≤α+τ0​1​时有ϕ0(λ,α,τ0)≤ϕ1(λ,α,τ0)\phi\_0(\lambda, \alpha, \tau\_0) \leq \phi\_1(\lambda, \alpha, \tau\_0)ϕ0​(λ,α,τ0​)≤ϕ1​(λ,α,τ0​)。

* 2024年论文《A Queueing Theoretic Perspective on Low-Latency LLM Inference with Variable Token Length》

前面的论文用`M/D/1`建模，比较适用于DNN场景。但是对于LLM，由于其输出长度是不确定的，因此在batch size一定的情况下其处理时间也是不确定的。该文研究了LLM场景下的queueing delay。它考虑了max-token clipping和batch inference，并得出结论：添加output token的最大限制可以极大地减少queueing delay。

对于batch inference，它将service过程建模为bulk queue。Batch processing time受batch size和batch内最大token size的影响。文中采用`M/G/1`建模，意味着不对服务时间分布做特定假设。该模型下，由排队论中的PK（Pollaczek-Khintchine）公式：
Lq=λ2σ2+ρ22(1−ρ)
L\_q = \frac{\lambda^2 \sigma^2 + \rho ^2}{2(1 - \rho)}
Lq​=2(1−ρ)λ2σ2+ρ2​
和指标间关系
L=Lq+ρLq=λWqW=Wq+1μ
\begin{align\*}
L &= L\_q + \rho \\
L\_q &= \lambda W\_q \\
W &= W\_q + \frac{1}{\mu}
\end{align\*}
LLq​W​=Lq​+ρ=λWq​=Wq​+μ1​​
可推导出几个关键量的表达式。根据《Fundamentals of Queuing Theory》一书第五版第六章中表6.1，该模型中mean queuing delay（即队列中平均等待时间）可表示为：
Wq=λE[S2]2(1−ρ)
W\_q = \frac{\lambda \mathbb{E}[S^2]}{2(1-\rho)}
Wq​=2(1−ρ)λE[S2]​
文中根据推理延迟可用S=an+cS=an+cS=an+c近似的观察，将上式中的E[S2]\mathbb{E}[S^2]E[S2]写成：
E[S2]=E2[S]+a2(E[nreq2]−E2[nreq])
\mathbb{E}[S^2] = \mathbb{E}^2[S] + a^2 (\mathbb{E}[n^2\_{req}] - \mathbb{E}^2[n\_{req}])
E[S2]=E2[S]+a2(E[nreq2​]−E2[nreq​])
其中nreqn\_{req}nreq​为代表output token数量的随机变量。在有max token limit的场景下（即模型最多吐nmaxn\_{max}nmax​个token），它的期望是nmaxn\_{max}nmax​的函数。

另外，它基于前一篇paper中关于mean queueing delay上界的结论，扩展到LLM推理中的多种batching方式。在前文中将推理时间表达成batch size的线性函数：
H[b]=αb+β
H^{[b]} = \alpha b + \beta
H[b]=αb+β
上界是其中系数α\alphaα与β\betaβ的函数。因此扩展到几种batching方式主要就需要得到这两个系数。该文将之拓展，考虑了三种batching方式：

1. Fixed batching（即static batching）
   H[b]=k1b+k2+k3bE[L]+k4E[L]
   H^{[b]} = k\_1 b + k\_2 + k\_3 b \mathbb{E}[L] + k\_4 \mathbb{E}[L]
   H[b]=k1​b+k2​+k3​bE[L]+k4​E[L]
   LLL代表batch中max output token size的随机变量。
2. Dynamic batching
   H[b]=k1b+k2+k3m2b2b+1+k4m2bb+1≤(k1+k3m2)b+k2+k4...