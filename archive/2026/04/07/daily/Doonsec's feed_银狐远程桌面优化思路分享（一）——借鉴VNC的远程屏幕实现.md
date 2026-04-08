---
title: 银狐远程桌面优化思路分享（一）——借鉴VNC的远程屏幕实现
url: https://mp.weixin.qq.com/s/mG4aEL5rrhbUs01C27Irtg
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:33:21.951916
---

# 银狐远程桌面优化思路分享（一）——借鉴VNC的远程屏幕实现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IRUJvvhticxSbflH28EP5R5SP0xjLbxjnpmtAAlfzoJr34jQ5QbUh92LbzeKAX5z3Adt6v3f5NOx8QibChLEibiaNe1hjHCmTBEXA0NWq4LdCic0/0?wx_fmt=jpeg)

# 银狐远程桌面优化思路分享（一）——借鉴VNC的远程屏幕实现

原创

安全研究员
安全研究员

CppGuide

![]()

在小说阅读器中沉浸阅读

前言

这几年来，我一直在研究远程桌面技术，市面上便宜好用的远程桌面软件并不多，因此我一直想做一套比较好的远程桌面系统。远程桌面的核心是抓屏、传输和渲染。

我为此储备了一些基于WebRTC的技术，由于这个目前还在学习中，思路不成熟，暂时不提。

