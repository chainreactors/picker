---
title: Frida 脚本运行时机与Java.perform的原理
url: https://mp.weixin.qq.com/s/tN9M2N3X43NL-PwCpnfEPw
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:28.462943
---

# Frida 脚本运行时机与Java.perform的原理

# Frida 脚本运行时机与Java.perform的原理

mb\_peeqldfc
mb\_peeqldfc

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

源码锚点：`frida-core` / `frida-gum``17.9.1`；`frida-tools``14.8.0`；`frida-java-bridge` 固定提交 `f72e61ed18fa6b72f0559df223b22a899685b22c`；AOSP `frameworks/base` 固定提交 `6e47c7075b91983ae501114425ea25e6df7690c8`；AOSP ART / libnativehelper 固定 tag `android-14.0.0_r1`

进度：已打通脚本 top-level、Android `LoadedApk`、JavaVM/JNIEnv、`Java.perform()`、ART ClassLoader 枚举与指定 `ClassFactory` Hook 的完整源码链；待补插件双 ClassLoader 真机记录

##

---

##

开课词库

词库按“脚本执行、JNI 环境、类加载命名空间”三段排列。带 ★ 的对象决定本课主时间线。

### A. 脚本从创建到执行

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3PJicgOJkm05eJrTuKIBrfongmTtViciceVIYAc8caUANbP9GDDiapl6AVzBerWQWyBcfw15wMtxy2J0zsb9xaZ0YE6a8nZjdrcHk/640?wx_fmt=png&from=appmsg)

### B. Frida 进入 Java 世界

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1r9mDahdLD13vVIIiaLaaiaXQdiaHXuy0eichInZMWIz2tF1lUia07IZQ4NHB480XbWDR2iaH8bvpvwdIWgVLrJAlOyOhKZpgn9txRE/640?wx_fmt=png&from=appmsg)

### C. Android 类加载命名空间

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2XJong4HFWIBSvF6Xr78NuCAIBEz0BfMB5UdBHTNaUNMbgIQjJMvWJicb9nsTTuSnriba4tNGp6L8a7ddXkBpJ2IytvZbqkgLno/640?wx_fmt=png&from=appmsg)

先确定本课结论

“Frida 第一个脚本运行时机”指的是用户脚本的第一行 JavaScript，不是最早进入进程的 Frida 原生代码。后者是 F01 已讲过的 zymbiote、loader 和 agent 初始化；用户 JS 要等 `Script.load()` 才执行。

对 Android 普通、无 instrumentation 的早期 spawn，主线顺序是：

```
Zygote fork / specialize
  → zymbiote 让 App 主线程停在 recv()
  → frida-server 向新进程注入完整 agent
  → client 建立 Session
  → create_script() 创建脚本实例
  → Script.load() 在 agent 的 JS 线程执行 top-level
  → Java.perform(fn) 发现默认 loader 为空，将 fn 入队
  → VM.perform 为 JS 线程取得 JNIEnv，安装 framework Hook
  → client 调用 resume()
  → zymbiote 收到 ACK，App 主线程继续
  → ActivityThread.main()
  → bindApplication
  → LoadedApk / App ClassLoader
  → Hook 设置 ClassFactory.loader
  → VM.perform 为触发 Hook 的线程取得 JNIEnv
  → 执行 Java.perform(fn) 回调
  → Application / Provider / Activity
```

这条时间线只有三个需要分别判断的边界：

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K11LFfL8FHkYbwI1QWcof4wEPXUuM6XFBT4u9G9S2gAB627CFLPIO6p2GOKj6njE1YwFT4a2fgvFq145to3ibQkvpia9QBnajgiao/640?wx_fmt=png&from=appmsg)

后文只沿这三个边界展开。

##

一次讲完 create\_script() 与 Script.load()

源码直达：client `Session.create_script()` · client `Script.load()` · agent create/load 入口 · `ScriptEngine.create_script()` · `ScriptInstance.load()` · QuickJS backend create · QuickJS load / `JS_EvalFunction()` · JS scheduler

脚本生命周期由 client 发起，由目标进程内的 agent 执行。`frida-server` 负责会话路由，不负责运行 JavaScript [1][2]。

```
client
  → frida-server
  → AgentSession
  → BaseAgentSession
  → ScriptEngine
  → QuickJS / V8
```

client 侧先创建，再加载 [1]：

```
public async Script create_script (string source,
        ScriptOptions? options = null,
        Cancellable? cancellable = null)
        throws Error, IOError {
    check_open ();

var raw_options = (options != null)
            ? options._serialize ()
            : make_parameters_dict ();

    AgentScriptId script_id;
try {
        script_id = yield active_session.create_script (
                source, raw_options, cancellable);
    } catch (GLib.Error e) {
        throw_dbus_error (e);
    }

    check_open ();

var script = new Script (this, script_id);
    scripts[script_id] = script;
return script;
}

public async void load (Cancellable? cancellable = null)
        throws Error, IOError {
    check_open ();

try {
yield session.active_session.load_script (id, cancellable);
    } catch (GLib.Error e) {
        throw_dbus_error (e);
    }
}
```

`active_session` 是远端 `AgentSession` 的代理。第一段调用返回 `script_id`，client 据此建立一个可控制的 `Script` 对象；第二段才要求 agent 加载这个实例。

agent 侧的 create 路径把源码交给 `ScriptEngine`，选择 backend，创建 `Gum.Script` 并保存实例 [2][3]：

