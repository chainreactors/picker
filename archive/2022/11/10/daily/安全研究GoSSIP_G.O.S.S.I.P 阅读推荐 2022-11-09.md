---
title: G.O.S.S.I.P 阅读推荐 2022-11-09
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493210&idx=1&sn=00d3b069b027452cef8b5c28086608b8&chksm=c063c883f714419591ef4ef1f008789a5da00e7c4472d4699b2169705c431e39141d3ce0a038&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-11-10
fetch_date: 2025-10-03T22:15:35.668906
---

# G.O.S.S.I.P 阅读推荐 2022-11-09

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2Vh6YnFSFUJqpHpGvnDQn4bj5ZrMsPPaaicY2GW6gLcR6P5ubttlsGQaQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-11-09

原创

Ryan Zhou

安全研究GoSSIP

今天我们推荐的这篇被AsiaCrypt 2022录用的论文——*A Third is All You Need: Extended Partial Key Exposure Attack on CRT-RSA with Additive Exponent Blinding* 看上去很奇怪，这需要读者了解一些背景知识：鼎鼎大名的密码学家Nadia Heninger在Crypto 2009发表的研究论文 *Reconstructing RSA private keys from random key bits* 中指出“*an RSA private key with small public exponent can be efficiently recovered given a 0.27 fraction of its bits at random.*” 所以你搞清楚这个a third是什么意思了吗？如果还不清楚，那请继续往下阅读！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VATuJvz9eaGqZ9lscaLXvw9l99E05fTGPib8RGDrXQKuln3p9JsppP2w/640?wx_fmt=png)

抛开论文的细节，直接说最重要的结论：本文提出了一种新的针对盲化CRT-RSA实现的攻击 而盲化CRT-RSA实现是现在几乎所有智能卡采用的侧信道防护实现，那么本文的现实意义就是能够突破现实中大量的智能卡中的RSA运算的防护。下面我们来看看论文作者的详细介绍吧。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VeTSLc31lhqzA8d4tSl9tws3bFr6pk7ltiarNpT3MCd88kVqxmPN2vicw/640?wx_fmt=png)

**EPKE on CRT-RSA之缘起**

EPKE是指“扩展部分私钥暴露攻击”（Extended Partial Key Exposure），所谓“部分私钥暴露攻击”就是攻击者利用已获得的一部分私钥信息来恢复出完整私钥。自1998年Dan Boneh引入对RSA的PKE攻击以来，业界已经发表了很多针对（CRT）RSA的PKE攻击，绝大多数工作（见表1）都是针对没有指数盲化的情形。如表中最后两行所示，May等人在今年欧密上将无指数盲化的CRT部分私钥暴露攻击进一步推进到攻击者只需dp和dq的1/3最高位（或最低位）即可恢复出完整私钥。另一方面，指数盲化—尤其是加法指数盲化已被广泛采用来防范诸如侧信道之类的攻击。本文就是着眼于加法指数盲化情形下的CRT部分私钥暴露攻击，得到的结果是利用加法盲化后的dp‘ （= dp + rp(p-1)）和dq’（= dq + rq(q-1)）的1/3最高位（当rp2/3e
≈ N1/12，或最低位当rpe ≈ N1/12）即可恢复出完整私钥。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VgGtO2EJb4mmRsLcBA5Kgoq72x074ib75BlPvWr0USLxEdbp6yQ0P8fg/640?wx_fmt=png)

表1 部分私钥暴露攻击（无指数盲化）现状

我们采用了May等人欧密论文中提出的两步法来实施EPKE攻击：第一步是计算出CRT密钥生成的相关常数k‘（e\*dp’ = k’ \*(p-1) + 1， e\*dq’ = l’
\*(q-1) + 1）；第二步则是利用对k‘p的估计值来分解N以得到p。第一步又细分为以下三种情形：

1. 对已知dp’，dq'最高位的情形：**如果只有一个****dq‘的最高位已知，我们对k’l’的估计值进行因数分解以得到k’，所以是亚指数时间复杂度**。但因其长度大约只有N的1/6，所以用普通的PC就可在合理时间内分解得到k'（在我们的实验中绝大多数情况都在分钟级）。下图中的A就是k’l’的估计值，可以利用已知的信息计算出来，对A进行因数分解得到所有约数，然后再利用k'和l'的模加之和作为限定条件得出k'的两个可能值作为第二步的输入。

