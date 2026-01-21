---
title: 银狐木马攻击常用的高级进程注入方式
url: https://mp.weixin.qq.com/s/21YjeqhSBEcdSWmbcm3YEw
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:30:56.120285
---

# 银狐木马攻击常用的高级进程注入方式

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rSuZI9Hg5ldFcp7KH6QpXy5j0VmC8EzYdVr6Ey3X09Qg0R0oI1zA831pLOMHyj8vpf082iaNk4gpGz5jGibY9lSg/0?wx_fmt=jpeg)

# 银狐木马攻击常用的高级进程注入方式

cyberpanda
cyberpanda

SOC安全分析之旅

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/rSuZI9Hg5ldFcp7KH6QpXy5j0VmC8EzY0Wj0estuibTtY93EExuYibWUjvCpJYNs3rXKoXj1lNgp0pSDx5nZ86IQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/rSuZI9Hg5ldFcp7KH6QpXy5j0VmC8EzY18LeicutaYT54cQoKQwsk8SJAcwF8a02ZkFx5FLADvgxyR0gQpTUMlg/640?wx_fmt=gif&from=appmsg)

目前最典型的 “普通注入”，是 以 CreateRemoteThread （远程创建线程）为核心的注入方式；而银狐等高级威胁组织常用的，则 是 MapViewOfSection + RemoteSetThreadContex t 组合的 “高级注入”。两者在关键操作上差异显著：

01

内存传递恶意代码的方式不同

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rSuZI9Hg5ldFcp7KH6QpXy5j0VmC8EzY9icwRyeVmicqOhYbicia5ec1clEvkCBZEvtQ1xNBEZMvEjI2ogUWSPARyw/640?wx_fmt=png&from=appmsg)

普通注入（ 以 CreateRemoteThrea d 为例） ：采用 “显式写入” 逻辑，分两步操作。首先通 过 VirtualAllocEx API 在目标进程的地址空间中，申请一块空白内存；接着调 用 WriteProcessMemory API，将恶意代码直接 “写” 进这块空白内存。整个过程相当于 “明着给目标进程塞东西”，操作痕迹直接可见，容易被安全工具捕捉。

高级注入（ MapViewOfSection + RemoteSetThreadContext ） ：采用 “内存映射共享” 逻辑，无需显式写入。通 过 MapViewOfSection API，将恶意代码所在的内存区段（比如内存马、无文件形态的恶意程序），直接 “映射” 到目标进程的地址空间中。这相当于 “偷偷共享一块内存，让目标进程自己读取恶意代码”，全程没有明显的 “写入” 操作痕迹，更难被察觉。

02

触发恶意代码执行的方式不同

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rSuZI9Hg5ldFcp7KH6QpXy5j0VmC8EzY9icwRyeVmicqOhYbicia5ec1clEvkCBZEvtQ1xNBEZMvEjI2ogUWSPARyw/640?wx_fmt=png&from=appmsg)

普通注入（ 以 CreateRemoteThrea d 为例） ：依赖 “新建线程” 触发。调 用 CreateRemoteThread API 在目标进程中，直接新建一个独立线程，然后让这个新线程专门执行注入到内存中的恶意代码。这种方式相当于 “给目标进程新增一个‘打工仔’，让它干坏事”，而 “远程创建线程” 的行为是安全软件重点监控的高危操作，新线程的创建记录很容易被捕捉。

高级注入（ MapViewOfSection + RemoteSetThreadContext ） ：依赖 “劫持现有线程” 触发，不新建任何线程。通 过 RemoteSetThreadContext API，修改目标进程中已存在的某一线程的 “上下文”—— 比如将线程的指令指针（ RIP/EIP ）强行改成恶意代码的内存地址。当这个被修改的线程下次被系统调度运行时，就会 “不知不觉” 地从原本的正常代码，切换到恶意代码的执行逻辑。整个过程相当于 “拐走目标进程原本的‘打工仔’，逼它干坏事”，没有新线程创建记录，行为更贴近进程正常运行逻辑。

03

