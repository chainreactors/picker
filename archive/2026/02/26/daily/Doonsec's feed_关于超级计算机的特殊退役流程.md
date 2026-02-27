---
title: 关于超级计算机的特殊退役流程
url: https://mp.weixin.qq.com/s/I7ZzJAbJV7LTA5WV-61L3Q
source: Doonsec's feed
date: 2026-02-26
fetch_date: 2026-02-27T04:05:39.292684
---

# 关于超级计算机的特殊退役流程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpeFlAQQkEmPPCyjFEEZwqBf08dwk7Wer1ad6rm16TpGPdtQUa9iaxQdYpdThkax6DmfQYibOEtGiaXWMUXUURs7956oGUxrRNMW0/0?wx_fmt=jpeg)

# 关于超级计算机的特殊退役流程

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

本文展示美国国家级超级计算机 “塞拉（Sierra）” 的退役全流程，同时揭秘了超算行业的服役规则、退役处置标准与行业未来发展趋势。

塞拉部署于美国劳伦斯・利弗莫尔国家实验室，服役周期 7 年，核心使命是为美国国家核安全管理局执行高保密级别的核武库模拟运算。

它由 IBM Power9 CPU 与英伟达 Volta V100 GPU 搭建而成，峰值算力达 94.64 千万亿次浮点运算 / 秒（PFlops），曾位列全球超级计算机 TOP500 榜单第二名，即便在退役前夕，算力仍稳居全球第 23 位。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDq22Nd5IjFZWYOqKw2nJtI5Dw7KbiatticnO87qImb3lFnyjuzibMyicicgg0Stc9daNVmLqVr5VChnF0kGfHYKL9qdPZ3VHiauJTx6s/640?wx_fmt=png&from=appmsg)

它与橡树岭国家实验室的 “巅峰（Summit）” 为孪生机型，美国政府为两台超算累计投入至少 3.25 亿美元。

**那么它为何退役。**

1、软硬件全面停服，核心组件已停产，IBM 停止对其搭载的红帽企业 Linux 版本提供官方支持，备件采购与运维成本急剧攀升；

2、算力代差彻底拉开，继任者 “埃尔卡皮坦（El Capitan）” 峰值算力达 1.809 百亿亿次浮点运算 / 秒（EFlops），性能是塞拉的 19 倍，继续维护塞拉的投入产出比已完全不具备经济性；

3、硬件故障率进入上升周期，贴合 IT 行业 “浴缸曲线” 规律，故障风险与运维成本持续走高；

浴缸曲线（Bathtub curve），又称U型曲线，是用于描述半导体产品随时间变化的瞬时故障率的通用曲线。该曲线以使用时间为横坐标、失效率为纵坐标，呈现两头高中间低的形态，反映产品从投入使用到报废期间可靠性变化的规律性特征。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDo5G6CEl0NCnPYfMqy1jpoTlLv2KVLKFgibK4CkXKHKT4hXFmQTicaQzdFjxk4uhVT05icfcS2RIkhxCD74yg6MaPalBFNejar5BQ/640?wx_fmt=png&from=appmsg)

4、美国能源部的资源分配逻辑，7 年是美国国家级超算的典型服役周期，有限的预算需全面向新一代超算倾斜。

涉密超算的特殊退役流程

关停超算，并没有一个醒目的红色急停按钮，也没有一个巨大的拉杆能一次性切断整机电源。当然，有人可以直接剪断电源线，但这绝非规范操作。

退役流程的第一步，是通过邮件向使用塞拉的科研人员发出预警，要求他们备份并保存好所有研究数据。随后，正式启动 “零备件更换” 程序 :不再为故障组件更换任何新备件。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrSkJV3eibQy2yPjEVFwvVpq7M5Kp0bYfzJovXQVGu02vyzPfwPSnoHLSwicuAxic5lcsd28vic6pciaF4SUaV0iaVcGKplkN2O4dbCk/640?wx_fmt=png&from=appmsg)

退役工作分阶段推进，最先关停的是计算节点与机架交换机，管理节点则留到最后处理，因为全程都需要它们维持系统的基础运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDp8FyKQew4DxfMX8rSBFhrOoX5Xqe7pME3kvDYotibMPOQXia0AerFmdKhBDYvKCQNhzibAI3q7G8Uqczu1hibgW91c0Lnia86sCjKg/640?wx_fmt=png&from=appmsg)