2. ![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VjYwekbricXzzcZ6k4iaDAvmGpP6jsnPJEKJSrX86u72GIKCmavAMxSSQ/640?wx_fmt=png)
4. **2. 如果有两个及以上的dq‘的最高位已知，我们则可以在概率多项式时间内求解相应的两个（或以上）k'l'的估计值的最大公约数以得到k**'，如下图所示。因为不同k'l'估计值不一定会互质，所以求解最大公约数直接得出k'的概率是跟所用到的k'l'估计值的多少直接正相关。我们的实验和概率的估计值表明5个（及以上）k'l‘的估计值就能达到将近1的概率，而两个k'l'的估计值能达到0.65左右的概率，但我们的实验也验证了在这种情形下可以结合一个小的穷举搜索得到k'的值，因为两个k'l'的估计值的最大公因数都比较小，穷举的代价完全能够接受。
5. ![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VUP6ib1632Q3dMSsgd5PZewhX19ribmViayyDDqRfliaGYnWwguUHk88wxw/640?wx_fmt=png)
6. **3. 对已知dp’，dq'最低位的情形：可在多项式时间内用Coppersmith的方法求解如下二元多项式的根得到k’**。
7. ![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VuK2LtFkUkDib8WUMcPLuqdtbnTYz7bhYkxmYU4YTsFhVV9lKlfIKtBA/640?wx_fmt=png)

第二步则都是在多项式时间内利用k'p的估计值分解N以求得p。**对已知****dp'，dq‘最高位情形：求解如下一元多项式的根得到dp’的未知LSB部分，然后分解N得到p**

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2V3jVcCGQBGKNZlAkibaic1XYzjibB6tyHrsicSpOnvVhfNT48rNgLKtWRWg/640?wx_fmt=png)

**对已知dp'，dq‘最低位情形：求解如下一元多项式的根得到dp’的未知MSB部分，然后分解N得到p**

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VfcEoAic6hFl8o0h0hM9ibMpPgJmYz42JmicGVdDAGwDc4RXCZ2ySxvHng/640?wx_fmt=png)

我们严格证明了所有情形下EPKE的正确性和时间复杂度，接下来我们用实验验证了不同情形下EPKE攻击的可行性和攻击所需时间。

**EPKE on CRT-RSA之验证**

我们实验了三种典型的密钥长度：1024，2048和3072位；以及三种常见的加法盲化因子长度：32，64和128位。实验环境是：Sagemath
v9.5, 开源因数分解库YAFU v2.08， Ubuntu
20.04.4操作系统以及Intel Core i5-7500 3.4GHz CPU。每种参数配置下我们都重复100次实验，每次实验都重新随机生成CRT密钥及相应盲化因子。

下表是只有一组dp'和dq'的MSB情形下的实验结果。如表中第5列所示，实验结果证明了因数分解k'l'所需的时间大概都在两个小时内（对2048位密钥长度以内的绝大多数情况甚至都在分钟级，图1~3分别对应1024，2048及3072密钥长度下100次实验的因数分解所需时间）。表中第4列的粗体数值对应理论值，我们的实验值非常逼近理论值（除了第4行，因为该情形下e不满足rp2/3e ≈ N1/12的条件而是选择了一个非常常见的e的长度，例如常用的e=65537就是一个17位的公钥指数）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VsjuWLCFwvzTZASwBLQaPIQicU46r471W5bHPMtU57v4fYUib9XhOupWg/640?wx_fmt=png)

表2 已知一组dp‘，dq’最高位实验结果

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VBCBW9LB6xNAxSicpAkTHibwibhDPduO4fe8ictk4ic5kXvhYnSEExMuQ1vg/640?wx_fmt=png)

图1 密钥长度1024因数分解所需时间（已知一组dp‘，dq’最高位）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2V4g1iaic1qqkE6KeK99tWWfic8T9ndGgD4I8vjuA9ZUp8xm90xibV52j6eQ/640?wx_fmt=png)

图2 密钥长度2048因数分解所需时间（已知一组dp‘，dq’最高位）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2V07VOLBcxPyLAze3ic1fe9ln17SYpbYnSCGXc9CaDdzWwmz5egscRcFA/640?wx_fmt=png)

