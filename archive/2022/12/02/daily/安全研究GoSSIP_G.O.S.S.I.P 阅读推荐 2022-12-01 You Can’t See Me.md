---
title: G.O.S.S.I.P 阅读推荐 2022-12-01 You Can’t See Me
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493456&idx=1&sn=5e32e2fe8392e4bbfe13003e1af3ef34&chksm=c063c989f714409f7546a97ceaaaf469d8f036edc09f87230dff0030884d1790c7dce6e93d57&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-12-02
fetch_date: 2025-10-04T00:18:16.757973
---

# G.O.S.S.I.P 阅读推荐 2022-12-01 You Can’t See Me

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21FCuobmJmBapFnx7Hu35hJ2hAB5uM0BFHCZlgibWYeWlEibFSkMALPXISQMW3KwadZjOTCFTbwxsv2Q/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-12-01 You Can’t See Me

Yulong@MU

安全研究GoSSIP

轮台东门送君去，去时雪满天山路。

千回路转不见君，雪上空留马行处。

---

沪上今日风雪交加，12月的头一天分外寒冷，时间的脚步若不能走得更慢一些，那就让我们去追赶时间，奋勇前行便是最好的告别。

今天为大家推荐的论文是来自美国密歇根大学、佛罗里达大学、日本电气通信大学合作的，由一作投稿的关于自动驾驶安全的最新工作You Can’t See Me: Physical Removal Attacks on LiDAR-based Autonomous Vehicles Driving Frameworks，目前该工作已被USENIX Security 2023录用。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FCuobmJmBapFnx7Hu35hJ25wwJLAlxOU166OmV9ia4B1EQI2iaW4dcl6koZPPYlk5LmLKLQMtX1WFw/640?wx_fmt=png)

自动驾驶系统很多依赖激光雷达(LiDAR)来识别路上的车辆或行人。作者团队最近发现了一种通过利用激光攻击传感器来选择性移除激光雷达点云的攻击（**P**hysical **R**emoval **A**ttack），借此使得自动驾驶系统无法检测到路面障碍物。由于视觉感知对于自动驾驶系统的安全驾驶决策至关重要，这类攻击会导致无人车做出错误决策乃至导致交通事故发生。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FCuobmJmBapFnx7Hu35hJ2iaCib1o7zIpJxtatI5NE7iaWo7HnccyVdJaHowGW6iawvibxKBicBYTupn1Q/640?wx_fmt=png)

作者在三个常用的目标识别系统（Apollo，Autoware，PointPillars）以及三个传感器融合模型（Frustum-ConvNet，AVOD和整合型融合）上验证了我们的方法的有效性。实验结果显示可以移除高达45度角的点云，移除90%障碍物的攻击成功率高达92%。

PRA攻击通过用传感器欺骗攻击在激光雷达的最小工作距离(通常为50cm）内注入虚假点云来移除本来障碍物的点云。由于激光雷达通常会优先选取较强的反射信号，欺骗攻击注入的点云会替代真实障碍物的点云。进一步由于激光雷达通常有最小工作距离且此距离内检测到的反射信号不会被进一步处理，所以通过在最小工作距离内注入虚假点云即可移除本来障碍物的点云，实现通过注入虚假信号来移除真实信号的攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FCuobmJmBapFnx7Hu35hJ2aFy0UMoDPzpxZn7x1MiaNMzusNtibZFBfubPnom5NUQh89ZvH4Sn1TWQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/uicdfzKrO21FCuobmJmBapFnx7Hu35hJ2VQicUnibaBtUf3uA0aX4niaSJJ4Q3aZOD4xibCmiaQPTpH1H8kpZkNEVibpQ/640?wx_fmt=gif)

作者对PRA的有效性进行了多步验证。先通过攻击静态的激光雷达来测量激光雷达欺骗攻击的能力，作者成功实现了移除静止警示牌和移动路人的攻击。为了进一步验证对于移动车辆的攻击有效性，作者通过训练一个激光雷达识别模型来帮助机械云台自动瞄准移动的激光雷达传感器，在低速环境的停车场里验证了攻击的有效性。具体实验设置和demo可以参考该工作的项目网站。

最后为了更好地展示攻击产生的端到端的效果，作者在LGSVL仿真模拟器里模拟了对应的攻击并发现其可能使得无人车因无法发现或太晚发现障碍物而撞到行人或车辆。由于仿真模拟的易复现性，作者测试了多个不同起始位置和速度场景下的攻击并发现PRA可以在多种场景下影响无人车的障碍物检测以及后续的行车决策。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21FCuobmJmBapFnx7Hu35hJ2ns3mhL8aOSD0UQTQUIkPuC7JRrVzHbzGBX34tATfqDHKJVDvVoqDOw/640?wx_fmt=png)

由于PRA属于只对激光雷达进行的攻击，作者还验证了此类攻击是否对基于传感器融合的目标检测模型有效。作者惊讶的发现，无需改变相机图像而仅对激光雷达进行攻击也是可以得到基于传感器融合的目标检测模型有效的！

论文下载：

https://arxiv.org/pdf/2210.09482.pdf

项目网站：

https://cpseclab.github.io/youcantseeme/

预览时标签不可点

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