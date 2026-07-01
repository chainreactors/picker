---
title: 手搓 JniForward：Unidbg JNI 转发真实 Android ART 的探索
url: https://mp.weixin.qq.com/s/2PYClQ3k1WZQc5Q3TQnqDA
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:22:27.636333
---

# 手搓 JniForward：Unidbg JNI 转发真实 Android ART 的探索

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2YuaS6vOm2U70IXeRJTsRicPbbH59qRgqVy1BxcxlO3RQgKvK3jQBicacek48RVhbWSAehzpaWznmQYDZQTUwUqR4yKMcZ2ias6U/0?wx_fmt=jpeg)

# 手搓 JniForward：Unidbg JNI 转发真实 Android ART 的探索

r8e8cd8
r8e8cd8

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 论坛里偶尔能看到「SO 在 PC 模拟、JNI 丢真机跑」的说法，当时没看太懂中间怎么接。后来手写补环境补烦了，自己撸了一版。

* Unidbg 跑 SO，Native 一般没问题，一回调 JNI 就卡：`TreeMap` 遍历、`String.getBytes`、`getPackageManager` 等，全得 `AbstractJni` 里 switch。
* 换 App 就复制改一轮；Iterator 状态、字符编码差一点点，签名就歪。
* 想搞明白的是：**Native 继续在 Unidbg 里跑，JNI 里哪些该扔真机、怎么传、怎么接回来。**

下面先简单说下整体思路，再写实现细节和踩坑。

**整体思路**

**分工：PC 跑 SO，手机跑该真算的那部分 Java**

* SO 的 Native 指令仍在 Unidbg/Unicorn 里执行。
* 遇到 `java/*` 这类 JNI（`TreeMap`、`String.getBytes` 等），PC 不在 `AbstractJni` 里硬编返回值，而是经 adb 发一行 JSON 到手机 Agent，在真机 ART 里调完，再把结果传回。
* PC 和手机之间用 **JSON 一行一问一答**，方便写协议、对 log。

**对象跨进程：只传编号，不传指针**

* Unidbg 里 SO 拿到的 Java 引用，本质是 `**DvmObject`\*\*（模拟器里的「Java 对象壳」）。
* 真机 Agent 里对应的是 `**jobject`\*\* / 普通 Java 对象。
* 这两者都不能塞进 Socket，所以线上只传 `**Handle`（整数编号）\*\*，两边各一张表：`编号 → 真对象`。

举个短例子（SO 遍历 TreeMap）：

* PC 发 JSON，让手机 `new TreeMap({"width":"1080"})`，手机登记 **1001**，回 `{HANDLE, 1001}`。
* PC 收到后造一个 `**DvmObject` 壳\*\*，里面不写真 Map，只记「远程编号 = 1001」——SO 以为手里有个 Java 对象，继续跑。
* SO 调 `entrySet()`，PC 再发 JSON：`对 HANDLE 1001 调 TreeMap->entrySet`；手机查表找到真 TreeMap，调完登记 **1002** 回传。
* PC 又造一个新 `**DvmObject` 壳\*\*（编号 1002），SO 接着调 `iterator`、`hasNext`、`next`……**Iterator 的状态一直在手机那张表里**，PC 只传递编号。

要点：PC 的 `DvmObject` 多半是「指向手机的遥控器」；手机 Handle 表里才是 `TreeMap`、`Iterator` 本体。同一条链里编号对得上就行，PC 的 1003 和手机的 1003 不要求是同一个内存对象。

**手机算完之后怎么传回来？按返回值类型来**

一次 JNI = 一次 JSON 往返。手机 invoke 完，**按 JNI 返回值是什么类型**，在 JSON 里带不同的 `result`，不是固定只传 Handle：

* **返回 Java 对象**

  （Map、Iterator、Entry…）→ `HANDLE` 编号，PC 造 `DvmObject` 壳，下次 JNI 再把这个编号发回去。
* **返回 boolean / int 等**

  → `BOOL`、`I32` 等，把值直接传回来。
* **返回 byte[]**

  → `BYTES`（Base64），比如 `String.getBytes()`。
* **返回 String**

  → `STRING`，PC 包成 `StringObject`。
* **void / null**

  → `NULL` 或空 result。

对象还要链式调用（`next` 再 `getKey`），就靠 Handle 来回指；字符串、字节数组 **把值传回来就行**，SO 在 Native 里直接用，通常不必再登记成 Handle。

**分流：不是全部 JNI 都上网**

* 独立 Agent 是单独安装的 App，没有目标 App 的 Context / ClassLoader。
* `java/`*、`javax/`*

  → 发手机（JDK 类，ART 算得准）。
* `android/*`

  、包名签名、`com.xxx` 业务类 → 留 PC 补环境。
* 以后若接 Frida / Xposed 模块（跑在目标进程里），这条边界可以往后挪，协议不用改。

##

**几种做法（简单对比）**

本质都是：**PC 截 JNI → 发请求 → 真机 ART 执行 → 结果回传**。

