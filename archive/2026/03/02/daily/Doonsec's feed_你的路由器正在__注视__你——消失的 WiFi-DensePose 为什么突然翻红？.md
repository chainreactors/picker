---
title: 你的路由器正在\"注视\"你——消失的 WiFi-DensePose 为什么突然翻红？
url: https://mp.weixin.qq.com/s/9gc8xwFw2TlfP0gJNNirHQ
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:07:28.594349
---

# 你的路由器正在\"注视\"你——消失的 WiFi-DensePose 为什么突然翻红？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VykGUIjcconlwW5mYr0Tqyciaql2Lpj5wL3SwxbicqkzZBsibPnqu4ibbp3ZYNIQ89XUHa5lWtMgLlyMRscNAH8TPw7byVJIVS8M9sZ2Y1upDWw/0?wx_fmt=jpeg)

# 你的路由器正在"注视"你——消失的 WiFi-DensePose 为什么突然翻红？

原创

赛博朋克猫
赛博朋克猫

混入安全圈的程序猿艾恩

![]()

在小说阅读器中沉浸阅读

2026 年 2 月 27 日，一个生产级的实现突然冲上 GitHub Trending 榜首。

**WiFi-DensePose**，这是一个什么项目？它的作用很简单，将你的Wi-Fi变成雷达，还原你的动作轨迹。

![](https://mmbiz.qpic.cn/mmbiz_png/VykGUIjccolBhcUVoRFZcdAsia01fqNvGPj2e0zhibCz4s8bmdoToo0rhsMibBZr9q1IIA4lade9xuWpK5bUONCicK33YkdV6icmvMT7sp5QUJBE/640?wx_fmt=png&from=appmsg)

WiFi-DensePose 不是新技术。卡内基梅隆大学（CMU）早在 2023 年就发布了相关研究，用 WiFi 信号捕捉人体姿态。但一直停留在实验室阶段，没什么人关注。

# 为什么突然老树开花了？

但是为什么一个冷门项目突然火了？简单说：**它终于从"论文"变成了"能用的东西"**。

## Rust 重写，快了 810 倍

之前用 Python 写的版本，实时性根本不行。新版用 Rust 重写后，端到端加速了 810 倍。

* • 处理速度：每秒 54,000 帧
* • 延迟：低于 50ms

这意味着什么？实时人体姿态追踪终于可以落地了。

![](https://mmbiz.qpic.cn/mmbiz_png/VykGUIjccomQk9ickoqLFHYCVdsckzj6LoJcYMlpusmtAyuu97Yct7WekJTV9Hdd5fgDQIvqqnBgDOruK1JkW5xneWyJA1icfRhkBWhibhLyhc/640?wx_fmt=png&from=appmsg)

## 不需要标注数据了

早期 WiFi 感知项目最大的坑是数据标注——你得用昂贵的摄像头或动捕设备采集标签。

新版引入了 Project AETHER，用自监督对比学习直接从原始 WiFi 数据学习。不需要视频，插上设备，10 分钟自动适配新环境。

## 换个房间也能用

以前的模型换个房间精度就掉 40-70%，因为 WiFi 信号的多径效应跟房间布局强相关。

Project MERIDIAN 用对抗性领域泛化，让神经网络"忘掉"房间特征，只记人体运动。配合硬件归一化，无论用 ESP32 还是 Intel 网卡，都能保持精度。

一次训练，到处部署。

## 硬件成本：8 美元

**成本**，这个我认为是一个从实验性质的性质转向生产级项目最核心的提升，之前需要毫米波雷达或改装网卡，几千美元起步。

现在：

* • ESP32-S3 芯片，约 8 美元
* • Transformer 模型只有 55 KB
* • 三台普通 Mesh 路由器，精度 96%

## 隐私友好的"无像素"方案

GDPR 和 HIPAA 越来越严，WiFi-DensePose 提供了一个折中方案：只有骨架，没有像素。

**养老医疗**：在浴室、卧室监测跌倒、呼吸、心率，不需要摄像头。呼吸误差 ±1 BPM。
**极端救援**：火灾、地震这些视觉传感器失效的场景，WiFi 能穿透 30cm 混凝土定位幸存者，自动做 START 分诊。

# 总结

WiFi-DensePose 这次翻红并不是偶然。Rust 重写解决了性能，AETHER 解决了数据，MERIDIAN 解决了泛化，成本压到了几美元。

WiFi 不只是通信工具了，它是未来的"第六感"——无处不在、保护隐私、还能穿墙。但是这同样也带了安全隐患，虽然移除了个人特征，但是我想也没有愿意家里的路由器随时有可能变成一个监控工具吧。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/2M1GPuwVV4pyic7uufCnIaHm6oWh3STfszEe6zQPEKJJg7CkQjDe0I3wrZTcia9owicibCEmZJUPHCE9Ticx8EYEbKg/0?wx_fmt=png)

混入安全圈的程序猿艾恩

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2M1GPuwVV4pyic7uufCnIaHm6oWh3STfszEe6zQPEKJJg7CkQjDe0I3wrZTcia9owicibCEmZJUPHCE9Ticx8EYEbKg/0?wx_fmt=png)

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