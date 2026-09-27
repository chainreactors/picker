---
title: 手机传感器，也会“听见”CPU的功耗
url: https://mp.weixin.qq.com/s/l0ta1iVrVrLoQfjrYHojzg
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:23:31.205010
---

# 手机传感器，也会“听见”CPU的功耗

# 手机传感器，也会“听见”CPU的功耗

数缘科技
数缘科技

数缘信安社区

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**FRONTIER INSIGHTS**

**前沿导读**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwVn6YGC8fIYTSA65G8J7ZfWLWqibr6h9Qn73Bricic7ibzFju55BcJAbFF2yJDPpibkoqb4w5CVPZdhKYBKJoEvTe69ZdgsRPYw0ZNI/640?wx_fmt=png)

撰文 | 杨易明

编辑 | 刘梦迪

**从Android传感器到**

**像素窃取与AES密钥泄露**

**一、**

**背景介绍**

功耗侧信道攻击通常让人联想到示波器、电流探头或芯片内部的能耗计数器：攻击者观察设备执行不同操作时的功耗差异，再从波形中推断正在处理的数据。近年来，操作系统和硬件平台逐步收紧了直接功耗接口的访问权限，但“看不到功耗值”并不等于功耗的物理影响已经消失。CPU负载、供电电压、工作频率和电磁活动仍会在系统内部相互耦合，并可能被其他软件可见的信号间接记录。

在NDSS 2025论文《Power-Related Side-Channel Attacks using the Android Sensor Framework》中，来自格拉茨理工大学的研究团队把目光投向了一个几乎每部智能手机都开放的接口：Android传感器框架。该框架向普通应用提供加速度、磁场、方向、气压等读数，许多传感器不需要用户授予额外权限。作者提出的问题是：这些本来用于感知环境和姿态的传感器，是否也会“听见”CPU的功耗变化？

答案是肯定的。研究团队系统分析了9款Android手机中的137个流式传感器，发现大量读数受到CPU活动的寄生影响。更重要的是，这种影响不仅能区分“忙”和“闲”，还可能区分指令类型、数据操作数，进而支持远程像素窃取和本地AES密钥字节泄露。

**二、**

**基本原理**

Android传感器大体可分为两类：一类直接读取专用硬件，例如磁力计、加速度计和气压计；另一类是由多个硬件读数融合得到的软件传感器，例如方向传感器、旋转矢量传感器和地磁旋转矢量传感器。普通应用通过统一的传感器框架订阅这些数据，系统会按照传感器支持的刷新率持续上报。

当CPU执行不同工作负载时，晶体管开关活动会改变瞬时电流和供电电压，动态电压频率调节又会改变芯片的工作点。这些变化可能通过电源网络、电磁耦合、模数转换器参考电压或传感器融合链路，最终反映到传感器输出中。论文将这种与实际功耗强相关、但并非直接功耗读数的信号称为“功耗相关信号”。

需要强调的是，传感器并不是在“测量CPU功耗”。研究利用的是功耗活动对传感器链路造成的寄生扰动，因此不同传感器、不同手机、不同摆放方向的泄露强度差异很大。为了衡量攻击面，作者从三个层次逐步提高分析粒度：先区分CPU高/低利用率，再区分不同指令序列，最后测试相同指令在不同数据操作数下是否仍会泄露。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwUjoohNcV7EnictH1ia0UVrgZfLYhvu5fxfuxzBxqo90xUFiaKVib9Jg5wV9uicwPcbw6Pibzr2EznYjdOziaQXHsqw7OJhAMiaAmrFg14/640?wx_fmt=png)

地磁旋转矢量传感器、气压传感器读数与CPU负载的同步变化

上图给出了最直观的证据：CPU压力测试与休眠阶段每约2.5秒交替一次，地磁旋转矢量传感器的输出几乎同步地在两个平台之间切换。气压传感器的响应更慢、噪声更大，但同样能看到与系统状态一致的趋势。侧信道的关键就在这里：应用看到的只是“合法”传感器值，其中却夹带了并发计算的信息。

**三、**

**系统性传感器泄露分析**

