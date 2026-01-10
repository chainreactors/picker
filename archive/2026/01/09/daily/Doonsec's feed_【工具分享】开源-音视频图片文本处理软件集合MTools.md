---
title: 【工具分享】开源-音视频图片文本处理软件集合MTools
url: https://mp.weixin.qq.com/s/7mVC_vp4oSO9nelPDwHI6w
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:30:13.499516
---

# 【工具分享】开源-音视频图片文本处理软件集合MTools

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1rcArtbwed2tibGsu3xSRszEzda1cs8dmpGtuj25ET3zsdPa02VXVEuDjnJGc2uehLa8yFx3IIwhqbZHy5oHSjw/0?wx_fmt=jpeg)

# 【工具分享】开源-音视频图片文本处理软件集合MTools

原创

香农Shannon

网络铅笔头

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1rcArtbwed2tibGsu3xSRszEzda1cs8dmm8NjOYBUiap8bjje0Qic7Ib19hX0E1OzTO1iaufpjTPlxdKuS0T2xGuOg/640?wx_fmt=png&from=appmsg)

今天聊个“大杂烩”工具：**MTools**。一个开源免费的桌面集合类软件，试图把你桌面上那一排排音视频图片编码软件的图标，塞进一个窗口里。

它长得挺朴实，但肚子里货不少。

**音视频处理**是基本功，裁剪、转换、合并、压缩、插帧、配字幕、去水印，都不在话下，还藏了些AI魔法，比如一键增强画质、智能人声分离。（初次使用时可根据需求选择现在对应的模型文件或辅助包）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1rcArtbwed2tibGsu3xSRszEzda1cs8dmQVJHHf2N2pbribib9f9ns3foiczstgZV3e74U8icuxNFU23B3c3gibOp5Yw/640?wx_fmt=png&from=appmsg)

**图片编辑**也够日常折腾，压缩、格式转换、简单调色，应急足够。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1rcArtbwed2tibGsu3xSRszEzda1cs8dmta3fY5Hjuu6pPMKBl3WuDreqgP5NC1XvovR48LSbrKusXrFBxzmHgg/640?wx_fmt=png&from=appmsg)

至于**文本处理**和**编码小工具**，像是程序员顺手塞进去的彩蛋，哪天用上了会觉得挺贴心。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1rcArtbwed2tibGsu3xSRszEzda1cs8dmrJNNDyNdQWdvTXADf2tpqxicmAz7ecdIqQX9ae3xnOfFEK6QYUSzZyQ/640?wx_fmt=png&from=appmsg)

举个栗子：文本对比，可鲜明标记文本间区别...

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1rcArtbwed2tibGsu3xSRszEzda1cs8dmcJzBlzUgUHRWuT1NjqMwbl4ONLezZFCHdhpBKCl9xA9dtEVPwdqialg/640?wx_fmt=png&from=appmsg)

...

最有意思的是它的“**AI增强**”模块。不是什么噱头，而是把一些实用的AI能力（比如背景去除、智能抠图）做成了点点鼠标就能用的按钮，直接插进你的工作流里，不用再去折腾复杂的在线服务。

**它不替代任何领域的专业软件**，但胜在“**顺手**”。当你不想为一点小操作启动庞然大物，或者需要快速串联几个简单步骤时，它会是个安静的桌面伙伴。开源免费，没有广告，解压即用，用完即走。

美中不足：python语言编写，所以启动速度有待提高；有的地方存在小BUG，期待后续改进。

如果你偶尔也需要这种“轻量的全能”，不妨去它的GitHub页面逛逛。工具箱里多把瑞士军刀，总没坏处。

开源地址 : https://github.com/HG-ha/MTools

下载链接：https://openlist.wer.plus/MTools/

* 支持Win平台及预编译版本说明：

