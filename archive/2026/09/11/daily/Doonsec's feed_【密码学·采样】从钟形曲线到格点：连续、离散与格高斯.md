---
title: 【密码学·采样】从钟形曲线到格点：连续、离散与格高斯
url: https://mp.weixin.qq.com/s/4P5qRR-Xu5rhRK_ROoAfmQ
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:47:45.987735
---

# 【密码学·采样】从钟形曲线到格点：连续、离散与格高斯

# 【密码学·采样】从钟形曲线到格点：连续、离散与格高斯

原创

Litt1eQ
Litt1eQ

Coder小Q

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 【密码学·采样】从钟形曲线到格点：连续、离散与格高斯

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mdiagd7Bulj1PR7LV4ibomNSNJNiajrmkny6Xx3Rst7VMA1pLsrOnxzcy5POHnlQnJNTCHOXqSE9e9bM1Ztich3bkVhRHCQp33D3FZX2tJMd1Zk/640?wx_fmt=png&from=appmsg)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mdiagd7Bulj2R326ic2FTIjTwpia6f4HrYoqNPfSDIc0l2bMXNJSp8lv3YIib9rzvKpUToKB0WLib6NKDYZeWFqqdPjLsBMiaiagQasw3OVmEib4QD0/640?wx_fmt=png&from=appmsg)钟形曲线还不是格点概率表

上一篇把最近格点与随机采样分开了：前者要从候选中选出一个近点，后者要让许多合法输出按照指定比例反复出现。现在把几何选择换成概率问题。假设一条钟形曲线覆盖在整数轴上，我们究竟怎样从它得到整数点的概率？

连续分布的密度描述的是概率怎样沿实数轴分布，区间概率要靠积分得到；密度在某一点的高度不是这个点的点概率。这个区别已经在第 3 篇建立过，这里只保留它最关键的后果：连续随机变量恰好等于某个整数的概率为零，而我们要构造的整数随机变量却必须给每个可能输出一个确定概率。

把曲线画在格点背后，只能提供形状上的提示。可以对每个整数读取曲线高度，也可以把每个整数周围的一段曲线面积交给它，还可以先在实数轴上抽样再执行某种舍入；这些规则都能输出整数，却一般产生不同的概率表。输出类型正确只是第一道门槛，输出分布正确才是采样算法真正需要证明的事情。

因此，本篇不把“钟形”当作定义，而会依次回答三个问题：格点上的相对偏好怎样写成权重，权重怎样变成总和为一的概率，以及同一套定义放到高维格上后会受到哪些几何因素影响。等这张概率表写清楚，我们才有资格讨论算法是否真的从中采样。

## ![](https://mmbiz.qpic.cn/mmbiz_png/Mdiagd7Bulj1YTp5Dl0dGsfKoXJaB2sucy5Aj9oZWveXblkSU6XnzxsI5H0YPticspuHcRAOQ8RW9icWSSTuBecTztKhdWDpoHLb2ELup9WYOs/640?wx_fmt=png&from=appmsg)先给整数轴上的每个点一份权重

既然连续曲线的高度不能直接充当点概率，第一步应当保留什么？最自然的做法，是让离中心近的整数更受偏爱、远处整数的偏爱按距离平方迅速衰减。也就是说，先给每个整数点一份尚未归一化的相对分量，再让所有分量共同决定最终比例。

先留在整数轴上。设尺度 、中心参数为 ，给每个整数点  分配相对分量

这个正数称为**高斯权重**（Gaussian weight）。它在  时达到一，并随  到  的距离增大而迅速下降；若  不是整数，则没有哪个整数点的权重能达到一。

高维推广只需把一维距离换成欧氏距离。对中心  和空间中的点 ，定义

距离相同的点权重相同。这里的  不是装饰；这种参数约定会让后面的积分、缩放和格论公式更整齐。它与统计课中常见的标准差参数并不相同，二者的换算将在后文给出。

先把向量退化为实数。取  时，整数  的权重依次约为

这些数已经表达了远近顺序，却还不是概率，因为它们的总和不是一。对一个可数集合 ，把各点权重相加，所得

称为集合  的**高斯质量**（Gaussian mass）。当  时， 是把无穷多个整数权重压成概率表所需的**归一化常数**（normalizing constant）。于是

这个概率分布称为**离散高斯分布**（discrete Gaussian distribution），记作 。

分母看起来是一串无穷和，但它确实有限：格点数随观察半径至多按多项式增长，高斯权重却按距离平方指数衰减，后者最终压过前者。严格论证放在第一则附录。这里特别要注意，图中只画出的有限个点不是支撑集的截断定义；整数轴上每个整数仍有严格为正的概率，只是远处的概率迅速变小。

