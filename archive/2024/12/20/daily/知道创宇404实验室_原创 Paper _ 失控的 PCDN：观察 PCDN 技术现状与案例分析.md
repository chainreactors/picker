---
title: 原创 Paper | 失控的 PCDN：观察 PCDN 技术现状与案例分析
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650990259&idx=1&sn=b4d341016fe7340aab15767f5c7a78c1&chksm=8079a481b70e2d97b577e1f25fa4525f30179dbd2a6f6905ab10935c096fde86e61d3ea63ea5&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-12-20
fetch_date: 2025-10-06T19:38:57.623573
---

# 原创 Paper | 失控的 PCDN：观察 PCDN 技术现状与案例分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztIYKbgJBLUDXtxIPnicNUkTMtZWKTzA4umkDRUOzicWZM5k90pMr3CVMw/0?wx_fmt=jpeg)

# 原创 Paper | 失控的 PCDN：观察 PCDN 技术现状与案例分析

原创

404积极防御

知道创宇404实验室

**作者：******知道创宇404积极防御实验室****

**1 背景介绍**

参考资料

2024年10月，知道创宇404积极防御实验室监测到某客户网站流量异常，疑似遭到CC攻击。经过分析，本次CC攻击疑似为PCDN厂商为了平衡上下行流量对客户网站视频文件进行的盗刷流量行为。

在调查分析的过程中，我们发现PCDN技术的发展正逐渐失控。为了深入研究，我们对PCDN技术现状及其背后的产业链进行了调查和分析，并对本次CC攻击的发起者进行溯源分析。

**2 PCDN现状**

参考资料

### **2.1 PCDN介绍**

PCDN（Peer-to-Peer Content Delivery Network，即P2P内容分发网络）是一种结合了P2P技术和CDN技术的内容分发加速网络。其核心思想是利用用户设备的闲置带宽和存储资源来提供高效、低成本的内容分发服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztLWpk0CtpFiaaFCORXHNyktKib3WlC10KHTtrFNVxHtt6tmaRmd8TYNZQ/640?wx_fmt=png&from=appmsg)

与传统CDN需要在数据中心机房部署CDN服务器节点不同，PCDN网络直接将用户终端作为PCDN节点。用户访问时可以直接从其他用户处取得数据，大大降低了对数据中心机房资源的需求。

但是PCDN也存在较大的弊端。PCDN的海量流量对电信运营商骨干传输网络形成了巨大压力。由于用户的宽带通常按月峰值限制计费，而不是按流量计费。因此，在未达到峰值前，用户使用越多，电信运营商承担的成本越高。

以上海地区同样至少拥有100Mbps带宽的家用套餐和企业宽带为例。中国电信拥有1000Mbps下行、100Mbps上行的家用套餐仅需229元/月 [1]。拥有100M上下行对等带宽的企业宽带却需要1910元/月 [2]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztbpnMYeDpXiaS2hO1zabzG6gRzA4eK7rc9QkwGYjWpUPHLOwBPicdLWvw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztEh9yUHWicLIKjHX5taTicYBlcYCgEHQF5ibrxH66RU9bImr7TelNkZuTA/640?wx_fmt=png&from=appmsg)

两者间巨大的成本差异，让互联网厂商积极推动PCDN技术的落地。PCDN技术利用家用宽带的资源，让大量本该走企业宽带的流量，走了家庭宽带的路线，极大的降低了企业用户的成本。

### **2.2 PCDN厂商与运营商的对抗**

PCDN技术推广固然使企业降低了成本。但也在一定程度上增加了运营商的成本，影响了他们的收益。自今年年初起，各地运营商加大了对利用家用宽带作为PCDN节点行为的打击力度。PCDN节点的上行流量远大于下行流量，正常家用宽带下行流量远大于上行流量，部分运营商通过这种上下行流量间比例的差异来鉴别PCDN节点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztR7Eibp7ZGL52UxJ75plHnPn1LoajJJ6c7Fhx5b20Rhb2Y9f3fbjyuiag/640?wx_fmt=png&from=appmsg)

PCDN厂商为了规避电信运营商的检查，必须将PCDN节点的流量特征伪装成和普通家用宽带流量特征一致，使上下行流量对等。于是PCDN厂商们开始大肆盗刷下行流量。为了高效地刷取下行流量，PCDN厂商将盗刷目标对准包含大量资源文件的BT节点和包含镜像文件、安装包、音视频文件资源的各类网站。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztOibOsicMwAgRVyBY1vOB02r0uFLgc85Zmp1bia6FLtCibQ2J64gvHObVicg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdzt8AEnHLFgu23ic4F91aKH4QjaF85TiaTcFBW710ySrVC7TBojzbYuHpvA/640?wx_fmt=png&from=appmsg)

PCDN厂商盗刷下行流量行为具有以下几个特点：

