---
title: 干掉抽取壳！FART自动化脱壳框架与Execute脱壳点解析
url: https://mp.weixin.qq.com/s/88KcWCaPkBhnhFDsQ3OkuQ
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:39:50.157010
---

# 干掉抽取壳！FART自动化脱壳框架与Execute脱壳点解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hibUrj5WA1jk6gvE57tl3Kb9Ap1K3xr2rx16yxs32kJFSJicJIMgEz3Aazfr8Rsibza6fhOI50PNbQ5V3bvje2OHw/0?wx_fmt=jpeg)

# 干掉抽取壳！FART自动化脱壳框架与Execute脱壳点解析

哆啦安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于CYRUS STUDIO
，作者CYRUS STUDIO

![](http://wx.qlogo.cn/mmhead/vDwntJFbiafsE5SS4pEaaafW5WGXkRUsW2zLua98hpAX1Ok8ibsbiazq3szmce5AqXQaZAxT95UYYE/0)

**CYRUS STUDIO**
.

Android 逆向｜聚焦移动安全、攻防对抗 | 分享 Frida / Native 层分析 / 加壳脱壳 / 加密算法还原等方向内容｜欢迎关注、交流、合作

> 版权归作者所有，如有转发，请注明文章出处：https://cyrus-studio.github.io/blog/

# FART 简介

在 Android ART 环境中，市面上一些加固方案会通过“函数抽取壳”将应用的核心逻辑剥离，运行时再动态加载执行，从而增加逆向分析的难度。

FART是一种基于主动调用的自动化脱壳方案，能够在ART虚拟机的执行流程中精准捕获并还原这些被抽空的函数，实现对被加固的dex文件整体dump。

[APP逆向分析工具V4.5](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499437&idx=1&sn=d16d6e56aece786a75b2783c0ad2fd7b&scene=21#wechat_redirect)

[APK安全加固平台V5.2](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499425&idx=1&sn=f92ff3d7add367c335b2164d2408912a&scene=21#wechat_redirect)

[Unity手游无Root注入工具](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499408&idx=1&sn=5260012899e6425667e8d24a354dd9d7&scene=21#wechat_redirect)

[Android智能调试分析工具V7.5](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499445&idx=1&sn=f96192373e9e1b97cf3f3ccaa342542d&scene=21#wechat_redirect)

[frida魔改绕过检测(Android和iOS)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499371&idx=1&sn=1964a912ab735c3205b840ff83fd21e0&scene=21#wechat_redirect)

[Android开发智能调试分析软件V7.2](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499384&idx=1&sn=49938ef6b67dcde53eda6362ff57fcf7&scene=21#wechat_redirect)

[Android Apk逆向分析工具(jadx-ai-mcp)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499459&idx=1&sn=f2d28d2957373ad15deb88a321038162&scene=21#wechat_redirect)

[逆向交流群|Android智能调试工具(下载地址)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499472&idx=1&sn=0b0a5245ce898f0a53aaa6a36bdd4a6b&scene=21#wechat_redirect)

[Smali/AAR/JAR/DEX/APK逆向分析转换工具V2.5](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499404&idx=1&sn=4557961adf884684f5d71f7761fabdce&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/LtmuVIq6tF1XkEJNBa5PtmIASUG964GG582StRNDp22MIaTqibicScD8vzy1C2SJ4JDSwIlWAOIt38AicicRmvrW6w/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

Android开发智能调试分析软件V7.5

```
链接: https://pan.baidu.com/s/1cSibTh8nDMwsEvJ59Oblvg 提取码: rx32
```

使用方法

先注册、再输入密码cd\_admin\_001&2025\_001，点击登录！

* • 项目地址：https://github.com/hanbinglengyue/FART
* • 函数抽取壳的实现原理：打造基于 ART 的 Android 函数抽取壳：原理剖析与完整源码实战[1]

# FART 框架

![word/media/image1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/hibUrj5WA1jk6gvE57tl3Kb9Ap1K3xr2rO9OopfCOXnxaky2LzUef26uicw10IZeicqnRwyibeEibD7n7XxdPAyL4yA/640?wx_fmt=png&from=appmsg "null")

word/media/image1.png

FART 框架的 3 大组件：

* • 脱壳组件：将内存中的 Dex 数据完整 dump 出来
* • 主动调用组件：构造主动调用链，完成对函数粒度的主动调用并完成 CodeItem 的 dump
* • 修复组件：利用脱壳组件得到的 dex 和主动调用 dump 下来的函数体，完成函数粒度的修复

# FART 中的脱壳点

其中 FART 脱壳组件 选择 Execute 作为脱壳点，它是 Interpreter 模式执行所有 Java 方法的统一入口，能够稳定截获和提取所有解释执行的真实方法，从而达到通用脱壳的目的。

ART 下函数在运行时可能是解释执行（Interpreter 模式）或编译执行（Quick 模式）。

为何选择 Execute 作为脱壳点？这就需要先搞懂 dex2oat 编译与 ART 函数调用流程。

# dex2oat 编译流程

dex2oat 编译流程入口函数：

```
int main(int argc, char** argv) {
  int result = static_cast<int>(art::Dex2oat(argc, argv));
  // Everything was done, do an explicit exit here to avoid running Runtime destructors that take
  // time (bug 10645725) unless we're a debug or instrumented build or running on a memory tool.
  // Note: The Dex2Oat class should not destruct the runtime in this case.
  if (!art::kIsDebugBuild && !art::kIsPGOInstrumentation && !art::kRunningOnMemoryTool) {
    _exit(result);
  }
  return result;
}
```

https://cs.android.com/android/platform/superproject/+/android10-release:art/dex2oat/dex2oat.cc;l=3027

apk 安装时进行的 dex2oat 编译流程，dex2oat 的编译驱动会对函数逐个编译

![word/media/image2.png](https://mmbiz.qpic.cn/sz_mmbiz_png/hibUrj5WA1jk6gvE57tl3Kb9Ap1K3xr2ria6HCwdBZ26cwgJ9YPD7rmUFhnmibwmI6cWuuia6ic9MicamCjGOIjKlPZA/640?wx_fmt=png&from=appmsg "null")

word/media/image2.png

https://www.processon.com/i/6825c4e0c168ca282c1b9fb4?full\_name=PO\_iNeoB2

模板函数 CompileDexFile：编译 dex 文件中的所有类和方法，最后会调用 compile\_fn 进行函数粒度编译

```
// 模板函数：编译 dex 文件中的所有类和方法
template <typename CompileFn>
static void CompileDexFile(CompilerDriver* driver,
                           jobject class_loader,
                           const DexFile& dex_file,
                           const std::vector<const DexFile*>& dex_files,
                           ThreadPool* thread_pool,
                           size_t thread_count,
                           TimingLogger* timings,
                           const char* timing_name,
                           CompileFn compile_fn) {
  // 用于性能分析记录这段编译过程的时间
  TimingLogger::ScopedTiming t(timing_name, timings);

  // 创建一个用于并行编译的上下文管理器
  ParallelCompilationManager context(Runtime::Current()->GetClassLinker(),
                                     class_loader,
                                     driver,
                                     &dex_file,
                                     dex_files,
                                     thread_pool);

  // 编译单个类的回调函数
  auto compile = [&context, &compile_fn](size_t class_def_index) {
    const DexFile& dex_file = *context.GetDexFile();
    SCOPED_TRACE << "compile " << dex_file.GetLocation() << "@" << class_def_index;

    ClassLinker* class_linker = context.GetClassLinker();
    jobject jclass_loader = context.GetClassLoader();
    ClassReference ref(&dex_file, class_def_index);
    const dex::ClassDef& class_def = dex_file.GetClassDef(class_def_index);
    ClassAccessor accessor(dex_file, class_def_index);
    CompilerDriver* const driver = context.GetCompiler();

    // 跳过验证失败的类（这些类在运行时也会失败）
    if (driver->GetCompilerOptions().GetVerificationResults()->IsClassRejected(ref)) {
      return;
    }

    // 进入托管代码环境，访问 Java 对象
    ScopedObjectAccess soa(Thread::Current());
    StackHandleScope<3> hs(soa.Self());

    // 解码 class_loader 对象
    Handle<mirror::ClassLoader> class_loader(
        hs.NewHandle(soa.Decode<mirror::ClassLoader>(jclass_loader)));

    // 查找类对象
    Handle<mirror::Class> klass(
        hs.NewHandle(class_linker->FindClass(soa.Self(), accessor.GetDescriptor(), class_loader)));

    Handle<mirror::DexCache> dex_cache;
    if (klass == nullptr) {
      // 类加载失败，清除异常并使用 dex cache
      soa.Self()->AssertPendingException();
      soa.Self()->ClearException();
      dex_cache = hs.NewHandle(class_linker->FindDexCache(soa.Self(), dex_file));
    } else if (SkipClass(jclass_loader, dex_file, klass.Get())) {
      // 判断是否跳过该类（如外部类、系统类等）
      return;
    } else if (&klass->GetDexFile() != &dex_file) {
      // 重复类（已从另一个 dex 文件加载），跳过
      return;
    } else {
      dex_cache = hs.NewHandle(klass->GetDexCache());
    }

    // 没有方法的类无需编译
    if (accessor.NumDirectMethods() + accessor.NumVirtualMethods() == 0) {
      return;
    }

    // 进入 native 状态，避免阻塞 GC
    ScopedThreadSuspension sts(soa.Self(), kNative);

    // 判断是否启用 dex-to-dex 编译（可能是省略优化过程）
    optimizer::DexToDexCompiler::CompilationLevel dex_to_dex_compilation_level =
        GetDexToDexCompilationLevel(soa.Self(), *driver, jclass_loader, dex_file, class_def);

    // 编译类中所有 direct 和 virtual 方法
    int64_t previous_method_idx = -1;
    for (const ClassAccessor::Method& method : accessor.GetMethods()) {
      const uint32_t method_idx = method.GetIndex();
      if (method_idx == previous_method_idx) {
        // 处理非法 smali 文件：可能多个 method 共用同一个 method_idx（重复定义）
        continue;
      }
      previous_method_idx = method_idx;

      // 调用外部传入的 compile_fn 进行实际方法编译
      compile_fn(soa.Self(),
                 driver,
                 method.GetCodeItem(),
                 method.GetAccessFlags(),
                 method.GetInvokeType(class_def.access_flags_),
                 class_def_index,
                 method_idx,
                 class_loader,
                 dex_file,
                 dex_to_dex_compilation_...