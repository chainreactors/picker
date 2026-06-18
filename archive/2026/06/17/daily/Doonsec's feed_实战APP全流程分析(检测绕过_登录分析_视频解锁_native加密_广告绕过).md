---
title: 实战APP全流程分析(检测绕过/登录分析/视频解锁/native加密/广告绕过)
url: https://mp.weixin.qq.com/s/xHRastdqtUp3qmBlEPtk0w
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:48:48.348381
---

# 实战APP全流程分析(检测绕过/登录分析/视频解锁/native加密/广告绕过)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0TQ11ua67EpNk1RfTYyhntls25DxhD05FGKFwszQwz7WDFtvUKFRSjcq8hGwBQXw63g4DAy4M96DFNDX6USn7V1woIic3Af2nc/0?wx_fmt=jpeg)

# 实战APP全流程分析(检测绕过/登录分析/视频解锁/native加密/广告绕过)

Mengz3
Mengz3

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**0、分析结论摘要**

基本判断

* APP 名称：BeautyBox
* 包名：com.secret.prettyhezi
* 版本：5.1.5 / 120
* 目标 SDK：29
* 主要载荷：Java 层存在明显混淆，Native 层加载 `libali.so`
* 本次重点：重建样本基础信息、Manifest、启动链静态分析，以及 `abc.c()` 的 Native 解密算法

### 核心发现

* 启动入口为 `com.secret.prettyhezi.OuiCrGxF`，`Application` 为 `com.secret.prettyhezi.MainApplication`。
* 启动链同时存在 Root、模拟器、Xposed 等多条会直接触发 `m0()` 退出的环境检测分支；`debuggable` 检测则更偏提示性质。
* 启动阶段除了环境检测外，还会进入广告放行、登录态恢复与页面跳转等关键分支。
* `libali.so`

  通过 `JNI_OnLoad` 动态注册 `c.abc`，承担关键字符串常量返回与编解码能力。
* `abc.c(1)/c(2)/c(3)`

  并非简单查表，而是“密文表 + 自定义预处理 + Blowfish 解密 + 自定义后处理”的完整 Native 常量保护方案。

### 按实际逆向推进顺序看

* 第一步先从 `Manifest` 确认入口：`MainApplication` 与 `OuiCrGxF`。
* 第二步进入启动页 `OuiCrGxF.onCreate()`，定位多条启动检测与直接退出分支。
* 第三步结合 `hook.js` 绕过 Java 层检测、广告拦截与 Native `ptrace` 反调试，让样本能够顺利进入后续流程。
* 第四步继续顺着启动页向下拆，确认广告放行、登录态恢复与页面跳转的衔接关系，并识别出 `abc.c()` 与 `ea2/da2` 的 Native 介入点。
* 第五步分析登录页与自动登录链，确认请求统一汇入 `j.t(mode=1)`，再由 `abc.ea5/da5` 负责请求与响应的 Native 编解码。
* 第六步分析视频详情与积分解锁链，确认 `user/pverify/json -> rrvideo/unlock/json -> 用户态回写` 的完整业务流程，并用真实日志验证积分与经验变化。

**1、样本信息**

### 1.1 APK 基本信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2D0F0SBuJUiazqAzFBIpNEl0GGBqoGgMkaibEPkCia2ia3HBicJHgeTGhSOkHZ3pbtx7UhbfJ1qVbPDibaeNCFFSLouGY4Ph3VXYOtk/640?wx_fmt=png&from=appmsg)

### 1.2 Hash 信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0L7A823QRqgxUYIOENRTibjd2DFSAHRFRYUtiaGesmp9icJYia9XETkzvNL9U5k98dZmV3w7l8xGb98BZeLuo49CSpuyumqJyrgPc/640?wx_fmt=png&from=appmsg)

##

**2、分析环境**

### 2.1 设备 / 运行环境

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0ADE5u4LudHxQOJNS2RNLnB6J0TXfUb8Uw8kXPVnAWXTsRicTyWKTm0wU9SBG3WA2bu4IhrdQRQWoROzepgxaUdqCeJtC8a3Oc/640?wx_fmt=png&from=appmsg)

### 2.2 工具清单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0Pnqc6xQ8roBsHzoJia6Itnv3BQ8SLlgq0CxHZ6C2c0NKOEgibmGJYdU23TG0rlwFdzt69EdaqQ4BnFdOHLpGQp08ia9ia0l2bHA8/640?wx_fmt=png&from=appmsg)

**3、初始处理记录**

### 3.1 初始观察

* 样本未见明显壳特征，可直接进入 `jadx` 分析。
* 在已 Root 且装有 Magisk 的实验机上启动时出现白屏并退出，说明启动期存在明显环境检测。
* 从 `jadx` 代码来看，`OuiCrGxF.onCreate()` 是启动检测与配置调度的总入口。

