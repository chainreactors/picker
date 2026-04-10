---
title: 【安全研究】银狐远控远程屏幕使用场景和优化建议
url: https://mp.weixin.qq.com/s/eZaOYvjxsM0KQfq1WBoKMQ
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:44:02.417134
---

# 【安全研究】银狐远控远程屏幕使用场景和优化建议

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/IRUJvvhticxTic5kWiad8Id7GxczLOQKQ5fSL0mfhMFctAGJnErJPdeNFjmSlcDpAic8YbhkH3tk3FMPjevg5HAAtsp1lfrYbpqElRvZkBNmdA8/0?wx_fmt=jpeg)

# 【安全研究】银狐远控远程屏幕使用场景和优化建议

原创

安全研究员
安全研究员

CppGuide

![]()

在小说阅读器中沉浸阅读

特别申明：

**本文内容仅限于用作技术交流，请勿使用本文介绍的技术做任何其他用途，否则后果自负，与本号无关。**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/GSweNIrkicYuO7qxZCEZEPIa3STMW4wa20ylAJb7YVeqK8MAV71BZaDEV1eIvcZ4r2N5mr9pMJwnuiav2c0dTTEg/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

银狐远控除了提供了后台桌面这种非正常屏幕，还提供了差异屏幕、高速屏幕和娱乐屏幕三种远程屏幕。

下面从总体和关键实现逻辑上介绍一下它们的区别和使用场景。

## 三种屏幕模式技术分析

### 核心参数对比

| 特性 | 差异屏幕 | 高速屏幕 | 娱乐屏幕 |
| --- | --- | --- | --- |
| **压缩算法** | zlib deflate | JPEG (libjpeg) | H.264 (x264) |
| **默认色深** | 8-bit (可选 4/8/16/32) | 32-bit BGRA (固定) | 32-bit BGRA (固定) |
| **默认帧率** | 1 fps | 1 fps | 30 fps |
| **差异检测单元** | 扫描线，步长19行，偏移24px | 网格，Y步长10行，X步长32px | 无（整帧编码） |
| **线程模型** | 2线程 (工作+控制) | 2线程 (工作+控制) | 3线程流水线 (采集→编码→发送) |
| **首帧传输** | 全屏 bitmap → zlib压缩 | 全屏 → JPEG压缩 | SPS/PPS + IDR帧 |
| **后续帧** | 仅变化矩形 → zlib | 仅变化矩形 → 各自JPEG | 连续 P/B 帧流 |
| **质量调节** | 无（色深切换代替） | 60 / 85 / 100 三档 | 码率 + preset |
| **多显示器** | 不支持 | 不支持 | 支持 (Monitor 枚举) |
| **录制** | 无 | 无 | MP4 录制 |

### 一、差异屏幕 (`ScreenSpy.cpp` — DEF\_STEP=19, OFF\_SET=24)

**工作原理：**

```
全屏抓图 → 逐行扫描(步长19行) → 和上帧对比单像素 →
找到变化行 → 向上下各扩展 OFF_SET(24) → zlib压缩矩形 → 发送
```

**关键代码** (`差异屏幕/ScreenSpy.cpp:161`)：

```
::SetRect(&m_changeRect, -1, nStartLine-DEF_STEP, -1, nStartLine+DEF_STEP*2);
// 对比时按 m_nIncSize 步长跳跃(32/biBitCount 个像素)
for (int j = 0; j < m_nFullWidth; j += m_nIncSize)
    if (*p1 != *p2) { ... }
```

**适用场景：** 网络带宽极差（拨号/低速网络）、被控端屏幕静止内容多（文档操作、命令行）、需要低色深节省流量

**缺点：** 步长19行会漏检两次扫描之间的变化行；矩形合并策略粗糙，一行有变化就扩展整个宽度带来大量无用数据

### 二、高速屏幕 (`ScreenSpy.cpp` — DEF\_YSTEP=10, DEF\_XSTEP=32)

**工作原理：**

```
双缓冲采集(last/curr) → 网格扫描(10行×32像素块) →
对比上一帧 → 对每个变化矩形独立JPEG编码 →
按需zlib二次压缩 → 发送 [矩形JPEG长度+数据+坐标]
```

**关键代码** (`高速屏幕/ScreenSpy.cpp:325`)：

```
for (int y = m_nScanLine; y < m_nFullHeight; y += DEF_YSTEP)
    for (int x = 0; x < m_nFullWidth; )
        if (*p1 != *p2) { /* JPEG压缩该矩形 */ }
```

首帧和后续帧都发送算法标识字节，支持运行时切换到 XVID（预留接口）。JPEG质量默认85，可动态调整。

**适用场景：** 普通宽带环境、屏幕有持续动态内容（视频窗口、游戏界面）、需要较好画质同时保持响应速度

**优势：** JPEG对自然图像压缩率高于zlib raw bitmap，32-bit真彩色画质好；双缓冲避免撕裂

### 三、娱乐屏幕 (`H264ScreenManager.cpp` — x264 ultrafast+zerolatency)

**工作原理：**

```
采集线程: BitBlt → BGRA帧 → libyuv转YUV420 → 入YUV队列
编码线程: YUV队列 → x264编码(ultrafast预设) → NAL单元 → 入H264队列
发送线程: H264队列 → TCP发送 [PacketHead+NAL数据]
```

