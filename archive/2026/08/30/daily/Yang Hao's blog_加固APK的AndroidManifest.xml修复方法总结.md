---
title: 加固APK的AndroidManifest.xml修复方法总结
url: https://yanghaoi.github.io/2026/08/31/jia-gu-apk-de-androidmanifest-xiu-fu-fang-fa-zong-jie/
source: Yang Hao's blog
date: 2026-08-30
fetch_date: 2026-08-31T07:53:08.891556
---

# 加固APK的AndroidManifest.xml修复方法总结

[![LOGO](https://cdn.jsdelivr.net/gh/yanghaoi/yanghaoi.github.io/medias/logo.png)
Yang Hao's blog](/)

* [首页](/)
* 文章
  + [标签](/tags)
  + [分类](/categories)
  + [归档](/archives)
* [关于](/about)
* [留言板](/contact)
* [友情链接](/friends)

![](https://cdn.jsdelivr.net/gh/yanghaoi/yanghaoi.github.io/medias/logo.png)

Yang Hao's blog

Yang Hao's blog

* [首页](/)
* 文章
  + [标签](/tags%20)
  + [分类](/categories%20)
  + [归档](/archives%20)
* [关于](/about)
* [留言板](/contact)
* [友情链接](/friends)

# 加固APK的AndroidManifest.xml修复方法总结

[Android](/tags/Android/)
[加固](/tags/%E5%8A%A0%E5%9B%BA/)
[AXML](/tags/AXML/)
[drozer](/tags/drozer/)
[aapt2](/tags/aapt2/)

[逆向分析](/categories/%E9%80%86%E5%90%91%E5%88%86%E6%9E%90/)

发布日期:
2026-08-31

更新日期:
2026-08-31

文章字数:
3.4k

阅读时长:
13 分

阅读次数:

---

# 加固APK的AndroidManifest.xml修复方法总结

分析加固后的 Android 应用时，解包得到的 `AndroidManifest.xml` 经常无法解码或显示为乱码，导致包名、组件声明等关键信息无法获取。本文以 X加密加固的银行类样本（`cn.com.x.bank`）为例，分析乱码的成因，整理三种修复方案的原理、操作方法和适用场景。

## 1. 简介

APK 内的 `AndroidManifest.xml` 本身就不是文本文件，而是 AXML（Android Binary XML）格式——Android 为安装时快速解析设计的二进制编码。所以直接解包后用编辑器打开看到”乱码”是正常现象，正常情况下解码工具可以还原。一般可以通过`jadx`工具解析APK查看`AndroidManifest.xml`配置文件：

![image-20260831095245516](/2026/08/31/jia-gu-apk-de-androidmanifest-xiu-fu-fang-fa-zong-jie/image-20260831095245516.png)

当APK（cn.com.x.bank）经过加固后，可能会混淆`AndroidManifest.xml`，这时候使用`jadx`工具查看就是乱码形式了：

![image-20260831095850691](/2026/08/31/jia-gu-apk-de-androidmanifest-xiu-fu-fang-fa-zong-jie/image-20260831095850691.png)

这种加固混淆一般是在`AndroidManifest.xml`中插入垃圾字节或非常规格式，破坏工具的解析。但是对于这种混淆的场景，有一个底层事实：**Android 系统安装时必须能解析 manifest**，厂商可以对 dex 加密、对资源混淆，但 manifest 必须保持 PackageManager 可读的形态。Android 系统必须能读懂这份 manifest，所以永远存在一条还原路径。原因是框架自带的解析器对规范外的脏数据相当宽容（跳过、忽略、按剩余有效信息继续解析），而 jadx、AXMLPrinter2 这类严格按规范实现的解析器一遇到偏差就直接报错放弃。

## 2. 方案一：aapt2 直接提取

系统必须能读懂 manifest，官方解析工具自然也能。AAPT2（Android 资源打包工具）是一种构建工具，Android Studio 和 Android Gradle 插件使用它来编译和打包应用的[资源](https://developer.android.com/guide/topics/resources/providing-resources?hl=zh-cn)。AAPT2 会解析资源、为资源编制索引，并将资源编译为针对 Android 平台进行过优化的二进制格式。AAPT2工具随 [Android SDK Build Tools](https://developer.android.com/studio/releases/build-tools?hl=zh-cn) 工具包发布：

![image-20260831142029546](/2026/08/31/jia-gu-apk-de-androidmanifest-xiu-fu-fang-fa-zong-jie/image-20260831142029546.png)

`aapt2` 对新旧格式原生兼容，工具可直接对 APK 操作（实测 build-tools 36.1.0；cmd 下使用命令 chcp 65001 切换到 UTF-8 编码再执行）：

```
# 关键摘要：包名、版本、SDK、入口 Activity、权限
aapt2 dump badging your_app.apk

# 完整 manifest 的 XML 树
aapt2 dump xmltree --file AndroidManifest.xml your_app.apk

# 老版 aapt 同样可用
aapt dump badging your_app.apk
```

如使用`aapt2 dump badging`解析加固包配置：

![image-20260831103443463](/2026/08/31/jia-gu-apk-de-androidmanifest-xiu-fu-fang-fa-zong-jie/image-20260831103443463.png)

使用`aapt2 dump xmltree --file AndroidManifest.xml your_app.apk`输出`AndroidManifest.xml`：

![image-20260831104205524](/2026/08/31/jia-gu-apk-de-androidmanifest-xiu-fu-fang-fa-zong-jie/image-20260831104205524.png)

实测包名、版本号、minSdk/targetSdk、启动 Activity、全部 `uses-permission` 可以 100% 拿到。但是输出数据是 aapt2 自定义的摘要/树形格式，**不是标准 XML 文件**，无法直接喂给需要 XML 输入的下游工具。

## 3. 方案二：drozer 运行时还原

`run app.package.manifest` 模块的思路是把 APK 装进真实设备，由 Android 框架自带的资源解析器代为解析 manifest（细节见 3.1），drozer 再输出解析结果。任何格式差异、加固混淆，只要系统能装能跑，输出的就是完整明文。

前置条件：设备上安装 drozer Agent 并启动（进入 Embedded Server），然后建立端口转发和连接 Agent（实测 drozer Console v3.1.0）：

```
adb forward tcp:31415 tcp:31415
drozer console connect
```

然后在 `drozer` 控制台中执行：

```
dz> run app.package.manifest cn.com.x.bank
```

![image-20260831143755267](/2026/08/31/jia-gu-apk-de-androidmanifest-xiu-fu-fang-fa-zong-jie/image-20260831143755267.png)

输出为完整、标准的 XML，包含全部组件声明、intent-filter、meta-data，信息完备性优于方案一。

局限：需要设备、drozer Agent 和端口转发，环境搭建成本最高；原版模块输出在控制台，只能手动复制保存；不适合批量分析。适合对少量重点样本做深度分析。

### 3.1 drozer 模块实现原理

模块源码位于 PC 端 `drozer\modules\app\package.py`（`class Manifest`），实现分两层：

**解析层**：`getAndroidManifest()`（定义在 `drozer\modules\common\assets.py`）通过反射操作设备端 Java 对象，三步拿到清单：

```
def getAndroidManifest(self, package):
    XmlAssetReader = self.loadClass("common/XmlAssetReader.apk", "XmlAssetReader")
    asset_manager = self.getAssetManager(package)
    xml = asset_manager.openXmlResourceParser("AndroidManifest.xml")
    xml_string = str(XmlAssetReader.read(xml))
    return xml_string
```

1. `createPackageContext(package).getAssets()` —— 在设备端为目标应用创建 Context，取得指向它的 AssetManager；
2. `openXmlResourceParser("AndroidManifest.xml")` —— 由 Android 框架自带的资源解析器（AssetManager / ResourceTypes 层，运行时读资源用的同一套代码）把二进制 AXML 解析成 XmlResourceParser。严格说干活的是它而不是安装阶段的 PackageParser，但效果相同：系统解析什么，我们就拿到什么；
3. `XmlAssetReader.read()` —— drozer 打包的小 Java 助手，遍历 XmlPullParser 事件流序列化回 XML 字符串。

**输出层**：字符串回传 PC 后，`__write_manifest` 给它加缩进和 `[color green]` 之类的标记，console 再渲染成终端着色——原版只能复制终端内容就是这么来的。

这里有一个容易误解的关键点：**模块的 `execute()` 是在 PC 端 console 进程里执行的**（`drozer\modules\base.py` 的 `run()` 直接本地调用 `self.execute(arguments)`），只有 Java 相关操作通过 reflector 代理到设备端。也就是说，raw XML 字符串返回时已经在 PC 的内存里了——这为直接落盘创造了条件。

### 3.2 drozer module 改造

基于上面的结论，可以在 `Manifest` 模块中增加 `-o/--output` 参数实现`AndroidManifest.xml`配置本地写入，共两处改动：

**改动一：新增 `-o` 参数，raw XML 直接写 PC 本地文件**

```
def add_arguments(self, parser):
    parser.add_argument("package", help="the identifier of the package")
    parser.add_argument("-o", "--output", default=None, metavar="PATH",
                        help="write the raw manifest to a local file on the PC, e.g. C:/1.xml")

def execute(self, arguments):
    if arguments.package == None or arguments.package == "":
        self.stderr.write("No package provided.\n")
        return
    manifest = self.getAndroidManifest(arguments.package)
    if arguments.output != None:
        self.__save_manifest(manifest, arguments.output)
    else:
        self.__write_manifest(manifest)   # 原行为不变

def __save_manifest(self, manifest, path):
    data = manifest.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    self.stdout.write("[+] manifest written to %s (%d bytes)\n" % (path, len(data)))
```

原理：`execute()` 既然跑在 PC 进程里，`open()` 写的就是本地路径——数据在模块内部就已经落盘，不经过控制台渲染，天然无横幅、无颜色标记。不带 `-o` 时行为与原版完全一致。

**改动二：顺带修复上游 bug**

`package.py:319` 有一处上游代码 `if out is not ""`，在 Python 3.8+ 会触发 `SyntaxWarning: "is not" with a literal`。`is not` 比较的是对象身份而非值，对字符串字面量应使用 `!=`，已一并修正。

**改进后的用法**——一条命令直接得到标准 XML 文件：

```
drozer console connect -c "run app.package.manifest cn.com.x.bank -o m_raw.xml"
```

实测输出 `m_raw.xml`（79241 字节）即为标准 XML，可直接用编辑器打开：

![image-20260831120941652](/2026/08/31/jia-gu-apk-de-androidmanifest-xiu-fu-fang-fa-zong-jie/image-20260831120941652.png)

![image-20260831122343609](/2026/08/31/jia-gu-apk-de-androidmanifest-xiu-fu-fang-fa-zong-jie/image-20260831122343609.png)

两点注意：

1. console 用 `shlex.split` 解析参数，会把 `\` 当转义符吃掉，Windows 路径请写 `C:/1.xml` 或 `C:\\1.xml`；
2. 模块代码每次运行由 console 下发，改动只需重启 console 生效，无需重装 Agent；但 drozer 升级会覆盖 `package.py`，常用建议把改过的 `Manifest` 类放进自己的 module repository。

改造后的完整模块文件见随文附件 `drozer_module/package.py`，直接覆盖 `site-packages/drozer/modules/app/package.py` 即可。

## 4. 方案三：AXML 字节级修复

前两种方案都是绕过文件，但如果手头只有一份损坏的 manifest（来源 APK 都不在了），或者需要离线批量处理，就得正面修文件。这就需要先理解 AXML 的格式。

### 4.1 AXML 格式结构

AXML 是线性的块（chunk）序列：

```
偏移    结构
0x00    根块 RES_XML_TYPE (type=0x0003)
        ├─ 老格式: headerSize=0x08  [type:2][headerSize:2][size:4]
        └─ 新格式: headerSize=0x0C  [type:2][headerSize:2][size:4][保留:4]
0x08*   字符串池 RES_STRING_POOL_TYPE (type=0x0001, headerSize=0x1C)
        [块头 28B][字符串偏移表 4*N][可能的对齐填充][字符串数据]
随后    资源映射块 → 命名空间 → 元素 ...
```

> \* 字符串池紧跟根块头之后：老格式在 0x08，新格式在 0x0C。

老版解码工具（以 `AXMLPrinter2.jar` 为代表）失败的原因是新版 aapt2（AGP 7+ / Android 12+ 构建链）的两处格式变化：

* **坑① 根块头从 8 字节扩为 12 字节**：多出 4 字节保留字段（通常为 `00 00 00 00`），老工具按 8 字节读头后整体错位，报 `Expected chunk of type 0x80003, read 0xc0003`；
* **坑② 字符串池新增对齐填充**：偏移表与字符串数据之间插入若干字节 0 填充（`stringsStart > 28 + 4*字符串数`），老工具不跳过填充，报 `Invalid chunk type` 之类的怪错误。

### 4.2 文件头诊断

| 文件头特征 | 状态 | 处理 |
| --- | --- | --- |
| `03 00 08 00` | 标准老格式 AXML | 直接 `java -jar AXMLPrinter2.jar` 解码 |
| `03 00 0c 00` | 新 aapt2 格式（根块头 12 字节） | 坑①②修补后解码 |
| 开头正常但大量 `EF BF BD` | 文本编码损坏 | 不可逆，回 APK 二进制重提取 |
| `50 4b 0...