---
title: 2022年全球高级持续性威胁（APT）研究报告
url: https://mp.weixin.qq.com/s?__biz=MzU5MjEzOTM3NA==&mid=2247491759&idx=1&sn=c8e4a1e23fdf7a1dec6c470d9289d0cb&chksm=fe26e5aec9516cb85de2150cac8e029a979a4d7ed2a4aa33bd4861f1c06a2be4db6a6d3a5fdb&scene=58&subscene=0#rd
source: 三六零CERT
date: 2023-01-19
fetch_date: 2025-10-04T04:18:11.145536
---

# 2022年全球高级持续性威胁（APT）研究报告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PpxR19tHoNneibsBZeqUOoq3t9YH0X5WSGy4Jp3kOiaUf3ia0VM5SnTxhxDDT3K7gkDufzO4S9JII0xA/0?wx_fmt=jpeg)

# 2022年全球高级持续性威胁（APT）研究报告

三六零CERT

以下文章来源于360威胁情报中心
，作者高级威胁研究院

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6ZK2DRam9aQ0pxBMyaibQ7dQAv6FGxgBwRibZZUkRlJB4A/0)

**360威胁情报中心**
.

360威胁情报中心是全球领先的威胁情报共享、分析和预警平台，依托360安全大脑百亿级样本，万亿级防护日志等海量安全数据，整合360漏洞挖掘、恶意代码分析、威胁情报追踪等团队的安全能力，产出高质量的安全威胁情报，驱动安全的防御、检测和响应。

**2022年高级持续性威胁概****览**

在经历了新冠肺炎疫情肆虐，当今世界正处在大发展大变革时期。俄乌冲突爆发、全球经济衰退加之国际间各种力量的较量，使得国际局势日益错综复杂。2022年全球高级持续性威胁（APT）形势依然严峻。全年全球网络安全厂商公开发布的APT报告累计742篇，报告中披露的攻击活动涉及APT组织141个，其中首次披露的APT组织54个，均比2021年明显增加。全球范围内APT攻击活动依然紧跟政治、经济等时事热点，攻击目标集中分布于政府、国防军工、教育、金融等行业领域。

依托自身“看见”的能力，360已累计发现了51个境外APT组织，监测到5800多起针对中国的网络渗透攻击。2022年，360高级威胁研究院捕获到境外新组织：APT-C-63（沙鹰），另外在全球范围内率先监测到APT-C-06（DarkHotel）组织利用Firefox浏览器的2个在野0day漏洞（CVE-2022-26485、CVE-2022-26486）针对特定目标进行水坑攻击。这也是2022年国内唯一一家捕获APT攻击活动中利用0day漏洞的安全厂商。2022年全球APT组织利用0day漏洞展开攻击活动的增长趋势放缓，但仍处高位。

2022年2月24日俄乌冲突爆发，成为全球关注的焦点。俄乌冲突期间，与俄乌冲突相关的APT攻击、大规模DDoS攻击、黑客组织网络攻击、网络信息舆论对抗等一系列网络攻击和对抗活动，将网络空间战争形态展现在了世人面前。网络空间已经成为俄乌间冲突对抗的重要战场，在军事冲突之外产生着愈发深刻的影响。

2022年是我国“十四五”规划的第二年，在全面建设社会主义现代化国家新征程中，一批5G、工业互联网等新基建项目扎实推进，为数字经济发展开拓新空间、增添新动能。新基建的背后是产业、经济、政府、社会的全面数字化，而数字化安全将成为发展数字经济、建设数字中国的底座，成为新基建的安全基建。

通过2022年全球高级持续性威胁态势分析看，我国数字化转型和自主可控领域的发展面临更加严峻和复杂的网络威胁形势。需要网络安全从业者保持网络空间常态实战化的状态应对网络空间的攻防对抗，不断提升我国网络安全和数据安全保护能力，保障国家网络空间安全。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrKZ499HubWo60UNCj0vHA4DalaZMgGsMftzwtwfadeNic6cZOnetkDL0dWKuzT5Ir9olgG7OX1v6Q/640?wx_fmt=png)

2022年全球典型APT组织分布

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrKZ499HubWo60UNCj0vHA4b2RffcpEo6PGh2s5eHyzKHibvNEeqeJFRnHpkyEibqdtVyX1EsFITPkA/640?wx_fmt=png)

2022年针对中国地区TOP10境外APT组织

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrKZ499HubWo60UNCj0vHA4nBiabZDHhtHChtqqzudslWyHJDgkBFiajxCTY8jKYdia4Ckub3dAFouJg/640?wx_fmt=png)

2022年中国地区受APT攻击影响行业分布

**2022年APT攻击态势总结**

* APT攻击利用0day漏洞的攻击活动增长势头放缓，但仍处高位。2022年APT组织在0day漏洞的利用上呈现出利用0day漏洞修复不全或者0day漏洞变种发起攻击的趋势，同时需要关注APT和网络犯罪组织利用Log4j2漏洞展开的网络攻击。
* APT组织针对移动平台私有化武器趋势显露，2022年，针对iOS平台的攻击活动保持活跃。
* 2022年，APT组织针对我国重点行业领域的攻击活动仍旧保持较高热度，360高级威胁研究院监测到，2022年针对中国发起的攻击活动共涉及14个APT组织，政府、教育、信息技术、科研和国防军工等15个行业领域依然是APT组织攻击活动主要的目标领域。
* 2022年APT组织涉及挖矿勒索攻击、窃取加密货币等形式的攻击活动持续被披露，呈现不断上升的趋势。APT组织展开勒索攻击或窃取加密货币攻击活动的真实意图，既存在本身以牟利为目的，也包含利用勒索加密攻击做真实攻击目的掩护。

**关键威胁形势分析**

* 2022年俄乌冲突期间，APT攻击急剧增加，地缘归属东欧的APT组织异常活跃，网络攻击活动也不断上演。与此同时，APT组织利用正在进行的俄乌冲突话题作为诱饵展开的定向攻击活动不断被披露。
* 面对传统网络安全强国在网络安全领域常态化的攻击渗透这一实际威胁，需保持网络空间常态化战时状态思维，应对网络间的攻防对抗，来保障国家网络空间安全。
* 国与国之间的网络对抗愈演愈烈，成为了国家间对抗的重要形式。一系列网络犯罪组织逐渐将以往的“技术对抗”不断扩展到“舆论对抗”、“舆论造势”。
* 在2022年APT组织针对我国展开的攻击活动目标中，包含我国国产化操作系统和自主软件供应商，显示出了攻击活动瞄准我国自主可控领域发展的趋势。
* 在数字化转型进程中，网络安全威胁风险日益凸显，数字化转型面临更加复杂多样的网络威胁，网络威胁或将超越传统安全威胁，成为数字时代最大的威胁。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrKZ499HubWo60UNCj0vHA4cY2Y9BS2Uynf8pN05ibBelle9wa20XntKY8vLnxlXfpogRPLsIenh9g/640?wx_fmt=png)

（完整版报告请点击下方“阅读原文”查看）

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Ic3Rgfdm96ehiaKaNLl4R2jEAKbwYWArdHJBHLPsfvia7icjTiaGrgEvu6D11iaH6NLKSibIZxPSaiaiaQE0O5WfrpicKcQ/0?wx_fmt=png)

三六零CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Ic3Rgfdm96ehiaKaNLl4R2jEAKbwYWArdHJBHLPsfvia7icjTiaGrgEvu6D11iaH6NLKSibIZxPSaiaiaQE0O5WfrpicKcQ/0?wx_fmt=png)

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