---
title: Frida学习笔记（二十六）：DEX 脱壳实战
url: https://mp.weixin.qq.com/s/8DRlBCUFGHL6Toxp5YufgA
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:59:41.449884
---

# Frida学习笔记（二十六）：DEX 脱壳实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fJBlDTU8pLF5iaMNdkQUN0iatQS7cwSGdI0uPKvTSlS312Gf0q6QiccC6AOXz7yfib2affsO0ZkngG18sAVsuW0Goh6JEAbmFu62SQJrgR7iaqzQ/0?wx_fmt=jpeg)

# Frida学习笔记（二十六）：DEX 脱壳实战

原创

泡泡以安
泡泡以安

泡泡以安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 本篇目标：把市面上三个主流 Frida 脱壳工具——**frida-dexdump**（hluwa，4.6k★）、**frida\_dump**（lasting-yang，2k★）、**FART**（hanbinglengyue，2.7k★）——的原理、关键源码、使用边界讲透。当你用 jadx 打开一个 APK 却只看到 `StubApplication`、`ProxyApplication` 时，本篇教你按壳的代际选对工具，并能读懂工具源码、在工具失败时知道怎么改。

## 一、加固壳的本质：理解它在保护什么

### 1.1 为什么 jadx 看不到真正的代码

当 jadx 打开一个加固过的 APK，`classes.dex` 里通常只有壳的引导代码——一个 `StubApplication` 类和几段 SO 加载逻辑，App 真正的业务代码完全看不到。这是因为壳把原始 DEX 加密后藏在 APK 的某个角落（`assets/` 下的伪装文件，或嵌在壳的 SO 里），运行时由壳负责解密、回填、加载。

`classes.dex` 里的引导代码唯一职责是：在 App 启动时解密原始 DEX 并交给 ClassLoader，加载完成后把 `Application` 切换为真正的 Application。后续 App 的行为就和没加固时一致。

### 1.2 壳的工作流程

理解流程是选择正确脱壳时机的关键。