整个流程包括：运行专用脚本，以数字化方式关闭计算机系统，随后切断所有硬件电源开关。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpEg4OtH6EibhEZW3dFvXrWF1aGibZ2PREkJgwib7Mh4mtBmdxeqYBcNNf7pQicFqmiccJl9MQ20pvyIJKtCV7UU1MxBCvbFPTwdibLk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqqkYuYoJxia4ZGAzq1daHeHJk8DOuJJ9BKQpT1QEqKurPmWjXKKxT0cX7FJYJkflmTibYVLzWOndIxXOuZyF7OScKFNbj1Mt4OA/640?wx_fmt=png&from=appmsg)

此外，还有一套完整的冷却水排空流程。塞拉运行时会产生极高的热量，因此实验室会通过地板下的管道（如下），每分钟循环数千加仑的冷却水为其降温。随着系统关停，这些冷却水必须全部排出。安全人员会先对水质进行检测，确保其 pH 值符合环境健康标准后，再进行后续处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoo4eAOlzveXAv2ibpAuqIy88g7mxGhfVdqcmdf52GvguGsd5apO5K9PWf7qibldcxR7OL1BeZYmlumNHvR4jVhGpTiaCeWic1Mq5Q/640?wx_fmt=png&from=appmsg)

值得一提的是，超级计算机也可以有体面的退役方式。有些最终会被捐赠给其他科研机构或博物馆，也可以被拍卖，就像美国总务管理局在 2024 年，拍卖了硅谷图形国际公司制造的千万亿次级超级计算机 “夏延” 一样。

但现实是，市场对老旧超级计算机的需求极低，绝大多数最终都会被拆解成零件出售。早在 2013 年，新墨西哥州就因无人对整机感兴趣，选择将州政府资助的 “恩坎托” 超级计算机拆解售卖。阿贡国家实验室曾试图将曾位列全球第三的 “无畏” 超级计算机的大部分组件，捐赠给其他实验室和一家计算机博物馆，但应者寥寥。最终，除了少数机架捐赠给北卡罗来纳州立大学外，“无畏” 的其余部分全部被回收处理。

而塞拉，正在经历大规模的回收与销毁。毕竟，它的设计初衷是支撑美国的核武库研发，机身内存储了海量的机密数据，这台机器绝不能被随意处置。与之相反，塞拉必须被彻底拆解销毁，杜绝任何组件被部分 “复活”、进而导致国家机密泄露的可能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpibcpiaxmea0fu4uia1NWrb5tgvnTyulz3iaXAYkAAdLXyh54zRejkzHxQ6yNmWy3JZxibEnRxzzhqE3QJiaBCOJIXu4vT51F92sIAI/640?wx_fmt=png&from=appmsg)

这个过程极为严苛。工作人员佩戴手套，逐一取出各个计算节点，拆除分布在机身各处的锂离子电池（这些电池将被送往专业的电池回收商处理）。其余组件，比如系统主板、处理器，以及支撑塞拉的机架骨架，将被送往异地进行粗粉碎处理。任何无法回收利用的组件，在经过严格的数据安全检测后，都将被彻底销毁。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrDA3myHAQJKoy1pfZPKNjEuWrvXluOhmq4bMYOq0IjfbF1ccpR6lcBFSQAOYzdQib4XYj1m9LXibQTESbH6HDkcYqLr844n6q5E/640?wx_fmt=png&from=appmsg)

而塞拉的闪存组件，即便断电也能长期存储数据，因此需要被研磨成极细的粉末。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoY7TPiabpyN5FvZt2H0BXCaT4sPibKjA2nSnC3pvNFwzYquD0q4kINexdaV8Oarr6PN83RCOusYk4w4k34CgbLiaMUibGOia2hhmIE/640?wx_fmt=png&from=appmsg)

同时，为了处理所有磁性硬盘，实验室在楼下配备了一台经美国政府认证的专用消磁器。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDq8bBr0VH8e14GDlDK3YppLs4RSGECIAAYU3lfvGqAlXw21Z45X4iaPgiauTnCBUsz2rB30fE53kbeIB1icXYPWQACNeBiawWJeshk/640?wx_fmt=png&from=appmsg)