1. 攻击IP多为家用宽带，且多为同一省份：当某一地区的运营商对PCDN节点进行打击时，PCDN厂商便会控制当地PCDN节点刷下载流量伪装成普通家用宽带；
2. 刷取时间较为固定，具有相对固定的User-Agent头、Referer头；
3. 刷取的目标多为数据量较大的资源文件。

### **2.3 PCDN各利益方**

纵观整个PCDN产业，可以发现其中存在这么几个角色：

1. 想要获得低价高质内容加速服务的互联网厂商；
2. 搭建PCDN网络赚取利益的PCDN厂商；
3. 出卖自身带宽资源和计算资源赚取赏金的PCDN赏金用户；
4. 需要维护自身利益的运营商；
5. 需要内容加速服务或利用漏洞构建PCDN节点的黑灰产组织；
6. 提供盗刷教程或服务的潜在黑灰产从业者。

其中，PCDN厂商和PCDN赏金用户因为利益基本一致，需要通过利用家用宽带廉价带宽资源获取利益，可以算作同一角色（下文统一使用PCDN厂商进行指代）。

提供直播、视频等服务的互联网厂商需要通过使用廉价的PCDN流量，降低自己的成本。他们或在自己的客户端内建PCDN节点，或购买PCDN厂商的流量。如爱奇艺客户端启用HCDN技术（结合了传统CDN和P2P网络技术的内容分发网络），用于加速用户体验 [3]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztM1MeEoPTciaGaEnXnib0XzCOOIz9uSOjpw3IiaNrICK9LIcPwXttibvIBQ/640?wx_fmt=png&from=appmsg)

PCDN厂商通过自行搭建或赏金招募获取PCDN节点，将PCDN流量资源卖给其它需要的厂商。他们拥有对PCDN节点的控制权，实现对PCDN网络资源的合理调度。如阿里节点共享平台招募节点，需要用户给予登录权限和重置口令 [4]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztZt68NljcFnJ5LoVqZ7JRdf6QGI4N4oEKh9oaMkWibkm2BHsKricKib1gg/640?wx_fmt=png&from=appmsg)

我们统计了如今市面上体量较大的70家涉及PCDN业务的厂商，发现其中67家使用现金作为赏金，3家使用积分（积分可用于兑换现金和礼品）作为赏金，用于招募PCDN节点。PCDN赏金用户通过在本地部署相关软硬件设备赚取PCDN厂商的赏金。PCDN厂商通过这种招募方式实现快速部署PCDN节点，获得更多流量资源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztkaLFX6dUHejaZq0aGtanZTJy9ib7DiaG5I7mjNh4Qia00QAVO8jUUxfYg/640?wx_fmt=png&from=appmsg)

运营商一方面因为提供直播、视频业务的互联网厂商对传统CDN需求的降低，营收受到影响。另一方面，因为家用宽带用户搭建PCDN节点，造成骨干网络流量增加，运营成本上升。再加上今年三大电信运营商开始集团内部跨省流量结算 [5]，各地运营商必须加大对PCDN节点的打击力度才能维持自己的收益。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztCVNxBhqkIMsAo9wiclkNN8PCmdbibfYzuQvflHDa8tgQ6GKDibCb41N6A/640?wx_fmt=png&from=appmsg)

2024年初，奇安信X实验室发布了一篇名为《笼罩在机顶盒上空的阴影：揭开隐蔽8年黑灰产团伙Bigpanzi的神秘面纱》的文章 [7]。里面介绍了一个使用机顶盒漏洞将受害者变为PCDN节点的团队。利用PCDN技术搭建内容分发网络能够大大减少机房成本，同时也能为黑灰产组织控制下的终端提供更好的变现方式。由此可见，黑灰产组织利用PCDN技术来进行违法行为已成为趋势。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdzt1NHdQ4W2NwdmgsuP20OX2iaXGMrXcI6MicsHVoiasGONbVrGHMaxEibRdQ/640?wx_fmt=png&from=appmsg)

获得了利益的PCDN厂商为了规避运营商的查封，大量的盗刷其他网站下行流量，对其他网站运营者造成了极大的损失。为了迎合PCDN厂商逃避运营商检测的需求，闲鱼、淘宝等平台上甚至出现了大批提供付费盗刷下行流量服务/教程的商家。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztQgo6nGoHGXYGeLEMs8nBwiaPkiao0XibqAdiblH4sIic2Vmu6fAgpVPIhpQ/640?wx_fmt=png&from=appmsg)

这些商家的行为直接违反了《中华人民共和国网络安全法》第二十七条规定的内容 [8]，使他们自己成为了事实上的黑灰产从业者。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT1rZQMP9F5354BvOcwtqdzt8C9Du5vHqNIt6cbpnRJMMqTYUicUWgYrOia8I086xSMLKuyTsX6kg6Jw/640?wx_fmt=jpeg&from=appmsg)

**3 事件分析**

