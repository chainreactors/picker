---
title: 2026腾讯游戏安全竞赛决赛安卓客户端安全分析
url: https://mp.weixin.qq.com/s/Vn6k_9-eSCQskYzHwrmLhw
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:57:00.897021
---

# 2026腾讯游戏安全竞赛决赛安卓客户端安全分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3xFAuvRw9NFrzLic8HaFhtkIiagc8yGl0r4qpXCR9lAjWCRKWXsCiaEONh3eh0GQfLvIvfjGUKdaQery5jqibxxibZUotoA20akDZ4/0?wx_fmt=jpeg)

# 2026腾讯游戏安全竞赛决赛安卓客户端安全分析

mxystery
mxystery

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1**

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3vjXOTZbTers7VAteqibR4KNfQ5ibDq8MFhkkax1aatCLPv4pwlzSD39tJ665FKcgEJv7AVA42QUDqZozPpJAK95BrHt2j3SKgI/640?wx_fmt=png&from=appmsg)

**分析过程**

# 1.1 前置工作与总体判断

#### 1.1.1 初赛经验

第一，Godot 安卓题不能先押单线。初赛已经证明，只要一上来就认定“脚本一定是主线”或者“native 一定才是真核心”，后面就很容易在错误方向上投入过多时间。更稳的做法，是先把资源层、对象层、native 层都保留成候选入口，再让证据去决定谁先走。

第二，资源层可见不等于资源层可直接利用。初赛里已经反复遇到过这种情况：APK 里能看见`.gdc`、场景文件、pack 文件，但它们并不等于可直接阅读的源码，也不等于真实执行时看到的那一份逻辑。这个经验直接影响了决赛的开局判断，也就是不能因为看到了`project.binary`、`assets.sparsepck`、`token.gdc`和`Trigger/*.gdc`，就立刻把主战场押在资源恢复上。

第三，真实样本优先于完整理解。初赛里真正帮助主线快速收束的，从来不是先把所有文件都解释清楚，而是尽快拿到一组真实`token -> flag`或真实对象触发样本。因为只有样本到手之后，后面的脚本分析、native 还原、逆算法验证才有硬约束。这个经验到了决赛里依然成立，所以后面的路线才会不断强调“先撞到真块、先看到真输出、先抓到真样本”。

第四，动态窗口必须优先稳定。初赛已经说明，Godot 和 native 混合题如果动态窗口不稳定，后面的对象枚举、脚本实例化、运行时调用、VM trace 全都无从谈起。所以决赛一开始并不是先去深挖某个算法函数，而是先判断启动期和注册期的探针应该落在哪里，才能保证进程真的活着进入主场景。

也正因为有了这四条经验，决赛开局的判断顺序才会显得比较“克制”：先判断哪一层最有机会快速形成闭环，而不是看到哪一层信息多就一股脑扎进去。

#### 1.1.2 题面、APK 结构与三层主战场的最初划分

从 APK 结构上看，题目同时给出了三类非常明显的入口信号：

资源层信号：

* `project.binary`
* `assets.sparsepck`
* `token.gdc`
* `Trigger/*.gdc`
* `.gdextension`

对象层信号：

* 题面直接说明存在四种方块、车辆、左右上下载具操作
* 这意味着真实场景对象、碰撞体、Label 文本都能成为动态切入点

native 层信号：

* `libsec2026.so`
* `extension_init`
* `VMEntry`
* 多条可疑导入：`ptrace`、`dl_iterate_phdr`、`opendir/readdir/lstat`

因此最初并没有理由武断地认为“题目一定主要靠资源层”或者“题目一定主要靠 VM”。更合理的做法，是先把三层都保留成候选主线，再用证据决定谁先走。

决赛里最终形成的总体分工如下：

1. 资源层负责解决“脚本归属”和“方法名字”。
2. 对象层负责解决“怎么真实触发”和“真实样本是什么”。
3. native 层负责解决“检测机制是什么”和“最后的白盒算法怎么写”。

#### 1.1.3 启动窗口稳定与动态基线建立

本题后续所有实机样本获取、对象层验证、脚本运行时调用和 VM 取证，都建立在启动窗口可稳定利用这一前提之上。因此在进入三个 Part 的具体逆向之前，需要先交代启动期反调试链是如何被压缩到可工作的分析窗口中的。只有这一窗口稳定下来，后面的截图、日志和运行时证据才具备可重复性。

最初的教训是：不要太早把 hook 压到库内直钩上。实际对照现象非常明显：

* 只观察`libdl.so!android_dlopen_ext`和模块出生时，进程可以继续存活
* 一旦在`libsec2026.so`内部关键点过早下 inline hook，进程往往会在注册期前后直接终止

随后又通过线程级隔离实验确认：

* `thread_ptrace_fork_watch`

  可以单独旁路
* `thread_state_machine_watch`

  单独旁路不会立刻崩
* `thread_phdr_fd_watch`

  不能整体`noop`，否则会直接`Bad access`

