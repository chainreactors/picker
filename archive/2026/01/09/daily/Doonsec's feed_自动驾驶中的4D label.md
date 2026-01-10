---
title: 自动驾驶中的4D label
url: https://mp.weixin.qq.com/s/AXoKY7322o4bH_xThS4P1Q
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:21:52.230739
---

# 自动驾驶中的4D label

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWiawb5K9v6usiajw9Pwz9jGIyNxCIibw9BDqvaVibzovibbSiccvx5DN5zsjQ/0?wx_fmt=jpeg)

# 自动驾驶中的4D label

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

**01**

**什么是BEV感知**

回顾自动驾驶感知的发展历程，先是早期的单目2D特征，然后到单目3D特征，再到多相机的鸟瞰图BEV特征和占据栅格特征，感知范式不断迭代，算法能力也越来越强，当然对算力的需求也越来越高；

* 单目3D特征（Monocular 3D Features）是指从单张2D图像中提取的、能够表示三维空间信息的特征。这些特征使得计算机能够通过单一摄像头推断深度、形状和空间关系；
* 鸟瞰图BEV特征

**1.1 BEV出现之前行业瓶颈**

所有问题的症结来源是；摄像头没有转到BEV空间！

BEV空间不是3D空间，车辆运行的路面是结构化的，局部是平面的；锥桶是特例需要估计三维空间，另外会节约一个维度的算力；2.1 BEV出现之前行业瓶颈

所有问题的症结来源是；摄像头没有转到BEV空间！

BEV空间不是3D空间，车辆运行的路面是结构化的，局部是平面的；锥桶是特例需要估计三维空间，另外会节约一个维度的算力；

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWvrRr6nTibaJgbzibX3lxDXfAOXTe25XaAnLs6ib2ZyRulejmyrUjAEaRw/640?wx_fmt=png&from=appmsg)

大陆ARS408雷达输出：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWZdbLOqic1zmb4Lxo4cN34YAU2c3gmpHzMwjvH2SdhhF0mNZVneFqfAA/640?wx_fmt=png&from=appmsg)

4D成像毫米波雷达(Image Radar)，它输出3D位置+径向速度，相对于传统的3D毫米波雷达（2D位置+速度）多了一维高度信息输出,Image Radar具备传统3D雷达所有的特点，同时弥补了后者高度信息缺失导致的一系列问题；如TI AWR2243：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWLGl1VNiaVrmGYhoN0K9iaEBbiaOGuOCkJibtgCeB7UVxibFrJk8M3Dc2XdQ/640?wx_fmt=png&from=appmsg)

Radar原始输出就是BEV空间的:

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOW5kNAl0toumxz4qZD0FVWPhyIdQq0Vz5oslH3fxjvIhrUHf9QjaURdA/640?wx_fmt=png&from=appmsg)

当这个问题梳理清楚后，如何从图像特征提取BEV特征就成为了重点！

**1.2 为什么需要4Dlabel?**

高效和准确的标注，当然我们可以选择其他的2D标注方案：Annotate better withComputer Vision Annotation Tool (CVAT)等，但是会有问题，比如想标注后面位置的空间角点，因为2D图像没有深度的原因，很可能导致这个标注过程产生很大的误差，所以，这个时候就需要通过点云反过来投影到视觉图像上，这样的数据标注是更加准确的，比如南方科技大学的标注工具SUSTechPOINTS: Point Cloud 3D Bounding Box Annotation Tool For Autonomous Driving来实现4D label。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWKty0pN8MaA3q7vTyvpOrAH1lBkcY4L8QGBVicWbCtWWdJtXFpzx5QibQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWHyhQWAHv2WvmHb6oMOdQNaOohYwCFpiaxZeibxhIHkL7Xk4Tcz6dNQQg/640?wx_fmt=png&from=appmsg)

跨车范化性：将Homography Matrix将所有只有纯旋转外参的相机都变换到同一个平面；为什么是纯旋转，是因为传感器在车辆上位置的公差是可控的、很小的，但旋转是不可控的，所以通过纯旋转的单应变换；这样能够通过算法复用，降低车辆开发的成本！

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWxjjoUATvVuwHllazUbf8OMUDRwqWbibUfUlw1VVKMa7DIUNruTE29RQ/640?wx_fmt=png&from=appmsg)

**1.3 特征空间转换(View Transformation)方法汇总**

2D和3D感知后的是4D感知；前2者属于静态标注，但是最后一个4D属于是动态标注，对于动态物体的实时感知，包含物体的时序信息如跟踪、预测、速度、加速度等信息；

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWCAftqwiaZBUXApe157kcxR2cHvvUxHAAHiaenfKakBvsoOJcI2pgzFTw/640?wx_fmt=png&from=appmsg)

IPM的方法可参考 ，LSS方法可以参考；几种方法的对比：并不是tranformer的方法就是最好，要结合实际量产中的需求，量产追求的是性能与成本的trade off

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWuaDc2s38WtNOhzfjhkZKZlKZvpSx4JMatKiaIrib8dp51gakrgoLiav3g/640?wx_fmt=png&from=appmsg)