差别在执行端放哪、要少写多少补环境。

* **纯 Unidbg 手写补环境**

  — 不连手机，全在 `AbstractJni` 里 switch；简单，JNI 多了难维护。
* **Unidbg + 独立 Agent APK + adb（我用的）**

  — PC 跑 SO，`java/`\* 发 JSON 到自写 App；包名、业务类仍 PC 补；不 root、不注入目标 APK。
* **Frida / Xposed 当 Agent**

  — 跑在目标 App 进程里，**能补的环境更多**（Context、业务类、包名等）；JSON 协议可以共用，但注入/框架 **有可能被检测**，我还没做到这一步。

##

**整体架构**

##

```
PC（Unidbg）
  libxxx.so 在 Unicorn 里跑
  SO 调 JNI
    ↓
  【代理层】拦住所有 Jni 回调，统一进 Router
    ↓
  【Router.dispatch】打包成一次 JniCall（方法名 + 参数）
    ↓
  【路由策略】看 signature 前缀
    ├─ java/*、javax/*  ──► 【远程执行器】编 JSON → adb → 手机
    └─ android/*、业务类  ──► 【本地执行器】反射调 AbstractJni 补环境
手机 Agent
  127.0.0.1:8765 收 JSON → 真机 invoke → 回一行 result（HANDLE/BOOL/BYTES…）
```

**Router 在架构里干什么（和上面对应）**

Router 本身**不算 JNI、也不连手机**，只做三件事：

* **统一入口**

  — SO 每次 JNI 都先到 `dispatch(方法名, 参数)`，不再散落到各处 switch。
* **打包**

  — 压成 `JniCall`，后面无论本地还是远程，格式一致。
* **分拣**

  — 查 signature：

* `java/util/Iterator->hasNext()Z`

  → 远程 → 发手机 → 回来 `BOOL`
* `java/util/Iterator->next()...`

  → 远程 → 回来 `HANDLE` → PC 造 `DvmObject` 壳
* `android/app/Application->getPackageManager()...`

  → 本地 → 进本地补环境
* `acceptMethod`

  → 本地（只问接不接，不是最终执行）

分拣之后是两条执行链，**互斥、只走一条**：

```
JniCall
  → 路由：isRemote?
       否 → LocalJniExecutor → 反射调 AbstractJni（补环境 switch）
       是 → RemoteJniExecutor → JSON 往返 → JniArgBridge 译回 DvmObject/boolean/bytes
```

所以架构图里「代理 → Router → 分叉」就是：**先进 Router 再决定本地算还是手机算**；控制台 `[local]` / `[remote]` 就是这次走了哪条叉。

Native 指令只在 PC；需要真 JVM 的 JNI 才走右边那条叉。

## Router 到底是干什么的、怎么分发

可以把它想成快递分拣中心：SO 每次调 JNI，都先到 Router，Router **不自己算**，只负责「这单该本地送还是发手机」。

### 第一层：统一入口（代理）

Unidbg 原来直接调 `AbstractJni`。我在外面包了一层**动态代理**：任何 `callObjectMethod`、`findClass`……先进代理，代理只做一件事：

```
return router.dispatch(方法名, 参数数组);
```

这样不用改 Unidbg 源码，用户还是 `vm.setJni(this)`。

### 第二层：打包（JniCall）

Router 收到「方法名 + 参数」，压进一个小结构：

```
public Object dispatch(String op, Object... args) {
return executor.execute(new JniCall(op, args));
}
```

`op` 比如 `"callObjectMethodV"`，`args` 里是 `[vm, dvmObject, signature, varArg]`。

**为什么要打包？** 后面发 JSON 时，整包 `JniCall` 转 args 就行，Router 本身不关心本地还是远程。

### 第三层：选执行器（Hybrid）

真正「分发」发生在 `HybridJniExecutor`：

```
public Object execute(JniCall call) throws Throwable {
if (!路由策略.isRemote(call)) {
return 本地执行器.execute(call);   // 还是调 AbstractJni
    }
try {
return 远程执行器.execute(call);   // 发 JSON 到手机
    } catch (IOException e) {
if (允许回退) return 本地执行器.execute(call);
throw e;
    }
}
```

**路由策略怎么判？** 从参数里找出 JNI 的 signature 字符串（形如 `java/util/Iterator->next()Ljava/lang/Object;`）：

* 以 `java/`、`javax/` 开头 → **发手机**（框架类，真机 ART 算最准）
* 以 `android/`、`com/`、`org/` 开头 → **留 PC**（包名、系统 API、业务类）
* `acceptMethod`

  / `acceptField` → **永远 PC**（只是 Unidbg 问「该方法是否由补环境接管」，不是真执行）

判完以后，两条路：

**本地路**：`LocalJniExecutor` 用反射找到 `Jni` 接口上对应方法，调原来的实现类——和没加转发前一模一样，补环境 switch 还写在这。