隐蔽性与被检测概率不同

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rSuZI9Hg5ldFcp7KH6QpXy5j0VmC8EzY9icwRyeVmicqOhYbicia5ec1clEvkCBZEvtQ1xNBEZMvEjI2ogUWSPARyw/640?wx_fmt=png&from=appmsg)

普通注入（ 以 CreateRemoteThrea d 为例） ：痕迹明显，被检测概率高。一方面，“远程创建线程” 是所有安全软件（尤其是 EDR 终端检测与响应工具）重点拦截的高危行为，几乎没有规避空间；另一方面， WriteProcessMemor y 的跨进程写入操作，会触发内存修改告警，一旦目标进程是系统核心进程（ 如 svchost.exe ），这种写入行为会立刻被标记为异常。

高级注入（ MapViewOfSection + RemoteSetThreadContext ） ：极度隐蔽，被检测难度高。首先，没有新线程创建记录，仅修改现有线程的上下文，操作逻辑与进程正常运行时的线程调度差异极小；其次， MapViewOfSectio n 本身是 Windows 系统的常规功能，常用于实现文件共享、进程间数据交互等合法场景，安全工具很难直接判定这种操作是恶意的；最后，这种注入方式可实现 “完全无文件落地”—— 恶意代码全程只存在于内存中，不生成任何独立的恶意文件，彻底规避了传统的 “文件查杀” 机制。

04

高级威胁组织的选择：为什么偏爱高级注入？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rSuZI9Hg5ldFcp7KH6QpXy5j0VmC8EzY9icwRyeVmicqOhYbicia5ec1clEvkCBZEvtQ1xNBEZMvEjI2ogUWSPARyw/640?wx_fmt=png&from=appmsg)

以近期活跃的银狐组织为例（该组织常针对政企、能源等关键行业发起定向攻击），其之所以频繁使 用 MapViewOfSection + RemoteSetThreadContex t 组合的高级注入，核心原因就是 “对抗检测”—— 通过更隐蔽的操作逻辑，突破系统的多层防御体系。

银狐的典型攻击流程可拆解为以下 5 步：

1. 伪装诱骗 ：将恶意代码打包成 “WPS 安装包”“办公模板”“系统补丁” 等具备合法外观的文件，通过邮件附件、钓鱼链接等方式，诱导目标用户点击运行；
2. 前置突破 ：恶意程序运行后，先执行一系列 “破防” 操作 —— 比如通过漏洞添加管理员权限、修改安全软件（如 Windows Defender）的排除路径、禁用系统自带的安全防护功能，削弱目标设备的防御能力；
3. 内存映射传递代码 ：调 用 MapViewOfSection API，将内存中无文件形态的恶意代码，映射到目标合法进程（ 如 explorer.exe ）的地址空间，完成恶意代码的 “隐蔽投递”；
4. 线程劫持执行 ：通 过 RemoteSetThreadContext API，修改目标进程中某一现有线程的上下文，将线程的执行逻辑 “拐向” 恶意代码，触发恶意行为；
5. 隐蔽控制 ：恶意代码以合法进程的身份，发起数据窃取（如读取敏感文档、收集系统信息）、远程控制（如建立反向连接、接收攻击者指令）等操作，系统日志中仅会记录合法进程的行为，极大增加了攻击溯源的难度。

对比普通注入，高级注入能帮银狐规避 90% 以上的常规检测 —— 没有新线程创建、没有显式内存写入、没有恶意文件落地，整个攻击流程完全贴合系统正常运行的逻辑，让攻击行为像 “隐身” 一样，很难被目标察觉。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rSuZI9Hg5leysNlQzCqwjzznXDSNxEicPLlSj1GsPIm9D7wSysDvtcHqEia3eJbAXZBkORTf2YOqo6GQJXJZibIkQ/0?wx_fmt=png)

SOC安全分析之旅

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rSuZI9Hg5leysNlQzCqwjzznXDSNxEicPLlSj1GsPIm9D7wSysDvtcHqEia3eJbAXZBkORTf2YOqo6GQJXJZibIkQ/0?wx_fmt=png)

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