这组实验把策略从“整条守卫线程静音”修正成了“只旁路纯反调试线程，保留兼带初始化职责的线程，只改它看到的危险输入”。这不是风格选择，而是被崩溃现象强制出来的工程结论。

后续之所以采用：

* 仅旁路`thread_ptrace_fork_watch`
* 保留`thread_phdr_fd_watch`
* 只对`strstr`的可疑模块名做 haystack 改写

本质上就是因为前面的试错已经证明：如果想继续在真机上拿样本、截屏、dump 脚本对象、trace VM，就必须优先保证这条动态基线足够稳定。

本题的总体推进顺序可以概括为下图。

![流程图 1](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2ldWYlbVaFfaSVM6XU50GdS1Sny7axZMx5rUV1mnNdhvqcF3u4BN2HUWjoEvQ2ppe6t5lkzD9nzr1v2icr9AibtvZB6NweRE7U0/640?wx_fmt=png&from=appmsg)

因重要程度，反调试/反注入和详细的入口线程、关键字符串、kill gate 具体会在第三章说明，本章节只写逆向分析过程。

稳定动态基线的关键是两步：

* 只旁路`thread_ptrace_fork_watch`，不整体删掉`thread_phdr_fd_watch`。
* 只在`libsec2026.so`发起的`strstr`比较里改写可疑模块路径，把`/memfd:frida-agent-64.so (deleted)`伪装成正常系统模块名。

对应的关键运行日志如下，已经足够说明启动期模块白名单检查被压制，而进程不会立刻在`%resume`后死亡：

```
[PTHREAD_BYPASS] thread_ptrace_fork_watch start=0x7088cba654
[PTHREAD_SEEN] thread_state_machine_watch start=0x7088cbadc4
[PTHREAD_SEEN] thread_phdr_fd_watch start=0x7088cb97d8
[STRSTR_REWRITE] caller=0x7088cbd1f0
orig_haystack=/memfd:frida-agent-64.so (deleted)
needle=libgodot_android.so
fake_haystack=/system/lib64/libgodot_android.so
```

而在继续给 libc 的`exit / abort / __assert2`加观测后，又能看到进程终止前并不会命中这些高层终止接口：

```
[*] hook exit @ 0x73fc1374f0
[*] hook abort @ 0x73fc132318
[*] hook __assert2 @ 0x73fc132b88
[*] hook android_set_abort_message @ 0x73fc1325d4
...
[STRSTR_REWRITE] caller=0x70898c31f0 orig_haystack=/memfd:frida-agent-64.so (deleted)
Process terminated
```

这组对照意味着：后续所有算法分析都不是在“裸奔环境”里进行，而是在已经穿过启动期检测窗口之后进行的。也正因为如此，后续三条主线才能分别闭环，而不是反复卡死在 attach/spawn 阶段。

### 1.2 Part1 逆向过程

`Part1`的关键并不是“先把 native VM 完全逆干净”，而是先确认绿色块到底走哪条真实生成链。这个判断在推进过程中经历过一次明显的路线修正。

最早的直觉是：题目既然显式带有`libsec2026.so`和`VMEntry`，那绿色块很可能也会落进 native VM 主线。因此最初一段时间的工作重点，确实放在了：

* 沿 GDExtension 注册链枚举类和方法。
* 观察`GameExtension.Process(PackedByteArray) -> String`这类 native 接口。
* 判断 32 位十六进制中间值是否能直接折叠成`Part1`后缀。

但随着样本积累，这个判断被证据推翻了。后续主线改到脚本层，直接原因就是`trigger2.gd`的运行时调用结果与真实样本一致。

#### 1.2.1 从场景对象和资源归属定位`trigger2.gd`

对象层先给出了第一批硬证据。我在外侧挂三类窄目标 hook：`android_dlopen_ext`用来确认`libsec2026.so`何时加载，`pthread_create`用来识别三条守卫线程并仅旁路`thread_ptrace_fork_watch`，`strstr`用来把`/memfd:frida-agent-64.so (deleted)`这类危险模块名伪装成正常系统模块路径。主线程`%resume`之后，再进入场景树枚举对象。用于稳定这个窗口的关键 Frida 代码如下：

```
const TARGET = "libsec2026.so";
let secBase = null;
function safeCString(p) {
try {
return !p || ptr(p).isNull() ? null : ptr(p).readCString();
    } catch (_e) {
return null;
    }
}

const noopThread = new NativeCallback(function () {
return ptr(0);
}, "pointer", ["pointer"]);

Interceptor.attach(Module.getExportByName("libdl.so", "android_dlopen_ext"), {
onEnter(args) {
this.path = safeCString(args[0]);
    },
onLeave() {
if (this.path && this.path.indexOf(TARGET) !== -1) {
            secBase = Process.findModuleByName(TARGET).base;
        }
    }
});

Interceptor.attach(Module.getExportByName("libc.so", "pthread_create"), {
onEnter(args) {
const start = args[2];
if (secBase && start.equals(secBase.add(0x9C654))) {
            args[2] = noopThread;
        }
    }
});

Interceptor.attach(Module.getExportByName("libc.so", "strstr"), {
onEnter(args) {
const hay = safeCString(args[0]);
const needle = safeCString(args[1]);
if (hay && needle &&
            hay.indexOf("/memfd:frida-agent-64.so") !== -1 &&
            needle.indexOf("libgodot_android.so") !== -1) {
            args[0] = Memory.allocUtf8String("/system/lib64/libgodot_android.so");
        }
    }
});
```

