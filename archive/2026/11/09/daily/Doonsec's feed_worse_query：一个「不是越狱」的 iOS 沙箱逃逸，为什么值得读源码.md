---
title: worse_query：一个「不是越狱」的 iOS 沙箱逃逸，为什么值得读源码
url: https://mp.weixin.qq.com/s/4eEQN3CIkRHnxAhqcIby3Q
source: Doonsec's feed
date: 2026-11-09
fetch_date: 2026-11-10T09:01:48.775140
---

# worse_query：一个「不是越狱」的 iOS 沙箱逃逸，为什么值得读源码

# worse\_query：一个「不是越狱」的 iOS 沙箱逃逸，为什么值得读源码

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0EtUvdYOgtOQNxQs4icw85ybJrSfRZAP5aue2Nia3X3rUqSX0nc3TibFAhWrF2Zib5mPqXz4WHhib4icdglvQIpGWOQw5oqsDcRmXGd8/640?wx_fmt=jpeg&from=appmsg)

## 一、先看问题：三条钉住的事实，和一处必须留着的分歧

这条链接值得写，不是因为「又一个 iOS 漏洞」，而是因为围绕它的公开信息里，同时存在一手证据、同日核查结论和作者自述，三者并不完全对齐。先把这层理清楚，后面的技术内容才有意义。

**其一，仓库真实存在，而且源码是完整的。** 我直接读取了 `github.com/forcequitOS/worse_query` 的目录与源码文件：主提交信息为 `Hello (again)`，时间 2026-11-08，仓库含 Xcode 工程、`README.md`、`LICENSE`（GPL-3.0）以及 10 个源码/资源文件。核心实现在 `worse_query.m`（6580 字节）与 `pathleak.m`（2935 字节）。README 首句是「A sandbox escape for iOS 26.0 - 26.7.2 / 27.2.」。这不是传闻，是可逐行核对的一手材料。

**其二，同日有一篇核查文说「查无此仓库」。** PBX Science 在 2026-11-08 发布《Sandbox Escape Claims Spread for iOS 27.3, but Evidence Stops at Beta 4》，其中两条结论是「搜不到 worse\_query 这个名字，只找到 bad\_query」以及「找不到 GestaltX 的公开页面」。这两条已被一手证据推翻：worse\_query 仓库在，`huamidev/GestaltX` 也在（96 stars、38 forks、8 次提交，README 明写 `Powered by worse_query`）。两者同在 11-8，更合理的解释是核查文的检索发生在仓库公开或索引收录之前；公开信息未说明确切先后，这里不做断言。

但那篇核查文真正有价值的部分没有被推翻，反而应该保留：

* 「支持 iOS 27.2 / 27.3 beta」缺少第三方独立复现，公开文档此前只到 27.0 beta 4；
* 有下游工具开发者称 iOS 27 beta 5 意外修补了逃逸；
* 沙箱逃逸不等于内核漏洞，更不等于越狱。

**其三，版本覆盖是作者自述，且与补丁时间线存在张力。** worse\_query 的 README 声称覆盖到 iOS 26.7.2 与 27.2；而 Apple 在 2026-10-27 发布的 iOS 27.2（build 24B119）/ 26.7.2 安全说明列出 160 余项修复，Calif 团队演示所用漏洞链的大部分在其中被修。不过这些修复集中在 WebKit、内核、App Intents、CoreAudio、CoreGraphics 等条目，与「容器沙箱扩展」未必是同一条代码路径。两者关系，公开信息未说明；把「27.2 打了补丁」直接等同于「这个 PoC 失效」，或反过来等同于「它绕过了补丁」，都不成立。

**几处明确留白**（不猜、不补）：

* worse\_query / bad\_query 的 **CVE 编号未见**，所有来源都未给出；
* 是否已向 Apple 提交报告、Apple 是否确认，**公开信息未说明**；
* 27.2 / 26.7.2 上是否经第三方独立复现，**未见公开记录**；
* ONE Jailbreak 提到的 SwiftUI 工具 `Worse Query Explorer`，**未找到公开仓库**；
* 本文引用了 `worse_query.h` / `pathleak.h` / `.entitlements` 的公开头文件，但**未逐行审阅 `worse_query.m` 实现体**，涉及内部机制的部分会标明是参照前代 bad\_query 的公开实现说明所作推断。

最后钉住一句定位，它决定了整篇文章的读法：README 用加粗写的是 **「This is not relevant to a jailbreak and never will be.」**——与越狱无关，将来也不会有关。任何把它写成「iOS 26/27 越狱来了」的转述，都是失实的。

---

## 二、这是什么：一个只给开发者看的沙箱逃逸 PoC

**项目**：`forcequitOS/worse_query`，作者署名 Taj C（forcequit），源码版权头显示文件创建于 2026-08-20 与 2026-09-02，仓库于 2026-11-08 公开，GPL-3.0。ONE Jailbreak 的报道称这次发布与 @0xjohnny 协作。

