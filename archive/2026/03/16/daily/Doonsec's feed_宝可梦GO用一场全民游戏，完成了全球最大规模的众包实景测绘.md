---
title: 宝可梦GO用一场全民游戏，完成了全球最大规模的众包实景测绘
url: https://mp.weixin.qq.com/s/bB98Zix-3Os0k2Wbepcbvg
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:10:48.131057
---

# 宝可梦GO用一场全民游戏，完成了全球最大规模的众包实景测绘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDofd5deOb0InXOJaD4zcBVpvMhetdicaD5UyF5A8vxsljOhGaakKhibZh42dPALPetOAJQC6rqwLXhueZjMo7uM7sxYnVQP7dEGw/0?wx_fmt=jpeg)

# 宝可梦GO用一场全民游戏，完成了全球最大规模的众包实景测绘

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

2026 年 3 月，Niantic 旗下空间智能企业 Niantic Spatial 宣布与末端配送机器人厂商 Coco Robotics 达成战略合作，将《宝可梦 GO》全球玩家 10 年间众包积累的 300 亿张带精准定位的实景影像，用于训练视觉定位系统（VPS），为城市配送机器人提供厘米级定位能力，解决城市场景 GPS 失效的核心痛点，实现 VPS 技术从消费级 AR 游戏到企业级空间智能基础设施的规模化商业化落地。

视觉定位系统（VPS，Visual Positioning System），简单来说，就是用眼睛/摄像头看周围环境来判断自己在哪里的技术。想象一下：
当你在高楼大厦之间、室内商场、地下停车场，普通GPS经常实效（误差几米到几十米，甚至完全没信号），这时候VPS就像给手机/设备装了个“超级认路大脑”，它看一眼周围的建筑、招牌、路灯、墙上的纹理，就能知道你精确到厘米级的位置和朝向。

* GPS ≈ 用天上的卫星喊话：“我在哪？”（容易被大楼、树、隧道挡住）
* VPS ≈ 你自己睁眼看四周：“哦！这是那个有大钟的教堂拐角，我知道自己在哪了！”

意味着它直接理解真实世界路况，而不是靠无线电信号。

VPS最经典的工作原理（三步走，像人认路）

1. 提前建“视觉地图”（云端数据库）
   像谷歌/ Niantic 等公司开车或用无人机拍无数街景照片，把每张照片里的关键点（特征点，比如窗户角、广告牌边缘）提取出来 + 记录精确3D坐标，建成一个超级详细的“视觉指纹库”。
2. 你拍照/摄像头看一眼
   你的手机摄像头拍下当前画面 → 系统快速提取画面里的特征点（也叫“视觉指纹”）。
3. 云端比对 → 瞬间定位
   把你拍的“指纹”上传云端，和提前建好的海量视觉地图比对 → 找到最匹配的位置 → 直接告诉你：你现在就在这个路口，朝北偏西12度，误差±10厘米。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoCHo5oFfHqxNavkg2xib4f2PDWRx6ZORh6qpAQiaaokRIrE4SBlMftfuj4IebnW37hyv5po6iaCj0fyhve3Ev8VRIQwiaqH24kots/640?wx_fmt=png&from=appmsg)

经典例子：手机对准街道，出现卡通狐狸引导你转弯，这就是Google VPS + AR导航的典型表现

如下图所示，特征点匹配示意：把建筑物关键点连线，像蜘蛛网一样匹配你当前视角和地图视角

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrUOCibHkReYUj7T8u7872Wf4YSsQAAFK3Yq3Jclnz7ZwOsDOmhgAb2v2VSooytYatHOUdOSRx52OLolHWMmb7PzOuX0ZolkYlM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpBZ9jWhVIxBnK1uJtMqnrj1C9xJzGibq9YdOWh79MBIuNlibtBB4vCicYSOzhTniasRZBXlVTax9nsvlzz2f57QwSbbOO1KvNEZak/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqTiaEBFxgddBDyCpSbt2hwMrSw1KsCysmdu5uUreleCEoRCUiaxYmHrdJa0vmaAwhKI5ibCpNqSRTwhvJAKQ3kia6gTo3bd4XywIc/640?wx_fmt=png&from=appmsg)