下图把三个容易混淆的对象排在一起。顶端是连续密度，中间是尚未归一化的格点权重，底端才是总和为一的点概率。曲线决定了衰减轮廓，但从曲线到概率表还隔着“只在格点取值”和“对全部权重归一化”两次变化。

![连续密度、格点权重和归一化点概率具有相似轮廓，却是三种不同对象。](https://mmbiz.qpic.cn/sz_mmbiz_png/Mdiagd7Bulj2rVUEsDcJIsaeOjPuBQ9n3XCSScphLzwtFZIAcfwIXibMQtvNtOG8Wa7OibcT5S7mUk1mVZcCE5M55DqvvwUY3MNFqIFPJUibVe8/640?wx_fmt=png&from=appmsg)

连续密度、格点权重和归一化点概率具有相似轮廓，却是三种不同对象。

归一化还有一个重要作用：它把“每个点有多受偏爱”变成了相互依赖的整体概率。若只改动一个点的权重，分母也随之改变，其他所有点的概率都会略微变化。因此验证离散高斯不能只检查几个中心点；目标是一张覆盖整个支撑集的概率表。

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mdiagd7Bulj3vydic3PibPIHXq220K0JX8IT1ZFPNCeL30FKgNicQanAjQ6TgBhXZkXrMDz15sS41hwxMGnb3ia6e07XXb6z4X120ECicGoUklVLU/640?wx_fmt=png&from=appmsg)连续高斯取整为何得到另一张概率表

既然连续高斯和离散高斯都呈钟形，能否先抽一个连续高斯，再把结果四舍五入？设连续随机变量  的密度为

因高斯积分的缩放关系，这个密度在整条实数轴上的积分为一。若使用通常的最近整数取整，并固定半整数处的任意决胜规则，那么边界点本身概率为零，输出整数  的概率为

这条规则把以  为中心、长度为一的区间面积交给 。

离散高斯则使用另一条公式：

所以取整依靠区间积分分配质量，离散高斯依靠逐点权重再统一归一化，两种过程一般不会给出同一张概率表。差异并非来自数值误差，而是来自定义本身：前者平均了一个单元区间内的曲线，后者读取单个格点处的权重，再由全体格点共同确定分母。

下图显示了这种差异。中心附近，区间积分把曲线峰顶两侧的一部分面积一起交给零点；离开中心以后，区间中靠近中心的一侧又会比远侧更高。逐点取值无法逐项复现这种区间平均，因此两组点概率虽然轮廓相似，却不会完全重合。

![连续取整按单元区间积分，离散高斯按格点权重归一化，二者并不相同。](https://mmbiz.qpic.cn/mmbiz_png/Mdiagd7Bulj0ovFbgs3iawdSV3shPVsEicibaEfibZqBQf2U5zjEYaAsfDe9xHc7dcFqFbdSTzicxIKAJPaqJp30DiclclqXMscyCHf79afXMT2ZtU/640?wx_fmt=png&from=appmsg)

连续取整按单元区间积分，离散高斯按格点权重归一化，二者并不相同。

某些尺度下，两张图可能非常接近；但“肉眼接近”不是分布相同的证明。若安全论证允许近似，还必须像第 7 篇那样明确使用何种分布距离、误差有多大，以及这种误差在重复调用后怎样累积。这里暂不估计距离，只锁定结构性的事实：连续抽样后取整是一种合法的整数采样算法，却不是离散高斯定义的自动实现。

同样的警告适用于最近格点算法。把连续样本送入确定性的最近点过程，相当于把空间切成许多判定区域，再把每块区域内的连续质量交给对应格点。所得点概率由整块区域的形状决定，而目标离散高斯只由格点到中心的距离和全局归一化决定。除非另有证明，两种概率表没有理由恰好一致。

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mdiagd7Bulj0kDuGs4IzibeibiadftzOjm4opmzkrN9EaDic6ux5oyeth5gV9m364Xfq6BH1pn221YXSMibAFCvZmMiaI2s8AMN8HqawsHqCM0vlCI/640?wx_fmt=png&from=appmsg)从整数点推广到平移格

整数轴上的定义怎样搬到任意格上？公式本身并不困难，真正需要先理清的是几何：究竟哪些点允许成为输出，钟形权重又围绕哪个位置衰减。移动允许输出的点集，与移动权重的中心，是两种不同操作。

设  是满秩格，。把整个格平移  得到的集合

称为**平移格**（shifted lattice / lattice coset）。它通常不是一个含原点的格，因为其中两点相加未必还在集合中；但它仍是一张规则的离散点阵，点与点之间的相对位移和原格完全相同。

对任意非空可数集合 ，只要

就定义

当  是格或平移格时，这个分布称为**格高斯分布**（lattice Gaussian distribution）。特别地， 的支撑集是 ，而中心参数  可以在空间中的任意位置，不必属于这个支撑集。

