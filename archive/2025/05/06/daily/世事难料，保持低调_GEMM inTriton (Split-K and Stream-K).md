---
title: GEMM inTriton (Split-K and Stream-K)
url: https://blog.csdn.net/ariesjzj/article/details/147597135
source: 世事难料，保持低调
date: 2025-05-06
fetch_date: 2025-10-06T22:25:20.359658
---

# GEMM inTriton (Split-K and Stream-K)

# GEMM inTriton (Split-K and Stream-K)

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[ariesjzj](https://jinzhuojun.blog.csdn.net "ariesjzj")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2025-05-05 13:18:02 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.3k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

22

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
22

CC 4.0 BY-SA版权

文章标签：
[GEMM](https://so.csdn.net/so/search/s.do?q=GEMM&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[Triton](https://so.csdn.net/so/search/s.do?q=Triton&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[Stream-K](https://so.csdn.net/so/search/s.do?q=Stream-K&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[Split-K](https://so.csdn.net/so/search/s.do?q=Split-K&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[CUDA](https://so.csdn.net/so/search/s.do?q=CUDA&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2025-05-05 13:17:42 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/jinzhuojun/article/details/147597135>

Triton是OpenAI的开源项目。官网https://openai.com/index/triton/。Github地址https://github.com/triton-lang/triton。自问世来，一直以来都受到业界关注，而且近年来热度似乎有了明显提升。可以看到将Triton用于LLM的例子越来越多。各种流行的LLM框架，如vLLM，SGLang和TRT-LLM中也都有了Triton的身影。PyTorch也对它进行了官方支持。在PyTorch中Triton可用于自定义算子的开发并方便地与`torch.compile`集成（https://pytorch.org/tutorials/recipes/torch\_compile\_user\_defined\_triton\_kernel\_tutorial.html）

它主要解决的是在并行加速芯片上写高性能算子的问题。像CUDA这样的编程接口易学难精。写个能工作的实现和写出具有SOTA性能的kernel所需的专业时间和工程精力差别巨大。Triton的定位就是以极小的工程代价能达到手写算子约八成的性能。正如同Python与C++，或者C++与汇编的关系。将来可能大多算子会用Triton开发，只有在那些性能瓶颈的算子才会用CUDA去开发。

对于大多数使用者而言，更关心的是如何使用Triton。一个官方hello world可见：https://triton-lang.org/main/getting-started/tutorials/01-vector-add.html。从中可以大概看到用Triton写一个kernel的基本范式与套路。Triton的DSL中有`program_id`的概念，对应CUDA中的CTA，也就是thread block。使用中很多时候以block为单位，这样就可以尽量少地纠缠于warp, thread等更细节的概念。

本文以最常见的计算GEMM为例，看下用Triton是如何实现它以及它的几种变体（Split-K，Stream-K）的。

### Classic GEMM

作为引子，首先看下经典的用tiling来做GEMM是如何在Triton中实现的。基本的写法可参见：https://triton-lang.org/main/getting-started/tutorials/03-matrix-multiplication.html。Kernel的CTA的个数就是输出矩阵中的tile数量。也就是说，每个CTA计算一个输出矩阵中的tile。它需要循环多次进行累加。循环次数为k维上的block数。

与CUDA有所不同的是，像这里的`offs_am`，`offs_bn`等描述的都是一个range，即下标数组。如果`BLOCK_SIZE_M`不能整除`M`的话，余数部分会从0开始。这一部分是冗余计算，最后会用mask过滤掉。整体代码比较易懂，不需要过多解释。这里稍微绕一些的可能用于L2 optimization的CTA id重映射。

```
pid = tl.program_id(axis=0)
num_pid_m = tl.cdiv(M, BLOCK_SIZE_M)
num_pid_n = tl.cdiv(N, BLOCK_SIZE_N)
num_pid_in_group = GROUP_SIZE_M * num_pid_n
group_id = pid // num_pid_in_group
first_pid_m = group_id * GROUP_SIZE_M
group_size_m = min(num_pid_m - first_pid_m, GROUP_SIZE_M)
pid_m = first_pid_m + ((pid % num_pid_in_group) % group_size_m)
pid_n = (pid % num_pid_in_group) // group_size_m
```

经过这个变换（M维度上的分块）后，按CTA id递增tile的顺序变成：
 ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ac3c3485caed443abf9d92118d779dbf.jpeg#pic_center)

### Split-K GEMM

源码可参考https://github.com/triton-lang/triton/blob/v2.1.0/python/triton/ops/matmul.py。首先是kernel启动部分：

```
# launch kernel
grid = lambda META: (
    cdiv(M, META["BLOCK_M"]) * cdiv(N, META["BLOCK_N"]),
    META["SPLIT_K"],
)
_kernel[grid](
```

这里grid为二维，第一个维度为output矩阵的tile数，即M维的block数 x N维的block数，第二个维度为Split-K中的K，即K维上分成几个partition。这些partition由不同的CTA计算并累加。

接下来就是kernel的定义：

```
@autotune(
    configs=[
        # basic configs for compute-bound matmuls
        Config(
            {"BLOCK_M": 128, "BLOCK_N": 256, "BLOCK_K": 32, "SPLIT_K": 1},
            num_stages=3,
            num_warps=8,
        ),
        ...
}
@heuristics(
    {
        "EVEN_K": lambda args: args["K"] % (args["BLOCK_K"] * args["SPLIT_K"]) == 0,
    }
)
@jit
def _kernel(...)
```

这里由`@jit`修饰的就是kernel函数的定义了。Kernel函数的参数分成几类：

* 调用者给的，如输入输出，维度信息这些。
* 可tuning参数，如block大小。它们与性能相关。可参见：https://triton-lang.org/main/python-api/generated/triton.autotune.html。
* 基于heuristics得到的参数，基于预定义规则得到。如`EVEN_K`代表K维上的元素能否被CTA平分。可参见：https://triton-lang.org/main/python-api/generated/triton.heuristics.html。

上面这个kernel实现可分为三个部分：

1. 根据`program_id`确定当前要处理的数据。

```
# matrix multiplication
pid = tl.program_id(0)
pid_z = tl.program_id(1)
grid_m = tl.cdiv(M, BLOCK_M)
grid_n = tl.cdiv(N, BLOCK_N)
# re-order program ID for better L2 performance
width = GROUP_M * grid_n
group_id = pid // width
group_size = min(grid_m - group_id * GROUP_M, GROUP_M)
pid_m = group_id * GROUP_M + (pid % group_size)
pid_n = (pid % width) // (group_size)
# do matrix multiplication
rm = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
rn = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
ram = tl.max_contiguous(tl.multiple_of(rm % M, BLOCK_M), BLOCK_M)
rbn = tl.max_contiguous(tl.multiple_of(rn % N, BLOCK_N), BLOCK_N)
rk = pid_z * BLOCK_K + tl.arange(0, BLOCK_K)
# pointers
A = A + (ram[:, None] * stride_am + rk[None, :] * stride_ak)
B = B + (rk[:, None] * stride_bk + rbn[None, :] * stride_bn)
```

其中以下几行：

```
rm = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
rn = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
ram = tl.max_contiguous(tl.multiple_of(rm % M, BLOCK_M), BLOCK_M)
rbn = tl.max_contiguous(tl.multiple_of(rn % N, BLOCK_N), BLOCK_N)
```

告诉编译器数据是align且连续的。这样编译器就可以做一些诸如vectorization的优化。

2. 对于每个输出中的tile，在K维上做进行累加。

```
acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=acc_dtype)
for k in range(0, tl.cdiv(K, BLOCK_K * SPLIT_K)):
    if EVEN_K:
        a = tl.load(A)
        b = tl.load(B)
    else:
        k_remaining = K - k * (BLOCK_K * SPLIT_K)
        _0 = tl.zeros((1, 1), dtype=C.dtype.element_ty)
        a = tl.load(A, mask=rk[None, :] < k_remaining, other=_0)
        b = tl.load(B, mask=rk[:, None] < k_remaining, other=_0)
    if AB_DTYPE is not None:
        a = a.to(AB_DTYPE)
        b = b.to(AB_DTYPE)
    if fp8_fast_accum:
        acc = tl.dot(
            a, b, acc, out_dtype=acc_dtype, input_precision=input_precision
        )
    else:
        acc += tl.dot(a, b, out_dtype=acc_dtype, input_precision=input_precision)
    A += BLOCK_K * SPLIT_K * stride_ak
    B += BLOCK_K * SPLIT_K * stride_bk
acc = acc.to(C.dtype.element_ty)
```

3. 写回结果。

```
# rematerialize rm and rn to save registers
rm = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
rn = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
C = C + (rm[:, None] * stride_cm + rn[None, :] * stride_cn)
mask = (rm < M)[:, None] & (rn < N)[None, :]
# handles write-back with reduction-splitting
if SPLIT_K == 1:
    tl.store(C, acc, mask=mask)
else:
    tl.atomic_add(C, acc, mask=mask)
```

这里首先重新计算了输出矩阵中的坐标。其实前面已经算过了，但如果保留到这里就需要耗费register。

然后用mask保证不越界。最后判断如果`SPLIT_K`为1，即退化为非SPLIT K的情况，那就直接存结果。否则意味着多个CTA共同计算一个output矩阵的tile，那就需要做累加。又由于这些写的线程属于不同CTA，可能并行执行，因此需要使用atomic add。

### Stream-K GEMM

传统的做法是以problem为出发点，将problem size进行切割后，再将它们分到并行的计算单元上。但GPU上的并行计算处理器（SM）数量是固定的。这可能导致wave quantization问题（即子问题的数量不是并行处理器的整数），浪费计算资源。举个最简单的例子，一个任务可分为11个小任务（每个小工作需要1人/天），分给10个人干。但共需要2天才能全部完成，第二个会有9个人是无事可干的。而且这种问题随着GPU的更新，会越来越严重。因为计算单元更强，意味着需要更大的子问题才能“喂饱”它。那子问题的数量自然就会更少，这样就更容易出现wave quantization的现象。

那我们是否可以将子问题切得足够小（如果M, N维不够切就用Split-K），这样就能减少或避免wave quantization。但这样虽然SM利用率可能高了，但性能未必高。Block size过小可能会导致线程内IPL机会变小，另外计算密度变小。如果这样比较抽象的话，可以看一下具体的例子：https://pytorch.org/blog/accelerating-triton/#50-warp-stalling。

Split-K的限制在于它需要K维上的block在CTA间均分。那我们可不可以换个角度，从并行计算处理器为出发点，将子问题按SM数量来切分？这样所有的任务都可以在一个wave中完成，自然也不存在wave quantization的问题。这就是Stream-K的思想。还是用上面的例子，一个任务分为11个小的子任务，将11个子任务按人数分成10份，每个人完成1.1份。Stream-K与Split-K相比，SM利用率更高。而且同步归约次数也更少（不多于SM个数）。

Stream-K算法可参见2023年的论文《Stream-K: Work-centric Parallel Decomposition for Dense Matrix-Matrix Multiplication on the GPU》的`Algorithm 5`。但单纯使用Stream-K可能导致tile-processing skew问题。因此实际使用时会采用称为"two-tile...