```
Gum.ScriptBackendbackend = pick_backend (options.runtime);

Gum.Script script;
try {
if (source != null)
        script = yield backend.create (
                name, source, options.snapshot);
else
        script = yield backend.create_from_bytes (
                bytes, options.snapshot);
} catch (Gum.Error e) {
throw new Error.INVALID_ARGUMENT ("%s", e.message);
}

varinstance =new ScriptInstance (script_id, script);
instances[script_id] = instance;
```

QuickJS 的 backend create 会建立 runtime/context，并解析或编译源码 [4]：

```
script = g_object_new (GUM_QUICK_TYPE_SCRIPT,
"name", d->name,
"source", d->source,
"main-context", gum_script_task_get_context (task),
"backend", self,
    NULL);

gum_quick_script_create_context (script, &error);
```

所以语法错误可能在 create 阶段出现，但这不等于用户顶层代码已经执行。create 完成时，脚本状态仍是 `CREATED`。

load 路径从实例表取回脚本并推进状态 [3]：

```
if (state != CREATED)
throw new Error.INVALID_OPERATION (
"Script cannot be loaded in its current state");

load_request = new Promise<bool> ();
state = LOADING;

yield script.load ();

state = LOADED;
load_request.resolve (true);
```

QuickJS 不在控制请求线程上直接执行用户代码，而是把 load 任务交给 JS scheduler [5]：

```
gum_script_task_run_in_js_thread (
    task,
gum_quick_script_backend_get_scheduler (self->backend));
```

JS 线程中的 load 最终求值 entrypoint：

```
result = JS_EvalFunction (
    ctx, g_array_index (entrypoints, JSValue, i));
```

V8 对应路径使用 module `Evaluate()` 或 script `Run()`；实现函数不同，但 create 与 load 的边界相同 [6]。上游 `17.9.1` 的 scheduler 创建 `gum-js-loop` 后台线程并运行 GLib main loop [7]：

```
self->js_thread = g_thread_new (
"gum-js-loop",
    (GThreadFunc) gum_script_scheduler_run_js_loop,
self);

g_main_loop_run (self->js_loop);
```

因此这部分只需记住一条源码链：

```
create_script()
  → backend.create()
  → context + Gum.Script + script_id
  → state = CREATED

Script.load()
  → state = LOADING
  → JS scheduler
  → QuickJS JS_EvalFunction / V8 Evaluate 或 Run
  → 用户 top-level
  → state = LOADED
```

`LOADED` 只说明顶层初始化完成。`Interceptor.attach()` 可以已经安装，但它的回调仍要等目标控制流经过 Hook 点；`Java.perform()` 也可能仍在等待 App ClassLoader。

##

为什么 top-level 能早于 App 业务代码

> 源码直达：frida-tools `application.py` · `repl.py` · F01 · resume 放行

`frida -U -f TARGET_PACKAGE -l probe.js` 在工具内部不是一个不可分割的动作，而是下面的固定次序 [8]：

```
Device.spawn(TARGET_PACKAGE)
  → attach(pid)
  → Session.create_script(source)
  → 注册 message handler
  → Script.load()
  → Device.resume(pid)
```

F01 的 zymbiote 此时只阻塞 App 主线程。agent 已经拥有自己的控制线程和 JS scheduler，所以它能在 App 主线程尚未进入 `ActivityThread.main()` 时执行 top-level。

这也是 spawn 模式能提前安装 Hook 的原因：

```
App 主线程：specialize → zymbiote.recv() ─────────────→ ActivityThread.main()
                                      ↑ resume / ACK

agent 线程：attach → create → load → top-level ──────→ 等待 Hook 命中
```

`--pause` 只让 frida-tools 跳过最后的自动 `resume()`。它不暂停 agent，也不阻止 `Script.load()`：

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1oBruDlJSdsopibyFdqMiaM7GhbBoCTJajOELswweYSpPG17xJcjRicPCTgSOX6NTHoXiaGo2GGuhk2g2nS8Zs3dW8x7jAmZayGYo/640?wx_fmt=png&from=appmsg)

`send()` 和 `console.log()` 还要经过 agent 消息队列、控制通道与主机回调。终端显示时间晚于代码执行时间，适合证明阶段是否到达，不适合推断进程内的精细时间差 [9]。

##

Android App 怎样建立 LoadedApk与最终 ClassLoader

理解 `Java.perform()` 之前，必须先建立 Android 自身的装载基线：

```
ActivityThread.main()
  → attachApplication()
  → ApplicationThread.bindApplication()
  → H.BIND_APPLICATION
  → handleBindApplication()
  → getPackageInfo()
  → LoadedApk
  → LoadedApk.getClassLoader()
  → Application / Provider / Activity
```

下一节再解释 Frida 在哪个返回点接入这条链。

### 源码直达：AOSP `ActivityThread.java` · `LoadedApk.java` · `ApplicationLoaders.java` · `ContextImpl.java` · `AppComponentFactory.java`

### 3.1 从 `ActivityThread.main()` 到 `handleBindApplication()`

源码直达：AOSP `ActivityThread.main()` · `ActivityThread.attach()` · `ApplicationThread.bindApplication()` · `H.handleMessage()` · `ActivityManagerService.attachApplicationLocked()`

App 主线程进入 `ActivityThread.main()` 后准备主 Looper，并把本进程的 `ApplicationThread` Binder 对象交给 system\_server [13][18]：

```
Looper.prepareMainLooper();

ActivityThread thread = new ActivityThread();
thread.attach(false, startSeq);

if (sMainThreadHandler == null) {
    sMainThreadHandler = thread.getHandler();
}

Looper.loop();
```

`attach(false, startSeq)` 的非 system 分支调用：

```
final IActivityManagermgr = ActivityManager.getService();
mgr.attachApplication(mAppThread, startSeq);
```

system\_server 的 `attachApplicationL...