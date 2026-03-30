---
title: 为C2扫清障碍：从 DLL 劫持到无感知强制kill360所有进程
url: https://mp.weixin.qq.com/s/pjlIGf3q0pFRvqQQLutD7A
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:41:36.795296
---

# 为C2扫清障碍：从 DLL 劫持到无感知强制kill360所有进程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cGhMn4Bj3bbT0VEeOicoociaWlqZibf0d3OricoFH1meN5f1lDHUBo00Tr6IdB4NkWVFY3PnIDxw79gR1H2u85XE8icLJHOftQn8wR6yoXicibsozs/0?wx_fmt=jpeg)

# 为C2扫清障碍：从 DLL 劫持到无感知强制kill360所有进程

原创

信益安研究院
信益安研究院

信益安信息安全研究院

![]()

在小说阅读器中沉浸阅读

当防线被物理抹除，原本被秒杀的 C2 瞬间化身为终端安全的利剑

测试流程

1.这里我们先放一个C2生成的原生后门，被360检测到是恶意后门程序

![ac51eea770c254e968ee1aa430869e8d.png](https://mmbiz.qpic.cn/mmbiz_png/T5wSZNgEHntdWbkmEsccHmEI9avk3vaz7gEMaACiaQeZybWKeGsVL8mJOd6XBq55vwwof6Iza4icvu6EWJCicsBvKwarKpKwM6PqW9dV2hMXf0/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

2.我们用此项目已处理的白加黑程序经过扫描也是成功bypass了360， 360相关程序后台也是还存在的

![ecd84b28bb43a82eff9630cdfc893285.png](https://mmbiz.qpic.cn/mmbiz_png/T5wSZNgEHnsfqAHAHU0nbyBSTVhgAiaUnMgNGdt6K4vh58czVI3doEic7nYqf7ZHZalElbGd9R2QA363C5yyBnmW3ciaVPa5tWH5icD0dcgIZ98/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

3.此时我们以管理员运行我们白加黑的程序，**发现360进程全部被kill掉了！并且我们重新启动360，也无法启动！**

![7300a1097f5f4c5a3333d9890c744aec.png](https://mmbiz.qpic.cn/sz_mmbiz_png/T5wSZNgEHnsCrPQlaan7njVXKXsicvAUX7SUibqTYJ5q2JbxbiaKnD61RS4JlplhwSf7t39oEquaicfXmoHZE2sfqsibIv5FYoa6KxicMviaIdYrlc/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

4.现在我们再次把原始的后门程序放进去运行发现也平安无事，原始的后门直接上线

![1d0b904eb3dd07e125c11b90c9baf0d2.png](https://mmbiz.qpic.cn/mmbiz_png/T5wSZNgEHnuY55qQfP5cfKwafBt5icsKiazUxMOibRU5LkbIr7MSCywRAMzLdTCXGgzSibrxVxSK4miaCCc7NYwUqIjOciaofGibKkAGVbfGKf9QO4/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

![a762d01ea4dc068e7e4563f22ec0cbb3.png](https://mmbiz.qpic.cn/mmbiz_png/T5wSZNgEHnsNG6EAibjrAmFhfsNibfFuYPJPXZ1cJI8ibUcowbR5lwtlw3QqxPicXkUCcmRRkENOTS77C8DWFceiaIhNSLs5wm6QEQGTuNeicXamo/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

核心技术揭秘

本方案之所以能在高强度防护环境下实现 C2 稳定上线，核心不在于特征码的反复混淆，而在于一套**基于底层逻辑对抗的多阶段执行链路（Multi-stage Execution Chain）**。

#### 1. 载体侧：基于 DLL Side-Loading 的白加黑驻留

放弃传统的独立 PE 文件运行模式，采用 **DLL 劫持（DLL Hijacking）** 技术。

* **技术实现**：针对特定白名单程序（如 `Arduino IDE.exe`）的依赖加载路径进行劫持，通过恶意 `ffmpeg.dll` 实现代码执行流的寄生。
* **战术优势**：利用高信誉度数字签名进程作为宿主，规避了 EDR 对未知不可信进程的静态启发式扫描与初始行为监控。

####

#### 2. 对抗侧：动态环境溯源与反沙箱自检（Anti-Analysis）

载荷（Loader）在触发核心逻辑前，预置了严格的**环境探测模块**。

* **技术实现**：通过遍历进程环境块（PEB）实时校验父进程身份及执行路径。
* **战术优势**：若识别到执行环境为自动化沙箱或非预期宿主，载荷将立即转入“静默混淆”状态，仅执行合法的 DLL 导出函数，从而规避安全厂商的自动化样本捕获与逆向分析。

#### 3. 通道侧：防御层级致盲（Patching ETW）

在发起敏感操作前，首先对系统的监测“神经”进行手术级阻断。

* **技术实现**：通过内存补丁技术强制 Patch 内核事件跟踪机制（**ETW**）的核心函数 `EtwEventWrite`。
* **战术优势**：此举直接切断了应用层行为上报 EDR 核心驱动的通道。即便后续产生高危动作，防御组件也因失去底层事件流支持而陷入“逻辑致盲”状态，无法生成有效报警日志。

#### 4. 执行侧：高特权级进程收割与动态 API 解析

这是整套方案的“物理清场”环节，旨在彻底移除防御干扰。

* **技术实现**：利用 `RtlAdjustPrivilege` 提权至系统级调试特权（**SeDebugPrivilege**），并采用**无 API 特征**的动态解析技术（通过遍历导出表哈希定位函数地址），避开 IAT 特征监测。
* **战术优势**：程序内置 100ms 级别的毫秒级轮询监控，针对目标防护进程实施强制终止（TerminateProcess）。通过先物理清场，后内存上线的降维打击逻辑，为 C2 载荷开辟绝对真空的运行环境。

**学习杀软致盲技术**

很多人执着于把 C2 的特征码改得天衣无缝，但真正的老手知道：**与其在防线下反复试探，不如直接让防线消失。**

在我的测试中，原生 C2 上传即被扫描拦截。但当我祭出这款 **Rust 编写的白加黑 Killer** 后，情况瞬间反转——

1. **白加黑启动**：劫持 Arduino IDE，在杀软眼皮底下完成特权提升。
2. **强制收割**100ms 循环扫描，360 核心进程被瞬间终止。
3. **丝滑上线**：当那个熟悉的图标消失时，我的 C2 控制台秒弹 Session，全程再无阻碍。

这，就是**底层对抗**的魅力。

*（此项目不适用于360核晶）*

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bYDpdtf0Ogib8YCS4IExdPogAvA1oCibXeA227DzXzn2dRYJ0ARFRRvdO3Rsm5ColLialnVdaZl6kHQkl9Hxm9DB4tVy2heicrDvNU/640?wx_fmt=png&from=appmsg)

*核心技术细节已在【纷传】独家解锁*

# 最后

🌟感谢您看到这里，您的支持与关注，是我们持续输出内容的最大动力

🌟欢迎加入我们的交流群

![](https://mmbiz.qpic.cn/mmbiz_png/cGhMn4Bj3bZqQogYVT5KiaHO3ia1iaOxDnXnaL8oT2MlQib8Ow1nucRrNqbmQpxPcTFTrUcDm9yZKup61jAGGGef5bDXajZLbctdNEWbz1YPssU/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QuEg2icmqMJN031QmqC3zSSEqFE7RmUhmgcPTFGGHIofVlkhte6tRlku5hMKHfMWbOoeOSzfs9CcypicibwibvDGeQ/0?wx_fmt=png)

信益安信息安全研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QuEg2icmqMJN031QmqC3zSSEqFE7RmUhmgcPTFGGHIofVlkhte6tRlku5hMKHfMWbOoeOSzfs9CcypicibwibvDGeQ/0?wx_fmt=png)

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