这台设备利用永磁体（一种无需供电即可产生强磁场的材料），彻底清除磁性组件上的所有数据。这块磁铁的磁力极强，甚至能吸走附近的信用卡，干扰精密的医疗设备。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDobMTicDsyMBCsg8tmBeASA7JnKatagzBJTkjTsKib7xIvOctsfVJlA2uDruCic99Me3xJbu3dOaYdYib95xFOoSACDyK5LRarXxL0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDreDUs9tftgMwbAfwd7GKaMWqWc1EfvQXvgmc8DEjW7ktMV5qUicabSlfiaIqIvulx6JLiaoULurvJPVe6kx5HLqRSnIezZgvgWdE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDo7Tbq0s7LaTXUrGYXG3Tbh8aNRxwnonfmeUbTN4R5fAxJwYo4drPibTJyhKuzOyCHiaZQpAgy2COO56xJvg3GVjQnwDloe5as5I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqC1TiaIclK5XlQkpUEWq5U9PjtOsKqbJnfrGsddKm0LvNtU8M4RvmDp2PapE1TSict1QpOnwqXiaXDVhsqTZwoweLM7O9JxfbupQ/640?wx_fmt=png&from=appmsg)

整个销毁流程需要数月时间，截至本文刊发时，塞拉的拆解工作已基本完成。最后一步，电工将彻底切断它的供电线路。

除了地板下的冷却与供电系统，以及实验室为保护超级计算机免受地震影响搭建的抗震基座外，它将彻底消失。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqHpn6vIuIT6fzs5ibiarWRCibmLa8sSlnAghIt8gFiboMZHpM6ddfw4bib4Vm9j5rvs92TC6g6bzRO8h3GZtjbT08d5Q1ud4h5pQko/640?wx_fmt=png&from=appmsg)

而这些保留下来的基础设施，将用于支撑下一代超级计算机的部署。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrC834CKF5Xj2JhGrbvUgZ972TiaJYLfrr78mKlKS0ibAngsG0Pu6Vxu7mdb24YnJDjiab2TEB5Qibboc53icM36GH3t1owA0vN6Nr4/640?wx_fmt=png&from=appmsg)

有人在接受采访时表示，当机器被拆解报废时，他们确实会感到难过。也有人强调，真正会感到不舍的，是那些实际运行模拟程序的用户，而非运维的 IT 部门。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqXcDtTDDe3glQdO95RiaBJWPcb3wWiccKxmesdv7EWJdIa6qQIv7lPOIJUerU1ibdC9JG4Qico89ZjAlLiaXREv1T5O4K7qKMdKmQk/640?wx_fmt=png&from=appmsg)

“我从来没有对任何硬件产生过情感上的依恋。” 桑迪亚国家实验室的系统工程师拉里・巴卡说道，在他的职业生涯中，他已经打包拆解过几十台计算机。参与创办 TOP500 榜单的超级计算专家霍斯特・西蒙也认同这个观点。“尽管单台超级计算机终会落幕，” 他说，“但整个超算领域，依然在蓬勃发展。”

但这样的蓬勃发展，终有一天可能会迎来终点。

专家表示，至少有两种可能，会让超算的迭代逻辑彻底改变。

一种可能是，未来某一天，新硬件与旧软件、新软件与旧硬件的兼容适配变得无比简单，届时我们不再需要打造全新的超级计算机，只需在同一套系统上，持续更换性能更强的组件即可。

而另一种可能性则没那么乐观：我们可能再也研发不出性能更强、速度更快的芯片，无法再证明打造新一代整机的必要性。

很多人都担心，摩尔定律的放缓，已经成为不争的事实。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqueyZqpNRgdx4epMqlMWBbp4dPyNbJ9UZmlLvSHsuAt97hNGtTl35pSOPa6AoadRLa9bwWbjZQRSwWKLKkMlMcLJMXDneLjw8/640?wx_fmt=png&from=appmsg)

不过，塞拉的退役，终将为另一台超级计算机让路，而这台新机器，几乎肯定会部署在它曾经所在的楼层。

\*图片均来自wired报道《Why Sierra the Supercomputer Had to Die》 的Balazs Gardi拍摄。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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