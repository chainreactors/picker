---
title: 车载传感器欺骗与融合一致性校验：摄像头、LiDAR、雷达、GNSS
url: https://mp.weixin.qq.com/s/hV8ItTS9RrhcAQ6qCWeNgw
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:39:23.161989
---

# 车载传感器欺骗与融合一致性校验：摄像头、LiDAR、雷达、GNSS

# 车载传感器欺骗与融合一致性校验：摄像头、LiDAR、雷达、GNSS

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB995ym51yuiaz6UL4C02FAq637ia0w2GiaMZ1NeOTbZsFia0oXMWjkiatyNdibc3tWmRVo9GcFVPnLmf3HcbwDyar3YhWkLDt0DZ4SY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247582550&idx=1&sn=d7226bc800af241beba7f3da987f9de3&scene=21#wechat_redirect)

车内网络、诊断口、证书体系这些主题，讨论的都是「数据进了系统之后怎么被相信」。感知链面对的是更早的一层：数据还没进系统，物理世界的信号本身就可能不是真的。摄像头、激光雷达、毫米波雷达与 GNSS 各自有一套可被干扰或伪造的物理信道，而多传感器融合原本正是用来兜住单点失效的冗余设计。

近年公开研究里最值得工程侧注意的一类结论，是攻击者不再让两个传感器互相矛盾，而是让它们「一致地」看见同一个不存在的物体。这篇把欺骗路径、跨模态一致性的失效条件、物理层与融合层 defenses，以及感知事件的取证字段，整理成一份可验收的清单。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaC3qJo1tnYPZ50ibmX6Dq4kibDRBXkUjXwYH26Id4a0FPLLlzibFycfibMujbvDVmBHMhojD4tEvtH0mUPLHO22wTgKib7snnQulnr0/640?wx_fmt=jpeg&from=appmsg)

图 1｜道路场景激光雷达 3D 点云

**一、感知链对物理层输入的默认信任**

绝大多数量产感知栈把传感器输出当作可信输入：摄像头给像素、LiDAR 给点云、雷达给回波、GNSS 给位置与时间，融合模块负责把这些对齐成一张环境模型，再交给预测与规划。这个假设在随机故障下是成立的——单个传感器脏了、糊了、掉帧，冗余与一致性检查能把它挑出来；但在蓄意构造的物理输入下，它会被反过来利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaA5fMJHQQTGCMI0qv6GhzzdpRo70vcyErUDcUEibHu1xUP6hI7wfL1nxaVfuvgbK72Pick6o5nZMy4g9LjcfTk6wYriccXoics9smU/640?wx_fmt=png&from=appmsg)

关键差别在于：物理层攻击不需要入侵 CAN 总线、不需要拿到车云凭证、也不需要在 ECU 里落地代码，攻击者只需要在传感器的感知范围内改变信号。这让传统的网络侧 IDS、验签与访问控制几乎无从观测。

**二、摄像头、LiDAR、雷达与 GNSS 的欺骗路径**

四类传感器的物理信道不同，手法也不同，但都落在「移除真实信号」与「注入虚假信号」两类动作上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDzLJOuA1AS67df4yPlYr6X2eDVm04uMgCYWNAJNBW7txLNckWBicf3cLPZ9pSN1LymSBbbJFHDvVw43sBj5CqVeHZ2iaibFcELZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDAfxG3lqgGZ9t4DMVzK6HtLFtmZ0PqZM9R0YJzNjiatU3Jcd1vKN7KTx9nObqagXOZm8sKTzYNcQfuZjn6dYz4iawxxNIfAWib0I/640?wx_fmt=jpeg&from=appmsg)

图 2｜全景环视系统四个摄像头

摄像头侧，公开研究里既有把对抗补丁贴在交通标志或目标框外的做法，也有用红外激光在路面投出图案以制造高置信度假检测；还有用转向光学膜改变传感器视场角，让里程计与车道线判断偏移，而目标检测的置信度几乎不降。LiDAR 侧，一类做法是主动注入与真实回波同步的激光脉冲，在点云里造出幻影或抹掉行人；另一类不加任何信号，只在路面铺特定倾角的镜面材料，把光束反射到天空形成点云「阴影」，让体素类 3D 检测器把空白区域识别成一辆车。后者不需要主动发射、不需要持续在场，材料还能伪装成路面反光，实现门槛很低。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaD1AiczHDIewBA9WkkocRxN3sk2lkOyVk5JAbjPKLcNoHBRCpubczYh2LEj2q506FsM99sAZZM18nc9rgBCfqvR1QOXrPwmiaSjs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBwFWibC7kjG23FB8Nk2OhLGb70H4S5IyBnSxN9HOzun85iaMOsibO3oIWIAzmzuzdZs9Lbrs8CBuvgTGKCUyWdkhckAuaebwtBw8/640?wx_fmt=png&from=appmsg)

