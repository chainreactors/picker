---
title: 芯片电磁相位泄露与密码侧信道攻击
url: https://mp.weixin.qq.com/s/gxvHE_48GQWjl8Rdo564xw
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:03:44.550995
---

# 芯片电磁相位泄露与密码侧信道攻击

# 芯片电磁相位泄露与密码侧信道攻击

数缘科技
数缘科技

数缘信安社区

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**FRONTIER INSIGHTS**

**前沿导读**

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwXwDmYlO0Qbc77lUndI1yVLXYFXnoRgibdBqA2ibReIPRFrdMA8VzxKZqKOLDLav0Y65SD7r7uOj2w0sWgxj9rxgG4cmn3yugJQY/640?wx_fmt=png)

撰文 | 周昱炜

编辑 | 刘梦迪

**当看不见的时钟抖动暴露了加密密钥**

**一、**

**背景介绍**

侧信道攻击并不直接破解密码算法本身，而是利用设备运行时产生的时间、功耗或电磁辐射等物理信息推测秘密数据。长期以来，电磁侧信道研究主要关注信号幅度：处理器执行高级加密标准（Advanced Encryption Standard，AES）等密码运算时，数据相关的功耗活动会改变辐射强弱，攻击者可据此建立模型并恢复密钥。相比之下，相位是一种相对且具有周期性的量，容易受到本地振荡器不同步、相位缠绕和跨次采集初始相位变化的影响，因此以往使用无线电接收机的电磁侧信道攻击几乎都只利用幅度信息。

刊载于《IACR Transactions on Cryptographic Hardware and Embedded Systems》（密码硬件与嵌入式系统汇刊，TCHES）2025年第1期的论文《PhaseSCA: Exploiting Phase-Modulated Emanations in Side Channels》，由EURECOM的Pierre Ayoub、Aurélien Hernandez、Romain Cayre、Aurélien Francillon，以及法国里尔大学、法国国家科学研究中心（Centre national de la recherche scientifique，CNRS）和Inria研究院的Clémentine Maurice共同完成。作者识别出非预期的电磁相位调制，提出从软件定义无线电（Software-Defined Radio，SDR）采集的同相/正交（In-phase/Quadrature，I/Q）信号中构造相位偏移轨迹的方法，并仅凭相位信息完成AES全密钥恢复；在此基础上，幅度与相位融合还能进一步提升攻击性能[1]。

**二、**

**基本原理**

SDR通过直接变频将目标时钟附近的高频载波搬移到基带，并同时输出同相分量I和正交分量Q。两者可组成复数采样：传统攻击根据I/Q分量计算信号幅度，本文则对复数采样求相角得到瞬时相位。由于相位是相对于接收机本地振荡器测得的，不同采集之间通常缺乏统一的绝对相位基准，原始相位不能直接作为稳定、可重复比较的侧信道轨迹。核心计算关系如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwUuajKMFUkgicCdqhjwxiaRTr5AsHcubQx0dtQdJhvxATgt5c3mmjuibgVNa3XNTwj2tNehotMkkzfdvyJ7ZYvcZFNHIaloEI3lVI/640?wx_fmt=png)

同相/正交采样及相位偏移轨迹的核心计算关系

作者将相位转换为可供标准侧信道算法处理的一维实值轨迹。首先把瞬时相位限制在[-π, π]的主值区间；随后进行相位解缠，消除2π跳变并得到连续瞬时相位；再减去每条轨迹的首个采样值，使不同采集从同一相位起点开始；最后对连续相位作一阶差分，以相邻采样之间的相位变化量构造相位偏移轨迹。差分步骤既去除了跨次采集的初始相位偏置，也避免了连续相位长期累积，不需要额外的参考时钟即可形成可攻击轨迹。转换过程如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwWyU0Jvc10AMFu46IRicpGwia99YdwiaQ9TzlicAyic3sc0KbcHbBXOQqibkwz5rq9eicQKSkW8wzDBkiac5IUWd6HDO5nTAoibj5AJMz6Q/640?wx_fmt=png)

相位轨迹从缠绕相位到相位偏移的转换过程

相位泄露的物理基础是时钟抖动与相位偏移之间的对应关系。数字电路的时钟边沿无法始终在理想时刻到达；当处理器活动引起的数据相关功耗变化通过供电网络、振荡器、锁相环（Phase-Locked Loop，PLL）、时钟树或芯片衬底耦合影响传播延迟时，时钟周期会产生确定性变化。在无线电接收端，时间上的微小偏移会表现为载波相位变化。因此，相位偏移可以看作对时钟抖动的间接测量，而时钟抖动又可能携带处理器活动与秘密数据的信息。

**三、**

**实验内容**

侧信道攻击实验以SDRPlay RSPdx为接收机，一次记录目标时钟附近10 MHz带宽的I/Q数据；TekBox TBPS01近场探头置于芯片数毫米处，且不与目标建立电气连接；泄露较弱时再使用TBWA2宽带放大器。接收机通过通用串行总线3.0（Universal Serial Bus 3.0，USB 3.0）将原始采样传送至计算机，目标板运行包含TinyAES软件实现的自定义固件。为降低环境射频噪声，整套测量装置置于电波暗箱中，具体结构如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwWSNv6HTte7B9Xk1zsSuUdiaRpe1N9HnibfsbEj8ibb61bXbfdxSMzYIn3hPicTWeWFBia66md9MU3Lx0wZgoSxnBaf7jB3FwD0Xo58/640?wx_fmt=png)

