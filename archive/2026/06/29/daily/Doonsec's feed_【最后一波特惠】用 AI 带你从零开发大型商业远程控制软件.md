---
title: 【最后一波特惠】用 AI 带你从零开发大型商业远程控制软件
url: https://mp.weixin.qq.com/s/ba09ozRWGT2pVWoxpoMyIg
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:06:44.725099
---

# 【最后一波特惠】用 AI 带你从零开发大型商业远程控制软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IRUJvvhticxTHEECuJxJBh2iaibLEpnpm9qiaiaEibzomfibyuGYaxbLKqdFGrgJthPGYtPL76dINeNaicnLnbib76F9S21RjhThhqNZsD8NJzVHo6iaI/0?wx_fmt=jpeg)

# 【最后一波特惠】用 AI 带你从零开发大型商业远程控制软件

原创

张小方
张小方

CppGuide

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

☁️ AI 开发训练营 · 跟着做，从零到一

用 AI 带你从零开发
大型商业远程控制系统

入云龙（ryl）是一套完整的远程控制系统：远程桌面、屏幕墙、文件管理、远程终端、音视频通话、系统管理一应俱全。

这门训练营带你用 AI 把它的开发过程拆成可跟随的课程——从服务器地基、连接通道，到主控框架、插件体系，再到多媒体大件，一节课对应一个真实里程碑。

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxQ61YO0ha7Zl1tHv8mw4JZqIhBicHfeeXM4iaOLroT0qviaFuVbYRZuMHkkqWK6GEqmjrxo1OGMFr1qKF6V0hicxLOwbagdbCGVroM/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| 7  课程阶段 | 30  实战课程 |
| 8  功能插件 | 48  开发里程碑 |

ARCHITECTURE

软件架构：四个进程协同

直连 → P2P 打洞 → 中转，逐级协商，哪条路通走哪条

🖥️ master 主控端

Qt / QML · 设备列表 · 功能 tab

↑↓
直连 / P2P 打洞 / 中转

|  |  |
| --- | --- |
| 🛰️ rylss  信令 · 撮合打洞 | 🔁 rylsr  中转 · 双向透传 |

↑↓

🧩 agent 受控端

Win32 自绘 · 单文件部署 · 插件托管

直连=最优 · P2P 打洞=次选 · 中转=兜底 · 信令负责撮合

DATA FLOW

一次会话是怎么建立的

从 agent 上线、master 查找，到逐级建链、开功能副连接

① agent 注册上线

向信令服务器上报设备 ID 与网络信息

② master 查找目标设备

向信令服务器请求目标 agent

③ 信令撮合

向双方下发对方地址

④ 尝试直连 / UDP 打洞

成功即建立链路（最优路径）

⑤ 打洞失败 → 走中转

按会话 ID 配对、接力转发

⑥ 控制主连接建立

加密信道，小而稳

⑦ 按需开副连接

屏幕 / 文件 / 升级 / 下载 …

⑧ 心跳 · 状态 · 数据流

画面与数据持续传输

主连接断开 → 该设备所有副连接与功能 tab 立即回收

FEATURES

训练营会带你做出这些功能

每个功能都是一节或多节实战课的产出

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxR4Dysp14PnfTC8XBq9c8GQ51qc7NZCm62TnsyibfdTlwoaDMZxMmvsBM0lHhL6je4hjxZyn68WI7a5PyRmlG4MkzKQItialDibqo/640?wx_fmt=png&from=appmsg)

📋 设备管理

所有 agent 在线/离线、延迟、分组一目了然，右键直达各功能

在线状态分组管理批量操作

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxTLOsVgibXW2cQGJbiaB8iciaACaW3jOjWS46lBssuXCcDC8128yicFp17Wpd0TN9vFJHx15wiaVbhibVDzRImTRAjVFRdD9fbFfGPook/640?wx_fmt=png&from=appmsg)

🖥️ 远程桌面

实时画面 + 键鼠控制，多显示器、清晰度档位、画质自适应

多屏清晰度档位剪贴板互传

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxSbYsWIJyx2CcicYib3wPibOJ0Wn00pTAFxeAbRSpBcFsbOevS87dML8iaonY8Qic93C8DDjz9UBugjiaOubNqic3RmOM6TfDWxUKttww/640?wx_fmt=png&from=appmsg)

🧱 屏幕墙

