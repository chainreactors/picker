---
title: 如何理解镜像频率？
url: https://mp.weixin.qq.com/s/q4ADgG6NH9EtY0CDiZUfuQ
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:08:18.754904
---

# 如何理解镜像频率？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0plbPNoicicKQ3DTsdaEXst4qibk7IfibPSNSkzsdpRiaonZtcrFO300niczDCT8nnMoRRMHFbsvGWAOZr33gXxicF55XcBslIm5oGraskLCPdd7Mg/0?wx_fmt=jpeg)

# 如何理解镜像频率？

原创

班班高
班班高

网络安全自学

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6nNyjd9QeAUdlJnqcbr4Ys8FkITF5IX4d9ER5WHB4uz0CSWlE3X4LMvu9yaZhib7zPDu1QEJQEveg/640?wx_fmt=gif)

**点击上方蓝字  关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC7SjNGMmDlqHKXEtpiaH6GxlKkhZA3ecMxLq3e1LiaV4pKn6nicfEXoCg3Ij97wdpUaCfoJRWw1u68mQ/640?wx_fmt=png)

什么是镜像频率？

      在理解镜像频率之前，我们需要先了解超外差接收机基本工作流程中的混频。

      超外差接收机接收一个频率为100MHz的电台。直接处理这么高的频率理论上可行，但在工程实践中对接收机内部的器件要求比较高，提高了接收机的成本。所以我们通常会把100MHz频率降为一个固定的、较低的“中频”（英文全称：Intermediate Frequency, 简称IF），这个降低频率的过程就叫混频，使用到的元器件叫做混频器。

**一、混频的过程**

      100MHz的信号进入混频器后，混频器把输入的100MHz信号(记为：f\_RF)和由接收机内部晶振产生的本振（英文全称：Local Oscillator）信号（记为：f\_LO）进行运算后得到中频信号，中频信号的频率通常为输入信号的频率减去本振信号的频率后取绝对值，即f\_IF=|f\_RF-f\_LO|。

     如果我们想让中频信号的频率是10MHz，因为100MHz (f\_RF)-90 MHz (f\_LO)=10MHz (f\_IF) ，所以接收机只需要把本振信号的频率 f\_LO设置在90MHz就可以了。这样我们就成功地把 100MHz 的信号搬移到了10MHz。

**二、镜像频率是如何产生的？**

      假设空中除了100MHz的真实电台信号外，还有一个频率为 f\_IMAGE 的干扰信号。这个干扰信号频率和本振信号频率之间的间隔也是10MHz，即|f\_LO-f\_IMAGE|=10MHz=f\_IF，如图1所示，在频率轴上，f\_IMAGE和f\_RF以f\_LO为中心呈左右镜像对称。因为我们已经把本振信号的频率 f\_LO设置在了90MHz，所以可计算出f\_IMAGE=80MHz，这个80MHz 就被称为镜像频率。

![什么是镜像频率？.png](https://mmbiz.qpic.cn/sz_mmbiz_png/0plbPNoicicKTJuX7MAl0oPpfnbA1T7qDzQ8AT7W9lPpRbrzmHYgJ1R8lyGwB3y4HNYkibtcVo0F1evLENOBHOmGicoTfUJBnegRCbVRvcswRx0/640?from=appmsg)

**图1 镜像频率和真实频率的关系**

**三、****镜像频率的危害**

      当80MHz的镜像干扰信号和100MHz 的真实信号同时进入混频器后，混频器都会输出10MHz 的信号，后续的中频放大器和滤波器完全无法区分这两个频率一样的信号哪个是真实的中频信号，它们会被当作同一个信号一起处理。最终导致接收到的电台信息里会混入干扰噪声，无法进行电台节目收听。

**四、****如何解决镜像频率干扰？**

      解决方法就是使用前期内容提到的镜像抑制滤波器。镜像抑制滤波器的任务就是在信号进入混频器之前，将80MHz的镜像频率滤掉，同时让100 MHz的真实信号通过。这个滤波器的设计难度取决于真实信号和镜像频率的距离，也就是 2 \* f\_IF。中频 f\_IF 越高，它们离得越远，滤波器就越容易做。但是中频也不能一直提高，否则会增加后续元器件的成本，在射频系统设计中，需要对这一点作出权衡。

**本节内容概括**：

![什么是镜像频率？.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/0plbPNoicicKREgDXq712YT1qYTrD2oHgp1cyiboUbRUvdn07icOP87AtViaA7yd9eRpaS9xcBEFfDaQ4CnQGHfxXB04VADNvqIS7xjd3wibSaO3g/640?from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KzC2TfrDajDdIvfvMXyFs0bcsf7sicEBZsoCfFotNF6HbcrIqyNKTXCnMLBzAR0n9NTK7bFKGdOlxZTgicYics35A/0?wx_fmt=png)

网络安全自学

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KzC2TfrDajDdIvfvMXyFs0bcsf7sicEBZsoCfFotNF6HbcrIqyNKTXCnMLBzAR0n9NTK7bFKGdOlxZTgicYics35A/0?wx_fmt=png)

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