**远程路**：`RemoteJniExecutor` 把 `JniCall` 编成 JSON，Socket 发到 8765，等手机回一行 JSON，再解码塞回 Unidbg。

### 第四层：日志（可选）

外面再包一层「打印执行器」，控制台就会看到：

```
JNI >> [remote] callObjectMethod java/util/Iterator->next()Ljava/lang/Object;
JNI >> [local]  callObjectMethod android/app/Application->getPackageManager()...
```

`[remote]` / `[local]` 就是 Router 分发结果的直观体现。

**一句话**：Router = 统一进门 → 打包成 JniCall → 按类名前缀分拣 → 本地反射 or 远程 JSON。

**我是怎么一步步做的**

**第 1 步：先想直接改 AbstractJni —— 不行**

最开始很直接的想法，把 Unidbg 里每个 JNI  override 改成一行转发，例如：

```
@Override
public DvmObject<?> callObjectMethod(BaseVM vm, DvmObject<?> o,
String signature, VarArg varArg) {
return (DvmObject<?>) router.dispatch("callObjectMethod", vm, o, signature, varArg);
}
```

`findClass`、`callBooleanMethod` 等几十个方法都要这么改。能跑，但：

* 动的是框架源码，以后升级 Unidbg merge 很痛苦；
* 本地 / 远程写死在改过的类里，不好切换。

后来改成 **不动 AbstractJni**，外面用动态代理包 `Jni` 接口，再只做 Router + 本地反射，跑通 SO 确认和改之前结果一致。

**第 2 步：定 JSON 协议 + PC 端假 Agent**

在 PC 再起一个监听 8765 的小程序，用真 Java 处理 TreeMap/Iterator，跟未来手机 Agent 同一套 JSON。协议定成 **一行 JSON 一问一答**，方便 log 里直接 grep。

**遇到的问题：Unidbg 回调名带 `V`，Agent 只认不带 `V` 的 op**

Unidbg 的 `Jni` 接口里，处理可变参数的方法名末尾会多一个 `V`（表示 VarArg），比如 `callObjectMethodV`、`callBooleanMethodV`。我在 PC 侧用动态代理转发时，`method.getName()` 拿到的就是这个带 `V` 的名字，原样写进 JSON 的 `op` 字段。

假 Agent 分发器是按「不带 V 的标准名」写的 switch，两边对不上：

```
// PC 侧：代理里 method.getName() 拿到的名字
request.setOp("callObjectMethodV");   //  JSON 里 op 带 V 不行

// Agent 侧
switch (req.getOp()) {
case "callObjectMethod":   // 只注册了这条
return invokeObjectMethod(req);
default:
throw new UnsupportedOperationException("unknown op: " + req.getOp());
}
```

表现就是：Socket 通了、JSON 也 parse 成功，但 Agent 回 `ok:false`，或直接抛 `unknown op: callObjectMethodV`。跟参数翻译无关，纯粹是 **op 名字不一致**。

PC 发 JSON 前，把末尾的 `V` 剥掉即可：

```
private static String normalizeOp(String op) {
if (op.endsWith("V") && op.length() > 1) {
return op.substring(0, op.length() - 1);
    }
return op;
}
// callObjectMethodV  → callObjectMethod
// callBooleanMethodV → callBooleanMethod
```

这样 PC 和 Agent 只维护一套 op 分支，不用为每个 `xxxV` 再复制一份。

**第 3 步：参数翻译（最难，具体代码 AI 帮着改了几轮）**

Unidbg 里 SO 调 JNI 时，参数不是普通 Java 对象，而是一堆框架类型：`DvmObject`、`VarArg`、`VaList`、`StringObject`……PC 要把这些「翻译成 JSON 能发的形式」再发出去，手机算完还要「翻译回来」塞给 Unidbg。我主要理规则（什么发 HANDLE、什么发 MAP），具体反射和编码 AI 帮着改了几轮。

**第 4 步：分流策略 —— 为什么「全扔手机」不行**

跑通 PC 假 Agent 之后，很自然地想：**既然真机 ART 算得准，干脆所有 JNI 都发手机，PC 一个 switch 都不用写。**

试下来不行，原因是：**独立 Agent 是一个自己安装的 APK，不在目标 App 进程里。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0ordZrtXuBwnsmPGqqA9HJfZavhJzG3xmxLBsFFBAIfhvP3xyRPxUI8kJOlQ1fh9b6QaNPWArx3k4SEns84iaBXkibia1sUnuL34/640?wx_fmt=png&from=appmsg)

所以分流不能是「能发就发」，而是 **按类名前缀划边界**：

* `java/`*、`javax/`*

  → 发手机。JDK 框架类，跟哪个 App 无关，ART 算 TreeMap、String、Iterator 最靠谱。
* `android/`*、目标包名、`com/` 业务类*

  → 留 PC 补环境。要么需要 Android 上下文，要么需要目标 App 的 ClassLoader，独立 Agent 给不了。
* **`acceptMethod` / `acceptField`**

  → 永远 PC。这只是 U...