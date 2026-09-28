---
title: OnePlus15手机本地提权Root分析
url: https://mp.weixin.qq.com/s/HU884UzDNwekvifNYXJSwQ
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:53:00.843041
---

# OnePlus15手机本地提权Root分析

# OnePlus15手机本地提权Root分析

原创

非虫
非虫

软件安全与逆向分析

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# OnePlus15手机本地提权Root分析

> 2026年9月24日，安全研究者Rasmus Moorats（nns.ee）公开了一条针对OnePlus 15的本地提权链。他在2026年4月把问题报给OnePlus，5月补齐技术细节，OnePlus确认漏洞影响旗下多款产品，同时提示公开会带来法律风险；研究者按协调披露约定延期后，仍在9月发布了完整分析。整条链里最扎眼的一点是，一台出厂状态、未解锁BL的OnePlus 15，只要装上一个不申请任何危险权限的普通APK，就能从`untrusted_app`一路拿到uid 0，最后落在持有全部Linux capability的shell里。OnePlus 15侧已在`16.0.10.500(EX01)`修复。下文只讨论已公开的机制、成因与缓解。
>
> 文章作者：非虫（fei\_cong@hotmail.com）

安卓本地Root的常见样本是GPU驱动、binder或某个vendor ioctl里的内存破坏，通常要先泄露KASLR，再构造写原语，最后劫持控制流。这条OnePlus链走的是另一条路，从头到尾没有一处内存破坏，没有堆喷，也没有靠碰运气的竞态窗口。它把OxygenOS自己的几个binder服务与vendor HAL串起来，每一环都是一处独立的设计缺陷，串在一起就把权限从App一路抬到内核级能力。这条链适合用来观察厂商定制层的IPC攻击面怎么被逐环放大。

## 漏洞概览与时间线

这条链的关键信息如表1所示。

| 字段 | 内容 |
| --- | --- |
| 目标 | OnePlus 15（CPH2747），OxygenOS 16，实测`16.0.3.503` |
| 入口 | `AtlasService.setEvent` ，binder对任意UID开放，无权限校验 |
| 类型 | 纯逻辑链，缺失调用方校验加命令注入加弱身份判断 |
| 前置条件 | 本地代码执行，一个不申请危险权限的普通APK |
| 最终权限 | uid 0，落在`u:r:vendor_qti_init_shell:s0`，持有全部Linux capability |
| CVE | 公开时未分配编号 |
| 修复 | OnePlus 15侧`16.0.10.500(EX01)` |
| 披露 | Rasmus Moorats（nns.ee），2026年9月24日公开完整分析 |

表1 OnePlus 15提权链要点

披露过程按公开资料整理如下：

1. 2026年4月18日：研究者向OnePlus提交初始报告。
2. 2026年5月14日：应厂商要求补齐技术细节。
3. 2026年5月20日：OnePlus确认漏洞，并称影响旗下多款产品，同时提示公开会带来法律责任。
4. 2026年6月1日：研究者声明将按90天窗口披露。
5. 2026年6月22日：研究者同意把公开时间推迟到9月17日。
6. 2026年9月24日：完整分析公开，此时厂商未回应最后的协调邮件，OnePlus 15侧的修复随后由`16.0.10.500(EX01)`带出。

这条时间线里有两点。第一，从4月报告到9月公开跨了五个月，属于经过完整协调披露、公开当日用户仍拿不到补丁的情况。第二，厂商确认影响面覆盖多款OnePlus与OPPO机型，但没有公开完整机型与版本清单，防守方无法据此精确排查，只能按攻击面自查。

## 威胁模型与影响面

对手模型很朴素：攻击者能在设备上运行本地代码即可。最典型的载体就是用户从非应用商店渠道侧载的一个APK，它不需要任何危险权限，不需要无障碍服务，不需要设备管理员，安装界面上看不出任何异常。也可以是别的远程漏洞先拿到某个普通App的同UID执行能力，再接上这条链完成本地提权。