图3 密钥长度3072因数分解所需时间（已知一组dp‘，dq’最高位）

表3则列出了已知一个dp'和多个dq'的MSB情形下的实验结果。最后一列对应2到10个dq'情形下求解最大公因数得出k'的概率，如果有5个及以上dq'最高位已知，攻击成功的概率已经接近1了。这些结果也吻合我们的理论值（见图4）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VFYDp772TwZGgh9V9Fic7oXzcXLz6R1v5DKaIEgUtIjsKwTouT1Z1ENA/640?wx_fmt=png)

表3 已知一个dp‘和多个dq’最高位实验结果

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2Vz0wKz6SMYvEaTrqejdOgA7hPFXvsCSc8tibg3Hdpx6IljoHfYlKk3MA/640?wx_fmt=png)

图4 多个dq'求解最大公因数成功概率（已知一个dp‘和多个dq’最高位）

如前文所述，如果只有2个dq'的最高位已知，攻击成功的概率大约在65%以上，但可以辅以一个穷举搜索得出k'。我们也用实验验证了穷举搜索两个k'l'的最大公因数是实际可行的，因为二者的最大公因数都很小（绝大多数都小于100，见图5~7，分别对应1024，2048及3072密钥长度下100次实验的最大公因数归一化直方图）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2V6OOibPEVVDl9OGgMY8hNKKibicSqzdMraeI5GfUqlY1s2AtUX2pGYdPPw/640?wx_fmt=png)

图5 密钥长度1024最大公因数归一化直方图（已知一个dp‘和两个dq’最高位）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VmeutqpJicbOwu4vFdic0oFlKknUf26icicHQnoGLb5ZqByn4sXYsfQS07w/640?wx_fmt=png)

图6 密钥长度2048最大公因数归一化直方图（已知一个dp‘和两个dq’最高位）

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VstnQAu54aialFTibfyNLrY1zYA8WS5kTavKBHPfOe8JkVU4ticbIgvckA/640?wx_fmt=png)

图7 密钥长度3072最大公因数归一化直方图（已知一个dp‘和两个dq’最高位）

表4则是我们进行的已知一组dp'和dq'的LSB情形下的实验结果，实际验证了Coppersmith启发式假设（这种情形下第一步求解k'是基于这个启发式假设）的有效性。相比MSB情形，同样的密钥长度及盲化因子长度条件下，LSB情形下需要已知更多位数的dp'及dq'。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2Ve5Lt6hJibdO2mkAiaOWyELs9SibW557ib5a0lzfQoDabRezxzN8ap3xqIQ/640?wx_fmt=png)

表4 已知一组dp‘，dq’最低位实验结果

# **EPKE on CRT-RSA之实例**

最后，我们还利用实际的侧信道泄露信息来实际演示如何在真实场景中应用EPKE攻击获取完整密钥。我们针对一款45 nm安全芯片上的Montgomery
Ladder模幂实现（乘法模数盲化 + 加法底数和指数盲化，2048位密钥和64位加法盲化因子）实施基于深度学习的模板攻击（见图8），再利用得到411位MSB或441位LSB盲化私钥指数（各10组密钥）进行EPKE攻击恢复完整私钥（如图9~10所示）。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VDKicgkFnNZEdY6GictBb7wt83OH6V8xl75fb88BYQyylRNGMVoTGxZcQ/640?wx_fmt=png)

图8 基于深度学习的模板攻击结果

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2Vy4G2oiajNslC1MZhnUxq6rFh1TAAmEIeBuyeZ8yrb53797U1yMiaEnxg/640?wx_fmt=png)

表5 基于侧信道攻击获取dp'及dq'的最高位的EPKE攻击结果

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21Gdr3aOeoYGXJNvu5GrlE2VFK9Rq7UP2iaNWpGYiavtGIgJlp1rJU6utAClkyZOfa7MecM7mzz5bj9A/640?wx_fmt=png)

表6 基于侧信道攻击获取dp'及dq'的最低位的EPKE攻击结果

跟其它PKE攻击一样，EPKE攻击需要已知的MSB或LSB信息完全正确，但实际攻击（例如侧信道攻击）结果很难做到100%的正确率，所以如何解决(E)PKE容忍一定程度的错误信息就是一个新的研究方向。

论文PDF：https://eprint.iacr.org/2022/1163.pdf

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过