**形态**：一个 Xcode 工程，Swift 与 Objective-C 混编（有 `worse_query-Bridging-Header.h`），带 SwiftUI 界面（`ContentView.swift`、7631 字节）和一个把 stdout 重定向到界面的日志组件（`Console.swift`）。它不是命令行工具，也不是一键 IPA，更不是面向普通用户的成品。

README 里三句话把定位说得很死，值得原样摆出来：

> A sandbox escape for iOS 26.0 - 26.7.2 / 27.2.
> This is a proof-of-concept for developers and isn't useful by itself.
> **This is not relevant to a jailbreak and never will be.**

翻过来就是：这是给开发者用的概念验证，**单独跑起来没有实际用途**。作者甚至预判了会被误读，专门加粗了一句「别拿它跟越狱扯上关系」。这种反复澄清在安全项目里并不常见，通常说明此前同类项目已经被媒体或社群曲解过——前代 bad\_query 的确被大量包装成「不用越狱也能改系统」的玩机工具。

名字也直白：`bad_query` → `worse_query`，作者在 ONE Jailbreak 的转述里说它「是直接后继，基本上取代了前者」。不是新漏洞家族，是同一条思路在新固件上的续作。

---

## 三、从 bad\_query 到 worse\_query：变的是什么

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GEJMefL0AZzWF8YPfGiaibhuOhbTJURgiczWAR4Pp86eXW2Nm8WLFTicU7TssIcuVLhcfkYhZAqCJm1NrAvVwEgVCwrqzJZjOut6Y/640?wx_fmt=png&from=appmsg)

*图：本文依据两代仓库 README 绘制，区间为作者自述。*

前代 `bad_query` 公开于 2026-08-11，README 写的是 iOS 26.0–26.6.1 / 27.0 beta 4，与 0xjohnny、rooootdev 协作；它还留了一句「might also work on iOS 18 but I haven't tested literally at all so ymmv」——iOS 18 只是猜测，作者自己说完全没测。这句在 worse\_query 的 README 里没有再出现，公开信息未说明是否仍然成立。

两代之间的差别，可以拆成三块看：

**① 覆盖区间**

* 前代：26.0–26.6.1，加上 27.0 的开发者 beta 1–4；
* 本代：26.0–26.7.2，以及 27.2。

从「测试版」跨到「已公开发布的正式版」，是这次最显眼的变化。但要注意，两代 README 的路径清单几乎一致，变化主要在**可用固件的范围**，不在能力种类。

**② 前置条件从回退手段变成硬门槛**

* 前代在 `/var/mobile/Containers/Shared/AppGroup/*` 这一条后面标注 `(Requires App Group sacrifice on iOS 26)`——App Group 是 iOS 26 上的一种「牺牲式」回退；
* 本代 README 直接写 `To use worse_query, you'll have to set up an App Group container for your app.` ONE Jailbreak 也特意点出「这次配置不一样了」。

**③ 接口形态**

* 前代公开实现说明里的入口大致是 `bad_query(path, create, group_identifier, is_group)`；
* 本代头文件是 `worse_query(NSString *path, NSString *group, bool alt_flags, bool create_dir)`，返回 `int64_t` 句柄，并新增配对的 `worse_query_release(int64_t handle)`；另外把路径枚举独立成 `pathleak` 模块。

「申请句柄 / 释放句柄」这对接口的出现，比版本号更能说明问题：它把能力建模成了**可申请、可回收的资源**，而不是一次性的路径穿越动作。

---

## 四、跑起来要什么：App Group 是签名期的硬门槛

这一节是实操层面最容易被跳过、却最不能跳过的地方。

仓库里的 `worse_query.entitlements` 只有一项，原样如下：

```
<key>com.apple.security.application-groups</key><array>    <string>group.cc.forcequit.worse-query</string></array>
```

也就是说，这个 App Group 不是运行时填个字符串就行，它必须在**证书与描述文件（provisioning profile）签名阶段就生效**。下游 GestaltX 的 README 给了更直白的佐证：

> Signing requires a certificate and provisioning profile with at least one usable App Group. GestaltX detects the signed App Group at runtime.

翻过来：签名时至少要有一个可用的 App Group，程序在运行时去检测它。这解释了为什么 worse\_query 的函数签名里 `group` 是第二个参数——它要拿的是签名期就已被系统认可的那个组标识。

**环境上的合理推断**（部分来自前代生态的公开构建说明，非本仓库明示）：

* macOS + Xcode，iOS 26.0+ SDK，Swift/ObjC 混编工程；
* 一台版本落在 README 区间内的真机；
* 能把带 App Group entitlement 的 IPA 装到设备上的签名途径；
* 使用私有 API，因此不具备 App Store 上架可能。