VPS 技术的理论优势，在 Niantic 的十年布局中完成了从技术验证到规模化商业落地的闭环，而核心载体，正是现象级 AR 手游《宝可梦 GO》。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoicmibxQZY2dYYXMgw0GYm0d2AKCxkCWCjdIwkRliaJOB37WF7p9ttDZGpxaLulqIEgIsicEwK32rnqdibLkBDvy1HaAib9LMV8tHzY/640?wx_fmt=png&from=appmsg)

2016 年，由谷歌分拆企业 Niantic 联合宝可梦公司推出的《宝可梦 GO》，成为全球首个现象级 AR 产品。这款游戏将宝可梦 IP 与 LBS 技术结合，让全球数亿玩家走上街头，通过手机摄像头捕捉叠加在现实场景中的虚拟宝可梦，也在无意间完成了一场全球规模最大的众包实景测绘。

2020 年，游戏新增实地研究功能，以游戏内稀有奖励为激励，引导玩家专门扫描现实中的雕像、地标、建筑，进一步加速了全球实景 3D 模型的构建；

Niantic Labs 推出的宝可梦游乐场（Pokémon Playgrounds），正是 VPS 技术首次在消费级应用中实现规模化落地。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqdvvdTWwIicCjzuhmjt1gAoAp6QN03K4Ln0SAOF9ZHDFlz7Tm0nPSUIAKHRNkdzicQ0sZcVm8N8hiclXXrOcxMMkkZqL1DCNC6CA/640?wx_fmt=png&from=appmsg)

该项目通过视觉锚定技术，实现了与物理环境精准匹配的持续性数字体验，让虚拟元素与现实世界实现了无缝交互，也验证了 VPS 技术在消费级场景的成熟度。

截至 2026 年，游戏上线 10 年间，全球玩家累计贡献了**超 300 亿张带高精度定位元数据的实景影像**，覆盖全球超 100 万个地标热点，形成了全球规模最大、维度最丰富的城市实景 3D 模型库，这正是 Niantic VPS 技术的核心壁垒。

2025 年，Niantic 完成战略转型：

将全部游戏业务以 35 亿美元出售给手游厂商 Scopely，同步分拆成立 Niantic Spatial，全面转型为地理空间 AI 与空间智能服务商，核心产品正是基于十年众包数据打磨的 VPS 系统。

2026 年 3 月，Niantic Spatial 正式宣布与美国末端配送机器人厂商 Coco Robotics 达成战略合作，将其 VPS 系统规模化应用于城市末端配送场景，这也是 VPS 技术在企业级场景的首次大规模商业化落地。

Coco Robotics 目前已在美国洛杉矶、芝加哥、泽西城、迈阿密，以及芬兰赫尔辛基部署了约 1000 台配送机器人，设备最大可容纳 8 个超大号披萨或 4 袋生鲜杂货，以约 5 英里 / 小时的速度在人行道行驶，截至 2026 年已完成超 50 万单配送。

而制约其规模化扩张的核心痛点，正是传统 GPS 在城市峡谷场景的失效 ，高楼、地下通道、高架桥下的 GPS 信号反射与干扰，会导致定位误差最高达 50 米，直接造成机器人迷路、配送延误。

而 Niantic 的 VPS 系统，完美解决了这一痛点：

* Coco 的配送机器人搭载 4 颗全景摄像头，通过 VPS 系统实时匹配周边实景与后台 3D 模型，精准判断自身位置与前进方向，定位精度可达厘米级；
* 即便在 GPS 完全失效的场景，机器人也可精准停在餐厅外的取餐点，避免遮挡行人，同时精准停靠在客户家门口，解决了末端配送「最后一米」的定位难题；
* 机器人摄像头的腰部高度视角，与《宝可梦 GO》玩家的手持视角虽有差异，但基于海量多维度数据的 VPS 模型，仅需简单适配即可稳定运行。

