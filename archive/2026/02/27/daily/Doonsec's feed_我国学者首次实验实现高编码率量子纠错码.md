---
title: 我国学者首次实验实现高编码率量子纠错码
url: https://mp.weixin.qq.com/s/cdNuCACI3sjBjJe4S7JDzg
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:56:22.195499
---

# 我国学者首次实验实现高编码率量子纠错码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FNlvhjUaDTO8TZkNEDX29bYyr7FOOteMxXTheQIUEF0v2zxnlZNZ1yIULl2N74rmjNpxKHzSRLedOM2zKsia0PHaDFyyCN48R3pqHST0ty4Y/0?wx_fmt=jpeg)

# 我国学者首次实验实现高编码率量子纠错码

信息网络安全杂志

![]()

在小说阅读器中沉浸阅读

清华大学交叉信息研究院邓东灵课题组与浙江大学物理学院王浩华、宋超研究组等合作，首次在具有长程耦合器的超导量子处理器上实现了高编码率双变量自行车码（Bivariate bicycle codes）的量子纠错实验演示。该成果论文《低开销量子纠错码的演示》（Demonstration of low-overhead quantum error correction codes）近日以Article的形式在《自然物理》（Nature Physics）杂志发表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FNlvhjUaDTMIGXaur9vZGgsXicicrc1Q6iajDJMEoAKjZMGiaKDr42In2RT4Vl47r4r8sAPs40GkIWvpzdmUwicCMAXILeOrafnQb6F4pia6OC07A/640?wx_fmt=png&from=appmsg)

图1：昆仑量子处理器架构图以及双变量自行车码的非局域稳定子提取线路

通过量子纠错技术降低逻辑量子比特的错误率，是实现大规模容错通用量子计算的一条关键路径。长期以来，表面码凭借其硬件友好的近邻耦合需求，占据着容错量子计算的主流地位。然而，表面码的低编码率导致其在扩展性上面临着高昂的硬件资源开销。在此背景下，发展高编码率的量子低密度奇偶校验码被视为降低资源开销的重要路线。特别是2023年提出的双变量自行车码，理论表明其仅需表面码约十分之一的物理比特开销即可达到同等纠错性能，为低成本量子纠错指明了新方向。

尽管双变量自行车码理论优越，但其硬件实现却面临着极大的挑战。要在二维平面的量子芯片上构建非局域的长程连接，且要并行地在这些复杂的长程耦合上实现高保真度量子门，其工程实现的难度明显高于仅需近邻连接的表面码。

针对这一挑战，邓东灵课题组与王浩华研究组通力合作，协同设计并制造了名为“昆仑（Kunlun）”的32比特超导量子芯片。该芯片在二维近邻连接的基础上引入了额外的长程耦合结构，以支持双变量自行车码所需的非局域稳定子测量。为攻克长程耦合带来的布线交叉与寄生耦合等工程难题，团队在芯片制造工艺上进行了针对性优化，在每个长程耦合器上引入多达15个空气桥跨越结构。这一关键工艺不仅解决了复杂的拓扑布线问题，而且有效抑制了串扰。实验标定结果显示，“昆仑”量子处理器的单比特门与两比特门的平均并行保真度分别达到 99.95% 和 99.22%。

![](https://mmbiz.qpic.cn/mmbiz_png/FNlvhjUaDTMECIvawl8HlceeOzJbYNhNbNk4ibeXZfM4qgu0Zk1njfKFEjFQJX03DOpcfcFxoRj5IuSTbRZAHLz4OZvhRib3XEVa3ujmjdmes/640?wx_fmt=png&from=appmsg)

图2：[[18,4,4]]双变量自行车码的部分实验结果图

基于“昆仑”量子处理器，团队自主设计并在实验上演示了两种双变量自行车码：[[18,4,4]] 码和 [[18,6,3]] 码。前者利用18个数据比特编码4个距离为4的逻辑比特，后者编码了6个距离为3的逻辑比特。通过执行高效的非局域稳定子提取线路，团队成功演示了多轮量子纠错。实验结果表明，[[18,4,4]] 码和 [[18,6,3]] 码的平均逻辑错误率（按每轮、每逻辑比特统计）分别为8.91% 和 7.77%。此外，数值模拟预测，在所采用的噪声模型与解码设定下，若能将当前芯片的物理操作错误率降低至现有水平的一半，则可跨越双变量自行车码的纠错阈值，为未来突破盈亏平衡点奠定了基础。该工作在审稿阶段获得了同行专家的高度评价， 称其为“迈向容错且低开销量子计算重要而充满原创性的一步”。

该论文通讯作者为清华大学交叉信息研究院邓东灵长聘副教授，浙江大学物理学院宋超研究员与浙江大学物理学院王震研究员。上海期智研究院高级研究员鲁智德、浙江大学博士生王可、张川宇为文章共同一作。其他作者包括浙江大学超导量子计算团队部分其他成员，清华大学交叉信息研究院博士后孙正之、李炜康，清华大学交叉信息研究院博士生叶奇、蒋颸、马一瑄，以及波兰科学院玛丽·居里ERA Fellow沈培鑫博士。

该项目得到了国家自然科学基金，清华大学，合肥国家实验室，以及上海期智研究院等支持。

来源：清华大学交叉信息研究院网站

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=qnylxjok&tp=webp#imgIndex=2)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=fbknkhlb&tp=webp#imgIndex=3)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&randomid=23elspay&tp=webp#imgIndex=4)

我们在不断努力和完善中，期待您的关注和支持！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

信息网络安全杂志

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

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