这条链不依赖解锁bootloader，不改写`boot`分区，也不碰内核内存。它利用的是OxygenOS框架层与vendor层暴露给应用侧的服务接口，因此在一台完全出厂、BL锁定、能通过SafetyNet一类校验的设备上同样成立。

影响面方面，研究者在OnePlus 15（CPH2747）与OnePlus 12 Pro（CPH2581）上都验证成功，并指出这更像是OxygenOS 16的通用问题，覆盖面不限于单一机型。OnePlus在确认时也表示影响旗下多款产品。受影响机型与版本清单如表2所示，动手排查前应以厂商安全更新与实际系统版本为准。

| 设备 | 型号 | 系统线索 | 状态 |
| --- | --- | --- | --- |
| OnePlus 15 | CPH2747 | OxygenOS 16，实测`16.0.3.503` | 已确认，`16.0.10.500(EX01)`修复 |
| OnePlus 12 Pro | CPH2581 | OxygenOS 16 | 已确认 |
| 其它OnePlus/OPPO机型 | 未公开 | 多版本 | 厂商确认多款共享该攻击面，完整清单未公开 |

表2 受影响机型摘要

## 链路总览

在拆解每一环之前，先看整条链的全貌，如图1所示。流程图只描述权限与SELinux上下文的迁移，不涉及可直接运行的载荷。

