---
title: Hermes的应用（十四）：docker buildx
url: https://mp.weixin.qq.com/s/Es7jZpiEx9skf2VeMCYguw
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:33:33.183221
---

# Hermes的应用（十四）：docker buildx

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2PhZXrB0gN47QGxVMjcn2ZxibtN6b6ofvD1b8duL8JiaaBb13PTUd1ibSicH3KuAMLyEHNXEKicf5pGEfPtIA7b3lb5IxVBUb93wudZ2pX0z4ZrQ/0?wx_fmt=jpeg)

# Hermes的应用（十四）：docker buildx

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近，docker打包成需要arm架构的镜像包。第一想到的是租一台arm机。第二，使用windows下较新版本的 Docker Desktop。当直接运行docker build 命令时，它实际上已经在底层调用buildx了8。更准确地说：docker build 背后就是buildx。可以打开终端（如 PowerShell 或 CMD），运行以下命令来查看版本信息，确认buildx 是否可用：docker buildx version ，如果命令成功执行并输出版本号，就说明你的环境已经准备好了。第三，让hermes给我们准备好，完成时直接输出：完美！multiarch builder 已经启动并运行。现在环境已经准备好可以构建多架构 Docker 镜像了。

   1、可用平台：

   - linux/amd64 (Native)

   - linux/arm64 (ARM64/AArch64)

   - linux/arm/v7 (ARM 32-bit)

   - linux/arm/v6 (ARM 32-bit older)

   - linux/ppc64le 等

   2、使用方法：

   构建多平台镜像（一次构建多个平台）

docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t your-image:tag --push .

   或者只构建ARM64

docker buildx build --platform linux/arm64 -t your-image:tag .

   重要提示：

   - 使用 --push 会自动推送镜像到仓库

   - 不使用 --push 时，需要加 --load 才能加载到本地（仅支持单平台）

   - 多平台镜像会生成一个 manifest list

3、上面的参数：--load

docker buildx build --platform linux/arm64 -t mywork:1.0 .

当时末尾出现了警告WARNING: No output specified...，就是因为缺少了 --load。现在加上 --load（就是 docker buildx build --platform linux/arm64 -t mywork:1.0 --load .），这个警告就会消失，构建完成后镜像会成功加载到本地。就是当你docker images时，会看到mywork在本地容器中的镜像。同时，可以 docker save mywork:1.0 -o mywork.tar保存成文件mywork.tar。

### **⚠️ 使用**--load**的重要限制**

   - --load 仅在使用单平台且使用 docker driver 时才有效，不使用 --load 而只用 --platform 单平台时，默认不会加载到本地。

   - 对于 multiarch builder (docker-container driver)，即使单平台也需要 --load 才能加载到本地。

   - 如果需要推送到仓库，用 --push

   4、总结：

   （1）. 环境配置 ✅

   - QEMU 用户态静态二进制已安装

   - Docker buildx 已配置多平台 builder：multiarch

   - 支持平台：linux/amd64, linux/arm64, linux/arm/v7, 等

   （2）. 构建命令

   单平台（ARM64）：

docker buildx build --platform linux/arm64 -t your-image:tag --load .

   多平台（amd64+arm64）：

docker buildx build --platform linux/amd64,linux/arm64 -t your-image:tag --push .

   （3）. 示例验证

   构建测试镜像

docker buildx build --platform linux/arm64 -t test-arm:latest --load ./test-arm

   运行（会自动通过QEMU模拟ARM）

   docker run --rm test-arm:latest

   输出：Hello ARM from aarch64

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

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