### 3.2 原始文件与分析载荷

* 原始 APK：`com.secret.prettyhezi/BeautyBox_5.1.5.apk`
* Native 分析 IDB：`com.secret.prettyhezi/lib/arm64-v8a/libali.so.i64`

### 3.3 本次实际推进顺序

* 先读 `AndroidManifest.xml`，确认 `MainApplication` 与 `OuiCrGxF` 是后续静态分析的主抓手。
* 再跟进 `OuiCrGxF.onCreate()`，因为样本一启动就白屏退出，优先要解释“为什么起不来”。
* 锁定 `p0.d / p0.e / p0.a` 等启动检测后，结合 `hook.js` 逐项绕过 Java 检测，并在 Native 层替换 `ptrace`，让样本能顺利跑通启动流程。
* 样本放行后，继续沿 `OuiCrGxF` 拆出“广告放行 → 登录态恢复 → 页面跳转”这条启动主线。
* 在登录相关代码里观察到请求最终汇入 `j.t(mode=1)`，再顺着 `Server.e.c/a -> abc.ea5/da5` 识别出 Native 编解码链。
* 最后进入视频详情与积分解锁场景，用动态日志验证 `user/pverify/json`、`rrvideo/unlock/json`、积分扣减、经验刷新与 `keyCurUser<uid>` 回写是否和静态分析一致。

### 3.4 初步判断

* 启动失败与环境检测高度相关，不像普通网络错误或资源加载失败。
* `MainApplication.<clinit>()`

  会在 Java 层很早加载 `libali.so`，说明 Native 逻辑不是边缘功能。

**4、Manifest 分析**

### 4.1 AndroidManifest.xml 关键字段

| 项目 | 内容 |
| --- | --- |
| package | com.secret.prettyhezi |
| application name | com.secret.prettyhezi.MainApplication |
| main activity | com.secret.prettyhezi.OuiCrGxF |
| allowBackup | false |
| largeHeap | true |
| usesCleartextTraffic | true |
| requestLegacyExternalStorage | true |
| exported activity 数量 | 1 |

### 4.2 权限分析

| 权限 | 风险等级 | 用途判断 | 是否合理 |
| --- | --- | --- | --- |
| android.permission.ACCESS\_NETWORK\_STATE | 低 | 网络状态检测 | 是 |
| android.permission.INTERNET | 低 | 网络通信 | 是 |
| android.permission.READ\_EXTERNAL\_STORAGE | 中 | 读取外部存储 | 是 |
| android.permission.WRITE\_EXTERNAL\_STORAGE | 中 | 写入外部存储 | 是 |
| android.permission.REQUEST\_INSTALL\_PACKAGES | 高 | 安装 APK/更新包 | 是 |
| android.permission.WAKE\_LOCK | 低 | 保持设备唤醒 | 是 |

### 4.3 组件观察

* 主入口 Activity：`com.secret.prettyhezi.OuiCrGxF`
* `FileProvider`

  ：`com.secret.prettyhezi.fileprovider`
* 从 Manifest 看不到显式 `networkSecurityConfig`，但 `usesCleartextTraffic="true"` 已说明允许明文流量

**5、主流程分析**

打开 APP 先白屏退出，于是先去看 Manifest 和启动 Activity，定位到 OuiCrGxF.onCreate()。
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K36P91E43tmYGPI6osiaqrOUljArRbPKdByrG7Qr23BxZzdfDJjdv4yEDzlefIXRu2ASg18m2YSyqB1QWYr12RiaAaz5f6Vrm7R4/640?wx_fmt=other&from=appmsg)![]()
图 5-1  样本启动后先进入 OuiCrGxF.onCreate()，因此后续环境检测、广告控制、登录恢复等主流程都可以从这个入口继续往下追。

### 5.1 启动阶段环境检测链

#### 环境评分检测

`com.secret.prettyhezi.OuiCrGxF.onCreate()`

→ `p0.d.b().d(this, null)`

→ `m0()`

→ `System.exit(0)`

样本在启动很早阶段就会做一轮“多特征累计打分”的环境检测，命中后直接退出，不会继续走后续初始化。

```
// com.secret.prettyhezi.OuiCrGxF.onCreate(android.os.Bundle)
protected void onCreate(Bundle bundle) {
    super.onCreate(bundle);
    com.secret.prettyhezi.View.s.c();
W0();

// 启动后第一批检测之一就是 p0.d 的环境评分
// 一旦返回 true，就直接调用 m0() 结束整个 APP
    if (p0.d.b().d(this, null)) {
m0();
        return;
    }
    ...
}
```