![](https://mmbiz.qpic.cn/mmbiz_png/Sq4BUsrXeT9ekK8357u8IibOc54x77PMr80IoWrnLbJGFyKW7psH7mMsAbPuXhrRUdqvBJOwiaEjrjVCWRPTvS3Vqy3dSKdXhT7hPHF6Yl5Ls/640?wx_fmt=png&from=appmsg)

图1 OnePlus 15提权链流程

整条链有两次关键跳跃。第一跳把App的普通权限抬到`dumpstate`域的uid 0，靠的是一个无校验的框架服务加一处命令注入。第二跳把`dumpstate`抬到`vendor_qti_init_shell`域的满capability，靠的是一个只认uid的vendor HAL。下面逐环分析。

## 攻击面起点是AtlasService

`AtlasService`是OxygenOS里与遥测、调试相关的一个系统服务。问题出在它的`setEvent`接口：这个binder方法对调用方不做任何权限校验，任意UID的进程都能调用。研究者的原话是接口上没有对调用方的权限检查，任何UID都能调它。

这意味着一个普通App不需要声明任何权限，也不需要签名匹配，就能直接向这个系统服务投递事件。`setEvent`接受两个参数，一个是事件名字符串，一个是伴随的取值字符串。App侧调用形态大致如下，仅用于说明接口可达性。

```
// 通过反射或AIDL拿到AtlasService的binder代理后直接调用// 事件名决定走哪条内部分支，value是伴随该事件的取值atlasService.setEvent("atlas_event_multimedia_audio_dumpsys", value);
```

一个面向遥测的服务把写事件的能力开放给任意UID，单看这一点还不算致命。问题在于这个事件会被翻译成对系统属性的写入，并进一步触发一个以root运行的诊断服务，把不可信输入送进了高权限执行体。

## 事件名到处理器的分发

`AtlasService`收到事件后，交由内部的`OplusAtlasLogWriter::handleEvent`分发。这个函数通过一串硬编码的字符串比较，把不同事件名路由到不同处理路径。绝大多数事件名走的是普通的日志写入，无害。但事件名`atlas_event_multimedia_audio_dumpsys`会命中音频dump分支，进入`dumpsysAudioInfo`一类的处理逻辑。

这条分支做了两件事，把伴随取值写进一个系统属性，再请求init启动音频dump服务。

```
handleEvent(event, value)  比对event是否等于atlas_event_multimedia_audio_dumpsys  命中则:    property_set("oplus.audio.dumpinfo.type", value)   // 攻击者可控取值落地为属性    property_set("ctl.start", "audiodumpinfo")          // 请求init拉起诊断服务
```

到这一步，攻击者可控的字符串已经跨越了一次信任边界：它从一个不可信App的参数，变成了一个系统属性`oplus.audio.dumpinfo.type`的值，而这个属性马上要被一个以root运行的服务读回去使用。

## 属性取值注入到system

`ctl.start`触发后，init以uid 0启动`/system_ext/bin/audioDumpInfo`，其SELinux上下文是`u:r:dumpstate:s0`。这个二进制的职责是收集音频相关的调试信息，它会读回刚才写入的`oplus.audio.dumpinfo.type`属性，并把取值直接拼进一条shell命令交给`system()`执行，类似`system("chmod 777 " + 属性值)`，中间不做任何转义或白名单校验。

这就是一处经典的命令注入。安卓系统属性的取值长度上限是92字节，看上去短，但对注入而言足够。攻击者只要在取值里放进shell元字符，就能截断原命令、插入自己的命令、再把原命令残留部分注释掉。研究者公开的注入取值形态如下，用于说明逃逸机制。

```
x;sh</sdcard/Android/data/com.research.poc/files/boot.sh 2>&1|log -t AtlasOut;#
```

它的结构可以拆开理解：

1. 开头的`x`补上`chmod 777`的一个无害参数，让前半句合法。
2. 分号截断原命令，开始一条新命令。
3. `sh<`

   从App私有目录读入一个脚本作为标准输入交给`sh`执行，这个目录不需要任何权限即可写入。
4. `2>&1|log -t AtlasOut`

   把执行输出重定向到logcat，便于攻击者在无回显的服务里观测结果。
5. 结尾的`#`把`system()`拼接命令里跟在属性值后面的残余部分整体注释掉，保证语法完整。

执行成功后，攻击者已经在`u:r:dumpstate:s0`上下文、以uid 0拿到了任意命令执行，从App权限抬到了root，这是整条链里最难的一步。不过`dumpstate`域受SELinux策略约束，能做的事有限，只能当作下一步的跳板。

## olc2.doShell的唯一校验

拿到`dumpstate`域的root后，研究者发现了第二个可利用的vendor组件。OnePlus的vendor层暴露了一个HAL服务`vendor.oplus.hardware.olc2.IOplusLogCore/default`，它提供一个`doShell()`方法，对应binder事务码6，作用是执行一条shell命令。

这个方法服务端的唯一校验是`getCallingUid() == 0`。研究者的描述很直接：唯一的关卡就是调用方uid是不是0，只要你是uid 0，它就替你执行任意shell命令。它既没有SELinux层面的peer过滤，也没有对调用方所属域做进一步限制，任何位于允许属性内的uid 0进程都能调用。

前一环拿到的`dumpstate`恰好是uid 0，于是它可以直接调用`doShell()`。而`doShell()`执行命令的方式，是fork出`/vendor/bin/sh -c <命令>`，让子进程按`type_transition`规则落进`u:r:vendor_qti_init_shell:s0`域。这个域几乎不受约束，持有全部Linux capability，其`CapBnd`为`0x1ffffffffff`，包含`CAP_SYS_MODULE`、`CAP_SYS_RAWIO`、`CAP_SYS_PTRACE`等最危险的能力。到这里，攻击者手上的root已经不再受域策略约束，可以加载内核模块、直接读写物理内存、注入任意进程，接近无限制的执行环境。

## SELinux域与最终能力

把权限从入口到最终shell的迁移按阶段拉平，如表3所示。

| 阶段 | 执行体 | UID | SELinux域 | 关键能力 |
| --- | --- | --- | --- | --- |
| 入口 | 不可信App | App自身 | `u:r:untrusted_app:s0` | 受SELinux与seccomp严格约束，无危险权限 |
| 第一跳 | `audioDumpInfo` | 0 | `u:r:dumpstate:s0` | 可读写`/data`，但受dumpstate策略约束 |
| 第二跳 | `/vendor/bin/sh` 子进程 | 0 | `u:r:vendor_qti_init_shell:s0` | 全部capability，`CapBnd=0x1ffffffffff` |

表3 权限迁移阶段

SELinux本应在uid 0之外提供第二层约束，让拿到root的进程仍被域策略框住。`dumpstate`域做到了这一点，它虽然是uid 0，能干的事却有限。失守的环节在`vendor_qti_init_shell`域，它把一个本应只服务于厂商初始化脚本的高权限上下文，通过一个只认uid的HAL接口开放了出来，等于给任意uid 0进程留了一条绕过域约束、直达满capability的通道。命令注入负责拿到uid 0，弱身份校验的HAL负责把uid 0兑换成满capability，两者缺一不可。

## 为什么说这是一条纯逻辑链

和常见的安卓内核提权相比，这条链在工程上有几处明显区别：

1. 没有内存破坏。全程不涉及堆溢出、UAF、越界写，也就不需要泄露地址、绕过KASLR或构造ROP。
2. 结果确定。每一环都是逻辑必然，不依赖竞态窗口，不需要反复尝试，成功率接近100%。
3. 与内核版本、SoC分支、编译器画像无关。它打的是OxygenOS框架与vendor HAL的接口设计，不像栈布局型利用那样换个内核就要重新适配。
4. 每一环都是独立缺陷。`setEvent`缺权限校验、`audioDumpInfo`的命令注入、`doShell`的弱身份校验，任何一处补上都能截断整条链。

从防守角度看，这类漏洞靠内核加固、栈随机化或seccomp都挡不住，只能靠厂商在自己的服务边界上把权限校验、输入处理和调用方约束做对。

## 检测与缓解

真正的修复在厂商侧，公开分析给出的方向与OnePlus 15侧`16.0.10.500(EX01)`的修复一致，可归纳为三条：

1. 给`AtlasService.setEvent`加上调用方校验。按UID或SELinux peer限制谁能写事件，堵住整条链的入口。
2. 在`audioDumpInfo`把属性取值送进`system()`之前做转义或白名单校验，杜绝命令注入。更稳妥的做法是彻底不用`system()`拼接，改用参数化的执行接口。
3. 收紧或移除`olc2.doShell`。给它加SELinux peer过滤，只允许确有需要的域调用，或者干脆去掉这个可执行任意命令的接口。

对管理设备的一方，在厂商补丁到位之前，排查要落在攻击面上，不能等CVE。这条链没有分配CVE编号，靠编号去查会直接漏掉。可行的做法是：清点设备上是否存在`AtlasService`与olc2 HAL这两个组件及其可达性，在仍停留于`16.0.3.x`一类未修复版本的机群里，把每一个非应用商店渠道的侧载都当作潜在的root植入来对待，直到确认系统已升级到含修复的版本。厂商长期沉默不等于已修复，版本号看起来新也不等于补丁到位，要以实际系统版本与安全更新记录为准。

对普通用户，唯一可靠的动作是尽快把系统升级到OnePlus 15侧`16.0.10.500(EX01)`或更高、以及各机型对应的含修复版本，并在此之前谨慎对待来路不明的安装包。这条链的门槛极低，一个无权限的普通APK就能完成，公开之后，未修复的设备等于把root能力敞开给任意一个装进来的应用。

## 参考资料

* Rasmus Moorats（nns.ee），OnePlus 15本地提权完整分析：https://blog.nns.ee/2026/09/24/oneplus-root/
* The Hacker News，Unpatched OnePlus Flaws Let Installed Android Apps Gain Root Without Permissions：https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html
* Cybernews，OnePlus 15 root exploit lets malicious apps gain control：https://cybernews.com/security/oneplus-15-root-flaw-malicious-app-oxygenos/

已禁用此文档中的部分内容

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

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