**1.4 BEV输出3D空间，让端到端成为可能**

BEV将相机内外参嵌入到模型中，所以能够得出更加准确和稳定的结果；

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWWrtibl5YLYDqq81WQXsdg5FKDInqTrsHk1JzUCjnQtYvj61FZv0Ir6w/640?wx_fmt=png&from=appmsg)

通过将视觉传感器的特征转换到BEV空间，那么其它LiDAR自然就会转换到BEV空间；特斯拉的自动驾驶FSD，从2021年初至今已经迭代了12个版本，所以也叫v12；

**02**

**基于BEV 重构静态与动态感知任务**

**2.1 重构静态感知任务**

第一个HDmapNet只是简单的分割 ，MapTR V2是在感知基础上进行了实例化，可以理解成为在线生成高精地图，OpenLineV2是将相关联的元素进行绑定，比如通过红绿灯来绑定车道，不仅会估计物理层，神经网络还会得到物理层之间的关系，实现更加智能的“高精局部地图”，以上算法就是对高精地图生成的各个步骤进行分解；

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWla8NDYAOJiaycEweuF6BIbKlFmBGxFBVbJMQP3Akx83Usq4FyQL1uIg/640?wx_fmt=png&from=appmsg)

**2.2 重构动态感知任务**

动态感知，BEVnet只是作为Bonding Box的检测，然后MUTR3D是将预测吃掉，最后1个是端到端直接输出轨迹；真值的标注Tracking是需要用到时序信息，云端数据标注是可以拿到整个数据的信息的，所以可以使用“未来”的数据去标注当前时刻的数据，方便网络训练当前模型对车辆的预测；

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOW0phHNoBMibaxyEpvSWBRqRRkbMrKIg5bB2tKx4WzdYVozPVjZLoT0DA/640?wx_fmt=png&from=appmsg)

**2.3 影子模式中的数据闭环**

影子模式：当人的驾驶行为和自动驾驶发生冲突时，然后就将对应的数据自动采集回来进行分析；Tesla甚至可以做到1周进行更新，但是国内其它厂家只是几个月；

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWaff3sib6SvPBse09YMR9ZDibN6GOxCHJbC7521xBD6adnekpKxl0590g/640?wx_fmt=png&from=appmsg)

一个小的clip(片段)进行重建的结果不是很完整，那么多个clip进行重建，那么就会很完整了；仿真环境是现实当中比较少出现的场景；友商：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWGRdhbkY0FPcdPsyzSZQAk7f9tdgLkHGMicC5a6p9qiaoKVlHltSxumXw/640?wx_fmt=png&from=appmsg)

**03**

**4D Label在自动驾驶中的应用**

4D Label能够拿到所有环节高精度的真实信息； 在 BEV 空间内，由于坐标系相同，还可以进行时序融合形成 4D 空间。但传统的3D标注技术显然无法满足其需求，面向BEV的4D标注技术开始被业界关注和采用。

BEV 4D标注是一种通过将三维物体在二维鸟瞰图上进行标注的方式，标注人员可以在鸟瞰图上对车辆、行人、交通标志等物体进行标注，并记录其具体的位置、大小和速度等信息。同时，还需要进行时间轴标注，记录物体进入和离开画面的时间，以便后续的跟踪。增加的时间信息也能够帮助算法更准确地预测物体的运动轨迹，提高自动驾驶的安全性。

**3.1 为各种感知任务提供训练和评测的真值**

* FreeSpace 是感知系统检测出的没有障碍物、可安全通行的物理区域。
* 与障碍物（车辆、行人、墙壁等）相对，通常表示为连续的地面区域或三维空间

4D FreeSpace：加入时间维度预测运动物体的未来可行驶区域;

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWfASHrPA7F9yU0xib55opuNyoTnxpx6SRqc1lURUWXoDsyyTvOZXhXKw/640?wx_fmt=png&from=appmsg)

**3.2 数据闭环中的关键模块**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWDtT7dfZjJyoemuDsiaH70se1RjU4tmic8cicbvBNkMMC10ty7RdkJLawQ/640?wx_fmt=png&from=appmsg)

**3.3 用于仿真中的场景库构建**

静态的就是局部地图，动态的就是包含时间戳的动态物体；

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWooFFWfgCdDcZXzyjpMqZbnibjqhGCP03XiadJcxrxC9vibicyK6DhTyx8w/640?wx_fmt=png&from=appmsg)

**3.4 自动驾驶单环节/端到端测试**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOW2h14qRS36iahhFwVFmianfVgwBibNqkX4NciauEGjvpFqyeXiaRuuQ8OFjw/640?wx_fmt=png&from=appmsg)

来源：知乎@FrankDellaert

https://zhuanlan.zhihu.com/p/1896654369820219291

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicHdaQsibvoH8dLYIIcT5YQibwbnuZn1MLCOMydw2SMKWbibsLpooeE2jgCt8FABvsVmlJZO5PO00Ryw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561756&idx=2&sn=f9b8c214978537f47cccba736cdb5bfd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTi...