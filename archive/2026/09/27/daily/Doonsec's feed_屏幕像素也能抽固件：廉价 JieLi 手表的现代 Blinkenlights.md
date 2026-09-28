---
title: 屏幕像素也能抽固件：廉价 JieLi 手表的现代 Blinkenlights
url: https://mp.weixin.qq.com/s/hsjGXgJObYtLy9ktcLrQ-g
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:54:58.860249
---

# 屏幕像素也能抽固件：廉价 JieLi 手表的现代 Blinkenlights

# 屏幕像素也能抽固件：廉价 JieLi 手表的现代 Blinkenlights

黑卷
黑卷

赛博安全攻防日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 屏幕像素也能抽固件：廉价 JieLi 手表的现代 Blinkenlights

Quarkslab 的 Damien Cauquil（与 Thomas Cougnard / Xilokar）在 leHACK 上讲过这条线：一块约 **12 欧元** 的廉价智能手表，官方烧录器要等几周才到货——于是他们走出一条「现代 Blinkenlights」路径：**表盘解析越界读 → 把任意内存当 RGB565 像素画上屏 → 用 Raspberry Pi Pico 从屏幕总线把像素抓回来拼固件**。下文按防御视角摘关键方法与发现，完整代码与细节以原作者公开材料为准。

## 开箱：传感器可能是「样子货」

2024 年底他们在本地超市看到标价约 €11.99 的小智能手表，买了三块拆开看。血压、睡眠之类读数很离谱——原因很直接：贴近腕部、靠光反射测量的那类传感器，这块表里基本没有。

![表背「传感器」其实像焊在柔性板上的 LED](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84UJmNIpgushryTogWhWr99khBTs7xfKMaHghA3xmrh2fuoq2VCYQyhSMVGabN8SRiclrbRzb9WoGgwOwXoNA6CF8Z1frB8XiaaTY/640?wx_fmt=jpeg&from=appmsg)

*所谓传感器，看起来更像焊在柔性 PCB 上的 LED……*

## 先找固件出口：杰理 SoC，但官方烧录器太慢

PCB 上是一颗 **杰理（JieLi）** SoC（板级丝印约 AC6958C6）。杰理芯片丝印常不直接对应型号；板子上有 **DP / DM** 测点，暗示隐藏 USB 数据脚曾用于烧录。官方编程器在电商上约四周才到，DIY 方案又对这块目标无效——于是一边等货，一边从官方 App / BLE 找旁路。

![手表主 SoC（杰理）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84UibOcaWqxDIeAmYK0ojMftt59lQPtUwDwwDbdp5ktiaYfNkVdzyG3IUHVP7vgJe1rQicJVY0hhQTtxVWrO0oQeicYoMEcoMzDOZ1k/640?wx_fmt=jpeg&from=appmsg)

*主控 SoC（杰理 AC6958C6 一类）*

官方 App 能配对，但**看不到固件版本，也没有 App 内 OTA 升级入口**。倒是有个表盘商城：免费表盘可下载并推到手表，上传约两分钟后能正确显示。

![LeFun 表盘商城](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84UvRCkzoD5f1hNaZ24niaicRON9KXdnFftj7gjzPexIAN9pwl9PNhMHvPeAWvJ44wK5A6l2gJicdjnDmmLWmBlqy61JUgLhc2r2so/640?wx_fmt=jpeg&from=appmsg)

![表盘上传中](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84WygIDmsYw2npkMI9te6EVrSBHTuS7LibxyeKw3ZcaNMgr1grVLgn2xibmJSMYOExR9SWzPMYOjjYyUkRvz6kEjCxUPQ6gBbNjuo/640?wx_fmt=jpeg&from=appmsg)

![表盘已安装显示](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84Vfsd2HssgTnPS2IkmzISsEeBYN2epeAiafjkwVlPaKKUfRibq856xOVyyKwTaQOd7Eiajd2ciatHISUsNxW4kVWYXaw7t0ysL4udE/640?wx_fmt=jpeg&from=appmsg)

用 nRF Connect 可见设备走 **BLE**，默认 MTU 23，解释了上传为何偏慢。杰理公开仓库里的 `Android-JL_OTA` 能识别这块表为「兼容设备」——说明 GATT 上至少挂着 OTA 相关服务。Logcat 里握手很吵，能看到 `pass`（`02 70 61 73 73`）一类互认步骤。

## OTA 鉴权：复用了蓝牙遗留 E1，但抽不出固件

顺着 `RcspAuth` 一类类名逆向 APK / 原生库后，作者发现挑战应答落到了蓝牙规范里的 **E1 遗留认证算法**：硬编码的 6 字节「身份」+ 16 字节密钥 + 随机挑战，算出 SRES。实现上近似「带固定盐的哈希」，**抗不了转发 / 重放 / MITM**——攻击者甚至不必知道密钥，只要拿合法表转发挑战即可骗过 App。

![蓝牙遗留 E1 认证示意](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XicVvkXMZG9ZYHoeBuff55JRMZEibmaaBpHSPmvibK9UBiam2HUm5dqPPsMXKBvZnoNDv9nkOS8LCOibAztTahVtSRzHZPbGQOlUU4/640?wx_fmt=jpeg&from=appmsg)

*蓝牙遗留认证（E1）机制示意*

用公开的 E1/H 实现（如 BIAS 研究相关代码）加硬编码常量，可复现 logcat 里的应答；再用 WHAD 脚本完成握手。**结果却是：OTA 通道能进鉴权，但没有「从设备读出完整固件」的接口。** 这条线到头了。

## 失败是常态：把目光转向表盘与 Blinkenlights

安全研究里常有这种「深挖到死胡同」。2002 年 Loughry / Umphress 的 *Information Leakage from Optical Emanations*，以及 lcamtuf《Silence on the Wire》里讲过的故事提醒他们：很多设备曾把流量直接驱动到 **blinkenlights（指示灯）**，光学侧信道就能泄数据。OTA 不给固件？那就看表盘上传与屏幕输出。

## 空中抓表盘：鉴权居然是同一套

用 WHAD 把官方 App 上传免费表盘的 BLE 流量抓成 PCAP，又看到熟悉的 `02 70 61 73 73`：

![上传表盘前的 pass 通知](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84V9NyAkgKcJ8HrvVn3PMwQLluiaTY1UvktskZ3nicMWiclGj9LaNAxCBCFDdW0icwAK5KBs0WEwgmTAfR27hxOh5Ghq1qLM9ibia0rics/640?wx_fmt=jpeg&from=appmsg)

*又是熟悉的 `pass`——表盘上传前走同一套互认*

鉴权通过后，表盘按特征写入分块发送：首包带魔数与块数、Dallas 8-bit CRC；后续块约 **16 字节** 载荷。作者据此写脚本还原多个表盘文件，做差分分析猜格式。

首包结构（摘要）：

| 偏移 | 长度 | 含义 |

| --- | --- | --- |

| 0x00 | 3 | 魔数 `AB 06 28` |

| 0x03 | 2 | 后续块数（大端） |

| 0x05 | 1 | 前序字节的 Dallas CRC8 |

数据块（摘要）：魔数 `AB 29` + 块序号 + 16 字节数据。

## 表盘格式：区域描述 + 偏移，没有可执行代码

对比多个表盘后发现：动画并不靠表盘里嵌代码，而是固件内置能力（时、分、指针钟、电量条、静态图等）。每个 **region** 带坐标、宽高与类型相关字段；像素可用 **RGB565** 等格式。关键点：头部用 **偏移** 去定位后续数据——经验上，缺边界检查时，偏移一旦指到文件外，解析器可能读到**任意内存**，再原样送给屏幕。

![自定义表盘文件结构](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XGLUFDbVvnHuWEA4e7ss5VB3Qgibf1MiblfvmQkoibiafz686oSQibpwJG5zNvRhsLwWiaMb0tPibU36RBfTaV8s7JI53D9AiadTgoia64/640?wx_fmt=jpeg&from=appmsg)

*表盘文件结构示意：头 + 区域描述 + 数据区*

## 自制表盘验证，再故意搞坏偏移

先按理解拼一个只显示一张 RGB565 图的合法表盘（屏幕约 240×286），用 WHAD 鉴权后上传。首轮因连接 hop interval 过大超时；缩短连接事件间隔后上传成功，确认格式与协议理解正确。

接着只改图像区偏移，做「坏偏移」表盘。Thomas（Xilokar）试出若干**不立刻变砖**的偏移——屏幕上出现「雪花」般的噪声像素：解析器**没校验偏移是否仍在表盘缓冲区内**，把读到的内存当像素刷到 TFT。

![坏偏移表盘：屏幕显示噪声像素](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84XVfvxI3jF0EwQ7FFpvbPFeJUtkHrA6rgsKsxkukmJ0hyiaiaRZGk2GbxuVvqoO3LagLXl2wOGicpG1KXwL2icKMVibl7xFPt2Yfub8/640?wx_fmt=jpeg&from=appmsg)

*坏偏移导致屏幕刷出「内存当像素」的噪声（图源：Thomas Cougnard）*

这一刻目标就清楚了：**现代 Blinkenlights——屏幕本身就是泄密信道。**

## 现代 Blinkenlights：光学难，走屏幕总线更稳

旧论文盯 LED；这里 TFT 上是标准 RGB565 像素，直接来自 SoC 内存。Thomas 尝试光学抓取整屏 LED 矩阵，装配复杂且难稳定。Damien 换思路：识别控制器（常见 ST7789 / ILI9341 一类，最终通过 Read Display ID `0x04` 响应锁定为 **NV3030B**），用逻辑分析仪 / Pico 抓 SoC→屏的串行总线。

便宜分析仪 8 Ms/s 跟不上；改用基于 **Raspberry Pi Pico、约 100 Msps** 的开源逻辑分析方案后，看到约 **25 MHz** 时钟上的标准刷屏命令。最终采用 Damien 的电信号抓取路线。

![Damien 的抓取台架](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JdicK53hX84U3zjx8ibr5gQcx3eTFVyjH1NYFqIDAic2LaRCo61iaMzCS98BPFcAKCcNqjY1GE4x8qgfV3UkTSTkoic4RkKchcfjk3ibu2tF0n9k4/640?wx_fmt=jpeg&from=appmsg)

*Damien：飞线 + Pico，从屏幕总线采数*

![Thomas 的光学尝试台架](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84XKxr4MFw05HCcXbibWic1qz6ZWBbtib3wmGQlAQOCiaBFZHkzYRiaamlbvr76nghj5cNKpHCzjcWLB0KhZ8GLORQOvoTGGAJD5M1sY/640?wx_fmt=jpeg&from=appmsg)

*Thomas：光学侧信道尝试（最终未作为主路径）*

## 用 Pico PIO 嗅探刷屏数据

Pico 可超频约 200 MHz，带 **PIO** 与约 264 KB RAM。思路：PIO 在时钟上升沿采数据位，攒满后经 USB CDC 以十六进制吐给主机。PIO 核心极短（等待上升沿 + `in pins,1`，autopush 32 bit），才能跟上 25 MHz 总线。主机侧缓冲约 145000 字节量级，覆盖一整帧更新后再解析。

刷屏模式很常见：设列地址 `0x2A`、设页地址 `0x2B`，再 `0x2C` 送像素。

![TFT 更新区域时的命令与像素流](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84Wesn0vwnopErvX7qYib5GEibJaFjHRdlTD6hSO6Wts9rS5qiarvyTNbxhKxId5ezRDXVCJkQaRLnRibXRQveJjLelA9fHPRK53yVQ/640?wx_fmt=jpeg&from=appmsg)

*更新指定区域时：`0x2A` / `0x2B` / `0x2C` 与随后的像素数据*

（完整 PIO / 主机解析脚本较长，此处从略；要点是「按命令切块 → 抽出像素载荷 → 校验同步字」。防御侧若在表盘解析加严格边界检查，这条链在源头就会断。）

## 切片 dump，再拼回整包固件

为对齐帧，他们在表盘顶部两行嵌入同步字与目标地址元数据（如 `0xa5a5a5a5`、`0xdeadbeef` + 地址），方便在捕获流里定位并校验有无 bit 错位。再批量生成「连续地址」坏偏移表盘，一边上传一边抓屏总线，把每片写成 `firmware-dump-0x........bin`，最后按地址拼成约 **2 MB** 镜像——与公开杰理固件格式文档相符。

![抽取出的固件开头字节](https://mmbiz.qpic.cn/mmbiz_jpg/JdicK53hX84W7qWbc8uSDlW1FUxuEFicZOmet4PwicLyUjt0FSDGUhu1NN8qZXVATibEd8J5zYagF8OphYDvUqodHjlMwHibB5ZlqhJry97AuJNQ/640?wx_fmt=jpeg&from=appmsg)

*拼出的固件镜像开头*

## 结论与防御启示

这条线的价值不在「又一个 dump 脚本」，而在威胁模型提醒：

* **官方通道不可用时**

  ，业务功能（表盘商店 / 自定义资源）仍可能变成内存读写原语；解析器缺边界检查 ≈ 任意读。
* **屏幕、指示灯、高速调试/显示总线**

  都可能成为侧信道。2000 年代 blinkenlights 论文盯的是网卡 LED；今天换成 RGB565 TFT + 约 25 MHz 串行屏总线 + 超频 Pico PIO，方法论同构。
* **OTA 鉴权**

  若只是硬编码密钥套一层蓝牙遗留 E1，只能挡住「随手连一下」，挡不住挑战转发与协议层滥用；更关键的是：即便鉴权通过，也不应暴露无审计的整片读出能力。
* 物理上，隐藏 USB 测点、屏幕排线飞线、廉价逻辑分析替代方案，都会拉低「拿到镜像」的成本——产品评估不能假设攻击者只会等官方烧录器。

### 产品 / 蓝队可落地的检查项

1. 表盘、字体、皮肤等资源解析：**强制偏移与长度落在缓冲区之内**，类型字段白名单，失败则拒载而非「尽量显示」。
2. BLE GATT：量产固件关闭调试/冗余服务；OTA 使用可轮换密钥或设备唯一凭证，并限制错误次数与会话绑定。
3. 固件读取与烧录：走受控、鉴权、可审计通道；DP/DM 等测点在量产版拆除或灌胶。
4. 显示链路：在高威胁场景评估排线是否可被夹取；敏感内存不要以「未校验指针 → 直接 DMA/刷屏」路径可达。
5. 传感器与健康声明：避免无硬件支撑的测量 UI 误导用户（本案「传感器」名不副实，属于产品诚信问题，也放大拆机动机）。

有了固件，原作者说下一步才是分析「生命体征数值到底怎么算出来的」——那是另一篇故事。本文仅作防御向技术分享，完整实验细节、演讲材料与工具链请参阅 Quarkslab 公开博文（Damien Cauquil；协作 Thomas Cougnard / Xilokar；杰理文档致谢 Kagaimiq）。

免责声明：

本人所有文章均为技术分享，均用于防御为目的的记录，请勿用于其他用途，否则后果自负。

更多 IoT / 车联网 / 机器人 / AI 安全资料在星球里，扫码进「车联网攻防日记」。

![知识星球·车联网攻防日记](https://mmbiz.qpic.cn/sz_mmbiz_png/JdicK53hX84Vuia7bicFPW5t342X1XEnM8p7cUVuf5ibsGXXibibQWJD7T6B1TCbNhoxwWsJU4c5tZPqW5WW570zL8usXm5tWFXeYSW5yN6ApDJEo/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/CBQpMBV9zPvo3ZuxicpWjWwCiaXOPrDAu26fx15icAgD6cJbOG3ZDppXvp3MQeISu15QT18odicltialEibcNsxS0WfA/0?wx_fmt=png)

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