---
title: “无审查”AI 视频模型来了！Sulphur 2 本地部署实测：8G 显存也能跑！
url: https://blog.upx8.com/AI-Sulphur-2-8G
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-05-16
fetch_date: 2026-05-17T05:47:43.523503
---

# “无审查”AI 视频模型来了！Sulphur 2 本地部署实测：8G 显存也能跑！

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# “无审查”AI 视频模型来了！Sulphur 2 本地部署实测：8G 显存也能跑！

发布时间:
2026-05-16 New Article

分类:
[共享资源/Free](https://blog.upx8.com/Free)

热度:
2902

最近，AI 视频生成领域突然冒出了一个极具争议的名字 —— Sulphur 2。它被不少网友称为“开源版 Sora”，不仅支持文生视频、图片转视频，而且最大的卖点只有四个字：**真正无审查**。目前网上已经开始出现大量使用 Sulphur 2 生成的敏感视频内容，甚至有些演示视频不得不打上马赛克后才能公开展示。这也让它在短时间内迅速爆火，成为近期 AI 圈讨论度最高的视频模型之一。

![20260511132103 956067](https://www.freedidi.com/wp-content/uploads/2026/05/20260511132103_956067.webp "爆火的“无审查”AI 视频模型来了！Sulphur 2 本地部署实测：8G 显存也能跑！ 9")

更让人意外的是，Sulphur 2 并不是那种只能跑在顶级服务器上的“实验室模型”。相反，它主打的恰恰是“本地部署”。官方与社区版本已经支持在普通消费级显卡上运行，甚至 8G 显存也可以启动体验。对于很多普通用户来说，这意味着你不再需要昂贵的云端订阅，也不需要 API Key，更不用排队等待生成，只要一台电脑，就能在本地自由生成 AI 视频。老司机们又有“大福利”了！

![20260511112126 122543 scaled](https://www.freedidi.com/wp-content/uploads/2026/05/20260511112126_122543-scaled.webp "爆火的“无审查”AI 视频模型来了！Sulphur 2 本地部署实测：8G 显存也能跑！ 2")

接下来，我们就来实测一下它的实际表现，以及如何在本地完成部署使用。

视频教程：https://www.youtube.com/watch?v=Nms56KhvIQw

## 部署教程：

**1、下载最新版的 ComfyUI 客户端**

【**[点击前往](https://blog.upx8.com/go/aHR0cHM6Ly9jb21meS5vcmcv)**】或 【**[备用打包下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy81ZmZkMWNmZDQxZTg)**】

![20260511112415 119523 scaled](https://www.freedidi.com/wp-content/uploads/2026/05/20260511112415_119523-scaled.webp "爆火的“无审查”AI 视频模型来了！Sulphur 2 本地部署实测：8G 显存也能跑！ 3")

下载后直接安装即可，如果你之前安装过旧版的ComfyUI，那么同样建议升级到最新版，否则部分模型可能不兼容，无法正常运行

![20260511112753 979461 scaled](https://www.freedidi.com/wp-content/uploads/2026/05/20260511112753_979461-scaled.webp "爆火的“无审查”AI 视频模型来了！Sulphur 2 本地部署实测：8G 显存也能跑！ 4")

**2、下载 Sulphur 2 开源无审查模型**

目前该模型有满血版和蒸馏版，前者需要32G以上的显存，适合电脑配置高的用户，小显存你就选择蒸馏版的压缩GGUF模型

**1、Sulphur 2 官方下载**

**【[点击前往](https://blog.upx8.com/go/aHR0cHM6Ly9odWdnaW5nZmFjZS5jby9TdWxwaHVyQUkvU3VscGh1ci0yLWJhc2U)】或 【[网盘下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy83MzI2ZGI2MmE5Njg)】、【[打包下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4uY2xvdWRlb3AuY29tL3MvRkFDQUMzRENEM0I0MkQ1Rg)】**

如果你的显存大于32G，那么你可以选择bf16精度的模型，生成质量最高，如果你的显存是8G以上的，那么建议选择fp8精度的模型，它对显存要求会更少，速度也更快！注意：模型大小不等于显存大小，只需你的硬盘空间足够即可！

![20260511113245 928617](https://www.freedidi.com/wp-content/uploads/2026/05/20260511113245_928617.webp "爆火的“无审查”AI 视频模型来了！Sulphur 2 本地部署实测：8G 显存也能跑！ 5")

**2、Sulphur 2 蒸馏模型下载**

**【[点击前往](https://blog.upx8.com/go/aHR0cHM6Ly9odWdnaW5nZmFjZS5jby92YW50YWdld2l0aGFpL0xUWDIuMy0xMEVyb3MtR0dVRg)】或 【[网盘下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy9jNWZmNzhjMDY1NTg)】、【[备用下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4uY2xvdWRlb3AuY29tL3MvOUIxRjQwRDdBMjBFRDVBNQ)】**

蒸馏版模型是gguf格式的文件，需要配合 ComfyUI-GGUF 插件进行使用！

![20260511113158 582426](https://www.freedidi.com/wp-content/uploads/2026/05/20260511113158_582426.webp "爆火的“无审查”AI 视频模型来了！Sulphur 2 本地部署实测：8G 显存也能跑！ 6")

下载好模型以后跟着教程操作，将模型放入对应的文件夹下

**3、图生视频**

**下载工作流**重启并进入 ComfyUI 客户端，在（模板-视频）中下载 LTX-2.3:图生视频，来获取生成的工作流，载入后将默认的主模型切换到之前下载好的无审查的Sulphur 2模型

![20260511113910 889627](https://www.freedidi.com/wp-content/uploads/2026/05/20260511113910_889627.webp "爆火的“无审查”AI 视频模型来了！Sulphur 2 本地部署实测：8G 显存也能跑！ 7")

最后上传图片，就可以通过图片生成你需要的任何视频了

![20260511114026 970937 scaled](https://www.freedidi.com/wp-content/uploads/2026/05/20260511114026_970937-scaled.webp "爆火的“无审查”AI 视频模型来了！Sulphur 2 本地部署实测：8G 显存也能跑！ 8")

**4、文生视频**

先下载工作流 【**[点击下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4ucXVhcmsuY24vcy8xODZkNmZmMmJiMTQ)**】或【**[备用下载](https://blog.upx8.com/go/aHR0cHM6Ly9wYW4uY2xvdWRlb3AuY29tL3MvNENGMjE3MDY3NkVGMEJFNg)**】

获取到工作流后，直接拖入ComfyUI 客户端，在文本输入里填写你需要的提示词，就可以通过文字生成视频了！

[取消回复](https://blog.upx8.com/AI-Sulphur-2-8G#respond-post-8176)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [All](/all.html)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [便签](https://txt.upx8.com)
* [关于](/about.html)

[![又拍云赞助商](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved. [看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")