![壳的工作流程](https://mmbiz.qpic.cn/mmbiz_png/fJBlDTU8pLG2pYI5BkstGZC16hVrpJlu3s8Vhw0fMGE6UNV8sicADeq3jdHV8XgGvSxgFlPwmZdVyC5KUlGpmUA0L1h8KOPWbGtHiaFRK2VPQ/640?from=appmsg)

壳的工作流程

脱壳的核心思路就是：**在壳完成解密之后、DEX 仍然在内存中的时候，把它取出来。**

### 1.3 加固壳的代际演进

了解代际差异，可以判断脱壳的难度和该选哪个工具。

**一代壳（整体加密）**：把整个 `classes.dex` 加密存储，运行时整体解密并通过 `DexClassLoader` / `InMemoryDexClassLoader` 加载。这是最简单的方案，**内存里就有完整明文 DEX，搜 magic 就能取**。2020 年前的免费加固版本多属此类，目前仍能在维护周期长的老版本 App、内部测试构建、个别小厂方案上看到。

**二代壳（指令抽取 / 函数抽取）**：在一代壳之上，把每个方法的字节码从 DEX 里抽走单独加密，DEX 的"骨架"（类结构、方法声明）还在，但方法体被 `return-void` 或单条 `goto` 占位。运行时**每个方法在首次被调用前**才解密并把字节码回填到内存 DEX 里。这种壳，搜内存只能拿到"空壳子 DEX"，必须主动让每个方法被调用一次。**2022 年起主流加固厂商的免费版默认就是二代**。

**三代壳（VMP / 虚拟机保护）**：把方法字节码翻译成壳自定义虚拟机的指令集。即使你 dump 出 DEX，方法体里也只看到对壳自定义解释器的 `native` 跳转。分析三代壳要先逆向自定义虚拟机的解释器，复杂度极高。

**Dex2C（编译化保护）**：和三代壳并列存在的另一条路——把关键方法翻译成 C 代码编译进 SO。从 DEX 看是 `native` 跳转，但跳转目标不是自定义解释器，而是直接的 ARM 机器码。分析要走 SO 逆向（参考第 22-23 篇）。网易易盾 Pro、阿里聚安全企业版、几维安全等高端产品多采用 Dex2C。

![三代加固壳对比](https://mmbiz.qpic.cn/sz_mmbiz_png/fJBlDTU8pLFohObKczaXlyFUibUic9EztNgxTlhiaiaibMVe8W09IJA0vhzpB81XTcpwqcm7r2mqCvIqwzwZnicMtn0pd4mMvicuXW2HkKibrbfqOFo/640?from=appmsg)

三代加固壳对比

### 1.4 识别加固厂商

```
# 方法一：看 APK 里的 SO 文件
unzip -l target.apk | grep "\.so"
```

| 特征 SO 文件 | 对应厂商 |
| --- | --- |
| `libjiagu.so` / `libjgdtc.so` | 360 加固（新版本改名为 jgdtc） |
| `libshell*.so` / `libBugly.so` | 腾讯乐固 |
| `libDexHelper.so` | 梆梆加固 |
| `libexec.so` | 爱加密 |
| `libnaga.so` | 娜迦加固 |
| `libbaiduprotect.so` | 百度加固 |
| `libnesec.so` / `libsec2023.so` | 网易易盾 |

```
# 方法二：看 AndroidManifest.xml 中的 Application 类名
aapt dump badging target.apk | grep application
```

如果 Application 类名是 `com.stub.StubApp`（360）、`com.tencent.StubShell.TxAppEntry`（腾讯乐固），就能确认对应厂商。

> 上表对应 2022-2024 主流版本，新版本可能改名（如 360 把 `libjiagu` 改成 `libjgdtc`）。识别完之后查厂商官网产品页，能进一步判断是基础版（一代/二代）还是 Pro 版（三代/Dex2C）。

## 二、主流 DEX 脱壳工具横评

本篇正文精读的是三个 Frida 生态的脱壳工具（`frida-dexdump` / `frida_dump` / `FART`），因为它们的原理最能讲清楚"内存搜 magic → ART 反向定位 → CodeItem 抽取"这条完整技术演进链。但读者要知道，脱壳工具地图不止 Frida 一系——独立 App 形态的 `BlackDex` 星数比这三家都高，Xposed 时代的 `DumpDex` 至今仍是老 Android 版本首选。星数与维护状态（截至 2026-07 GitHub API）先摆全景：

**Frida 生态（本篇正文精读）**：

| 工具 | Star | 维护状态 | 安装 | 一句话定位 | 核心机制 | 主战场 |
| --- | --- | --- | --- | --- | --- | --- |
| **frida-dexdump** | 4.5k | ⚠ archived 2023-03 | `pip install frida-dexdump` | 一行命令脱一代壳的事实标杆 | 全进程内存搜 DEX magic + map\_list 校验 + 磁头修复 | 一代壳 / 整体加密类 |
| **frida\_dump** | 2.0k | ✓ 2025-08 更新 | `git clone` 后跑 .js | 从 ART 数据结构反向定位 DEX 的精确派 | hook `ClassLinker::DefineClass` / 枚举 `java.lang.DexCache` | 一代壳 / 需要精确 dump 不容误匹配的场景 |
| **FART** | 2.7k | ✓ 2025-01 更新 | AOSP 镜像或 `frida_fart_hook.js` | 二代壳唯一通用方案 | 主动 `loadClass` + hook `ClassLinker::LoadMethod` + CodeItem 重组 | 二代壳 / 方法抽取 |

**非 Frida 主流替代（本篇不精读但读者需要知道）**：

| 工具 | Star | 维护状态 | 形态 | 一句话定位 | 优势 |
| --- | --- | --- | --- | --- | --- |
| **BlackDex** | 6.4k ★ | ⚠ 2023-11 后无更新 | 独立 APK / 免 root（Android 5-10）+ root（11-13） | 一键脱壳最广受众之选 | ART native inline hook · Android 5-13 全覆盖 · 不依赖 Frida/Xposed |
| **DumpDex** | 3.2k | 停更 2020-05 | Xposed 模块 | Xposed 时代事实标准 | 对 Android 4-8 老壳无解替代 |
| **frida\_dex\_dump** | 100+ | ✓ 2026-04 更新 | Frida 脚本（FART 接力） | CYRUS-STUDIO 维护的 FART Frida 版新分支 | 补 FART 停在 Android 10 的空缺 · 详见第 9.1 节 |

**为什么正文只精读 Frida 三家**：BlackDex 是一体化 App 用户看不到源码机制，学习价值低；DumpDex 依赖 Xposed（现代 Android 上迁移到 LSPosed），本系列不覆盖 Xposed 生态；`frida_dex_dump` 属于 FART 接力方案，机制在第 5 节讲清楚 FART 后，第 9.1 节一句话交代即可。

**怎么选**：

* **快脱**：优先 BlackDex（一键 App 免脑力），或 frida-dexdump（Frida 用户）
* **精细可控**：frida\_dump 的 dexCache 方案 · 精确定位不容误匹配
* **二代壳指令抽取**：FART（AOSP 版最稳）或 CYRUS-STUDIO/frida\_dex\_dump（不刷 ROM）
* **Android 4-8 老 App**：DumpDex（唯一活着的方案）
* **三代壳 VMP / Dex2C**：DEX 层无 meaningful 内容，转 SO 逆向（第 22-23 篇）

## 三、frida-dexdump：源码精读

### 3.1 安装与一行实战

frida-dexdump 是 hluwa（看雪资深安全研究员）维护的项目，2023-03 最后一次 push 后归档不再更新，但截至 2026-07 仍是中文圈一代壳脱壳的事实标杆。**安装就一行 pip**：

```
pip3 install frida-dexdump
```

实战也是一行：

```
# spawn 模式（推荐）：自动等 5s 让壳解密，dump 完即退出
frida-dexdump -f com.target.app -d
# attach 模式：App 已经在跑了，附加上去 dump
frida-dexdump -F                       # 当前前台 App
frida-dexdump -n com.target.app        # 按包名 attach
# -d 是 deep-search，对付被故意改坏 magic 的壳
# -o ./outdir 指定输出目录，默认 ./<包名>/
```

dump 出来的文件命名是 `classes.dex` / `classes2.dex` / ...，直接用 jadx 打开就能看业务代码。

接下来按"agent 端 → 主机端"的顺序看核心源码。

### 3.2 agent/src/search.ts：DEX 搜索的核心

![frida-dexdump 内存搜索管线](https://mmbiz.qpic.cn/sz_mmbiz_png/fJBlDTU8pLFOacwHVmADhL8PpTEmC4lMB7pSdN86pnhXoW4BiaSNLpkPv7loPxTo040d0COib7HmicQl3n9Yh2SjEYkJvgYmv6lSD7Oa0YXEKU/640?from=appmsg)

frida-dexdump 内存搜索管线

整个 frida-dexdump 的精华全在这一个文件里。最关键的是它**用通配符一次性匹配所有 DEX 版本**：

```
// search.ts L115，frida-dexdump v2.0
Memory.scanSync(range.base, range.size, "64 65 78 0a 30 ?? ?? 00").forEach(...)
```

`64 65 78 0a 30 ?? ?? 00` 对应 ASCII `"dex\n0XX\0"`，第 6、7 字节用 `??` 通配——一次性命中 DEX 035 / 037 / 038 / 039 **所有正式版本**（顺带覆盖从未发布的 036 占位）。这是个关键细节：

* DEX 035：Android 1-6 默认
* DEX 037：Android 7（Nougat）+
* DEX 038：Android 8.0 +
* DEX 039：Android 9.0 +
* DEX 036：Google 从未正式发布，035 直接跳到 037

很多自造脱壳脚本只写死 `... 30 33 35 00`（035），现代 App 编译出的 DEX 多是 037/038/039，加固壳脱出来的版本号 ≥ 编译期版本，写死 035 经常会"一个 DEX 都搜不到"。Frida 的 `Memory.scanSync` 支持 `??` 通配字节，这个特性必须用上。

紧跟在 magic 搜索后面的是**双层 verify**：

```
// fast 模式：校验 string_ids_off 字段（DEX 头偏移 0x3C 处必为 0x70）
// 真正的 header_size 字段在偏移 0x24，但 header 结构固定 0x70 字节，紧接着就是
// string_ids 表，所以合法 DEX 的 string_ids_off = 0x70——用这个 0x70 常量做快速筛
if (verify(match.address, range, false)) { ... }

function verify(dexptr, range, enable_verify_maps) {
    if (dexptr.add(0x70) > range_end) return false;     // 头不能超出内存段
    if (enable_verify_maps) { /* 走 deep 路径 */ }
    else { return dexptr.add(0x3C).readUInt() === 0x70; }  // fast：string_ids 紧贴 header 尾部
}
```

fast 模式只是粗校验"是不是 DEX 头"。deep 模式会校验 **map\_list**——DEX 文件末尾有一段 map\_list 记录所有 section 的偏移和类型，其中有一项 `type=0x1000`（DEX 规范里叫 `TYPE_MAP_LIST`，代表 map\_list 自身），它的 `offset` 字段必须等于 DEX header 中的 `map_off`（偏移 0x34）。这是一个自我引用的环路，伪 DEX 几乎不可能伪造正确：

```
function verify_by_maps(dexptr, mapsptr) {
    const maps_offset = dexptr.add(0x34).readUInt();        // header.map_off
    const maps_size = mapsptr.readUInt();
    for (let i = 0; i < maps_size; i++) {
        const item_type = mapsptr.add(4 + i * 0xC).readU16();
        if (item_type === 4096) {                            // 0x1000 = DEX 自身
            const map_offset = mapsptr.add(4 + i * 0xC + 8).readUInt();
            if (maps_offset === map_offset) return true;     // 自我引用闭合 → 真 DEX
        }
    }
    return false;
}
```

接下来是**真实大小的反推**。很多壳为了对抗 dump，会故意把 DEX 头的 `file_size` 字段（偏移 0x20）改成 0 或一个错值。frida-dexdump 不信任 `file_size`，而是从 map\_list 末尾反推：

```
function get_dex_real_size(dexptr, range_base, range_end) {
    const dex_size = dexptr.add(0x20).readUInt();           // header.file_size
    const maps_address = get_maps_address(dexptr, range_base, range_end);
    if (!maps_address) return dex_size;                     // 拿不到 maps 就退回 file_size
    const maps_end = get_maps_end(maps_address, range_base, range_end);
    if (!maps_end) return dex_size;
    return maps_end.sub(dexptr).toInt32();                  // map_list 末尾 - DEX 起点 = 真实大小
}
```

最后是 **deep\_search 模式的反向搜索**。如果壳把 DEX magic 也抹...