所有在线设备桌面缩略图栅格化，自动布局、双击进远程桌面

缩略图栅格拖动重排尺寸档位

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxQFHB2FzV4OPp0AOAbtXNwxW3fpgyWSE1HTpEL5MWicNy2zBzBsfCr8YO9Osx8wyBfwQYIfSEB4Xp3I0kdiamdPZhRzMRaRvMHe8/640?wx_fmt=png&from=appmsg)

📡 屏幕广播 / 中转

一块屏一对多广播，或在两台设备间中转画面，带源端授权

一对多源端授权广播录屏

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxTSAk89OChbibozgqeMeciahEvHmJhrFMUv1JjVsib2t9OAaOBKBRJ9y23slqwOSTjT6vkjVV7EdIoPJd9BTXWkxfzAvldHQKWoSk/640?wx_fmt=png&from=appmsg)

⌨️ 远程终端

在主控端操作远端命令行，实时输出、命令历史、中断

实时输出命令历史可选区复制

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IRUJvvhticxRSN3URIHA4meHEO3EqKgVY9w7L7TzsBxS9hicgSMeCZwDpAPvJEAR4oibIy54LKAzzjHUepZZJuLOy4PvXOTZ5x2MDHXvoUCrE0/640?wx_fmt=png&from=appmsg)

📁 文件管理

本地/远程双栏，单/多文件与文件夹整传，队列+断点续传

拖拽传输断点续传冲突策略

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxRPicwf4tDLGa1YicD9kFXjo7x2YfSucVIkN4ZU13oc5RudtYQakVEn4puknFN3VHgHfbemqzI7D58iaXobyxPib4s4mucFOMpREvU/640?wx_fmt=png&from=appmsg)

💬 远程聊天

文字/图片/表情/语音片段，图文混排，双端历史，撤回删除

图文混排历史持久化消息撤回

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IRUJvvhticxRC9jHicTR2MurWFzktvD7kprVq4pG2jzne7eQK6yDezU9Ae4Txj5I78e2f7UlTgdibCWXOxLc1grSIwtvafk3TRxlhetdYicURro/640?wx_fmt=png&from=appmsg)

🎥 音视频通话

双向语音 + 摄像头视频，振铃接听、计时、浮动置顶窗

双向语音摄像头浮动窗

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxQp5WwOrVd6iboNS05QanWVaDAsSjLt2AxaAReQotG5eRP4zGhr8s6oVM61CdcnhYuJCTyRjv0OkwW1xU51YiaJ0sLoic6LNQGIE0/640?wx_fmt=png&from=appmsg)

⚙️ 系统管理

一个插件托起 21 个运维子标签（见下方工具箱）

21 个子标签只读护栏二次确认

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IRUJvvhticxQZY6z889dUqk2Ct92UzDGPaEVYwhU4UKZibRKretFIkAkfzJicJDo0sWaLh7KHPN6Tj28poROFbYXsfu7iaW5oicGaIOWrq8cABc0/640?wx_fmt=png&from=appmsg)

🗄️ 注册表编辑

仿 regedit 的远程注册表：树形浏览、值增删改名、查找

树形浏览全类型值路径导航

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IRUJvvhticxTaxic4QQwhlH1YeRh8HtKXeNqQYCVxs7xxyPBnaudOxrn3n8gEolWwTYUpv6zF6nZM4U0XTxuLf3KL5egchPI6uE1fXc2iatlLw/640?wx_fmt=png&from=appmsg)

📢 公告下发

向设备推送公告，支持需确认回执、定时发送、草稿箱

需确认定时发送草稿箱

![](https://mmbiz.qpic.cn/mmbiz_png/IRUJvvhticxTthDaMPBc8TRy4icpM7DoIaJmq7ibaEfpougwN574EmdwWiaOWuNK5Vzx80HkA7VNiaibgk3fXsWIytyoLZE2r5Cv50qyyhbsl4dMQ/640?wx_fmt=png&from=appmsg)

🚀 升级 / 电源

新版本自我替换、回滚；远程重启/关机/休眠/锁屏与开机自启

批量升级电源控制开机自启

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IRUJvvhticxRChFtABApjmVh0Yic5MnMaVmjh1RiaESpFMASria6jaVPy71ADcSFEX82rzJ6y1MQRpicBiadswedPs3qZrGTTyXpUxxS8MHa5ztF4/640?wx_fmt=png&from=appmsg)