在这个窗口稳定之后，主场景里可以直接枚举到四个关键`Area3D`：

```
[AREA]id=43201333021 pos=-12.845476150512695,5.8220415115356445,-15.349905967712402
[AREA]id=43251664672 pos=-14.960197448730469,11.67391300201416,-3.0830507278442383
[AREA]id=43318773540 pos=-13.811505317687988,6.613474369049072,-22.492664337158203
[AREA]id=43385882408 pos=3.749691963195801,4.5928826332092285,-16.55986785888672
```

结合题面和后续实测，这四个对象分别对应：

* `43201333021：黄色示例方块。`
* `43251664672：绿色Part1方块。`
* `43318773540：红色Part2方块。`
* `43385882408：隐形Part3方块。`

这里还有一个很容易被忽略但实际非常重要的观察：绿色`Part1`方块的`y`值明显高于其他几个方块，达到`11.673913...`。这和后续实机截图中“绿色方块在屋顶附近”的画面是互相吻合的。也就是说，绿色块不是“代码上能出分但玩家一定碰不到”的伪目标，而是一个可以直接通过对象层传送验证的真实得分点。

#### 1.2.2 车辆传送与绿色块触发

`Part1`这条线的第一步动作不是先读脚本，而是先把车移动到绿色块，先确认题面的绿色目标在实机里到底会不会真正出分。场景树里只有一个可控车体，运行时对象为`VehicleBody3D id=38470157839`，初始位置约为`(7.119446, 3.489174, -16.001696)`；绿色块`Area3D id=43251664672`的位置约为`(-14.960197, 11.673913, -3.083051)`。因此对象层的第一步，就是把这辆车直接传送到绿色块上方一点，再轮询左上角`Label`和右上角`Label2`。

frida代码如下：

```
const vehicle = objectFromId("38470157839");
const greenTarget = vector3(-14.960197, 12.173913, -3.083051);

variantSet(vehicle, "global_position", greenTarget);
const curPos = variantGet(vehicle, "global_position");
```

也就是先通过`set(global_position)`把唯一车体放到绿色块附近，再立即回读位置，确认对象层传送已经生效。完成这一步后，轮询左上角`Label`和右上角`Label2`，就能直接拿到第一组绿色块真样本：

```
左上角 Label = Token:16663b2a
右上角 Label2 = flag{sec2026_PART1_879d0d6c}
```

这一步先把对象层的三个关键事实固定了下来：

* `43251664672的确是绿色Part1真得分块。`
* 右上角输出并不是离线构造出来的，而是现场撞块直接出现的真实结果。
* 后续所有脚本分析都必须回到这组现场样本上来对齐。

实机截图也对应了同一条对象层链路。下图是绿色块`Part1`命中截图，可以看到左上角是实时`Token: 4a23ab75`，右上角已经显示`flag{sec2026_PART1_203703fc}`，说明绿色块现场输出和后续恢复出来的脚本算法是一致的。

![图 1-1 Part1 绿色方块实机截图](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K35eicVRz8yKnsRpzWOCnnOIoKQBXcKJ5t6nYyN4yRV3ISIBkgeqJ1ygETWVyNjfAKDMVHAia4CYMxkJn5EQLnYrJ65pJ23NZPCI/640?wx_fmt=png&from=appmsg)![]()![]()

#### 1.2.3 资源归属与`_fe`主入口确认

在对象层拿到绿色块真样本之后，再回到资源层补脚本归属。`trigger2.gd`在运行时可以被`ResourceLoader`直接加载、实例化，并且方法列表中能稳定看到以下辅助函数：

* `_h2b`
* `_rf`
* `_xb`
* `_b2h`
* `_fe`

这一组命名已经非常关键，因为它同时覆盖了：

* `hex string -> bytes`
* 基于 key/round 的字节级处理
* 字节异或
* `bytes -> hex string`
* 最终封装函数

这说明`trigger2.gd`并不是简单触发器，而是已经带有完整的脚本级算法管线。

与之形成对照的是`token.gd`。运行时日志显示，`token.gd`的方法表只有`_mk`和`_ready`两个核心方法，并且直接调用`_mk(8)`会返回形如`52303553`这类 8 位 token。它说明`token.gd`负责的是“左上角 token 从哪里来”，而不是“右上角`Part1`怎么算”。这一步在过程里也很关键，因为它帮助我们把“token 生成脚本”和“flag 生成脚本”明确分开，避免把两条职责不同的脚本误混在一起。

确认`trig...