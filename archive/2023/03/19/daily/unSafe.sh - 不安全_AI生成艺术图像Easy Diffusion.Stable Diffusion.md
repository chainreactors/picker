---
title: AI生成艺术图像Easy Diffusion.Stable Diffusion
url: https://buaq.net/go-154085.html
source: unSafe.sh - 不安全
date: 2023-03-19
fetch_date: 2025-10-04T10:01:56.537997
---

# AI生成艺术图像Easy Diffusion.Stable Diffusion

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

![](https://8aqnet.cdn.bcebos.com/5e034af0486561eba7e17a82a747bdc9.jpg)

AI生成艺术图像Easy Diffusion.Stable Diffusion

最近AI绘图非常热门，尝试了一些网上的在线工具，但在线工具免费次数有限，若要获得更多的使用次数，所需付费的价格也并不低廉。xiaoz得知可以通过本地搭建
*2023-3-18 21:44:0
Author: [blog.upx8.com(查看原文)](/jump-154085.htm)
阅读量:23
收藏*

---

最近AI绘图非常热门，尝试了一些网上的在线工具，但在线工具免费次数有限，若要获得更多的使用次数，所需付费的价格也并不低廉。xiaoz得知可以通过本地搭建“Stable Diffusion”来实现本机AI绘制“艺术图像”，这样就无需支付高额费用了，嘿嘿。

![](https://img.7761.cf/img/20230318/1104386422.png)

### 什么是Stable Diffusion

Stable Diffusion是由计算机科学家和艺术家一起开发的，它使用深度学习算法和稳定扩散过程来生成艺术图像。具体来说，它使用一种称为随机游走的算法来创建图像，这种算法通过对像素值进行微小的、随机的变化来模拟稳定扩散过程中的路径漫步。该算法还使用神经网络技术来学习并生成不同的图像风格。

Stable Diffusion可以生成非常美丽和复杂的艺术作品，其应用包括艺术创作、图像生成、视觉效果设计等。如果您对此感兴趣，可以通过在线搜索了解更多信息，或者尝试使用该工具进行艺术创作。

### 开始之前

在网上搜索了一下“Stable Diffusion”的搭建过程，结果发现这一过程十分复杂，看得我都想放弃了。就在我正准备放弃的时候，在Github上发现了一个名为“Easy Diffusion”的项目，它提供了一键安装Stable Diffusion所需的各种环境、模型等依赖，从而大大降低了安装难度。

本文旨在分享并记录xiaoz安装“Easy Diffusion”的过程，尽管这个工具简化了很多步骤，但安装仍然具有一定难度，推荐对计算机有一定了解的朋友尝试。

### 准备工作

1. 可科学上网的TZ（能访问Github）
2. 一台配置不太差的电脑，CPU和显卡配置越高越好（xiaoz的配置是AMD 3600 + RTX 3050勉强凑合）
3. 听说过HTTP代理，了解HTTP代理如何使用（可将ss转为HTTP代理，请自行去研究）

### 下载Easy Diffusion

下载地址：[https://github.com/cmdr2/stable-diffusion-ui/releases/download/v2.5.15/stable-diffusion-ui-windows.zip](https://github.com/cmdr2/stable-diffusion-ui/releases/download/v2.5.15/stable-diffusion-ui-windows.zip "https://github.com/cmdr2/stable-diffusion-ui/releases/download/v2.5.15/stable-diffusion-ui-windows.zip")

> 后续的更新版本可以在这里查看：[https://github.com/cmdr2/stable-diffusion-ui/releases](https://github.com/cmdr2/stable-diffusion-ui/releases "https://github.com/cmdr2/stable-diffusion-ui/releases")

### 设置HTTP代理

Easy Diffusion会从国外网络下载大量的内容，比如Python环境、绘图模型等，国内网络访问困难或者几乎无法访问，因此我们需要让Windows的命令行可以科学上网才行。

打开你的CMD命令行，输入下面的命令设置HTTP代理：

```
set http_proxy=http://127.0.0.1:10809
set https_proxy=http://127.0.0.1:10809
```

`http://127.0.0.1:10809`为您的HTTP代理地址，如果您不清楚这是啥，建议直接放弃。

### 安装Easy Diffusion

将上面下载好的压缩包`stable-diffusion-ui-windows.zip`解压到任意一个目录。然后：

1. 打开`stable-diffusion-ui`目录
2. 双击运行`Start Stable Diffusion UI.cmd`这个脚本

接下来就是漫长的等待，可能会出现一些错误，我把我遇到的错误整理到了下方。

如果提示Python包下载超时：

> HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.

可通过设置pip镜像源解决，Easy Diffusion会单独为您安装一个Python 3.8的环境，我们需要设置pip镜像源。下面的命令将Easy Diffusion的pip镜像源设置为了阿里云镜像：

```
cd D:\stable-diffusion-ui\installer_files\env\Scripts>
d:
pip.exe config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

如果遇到模型下载失败的提示错误，可以直接去Google或者Github搜索模型的名字下载，然后放到`models`的指定目录下即可。

![](https://img.7761.cf/img/20230318/1033621703.png)

![](https://img.7761.cf/img/20230318/633971822.png)

我整理了部分模型下载地址：

* [GFPGANv1.3.pth](https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth "GFPGANv1.3.pth")
* [RealESRGAN\_x4plus.pth](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth "RealESRGAN_x4plus.pth")
* [RealESRGAN\_x4plus\_anime\_6B.pth](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth "RealESRGAN_x4plus_anime_6B.pth")

Easy Diffusion安装遇到报错注意看报错提示信息，然后可以尝试通过上述办法手动解决，手动解决后重新运行`Start Stable Diffusion UI.cmd`脚本即可。

xiaoz在安装过程中遇到了Python包安装超时和模型下载错误的问题，通过上述方法已经成功手动解决了。每个人的情况不尽相同，建议灵活变通并在网上搜索解决方法。

### 运行Easy Diffusion

安装成功后会自动打开浏览器地址`http://localhost:9000/`看到WEB界面，接下来就可以根据你的喜好生成“艺术图像”啦，具体的一些使用方法xiaoz还在进一步研究，欢迎留言讨论。

![](https://img.7761.cf/img/20230318/4234583317.jpg)

### 取消HTTP代理

安装完毕后我们可以取消Windows命令行的HTTP代理了：

```
set http_proxy=
set https_proxy=
```

> 此文部分内容参考了：[https://github.com/cmdr2/stable-diffusion-ui](https://github.com/cmdr2/stable-diffusion-ui "https://github.com/cmdr2/stable-diffusion-ui")

在Windows系统上成功安装Easy Diffusion（Stable Diffusion）并实现AI生成艺术图像

文章来源: https://blog.upx8.com/3304
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)