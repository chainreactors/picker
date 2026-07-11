---
title: GigaWiper 利用 OneDrive 更新计划任务进行持续破坏性访问
url: https://mp.weixin.qq.com/s/Sv-X6DpQ7-Dy1W2z7JkICA
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:57:49.812393
---

# GigaWiper 利用 OneDrive 更新计划任务进行持续破坏性访问

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PryP5BylpgG510KicUUUVib791Hnw01dFVrSFqtI9WQv4lxPEGFb4oZGsclHeOOLebGsCJHrzWuoPlWtInlZomsA1sziabg1HBk4/0?wx_fmt=jpeg)

# GigaWiper 利用 OneDrive 更新计划任务进行持续破坏性访问

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一个名为 GigaWiper 的复杂基于 Golang 的后门家族，它将广泛的 C2 控制与多个破坏性有效载荷融合在一起。

GigaWiper 的显著之处不仅在于其破坏能力，还在于它将几个以前独立的擦除器和勒索工具集成到一个模块化植入体中。

这种整合使运营商能够按需切换销毁模式，例如物理磁盘擦除、使文件无法恢复的伪勒索软件、多遍安全擦除，同时保持持久的远程控制访问。

观察到的一种持久化机制看似简单：该植入程序创建一个名为“OneDrive Update”的计划任务，并使用 HKCU\SOFTWARE\OneDrive\Environment 中的注册表项来跟踪执行情况。

首次运行时，它会写入密钥并创建OneDrive 更新计划任务，该任务配置为每分钟运行一次并在启动时运行。

后续运行会检测注册表值，将其递增，并像预期的计划任务子进程一样运行——这种操作选择可以减少怀疑，并利用受信任的 Windows 计划程序进行持久的破坏性访问。

独立组件通过 WMI 主动枚举物理磁盘，识别 Windows 安装驱动器，使用 DeviceIoControl (IOCTL\_DISK\_CREATE\_DISK) 从非系统驱动器中删除分区元数据，使用随机化首字节缓冲区以大块覆盖原始磁盘扇区，并强制立即重新启动。

后门中嵌入的命令 1（WipeMain）功能相同，而命令 12（WipeCMain）提供仅针对 C 盘的多遍安全擦除。

第三个破坏性命令重现了 Crucio 衍生的逻辑：一个“勒索软件”例程，使用 AES-CBC 加密随机生成的密钥（永远不会保存）加密文件，将受害者的文件重命名为 .candy 扩展名，并且不留下任何可行的恢复路径，实际上是一个伪装成勒索的擦除器。

微软威胁情报发现， GigaWiper 主要以两种样本形式出现：紧凑的独立擦除器和更大的 Golang PE 后门，后者将独立代码作为命令包含在内。

## **GigaWiper 使用 OneDrive 更新**

C2 和运行遥测功能十分强大。GigaWiper 使用基于 AMQP 的 RabbitMQ 进行命令分发，并使用 Redis 进行状态和输出报告。

后门中实现的擦除器主程序是 rabbit\_tools\_tool\_wipe\_main.WipeMain 函数。

该植入程序解密了包含 C2 端点和凭据的硬编码 AES 保护配置；观察到的基础设施包括非标准端口上的地址，例如 185.182.193[.]21。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Nz3kzQ7gXCyg8keGVz3lPzu2STlgeFcxianfwRSq9aje7bDhvhINAASBcCKt6h3pghQmKajnzdlfJ8WicCSpeM6QX79PyfAet30/640?wx_fmt=jpeg)

RabbitMQ 设计使用名为“All”的扇出交换机进行广播命令，使用名为“Topic”的主题交换机进行目标任务，命令被建模为结构化的 Task 和 Result 对象。

这种消息传递方式可以对多个受感染主机进行控制，同时在需要时可以针对单个主机进行定向。

除了擦除和伪造赎金功能外，GigaWiper 还实现了广泛的远程访问和系统管理功能：进程和服务管理、注册表导航和持久会话、通过 MinIO 客户端上传文件、屏幕截图和屏幕录制、键盘记录器和类似 VNC 的远程控制、事件日志清除。

代码重叠和共享字符串将 GigaWiper 与至少三个先前的系列联系起来：一个独立的擦除器、类似 Crucio 的勒索代码（BigBangExtortMain）和 FlockWiper，后者从 C 重新实现为Golang 访问，以便作为 WipeCMain 包含在内。

PDB 路径工件引用“GRAT”进一步将这些组件联系在一起，并表明不同迭代版本之间存在共同的开发者或框架。

防御者应优先阻止已识别的 C2 基础架构，强制执行防篡改保护和始终在线的 EDR，并防止从非特权上下文中创建未经授权的计划任务和修改注册表。

微软在其 GigaWiper 安全公告和 Defender 遥测数据中发布了检测和缓解措施；各组织应将这些指标映射到网络和终端控制，并启用云交付的保护措施，以捕获不断演变的变种。

GigaWiper 攻击活动凸显了一种转变：破坏性工具正从单一用途的擦除转向模块化、远程协调的平台，这些平台将隐蔽的持久性（例如“OneDrive 更新”计划任务）与按需使用多种可互换的擦除技术的能力相结合。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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