下图比较了三种变化。固定整数格而移动中心，只会重新分配同一批整数的权重；固定中心而平移支撑集，则会改变哪些实数点能够出现。平移格的支撑集、中心参数、期望与众数因此必须分别辨认，不能因为图形都围绕某个位置显得集中就把四者混成同一个量。

![移动中心改变点的相对权重，移动支撑集则改变随机变量可以取得的值。](https://mmbiz.qpic.cn/mmbiz_png/Mdiagd7Bulj2ibbErt7rMCMT84zFgofjbfVicMT139RINYajKL1wUx0E85RSMBNdvaO49OHTIIkjbxL8snRiad65rm5hknGAq3dVdUogvt82RnQ/640?wx_fmt=png&from=appmsg)

移动中心改变点的相对权重，移动支撑集则改变随机变量可以取得的值。

平移坐标可以把问题送回原格。若

令 ，则 ，并且对每个 ，

因此

这不是说平移可以忽略，而是说“移动支撑集”和“反向移动中心”可以通过坐标变换互相换写。后面比较不同平移格的总质量时， 仍会成为关键变量。

## ![](https://mmbiz.qpic.cn/mmbiz_png/Mdiagd7Bulj2ZTz1bjrhe1vLfxggOkp7fibGQCjhhIIQxh20SHRNv14bJlISa8xO3MICKKQtGDL344yDpqlwHhiavo3IKfPNLjcTtv4EGtQVtU/640?wx_fmt=png&from=appmsg)中心、均值与最可能点并不总在一起

中心参数  决定单点权重如何随距离衰减，但它不一定是随机变量的期望，更不一定是一个可输出的点。对固定支撑集 ，权重最大的点是离  最近的支撑点；若最近点不唯一，众数也可以有多个。这只是比较单点权重，不涉及把全部概率乘以位置后求和。

一维整数格已经能看出差别。若尺度取 、中心取 ，零点比一点更近，因此零点是唯一众数；但负整数仍带有少量概率，正整数也不只包含一点。把所有位置按概率加权后，所得期望约为 ，并不等于中心参数 。偏差很小不等于偏差不存在，它来自离散支撑集相对于中心并不镜像对称。

什么时候二者会重合？若集合关于  中心对称，即

那么每个  都能与  配对，两点权重相同、相对中心的位移相反。只要相应级数绝对收敛，对称配对便给出 。这条等式来自支撑集与权重的共同对称，而不是“中心”这个名字本身。

众数与期望也回答不同问题。众数寻找单点概率的最大值，通常落在离中心最近的一个或几个格点上；期望却汇总整张概率表，可以落在支撑集之外。对于密码学采样，算法输出当然必须在支撑集内，但安全证明比较的是所有点概率，不会因为众数位置正确或样本均值接近中心就自动成立。

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mdiagd7Bulj0nJIEAEttibKOmj2wsvC9RkvEgwSvDkROO0QIvRftbicMooCbgbJIS78ZSSyNt1QuoiagLRIwcvVo3Gw1qXVYICaEd3aImqzHwyc/640?wx_fmt=png&from=appmsg)尺度必须和格点间距一起看

参数  控制衰减速度，却不能脱离支撑集的几何单独解释。在球形模型中， 只有放到具体格的几何尺度旁边才有完整意义。对连续的一维球形高斯，统计标准差  与本篇尺度的关系是

因此  不是标准差本身。连续  维球形情形中，每个正交坐标方向的方差为 ；这条连续结论也不能未经条件直接搬给任意离散支撑集。

真正决定点概率轮廓的是  与格点间距的相对大小。下图中，上排固定间距而改变 ，下排则同时改变格距：同一个 ，放在间距  的细格上会覆盖许多点，放在间距  的粗格上却只给少数点可见概率。

