---
title: 不只是脱壳！这个工具尝试把 nmmp 加固后的代码重新变回 DEX
url: https://mp.weixin.qq.com/s/bCEuKz0UbUuxV5qxBNKvYA
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:17:30.155480
---

# 不只是脱壳！这个工具尝试把 nmmp 加固后的代码重新变回 DEX

# 不只是脱壳！这个工具尝试把 nmmp 加固后的代码重新变回 DEX

原创

菜狗
菜狗

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# Android 逆向又有新工具了：unmmp，尝试把 nmmp 虚拟机保护的方法还原成 DEX

做 Android 逆向，经常会碰到各种加固方案。

普通的 DEX 脱壳还好处理，真正麻烦的是虚拟机保护。原本的方法被转换成虚拟机指令，交给 Native 层解释执行。拿到 APK 之后，直接用 JADX 打开，看到的可能已经不是原来的代码逻辑了。

最近发现一个 GitHub 项目：**unmmp**，专门针对 nmmp 虚拟机加固进行还原。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Pled5HYvsFEFw0xX870QGicPncgjfF2dPeej22jwic2ZcSmHQWgx5NXwicibHyoYQbrXoibnWP1nfr2V2PkpicAgkpd2ohXToaJ2F5fowpGobTLvs/640?wx_fmt=webp&from=appmsg)

## 一、这个工具是做什么的？

简单来说，unmmp 想解决的是：**把 nmmp 虚拟机保护过的方法重新还原成 DEX 字节码。**

它使用 Unicorn 模拟执行目标 Native 虚拟机，通过分析执行过程中的寄存器变化、跳转行为以及 JNI 调用，识别虚拟机指令对应的 Dalvik 指令语义。

最后结合 DEX 中的类、方法、字段和字符串等信息，生成 Smali 方法体，再重新组装 DEX。

整个过程并不是简单地把文件解出来，而是尝试把被虚拟机保护的方法逻辑恢复出来。

## 二、主要做了哪些事情？

**1. 模拟 Native 虚拟机**

项目使用 Unicorn 模拟目标程序的执行过程，分析虚拟机运行时的指令行为。

相比单纯依赖固定 opcode 映射表，这种方式可以从目标程序自身的执行行为中获取指令信息。

**2. 分析并还原 opcode**

虚拟机指令和 Dalvik 指令并不是一一对应的，需要结合实际执行过程判断指令语义。

unmmp 会分析寄存器变化、分支跳转以及 JNI 调用，尝试恢复对应的 Dalvik 指令。

**3. 恢复 Smali 方法**

识别出指令之后，还需要处理方法引用、字段引用、类型、字符串等信息。

项目会结合 DEX 元数据生成 Smali 方法体，并替换需要还原的 native 方法。

**4. 重新生成 DEX**

完成还原后，可以进一步组装 DEX 文件，方便后续使用 JADX、Baksmali 等工具继续分析。

项目运行后会生成一些分析文件，例如：

* `classes_restored.dex`：还原后的 DEX。
* `opcode_mapping.json`：opcode 语义映射。
* `opcode_aliases.json`：需要结合上下文区分的指令变体。
* `native_methods.json`：Native 方法绑定信息。
* `lifted_bodies.json`：恢复后的 Smali 方法体。
* `recovery_summary.json`：还原过程的统计信息。

## 三、安装和使用

项目使用 Python 开发，主要依赖 Unicorn。

安装：

```
git clone https://github.com/poping520/unmmp.git

cd unmmp

python -m pip install -r requirements.txt
```

使用 APK 进行还原：

```
python unmmp.py app.apk -o out
```

指定优先使用的 ABI：

```
python unmmp.py app.apk -o out --prefer-abi armeabi-v7a
```

如果只想分析指令映射和方法体，不需要组装 DEX，可以使用：

```
python unmmp.py app.apk -o out --skip-dex
```

几个参数的作用：

* `-o`：指定输出目录。
* `--prefer-abi`：指定优先使用的 ABI。
* `--skip-dex`：跳过 DEX 组装过程。

除了直接输入 APK，也可以输入已经提取好的文件目录。不过目录中需要包含 DEX、`libnmmp.so` 和 `libnmmvm.so`。

## 四、作者提供的测试结果

项目 README 中给出了一个 Demo 测试结果：

* 测试样本：`app-release-protect.apk`
* 测试架构：ARM64、x86\_64
* 恢复方法数量：7987 个

作者表示，两个架构下均完成了 7987 个方法的恢复，并通过了相关 DEX 校验。

这个数据可以作为项目能力的参考，但不能直接理解为所有 nmmp 加固 APK 都能完整还原。实际效果还是要看加固版本、目标程序结构以及运行环境。

## 五、使用前需要注意

这个工具不是通用脱壳工具，主要针对特定的 nmmp dex2c VM 实现。

目前有几个限制：

1. 不支持任意修改过 VM 规范的版本。
2. 不支持 C++ 源码模式恢复。
3. 如果 APK 还叠加了其他加固，需要先处理其他保护层。
4. 支持重建的原始 DEX 版本包括 035、037、038、039。
5. 生成 DEX 后仍然需要结合实际运行情况验证，不能只看工具输出的恢复数量。

## 六、最后说两句

我觉得这个项目比较有意思的地方，是它没有停留在提取文件这一步，而是尝试通过模拟执行，把虚拟机中的指令重新转换成可以阅读的 Smali。

如果平时在研究 Android 加固、DEX 结构、JNI 和 Native 虚拟机，可以把这个项目拉下来看看。

尤其是想研究 dex2c VM 保护原理的，可以重点关注它的指令识别和方法恢复过程。

**项目地址：**

https://github.com/poping520/unmmp

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

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