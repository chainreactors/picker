---
title: LayerNorm与Softmax的online化与并行化
url: https://blog.csdn.net/ariesjzj/article/details/144321133
source: 世事难料，保持低调
date: 2024-12-09
fetch_date: 2025-10-06T19:35:47.286797
---

# LayerNorm与Softmax的online化与并行化

# LayerNorm与Softmax的online化与并行化

最新推荐文章于 2025-08-21 11:25:02 发布

原创
最新推荐文章于 2025-08-21 11:25:02 发布
·
1.5k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

23

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

27
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#LayerNorm](https://so.csdn.net/so/search/s.do?q=LayerNorm&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#Softmax](https://so.csdn.net/so/search/s.do?q=Softmax&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#GPU](https://so.csdn.net/so/search/s.do?q=GPU&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#并行计算](https://so.csdn.net/so/search/s.do?q=%E5%B9%B6%E8%A1%8C%E8%AE%A1%E7%AE%97&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#Online](https://so.csdn.net/so/search/s.do?q=Online&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#CUDA](https://so.csdn.net/so/search/s.do?q=CUDA&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756916.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

AI
专栏收录该内容](https://blog.csdn.net/ariesjzj/category_1243833.html "AI")

43 篇文章

订阅专栏

现代神经网络中有不少算子需要先做归约（reduction），再基于reduction的结果来对每个元素进行处理。这类算子会带来一些问题，如：

* 难以并行计算：原始的语义是序列化的，难以在GPU这样的并行计算硬件上加速。
* Overflow风险：如果是累加的话，当元素多或者元素大时，可能会超过浮点表示范围。

接下来以深度学习中常见的Softmax与LayerNorm算子为例看看这些问题在业界是如何被解决的。

### Softmax

Softmax在深度神经网络中应用广泛，像计算logits，Transformer中的Attention，或是MoE中的门控中都有用到。先来看其数学定义：
yi=exi∑j=1Vexj
y\_i = \frac{e^{x\_i}}{\sum\_{j=1}^{V} e^{x\_j}}
yi​=∑j=1V​exj​exi​​
其中x,y∈RVx, y \in \mathbb{R}^Vx,y∈RV。

按定义进行计算的Naive softmax是个2-pass算法。即先遍历所有元素做一次reduction操作求出分母（即normalization term），再遍历一遍元素计算每个yiy\_iyi​。

但由于计算机的浮点精度表示范围有限，现实当中，这种累加非常容易overflow。为了数值稳定性，通常会让每个数减去最大值。
yi=exi−max⁡k=1Vxk∑j=1Vexj−max⁡k=1Vxk
y\_i = \frac{e^{x\_i - \max\_{k=1}^V x\_k}} {\sum\_{j=1}^V e^{x\_j - \max\_{k=1}^V x\_k}}
yi​=∑j=1V​exj​−maxk=1V​xk​exi​−maxk=1V​xk​​
由于分子与分母中的e−max⁡k=1Vxke^{-\max^{V}\_{k=1} x\_k}e−maxk=1V​xk​一项可以被提出并被约掉，因此这样的改动不会影响最终结果。另外由于每个元素减去最大值，使得求和中的每一项不会超过1，这样和就不容易overflow。这种算法称为safe softmax。但是，代价是原算法成了3-pass算法，因为求最大值本身也是个reduction操作。

这三个pass，前两个pass是为了得到maximum value与normalization term。2018年来自Nvidia的论文《Online normalizer calculation for softmax》（也就是后来大名鼎鼎的Flash Attention的基石）将前两个pass合成一个。在合成的这个pass中，以online的方式计算：
mj=max⁡(mj−1,xj)dj=dj−1emj−1−mj+exj−mj
\begin{align\*}
m\_j & = \max(m\_{j-1}, x\_j) \\
d\_j & = d\_{j-1} e^{m\_{j-1} - m\_j} + e^{x\_j - m\_j}
\end{align\*}
mj​dj​​=max(mj−1​,xj​)=dj−1​emj−1​−mj​+exj​−mj​​
第二次遍历后用下面公式计算所有值：
yi=exi−mVdV
y\_i = \frac{e^{x\_i} - m\_V}{d\_V}
yi​=dV​exi​−mV​​
这样，在解决了overflow问题的基础上，还没增加pass数量。但这是一个序列化的计算过程，难以被GPU加速。为了能够被GPU加速，还需要将算法并行化。上面的算法可被写成：
[mVdV]=[x11]⊗[x21]⊗⋯⊗[xV1]
\left[ \begin{array}{cc} m\_V \\ d\_V \end{array} \right] = \left[ \begin{array}{cc} x\_1 \\ 1 \end{array} \right] \otimes \left[ \begin{array}{cc} x\_2 \\ 1 \end{array} \right] \otimes \cdots \otimes \left[ \begin{array}{cc} x\_V \\ 1 \end{array} \right]
[mV​dV​​]=[x1​1​]⊗[x2​1​]⊗⋯⊗[xV​1​]
其中⊗\otimes⊗定义为：
[midi]⊗[mjdj]=[max⁡(mi,mj)di×emi−max⁡(mi,mj)+dj×emj−max⁡(mi,mj)]
\left[ \begin{array}{cc} m\_i \\ d\_i \end{array} \right] \otimes \left[ \begin{array}{cc} m\_j \\ d\_j \end{array} \right] = \left[ \begin{array}{cc} \max(m\_i, m\_j) \\ d\_i \times e^{m\_i - \max(m\_i, m\_j)} + d\_j \times e^{m\_j - \max(m\_i, m\_j)} \end{array} \right]
[mi​di​​]⊗[mj​dj​​]=[max(mi​,mj​)di​×emi​−max(mi​,mj​)+dj​×emj​−max(mi​,mj​)​]
它满足结合律。这意味着我们可以把它切分成多块，分别交给不同的计算单元计算，然后将它们的结果进行下一轮进行计算，直到得到最终结果。这样就给Flash Attention中对GEMM+softmax+GEMM进行tiling打下了理论基础。

下面看代码。这是官方实现：https://github.com/NVIDIA/online-softmax。先看调用的地方：

```
online_softmax<256><<<batch_size,256>>>(x, y, V);
```

输入为bs×Vbs \times Vbs×V的矩阵，需要对每一行进行softmax。Thread block个数为bsbsbs，每个thread block包含256个线程，负责处理一行 。

```
struct __align__(8) MD
{
    float m;
    float d;
};

__device__ __forceinline__ MD reduce_md_op(MD a, MD b)
{
    bool a_bigger = (a.m > b.m);
    MD bigger_m = a_bigger ? a : b;
    MD smaller_m = a_bigger ? b : a;
    MD res;
    res.d = bigger_m.d + smaller_m.d * __expf(smaller_m.m - bigger_m.m);
    res.m = bigger_m.m;
    return res;
}

template<int THREADBLOCK_SIZE>
__launch_bounds__(THREADBLOCK_SIZE)
__global__ void online_softmax(
    const float * __restrict x,
    float * __restrict y,
    int V)
{
    int thread_id = threadIdx.x;
    int vector_id = blockIdx.x;

    // reposition x and y to data for the current vector
    x += vector_id * V;
    y += vector_id * V;

    typedef cub::BlockReduce<MD, THREADBLOCK_SIZE> BlockReduce;

    __shared__ typename BlockReduce::TempStorage temp_storage;
    __shared__ MD md_total;

    MD md_partial;
    md_partial.m = -FLT_MAX;
    md_partial.d = 0.0F;
    for(int elem_id = thread_id; elem_id < V; elem_id += THREADBLOCK_SIZE)
    {
        MD new_elem;
        new_elem.m = x[elem_id];
        new_elem.d = 1.0F;
        md_partial = reduce_md_op(md_partial, new_elem);
    }

    MD md = BlockReduce(temp_storage).Reduce(md_partial, reduce_md_op);
    if (thread_id == 0)
        md_total = md;
    __syncthreads();

    float d_total_inverse = __fdividef(1.0F, md_total.d);
    for(int elem_id = thread_id; elem_id < V; elem_id += THREADBLOCK_SIZE)
        y[elem_id] = __expf(x[elem_id] - md_total.m) * d_total_inverse;
}
```

结构体`MD`包含`m`与`d`两个统计量，一个是maximum value，另一个是normalization term。`reduce_md_op()`函数为论文Algorithm 3的line 4,5。首先，每个线程把自己要做的先做完，然后用了cub这个库的`BlockReduce`进行跨block的reduce。最终的`m`与`d`放在shard memory中。这个过程如图：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/674f4af0cb9a40329b449626113f5cce.jpeg#pic_center)

### LayerNorm

LayerNorm（LN）在论文中《Layer Normalization》中提出。相比在视觉类模型中广泛应用的BatchNorm（BN），它更适用于语言类模型。像Transformer中就有它的身影。RMSNorm是它的简化变体。

LayerNorm的的数学定义如下：
y=x−E[x]V[x]+ϵγ+β
y = \frac{x - E[x]}{\sqrt{V[x] + \epsilon}} \gamma + \beta
y=V[x]+ϵ​x−E[x]​γ+β
计算过程中需要对所有元素做reduction操作求均值与方差。对于给定的样本，均值与方差可以用下面公式计算：
μn=1n∑i=1nxiσn2=1n−1∑i=1n(xi−μn)2
\begin{align\*}
\mu\_n & = \frac{1}{n} \sum\_{i=1}^{n} x\_i \\
\sigma^2\_n & = \frac{1}{n - 1} \sum\_{i=1}^n (x\_i - \mu\_n)^2
\end{align\*}
μn​σn2​​=n1​i=1∑n​xi​=n−11​i=1∑n​(xi​−μn​)2​
显然，如果直接按定义来算，需要将数据过遍历两遍，分别计算均值与方差。这不只是影响效率，就像前面提到的，还有数值稳定性问题。这里累加元素是平方，容易导致overflow。

要将之改成1-pass算法倒还比较容易，可以用概率统计中常用的公式：
V(X)=E[(X−μ)2]=E(X2)−E(X)2
V(X) = E[(X - \mu)^2] = E(X^2) - E(X)^2
V(X)=E[(X−μ)2]=E(X2)−E(X)2
但这样仍然有数据稳定性问题。不仅容易overflow，而且还可能有catastrophic cancellation问题（两个接近的浮点数相减可能导致很大的相对误差）。

于是就引出了Welford算法。它由B. P. Welford在1962年的论文《Note on a method for calculating corrected sums of squares and products. Technometrics》中提出。另初始M1=x1M\_1 = x\_1M1​=x1​，S1=0S\_1 = 0S1​=0，则有：
Mk=Mk−1+(xk−Mk−1)/kSk=Sk−1+(xk−Mk−1)(xk−Mk)
\begin{align\*}
M\_k & = M\_{k-1} + (x\_k - M\_{k - 1}) / k \\
S\_k & = S\_{k-1} + (x\_k - M\_{k - 1}) (x\_k - M\_k)
\end{align\*}
Mk​Sk​​=Mk−1​+(xk​−Mk−1​)/k=Sk−1​+(xk​−Mk−1​)(xk​−Mk​)​
它维护在第`k`个样本到来时的均值估计MkM\_kMk​，用于更新二阶统计量SkS\_kSk​。基于它可以得到方差的估计。

这样，就把方差的计算online化了。它不仅是1-pass算法，而且数值稳定性还好。看起来很不错，要是能被GPU并行起来就更好了。于是，1979年Tony F. Chan等人的论文《Updating Formulae and a Pairwise Algorithm for Computing Sample Variances》提出了计算方差的并行算法。设样本数量为n，如果将之分为[1,m]和[m+1,n]两个部分，则有：
S1,m+n=S1,m+Sm+1,m+n+mn(m+1)(m+nmT1,m−T1,n+m)2
S\_{1,m+n} = S\_{1,m} + S\_{m+1,m+n} + \frac{m}{n(m+1)} (\frac{m+n}{m} T\_{1,m} - T\_{1,n+m})^2
S1,m+n​=S1,m​+Sm+1,m+n​+n(m+1)m​(mm+n​T1,m​−T1,n+m​)2
其中T1,m=∑i=1mxiT\_{1,m} = \sum\_{i=1}^m x\_iT1,m​=∑i=1m​xi​。这意味着我们可以将一段数据分成两段，交给不同的计算单元分别计算，然后放在一起修正更新。

接下来看下代码。这里主要参考apex中的实现：https://github.com/NVIDIA/apex/blob/master/csrc/layer\_norm\_cuda\_kernel.cu。对于LayerNorm算子，在GPU上，`cuda_layer_norm()`函数会调用`HostApplyLayerNorm()`函数，继而调用C...