另外一种就是基于传统的GDI抓屏，为此我很早就研究了VNC的源码（包括RealVNC和tigerVNC等源码），并且由于这款软件的代码的实用性比较大，我在《[C/C++编程实战训练营](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247499222&idx=2&sn=d44789c463a8362d2ae1548dd8f76d00&scene=21#wechat_redirect)》中也给小伙伴们拆解了这套源码，由于大多数同学的目的对Windows图形方面的内容不是特别关注，因此在训练营拆解这些源码时，这块的内容讲的比较简略。所以这篇文章也可以看作是对VNC源码中桌面渲染实现的补充。

银狐的一共提供了4个远程桌面功能，其中`差异屏幕`、`高速屏幕`和`后台屏幕`，前三种屏幕都是正常的屏幕截图技术，只不过在屏幕数据传输大小和渲染效率上做了不同的取舍，而后台屏幕不是正常的屏幕，它是一个限制了很多正常界面操作的不可见桌面。

老实说，银狐前三类屏幕的实现上效率一般，导致其远程屏幕的效果也不是非常好。这里也可以借鉴VNC源码中的远程桌面效果来优化。但是，如果你去读VNC的源码，你会发现它的代码风格比较晦涩难懂。因此，这篇文章作为VNC源码的一个导读篇，希望对有需要的同学提供一些参考。

以下是 RealVNC 4.1.3 远程桌面画面实现的详细分析：

以下是 RealVNC 4.1.3 远程桌面画面实现的详细分析：

---

## 一、屏幕像素抓取（服务端）

### 核心文件结构

| 文件 | 作用 |
| --- | --- |
| `win/rfb_win32/SDisplay.cxx` | 主显示抽象层，支持3种更新模式 |
| `win/rfb_win32/DeviceFrameBuffer.cxx` | Win32 实际抓屏实现 |
| `win/rfb_win32/SDisplayCorePolling.cxx` | 轮询式变化检测 |
| `common/rfb/SDesktop.h` | 平台无关桌面接口 |

### 三种屏幕更新模式（`SDisplay.cxx` 第45-46行）

**模式 0 - 轮询（Polling）**（`SDisplayCorePolling.cxx`）

* 将屏幕划分为 16 个水平条带（第29行 `POLLING_SEGMENTS`）
* 定时器每 50ms 触发一次，逐条带扫描（第39, 60-81行）
* 比较新旧像素数据，检测变化区域

**模式 1 - 应用钩子（默认）**

* 通过 `WMHooks` 拦截窗口消息，即时通知变化

**模式 2 - 驱动钩子**

* 通过 DirectX/视频驱动获取变化通知

### 像素抓取实现（`DeviceFrameBuffer.cxx` 第107-120行）

```
BitBlt(memDC, ...)  ← Win32 GDI 抓屏
     ↓
PixelBuffer        ← 像素缓冲区存储
     ↓
ComparingUpdateTracker  ← 差异对比，生成变化矩形列表 (Region)
```

三种屏幕更新模式的详细细节后续文章会继续分析。

## 二、数据量压缩（编码层）

### 编码器工厂（`common/rfb/Encoder.cxx` 第67-75行）

支持的编码类型按压缩效率排列：

### 1. Raw 编码（`common/rfb/RawEncoder.cxx`）

* `RawEncoder::writeRect()` 第39行
* 直接写入原始像素字节，无压缩，作为兜底编码

### 2. RRE 编码（`common/rfb/RREEncoder.cxx` + `rreEncode.h`）

* 第47行：将矩形像素读入缓冲区
* 第58行：统计最高频颜色作为背景色
* 第60-79行：将不同颜色区域编码为"背景色 + 子矩形列表"
* 若编码后大于原始大小则回退到 Raw（第65-66行）

### 3. Hextile 编码（`common/rfb/HextileEncoder.cxx` + `hextileEncode.h`）

* 将矩形切分成 **16×16 的小瓦片**（tile）
* 对每个 tile 分析颜色特征：

+ 单色 tile → 仅存储背景色标志
+ 多色 tile → 背景色 + 带颜色的子矩形列表

* 标志位：`hextileBgSpecified` / `hextileFgSpecified` / `hextileAnySubrects`（第75-88行）

### 4. ZRLE 编码（`common/rfb/ZRLEEncoder.cxx` + `zrleEncode.h`）

* `ZRLEEncoder.h` 第48行：内含 `ZlibOutStream` 成员
* 切分成 **64×64 的瓦片**，对每个 tile：

+ 建立调色板（最多128色）（第72-77行）
+ 对调色板索引做 **游程编码（RLE）**
+ 最终再经过 **Zlib 压缩**

* 压缩率最高（20-50x），适合低带宽

### 数据流

```
PixelBuffer（屏幕截图）
  → ImageGetter::getImage()       [提取像素，格式转换]
  → Encoder::writeRect()          [选择编码方式]
  → SMsgWriter::writeRect()       [写入 RFB 协议头]
  → OutStream::writeBytes()       [网络发送]
```

---

## 三、客户端屏幕渲染

### 解码层（`common/rfb/`）

| 文件 | 作用 |
| --- | --- |
| `CMsgReader.h` 第36-73行 | RFB 消息读取器 |
| `CMsgHandler.h` 第34-68行 | 回调接口定义 |
| `Decoder.cxx` 第60-68行 | 解码器工厂 |

### 各编码解码过程

**RawDecoder** (`RawDecoder.cxx` 第38-55行)

* 第45行：分配图像缓冲区
* 第50行：从网络流读取原始字节
* 第51行：调用 `handler->imageRect()` 渲染

**RREDecoder** (`rreDecode.h` 第41-59行)

* 第47行：读取子矩形数量（U32）
* 第48行：读取背景色
* 第52-57行：循环读取每个子矩形的颜色、坐标(U16)、尺寸(U16)，调用 `FILL_RECT()` 填充

**HextileDecoder** (`hextileDecode.h` 第43行起)

* 第53行：分配 16×16 像素缓冲区
* 第61行：读取 tile 类型标志位
* 第69-70行：按需读取背景/前景色
* 第84-100行：解码子矩形（坐标/尺寸各4 bit 压缩存储）

**ZRLEDecoder** (`ZRLEDecoder.cxx` 第56-95行 + `zrleDecode.h`)

* 第58-59行：创建 `ZlibInStream` 解压
* 第70行：读取模式字节（bit7=RLE标志，bit0-6=调色板大小）
* 逐 tile 解码后调用 `IMAGE_RECT()` 或 `FILL_RECT()` 渲染

### Windows 客户端渲染（`win/vncviewer/`）

**`DesktopWindow.cxx`** 核心渲染方法（第98-102行）：

* `fillRect()` — 填充纯色矩形
* `imageRect()` — 渲染像素缓冲到屏幕
* `copyRect()` — 服务端矩形复制优化（无需传像素数据，直接让客户端拷贝已有区域）
* `invertRect()` — 鼠标光标渲染

底层使用 **Win32 DIB**（设备无关位图，`DIBSectionBuffer.h`）+ `BitBlt/StretchBlt` 最终呈现。

### 完整渲染流水线

```
网络流 (InStream)
  → CMsgReader::readMsg()        [解析 RFB 协议头]
  → Decoder::readRect()          [按编码类型解压/解码]
  → CMsgHandler 回调:
       handler->fillRect(rect, color)
       handler->imageRect(rect, pixels)
  → DesktopWindow 方法           [写入 DIB 位图缓冲]
  → Win32 BitBlt                 [呈现到屏幕]
```

---

## 压缩效率对比

| 编码 | 适用场景 | 压缩倍率 | 速度 |
| --- | --- | --- | --- |
| Raw | 兜底/测试 | 1x | 最快 |
| RRE | 纯色UI元素 | 1-10x | 快 |
| Hextile | 混合UI/图形 | 5-20x | 中 |
| ZRLE | 复杂图形/低带宽 | 20-50x | 慢 |

所有编码均通过宏模板支持 8/16/32 bpp 三种像素深度（在各 `*Encode.h`/`*Decode.h` 中通过 `#define BPP` 多次 include 实现）。

推荐阅读

[银狐远控问题排查与修复——Viusal Studio集成Google Address Sanitizer排查内存问题](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500025&idx=1&sn=62b234c8bddb267c6eb784fd8d3399b5&scene=21#wechat_redirect)

[银狐远控代码中差异屏幕bug修复](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500193&idx=1&sn=c7587c2b9d369f8a2bac15b4c648a343&scene=21#wechat_redirect)

[银狐远程屏幕内存优化方法探究](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500211&idx=1&sn=b022b7b171b8cddebef644b6fa26ee11&scene=21#wechat_redirect)

[银狐远程软件bug修复记录 第03篇](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500231&idx=1&sn=832d03b96f7c1713360c348c7ecce1de&scene=21#wechat_redirect)

[银狐远程软件 UDP 断线无法重连的bug排查和修复](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500363&idx=2&sn=1295e4610a5ff1ecc88f945b6767bd25&scene=21#wechat_redirect)

[银狐远程软件代理映射功能优化思路分享](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500374&idx=1&sn=cb33088e888e38b22f47b9ced854f29b&scene=21#wechat_redirect)

[银狐远程软件去后门方法](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500417&idx=1&sn=a9341ca6ac543ec4d1d53f1ce202934a&scene=21#wechat_redirect)

[银狐远控一键编译调试与开发教程](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500459&idx=1&sn=040336ebb05520aaf8bc8e96f224b921&scene=21#wechat_redirect)

[银狐远控免杀与shellcode修复思路分析 01](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500498&idx=1&sn=4b65c471f42785cb7157e807bb9ea12d&scene=21#wechat_redirect)

[银狐ShellCode混淆怪招](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500526&idx=1&sn=43dc3ebdd4d5277fd0bc6ffd0a5a0356&scene=21#wechat_redirect)

[详解银狐远控源码中那些C++编码问题](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500571&idx=1&sn=9e57cfeb1c51e063f5954fa7caf41676&scene=21#wechat_redirect)

[给银狐远控增加一个小功能01](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500609&idx=1&sn=e204c8c65dd0b33cacf3ba8c62c26472&scene=21#wechat_redirect)

[银狐远控的被控端是如何隐藏和保护自己的](https://mp.weixin.qq.com/s?__biz=Mzk0MjUwNDE2OA==&mid=2247500651&idx=1&sn=4597e6792b8516065d045db6ec6b0c65&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYvM1mIwPctlYONEDKJwUfRZ57uAkVR59MpX1cVnmmnyPZ5O9OCuys78Sy6fOEncwfgWpgCo9Tibeag/0?wx_fmt=png)

CppGuide

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYvM1mIwPctlYONEDKJwUfRZ57uAkVR59MpX1cVnmmnyPZ5O9OCuys78Sy6fOEncwfgWpgCo9Tibeag/0?wx_fmt=png)

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