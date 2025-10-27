---
title: 打破物理隔离：RAMBO侧信道攻击令人防不胜防
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512604&idx=2&sn=e28691514456eaaed77ba791576fd2c3&chksm=ebfaf53cdc8d7c2a02dccd185b89c58ddd28fe1eff746588cc7c1e93ff18b3a83b034ad31818&scene=58&subscene=0#rd
source: 安全内参
date: 2024-09-12
fetch_date: 2025-10-06T18:28:50.333607
---

# 打破物理隔离：RAMBO侧信道攻击令人防不胜防

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tcDvI4zyU6X6jfIAuticYiclY59WKTLCEX8iaA5jtFCnLMsAA7hayiagZ5yFkMZBn9UujFX7YqHgSmtQ/0?wx_fmt=jpeg)

# 打破物理隔离：RAMBO侧信道攻击令人防不胜防

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvYxDlS8tkjPhJkxEgduTcFPVlPPpeic11yjozEa5FPuDgad4iblEEuia2SQV22UdAOiaGDdaIk3icHmk9w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

从防御严密的物理隔离系统中窃取机密信息向来是黑客攻击的“圣杯”。近日，以色列大学的研究团队公布了一种名为“RAMBO”（Radiation of Air-gapped Memory Bus for Offense）的新型侧信道攻击方法。利用物理隔离系统中的内存组件生成电磁辐射进行数据泄露。这种突破性的攻击方式再次引发了人们对所谓高安全性环境（例如物理隔离系统）的担忧。

**物理隔离系统的新威胁**

物理隔离系统通常应用于政府机构、武器系统、核电站等高安全需求的关键任务环境中。这些系统与公共互联网及其他网络隔离，旨在避免恶意软件感染及数据盗窃。然而，尽管物理隔离，恶意软件仍可通过诸如U盘等物理媒介，或国家级攻击中的供应链漏洞，渗透到这些系统中。

RAMBO攻击便是利用这些恶意软件，通过操控系统内存总线的读写操作，生成受控的电磁辐射，并将数据传输至附近的接收设备。这种攻击方式不仅隐蔽，还难以被传统的安全产品检测或阻止。

**RAMBO攻击的工作原理**

RAMBO攻击的核心在于利用恶意软件在物理隔离系统中收集敏感数据，并通过操控内存访问模式，生成电磁辐射来实现数据传输。

这些电磁辐射信号被恶意软件通过开关键控（OOK）技术进行快速切换，进而形成“1”和“0”的二进制编码。该过程不会受到安全产品的主动监控，也无法被标记或停止。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvYxDlS8tkjPhJkxEgduTcFPqlSicXe3XTrcx6cHMdbuHuib7rET3YiaqszCxqFMPzhbV14P1texCT0wA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

*执行OOK调制的代码 来源：Arxiv.org*

研究人员还使用曼彻斯特编码来提升误差检测能力，确保信号同步，从而减少接收端错误解读的可能性。

攻击者可以使用低成本的软件定义无线电（SDR）设备和天线，截取这些调制过的电磁信号，并将其转换回二进制信息。这种方式不仅成本较低，还可以实现相对高效的数据窃取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvYxDlS8tkjPhJkxEgduTcFPKiaY20jPdibOJicWAodK4Uib6beVaiaVWoakcOic6iayiajAktrQicoeM5vH5XA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

*“DATA”的EM信号 来源：Arxiv.org*

**RAMBO攻击的性能与局限性**

RAMBO攻击的最高数据传输速率为1000bps，相当于每秒128字节，或0.125 KB/s。虽然这一速率不高，但足以窃取少量敏感数据，如文本、键盘记录和小型文件。例如，窃取一个密码仅需0.1到1.28秒，而窃取一个4096位的RSA密钥则需4到42秒。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvYxDlS8tkjPhJkxEgduTcFPKPMB90mBHTZ6kV5RuOQGaunGv5nLAT0Yhf2EZp8PLKX2a79ERDybjQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

*RAMBO攻击的数据传输速率  来源：Arxiv.org*

在实验中，RAMBO的传输范围最远可达7米，传输距离越远，数据传输速率越慢。然而，当速率超过5000 bps时，信噪比迅速下降，数据传输的有效性也大幅减弱。

**如何应对RAMBO攻击**

以色列研究团队在其发布于Arxiv的技术论文中，提出了多项应对RAMBO攻击及类似电磁辐射侧信道攻击的防御措施。这些措施包括：加强物理防御的严格区域限制、通过RAM干扰来阻断隐蔽信道、外部电磁干扰以中断信号，以及利用法拉第笼屏蔽系统的电磁辐射等。

研究团队还对RAMBO攻击在虚拟机内运行的敏感进程进行了测试，结果显示该攻击仍然有效。不过，由于主机内存与操作系统及其他虚拟机的交互较为频繁，这类攻击在实际应用中很可能被快速中断。

**总结**

RAMBO攻击展示了侧信道攻击的新潜力，即使是与外界隔绝的高安全性系统也难以避免类似威胁。这一攻击方式提醒我们，网络安全不仅仅局限于软件和网络层面，物理层面的威胁同样需要高度警惕。

参考链接：

https://arxiv.org/pdf/2409.02292

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：GoUpSec

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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