电磁侧信道攻击实验测量装置

作者选择STM32L1、nRF52832、nRF51422、ATmega328和RP2040五类常见微控制器或片上系统（System-on-Chip，SoC），覆盖不同处理器架构以及电阻-电容（RC）振荡器、PLL等时钟生成方式。采集中心频率设置在系统时钟基频或相近谐波处。攻击目标为AES第一轮替换盒（S盒）之后的中间值，并分别使用非模板的相关无线电分析（Correlation Radio Analysis，CRA）和模板化相关攻击，以检验相位轨迹能否独立恢复密钥。

对每一组I/Q测量，作者同时生成幅度轨迹和相位偏移轨迹。为判断两类泄露在频谱中的分布，原始复信号在解调前还接受高通或低通滤波。随后，作者在决策层进行多通道融合：先分别计算每个密钥猜测在幅度通道和相位通道上的皮尔逊相关系数，再将两者相加形成统一区分器。该方法不增加探头、接收机或采集次数，只对同一份I/Q数据进行不同处理。

为追踪泄露来源，论文另搭建时钟抖动复现实验。目标器件为STM32F103RB；示波器以每秒20亿次采样（2 GSa/s）直接测量其输出时钟。中央处理器（Central Processing Unit，CPU）被设置为休眠、空转循环和连续执行AES三种状态；同时，研究人员通过ChipWhisperer-Lite的场效应晶体管开关电路，在通用输入/输出接口（General-Purpose Input/Output，GPIO）上制造可控的额外耗电，并切换内部振荡器、外部时钟和PLL等配置。另一套SDR近场测量与示波器同步工作，用于比较功耗变化、时钟抖动和电磁相位偏移之间的关系，装置如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwXu1IJJ3IZ9zYCBoh1C6f4ImtxictGeUrib62t6ib7afhphulqBFVsxYcklZ7aZ7d6H4pmIjnVmrxLqR3pOeiaiaMZuib3vJH1HHsbqs/640?wx_fmt=png)

时钟抖动来源研究实验装置

**四、**

**实验结果**

**（一）**

**识别非预期相位调制**

作者首先比较无系统活动、软件AES和硬件AES三种情况下的连续瞬时相位。没有额外活动时，相位曲线保持近似稳定的趋势；执行软件或硬件AES后，曲线出现明显且结构化的偏移，说明密码运算不仅改变电磁信号幅度，也会改变相位。

对连续相位作差分后，相位偏移轨迹能够清楚呈现AES密钥扩展和多轮运算的时间结构。其时域与时频轮廓和传统幅度轨迹相似，为电磁辐射中存在可利用的数据相关相位调制提供了直接证据，具体如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwWReJicOzPyickwlf2Og2l12dzia2vibWK0zccNfkTh2DwibUKBACSJugzQzUGsCmt5hibLCHmUyKfAAgYrAVqGsibZYJSrACKTzvvrEc/640?wx_fmt=png)

不同系统活动对连续瞬时相位的影响

五个目标中，STM32L1、nRF52832、nRF51422和ATmega328均检测到可利用的幅度与相位泄露，并能通过两类通道分别完成密钥恢复；RP2040虽受CPU活动影响，但未发现可攻击的幅度或相位信号。这表明相位泄露不是单一芯片的偶发现象，其可利用性仍受动态频率调节、电源域隔离与时钟结构等因素影响。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwX11N6Zh5oshqRs4LJUj49KCsEZJILWb3GVRY5cXL3FVBBKicvs1wJhCyJ1hFvbGiaescbYZgqryBxxEU5EtDDROzyYAoIot6uqg/640?wx_fmt=png)

高级加密标准幅度/相位轨迹与不同片上系统测试结果

**（二）**

**相位侧信道攻击**

针对nRF52和STM32L1，作者分别采集4000条训练轨迹和1000条攻击轨迹建立模板，并在其他目标上实施相应的模板化或非模板化攻击。实验显示，相位偏移轨迹在多个采样点与AES输入模型的皮尔逊相关系数超过0.5，足以选择信息泄露最明显的兴趣点并完成全密钥恢复。

频率分布结果尤其值得注意：原始信号以10 MHz带宽采集，但对相位通道使用50 kHz低通滤波后仍能恢复完整AES密钥，说明相位泄露的主要成分集中在载波附近。幅度通道则呈现相反规律，高通滤波通常改善攻击，低通滤波会削弱攻击，表明幅度信息更多位于载波两侧的宽边带中。对相应频带进行选择性滤波，可以减少无关噪声并提高攻击效率。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwVFKiagNxtMIhXNXRXnayBibfYw0mwJzORlxG6up3pnDvSLD5xv8PZFWAuFYvj5mnibqjRibGOaMlhjyuLF2WbXoicX5qAzVKH2ib560/640?wx_fmt=png)