**必须如实说明的一点**：这个仓库的 README **没有给构建命令、没有给运行命令、没有给参数说明，也没有给截图或演示视频**。它只有一段定位、一份可达路径清单、一句 App Group 要求和一句越狱免责。所以「怎么用」这一节无法写成步骤教程——公开信息未说明，硬编一串命令只会误导读者。这也印证了作者那句 `isn't useful by itself`：PoC 的价值在于给人读、给人接，不在于拿来即用。真正把流程封装成产品的，是第八节要讲的下游工具。

---

## 五、仓库里有什么：从十个文件读出来的接口

源码目录通过 GitHub API 取回，完整清单如下（括号内为字节数）：

```
worse_query.m6580核心实现ContentView.swift7631   SwiftUI界面pathleak.m2935路径枚举实现Console.swift                    1382stdout 重定向日志worse_query.h1134核心函数声明pathleak.h1010枚举函数声明worse_query.entitlements          307   App Group 签名声明worse_queryApp.swift              228   App 入口worse_query-Bridging-Header.h151   Swift/ObjC 桥接Assets.xcassets                    0   资源目录
```

两个公开头文件的函数声明，是这份 PoC 里信息密度更集中的部分：

```
// worse_query.h  (Created by Taj C on 8/20/26)int64_t worse_query(NSString *path, NSString *group,bool alt_flags, bool create_dir);voidworse_query_release(int64_t handle);
// pathleak.h     (Created by Taj C on 9/2/26)// 注释原文：pathleak - The dumbest arbitrary path enumeration.NSArray<NSString *> *pathleak(NSString*filter, uint64_t max_inode);
```

从签名能读出四件事：

1. `path`

   + `group` 是输入，说明能力是**按路径、绑定某个 App Group** 去申请的；
2. `alt_flags`

   是一个布尔分支，暗示存在两套标志位组合（不同固件或不同容器类型走不同路径），具体差异要读 `worse_query.m` 才能确认，本文不下结论；
3. `create_dir`

   说明它有能力在目标位置建目录，不只是读；
4. 返回 `int64_t handle` 且有配对的 `release(handle)`，是典型的「申请扩展 — 使用 — 归还」生命周期。

`pathleak` 的参数 `max_inode` 与 `filter`，加上作者自嘲的注释「最笨的任意路径枚举」，指向一种**按 inode 区间扫描来枚举目录**的土办法。这与前代生态里 Jade 项目说明的 `inode-scan fallback for hidden/denied directories` 对得上：当正常目录列举被拒绝时，退回按 inode 探测。

两个文件的创建日期（8/20、9/2）与仓库公开日（11/8）之间隔了两个多月，也说明这不是补丁发布后临时赶出来的东西。

> 边界说明：本节只引用仓库公开的**头文件声明与 entitlements**，不转载 `worse_query.m` 的实现体。接口描述用于理解机制，不构成可直接使用的利用代码。

---

## 六、它借到了什么：沙箱扩展与路径枚举

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0ECDdCRyauqE3yU5WcL3e5SnU5ypNhgdDq3kJXB7EBu1fnicoC6l2vCicxyho7bKgKLRqWHP0wviah35ECBlmBK06lEOOQDxOSodU/640?wx_fmt=png&from=appmsg)

*图：本文依据公开源码签名与 README 绘制的机制示意，非原项目配图。*

iOS 上每个第三方 App 被限制在自己的容器里，能碰的只有 `Data/Application/<UUID>` 下属于它的那一份。要访问别的容器，正常途径是系统签发 **sandbox extension（沙箱扩展）**——由 `containermanagerd` 按容器类别与权限决定给不给。bad\_query / worse\_query 这条思路的核心，就是想办法让一个普通 App 也能拿到本不该给它的扩展。

**申请—使用—归还的模型。** 从 `worse_query()` 返回句柄、`worse_query_release()` 回收句柄这一对接口看，本代把能力做成了显式的资源管理。参照前代 bad\_query 的公开实现说明（Jade 项目文档），这类扩展有几个关键性质：

* **per-path，不递归**

  ：一次扩展只覆盖指定路径，目录里的每个文件仍要各自申请；
* **可缓存、退出时释放**

  ：扩展在进程生命周期内复用，退出即失效，因此不提供重启后存活的持久化；
* **依赖私有 API**

  ：走的是 `containermanagerd` 相关的容器管理接口，不是公开 SDK。

**可达的路径**（README 原文清单）：

```
/var/containers/Data/System                        (iOS 27)/var/containers/Shared/SystemGroup/*               (iOS 27)/var/mobile/Containers/Data/Application/*/var/mobile/Containers/Data/InternalDaemon/*/var/mobile/Containers/Data/PluginKitPlugin/*/var/mobile/Containers/Shared/AppGroup/*/var/mobile/Containers/Shared/AppGroup             (iOS 27)
```

前四条覆盖 App 容器、系统守护进程容器、插件容器与 App Group 共享区；iOS 27 上额外能摸到 `/var/containers/Data/System` 与 `SystemGroup/*`——后者正是 MobileGestalt 缓存所在的系统组容器（前代生态文档把它归为容器 class 13，路径形如 `systemgroup.com.apple.mobilegestaltcache`）...