![尺度只有和格点间距比较才有意义；相同宽度在粗格与细格上表现不同。](https://mmbiz.qpic.cn/sz_mmbiz_png/Mdiagd7Bulj11tGkb3Sc7Hu8hX2NxWHuV6WRQic86hlmYbrAe5uic3BCKPPqfC3SAKq6iatybCrPu7rvZHvEAxNktUMIGTlcibeFyiaVEiaDaXn9IY/640?wx_fmt=png&from=appmsg)

尺度只有和格点间距比较才有意义；相同宽度在粗格与细格上表现不同。

这种相对性可以写成精确的缩放恒等式。对任意 ，距离和尺度同时乘  时，指数中的比值保持不变，因此

所以把一幅图整体放大，并不会改变对应点的概率；只有单独改变支撑集、尺度或中心，才会改变相对权重。

当  趋近零时，稍远一点的权重就会被指数压得极小，概率集中到离中心最近的支撑点；若有多个等距最近点，极限质量会在这些点之间分配。这个现象像最近点选择，却仍是一个分布极限。反过来，让  越来越大，会使任何固定有限窗口内的点权重变得接近，但无限格上的均匀分布不存在：无限多个点不可能各自获得同一个正概率而总和仍为一，也不能各自概率为零却构成离散概率分布。

## ![](https://mmbiz.qpic.cn/mmbiz_png/Mdiagd7Bulj0qQkKcQBf7ftDDxylicYGMicaI5avny9LVMqtzkhwy4h254YvHXBzl7rzca52Swkz19icf7icxuYVcOzL0HMrfVxVvH95MQYaZXibo/640?wx_fmt=png&from=appmsg)正交坐标可以拆开，斜格通常不行

进入二维以后，格高斯不再只是把一维概率表并排放几次。对中心 ，权重的等值集合由欧氏距离决定，是一层层以  为中心的圆；高维时则是球面。下图中，点的大小只取决于空间位置到中心的距离。把同一个格换一组格基，只会改变点的整数坐标表示，不会改变任何点概率。

![格高斯属于空间中的点集；改变描述同一格的基，不会改变目标概率。](https://mmbiz.qpic.cn/sz_mmbiz_png/Mdiagd7Bulj0ZBcTo3fmEgKibUibw9I2E4IC4icduTBj5IMiaHejYce5YtCK43aG6rhrC6PHbPyI3KibYQzk0p76579DRMfJCOamFAFwNGHXlgk8I/640?wx_fmt=png&from=appmsg)

格高斯属于空间中的点集；改变描述同一格的基，不会改变目标概率。

设基矩阵为 ，格点写成 。指数中的距离平方为

若基向量倾斜， 含有非零的非对角项，坐标乘积  会进入距离。同一格点的一个坐标变化会与另一个坐标共同影响权重，因此不能把各坐标当作相互独立的一维离散高斯。

正交格是一个重要的可拆情形。设  两两正交，并把中心写成

格点  到中心的距离平方可分解为

指数把和变成乘积：

所有非负项的求和也能按坐标分开，所以归一化常数同样分解，最终点概率成为若干一维点概率的乘积。完整换序论证放在第三则附录。

下图把关键差别压缩成一幅几何图：正交方向上的两段移动满足勾股分解，斜方向的合位移却包含交叉影响。Gram–Schmidt 可以为分析距离提供正交方向，但它一般不把原格变成这些方向的整数直积；因此不能仅凭正交化就断言原分布能够沿这些正交方向独立分解。

![正交方向使距离平方逐项相加；斜坐标中的交叉项会耦合各个分量。](https://mmbiz.qpic.cn/mmbiz_png/Mdiagd7Bulj2W4ywicxibRtEDzibL4HibTTXAAQHUx82KwuQ1l9odM6OEhv1Lia5hgD4gov3QfdwfMpWEY5cNIjiaUhH1aK2bxvpWbXnw7SMicrNemU/640?wx_fmt=png&from=appmsg)

正交方向使距离平方逐项相加；斜坐标中的交叉项会耦合各个分量。

这一区分也说明目标分布为什么不应依赖秘密表示。换格基不改变空间中的支撑点、距离或点概率；一个实现可以利用某组好基完成内部计算，但公开输出所呈现的概率表必须属于格本身，而不是泄露“算法恰好使用了哪组坐标”。

## ![](https://mmbiz.qpic.cn/mmbiz_png/Mdiagd7Bulj3yMynbwEAIBicpb3un9paWL8jgKDRkoyOQicRfRKzyL85O7wXxL9ibDibrH87lSUbeKwnMJR2NtAeRIyibMKZDhVlH6Wyky8ZuhwI0/640?wx_fmt=png&from=appmsg)高维概率为什么不都挤在中心附近

每个点的权重都随距离减小，是否意味着高维样本几乎总在中心附近？答案要同时看两股力量：离中心越远，单点权重越小；可是半径稍大的薄壳能够容纳更多位置。高维中的典型距离由“壳里有多少位置”和“每个位置还有多少权重”共同决定，而不是只由钟形曲线的最高点决定。

下图左侧按半径画出若干壳，右侧把每层的点数、平均单点权重和总质量分开。点数可以随半径增长，单点权重则快速下降；两者乘积往往先增后减，使主要概率出现在离中心有一定距离的一圈，而不是全部压在中心点上。

![高维壳层的总质量由点数增长与单点权重衰减共同决定。](https://mmbiz.qpic.cn/mmbiz_png/Mdiagd7Bulj0mUEfTEyjQ2v84TztAvzwb6A5qFlsRuWJbWZswz7XEn8PvkzlAD94kzWjicAsot2NZSia71DpyeHSXs8ibuFxg711V6sBPiafiavx8/640?wx_fmt=png&from=app...