实验覆盖Google、Samsung、OnePlus和Honor等品牌，设备发布时间从2017年跨越到2024年，系统版本从Android 10到Android 14。所有传感器读取都在普通应用权限下完成，设备保持默认配置，CPU频率没有固定，动态电压频率调节保持开启。为了验证物理来源，部分实验额外读取了需要特权的电池电压、CPU频率和温度作为真值；真正的攻击入口仍然是无需特权的传感器读数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwV0aY5ViaV1CPUpFV4gTdIzuuOIZgSjhasgMAotkqH22vbW3DN8bve07xEqv6Bf8cMfTPpI0CRiavMVdNd7mLdicrFfONOM8ffgS0/640?wx_fmt=png)

Google Pixel 6a传感器泄露分析结果（加粗数值为各类测试中的突出结果）

**区分CPU利用率。**作者让重负载和空闲阶段各持续2.5秒，并用皮尔逊相关系数比较传感器曲线与高/低负载模型。结果显示，26个传感器的相关系数超过0.7，占全部137个传感器的18.9%。磁力计和地磁旋转矢量传感器通常表现最好，但气压、加速度、重力和游戏旋转矢量传感器等不含磁场数据的传感器也会受到影响。

**区分指令序列。**研究团队在ARM处理器上循环执行存储、逻辑、整数、浮点和AES等不同指令，同时记录传感器值与电池电压。以Google Pixel 6a为例，未经校准的磁力计对CPU利用率的相关系数达到0.973；气压传感器对不同指令序列的相关系数达到0.955；地磁旋转矢量传感器对指令序列的相关系数也达到0.913。这说明泄露并不只由“CPU是否繁忙”决定，具体执行内容同样会改变传感器读数。

**区分数据操作数。**作者固定一条周期恒定、仅在寄存器上运行的xor指令，只改变两个64位操作数之间的汉明距离，并把汉明距离作为功耗模型。60个传感器出现统计显著的数据相关泄露，占137个传感器的43.79%。这一比例不代表每个传感器都能直接完成实用攻击，但说明数据依赖的功耗扰动广泛进入了传感器链路。

不同手机上的最强泄露源并不相同，相关系数也不能简单互换。例如Google Pixel 6a的磁力计很适合区分CPU利用率，却不一定最适合区分指令；气压传感器则呈现相反的优势。攻击者因此需要先对目标设备做画像，找出最合适的传感器、采样率和信号通道。

**四、**

**方向相关的地磁旋转矢量传感器泄露**

在全部传感器中，地磁旋转矢量传感器最值得关注。它是一个融合传感器，用磁场信息估计设备相对于地磁北极的方向。作者发现，其功耗相关泄露不仅强，而且与手机朝向高度相关：同一台手机只要在桌面上转一个角度，泄露幅度和正负方向就会明显变化。

为量化这种效应，研究团队把Google Pixel 6a平放，每次旋转22.5度，完整测量360度。每个方向都让CPU高负载与休眠阶段以2.5秒为周期交替，并持续采集约45秒，最终得到16组可比较的传感器轨迹。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwXFLpEcU3llYsBb23j5KqS66TyVFB1yMqk06Vj7PVoAcj16jcY5PbkNroyyj03WQxkELdatQ8gZxX2YyZ2ONESXwboJTHwMY3E/640?wx_fmt=png)

手机旋转实验：每22.5度测量一次以寻找最大泄露方向

上图显示，最强泄露出现在手机指向地磁南极附近，转到与南北方向垂直时最弱；最强与最弱方向的平均幅度相差约50倍。在极端情况下，CPU压力造成的偏移足以让指南针应用的指针变化约30度。这已不是只有统计工具才能看到的细微差异，而是可能直接影响用户界面的可见扰动。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwU9P6YBibXxRZC44W73a88A6GLOOI2Naz3sAygqRba7kew5MKHbqACBxbqg2SAfAep9hYcgE9icTMK6wK9x9gnlFpibibJUiaI7Ez1c/640?wx_fmt=png)

不同方位下地磁旋转矢量传感器对CPU负载的响应