不同低通带宽下的相位轨迹与相关系数

从攻击性能看，仅使用相位在多种条件下已优于仅使用幅度。例如，在nRF52模板化攻击和nRF51非模板化攻击中，相位通道能够显著降低正确密钥的排名。更重要的是，相位并不是幅度的简单重复：两者来自同一组电磁测量，却在接收端保留了互补信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwUjiaGtChhIRJIv9ic1rejjLxeAkPX9zW1jyR25WEyRIeuIl9LsSIm5ZZ3MH3uk29GEicYib585EdiaibxBuwtqvR3XcWyFhVlJ962QQ/640?wx_fmt=png)

幅度、相位及融合攻击的正确密钥排名对比

将两类通道的相关系数相加后，融合曲线在所有成功目标上总体下降更快，即使用更少轨迹就能把正确密钥推到更靠前的位置。论文报告，在最佳场景下，相比仅使用幅度，融合方案可使正确密钥排名的以2为底对数降低约40。整个提升不依赖额外硬件或更多采集，只来自对既有I/Q信号的幅度与相位联合利用。

**（三）**

**时钟抖动与相位泄露来源**

抖动复现实验显示，CPU由休眠状态切换为空转循环或连续AES运算后，64 MHz系统时钟周期的标准差明显增大；即使不改变处理器指令，仅通过GPIO制造额外耗电，也会显著改变时钟周期的均值和离散程度。这表明可观测抖动与芯片总体功耗变化相关，而不是某一条指令独立造成的偶发现象。

不同时钟配置表明，内部与外部振荡器、PLL及时钟树都可能参与形成泄露。关闭PLL时，从休眠切换到AES的抖动增量更明显；启用PLL后虽有更高的基础抖动，仍保留数据相关变化；直接使用外部时钟时AES活动依然增加抖动，说明时钟树和传播路径也是潜在来源。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwUqLibj3iaaNicqdwOjFUz4MJwibPH4yYFu2QKsAMumRnK0MpFkWNK8ic3dZPAnub3YPDoMV8Ocu8DskTzYkK30YfFxewicoOFFichibOo/640?wx_fmt=png)

不同处理器状态、耗电事件和时钟配置下的时钟抖动

近场测量还观察到与人工耗电事件同步的周期性相位偏移。示例中，示波器测得约275 ps（皮秒）的时钟抖动，SDR解调得到约0.125 rad（弧度）的相位偏移，换算误差约为11%。由此可将“数据相关功耗变化—时钟抖动—电磁相位偏移”串联起来，为相位泄露的物理成因提供实验依据。

**五、**

**总结**

本文提出了把相对且周期性的相位转换为稳定侧信道轨迹的方法，并利用常见SDR与近场探头，在无电气接触条件下仅凭相位恢复完整AES密钥。五类商用SoC中有四类存在可利用的相位泄露，幅相融合还能进一步改善密钥排名；复现实验表明，数据相关时钟抖动可能是其重要来源。后续仍需在更多SoC、硬件AES加速器及其他密码算法上验证普遍性，区分振荡器、PLL、时钟树、串扰与阻抗变化等机制，并研究同时抑制幅度与相位/抖动泄露的防护方案。

**参考资料**

[1] AYOUB P, HERNANDEZ A, CAYRE R, et al. PhaseSCA: Exploiting Phase-Modulated Emanations in Side Channels[J]. IACR Transactions on Cryptographic Hardware and Embedded Systems, 2025, 2025(1): 392-419. DOI: 10.46586/tches.v2025.i1.392-419.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwXRvLfeiaWUmJsHF19JibPG82ABgAtTwu2SFzcphK204EBQNvcS3eTpGoYo6kQ7m4pbAgYaAmdatAbDOj5sSaf3PJ7joXerSxS6s/640?wx_fmt=png)

**往期精彩文章推荐**

* [利用RFM Rowhammer防御机制攻击GPU](https://mp.weixin.qq.com/s?__biz=MzI2NTUyODMwNA==&mid=2247496191&idx=1&sn=9448282cc0ddca4294f742371c1f3362&scene=21#wechat_redirect)

* [基于TLB侧信道攻击的稳定内核利用技术](https://mp.weixin.qq.com/s?__biz=MzI2NTUyODMwNA==&mid=2247496380&idx=1&sn=eff16cdb902e9d3bcf8c282d3c178dc5&scene=21#wechat_redirect)

* [手机传感器，也会“听见”CPU的功耗](https://mp.weixin.qq.com/s?__biz=MzI2NTUyODMwNA==&mid=2247496521&idx=1&sn=872e406f2e273d702886e0895e940525&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwWCPw029GQSzr9qam4JcgXjqCjibNu52CgfIkHmaiczCmc48AfTicibI8gMbk2YKETaQQpdjZGe0gkzyMQia8TicFg2o7xzvOHdNq5JQ/640?wx_fmt=png)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sSglg2t6pLdibP1eoMFnDyyCjXAfpDzbcSiahmcJJVCJGlVlhz3tn375M3T7671B9c4QAkhj2KBp6yynY1uOsU8w/0?wx_fmt=png)

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