---
title: DeepSeek V2/V3中的MLA和Matrix Absorption
url: https://blog.csdn.net/ariesjzj/article/details/145392128
source: 世事难料，保持低调
date: 2025-02-05
fetch_date: 2025-10-06T20:33:56.157063
---

# DeepSeek V2/V3中的MLA和Matrix Absorption

# DeepSeek V2/V3中的MLA和Matrix Absorption

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[ariesjzj](https://jinzhuojun.blog.csdn.net "ariesjzj")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2025-04-05 14:05:25 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.9k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

5

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
8

CC 4.0 BY-SA版权

文章标签：
[DeepSeek](https://so.csdn.net/so/search/s.do?q=DeepSeek&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[MLA](https://so.csdn.net/so/search/s.do?q=MLA&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[矩阵吸收](https://so.csdn.net/so/search/s.do?q=%E7%9F%A9%E9%98%B5%E5%90%B8%E6%94%B6&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[LLM](https://so.csdn.net/so/search/s.do?q=LLM&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[推理](https://so.csdn.net/so/search/s.do?q=%E6%8E%A8%E7%90%86&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2025-02-04 08:49:11 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/jinzhuojun/article/details/145392128>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756916.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

AI
专栏收录该内容](https://blog.csdn.net/ariesjzj/category_1243833.html "AI")

43 篇文章

订阅专栏

DeepSeek V3的网络结构基本沿用了DeepSeek V2，采用了MLA和DeepSeekMoE两大特性。本文主要涉及MLA（Multi-Head Latent Attention）。抛开维度变化，DeepSeek V3与V2在MLA结构上差别不大。详细请参见官方论文《DeepSeek-V3 Technical Report》和《DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model》。

关于MLA的介绍网上很多，不多讲了。这里将论文中的示意图，公式与官方代码（`modeling_deepseek.py`）的对应关系做了标注。
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/1c1ba3c5f40d479b8a8d278f600aabfc.jpeg#pic_center)

为了方便看出差别，这里按论文中的convention整了下matrix absorption后的示意图和公式，并标注了对应关系。代码由于官方没给出，参考的是SGLang中`python/sglang/srt/models/deepseek_v2.py`里的`DeepseekV2AttentionMLA::forward_absorb`。
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d3ffecb0d620493e9560f6c22c95db50.jpeg#pic_center)

其中matrix absorption的部分由于计算只涉及权重参数，因此可以提到初始化时，或者离线做。实现可以参考FlashInfer中`tests/test_mla_decode_kernel.py`中的`DeepseekV2AttentionMatAbsorbDecode`。

但注意该优化适用于generation阶段，不适用于prefill阶段。看下优化前后的相关两部分计算量比较：

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/7425c909988844e79d21d4e636920350.jpeg#pic_center)

将模型参数代入可发现，generation阶段时可以减少计算量，而prefill阶段时不能。

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/593b487487834c60800bd8d6f0545839_ariesjzj.jpg!1)

ariesjzj](https://jinzhuojun.blog.csdn.net)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  8

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  5

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

专栏目录

[*DeepSeek* V*2*版本*和*V*3*版本的区别](https://errol.blog.csdn.net/article/details/146548846)

[AI拉呱，专注于人工智与网络安全方面的研究，关注一起学习。](https://blog.csdn.net/weixin_32393347)

03-27
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
267

[*MLA*技术的引入，使得在大模型运行过程中，每次生成一个token时，只需要处理与之相关的token，极大地提高了处理效率并降低了显存占用。*DeepSeek*-V*2*首次引入MoE（混合专家模型）架构，这一架构通过多个子模型（即“专家expert”）的组合，有效减少了参数量*和*硬件消耗，从而实现了高效的*推理**和*成本效益高的训练。在 MoE 模型中，输入数据通过路由机制被分配给不同的专家（Expert），每个专家是一个独立的神经网络模块，负责处理特定部分的输入数据。每个深度上对每个标记进行预测时保持完整的因果链。](https://errol.blog.csdn.net/article/details/146548846)

[谈谈大模型的注意力机制 | *DeepSeek* V*3**中的**MLA*(多头潜在注意力)与传统的MHA(多头注意力)特性、差异与简化实现](https://devpress.csdn.net/v1/article/detail/145059060)

[m0\_56255097的博客](https://blog.csdn.net/m0_56255097)

01-12
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3773

[在Transformer模型中，注意力机制是其核心组成部分，它允许模型在处理序列数据时关注输入序列的不同部分。传统的多头注意力（MHA: Multi-head Attention）通过并行运行多个注意力头来捕捉输入序列中不同方面的关联。然而，MHA在计算*和*内存效率方面存在一定的局限性，尤其是在处理长序列时。*DeepSeek* V*3**中的*多头潜在注意力（*MLA*: Multi-head Latent Attention）旨在解决这些问题，提供一种更高效的注意力机制。](https://devpress.csdn.net/v1/article/detail/145059060)

参与评论
您还未登录，请先
登录
后发表或查看评论

[【*Deepseek*学习大模型*推理*】 *MLA*中*矩阵**吸收*原理。](https://devpress.csdn.net/v1/article/detail/146200150)

[王尚权 qq:2515162716](https://blog.csdn.net/qq_38662930)

03-12
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
335

[有了以上基础，再理解里面的*吸收*原理。](https://devpress.csdn.net/v1/article/detail/146200150)

[【大模型】*DeepSeek*核心技术之*MLA* (Multi-head Latent Attention)](https://devpress.csdn.net/v1/article/detail/145943672)

[酒酿小圆子呀～](https://blog.csdn.net/u012856866)

03-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2274

[在讲解*MLA*之前，需要大家对几个基础的概念（KV Cache， Grouped-Query Attention (GQA), Multi-Query Attention (MQA)，RoPE）有所了解，这些有助于理解*MLA*是怎么工作的，为什么需要这么做。](https://devpress.csdn.net/v1/article/detail/145943672)

[*MLA*实现及其*推理*上的十倍提速——逐行解读*DeepSeek* V*2*中多头潜在注意力*MLA*的源码(图、公式、代码逐一对应)

热门推荐](https://devpress.csdn.net/v1/article/detail/145552931)

[结构之法 算法之道](https://blog.csdn.net/v_JULY_v)

02-10
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1万+

[想来也是巧，最近*deepseek*实在是太火了，就连BAT这类大厂全部宣布接入*deepseek*，更不用说一系列国企、车企等各行各业的传统行业、企业都纷纷接入*deepseek*与此同时，也有很多公司、开发者对本地部署*deepseek*的诉求居高不下，我们也服务了一些B端客户，本文也提供了一些本地部署的方法结果，在网上看KTransformers资料的时候，无意中看到一篇帖子《*DeepSeek*-V*2* 高性能*推理* (1)：通过*矩阵**吸收*十倍提速 *MLA* 算子》，让我关注到了*DeepSeek*-V*2*对*MLA*的实现。](https://devpress.csdn.net/v1/article/detail/145552931)

[TensorFlow相关组件的安装](https://devpress.csdn.net/v1/article/detail/135495433)

[AAI666666的博客](https://blog.csdn.net/AAI666666)

01-11
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2985

[TensorFlow相关组件的安装](https://devpress.csdn.net/v1/article/detail/135495433)

[*LLM*笔记（九）KV缓存调研](https://jerryzhang.blog.csdn.net/article/details/148043609)

[Jerry的博客](https://blog.csdn.net/weixin_51147313)

05-18
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1474

[*LLM* KV缓存简单调研，待更新完善，目前为大纲。](https://jerryzhang.blog.csdn.net/article/details/148043609)

[*DeepSeek* v*2*/v*3*技术解读](https://blog.csdn.net/u012599545/article/details/145535882)

[hang on it more longer](https://blog.csdn.net/u012599545)

02-09
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1934

[v*2*论文：[*2*405.044*3*4] *DeepSeek*-V*2*: A Strong, Economical, and Efficient Mixture-of-Experts Language Modelv*3*论文：[*2*41*2*.194*3*7] *DeepSeek*-V*3* Technica...