结合上图，作者进一步分析了传感器的时间窗口。Google Pixel 6a上相邻地磁旋转矢量传感器事件的间隔约为4.571毫秒，且传感器并非只在某个瞬间取样，而是对一个时间窗口内的模拟信号进行积分。通过改变工作负载相对于传感器事件的偏移，攻击者可以找出最佳对齐位置，把目标运算尽量放入有效测量窗口。这一步为后面的AES分析提供了时间同步基础。

**五、**

**两个攻击案例**

**（一）**

**远程像素窃取**

第一个案例面向浏览器中的远程攻击。攻击者控制一个恶意网页，并在iframe中嵌入来自其他站点的图片。浏览器的同源策略禁止JavaScript直接读取iframe内容，但并不阻止页面把内容显示出来。攻击代码使用CSS clip-path逐像素裁剪图像，把选中的1×1像素放大到256×256，再叠加多层SVG高斯模糊和随机噪声，使黑、白像素在GPU上的功耗差异被放大。

在渲染的同时，网页通过JavaScript通用传感器接口采样。论文发现两种可用的泄露原语：磁力计的振荡频率会随像素颜色改变；绝对方向传感器虽然数值变化不明显，但相邻读数的时间间隔会改变。攻击者据此对单个像素分类，再把结果拼回图像。

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwWHaQTnPTvrvvNZBDk5rCXzibKpHQ5lw9PP8ckSxyl1TygrbPJhUcqVh2YDtFrLkuKDH2MXdTENwTVt1dpFeic3xAE4mVbMgMdvs/640?wx_fmt=png)

基于传感器的端到端像素窃取流程

上图展示了端到端像素窃取的处理流程。研究团队重建了一幅48×48像素的Chrome标识。在Google Pixel 6a上，磁力计以5秒/像素取得90.2%的准确率，绝对方向传感器以10秒/像素取得70%的准确率；Samsung Galaxy S20 FE上的磁力计以10秒/像素取得89.2%的准确率。结果仍有随机误码，但轮廓已经清晰可辨，具体重建结果见下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwWxicrmHrYtEnsiadluodV5vM6RDFKptsn79FXjyU2mibaWIETwJUia6TG6rgo6WV6IAffdRtou19QSo9X5VHrWwp2UeHfsbNxK1rk/640?wx_fmt=png)

Google Pixel 6a上的Chrome标识重建结果

该远程案例并非对所有当前浏览器配置都无条件成立。论文的通用威胁模型使用Android 13和披露补丁前的Google Chrome 120；磁力计接口还需要浏览器中一次性启用相关标志，而绝对方向传感器在实验配置中无需额外权限。它证明的是跨源隔离之外还存在一条传感器功耗相关通道，而不是宣称任意网页都能立即高速读取任意图片。

**（二）**

**本地AES相关功耗分析**

第二个案例假设恶意应用已经被用户安装，并以前台应用或前台服务运行。应用不需要额外的用户授权即可读取研究所用传感器，同时能够向某个接口提交已知明文并触发AES-128加密。目标实现使用ARM NEON扩展中的aese和aesmc硬件指令，每次加密的周期数与输入无关；但周期恒定只能消除时间差，不能消除数据相关的瞬时功耗。

攻击者把每次加密与地磁旋转矢量传感器的有效测量窗口对齐，采集已知明文和传感器读数，再用AES第一轮S盒输出的汉明重量作为模型进行相关功耗分析。实验总计记录约3560万组样本，耗时44小时，过滤后使用1780万组。虽然相关系数只有10的负3次方量级，部分中间值仍具有明显统计显著性。

在最多30万样本的密钥排名实验中，部分字节（如第0、6和12字节）的正确候选能够收敛到稳定的低排名，但其他字节没有形成有意义的趋势，因此论文没有实现完整密钥恢复。这个结果更准确地说是“密钥复杂度削减”和单字节泄露的概念验证：信号很弱、采集成本很高，却已经足以说明普通传感器能看到恒定周期AES硬件指令中的数据依赖功耗。三个字节的排名变化如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwW5S9mToXo4w4WXT9YMpoWWNKZPcKLK6gLeoiaibpicqY0jRgIuZwVqiabUO3qf6U3VLeXd3V2W4YqJSdDTgf5Q1mcTLBfdVz0Rdj0/640?wx_fmt=png)