+ MTools\_Windows\_amd64：体积最小，并且支持nvidia、amd、intel显卡加速，但不支持手动管理显存
+ MTools\_Windows\_amd64\_CUDA：体积中等，使用CUDA进行加速，但需要手动安装CUDA 12.x + cuDNN 9.x
+ MTools\_Windows\_amd64\_CUDA\_FULL：体积最大，内置完整的CUDA加速环境，无需手动安装CUDA和cuDNN

![](https://mmbiz.qpic.cn/mmbiz_gif/1rcArtbwed1YUISnt7dp86OibgnLrgCnu5y2b6vicoLhcq45k2T57CwVPGE5iaiaXp2ChiadoAzR7HzvEhHhN1iaoRSg/640?wx_fmt=gif)

下面为作者介绍：

## 部分工具展示

### AI 智能处理

* **AI 智能抠图**

  - 一键移除图片背景，支持人像、动漫、通用场景等多种模型，GPU 加速提速 3-10 倍
* **AI 证件照制作**

  - 智能生成各类证件照，支持多种尺寸和背景，自动美颜和人脸矫正
* **AI 音视频人声分离**

  - 专业级人声/伴奏分离，支持 UVR MDX-Net 模型，轻松制作卡拉OK伴奏
* **AI 音视频转文字**

  - 直接处理视频或音频，从中提取字幕，支持输出字幕文件
* **AI 视频插帧**

  - 将低帧率视频进行补帧，提高视频流畅度
* **AI 图片、视频超分**

  - 支持对图片、视频进行修复和放大，例如720p修复到2k

### 图片工具箱

* **格式转换 & 压缩**

  - 支持 12+ 种格式，集成 mozjpeg、pngquant 专业引擎
* **智能编辑**

  - 尺寸调整、裁剪、旋转、水印、去除 EXIF
* **创意拼接**

  - 九宫格、单图切分、横向/纵向拼接
* **实用工具**

  - 二维码生成、GIF 调整、信息查看

### 音视频处理

* **格式转换**

  - 支持主流音视频格式互转（MP3/WAV/FLAC/MP4/AVI/MKV...）
* **智能压缩**

  - H.264/H.265 编码，自定义比特率和质量
* **速度调整**

  - 音视频加速/减速，不改变音调
* **提取 & 合成**

  - 提取音轨、添加水印、视频修复

### 开发辅助

* **编码转换**

  - 自动检测文件编码，一键解决乱码问题
* **Base64 工具**

  - 图片与 Base64 互转
* **代码格式化**

  - JSON/XML/SQL 美化与验证

软件获取

在👆【网络铅笔头】聊框回词【MTools】即可Get..

#免责声明：本文仅限个人学习使用，请勿用于商业用途！

#温馨提示**：** 吾爱大佬出品，检测无毒，放心食用。公众号只限于对软件做测试、评测,请读者自行甄别及使用。

[【工具分享】AutoCMD+ 安卓自动化工具](https://mp.weixin.qq.com/s?__biz=MzA3MzgwMzYyMA==&mid=2452890475&idx=1&sn=574437738ebf9447da3f48f416bc8f83&scene=21#wechat_redirect)

[[软件分享]告别App开屏广告！这款开源神器让手机体验清爽无比](https://mp.weixin.qq.com/s?__biz=MzA3MzgwMzYyMA==&mid=2452890486&idx=1&sn=80b7d597b5f0c4636265730776a63ad7&scene=21#wechat_redirect)

[【工具分享】 PDF工具箱 PDF24 Tools](https://mp.weixin.qq.com/s?__biz=MzA3MzgwMzYyMA==&mid=2452890494&idx=1&sn=4406a9d701166d4948ae19f75c8a2168&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1rcArtbwed3S4OEHB9nlBLLFicFQlvy6XsqULXQibB5GiaJVoJniad8JcnoW3G7dHUea6JicnGIaibibkaMt5KFTH1c6g/0?wx_fmt=png)

网络铅笔头

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1rcArtbwed3S4OEHB9nlBLLFicFQlvy6XsqULXQibB5GiaJVoJniad8JcnoW3G7dHUea6JicnGIaibibkaMt5KFTH1c6g/0?wx_fmt=png)

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