**关键初始化** (`H264ScreenManager.cpp:141`)：

```
std::string x264_preset = "ultrafast";
std::string x264_tune  = "zerolatency";
fps = 30; btl = 9000; // 9000 kbps
```

x264 库从内存中加载（`MemoryLoadLibrary`），不依赖系统安装。

**适用场景：** 高带宽局域网环境、被控端有视频/游戏等高动态内容、需要录制操作过程（MP4）、多显示器切换

### 可优化方向

#### 1. 差异屏幕 — 扫描策略粗糙

**问题：** 步长19行 + 固定 OFF\_SET 24px 导致漏检+过量传输

```
// 当前：以整行宽度作为变化矩形宽度
::SetRect(&m_changeRect, -1, nStartLine-DEF_STEP, -1, nStartLine+DEF_STEP*2);
m_changeRect.left = j - OFF_SET;  // 仅左右收缩，不收缩上下
```

**优化：** 先做 dirty region 汇总，合并相邻小矩形后再压缩，避免一行小变化触发整宽矩形传输

#### 2. 高速屏幕 — 每帧重新 JPEG 编码开销

**问题：** 每个变化矩形独立调用 `jpeg_create_compress`/`jpeg_destroy_compress`，在变化区域多时重复创建/销毁压缩器开销大

```
// BMP_JPG() 每次创建、销毁 jcs
jpeg_create_compress(&jcs);
// ... 编码 ...
jpeg_destroy_compress(&jcs);
```

**优化：** 复用 `jpeg_compress_struct`（libjpeg 支持 reinit），或改用 libjpeg-turbo 的 `tjhandle` 池

#### 3. 高速屏幕 — 增量扫描行轮转未实现

**问题：**`m_nScanLine` 字段存在但 `getNextScreen` 中扫描始终从0开始，没有真正做分帧轮转

```
// 初始化
m_nScanLine = 0;
// getNextScreen 中
ScanChangedRect(TRUE); // 每次全屏扫描
```

**优化：** 实现 scanline 轮转（每帧只扫 1/N 行，N帧完成全屏），降低单帧CPU占用

#### 4. 娱乐屏幕 — 码率固定 9000kbps，无自适应

**问题：**`btl = 9000` 硬编码，网络差时会导致 NAL 队列积压、延迟增大

```
fps = 30; btl = 9000; // 固定码率
```

**优化：** 监测发送队列深度，动态调整 `x264_param.rc.i_bitrate`，实现简单的 ABR/CBR 自适应

#### 5. 三种模式共同问题 — FPS 控制用 `Sleep` 忙等

```
// 差异屏幕 / 高速屏幕
while (GetTickCount() - m_dwLastCapture < m_dwSleep)
    Sleep(10);
```

`GetTickCount` 精度 15ms，`Sleep(10)` 实际睡 ~15ms，导致帧率不精确。**优化：** 改用 `timeSetEvent` 或 `CreateWaitableTimer` 实现精确帧率定时

#### 6. 差异屏幕 — 色深切换重启线程代价高

**问题：**`ResetScreen()` 在切换色深时完全销毁重建 `CScreenSpy` 对象

```
void CScreenDifManager::ResetScreen(int biBitCount) {
    m_bIsWorking = false;
    WaitForSingleObject(m_hWorkThread, INFINITE); // 阻塞等待
    delete m_pScreenSpy;
    m_pScreenSpy = new CScreenSpy(biBitCount);
    m_hWorkThread = _beginthreadex(...); // 重新启动
}
```

**优化：**`CScreenSpy` 内部支持动态切换色深，无需重建对象和线程

---

### 选用建议

```
带宽 < 512Kbps  → 差异屏幕（8-bit灰度模式）
带宽 1-10Mbps   → 高速屏幕（质量85，动态fps）
带宽 > 10Mbps   → 娱乐屏幕（适合视频/游戏，支持录制）
局域网实时控制   → 高速屏幕（延迟最低，无编码器初始化延迟）
```

关于银狐远控的可以优化点很多，维护这一年多以来，我总共修复了100+问题，github提交记录就有`568`次之多。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/GSweNIrkicYuRVsKvmF9ymjCFtAmFmQG79ofibtmmxZNcXAJyVrWNGZxh2249NtiaQ3SezP2eSib7icepPSgU28ZctA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

当然，虽然这套源码bug挺多的，但瑕不掩瑜，它仍然是学习C/C++开发、多线程编程、网络编程、安全工程、综合项目实践、红蓝攻防非常好的材料。

为了更方便排查和优化代码，我除了修复以上bug以外，还将这套代码从原来的Visual Studio 2010工程全部升级成Visual Studio 2022，并补全和重编译了所有依赖库代码，并去掉所有后门，现在它是一款可以放心使用的远控软件。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IRUJvvhticxRS1k8ibbre5BFZia2uhyLUe7OJNcdkO3W1bf0mibd4GHgCaB2zNXp14ww27S4rv9iblqAv8rPNick6rZQng4BCAZQbA5XkA5mmapoo/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

由于篇幅有限，本次分享就到这里了，后续我将会更新更多的C/C++开发知识，欢迎关注公众号CppGuide。

源码获取

如果对银狐（winos）有兴趣，可以通过下面的方式获取全套源码：

关注后回复【winos】即可获取源码

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