三个AES密钥字节正确候选的排名变化

**六、**

**安全启示与缓解措施**

**平台访问控制。**可以把高风险传感器放到权限提示之后，限制后台和网页访问，或降低采样率。但许多导航、健身和姿态应用依赖连续传感器读数，过度收紧会明显损害功能；权限提示也只能部分降低风险，因为用户仍可能授权。

**降低精度与加入扰动。**对传感器值做量化、舍入、限频或随机化能够压低信噪比，但粗粒度接口并不天然安全。论文在2024年2月向Google披露后，Google为Chrome的磁力计接口增加了额外舍入，并计划为方向传感器增加权限提示。这里描述的是论文记录的披露响应，不代表对当前所有版本状态的独立核验。

**硬件隔离。**更根本的办法是降低寄生耦合，例如加强屏蔽，或把传感器电路与CPU供电域分离。这样可以从物理源头削弱“CPU功耗变化进入传感器读数”的路径，但通常需要芯片和主板层面的重新设计。

**密码实现防护。**恒定时间和恒定周期仍然重要，但不能替代功耗侧信道对策。对于高价值密码操作，需要进一步采用掩码等算法级防护，减少中间值与实际功耗之间的相关性。代价是额外延迟、能耗和实现复杂度。

**七、**

**总结**

这项工作揭示了智能手机攻击面中容易被忽略的一层：一个接口即使没有输出功耗值，也可能因为物理耦合而成为功耗相关侧信道。9款手机和137个传感器的系统性测试说明，这不是某一个型号或某一颗磁力计的偶然现象；方向相关的地磁旋转矢量传感器泄露、跨源像素重建和AES密钥字节排名进一步展示了从统计相关到实际攻击原语的完整路径。

对系统设计者而言，安全边界不能只画在“权限允许访问哪些逻辑数据”上，还要考虑被允许的模拟信号是否携带了其他硬件模块的寄生信息。对密码实现者而言，恒定时间并不等于恒定功耗；对浏览器和移动平台而言，传感器精度、访问场景和硬件耦合需要被一起纳入威胁模型。

**参考资料**

[1] Mathias Oberhuber, Martin Unterguggenberger, Lukas Maar, Andreas Kogler, and Stefan Mangard. Power-Related Side-Channel Attacks using the Android Sensor Framework. Network and Distributed System Security Symposium (NDSS), 2025. DOI: 10.14722/ndss.2025.240092.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Vcvo4WRFGwVkgkXsqy67qYaQ1GVx3vwQSdgfznjLKKiaFO62N7looQTPUnR7W3ITYm1gKO91GPQL2ZpRZaHtMrCicpMyXlqBmtGzHl3mB6z2I/640?wx_fmt=png)

**往期精彩文章推荐**

* [基于单条功耗轨迹的芯片密码侧信道攻击研究](https://mp.weixin.qq.com/s?__biz=MzI2NTUyODMwNA==&mid=2247495909&idx=1&sn=e4bc4a9a1642bda2ed4a617b0349e425&scene=21#wechat_redirect)

* [利用RFM Rowhammer防御机制攻击GPU](https://mp.weixin.qq.com/s?__biz=MzI2NTUyODMwNA==&mid=2247496191&idx=1&sn=9448282cc0ddca4294f742371c1f3362&scene=21#wechat_redirect)

* [基于TLB侧信道攻击的稳定内核利用技术](https://mp.weixin.qq.com/s?__biz=MzI2NTUyODMwNA==&mid=2247496380&idx=1&sn=eff16cdb902e9d3bcf8c282d3c178dc5&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/Vcvo4WRFGwWu2g7phm0lLQrENxr23IdWGMe1iaaY1UN1dzkMbmcRx5zn16p60anlgJEWwqZeyYAiaMialNOicjclOvgibJIyibDJTLmnkNQY9XCAA/640?wx_fmt=png)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sSglg2t6pLdibP1eoMFnDyyCjXAfpDzbcSiahmcJJVCJGlVlhz3tn375M3T7671B9c4QAkhj2KBp6yynY1uOsU8w/0?wx_fmt=png)

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