🔄 传输管理

升级/拉日志/拉dump/拉截图/HTTP下载 进度统一汇总

统一队列实时进度HTTP 下载

⚙️ 系统管理：21 个运维工具

全部跑在受控端进程内、零外部依赖，破坏性操作都有只读护栏与确认。

系统信息性能曲线进程管理服务管理窗口管理网络连接安装软件启动项设备管理磁盘空间分析/清理计划任务事件日志环境变量Hosts 文件防火墙规则用户与组共享会话/访问审计网络诊断安全体检网络适配器WMI 查询器

BOOTCAMP

开发训练营 · 课程大纲

七个阶段、三十节课，循序渐进

1打地基：规约与服务器

01**开发规范与项目蓝图**

里程碑 L01

02**信令服务器 rylss**

里程碑 L02–L04

03**中转服务器 rylsr**

里程碑 L02–L04

2连接三件套

04**master 主框架与设备列表**

里程碑 L05–L06

05**生成 agent 与直连**

里程碑 L07–L08

06**P2P 打洞**

里程碑 L09

07**中转兜底与降级编排**

里程碑 L09

08**多设备并存**

里程碑 进阶

3主控框架与设备运营

09**设备管理**

里程碑 L10–L14

10**审计日志与生命周期**

里程碑 L10–L14

11**批量操作**

里程碑 进阶

4插件体系

12**插件架构与副连接框架**

里程碑 L15–L18

13**远程终端插件**

里程碑 L19–L21

14**文件管理插件**

里程碑 L19–L25

15**注册表编辑插件**

里程碑 L19–L21

16**远程聊天插件**

里程碑 L19/L36+

17**系统管理插件**

里程碑 L41–L43

5安全与稳定

18**通讯协议加密**

里程碑 L30

19**数据压缩**

里程碑 L31

20**稳定性与优雅退出**

里程碑 L22–L29

6多媒体大件

21**远程屏幕：采集与编码**

里程碑 L32–L35

22**远程桌面：画面 + 键鼠**

里程碑 L33–L35

23**屏幕墙**

里程碑 L36–L40

24**屏幕广播 / 中转**

里程碑 L36–L43

25**屏幕录制**

里程碑 L36+

26**音视频通话**

里程碑 L36–L45

7运营增强与交付

27**公告下发**

里程碑 L36–L40

28**Agent 升级与电源**

里程碑 L41+

29**HTTP 下载与传输管理**

里程碑 L44–L45

30**整体优化与交付**

里程碑 L46–L48

ROADMAP

开发计划与当前进度

人工预估 vs AI 实际，每节标注里程碑 L 号

|  |  |  |
| --- | --- | --- |
| ≈250 人天  人工预估（约 12 人月） | ≈34 工作日  AI 实际投入 | ≈7×  综合提速 |

说明：两栏均为**据推测**的经验估值，仅供横向对比，非精确工时台账；L 号按提交记录归类（亦为据推测）。

1规约与地基 已完成

开发规范与项目蓝图

L01人工 2 人天AI 2 小时≈8×

信令服务器 rylss（注册/查找/撮合）

L02–L04人工 6 人天AI 6 小时≈8×

中转服务器 rylsr（按会话双向透传）

L02–L04人工 4 人天AI 4 小时≈8×

2连接三件套 已完成

master 主框架与设备列表

L05–L06人工 8 人天AI 1 天≈8×

生成 agent 与直连

L07–L08人工 5 人天AI 5 小时≈8×

P2P 打洞（NAT 穿透 + 可靠化）

L09人工 10 人天AI 1.5 天≈7×

中转兜底与降级编排

L09人工 5 人天AI 5 小时≈8×

多设备并存与多路复用

L09+人工 4 人天AI 4 小时≈8×

3主控框架与设备运营 已完成

设备管理（复制/分组/改名）

L10–L14人工 6 人天AI 6 小时≈8×

审计日志与生命周期

L10–L14人工 3 人天AI 3 小时≈8×

批量操作（多选群发）

L14+人工 4 人天AI 4 小时≈8×

4插件体系 已完成

插件架构与副连接框架

L15–L18人工 8 人天AI 1 天≈8×

远程终端插件

L19–L21人工 5 人天AI 5 小时≈8×

单会话 cmd实时输出命令历史中断可选区复制导出 txt

文件管理插件

