---
title: deface：开源视频/照片自动人脸打码工具（模糊｜马赛克｜黑框｜摄像头实时）
url: https://blog.upx8.com/4909
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2025-11-27
fetch_date: 2025-11-28T03:12:31.301826
---

# deface：开源视频/照片自动人脸打码工具（模糊｜马赛克｜黑框｜摄像头实时）

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# deface：开源视频/照片自动人脸打码工具（模糊｜马赛克｜黑框｜摄像头实时）

发布时间:
2025-11-27 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
1684

## deface 是什么

deface 是一款专注于“人脸匿名化”的开源命令行工具，可自动识别视频或照片中的所有人脸，并在对应区域叠加匿名化效果。工具通过深度神经网络检测每一帧画面中的人脸位置，再对检测区域应用模糊、马赛克或黑框等滤镜，生成脱敏后的视频或图片文件。

工具支持常见桌面操作系统（Linux、Windows、macOS），依赖 Python 环境运行，更适合习惯命令行的开发者、内容创作者、安全与合规团队使用。默认配置下会移除原始音轨，也可以通过参数控制是否保留音频内容。

![deface：开源视频/照片自动人脸打码工具（模糊｜马赛克｜黑框｜摄像头实时）](https://cdn.skyimg.net/up/2025/11/27/afd4df53.webp)

## 核心功能亮点

### 自动检测人脸，一键完成打码

* 自动检测视频/照片中的人脸区域，无需手动逐帧框选
* 每一帧单独处理，适用于动态画面、多人场景与复杂背景
* 对检测到的人脸区域统一应用匿名化滤镜，快速完成脱敏

### 多种匿名化方式可选

针对不同隐私与审美需求，deface 提供多种人脸处理方式：

* **模糊处理（blur）**：高斯模糊，适合大多数隐私脱敏场景
* **黑框遮挡（solid）**：在人脸上叠加实心矩形，效果醒目直接
* **马赛克（mosaic）**：以网格像素方式处理人脸区域，可通过参数控制块大小
* **自定义图片覆盖（img）**：使用自定义图片替换人脸区域，适合制作趣味效果或品牌化遮挡
* 支持设置蒙版缩放比例，保证覆盖范围足够完整，减少边缘泄露风险

### 可调检测阈值，平衡误检与漏检

人脸检测的阈值可以通过命令行参数灵活调整：

* 阈值升高，误检更少，更少“把非人脸当成人脸”
* 阈值降低，更不容易漏掉边缘、侧脸、遮挡等复杂场景中的人脸
* 支持启用“得分显示”，在输出内容上叠加检测置信度，便于测试与调参

通过在真实业务素材上多次试验，可以为自己的数据类型找到合适的阈值配置。

### 高分辨率媒体的性能优化

在面对 1080p、4K 等高分辨率素材时，如果直接在原始分辨率上进行检测，推理速度可能明显下降。

deface 提供输入下采样选项：

* 使用 `--scale WxH` 指定用于检测的下采样分辨率
* 检测在缩小后的画面上完成，最终输出仍保持原始分辨率
* 在保证识别效果的前提下，显著提升处理速度，减轻硬件压力

只需确保缩放比例与原视频的宽高比一致，即可避免因拉伸导致识别精度下降。

### 硬件加速支持

为了进一步提升处理速度，deface 支持结合 ONNX Runtime 等后端进行硬件加速：

* 使用支持 CUDA 的 Nvidia GPU，可通过相应依赖包，将人脸检测网络自动迁移到 GPU 推理
* 在部分 Windows 或 CPU 场景下，可结合其他执行后端获得一定程度的加速
* 高帧率、高分辨率、多文件批量处理任务中，硬件加速可以有效缩短整体处理时间

## 安装方式与环境要求

### 环境准备

* 操作系统：Linux、Windows 或 macOS
* Python 版本：3.6 及以上
* 建议使用虚拟环境隔离依赖，便于管理与升级

### 通过 pip 安装

在已激活的虚拟环境中，运行：

```
python3 -m pip install deface
```

如果希望直接使用 GitHub 最新（未正式发布）的代码版本，可以执行：

```
python3 -m pip install 'git+https://github.com/ORB-HD/deface'
```

## 快速上手：一条命令完成视频匿名化

### 本地视频一键打码

假设原始视频路径为 `myvideos/vid1.mp4`，执行：

```
deface myvideos/vid1.mp4
```

工具会在同目录下生成一个新文件：

```
myvideos/vid1_anonymized.mp4
```

默认会对检测到的人脸进行模糊处理，并移除音频轨道。

### 摄像头实时匿名化演示

如果设备连接了摄像头，可以直接对实时画面进行人脸匿名化预览：

```
deface cam
```

等价于对默认摄像头设备执行预览模式，可在隐私敏感场景中用作“实时打码监看”。当存在多路摄像头时，可以尝试不同的设备索引（如 `<video1>`、`<video2>` 等）。

## 常用命令行参数示例

下方为部分常见参数，方便根据需求调整：

* 指定输出文件名：

  ```
  deface input.mp4 -o output_anonymized.mp4
  ```
* 使用黑框遮挡而非模糊：

  ```
  deface examples/city.jpg --boxes --replacewith solid -o examples/city_anonymized_boxes.jpg
  ```
* 使用马赛克，并设置马赛克块宽度：

  ```
  deface examples/city.jpg --replacewith mosaic --mosaicsize 20 -o examples/city_anonymized_mosaic.jpg
  ```
* 调整数值阈值，减少误检或漏检：

  ```
  deface input.mp4 --thresh 0.3 -o input_tuned.mp4
  ```
* 保留原始音频：

  ```
  deface input.mp4 --keep-audio -o input_with_audio_anonymized.mp4
  ```

更多参数与组合方式可以通过帮助命令查看：

```
deface -h
```

## 典型使用场景

* 用户访谈、可用性测试录屏等需要“对外分享但隐藏人脸”的研究视频
* 教学视频、演示视频中出现路人或敏感人员，需要统一打码的素材
* 城市街景、商场监控画面剪辑，为合规发布进行脱敏处理
* 产品宣传片、活动回顾视频中需要隐藏未授权出镜者的脸部信息
* 数据标注、机器学习训练数据准备过程中的隐私保护环节

借助命令行与脚本能力，可以轻松将 deface 集成到现有媒体处理流水线或自动化工具中。

欢迎开发者、研究者与内容团队在遵守相关法律法规和平台政策的前提下，将此工具用于隐私保护与数据合规场景。

## 开源项目地址

deface 完全开源，可自由查阅源码与贡献改进：

GitHub 项目地址：[`https://github.com/ORB-HD/deface`](https://github.com/ORB-HD/deface "https://github.com/ORB-HD/deface")

[取消回复](https://blog.upx8.com/4909#respond-post-4909)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2025 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")