与 Coco Robotics 的合作，只是 Niantic VPS 技术商业化的第一步。公司的终极目标，是构建面向机器的、实时更新的全球活地图（Living Map），一套超精细的现实世界虚拟仿真系统，会随着现实世界的变化同步更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrSIfPqibrjh5EanqTN2wjy2zzBhunv40MibzUXIMNRJBIsCsibxswIkqKYyT00YRxrYX5ibCibHjEKVc2nODqxafFMnMaMZp4oAz50/640?wx_fmt=png&from=appmsg)

一旦搭载 VPS 的配送机器人、智能设备上路，它们采集的全新实景数据，将反哺 VPS 模型，进一步提升定位精度与场景覆盖度，形成数据采集 - 模型优化 - 场景拓展的持续闭环。而 Niantic 的差异化优势，在于通过消费级游戏，提前 10 年完成了全球规模的基础数据积累，无需像自动驾驶企业那样从零开始通过路测采集数据。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoa81hIfGc2CW4Yzo8v4HYNb6d2dhq3Nj3ianDaYdWcdk8IMqZTjuwpEOdKEQ9SoP26lQPtsfFI2HavLN8GjAeiaCtSmYTbK6hkE/640?wx_fmt=png&from=appmsg)

更长远来看，Niantic 正在重构地图的核心价值：传统地图的服务对象是人类，核心逻辑是地图点位对应现实空间坐标；而面向机器的地图，需要成为一套可被机器理解的世界指南，为每一个物体标注属性与语义信息，让机器真正理解它所看到的世界。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoYlbqhEGk4ZNiazKibd5ibMgX9KaH5IDTq3cdmsIDtA4Iia0c0cvFibCBGU03j1eVKk4q9cu9Ku0vVVwibVkUdyRNZt0jpib5IS1JysE/640?wx_fmt=png&from=appmsg)

黑鸟基于上述内容进行扩展，可以发现VPS的技术落地，是计算机视觉与空间计算的协同运作，核心分为五大关键步骤：

1. **特征检测与提取**

   设备摄像头采集环境影像后，VPS 会识别画面中的关键视觉特征 —— 包括角点、边缘、纹理等在不同视角、光照条件下仍可稳定识别的特征点，并将这些特征转化为数学描述符，形成场景的「视觉指纹」。
2. **特征匹配**

   将提取的特征点，与预存的参考数据库中的已测绘视觉数据进行比对。该匹配过程采用鲁棒性算法，可应对视角、光照、季节变化等对视觉外观的影响。
3. **位姿估算**

   当完成足够数量的特征匹配后，系统通过几何算法，计算出设备相对于匹配参考点的精准位置与朝向（二者合称「位姿」），最终形成六自由度定位结果 —— 覆盖空间位置（x、y、z 三轴坐标）与朝向（俯仰、偏航、横滚三轴角度）。
4. **3D 建图与空间锚定**

   VPS 平台会维护环境的精细化 3D 地图，通常通过摄影测量或激光雷达扫描构建。这些地图中包含空间锚点 —— 带有精准坐标的持续性参考点，可让数字内容精准锚定在物理空间中。
5. **机器学习优化**

   通过神经网络持续提升 VPS 能力，包括在复杂环境下更稳定的特征识别、可识别物体与空间关系的语义理解能力，以及可预判移动轨迹、提升系统响应速度的预测模型。

除末端配送机器人外，VPS 技术正在多个行业实现落地，推动运营效率提升与全新能力的构建：

### （一）零售行业

面向消费者：店内精准导航，可引导顾客直达目标商品，同时推送基于精准位置的个性化促销信息；