L19–L25人工 10 人天AI 1.5 天≈7×

本地/远程双栏上传/下载文件夹整传断点续传传输队列限速冲突策略拖拽历史

注册表编辑插件

L19–L21人工 5 人天AI 5 小时≈8×

五根树形浏览8 种类型值增删改名地址栏直跳递归查找64 位视图

远程聊天插件

L19/L36+人工 8 人天AI 1 天≈8×

文字图片图文混排语音片段抖一抖已读回执撤回历史未读角标

系统管理插件（21 个运维工具）

L15–L18/L41–L43人工 20 人天AI 3 天≈5×

系统信息性能曲线进程服务窗口网络连接安装软件启动项设备磁盘清理计划任务事件日志环境变量Hosts防火墙用户与组共享审计网络诊断安全体检网络适配器WMI 查询

5安全与稳定 已完成

通讯协议加密

L30人工 8 人天AI 1 天≈8×

数据压缩

L31人工 4 人天AI 4 小时≈8×

稳定性与优雅退出收口

L22–L29人工 5 人天AI 5 小时≈8×

6多媒体大件（远程屏幕/音视频） 已完成

远程屏幕 · 采集与编码（多重兜底）

L32/L44人工 12 人天AI 2 天≈6×

DXGI 采集GDI 兜底WGC 双显卡MF H.264openh264 兜底分片传输

远程桌面（画面 + 键鼠）

L33–L35人工 8 人天AI 1 天≈8×

实时画面键鼠控制多显示器清晰度档位缩放全屏截图统计

屏幕墙

L36–L40人工 6 人天AI 6 小时≈8×

多 agent 缩略格共享采集复用自动布局拖动重排双击进桌面

屏幕广播 / 中转

L36–L40人工 8 人天AI 1 天≈8×

一对多广播设备间中转源端授权接收窗控制推系统声/麦克风推摄像头

屏幕录制 / 广播录制

L36+人工 5 人天AI 5 小时≈8×

零重编码→MP4IDR 锚点分辨率锁定暂停/恢复广播录屏

音视频通话（voice-chat 插件）

L36–L45人工 14 人天AI 2.5 天≈6×

振铃接听双向语音双向视频摄像头静音系统混音语音升级视频通话录制浮动窗

7远程运维与运营增强 多数已完成

Agent 升级（下发/自替换/回滚/批量/提权重启）

L41+人工 8 人天AI 1 天≈8×

拉取 agent 日志

L41+人工 4 人天AI 4 小时≈8×

拉取崩溃 dump（自动 minidump + 拉取）

L44+人工 5 人天AI 5 小时≈8×

拉取屏幕截图

L44+人工 3 人天AI 3 小时≈8×

HTTP 下载（边下边传）

L44–L45人工 6 人天AI 6 小时≈8×

传输管理（统一汇总）

L44+人工 4 人天AI 4 小时≈8×

master 截图标注工具

L44+人工 6 人天AI 6 小时≈8×

公告下发（需确认/定时/草稿箱）

L36–L40人工 5 人天AI 5 小时≈8×

电源与启动（重启/关机/休眠/锁屏/开机自启）

L41+人工 3 人天AI 3 小时≈8×

网络监视器（连接/吞吐/RTT，真机待验）

L41+人工 6 人天AI 6 小时≈8×

8整体优化（进行中） 进行中

性能打磨与卡顿优化

L46–L48人工 5 人天AI 5 小时≈8×

真机回归与排障

L46–L48人工 6 人天AI 1 天≈6×

代码整体优化收口

L46–L48人工 5 人天AI 5 小时≈8×

9v1.0 交付（规划中） 规划中

全功能真机回归

待发布人工 8 人天AI 待评估

打包分发与文档完善

待发布人工 4 人天AI 待评估

10展望 · 后续版本方向 候选

性能监控总览、远程桌面键鼠控制完善、更多系统管理工具等（待定，暂不估时）

QUALITY

代码质量如何保证

不是“能跑就行”——从架构经验到流程纪律，七条共同兜住质量底线

01十多年商业项目架构经验

主导过多个大型商业项目的架构设计，提前知道坑在哪、边界怎么划。

02测试用例全覆盖

开发过程中关键路径与边界条件都有测试用例兜底，不留裸奔的代码。

03测试先行，再动代码

设计功能先把测试用例跑起来确认现状，验证...