图 3｜GNSS 智能欺骗原理示意

国内测评侧也已把这类风险纳入规程：中国汽研 IVISTA 网联智能与隐私安全专项测评设有 GNSS 信号伪造试验与 GNSS 信号干扰试验两个维度，检测手段包括交叉模糊函数特征分类，以及信号强度、迭代时间、多通道校验、多普勒频移等观测量。这一层的共同点是——防护必须发生在信号进入感知算法之前。

**三、跨模态一致性被伪造的攻击面**

多传感器融合的安全论证，通常建立在「一个传感器异常会被另一个否决」上。攻击者若能让两路传感器对同一个假物体达成一致，冗余反而成了放行通道。

公开研究里已有几条互补路径。USENIX Security 2022 的 frustum attack 用物理可实现的 LiDAR 欺骗，在黑盒条件下跨八种感知算法、三类融合架构做了大规模评估，说明随机分布的点云插入与精心摆成车形的插入效果相当，且多帧跟踪下能影响控制。UC Irvine 等团队用 3D 打印的对抗物体，同时改变摄像头像素与 LiDAR 点云，使两路都识别不到同一个交通锥。更近的工作直接模拟「红外投影造假摄像头检测 + 信号注入造假 LiDAR 点云」的协同组合，在 400 个 KITTI 场景上让融合模型接受一个并不存在的行人。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB4aImCbq6IsaCEIibObXiabgL7A5kznIibSAd5Yldt0jJs38z7n59OkFq1Ce7qyn29PicOasv4Es15vUQY0773bboE4aFaRgPHRTA/640?wx_fmt=png&from=appmsg)

图 4｜前融合系统架构图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCxr3tM93FEPPleBfHgghkZmR4Lu1Wtm2W4qUsqjba9KSic7uZVyY1QN5reqxHXgPExHSR1hpt8GYcW9bgb8HXnah4C36fjGhak/640?wx_fmt=png&from=appmsg)

这类失效最棘手的地方是「没有矛盾可查」。一致性检查的判据是两路是否互相应证，而不是其中任何一路是否对应真实物理世界；一旦一致性本身被构造出来，检查就会通过。

**四、物理层攻击的实现条件**

把论文里的成功率直接搬成量产风险是不准确的，实现条件决定了哪些手法需要优先防。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDt8PF3mImpiah8eEic2hzEibhcPu63K0tgibFaS8fbMicjrnQ8TJ9ibtxXbwar5L7cGwOEupNIj5ygLUV71XYxAA1MJ0c6TJ8Nd1lZw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCbvuiawia4BmA0xGVZldeKFbmf9V4lxkeu2gm0HcRJ0f8YxYYz1ZRH4icZZMLxpdLqRHx90yYbcWJ6Uj06weiaWkmOZ3mcXE4rQ8g/640?wx_fmt=png&from=appmsg)

图 5｜对抗性 STOP 标志实验图

举个例子：点云阴影攻击对体素类检测器效果显著，对原始点法的模型基本无效；镜面材料在不同 LiDAR 型号上的点云移除率也有差异。这说明「某论文在某模型上成功」不能外推为「某类传感器整体不安全」，工程上要按自己用的模型架构、传感器型号与场景分布重新验证。

**五、融合一致性与传感器健康校验**

防御要分两层：在信号层识别「这份输入不像真的」，在融合层拒绝「只有一致性、没有物理依据」的结论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCaPln0GniafDBzw76XVhgafeibjH2EGOL0Jx1wOUG6dQ67HY49iaeQ2VES7eY0q8biaNTbJbaoZWOicOt0vwwqd6kgKuEgt92txAPU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBS4JBzsJXHj4Cic5Cv1NnEHhpKEuVMJLmMI4hibDCuXPhYuSGXwskcjvZdF1zYl2PZMAt71YcOZrcJTOh2OFkIrCd8RHrcXCb1I/640?wx_fmt=png&from=appmsg)

图 6｜汽车角毫米波雷达主板及散热片

