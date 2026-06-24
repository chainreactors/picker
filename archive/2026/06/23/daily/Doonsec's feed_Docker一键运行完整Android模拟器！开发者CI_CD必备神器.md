---
title: Docker一键运行完整Android模拟器！开发者CI/CD必备神器
url: https://mp.weixin.qq.com/s/_MgHJLgWV4eqDyke5vfh0w
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:00:54.861600
---

# Docker一键运行完整Android模拟器！开发者CI/CD必备神器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kztGyHFwmfzzrplNMeZ6aHsQibxrS9nJKmDggp3DUTtiaJUA4g4by20FVY0jhyAgkEFFcLn56ky0CCyrFKXibmBtzrCw5e7JcjuC3ibiaSvFQrm4/0?wx_fmt=jpeg)

# Docker一键运行完整Android模拟器！开发者CI/CD必备神器

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

大家好，我是 **攻城狮成长日记** 的狮兄 👋

今天强烈推荐一个 **轻量且实用** 的开源项目 ——

👉 docker-android[1]

![项目封面](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxkUibRYkjM4TYRo5BOV1qPkyiaSvBYtW53ibjcUvr110HCU3icvibYFO2koVicmdHklxt23u1fjGSSW8pkek5qVUc9k7Sq1qR9wElXU/640?wx_fmt=png&from=appmsg)

它能让你在 `Docker` 容器中快速启动完整的 **Android Emulator**，适合自动化测试、`CI/CD`、多版本兼容验证等场景。

### · · · ✨ 项目核心亮点 · · ·

| 特性 | 说明 |
| --- | --- |
| 🪶 **极致轻量** | 基于 Alpine 系统，镜像体积可控 |
| 🚀 **硬件加速** | 完整支持 KVM + GPU（含 CUDA 版本） |
| 🎛️ **高度自定义** | 自由选择 Android API 版本、Google APIs、Play Store 等 |
| 📦 **开箱即用** | 内置 JRE 11 + Emulator + ADB |
| 🔄 **干净环境** | 默认每次重启自动重置，完美适合自动化流水线 |
| 📱 **远程控制** | 支持 scrcpy 实时画面投屏 |

### · · · 📊 镜像体积对比 · · ·

| 构建变体 | 未压缩大小 | 压缩后大小 |
| --- | --- | --- |
| API 33 + Emulator | 5.84 GB | 1.97 GB |
| API 32 + Emulator | 5.89 GB | 1.93 GB |
| API 28 + Emulator | 4.29 GB | 1.46 GB |
| 仅基础环境（无 SDK） | 414 MB | 138 MB |

> 💡 **建议**：本地测试推荐 **API 33**，云服务器可根据资源选择更轻量的版本。

### · · · 🚀 快速上手 · · ·

#### 方法一：使用 docker-compose（最推荐）

项目已提供 `docker-compose.yml`，直接执行：

```
# 启动标准版
docker compose up android-emulator

# 启动 GPU 加速版（推荐，性能更好）
docker compose up android-emulator-cuda

# 启动带 Play Store 的 GPU 版
docker compose up android-emulator-cuda-store
```

#### 方法二：纯 Docker 命令

```
# 构建镜像
docker build -t android-emulator .

# 运行容器（关键参数必须加上）
docker run -it --rm \
  --device /dev/kvm \                  # 启用 KVM 硬件加速（必须）
  -p 5555:5555 \                       # 暴露 ADB 端口
  --memory=4g \                        # 建议至少分配 4GB 内存
  android-emulator
```

### · · · 📱 连接模拟器与远程控制 · · ·

容器启动成功后，执行以下命令连接：

```
# 连接 ADB
adb connect 127.0.0.1:5555

# 查看设备列表
adb devices
```

### · · · 实时画面投屏（强烈推荐 🔥） · · ·

```
scrcpy
```

|  |  |  |
| --- | --- | --- |
| ![投屏效果1](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfx64LpOznGicy9ftibtTb0sD6Y1hlna1XX4ZaAicTAzzEaKr8QF6QbTOVDB9bc1OZKjTBWn8tFWkKxzW9SzI3dm2jXS2f7AkhHNX8/640?wx_fmt=png&from=appmsg) | ![投屏效果2](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfzLBrALamMz7fLVgXSNAVVp1lZlOGscbibQvDwNDCcwmuibvxOhWgyBwpXqFWJWDwbKKSIEyenHcysicBcgfB0h7M70vHhR6cIRKY/640?wx_fmt=png&from=appmsg) | ![投屏效果3](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyaLialX394sOqfbNvuxibKxyLjd2nSU9zb5N4xjIFD2icib7fMOI6WKWTia332llQEPfX0xjyEXyvMqp2e4zd8VUbosuP1IzvZiaAQE/640?wx_fmt=png&from=appmsg) |

默认使用 **Pixel 设备（1080×1920）**，操作流畅，适合远程调试。

### · · · ⚙️ 高级配置与用法 · · ·

#### 1️⃣ 持久化数据（不希望每次重启清空）

```
docker run -it --rm \
  --device /dev/kvm \
  -p 5555:5555 \
  -v ~/android_avd:/data \     # 挂载本地目录持久化 AVD 数据
  android-emulator
```

#### 2️⃣ 自定义构建 Android 版本

```
docker build \
  --build-arg API_LEVEL=34 \                    # 指定 Android 版本
  --build-arg IMG_TYPE=google_apis_playstore \  # 带 Play Store
  --build-arg ARCHITECTURE=x86_64 \             # 架构
  -t android-emulator-custom .
```

#### 3️⃣ 极致瘦身（跳过 SDK 打包）

```
docker build \
  --build-arg INSTALL_ANDROID_SDK=0 \   # 不打包 SDK
  -t android-emulator-slim .
```

运行时再挂载外部 SDK：

```
-v /your/path/to/android-sdk:/opt/android
```

#### 4️⃣ Play Store 版本注意事项

使用 Play Store 镜像时，需将本机 ADB 密钥复制到 `./keys` 目录：

```
cp ~/.android/adbkey ./keys/
cp ~/.android/adbkey.pub ./keys/
```

### · · · 🎯 适用场景 · · ·

* ●✅ 移动 App 自动化测试与 CI/CD
* ●✅ 多 Android 版本兼容性验证
* ●✅ 云服务器 / 远程开发环境
* ●✅ 稳定可重复的 Android 沙箱

### · · · 📦 预构建镜像（无需自己构建） · · ·

```
docker pull halimqarroum/docker-android:api-33
```

### · · · 📝 总结 · · ·

**docker-android** 是目前 Docker 中运行 Android Emulator **体验最好的方案之一**，配置灵活、性能优秀、文档清晰，非常值得收藏 ⭐

> 你已经在 Docker 中跑 Android 模拟器了吗？
>  欢迎在评论区分享你的用法或遇到的问题～

---

**点赞** 👍 + **在看** 👀 + **转发** 🔄
 我们下期继续分享更多实用开源工具！

参考资料:

[1] docker-android: https://github.com/HQarroum/docker-android

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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