```
// p0.d.b().d(this, null)
public booleand(Context context, c cVar) {
StringstrA = a("gsm.version.baseband");

// 基带版本异常时先记 1 分
inti6 = (strA == null || strA.contains("1.0.0.0")) ? 1 : 0;

StringstrA2 = a("ro.build.flavor");
// build flavor 命中 vbox / sdk_gphone 这类模拟器特征时加分
if (strA2 != null && (strA2.contains("vbox") || strA2.contains("sdk_gphone"))) {
        i6++;
    }
StringstrA5 = a("ro.hardware");
if (strA5 == null) {
        i6++;
    } else if (strA5.toLowerCase().contains("ttvm") || strA5.toLowerCase().contains("nox")) {
// 命中夜神 / Nox 等特征时大幅加分
        i6 += 10;
    }
intsize = ((SensorManager) context.getSystemService("sensor")).getSensorList(-1).size();
// 传感器数量过少也会作为可疑特征
if (size < 7) {
        i6++;
    }
intiC = c(p0.b.c().a("pm list package -3"));
// 用户安装应用数量太少时，也更像模拟器环境
if (iC < 5) {
        i6++;
    }
return i6 > 3;
}
```

函数作用：

* `OuiCrGxF.onCreate()`

  启动页总入口，前半段就串入了环境检测。
* `p0.d.d(Context, c)`

  按多项系统属性与设备特征累计打分判断是否像模拟器/虚拟环境。
* `m0()`

  统一结束所有活动并执行 `System.exit(0)`。

#### Xposed 检测

`com.secret.prettyhezi.Yclh4J3zF.onCreate()`

→ `p0.e.b().f()`

→ `m0()`

Xposed 检测在父类 `onCreate()` 中就已经执行，子类页面逻辑开始前就可能被拦截。

```
// com.secret.prettyhezi.Yclh4J3zF.onCreate(android.os.Bundle)
protected void onCreate(Bundle bundle) {
    super.onCreate(bundle);
    ...

// 父类 onCreate 中就会先做 Xposed 检测
// 命中后直接结束，不继续后续初始化
    if (p0.e.b().f()) {
m0();
    }
    ...
}
```

```
// p0.e.b().f()
public boolean f() {
try {
throw new Exception("gg");
    } catch (Exception e6) {
for (StackTraceElement stackTraceElement : e6.getStackTrace()) {
// 通过异常栈中是否出现 XposedBridge 来判断 Xposed
if (stackTraceElement.getClassName().contains("de.robv.android.xposed.XposedBridge")) {
return true;
            }
        }
return false;
    }
}
```

#### debuggable 检测

`com.secret.prettyhezi.OuiCrGxF.onCreate()`

→ `p0.e.b().a(this)`

→ `I("破解要小心哦~")`

debuggable 检测更偏提示性质，不承担强制退出逻辑。

```
// 这里检查当前包是否处于 debuggable 状态
// 命中后只弹提示，不会立即退出
if (p0.e.b().a(this)) {
I("破解要小心哦~");
}

// p0.e.b().a(this)
public boolean a(Context context) {
return (context.getApplicationInfo().flags & 2) != 0;
}
```

#### 第二套模拟器检测

这个检测藏在开头的父onCreate()中
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3aRvAa5vFtcZCJK1G53EhwSiapVBNo2iawqCE1FZqD0VIQvkQfxhqL6m5VffVARrz7UUAfTt8lv1TW0pr5h14LGNZlFNEaaBeZ8/640?wx_fmt=other&from=appmsg)![]()
图 5-2  除了前面的评分式检测外，样本在父类 onCreate() 中还额外埋了一套模拟器特征检测，命中后同样会直接退出。

`com.secret.prettyhezi.OuiCrGxF.onCreate()`

→ `p0.a.c(this)`

→ `m0()`

除了打分式环境检测外，样本还有一套独立的模拟器特征检测链，命中后同样直接退出。

```
// 这是另一套模拟器特征检测
// 只要命中特征，就直接结束 APP
if (p0.a.c(this)) {
    m0();
return;
}

// p0.a.c(this)
public static booleanc(Context context) {
ArrayListarrayList =new ArrayList();
try {
StringstrB = b(a(context));

// 先查静态特征，命不中再走备用检测
if (TextUtils.isEmpty(strB)) {
ListlistD = d(context);
if (listD.size() > 0) {
                arrayList.add(listD.get(0));
            }
        } else {
            arrayList.add(strB);
        }
    } catch (Exception e6) {
        e6.printStackTrace();
    }
return !arrayList.isEmpty();
}
```

#### Root 检测

`com.secret.prettyhezi.OuiCrGxF.onCreate()`

→ `p0.e.b().d()`

→...