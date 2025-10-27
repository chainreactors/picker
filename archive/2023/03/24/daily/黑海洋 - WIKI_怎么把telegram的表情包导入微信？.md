---
title: 怎么把telegram的表情包导入微信？
url: https://blog.upx8.com/3330
source: 黑海洋 - WIKI
date: 2023-03-24
fetch_date: 2025-10-04T10:30:27.364087
---

# 怎么把telegram的表情包导入微信？

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 怎么把telegram的gif表情包导入微信？

发布时间:
2023-03-23

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
45614

在Telegram里面添加一个机器人，就可以导出GlF格式的表情包啦。

**步骤简单：**直接在飞机里搜索**@tgstogifbot**机器人，然后想要那个表情直接发给机器人，机器人会打包出它所有尺寸的套图，拖到桌面解压，Gif发到微信收藏就可以了。

@Stickers（贴纸制作）
**GIF和贴纸下载↓**
@Sticker2GIFBot (支持动态贴纸)
@tgstogifbot (支持动态贴纸)
@GIFDownloader\_bot
@Stickerdownloadbot
@stickerset2packbot
@StickerResizerBot
@gif\_export\_bot
@fruitymelonbot
@WooMaiBot

成品可食用telegram表情包：[https://wwtc.lanzoum.com/itw9q0qulr4j](https://blog.upx8.com/go/aHR0cHM6Ly93d3RjLmxhbnpvdW0uY29tL2l0dzlxMHF1bHI0ag)

---

##### 另一个项目：把telegram导出的jpg/jpeg/png静态表情图片转换成微信能够导入的.gif文件

##### https://github.com/hellodk34/jpg2gif

---

# Telegram (\*.tgs) 到 GIF/PNG/APNG/WEBP 转换器的动画贴纸

将动画 Telegram 贴纸 (\*.tgs) 转换为 GIF / PNG / APNG / WEBP，并发布在了GitHub：[https://github.com/hadis898/tgbot-to-gif](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2hhZGlzODk4L3RnYm90LXRvLWdpZg)

### To easily convert stickers to GIFs you can use Telegram Bot：[https://t.me/tgstogifbot](https://blog.upx8.com/go/aHR0cHM6Ly90Lm1lL3Rnc3RvZ2lmYm90)

## 如何使用

有两种选择：使用[Docker](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZG9ja2VyLmNvbS8)运行和从源代码运行。

### 使用 Docker

用贴纸替换目录并运行：

* 转换为 GIF：

  ```
  docker run --rm -v <path to directory with stickers>:/source edasriyan/tgs-to-gif
  ```
* 转换为 PNG：

  ```
  docker run --rm -v <path to directory with stickers>:/source edasriyan/tgs-to-png
  ```
* 转换为 APNG：

  ```
  docker run --rm -v <path to directory with stickers>:/source edasriyan/tgs-to-apng
  ```
* 转换为 WEBP：

  ```
  docker run --rm -v <path to directory with stickers>:/source edasriyan/tgs-to-webp
  ```

您可以通过环境变量提供参数：

* `HEIGHT`：输出图像高度。默认值：512
* `WIDTH`：输出图像宽度。默认值：512
* `FPS`：输出帧率。默认值：apng、png、webp - 60；动图 - 50
* `QUALITY`：输出质量。默认值：90
* `THREADS`：要使用的线程数。默认值：CPU 数量

例子：

```
docker run --rm -e HEIGHT=256 -e WIDTH=256 -e FPS=30 -v /home/ed/Downloads/stickers:/source edasriyan/tgs-to-apng
```

结果将保存在同一目录中每个源贴纸文件旁边。

### From source

1. 安装依赖

   1. Make sure you have **C++17 compiler**, **make**, **[cmake](https://blog.upx8.com/go/aHR0cHM6Ly9jbWFrZS5vcmcv)** and **[conan](https://blog.upx8.com/go/aHR0cHM6Ly9jb25hbi5pby8)** tools installed; otherwise install them
   2. Make sure you have the tools installed:
      * **[gifski](https://blog.upx8.com/go/aHR0cHM6Ly9naWYuc2tpLw)** if you want to convert to GIF
      * **[ffmpeg](https://blog.upx8.com/go/aHR0cHM6Ly9mZm1wZWcub3JnLw)** if you want to convert to APNG
      * **[img2webp](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXJzLmdvb2dsZS5jb20vc3BlZWQvd2VicC9kb2NzL2ltZzJ3ZWJw)** if you want to convert to WEBP
   3. Install conan dependencies

      ```
      conan install .
      ```
2. Build

   ```
   cmake CMakeLists.txt && make
   ```

   CMake options
   `TGS_TO_PNG_STATIC_LINKING`: enable static linking. Default value: `OFF` if OS is darwin; otherwise `ON`

   ```
   cmake -DTGS_TO_PNG_STATIC_LINKING=ON CMakeLists.txt && make

   cmake -DTGS_TO_PNG_STATIC_LINKING=OFF CMakeLists.txt && make
   ```

   ARM troubleshooting (including Apple M1)
   Run the following command and try again:

   ```
   echo '#if defined(__ARM_NEON__)

   #include "vdrawhelper.h"

   void memfill32(uint32_t *dest, uint32_t value, int length)
   {
       memset(dest, value, length);
   }

   static void color_SourceOver(uint32_t *dest, int length, uint32_t color, uint32_t alpha)
   {
       int ialpha, i;

       if (alpha != 255) color = BYTE_MUL(color, alpha);
       ialpha = 255 - vAlpha(color);
       for (i = 0; i < length; ++i) dest[i] = color + BYTE_MUL(dest[i], ialpha);
   }

   void RenderFuncTable::neon()
   {
       updateColor(BlendMode::Src , color_SourceOver);
   }
   #endif
   ' > lib/src/rlottie/src/vector/vdrawhelper_neon.cpp
   ```
3. 转换

   * 转换GIF:

     ```
     ./bin/tgs_to_gif.sh /home/ed/Downloads/sticker.tgs
     ```
   * 转换PNG:

     ```
     ./bin/tgs_to_png.sh /home/ed/Downloads/sticker.tgs
     ```
   * 转换APNG:

     ```
     ./bin/tgs_to_apng.sh /home/ed/Downloads/sticker.tgs
     ```
   * 转换WEBP:

     ```
     ./bin/tgs_to_webp.sh /home/ed/Downloads/sticker.tgs
     ```
   1. 结果将保存在同一目录中的源标签文件旁边。

   #### CLI 参数

   ```
   $ ./bin/tgs_to_gif.sh --help
   usage: ./bin/tgs_to_gif.sh [--help] [--output OUTPUT] [--height HEIGHT] [--width WIDTH] [--threads THREADS] [--fps FPS] [--quality QUALITY] path

   Animated sticker for Telegram (*.tgs) to animated .gif converter

   Positional arguments:
    path              Path to .tgs file to convert

   Optional arguments:
    -h, --help        show this help message and exit
    --output OUTPUT   Output file path
    --height HEIGHT   Output image height. Default: 512
    --width WIDTH     Output image width. Default: 512
    --fps FPS         Output frame rate. Default: 50
    --threads THREADS Number of threads to use. Default: number of CPUs
    --quality QUALITY Output quality. Default: 90
   ```

   ## 注意事项

   您可以使用[@Stickerdownloadbot](https://blog.upx8.com/go/aHR0cHM6Ly90Lm1lL1N0aWNrZXJkb3dubG9hZGJvdA)下载 .tgs 文件。

##

[取消回复](https://blog.upx8.com/3330#respond-post-3330)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")