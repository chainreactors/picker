---
title: XR 世界导览 #3：当 XR 遇上 GPT
url: https://buaq.net/go-167080.html
source: unSafe.sh - 不安全
date: 2023-06-04
fetch_date: 2025-10-04T11:44:30.511428
---

# XR 世界导览 #3：当 XR 遇上 GPT

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/d4b92505e8ed2a493879e3aebe33f221.jpg)

XR 世界导览 #3：当 XR 遇上 GPT

写在前面2010 年发布 iPad 时，乔布斯曾说道：iPad 是《全球概览》的电子化身。时间来到 2023 年，另一项可与个人电脑 、智能手机媲美的个人计算设备，正在走向主流消费市场，那便是 XR，
*2023-6-3 18:43:8
Author: [sspai.com(查看原文)](/jump-167080.htm)
阅读量:26
收藏*

---

## **写在前面**

2010 年发布 iPad 时，乔布斯曾说道：iPad 是《全球概览》的电子化身。

时间来到 2023 年，另一项可与个人电脑 、智能手机媲美的个人计算设备，正在走向主流消费市场，那便是 XR，即扩展现实设备（Extended Reality，包括了增强现实 AR、混合现实 MR 及虚拟现实 VR 等设备）

XR 设备的成熟和推广，必将引发下一场个人计算设备的变革。在这样的黎明时刻，我们希望和你一起关注这一领域的进步与突破，第一时间知晓产品与技术的快速迭代，享受科技进步带来的美妙体验。

欢迎打开《XR 世界导览》，《XR 世界导览》是由少数派与 XR 基地共同创作的栏目，我们之后将以图文、播客和视频的形式，和你分享 XR 领域的行业动态、应用推荐、产品体验和技术解析。

一起进入 XR 的世界吧！

## 本期导览

* 头条：Meta 发布图像分割模型 Segment Anything，可以将其视为图像分割领域的 GPT**;LumaAI 发布 Unreal 插件;OpenXR Toolkit 开始支持 Meta Quest Pro 眼动追踪;NuEyes 将推出针对医疗和牙科市场的下一代智能眼镜;**
* 创意：本期将分享5个 XR 领域的开发创意，软件工程师 [Stijn Spanhove](https://twitter.com/stspanho) 用 ChatGPT 和 WebAR 成功地创建了一个场景**;Owlchemy Labs 开发的新游戏： Cosmonious High，让失明和低视力人群也能尽情游玩;**
* Code 与工具：本期将分享5个开发框架或工具，其中 SkyboxLab 可以根据文本提示生成令人惊叹的 360° 天空盒。

## 行业头条

### Meta 发布图像分割模型 Segment Anything

* [项目地址](https://github.com/facebookresearch/segment-anything)
* [在线演示地址](https://segment-anything.com/demo)

**关键词：**图像分割、全卷积神经网络、生成式 AI、人工智能

Facebook 最近发布了一款名为「Segment Anything」的模型，它基于图像分割，在某种程度上，可以将其视为图像分割领域的 GPT ，通过简单的提示，就可以对图像中的任何物体进行精确分割，如人、车、树等。

![](https://cdn.sspai.com/2023/06/02/376985187205881a0ab2a84598e3d38d.gif)

从技术角度来看，Segment Anything 采用了全卷积神经网络。这种网络可以对图像进行像素级的分割，因此可以处理不同大小和形状的图像，并且可以在不同场景下进行准确的分割。相比于传统的方法，全卷积神经网络在分割效果和准确性方面表现更为出色。

![](https://cdn.sspai.com/2023/06/02/article/9651118e7a9f34fad7a3a85b84e38a87?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

另外，Segment Anything 支持一种称为「模糊性处理」的方法进行数据标注，可以使得标注师只需要标注一部分区域，就能够得到整张图像的标注信息。这种方法可以大大提高标注效率，同时也减轻了标注师的工作强度。

除此之外，Segment Anything 还有以下优点：

* 可以根据数据特点自适应调整模型参数，使得模型的分割效果更加精准；
* 可以通过引入多种 prompt 信号，使得模型能够对不同类型的图像进行分割；
* 可以处理更为复杂的图像场景，例如医学图像、城市街景等；
* 支持主动学习等功能，可以帮助用户更加高效地进行数据标注；
* 提供了一种称为「数据标注引擎」的工具，可以在大规模数据标注时提高效率。

因此，Segment Anything 不仅可以提高数据标注的效率，还可以提高标注的精度和数据的利用率。

![](https://cdn.sspai.com/2023/06/02/article/cfba6656593ee188013df4b68dc524a4?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2023/06/02/article/ad9a0b62a3f9a347ea14725d72869d53?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Meta 提供了一些关于使用 Segment Anything 的实际案例。例如，SAM 可用于 AR 眼镜识别日常物品，向用户发出提醒和指示。SAM 还可以在农业领域，帮助农民或协助生物学家进行研究，辅助自动驾驶等等。

### LumaAI 发布 Unreal 插件

* [说明文档](https://docs.lumalabs.ai/9DdnisfQaLN1sn)

**关键词**：游戏引擎、 拍照建模、神经辐射场、体积渲染

近日，Luma AI 发布了第一版的 UE 5 （Windows） 插件。此插件使用本地运行的体积渲染——这意味着不需要再使用传统的基于网格、几何、材质的三维模型来进行渲染。根据网友测试，该插件只需 6G 显存的 RTX2060 显卡就可以流畅运行起来。

![](https://cdn.sspai.com/2023/06/02/article/7171f04f6730230eeef1992cab59d3d0?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Luma 是一个利用 **NeRF（Neural Radiance Fields：神经辐射场）** 技术来进行三维物体或场景重建的手机 App。简单地说，Luma 利用了 NeRF 来进行拍照建模，友好的界面引导、良好的重建效果及利用重建后的模型生成视频，是它的重要特色，同时还支持多种格式导出：obj、gltf、usdz、ply。随着本次 UE5 插件的发布，LumaAI 还支持导出为 Luma Field File，并导入 UE5 中直接进行体积渲染。

使用过程共 5 步：

* 下载示例工程并解压；
* 双击 **文件打开 UE5；.uproject**
* 下载自己建模好的 Luma Field 文件（需要自己提前使用 Luma App 拍照建模好）；
* 将下载好的文件拖入到 Unreal 编辑器的内容浏览器中；
* 等待几秒钟，就会根据 NeRF 文件生成 Unreal 蓝图，将其拖入到 UE5 中使用；

Luma 官方声称：对于其它三维引擎和三维软件的插件支持，要等 UE5 插件足够完善（as good as possible）之后，才会推出。所以 Unity 和 Blender 等版本插件还需要继续等待。

NeRF 最先是应用在新视点合成方向，由于其超强的隐式表达三维信息的能力，后续在三维重建方向迅速发展起来。相比较传统拍照建模算法，它可以生成无空洞、表面质量更高的三维模型。

![](https://cdn.sspai.com/2023/06/02/article/9082ff7bf95e10df4a20a454b08c2b82?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2023/06/02/article/ce16615195904160e27ec404852e7af0?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

NeRF 直接生成的数据是体素格式，也就是类似于一堆不同颜色的小球体，要想在 3D 游戏或 VR 中使用，需要转换为传统的 Mesh 格式模型。随着本次 UE5 插件的发布，可以无需经过格式转换，直接在 UE5 中进行体积渲染。

目前市面上，使用 NeRF 技术进行拍照建模的 App 还有 Epic Games 家的 RealityScan，也就是 Unreal Engine 自家的 NeRF 服务，不过目前还不支持导出并使用体积渲染。

### OpenXR Toolkit 支持 Meta Quest Pro 眼动追踪

* [项目页面](https://mbucchia.github.io/OpenXR-Toolkit/)

**关键词**：Meta Quest Pro、眼动追踪、OpenXR

从 2022 年 3 月开始，OpenXR Toolkit 已经支持 Varjo Aero 和 Pimax 的眼动追踪插件的眼动追踪式渲染。现在已更新支持 Quest Pro。

[OpenXR Toolkit](https://github.com/mbucchia/OpenXR-Toolkit) 是微软员工 mbucchia 的一个免费开源项目，为基于 OpenXR 标准的 PC VR 应用带来本身不支持的新功能，比如低分辨率图像 AI 放大、手势追踪、静态和动态注视点渲染等等。

眼动追踪注视点渲染（Eye Tracked Foveated Rendering，简称 ETFR）是一种新兴的技术。它只渲染眼睛当前正在注视的小块区域以全分辨率的形式，而其余部分则以较低的分辨率进行渲染。这种技术可以大大提高游戏的性能，因为释放的 GPU 资源可以用于提高性能、提高渲染分辨率或增加图形设置。眼动追踪技术还可以让玩家在游戏中更加自然地移动头部，这样他们可以更好地享受游戏的体验。总之，眼动追踪技术是一项非常有前途的技术，OpenXR Toolkit 的支持将为更多玩家带来更好的游戏体验。

![](https://cdn.sspai.com/2023/06/02/article/c3fd0401d4edfd33035380c93eeedb01?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

[OpenXR](https://github.com/KhronosGroup/OpenXR-SDK) 是 Khronos 提供的开放标准，旨在通过允许开发人员无缝地针对各种 AR / VR 设备来简化 AR / VR 开发，Khronos Group 一直致力于统一 XR 没有标准的混乱问题。目前，Meta、Sony、Valve、Microsoft、HTC、NVIDIA 和 AMD 已相继支持该标准。

![](https://cdn.sspai.com/2023/06/02/article/17b3347a8158d29e9e4e90bff5772f10?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

### NuEyes 将推出针对医疗和牙科市场的下一代智能眼镜

* [官方网站](https://www.nueyes.com/nuloupes)

**关键词**：智能眼镜、医疗 AR、医疗 VR

NuEyes 即将推出一款名为 NuLoupes 的智能眼镜，将会彻底颠覆外科和牙科放大镜市场，并且为医疗专业人士和患者带来许多便利。

![](https://cdn.sspai.com/2023/06/02/article/01fc87faad39256bd6a2dea70f981df3?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

对于医生来说，NuLoupes 的高分辨率可变数字放大技术提供亚毫米精度的深度感知，让医生能够更好地理解他们所看到的环境。此外，NuLoupes 还有实时 3D 立体成像和大量的增强现实应用和内容的生态系统，专门用于帮助临床医生。这些特点使得医生能够更准确地诊断和治疗疾病，提高手术和治疗的效率和精度。

对于患者来说，NuLoupes 也提供了更好的治疗体验。比如，医生可以通过 NuLoupes 使用增强现实应用和内容，进行口述或者记录手术笔记，进行物体识别，以及远程健康和 3D 立体直播流，同时可以在视野内查看患者数据和影像。这些特点让患者能够更好地了解自己的病情，同时也能够更好地理解医生的治疗方案。

![](https://cdn.sspai.com/2023/06/02/f7082f8f718019eba8f7b3c1f4ac083c.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

除了智能眼镜外，虚拟现实（VR）和增强现实（AR）技术在医疗方面也有许多潜在的应用场景。医学生和实习医生可以利用 VR 技术进行沉浸式的模拟手术和临床实践，从而提高其技能和信心。此外，AR 技术可以为医生提供实时的指导和提示，帮助他们更好地诊断和治疗病人。

使用 VR 技术可以帮助病人分散注意力，从而减轻疼痛和不适感。研究表明，使用 VR 技术可以降低手术后的疼痛程度，减少使用止痛药的需要。VR 技术还可以用于治疗焦虑症、抑郁症和创伤后应激障碍等心理健康问题。通过提供沉浸式的体验，VR 技术可以帮助病人学会应对和管理情绪。AR 技术可以提供实时的反馈和指导，帮助病人进行正确的动作和姿势，促进康复。

VR 和 AR 技术在医疗领域的应用潜力巨大，可以帮助医生提高诊断和治疗效果，同时也可以帮助患者更好地管理疾病和恢复健康。

## 产品创意

### Jim Henson’s The Storyteller：给阅读带来更上一层楼的体验

* [产品介绍](https://youtu.be/LKH1lwbrUJE)

**关键词**：AR、创意、阅读、概念视频

电子设备和纸质书，其实并不一定是完全冲突的关系。在 [Felix & Paul Studios](https://www.youtube.com/%40felixandpaul) —— 一个获得过艾美奖的创作者眼中，二者甚至可以互相成就的关系。

[](https://video.sspai.com/series/xr/Storyteller.mp4?e=1685805793&token=XxfqVWXxAgA7iVqM6tW71gsKWrdi_TDs6wWTDplI:AjK7OgyKeD6bwCYYm9NVzBcc158=)

在这个视频中，[Felix & Paul Studios](https://www.youtube.com/%40felixandpaul) 向我们介绍了如何使用增强现实（AR）技术来增强阅读体验。通过将 AR 标记添加到印刷材料中，读者就可以使用 AR 眼镜来换一种方式「看」这些书。当读者打开书本的时候，书本中的城堡就可以以 3D 模型的形式展现出来，在这个过程中再辅以生动的动画和逼真的音效，读者就可以更加沉浸式地感受书中场景。

基于这种构思，AR 眼镜还可以做到更多的真实交互，例如在视频中，当读者阅读到一个充满海水的场景时，随着读者将书本倾斜，书本中的海水也随之流出。不得不说真实度拉满。

### 使用 ChatGPT 制作 AR 场景

* [产品演示](https://80.lv/articles/making-ar-scenes-using-openai-s-chatgpt/)

**关键词**：ChatGPT、WebAR

最近，人工智能公司 OpenAI 发布了一款名为 ChatGPT 的对话模型。这个模型的应用非常广泛，创建者使用它做了很多有趣的实验，包括电影大纲、Blender 的 Python 脚本、"Choose Your Own Adventure" 故事，甚至还有一场金融科技和银行之间的 RAP 对决。这几个实验都展示出了 ChatGPT 的惊人能力。

[](https://video.sspai.com/series/xr/GTX-XR.mp4?e=1685805793&token=XxfqVWXxAgA7iVqM6tW71gsKWrdi_TDs6wWTDplI:PFv_gvCoMekx7DakOFjV9tGQMbg=)

此外，软件工程师 [Stijn Spanhove](https://twitter.com/stspanho) 还利用 ChatGPT 在增强现实（AR）领域做了一些有趣的实验。他利用 ChatGPT 和 WebAR 成功地创建了一个场景。先前，Stijn Spanhove 也在 AR 领域展示过他对 AI 的实验，他使用 Stable Diffusion 的图像修复功能在一个选择的区域内生成了艺术品。

### Before Your Eyes —— 一部美丽的 VR 叙事艺术展示

* [产品介绍](https://www.theverge.com/2023/3/10/23632733/before-your-eyes-playstation-vr2-psvr-2-vr-showcase-storytelling)

**关键词**：PlayStatation VR2、VR 游戏

![](https://cdn.sspai.com/2023/06/02/ar...