参考资料

互联网厂商对廉价内容加速服务的需求促使了PCDN产业快速扩张，这种快速扩张又严重影响到了运营商的利益。运营商对PCDN节点网络的打击又促使PCDN厂商疯狂盗刷下行流量。而这种盗刷下行流量的行为，又导致了此类CC攻击的频繁发生。

### **3.1 被攻击目标分析**

为了更加全面深入的分析此次CC攻击事件的影响，404积极防御实验室依托知道创宇云防御平台对2024年10月03日00：00：00 至2024年10月13日00：00：00的数据进行全量分析，共发现180个域名、1127个URL被盗刷流量，累计被访问51903872次，被盗刷35.89TB流量。根据计算，如果没有接入防御平台，上述域名将被盗刷8076.73TB流量。防御平台过滤了99.56%的恶意流量，有力的维持了上述网站正常运行。

被攻击的180个域名中，有90个域名属于政府机关、38个属于私营企业、26个属于国企单位，分别占总体的50%、21.11%和14.44%。属于政府机关和国企单位的116个域名，累计被访问37083261次，被盗刷31.75TB流量，占总访问次数的71.45%、总访问流量的88.46%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztCItuM1f5nrmyy0DjRy193oAwQv1HOcxch8wRQg0Jxl2zDFpiatqxNfg/640?wx_fmt=png&from=appmsg)

统计被攻击的URL，发现被盗刷次数最多的是视频（mp4）文件，共计33904968次，占总次数的65.32%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztcOelESt0U2pavMUCg2CnmTibapmnJS2FZjNcjOI1KIgsicd2VY2h79Kg/640?wx_fmt=png&from=appmsg)

视频类型文件通常具备文件体量大、访问限制少等特点，是PCDN厂商盗刷下行流量的首选目标。统计周期内，视频（mp4）文件累计被盗刷28.19TB流量，占总体的81.32%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztzQjGrS5MIa4xA9wBaT4XRGYpDz2FQGyRQUnicIjrLqVZwrMian9GyNew/640?wx_fmt=png&from=appmsg)

### **3.2 攻击IP分析**

对统计期间内访问IP进行分析，共得到1362个攻击IP。累计产生33979894次访问，12.71TB访问流量。

对这1362个攻击IP的归属地进行分析，可以发现这些IP大部分来自广东和山东，分别占总体的34.5%和27.8%。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztaOBYg41iaib5bfXOxRNahz8Z7ZFwENOtT8NdT1y6RxFicTLhkwKgSORLg/640?wx_fmt=png&from=appmsg)

被同一家PCDN厂商控制的一组PCDN节点，为了方便管理、盗刷下行流量，它们应当具有相似的访问频率和归属地。结合攻击IP的访问频率变化和归属地进行分析，可以得到以下两组IP，这部分IP之间具有相似的访问频率变化趋势和相同的归属地。故判断以下两组IP是由专业的PCDN厂商控制的。

| 序号 | IP列表 | 属地 | 访问频率 |
| --- | --- | --- | --- |
| 1 | 182.xx.xx.13,182.xx.xx.16,182.xx.xx.17,182.xx.xx.18 | 中国 山东 青岛 | 该组IP的访问主要集中在12：00~24：00 |
| 2 | 182.xx.xx.10,182.xx.xx.15,182.xx.xx.19,182.xx.xx.2,182.xx.xx.20,182.xx.xx.21,182.xx.xx.3,182.xx.xx.4,182.xx.xx.42,182.xx.xx.43,182.xx.xx.44,182.xx.xx.46,182.xx.xx.5,182.xx.xx.50,182.xx.xx.51,182.xx.xx.52,182.xx.xx.53,182.xx.xx.54,182.xx.xx.55,182.xx.xx.56,182.xx.xx.57,182.xx.xx.58,182.xx.xx.59,182.xx.xx.6,182.xx.xx.7,182.xx.xx.70,182.xx.xx.71,182.xx.xx.8,182.xx.xx.9 | 中国 山东 青岛 | 该组IP的访问主要集中在00：00~20：00 |

联动创宇安全智脑对这两组IP进行分析，发现其全部威胁等级全部为低，运营商均为电信，且均带有HTTP代理标签。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1rZQMP9F5354BvOcwtqdztZgbic56CBlfOxoHXO9tacctPEkVjrmYM7Fv00OyVzSDlV0U3nBoqOZQ/640?wx_fmt=png&from=appmsg)

| IP | 威胁等级 | 标签 | 地理位置 | 运营商 |
| --- | --- | --- | --- | --- |
| 182.xx.xx.9 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.8 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.71 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.70 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.7 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.6 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.59 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.58 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.57 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.56 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.55 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.54 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.53 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.52 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.51 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.50 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.5 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.44 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.43 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx.xx.42 | 低 | HTTP代理 | 山东 青岛 | 电信 |
| 182.xx...