面向运营：实现精准的货架巡检、陈列合规校验，以及实时库存位置追踪，大幅缩减商品查找耗时。

### （二）仓储物流行业

在配送中心部署 VPS，可为拣货人员提供精准的导航指引与实时操作指令，大幅提升拣货效率；同时让机器人与人类员工在共享空间内协同作业，凭借精准的空间感知能力保障安全，还可通过资产精准定位提升库存管理精度。

### （三）汽车行业

整车厂商正在通过 VPS，提升停车场、城市走廊等 GPS 失效场景的导航能力；同时优化复杂环境下的自动驾驶表现，为高级驾驶辅助系统提供精准的车道级定位。

例如全球领先的汽车系统供应商采埃孚（ZF Friedrichshafen AG），就通过 Niantic Spatial 的扫描技术与 Sphere 空间工具，替代了传统的 3D 打印与实物模型，通过虚拟设备布局与实时调整，以 XR 驱动的精准布局优化了工厂规划流程，验证了 VPS 在汽车制造领域的效率提升价值。

### （四）建筑与工地管理

在建筑场景中，VPS 可实现建材与设备相对于数字图纸的精准定位，实时对比施工进度与 BIM（建筑信息模型）数据，在偏差造成高额成本前，及时提供项目进度与施工偏差的可落地洞察。

尽管 VPS 拥有巨大的应用潜力，但企业在落地过程中，仍需应对多项技术与运营挑战：

1. **环境与光照条件限制**

   极端弱光环境、高反光表面等场景，会降低 VPS 的定位精度；
2. **算力与功耗的平衡**

   实时运行的 VPS 对设备算力要求较高，在移动设备上，需要在定位精度与电池续航之间做出平衡；
3. **数据库的持续更新**

   在物理环境频繁变动的动态场景中，维护最新的视觉参考数据库，存在一定的运营难度；
4. **企业系统集成难度**

   将 VPS 系统与企业现有业务系统集成，需要完善的规划，尤其对于拥有大量传统基础设施的企业，集成门槛更高。

   ![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp7C7icTSK5Yb2e9KKxFyZtZ8NnC3oZkMQxK3qibwJbdedHDTyAfmfsPJEFrUXoQAH3l4LiarYiaI6qkY9YZZ4iccWjKZh6gmXzV55w/640?wx_fmt=png&from=appmsg)

##

VPS 技术的核心壁垒来自海量的实景影像数据，而数据的采集、二次利用与商业化，也带来了严峻的隐私合规与伦理挑战，这也是本次《宝可梦 GO》数据赋能配送机器人事件引发行业热议的核心原因。

《宝可梦 GO》的所有影像数据，均来自玩家的游戏行为，但绝大多数玩家在拍摄实景、参与游戏时，并不知晓自己的行为会在数年后被用于训练配送机器人的 VPS 系统。

这种为单一目的收集的用户数据，被跨场景商业化二次利用的行为，超出了用户最初的授权预期，也成为 AI 时代数据合规的典型争议案例。

这并非个例：此前谷歌的 CAPTCHA 人机验证，就长期被质疑以验证身份为名，收集用户标注的图片训练 AI 视觉模型；位智（Waze）的用户生成内容，也曾被执法部门获取用于案件调查。

而 Niantic 的 VPS 系统，可通过单张照片的地标实现厘米级定位，对执法部门有着极强的吸引力，存在数据被违规调用的潜在风险。

玩家拍摄的实景影像中，不可避免地会包含行人、私人场所、车牌、人脸等敏感隐私信息。尽管 Niantic 声称会对数据进行脱敏处理，但大规模的实景影像收集、存储与商业化利用，始终存在隐私信息泄露、被滥用的隐患。

尤其当 VPS 技术规模化落地后，海量智能设备将持续采集街景影像，形成对公共空间的常态化视觉监控，进一步加剧了公众的隐私焦虑。

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