跨模态物理验证是最值得单独写出来的一条：当 GPS 报告车辆以 60 km/h 向北行驶，而惯导与视觉里程计都指向静止，正确动作是把 GPS 标记为遭受篡改，而不是对矛盾数据做加权平均求一个折中。同理，检测框内若没有足够多的 LiDAR 点，就该对该目标做二次验证；公开研究里这类 BBValidator 在正常数据集上对精度影响很小，却能把点云移除类攻击挡在检测阶段。硬件侧也有进展：在 dToF LiDAR 发射端随机化脉冲对的时间间隔与幅度比、在接收端做双域指纹认证，让伪造回波在测距之前被拒绝。

**六、物理层防御与硬件指纹**

把上述手段归到工程实现，会看到三类能力，各自的成本与适用位不同。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaC9uAJf4Eq8Ip068AP8iaULDM12TJ05yiaaCoe2iaxMFy1RpSKVJIR9z7PdtljqlffDEYFibUE5icOCeUQHiaymJuqTLj8ZrO0FqO5Qo/640?wx_fmt=png&from=appmsg)

一条容易被忽略的边界：MACsec、SecOC、TLS 这些机制保护的是报文在链路上不被改写，解决不了「传感器在采样那一刻看到的就不是真实世界」。物理层问题要在物理层留证据，网络层完整性无法替代。

**七、研究结论的适用范围**

公开材料里的攻击与检测结论，绝大多数来自实验网络、仿真、台架、原型或研究车辆：OMNeT++ / LGSVL / CARLA 仿真、KITTI 数据集、实验室光学材料部署、真实 TSN 或传感器测试床、以及少量研究车的实车验证。它们证明的是「在给定模型、给定传感器、给定条件下路径可行」，不等于量产车队已经被这类手法攻击过，也不等于某款车存在已确认的对应漏洞。

防御侧同理：某个检测器在论文数据集上给出的检出率、某个补丁防御在若干数据集上的表现，不能直接当成整车安全指标。标准与法规给出的是风险管理与可追溯要求——ISO 26262 要求安全机制与故障反应可论证，ISO/SAE 21434 与 UN R155 要求对网络安全风险做全生命周期管理，UN R156 与 ISO 24089 要求更新与配置可追溯；它们并不规定某款车必须采用哪一种融合算法或哪一种异常检测阈值。

**八、感知事件的证据链与版本上下文**

一旦发生争议，能支撑复盘的不是「当时检测到了什么」，而是「当时凭什么这么判断」。可采信的感知事件记录，至少要覆盖四组字段。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCrpXWMerxrmGt6giaduPDRrpvOibrICqtv3oBSeibLsQpyo4L8ic5Ve5NRg189dTdd2Amwe81LIYibxjCym0ENu7asuFouTkH8fmuI/640?wx_fmt=png&from=appmsg)

车端可用环形缓存做短时回溯，只在触发条件成立时固化取证包，并对内容加密、签名与完整性校验；上传侧按分级授权与审计访问，避免「能取证」变成「可滥用」。这一部分依赖统一且可信的时间轴：没有共同的时基与同步状态记录，多传感器的「一致性」本身就无从举证。

**九、工程验收项**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAq6cuIkMhmicWNpVM4wuo7mtmOGVOX0BXfTHgl0dibdBF11slsWnJyRZaM5iaoR1XGpHhC5VTLo9fFc6AuI2PZAW7iaoB0WH2vUYg/640?wx_fmt=png&from=appmsg)

感知安全最容易失守的地方，不是算法不够准，而是整套系统默认「进来的信号就是世界本身」。把这条默认信任拆成信号层、融合层、决策层各自可验证的条件，冗余才真的能兜住单点失效，而不是在有人刻意制造一致时，变成一条更顺畅的放行通道。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCfv8Rp38N5sYLv34P5K2FpbKBdOqic0AaRmDVCFhEyTzRU6zQT3tmaxMial0KrepPFt3Ew0Q9icVLRq6etEGGZUpF3eBwKBiaBqSU/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBvgQxffuoSxCK5zHBjMe1zHgWJ84eiapLGn9OJxaSDIkr7ZxqlZePY6F37BhEGKickoLHqodK770FzBXHPlIuxyHCSicGTiaF5FP4/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247580896&idx=1&sn=36a65f68d014c79310fdeb0e1e55b6b0&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=appmsg)

**公司类型占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJABYuCSyTpLXjRNbVv7OUTUUCxmB1OuPhtcM4j1kw/640?wx_fmt=png&from=appmsg)

**文章**

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?...